import React from "react";
import { FileText, Search, Filter } from "lucide-react";

export default function DocumentsPage() {
  // TODO: Fetch real documents from API
  const documents = [
    {
      id: "1",
      nombre: "Plano Estructural Rev. A",
      proyecto: "Proyecto Central Eléctrica",
      tipo: "Plano",
      fecha: "2024-02-10",
      tamaño: "2.4 MB",
    },
    {
      id: "2",
      nombre: "Memoria de Cálculo",
      proyecto: "Expansión Red Norte",
      tipo: "Documento",
      fecha: "2024-02-08",
      tamaño: "1.8 MB",
    },
    {
      id: "3",
      nombre: "Especificaciones Técnicas",
      proyecto: "Edificio Administrativo",
      tipo: "Especificación",
      fecha: "2024-02-05",
      tamaño: "856 KB",
    },
  ];

  return (
    <div className="p-8">
      {/* Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-4xl font-bold text-gray-800 mb-2 flex items-center">
            <FileText className="w-10 h-10 mr-3 text-red-600" />
            Gestión de Documentos
          </h1>
          <p className="text-gray-600">
            Administra todos los documentos del sistema
          </p>
        </div>
      </div>

      {/* Search and Filters */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 mb-6">
        <div className="flex items-center space-x-4">
          <div className="flex-1 relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
            <input
              type="text"
              placeholder="Buscar documentos..."
              className="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500"
            />
          </div>
          <button className="flex items-center px-4 py-3 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
            <Filter className="w-5 h-5 mr-2 text-gray-600" />
            Filtros
          </button>
        </div>
      </div>

      {/* Documents Table */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gray-50 border-b border-gray-200">
              <tr>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Documento
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Proyecto
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Tipo
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Fecha
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Tamaño
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                  Acciones
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {documents.map((doc) => (
                <tr key={doc.id} className="hover:bg-gray-50 transition-colors">
                  <td className="px-6 py-4">
                    <div className="flex items-center">
                      <FileText className="w-5 h-5 text-blue-600 mr-3" />
                      <p className="text-sm font-medium text-gray-900">
                        {doc.nombre}
                      </p>
                    </div>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600">
                    {doc.proyecto}
                  </td>
                  <td className="px-6 py-4">
                    <span className="inline-flex items-center px-3 py-1 bg-purple-100 text-purple-800 rounded-full text-xs font-semibold">
                      {doc.tipo}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600">
                    {new Date(doc.fecha).toLocaleDateString("es-ES")}
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600">
                    {doc.tamaño}
                  </td>
                  <td className="px-6 py-4">
                    <div className="flex items-center space-x-2">
                      <button className="text-blue-600 hover:text-blue-800 text-sm font-medium">
                        Ver
                      </button>
                      <span className="text-gray-300">|</span>
                      <button className="text-green-600 hover:text-green-800 text-sm font-medium">
                        Descargar
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
