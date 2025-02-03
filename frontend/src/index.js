// // // import React from 'react';
// // // import ReactDOM from 'react-dom';
// // // import './index.css';  // Import your styles here
// // // import App from './App';  // Import your main App component
// // // import reportWebVitals from './reportWebVitals';  // Optional, for performance metrics

// // // // This is the correct way to render your app to the DOM
// // // ReactDOM.render(
// // //   <React.StrictMode>
// // //     <App />
// // //   </React.StrictMode>,
// // //   document.getElementById('root')  // Make sure your HTML has this element
// // // );

// // // // Optional: report web vitals
// // // reportWebVitals();


// // import React from "react";
// // import ReactDOM from "react-dom/client"; // <-- Import from "react-dom/client"
// // import App from "./App";
// // import { BrowserRouter } from "react-router-dom";
// // import "./styles/index.css";

// // const root = ReactDOM.createRoot(document.getElementById("root")); // <-- Use createRoot
// // root.render(
// //   <React.StrictMode>
// //     <BrowserRouter>
// //       <App />
// //     </BrowserRouter>
// //   </React.StrictMode>
// // );


// import React from "react";
// import ReactDOM from "react-dom/client";
// import { BrowserRouter } from "react-router-dom";
// import App from "./App";
// import "./styles/index.css";

// const root = ReactDOM.createRoot(document.getElementById("root"));
// root.render(
//   <React.StrictMode>
//     <BrowserRouter> {/* ✅ Router should be only here */}
//       <App />
//     </BrowserRouter>
//   </React.StrictMode>
// );

import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom"; // Correct import
import App from "./App";

import './styles/index.css';

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <BrowserRouter>  {/* Only one Router */}
    <App />
  </BrowserRouter>
);
