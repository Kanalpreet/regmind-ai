import React from "react";
import {
  BrowserRouter,
  Routes,
  Route,
  useLocation,
} from "react-router-dom";

import Home from "./pages/Home";
import AskAI from "./pages/AskAI";
import ConflictDetection from "./pages/ConflictDetection";

import MainLayout from "./layouts/MainLayout";

function AppRoutes() {
  const location = useLocation();

  const isHome = location.pathname === "/";

  if (isHome) {
    return (
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    );
  }

  return (
    <MainLayout>
      <Routes>
        <Route path="/ask-ai" element={<AskAI />} />
        <Route
          path="/conflict-detection"
          element={<ConflictDetection />}
        />
      </Routes>
    </MainLayout>
  );
}

function App() {
  return (
    <BrowserRouter>
      <AppRoutes />
    </BrowserRouter>
  );
}

export default App;