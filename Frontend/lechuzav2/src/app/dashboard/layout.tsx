import React from "react";
import Sidebar from "./components/sidebar";

export default function DashboardLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <div className="flex h-screen bg-gray-100 overflow-hidden">
      {/* Sidebar */}
      <Sidebar className="flex-shrink-0" />

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto">
        <div className="min-h-full bg-gradient-to-br from-gray-50 to-gray-100">
          {children}
        </div>
      </main>
    </div>
  );
}