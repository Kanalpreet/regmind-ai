import React, { useState } from 'react';
import Sidebar from '../components/Sidebar';

const MainLayout = ({ children }) => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <div className="app-container">
      {/* Mobile Header */}
      <header className="mobile-header">
        <div className="mobile-logo">
          <div className="logo-icon-sm">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
              <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
            </svg>
          </div>
          <span>RegMind AI</span>
        </div>
        <button className="mobile-toggle" onClick={toggleSidebar} aria-label="Toggle Menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            {isSidebarOpen ? (
              <path d="M18 6L6 18M6 6l12 12" />
            ) : (
              <path d="M3 12h18M3 6h18M3 18h18" />
            )}
          </svg>
        </button>
      </header>

      {/* Sidebar with mobile state */}
      <div className={`sidebar-wrapper ${isSidebarOpen ? 'mobile-open' : ''}`}>
        <div className="sidebar-overlay" onClick={toggleSidebar}></div>
        <Sidebar />
      </div>

      <main className="main-content">
        {children}
      </main>

      <style dangerouslySetInnerHTML={{ __html: `
        .mobile-header {
          display: none;
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          height: 64px;
          background: rgba(2, 6, 23, 0.8);
          backdrop-filter: blur(12px);
          z-index: 1100;
          padding: 0 var(--space-md);
          align-items: center;
          justify-content: space-between;
          border-bottom: 1px solid var(--glass-border);
        }

        .mobile-logo {
          display: flex;
          align-items: center;
          gap: var(--space-xs);
          font-weight: 700;
          color: white;
        }

        .logo-icon-sm {
          width: 24px;
          height: 24px;
          background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
          border-radius: 6px;
          padding: 4px;
          color: white;
        }

        .mobile-toggle {
          background: none;
          border: none;
          color: white;
          width: 40px;
          height: 40px;
          display: flex;
          align-items: center;
          justify-content: center;
          cursor: pointer;
        }

        .mobile-toggle svg {
          width: 24px;
          height: 24px;
        }

        @media (max-width: 1024px) {
          .mobile-header {
            display: flex;
          }
          
          .main-content {
            padding-top: calc(64px + var(--space-lg));
          }

          .sidebar-wrapper {
            position: fixed;
            inset: 0;
            z-index: 1200;
            visibility: hidden;
            pointer-events: none;
            transition: visibility var(--transition-normal);
          }

          .sidebar-wrapper.mobile-open {
            visibility: visible;
            pointer-events: auto;
          }

          .sidebar-overlay {
            position: absolute;
            inset: 0;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(4px);
            opacity: 0;
            transition: opacity var(--transition-normal);
          }

          .sidebar-wrapper.mobile-open .sidebar-overlay {
            opacity: 1;
          }

          .sidebar-wrapper .sidebar {
            transform: translateX(-100%);
            transition: transform var(--transition-normal);
          }

          .sidebar-wrapper.mobile-open .sidebar {
            transform: translateX(0);
          }
        }
      ` }} />
    </div>
  );
};

export default MainLayout;
