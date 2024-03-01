import {Link, Outlet} from "react-router-dom";

const Navbar = () => {
    return(
        <>
        <header className="header">
        <nav className="nav container">
          <div className="nav__data">
          <Link to="/" className="nav__logo"><img src="assets/putih.svg" /></Link>
            <div className="nav__toggle" id="nav-toggle">
              <i className="ri-menu-line nav__burger"></i>
              <i className="ri-close-line nav__close"></i>
            </div>
          </div>
          <div className="nav__menu" id="nav-menu">
            <ul className="nav__list">
              <li>
                <a href="./index.html" className="nav__link" translate="no">Home</a>
              </li>
              <li className="dropdown__item">
                <div className="nav__link">Triangle</div>
                <ul className="dropdown__menu">
                  <li>
                    <a
                      href="./triangle/basic/B_triangle.html"
                      className="nav__link--dropdown"
                      >Basic</a>
                  </li>
                  <li>
                    <a
                      href="./triangle/advance/A_triangle.html"
                      className="nav__link--dropdown"
                      translate="no"
                      >Advance</a>
                  </li>
                </ul>
              </li>
              <li className="dropdown__item">
                <div className="nav__link">Tetrahedron</div>
                <ul className="dropdown__menu">
                  <li>
                    <a
                      href="./tetrahedron/square/square.html"
                      className="nav__link--dropdown"
                      >Square</a>
                  </li>
                  <li>
                    <a
                      href="./tetrahedron/rectangle/rectangle.html"
                      className="nav__link--dropdown"
                      >Rectangle</a>
                  </li>
                  <li>
                    <a
                      href="./polygon/triangle/triangle.html"
                      className="nav__link--dropdown"
                      >Rhombus</a>
                  </li>
                  <li>
                    <a
                      href="./polygon/triangle/triangle.html"
                      className="nav__link--dropdown"
                      >Kite</a>
                  </li>
                  <li>
                    <a
                      href="./tetrahedron/trapezoid/trapezoid.html"
                      className="nav__link--dropdown"
                      >Trapezoid</a>
                  </li>
                  <li>
                    <a
                      href="./polygon/triangle/triangle.html"
                      className="nav__link--dropdown"
                      >Parallelogram</a>
                  </li>
                </ul>
              </li>
              <li className="dropdown__item">
                <div className="nav__link">Polygon</div>
                <ul className="dropdown__menu">
                  <li className="dropdown__subitem">
                    <div className="dropdown__link">Quadrilaterals</div>
                    <ul className="dropdown__submenu">
                      <li>
                        <a
                          href="./polygon/quadrilateral/parallelogram/square/square.html"
                          className="dropdown__sublink"
                          >Square</a>
                      </li>
                    </ul>
                  </li>
                  <li>
                    <a
                      href="./polygon/triangle/triangle.html"
                      className="nav__link--dropdown"
                      >Other</a>
                  </li>
                </ul>
              </li>
              <li className="dropdown__item">
                <div className="nav__link">Circle</div>
                <ul className="dropdown__menu">
                  <li>
                    <a
                      href="./circle/basic/B_circle.html"
                      className="nav__link--dropdown"
                      >Basic</a>
                  </li>
                  <li>
                    <a
                      href="./circle/advance/A_circle.html"
                      className="nav__link--dropdown"
                      translate="no"
                      >Advance</a>
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </nav>
      </header>
      <Outlet/>
    </>
    );
}

export default Navbar;