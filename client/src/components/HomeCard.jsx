import "./HomeCard.css";
import PropTypes from "prop-types";

function HomeCard({ data }) {
  return (
    <div className="card-container">
      <div className="card">
        <div className="img-content">
          <img src={data.image} alt="posture" />
        </div>
        <div className="content">
          <h2 className="heading">Jour {data.id} 🎋</h2>
          <h3 className="postureName">{data.nom}</h3>
        </div>
      </div>
    </div>
  );
}

HomeCard.propTypes = {
  data: PropTypes.shape({
    image: PropTypes.string.isRequired,
    nom: PropTypes.string.isRequired,
    id: PropTypes.number.isRequired,
  }),
};

export default HomeCard;
