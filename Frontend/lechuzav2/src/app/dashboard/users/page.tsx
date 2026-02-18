import React from "react";
import { Users, Search, Plus, UserCheck, UserX } from "lucide-react";

export default function UsersPage() {
  // TODO: Fetch real users from API
  const users = [
    {
      id: "1",
      name: "Juan Pérez",
      email: "juan.perez@epen.gov.ar",
      role: "Admin",
      company: "EPEN",
      isActive: true,
    },
    {
      id: "2",
      name: "María García",
      email: "maria.garcia@empresa.com",
      role: "Usuario",
      company: "Empresa Ejemplo",
      isActive: true,
    },
    {
      id: "3",
      name: "Carlos López",
      email: "carlos.lopez@empresa.com",
      role: "Usuario",
      company: "Otra Empresa",
      isActive: false,
    },
  ];

  return (
    <div className="p-8">
      {/* Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-4xl font-bold text-gray-800 mb-2 flex items-center">
            <Users className="w-10 h-10 mr-3 text-red-600" />
            Gestión de Usuarios
          </h1>
          <p className="text-gray-600">
            Administra los usuarios del sistema
          </p>
        </div>
        <button className="flex items-center px-6 py-3 bg-red-600 hover:bg-red-700 text-white font-semibold rounded-lg transition-all duration-200 shadow-md hover:shadow-lg">
          <Plus className="w-5 h-5 mr-2" />
          Nuevo Usuario
        </button>
      </div>

      {/* Search and Filters */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 mb-6">
        <div className="flex items-center space-x-4">
          <div className="flex-1 relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
            <input
              type="text"
              placeholder="Buscar usuarios..."
              className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500"
            />
          </div>
          <select className="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500">
            <option value="">Todos los roles</option>
            <option value="admin">Admin</option>
            <option value="user">Usuario</option>
          </select>
          <select className="px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500">
            <option value="">Todos los estados</option>
            <option value="active">Activos</option>
            <option value="inactive">Inactivos</option>
          </select>
        </div>
      </div>

      {/* Users Table */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gray-50 border-b border-gray-200">
              <tr>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Usuario
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Email
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Rol
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Empresa
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Estado
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Acciones
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {users.map((user) => (
                <tr
                  key={user.id}
                  className="hover:bg-gray-50 transition-colors"
                >
                  <td className="px-6 py-4">
                    <div className="flex items-center">
                      <div className="w-10 h-10 bg-gradient-to-r from-red-500 to-red-600 rounded-full flex items-center justify-center text-white font-bold mr-3">
                        {user.name.charAt(0)}
                      </div>
                      <div>
                        <p className="text-sm font-medium text-gray-900">
                          {user.name}
                        </p>
                      </div>
                    </div>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600">
                    {user.email}
                  </td>
                  <td className="px-6 py-4">
                    <span
                      className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold ${
                        user.role === "Admin"
                          ? "bg-purple-100 text-purple-800"
                          : "bg-blue-100 text-blue-800"
                      }`}
                    >
                      {user.role}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600">
                    {user.company}
                  </td>
                  <td className="px-6 py-4">
                    <span
                      className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold ${
                        user.isActive
                          ? "bg-green-100 text-green-800"
                          : "bg-red-100 text-red-800"
                      }`}
                    >
                      {user.isActive ? (
                        <>
                          <UserCheck className="w-3 h-3 mr-1" />
                          Activo
                        </>
                      ) : (
                        <>
                          <UserX className="w-3 h-3 mr-1" />
                          Inactivo
                        </>
                      )}
                    </span>
                  </td>
                  <td className="px-6 py-4">
                    <div className="flex items-center space-x-2">
                      <button className="text-blue-600 hover:text-blue-800 text-sm font-medium">
                        Editar
                      </button>
                      <span className="text-gray-300">|</span>
                      <button className="text-red-600 hover:text-red-800 text-sm font-medium">
                        Eliminar
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
