import { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, Circle } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import axios from 'axios';

// Fix marker icon issue
delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon-2x.png',
  iconUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-icon.png',
  shadowUrl: 'https://unpkg.com/leaflet@1.7.1/dist/images/marker-shadow.png',
});

const MapComponent = () => {
  const [position, setPosition] = useState([44.8694507, -0.565266]);
  const [parks, setParks] = useState([]);
  const [zoom, setZoom] = useState(13);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition((position) => {
      const { latitude, longitude } = position.coords;
      setPosition([latitude, longitude]);
      fetchParks(latitude, longitude);
    });
  }, []);

  const fetchParks = async (lat, lon) => {
    const query = `
      [out:json];
      node
        [leisure=park]
        (around:10000, ${lat}, ${lon});
      out body;
    `;
    const url = `https://overpass-api.de/api/interpreter?data=${encodeURIComponent(query)}`;
    try {
      const response = await axios.get(url);
      const parksData = response.data.elements.map((element) => ({
        id: element.id,
        lat: element.lat,
        lon: element.lon,
        name: element.tags.name,
      }));
      setParks(parksData);
    } catch (error) {
      console.error("Erreur lors de la récupération des parcs:", error);
    }
  };

  return (
    <MapContainer center={position} zoom={zoom} style={{ height: "100vh", width: "100%" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      <Marker position={position}>
        <Popup>Vous êtes ici !</Popup>
      </Marker>
      {parks.map((park) => (
        <Marker key={park.id} position={[park.lat, park.lon]}>
          <Popup>{park.name || "Parc sans nom"}</Popup>
        </Marker>
      ))}
      <Circle
        center={position}
        radius={10000} // Rayon de 10 km
        pathOptions={{ color: 'blue', fillColor: 'blue', fillOpacity: 0.1 }}
      />
    </MapContainer>
  );
};

export default MapComponent;
