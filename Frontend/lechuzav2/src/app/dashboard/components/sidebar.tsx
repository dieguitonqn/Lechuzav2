"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  LayoutDashboard,
  Users,
  Building2,
  FolderKanban,
  FileText,
  Settings,
  LogOut,
  ChevronLeft,
  ChevronRight,
} from "lucide-react";
import { useState } from "react";
import { signOut } from "next-auth/react";
import Image from "next/image";

interface SidebarProps {
  className?: string;
}

export default function Sidebar({ className = "" }: SidebarProps) {
  const pathname = usePathname();
  const [isCollapsed, setIsCollapsed] = useState(false);

  const menuItems = [
    {
      title: "Dashboard",
      href: "/dashboard",
      icon: LayoutDashboard,
      description: "Vista general",
    },
    {
      title: "Usuarios",
      href: "/dashboard/users",
      icon: Users,
      description: "Gestión de usuarios",
    },
    {
      title: "Empresas",
      href: "/dashboard/companies",
      icon: Building2,
      description: "Gestión de empresas",
    },
    {
      title: "Proyectos",
      href: "/dashboard/projects",
      icon: FolderKanban,
      description: "Gestión de proyectos",
    },
    {
      title: "Documentos",
      href: "/dashboard/documents",
      icon: FileText,
      description: "Gestión documental",
    },
    {
      title: "Configuración",
      href: "/dashboard/settings",
      icon: Settings,
      description: "Ajustes del sistema",
    },
  ];

  const handleLogout = async () => {
    await signOut({ callbackUrl: "/auth/signin" });
  };

  return (
    <aside
      className={`${className} ${
        isCollapsed ? "w-20" : "w-64"
      } bg-gradient-to-b from-slate-900 to-slate-800 text-white transition-all duration-300 flex flex-col relative`}
    >
      {/* Header */}
      <div className="p-6 border-b border-slate-700">
        <div className="flex items-center justify-between">
          {!isCollapsed && (
            <Link href="/main" className="flex items-center space-x-3">
              <Image
                src="/lechu_logo_new.jpg"
                alt="Lechuza Logo"
                width={40}
                height={40}
                className="rounded-lg"
              />
              <div>
                <h2 className="text-xl font-bold text-white">Lechuza</h2>
                <p className="text-xs text-slate-400">Admin Dashboard</p>
              </div>
            </Link>
          )}
          {isCollapsed && (
            <Image
              src="/lechu_logo_new.jpg"
              alt="Lechuza Logo"
              width={40}
              height={40}
              className="rounded-lg mx-auto"
            />
          )}
        </div>
      </div>

      {/* Toggle Button */}
      <button
        onClick={() => setIsCollapsed(!isCollapsed)}
        className="absolute -right-3 top-20 bg-slate-700 hover:bg-slate-600 text-white rounded-full p-1.5 shadow-lg transition-all duration-200 z-10"
        title={isCollapsed ? "Expandir" : "Colapsar"}
      >
        {isCollapsed ? (
          <ChevronRight className="w-4 h-4" />
        ) : (
          <ChevronLeft className="w-4 h-4" />
        )}
      </button>

      {/* Navigation */}
      <nav className="flex-1 p-4 space-y-2 overflow-y-auto">
        {menuItems.map((item) => {
          const isActive = pathname === item.href;
          const Icon = item.icon;

          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex items-center ${
                isCollapsed ? "justify-center" : "space-x-3"
              } px-4 py-3 rounded-lg transition-all duration-200 group ${
                isActive
                  ? "bg-red-600 text-white shadow-lg"
                  : "text-slate-300 hover:bg-slate-700 hover:text-white"
              }`}
              title={isCollapsed ? item.title : ""}
            >
              <Icon
                className={`${
                  isCollapsed ? "w-6 h-6" : "w-5 h-5"
                } flex-shrink-0 ${
                  isActive ? "text-white" : "text-slate-400 group-hover:text-white"
                }`}
              />
              {!isCollapsed && (
                <div className="flex-1">
                  <p className="font-medium text-sm">{item.title}</p>
                  <p className="text-xs text-slate-400 group-hover:text-slate-300">
                    {item.description}
                  </p>
                </div>
              )}
            </Link>
          );
        })}
      </nav>

      {/* Footer */}
      <div className="p-4 border-t border-slate-700">
        <button
          onClick={handleLogout}
          className={`flex items-center ${
            isCollapsed ? "justify-center" : "space-x-3"
          } w-full px-4 py-3 rounded-lg text-slate-300 hover:bg-red-600 hover:text-white transition-all duration-200 group`}
          title={isCollapsed ? "Cerrar sesión" : ""}
        >
          <LogOut
            className={`${
              isCollapsed ? "w-6 h-6" : "w-5 h-5"
            } flex-shrink-0 text-slate-400 group-hover:text-white`}
          />
          {!isCollapsed && (
            <span className="font-medium text-sm">Cerrar sesión</span>
          )}
        </button>
      </div>
    </aside>
  );
}
