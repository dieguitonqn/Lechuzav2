import React from "react";
import Link from "next/link";
import { FolderKanban, Search, Plus, Calendar } from "lucide-react";

export default function ProjectsPage() {
  // TODO: Fetch real projects from API
  const projects = [
    {
      id: "1",
      nombre: "Proyecto Central Eléctrica",
      codigo: "PRJ-2024-001",
      empresa: "EPEN",
      estado: "En Progreso",
      fecha_inicio: "2024-01-15",
      documentos: 45,
    },
    {
      id: "2",
      nombre: "Expansión Red Norte",
      codigo: "PRJ-2024-002",
      empresa: "EPEN",
      estado: "Planificación",
      fecha_inicio: "2024-03-01",
      documentos: 23,
    },
    {
      id: "3",
      nombre: "Edificio Administrativo",
      codigo: "PRJ-2024-003",
      empresa: "Constructora ABC",
      estado: "Completado",
      fecha_inicio: "2023-11-01",
      documentos: 89,
    },
  ];

  const getStatusColor = (status: string) => {
    const colors: Record<string, string> = {
      "En Progreso": "bg-yellow-100 text-yellow-800",
      Planificación: "bg-blue-100 text-blue-800",
      Completado: "bg-green-100 text-green-800",
      Pausado: "bg-gray-100 text-gray-800",
    };
    return colors[status] || "bg-gray-100 text-gray-800";
  };

  return (
    <div className="p-8">
      {/* Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-4xl font-bold text-gray-800 mb-2 flex items-center">
            <FolderKanban className="w-10 h-10 mr-3 text-red-600" />
            Gestión de Proyectos
          </h1>
          <p className="text-gray-600">
            Administra los proyectos del sistema
          </p>
        </div>
        <Link
          href="/dashboard/projects/new_project"
          className="flex items-center px-6 py-3 bg-red-600 hover:bg-red-700 text-white font-semibold rounded-lg transition-all duration-200 shadow-md hover:shadow-lg">
          <Plus className="w-5 h-5 mr-2" />
          Nuevo Proyecto
        </Link>
      </div>

      {/* Search and Filters */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 mb-6">
        <div className="flex items-center space-x-4">
          <div className="flex-1 relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
            <input
              type="text"
              placeholder="Buscar proyectos..."
              className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500"
            />
          </div>
          <select className="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500">
            <option value="">Todas las empresas</option>
            <option value="epen">EPEN</option>
            <option value="abc">Constructora ABC</option>
          </select>
          <select className="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500">
            <option value="">Todos los estados</option>
            <option value="progress">En Progreso</option>
            <option value="planning">Planificación</option>
            <option value="completed">Completado</option>
          </select>
        </div>
      </div>

      {/* Projects Table */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gray-50 border-b border-gray-200">
              <tr>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Proyecto
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Código
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Empresa
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Estado
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Fecha Inicio
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Documentos
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Acciones
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {projects.map((project) => (
                <tr
                  key={project.id}
                  className="hover:bg-gray-50 transition-colors"
                >
                  <td className="px-6 py-4">
                    <p className="text-sm font-medium text-gray-900">
                      {project.nombre}
                    </p>
                  </td>
                  <td className="px-6 py-4">
                    <p className="text-sm font-mono text-gray-600">
                      {project.codigo}
                    </p>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600">
                    {project.empresa}
                  </td>
                  <td className="px-6 py-4">
                    <span
                      className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold ${getStatusColor(
                        project.estado
                      )}`}
                    >
                      {project.estado}
                    </span>
                  </td>
                  <td className="px-6 py-4">
                    <div className="flex items-center text-sm text-gray-600">
                      <Calendar className="w-4 h-4 mr-2 text-gray-400" />
                      {new Date(project.fecha_inicio).toLocaleDateString(
                        "es-ES"
                      )}
                    </div>
                  </td>
                  <td className="px-6 py-4">
                    <span className="inline-flex items-center px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-xs font-semibold">
                      {project.documentos}
                    </span>
                  </td>
                  <td className="px-6 py-4">
                    <div className="flex items-center space-x-2">
                      <button className="text-blue-600 hover:text-blue-800 text-sm font-medium">
                        Ver
                      </button>
                      <span className="text-gray-300">|</span>
                      <button className="text-green-600 hover:text-green-800 text-sm font-medium">
                        Editar
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
