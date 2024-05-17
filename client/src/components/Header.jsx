import './Header.css';
import { Link } from 'react-router-dom';

const Header = () => {
  const menuOnClick = () => {
    document.getElementById("menu-bar").classList.toggle("change");
    document.getElementById("nav").classList.toggle("change");
    document.getElementById("menu-bg").classList.toggle("change-bg");
  };

  const closeMenu = () => {
    document.getElementById("menu-bar").classList.remove("change");
    document.getElementById("nav").classList.remove("change");
    document.getElementById("menu-bg").classList.remove("change-bg");
  };

  return (
    <>
      <header className='header'>
        <div id="menu">
          <div id="menu-bar" onClick={menuOnClick}>
            <div id="bar1" className="bar"></div>
            <div id="bar2" className="bar"></div>
            <div id="bar3" className="bar"></div>
          </div>
          <nav className="nav" id="nav">
            <ul>
              <li><Link to="/" onClick={closeMenu}>Home</Link></li>
              <li><Link to="/About" onClick={closeMenu}>About</Link></li>
              <li><Link to="/Contact" onClick={closeMenu}>Contact</Link></li>
              <li><a href="#" onClick={closeMenu}>Blog</a></li>
            </ul>
          </nav>
        </div>
        <div className="menu-bg" id="menu-bg"></div>
        <div className='logoContainer'>
          <h1 className='title'>Yoga challenge</h1>
          <img src="src\assets\Logo_Yoga.png" alt="return to homepage" className='Logo_yoga'/>
        </div>
      </header>
    </>
  );
};

export default Header;