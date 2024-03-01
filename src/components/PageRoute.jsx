import {Routes, Route} from "react-router-dom";

import Navbar from "./Navbar.jsx";
import Home from "../pages/Home";

const PageRoute = () =>{
    <Routes>
      <Route path='/' element={<Home />} />
    </Routes>
}


export default PageRoute;