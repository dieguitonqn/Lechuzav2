"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { Menu, X, LogOut } from "lucide-react";
import { getSession, signOut } from "next-auth/react";
import { sign } from "crypto";


const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [isAdmin, setIsAdmin] = useState(false);

  useEffect(() => {
    const fetchSession = async () => {
      const session = await getSession();
      if (session?.user?.role === "admin") {
        setIsAdmin(true);
      }
    };
    fetchSession();
  }, []);

  const menuItems = [
    { name: "Dashboard", href: "/dashboard", adminOnly: true },
    { name: "Ingresar Documentación", href: "/main/documentos" },
    { name: "Corregir Documentación", href: "/main/informes" },
    { name: "CAOs", href: "/caos" },
  ];

  return (
    <nav className="bg-white shadow-lg border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <div className="flex items-center">
            <Link href="/" className="flex items-center">
              <div className="text-2xl font-bold text-red-600">
                Lechuza V2.0
              </div>
            </Link>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:block">
            <div className="ml-10 flex items-baseline space-x-4">
              {menuItems.map((item) => (
                isAdmin || !item.adminOnly ? (
                <Link
                  key={item.name}
                  href={item.href}
                  className="text-gray-700 hover:text-blue-600 hover:bg-blue-50 px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200"
                >
                  {item.name}
                </Link>
              ) : null))}
              <button
                onClick={() => {
                  signOut({ callbackUrl: "/auth/signin" });
                }}
                className="ml-4 bg-gradient-to-r from-red-600 to-pink-600 text-white px-3 py-2 rounded-md text-sm font-medium hover:from-red-700 hover:to-pink-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 transition-all duration-200 flex items-center gap-2"
              >
                <LogOut size={16} />
                Cerrar Sesión
              </button>
            </div>
            <div>
              
            </div>
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden">
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="text-gray-700 hover:text-blue-600 focus:outline-none focus:text-blue-600 p-2"
            >
              {isOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-gray-50 border-t border-gray-200">
            {menuItems.map((item) => (
              <Link
                key={item.name}
                href={item.href}
                className="text-gray-700 hover:text-blue-600 hover:bg-white block px-3 py-2 rounded-md text-base font-medium transition-colors duration-200"
                onClick={() => setIsOpen(false)}
              >
                {item.name}
              </Link>
            ))}
            <button
              onClick={() => {
                signOut({ callbackUrl: "/auth/signin" });
                setIsOpen(false);
              }}
              className="w-full text-left bg-gradient-to-r from-red-600 to-pink-600 text-white px-3 py-2 rounded-md text-base font-medium hover:from-red-700 hover:to-pink-700 transition-all duration-200 flex items-center gap-2 mt-2"
            >
              Cerrar Sesión
              <LogOut size={16} />
            </button>
          </div>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
