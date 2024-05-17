import "./AnalysePage.css";

function AnalysePage() {
  return (<>
    <h2 className="analyseTitle">Analyse</h2>
    <div className="analyseImageContainer">
      <img
        className="tempsEcran"
        src="/src/assets/temps_écrans.PNG"
        alt="Temps écran"
      />
      <img
        className="tempsEcran"
        src="/src/assets/temps_depense_sans_pratique.png"
        alt="Temps dépensé sans pratique"
      />
      <img
        className="tempsEcran"
        src="/src/assets/temps_depense_avec_pratique.png"
        alt="Temps dépensé avec pratique"
      />
      <img
        className="tempsEcran"
        src="/src/assets/temps_entrainement_sans.png"
        alt="Temps entrainement sans pratique"
      />
      <img
        className="tempsEcran"
        src="/src/assets/temps_entrainement_avec.png"
        alt="Temps entrainement avec pratique"
      />
    </div>
    </>
  );
}

export default AnalysePage;
