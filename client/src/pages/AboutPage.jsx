import './AboutPage.css';

const teamMembers = [
  { id: 1, name: 'Kévin', role: 'Développeur Front-end' },
  { id: 2, name: 'Paul', role: 'Développeur Front-end' },
  { id: 3, name: 'PJ', role: 'Développeur Front-end' },
  { id: 4, name: 'Samia', role: 'Développeur Back-end' },
  { id: 5, name: 'Mathile', role: 'Développeur Back-end' },
  { id: 6, name: 'Jimmy', role: 'Développeur Back-end' },
];

const AboutPage = () => {
  return (
    <div className="about-container">
      <h1 className='titleMembers'>À propos de notre équipe</h1>
      <p>Nous sommes une équipe dynamique et passionnée composée de six développeurs spécialisés dans le développement front-end et back-end.</p>
      <div className="team">
        {teamMembers.map((member) => (
          <div key={member.id} className="team-member">
            <h2>{member.name}</h2>
            <p>{member.role}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AboutPage;
