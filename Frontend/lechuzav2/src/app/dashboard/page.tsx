import React from "react";
import { Users, Building2, FolderKanban, FileText } from "lucide-react";

async function getDashboardStats() {
  // TODO: Fetch real data from API
  return {
    users: 42,
    companies: 8,
    projects: 15,
    documents: 234,
  };
}

export default async function DashboardPage() {
  const stats = await getDashboardStats();

  const cards = [
    {
      title: "Usuarios",
      value: stats.users,
      icon: Users,
      color: "from-blue-500 to-blue-600",
      href: "/dashboard/users",
    },
    {
      title: "Empresas",
      value: stats.companies,
      icon: Building2,
      color: "from-purple-500 to-purple-600",
      href: "/dashboard/companies",
    },
    {
      title: "Proyectos",
      value: stats.projects,
      icon: FolderKanban,
      color: "from-green-500 to-green-600",
      href: "/dashboard/projects",
    },
    {
      title: "Documentos",
      value: stats.documents,
      icon: FileText,
      color: "from-orange-500 to-orange-600",
      href: "/dashboard/documents",
    },
  ];

  return (
    <div className="p-8">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-4xl font-bold text-gray-800 mb-2">
          Dashboard Administrativo
        </h1>
        <p className="text-gray-600">
          Vista general del sistema de gestión documental
        </p>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {cards.map((card) => {
          const Icon = card.icon;
          return (
            <div
              key={card.title}
              className="bg-white rounded-xl shadow-sm hover:shadow-lg transition-all duration-300 border border-gray-200 overflow-hidden group cursor-pointer"
            >
              <div className={`bg-gradient-to-r ${card.color} p-6`}>
                <div className="flex items-center justify-between text-white">
                  <div>
                    <p className="text-white/80 text-sm font-medium mb-1">
                      {card.title}
                    </p>
                    <p className="text-4xl font-bold">{card.value}</p>
                  </div>
                  <Icon className="w-12 h-12 opacity-80" />
                </div>
              </div>
              <div className="p-4">
                <a
                  href={card.href}
                  className="text-sm text-gray-600 hover:text-gray-900 font-medium group-hover:underline"
                >
                  Ver detalles →
                </a>
              </div>
            </div>
          );
        })}
      </div>

      {/* Recent Activity */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <h2 className="text-xl font-bold text-gray-800 mb-4">
          Actividad Reciente
        </h2>
        <div className="space-y-4">
          {[1, 2, 3, 4].map((item) => (
            <div
              key={item}
              className="flex items-center justify-between py-3 border-b border-gray-100 last:border-0"
            >
              <div className="flex items-center space-x-4">
                <div className="w-10 h-10 bg-gradient-to-r from-red-500 to-red-600 rounded-full flex items-center justify-center text-white font-bold">
                  {item}
                </div>
                <div>
                  <p className="text-sm font-medium text-gray-800">
                    Actividad de ejemplo #{item}
                  </p>
                  <p className="text-xs text-gray-500">Hace 2 horas</p>
                </div>
              </div>
              <span className="text-xs px-3 py-1 bg-green-100 text-green-800 rounded-full font-medium">
                Completado
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
