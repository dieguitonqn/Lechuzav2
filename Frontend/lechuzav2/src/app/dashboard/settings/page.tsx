import React from "react";
import { Settings, Save, Bell, Shield, Database, Mail } from "lucide-react";

export default function SettingsPage() {
  return (
    <div className="p-8">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-4xl font-bold text-gray-800 mb-2 flex items-center">
          <Settings className="w-10 h-10 mr-3 text-red-600" />
          Configuración del Sistema
        </h1>
        <p className="text-gray-600">
          Ajustes generales y configuración avanzada
        </p>
      </div>

      {/* Settings Sections */}
      <div className="space-y-6">
        {/* General Settings */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div className="flex items-center mb-4">
            <Database className="w-6 h-6 text-red-600 mr-3" />
            <h2 className="text-xl font-bold text-gray-800">
              Configuración General
            </h2>
          </div>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Nombre del Sistema
              </label>
              <input
                type="text"
                defaultValue="Lechuza - Sistema de Gestión Documental"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Tamaño máximo de archivo (MB)
              </label>
              <input
                type="number"
                defaultValue="50"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500"
              />
            </div>
          </div>
        </div>

        {/* Notifications */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div className="flex items-center mb-4">
            <Bell className="w-6 h-6 text-red-600 mr-3" />
            <h2 className="text-xl font-bold text-gray-800">Notificaciones</h2>
          </div>
          <div className="space-y-3">
            <label className="flex items-center space-x-3">
              <input
                type="checkbox"
                defaultChecked
                className="w-5 h-5 rounded border-gray-300 text-red-600 focus:ring-red-500"
              />
              <span className="text-gray-700">
                Notificar nuevos documentos
              </span>
            </label>
            <label className="flex items-center space-x-3">
              <input
                type="checkbox"
                defaultChecked
                className="w-5 h-5 rounded border-gray-300 text-red-600 focus:ring-red-500"
              />
              <span className="text-gray-700">Notificar nuevos usuarios</span>
            </label>
            <label className="flex items-center space-x-3">
              <input
                type="checkbox"
                className="w-5 h-5 rounded border-gray-300 text-red-600 focus:ring-red-500"
              />
              <span className="text-gray-700">
                Notificar actualizaciones del sistema
              </span>
            </label>
          </div>
        </div>

        {/* Security */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div className="flex items-center mb-4">
            <Shield className="w-6 h-6 text-red-600 mr-3" />
            <h2 className="text-xl font-bold text-gray-800">Seguridad</h2>
          </div>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Tiempo de sesión (minutos)
              </label>
              <input
                type="number"
                defaultValue="60"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500"
              />
            </div>
            <label className="flex items-center space-x-3">
              <input
                type="checkbox"
                defaultChecked
                className="w-5 h-5 rounded border-gray-300 text-red-600 focus:ring-red-500"
              />
              <span className="text-gray-700">
                Requerir autenticación de dos factores
              </span>
            </label>
          </div>
        </div>

        {/* Email Settings */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div className="flex items-center mb-4">
            <Mail className="w-6 h-6 text-red-600 mr-3" />
            <h2 className="text-xl font-bold text-gray-800">
              Configuración de Email
            </h2>
          </div>
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Servidor SMTP
              </label>
              <input
                type="text"
                placeholder="smtp.ejemplo.com"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Email del remitente
              </label>
              <input
                type="email"
                placeholder="noreply@lechuza.com"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500"
              />
            </div>
          </div>
        </div>

        {/* Save Button */}
        <div className="flex justify-end">
          <button className="flex items-center px-8 py-3 bg-red-600 hover:bg-red-700 text-white font-semibold rounded-lg transition-all duration-200 shadow-md hover:shadow-lg">
            <Save className="w-5 h-5 mr-2" />
            Guardar Cambios
          </button>
        </div>
      </div>
    </div>
  );
}
