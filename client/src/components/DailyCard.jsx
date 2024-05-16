// import PropTypes from "prop-types";
import "../pages/DailyCard.css";
// import {
//   MapContainer,
//   TileLayer,
//   Marker,Popup
// } from 'https://cdn.esm.sh/react-leaflet'

function DailyCard() {
  return (
    <div className="container">
      <div className="card">
        <div className="card__content"></div>
        <article className="positionCard">
          <h2 className="positionTitle">Position</h2>
          <img
            className="positionImg"
            src="https://img.freepik.com/photos-gratuite/full-shot-woman-doing-yoga-pose-exterieur_23-2149123080.jpg?w=900&t=st=1715861423~exp=1715862023~hmac=82b3c3d62e2bc037f2eb86f33a21b06f646a157f96a88ff95067a3fd39d57300"
            alt="a yoga position"
          />
          <p className="positionTxt">
            From a seated position the feet are lifted up so that the thighs are
            angled about 45-50 degrees relative to the earth. The tailbone is
            lengthened into the earth and the pubis pulls toward the navel. The
            shoulder blades are spread across the back and the hands reach
            around the back of the calves, with legs pulled towards the body.
            The chin is tipped slightly toward the sternum so that the base of
            the skull lifts lightly away from the back of the neck. Gaze is
            forward.
          </p>
       
          {/* <MapContainer
            center={[51.505, -0.09]}
            zoom={13}
            scrollWheelZoom={false}
          >
            <TileLayer
              attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Marker position={[51.505, -0.09]}>
              <Popup>
                A pretty CSS3 popup. <br /> Easily customizable.
              </Popup>
            </Marker>
          </MapContainer> */}
          
        </article>
      </div>
    </div>
  );
}

// CocktailCard.propTypes = {
//   drink: PropTypes.shape({
//     position: PropTypes.string.isRequired,
//     positionImg: PropTypes.string.isRequired,
//     positionTxt: PropTypes.string.isRequired,
//   }).isRequired,
// };

export default DailyCard;
