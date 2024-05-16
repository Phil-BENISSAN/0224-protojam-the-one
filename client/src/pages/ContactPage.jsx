function ContactForm() {
  const [formData, setFormData] = useState({
    lastname: "",
    firstname: "",
    email: "",
    message: "",
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const messageToSend = `Name: ${formData.firstname} ${formData.lastname}\nEmail: ${formData.email}\nMessage: ${formData.message}`;
const channelId ="C06JRQQT5FH"
    try {
      const response = await client.chat.postMessage, ({
        method: 'POST',
        channel:channelId
        text:"hello world"
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: messageToSend }),
      });
      
      if (response.ok) {
        alert('Message envoyé avec succès à Slack !');
      } else {
        throw new Error('Erreur lors de l\'envoi du message à Slack');
      }
    } catch (error) {
      console.error('Erreur lors de l\'envoi du message à Slack :', error);
      alert('Une erreur s\'est produite lors de l\'envoi du message à Slack.');
    }

    // Réinitialiser le formulaire
    setFormData({
      lastname: "",
      firstname: "",
      email: "",
      message: "",
    });
  };

  return (
    <>
      <img src="./src/assets/images/logo.svg" alt="Logo Cocktail Club" />
      <section className="contact-form-container">
        <h2>Contact us</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="lastname">Last Name:</label>
            <input
              type="text"
              id="lastname"
              name="lastname"
              value={formData.lastname}
              onChange={handleChange}
              placeholder="Enter your lastname"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="firstname">First Name:</label>
            <input
              type="text"
              id="firstname"
              name="firstname"
              value={formData.firstname}
              onChange={handleChange}
              placeholder="Enter your firstname"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email:</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Enter your email"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="message">Message:</label>
            <textarea
              id="message"
              name="message"
              value={formData.message}
              onChange={handleChange}
              placeholder="Enter your message"
              required
            />
          </div>
          <button className="formButton" type="submit">
            Submit
          </button>
        </form>
      </section>
    </>
  );
}

export default ContactForm;