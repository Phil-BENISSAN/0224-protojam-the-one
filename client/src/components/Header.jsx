import React from 'react';
import './Header.css'; 

const Header = () => {
  const menuOnClick = () => {
    document.getElementById("menu-bar").classList.toggle("change");
    document.getElementById("nav").classList.toggle("change");
    document.getElementById("menu-bg").classList.toggle("change-bg");
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
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
            <li><a href="#">Blog</a></li>
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