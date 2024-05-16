import HomeCard from "../components/HomeCard";
import { Link, useLoaderData } from "react-router-dom";
import "./Home.css";

function Home() {
  const postureData = useLoaderData();

  return (
    <>
      <div className="homeCardContainer">
        <ul className="posture-list" id="posture-list">
          {postureData &&
            postureData.map((posture) => (
              <li className="postureCard" key={posture.id}>
                <Link to={`/${posture.id}`}>
                  <HomeCard data={posture} />
                </Link>
              </li>
            ))}
        </ul>
      </div>
    </>
  );
}

export default Home;
