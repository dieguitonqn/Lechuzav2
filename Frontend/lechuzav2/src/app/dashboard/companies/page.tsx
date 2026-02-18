import React from "react";
import { Building2, Search, Plus } from "lucide-react";

export default function CompaniesPage() {
  // TODO: Fetch real companies from API
  const companies = [
    {
      id: "1",
      name: "EPEN",
      description: "Ente Provincial de Energía de Neuquén",
      projects: 8,
      users: 25,
    },
    {
      id: "2",
      name: "Constructora ABC",
      description: "Empresa de construcción",
      projects: 3,
      users: 12,
    },
    {
      id: "3",
      name: "Ingeniería XYZ",
      description: "Servicios de ingeniería",
      projects: 4,
      users: 8,
    },
  ];

  return (
    <div className="p-8">
      {/* Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-4xl font-bold text-gray-800 mb-2 flex items-center">
            <Building2 className="w-10 h-10 mr-3 text-red-600" />
            Gestión de Empresas
          </h1>
          <p className="text-gray-600">
            Administra las empresas del sistema
          </p>
        </div>
        <button className="flex items-center px-6 py-3 bg-red-600 hover:bg-red-700 text-white font-semibold rounded-lg transition-all duration-200 shadow-md hover:shadow-lg">
          <Plus className="w-5 h-5 mr-2" />
          Nueva Empresa
        </button>
      </div>

      {/* Search */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 mb-6">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
          <input
            type="text"
            placeholder="Buscar empresas..."
            className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500"
          />
        </div>
      </div>

      {/* Companies Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {companies.map((company) => (
          <div
            key={company.id}
            className="bg-white rounded-xl shadow-sm hover:shadow-lg transition-all duration-300 border border-gray-200 overflow-hidden"
          >
            <div className="bg-gradient-to-r from-purple-500 to-purple-600 p-6 text-white">
              <Building2 className="w-12 h-12 mb-3 opacity-80" />
              <h3 className="text-xl font-bold mb-1">{company.name}</h3>
              <p className="text-purple-100 text-sm">{company.description}</p>
            </div>
            <div className="p-6">
              <div className="flex justify-between mb-4">
                <div>
                  <p className="text-2xl font-bold text-gray-800">
                    {company.projects}
                  </p>
                  <p className="text-sm text-gray-600">Proyectos</p>
                </div>
                <div>
                  <p className="text-2xl font-bold text-gray-800">
                    {company.users}
                  </p>
                  <p className="text-sm text-gray-600">Usuarios</p>
                </div>
              </div>
              <div className="flex space-x-2">
                <button className="flex-1 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-lg transition-colors">
                  Ver Detalles
                </button>
                <button className="px-4 py-2 border border-gray-300 hover:bg-gray-50 text-gray-700 text-sm font-medium rounded-lg transition-colors">
                  Editar
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
