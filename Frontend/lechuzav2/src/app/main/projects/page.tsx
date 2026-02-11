"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { Calendar, Upload, Mail, Building2, FileText, Hash, User, Plus, X } from "lucide-react";

interface ProjectFormData {
  nombre: string;
  codigo: string;
  descripcion: string;
  fecha_inicio: string;
  fecha_fin: string;
  emails_notificacion: string[];
  company_id: string;
  contrato: string;
  contrato_file: File | null;
}

const NewProjectPage = () => {
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [emailInput, setEmailInput] = useState("");
  const [formData, setFormData] = useState<ProjectFormData>({
    nombre: "",
    codigo: "",
    descripcion: "",
    fecha_inicio: new Date().toISOString().split('T')[0],
    fecha_fin: "",
    emails_notificacion: [],
    company_id: "",
    contrato: "",
    contrato_file: null,
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0] || null;
    setFormData(prev => ({
      ...prev,
      contrato_file: file
    }));
  };

  const addEmail = () => {
    if (emailInput.trim() && !formData.emails_notificacion.includes(emailInput.trim())) {
      setFormData(prev => ({
        ...prev,
        emails_notificacion: [...prev.emails_notificacion, emailInput.trim()]
      }));
      setEmailInput("");
    }
  };

  const removeEmail = (email: string) => {
    setFormData(prev => ({
      ...prev,
      emails_notificacion: prev.emails_notificacion.filter(e => e !== email)
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      const formDataToSend = new FormData();
      formDataToSend.append("name", formData.nombre);
      formDataToSend.append("code", formData.codigo);
      formDataToSend.append("description", formData.descripcion);
      formDataToSend.append("fecha_inicio", formData.fecha_inicio);
      if (formData.fecha_fin) {
        formDataToSend.append("fecha_fin", formData.fecha_fin);
      }
      formDataToSend.append("emails_notification", JSON.stringify(formData.emails_notificacion));
      if (formData.company_id) {
        formDataToSend.append("company_id", formData.company_id);
      }
      formDataToSend.append("contract", formData.contrato);
      if (formData.contrato_file) {
        formDataToSend.append("contract_file", formData.contrato_file);
      }

      // Aquí harías la llamada a tu API
      // const response = await fetch("/api/projects", {
      //   method: "POST",
      //   body: formDataToSend,
      // });

      console.log("Datos del proyecto:", Object.fromEntries(formDataToSend));
      
      // Simular éxito por ahora
      alert("Proyecto creado exitosamente");
      router.push("/projects");
    } catch (error) {
      console.error("Error al crear proyecto:", error);
      alert("Error al crear el proyecto");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-white rounded-lg shadow-lg">
          {/* Header */}
          <div className="px-6 py-4 border-b border-gray-200">
            <h1 className="text-2xl font-bold text-gray-900 flex items-center">
              <Building2 className="mr-3 text-red-600" size={28} />
              Nuevo Proyecto
            </h1>
            <p className="mt-1 text-sm text-gray-600">
              Complete la información requerida para crear un nuevo proyecto
            </p>
          </div>

          <form onSubmit={handleSubmit} className="p-6">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* Información Básica */}
              <div className="space-y-6">
                <div className="bg-gray-50 p-4 rounded-lg">
                  <h3 className="text-lg font-medium text-gray-900 mb-4 flex items-center">
                    <FileText className="mr-2 text-red-600" size={20} />
                    Información Básica
                  </h3>
                  
                  {/* Nombre del Proyecto */}
                  <div className="mb-4">
                    <label htmlFor="nombre" className="block text-sm font-medium text-gray-700 mb-1">
                      Nombre del Proyecto <span className="text-red-500">*</span>
                    </label>
                    <input
                      type="text"
                      id="nombre"
                      name="nombre"
                      required
                      value={formData.nombre}
                      onChange={handleInputChange}
                      className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-red-600 focus:border-red-600"
                      placeholder="Ingrese el nombre del proyecto"
                    />
                  </div>

                  {/* Código del Proyecto */}
                  <div className="mb-4">
                    <label htmlFor="codigo" className="block text-sm font-medium text-gray-700 mb-1">
                      Código del Proyecto <span className="text-red-500">*</span>
                    </label>
                    <div className="relative">
                      <Hash className="absolute left-3 top-2.5 text-gray-400" size={16} />
                      <input
                        type="text"
                        id="codigo"
                        name="codigo"
                        required
                        value={formData.codigo}
                        onChange={handleInputChange}
                        className="w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-red-600 focus:border-red-600"
                        placeholder="PRY-001"
                      />
                    </div>
                  </div>

                  {/* Descripción */}
                  <div>
                    <label htmlFor="descripcion" className="block text-sm font-medium text-gray-700 mb-1">
                      Descripción
                    </label>
                    <textarea
                      id="descripcion"
                      name="descripcion"
                      rows={3}
                      value={formData.descripcion}
                      onChange={handleInputChange}
                      className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
                      placeholder="Describa brevemente el proyecto..."
                    />
                  </div>
                </div>

                <div className="bg-gray-50 p-4 rounded-lg">
                  <h3 className="text-lg font-medium text-gray-900 mb-4 flex items-center">
                    <Upload className="mr-2 text-red-600" size={20} />
                    Contrato
                  </h3>
                  
                  {/* Descripción del Contrato */}
                  <div className="mb-4">
                    <label htmlFor="contrato" className="block text-sm font-medium text-gray-700 mb-1">
                      Descripción del Contrato
                    </label>
                    <input
                      type="text"
                      id="contrato"
                      name="contrato"
                      value={formData.contrato}
                      onChange={handleInputChange}
                      className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-red-600 focus:border-red-600"
                      placeholder="Nombre o descripción del contrato"
                    />
                  </div>

                  {/* Archivo del Contrato */}
                  <div>
                    <label htmlFor="contrato_file" className="block text-sm font-medium text-gray-700 mb-1">
                      Archivo del Contrato <span className="text-red-500">*</span>
                    </label>
                    <input
                      type="file"
                      id="contrato_file"
                      name="contrato_file"
                      required
                      onChange={handleFileChange}
                      accept=".pdf,.doc,.docx"
                      className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-red-600 focus:border-red-600"
                    />
                    <p className="mt-1 text-xs text-gray-500">
                      Formatos permitidos: PDF, DOC, DOCX
                    </p>
                  </div>
                </div>
                
              </div>

              {/* Información Adicional */}
              <div className="space-y-6">
                {/* Emails de Notificación */}
                <div className="bg-gray-50 p-4 rounded-lg">
                  <h3 className="text-lg font-medium text-gray-900 mb-4 flex items-center">
                    <Mail className="mr-2 text-red-600" size={20} />
                    Emails de Notificación
                  </h3>
                  
                  <div className="space-y-3">
                    <div className="flex gap-2">
                      <input
                        type="email"
                        value={emailInput}
                        onChange={(e) => setEmailInput(e.target.value)}
                        placeholder="ejemplo@email.com"
                        className="flex-1 px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-red-600 focus:border-red-600"
                        onKeyPress={(e) => e.key === 'Enter' && (e.preventDefault(), addEmail())}
                      />
                      <button
                        type="button"
                        onClick={addEmail}
                        className="px-3 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 focus:ring-2 focus:ring-red  -500"
                      >
                        <Plus size={16} />
                      </button>
                    </div>
                    
                    {formData.emails_notificacion.length > 0 && (
                      <div className="space-y-1">
                        {formData.emails_notificacion.map((email, index) => (
                          <div key={index} className="flex items-center justify-between bg-blue-50 px-3 py-2 rounded-md">
                            <span className="text-sm text-gray-700">{email}</span>
                            <button
                              type="button"
                              onClick={() => removeEmail(email)}
                              className="text-red-500 hover:text-red-700"
                            >
                              <X size={14} />
                            </button>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                </div>

                {/* Compañía */}
                <div className="bg-gray-50 p-4 rounded-lg">
                  <h3 className="text-lg font-medium text-gray-900 mb-4 flex items-center">
                    <Building2 className="mr-2 text-red-600" size={20} />
                    Compañía
                  </h3>
                  
                  <select
                    id="company_id"
                    name="company_id"
                    value={formData.company_id}
                    onChange={handleInputChange}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-red-600 focus:border-red-600"
                  >
                    <option value="">Seleccionar compañía...</option>
                    <option value="1">Compañía Example 1</option>
                    <option value="2">Compañía Example 2</option>
                  </select>
                </div>

                {/* Contrato */}
                
              </div>
            </div>

            {/* Botones de Acción */}
            <div className="flex justify-end space-x-3 pt-6 border-t border-gray-200">
              <button
                type="button"
                onClick={() => router.back()}
                className="px-4 py-2 border border-gray-300 rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:ring-2 focus:ring-red-600"
              >
                Cancelar
              </button>
              <button
                type="submit"
                disabled={loading}
                className="px-6 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 focus:ring-2 focus:ring-red-600 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {loading ? "Creando..." : "Crear Proyecto"}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default NewProjectPage;
