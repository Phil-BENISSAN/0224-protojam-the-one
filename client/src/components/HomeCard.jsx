import "./HomeCard.css";

function HomeCard({data}) {
  return (
    <div className="card-container">
      <div className="card">
        <div className="img-content">
            <img src={data.image}alt="" />
        </div>
        <div className="content">
          <h2 className="heading">Jour {data.id}</h2>
          <h3>{data.nom}</h3>
        </div>
      </div>
    </div>
  );
}

export default HomeCard;
