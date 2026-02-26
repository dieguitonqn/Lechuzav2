"use client";

import React, { useState, useEffect } from 'react';
import { useSession } from 'next-auth/react';
import { redirect } from 'next/navigation';
import { Project, IngresoDocs, DocsIn } from '../interfaces';
import { FileText, Building2, Upload, Plus, Minus, Send, Calendar, FileCheck, Info } from 'lucide-react';

export default function IngresoDocumentos() {
    const { data: session, status } = useSession();
    const [projects, setProjects] = useState<Project[]>([]);
    const [loading, setLoading] = useState(true);
    const [submitting, setSubmitting] = useState(false);
    const [documentCount, setDocumentCount] = useState(2);
    
    // Estado del formulario
    const [formData, setFormData] = useState<IngresoDocs>({
        obra_id:'',
        obra_codigo: '',
        obra_descripcion: '',
        np_ttal: '',
        np_ttal_file: null as any,
        np_ttal_descripcion: '',
        documentos: Array(2).fill(null).map(() => ({
            codigo: '',
            revision: '',
            fecha: '',
            file: null as any,
            descripcion: ''
        }))
    });

    // Cargar proyectos del usuario
    useEffect(() => {
        if (status === 'loading') return;
        if (!session?.accessToken) {
            redirect('/auth/signin');
        }

        const fetchProjects = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/v1/projects/', {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${session.accessToken}`,
                        'Content-Type': 'application/json',
                    },
                });

                if (response.status === 401) {
                    redirect('/auth/signout');
                }

                const data = await response.json();
                setProjects(Array.isArray(data) ? data : []);
            } catch (error) {
                console.error('Error fetching projects:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchProjects();
    }, [session, status]);

    // Actualizar cantidad de documentos
    const updateDocumentCount = (newCount: number) => {
        const count = Math.max(1, Math.min(10, newCount));
        setDocumentCount(count);
        
        const newDocuments = Array(count).fill(null).map((_, index) => {
            if (index < formData.documentos.length) {
                return formData.documentos[index];
            }
            return {
                codigo: '',
                revision: '',
                fecha: '',
                file: null as any,
                descripcion: ''
            };
        });

        setFormData(prev => ({
            ...prev,
            documentos: newDocuments
        }));
    };

    // Manejar cambios en el proyecto seleccionado
    const handleProjectChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        const projectId = e.target.value;
        const selectedProject = projects.find(p => p.id === projectId);
        
        setFormData(prev => ({
            ...prev,
            obra_id: projectId,
            obra_codigo: selectedProject?.codigo || '',
            obra_descripcion: selectedProject?.descripcion || ''
        }));
    };

    // Manejar cambios en campos del transmittal
    const handleTransmittalChange = (field: string, value: string | File | null) => {
        setFormData(prev => ({
            ...prev,
            [field]: value
        }));
    };

    // Manejar cambios en documentos
    const handleDocumentChange = (index: number, field: string, value: string | File | null) => {
        const updatedDocuments = [...formData.documentos];
        updatedDocuments[index] = {
            ...updatedDocuments[index],
            [field]: value
        };
        
        setFormData(prev => ({
            ...prev,
            documentos: updatedDocuments
        }));
    };

    // Validar formulario
    const validateForm = (): boolean => {
        if (!formData.obra_codigo) {
            alert('Por favor selecciona una obra');
            return false;
        }
        
        if (!formData.np_ttal || !formData.np_ttal_descripcion || !formData.np_ttal_file) {
            alert('Por favor completa todos los campos del transmittal');
            return false;
        }

        for (let i = 0; i < formData.documentos.length; i++) {
            const doc = formData.documentos[i];
            if (!doc.codigo || !doc.descripcion || !doc.file || !doc.revision) {
                alert(`Por favor completa todos los campos del documento ${i + 1}`);
                return false;
            }
        }

        return true;
    };

    // Enviar formulario
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        
        if (!validateForm()) return;

        setSubmitting(true);

        try {
            const submitFormData = new FormData();
            
            // Datos del transmittal
            submitFormData.append('obra_id', formData.obra_id);
            submitFormData.append('obra_codigo', formData.obra_codigo);
            submitFormData.append('obra_descripcion', formData.obra_descripcion);
            submitFormData.append('np_ttal', formData.np_ttal);
            submitFormData.append('np_ttal_file', formData.np_ttal_file);
            submitFormData.append('np_ttal_descripcion', formData.np_ttal_descripcion);

            // Documentos
            formData.documentos.forEach((doc, index) => {
                submitFormData.append(`documentos[${index}][codigo]`, doc.codigo);
                submitFormData.append(`documentos[${index}][revision]`, doc.revision);
                submitFormData.append(`documentos[${index}][descripcion]`, doc.descripcion);
                submitFormData.append(`documentos[${index}][file]`, doc.file);
            });
            // Debug: Log form data for inspection
            console.log('FormData preparada para envío:');
            console.log('- Obra Código:', formData.obra_codigo);
            console.log('- Obra descripción:', formData.obra_descripcion);
            console.log('- Transmittal N°:', formData.np_ttal);
            console.log('- Transmittal file:', formData.np_ttal_file?.name, formData.np_ttal_file?.size, 'bytes');
            console.log('- Transmittal descripción:', formData.np_ttal_descripcion);
            console.log('- Documentos:');
            formData.documentos.forEach((doc, index) => {
                console.log(`  [${index}]:`, {
                    codigo: doc.codigo,
                    revision: doc.revision,
                    descripcion: doc.descripcion,
                    fileName: doc.file?.name,
                    fileSize: doc.file?.size
                });
            });

            // Debug: Log all FormData entries
            console.log('FormData entries:');
            for (let pair of submitFormData.entries()) {
                if (pair[1] instanceof File) {
                    console.log(`${pair[0]}:`, `File - ${pair[1].name} (${pair[1].size} bytes)`);
                } else {
                    console.log(`${pair[0]}:`, pair[1]);
                }
            }
            const response = await fetch('http://localhost:8000/api/v1/documents/upload', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${session?.accessToken}`,
                },
                body: submitFormData,
            });

            if (response.ok) {
                alert('Documentos enviados exitosamente');
                // Reset form
                setFormData({
                    obra_id:'',
                    obra_codigo: '',
                    obra_descripcion: '',
                    np_ttal: '',
                    np_ttal_file: null as any,
                    np_ttal_descripcion: '',
                    documentos: Array(2).fill(null).map(() => ({
                        codigo: '',
                        revision: '',
                        fecha: '',
                        file: null as any,
                        descripcion: ''
                    }))
                });
                setDocumentCount(2);
            } else {
                const errorData = await response.json();
                alert(`Error al enviar documentos: ${errorData.detail || 'Error desconocido'}`);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Error al enviar documentos');
        } finally {
            setSubmitting(false);
        }
    };

    if (loading) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 flex items-center justify-center">
                <div className="text-center">
                    <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-red-600 mb-4"></div>
                    <p className="text-gray-600">Cargando proyectos...</p>
                </div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
            <div className="container mx-auto px-4 py-6 md:py-4">
                {/* Header */}
                <div className="mb-6 md:mb-4">
                    <h1 className="text-4xl md:text-3xl font-bold text-gray-800 mb-2 md:mb-1 flex items-center">
                        <FileText className="w-10 h-10 md:w-8 md:h-8 mr-4 md:mr-3 text-red-600" />
                        Ingreso de Documentos
                    </h1>
                    <p className="text-gray-600 text-base md:text-sm">
                        Sube documentación y transmittals para tus proyectos
                    </p>
                </div>

                <form onSubmit={handleSubmit} className="space-y-8 md:space-y-5">
                    {/* Selector de Obra */}
                    <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
                        <div className="bg-red-50 px-6 md:px-4 py-4 md:py-3 border-b border-red-100">
                            <h2 className="text-xl md:text-lg font-semibold text-red-800 flex items-center">
                                <Building2 className="w-6 h-6 md:w-5 md:h-5 mr-2" />
                                Obra
                                <Info className="w-4 h-4 md:w-3 md:h-3 ml-2 text-red-600" />
                            </h2>
                        </div>
                        <div className="p-6 md:p-4">
                            <select
                                value={formData.obra_id}
                                onChange={handleProjectChange}
                                className="w-full p-4 md:p-3 border-2 border-gray-200 rounded-lg focus:border-red-500 focus:outline-none text-lg md:text-base"
                                required
                            >
                                <option value="">Selecciona una obra</option>
                                {projects.map(project => (
                                    <option key={project.id} value={project.id}>
                                        {project.nombre} ({project.codigo})
                                    </option>
                                ))}
                            </select>
                        </div>
                    </div>

                    {/* Ingreso de Transmittal */}
                    <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
                        <div className="bg-blue-50 px-6 md:px-4 py-4 md:py-3 border-b border-blue-100">
                            <h2 className="text-xl md:text-lg font-semibold text-blue-800 flex items-center">
                                <FileCheck className="w-6 h-6 md:w-5 md:h-5 mr-2" />
                                Ingreso de Comunicación
                                <Info className="w-4 h-4 md:w-3 md:h-3 ml-2 text-blue-600" />
                            </h2>
                        </div>
                        <div className="p-6 md:p-4">
                            <div className="grid grid-cols-1 lg:grid-cols-6 gap-6 md:gap-4">
                                <div className="lg:col-span-1">
                                    <label className="block text-sm md:text-xs font-medium text-gray-700 mb-2 md:mb-1">
                                        Transmittal/NP N°
                                    </label>
                                    <input
                                        type="text"
                                        value={formData.np_ttal}
                                        onChange={(e) => handleTransmittalChange('np_ttal', e.target.value)}
                                        className="w-full p-3 md:p-2 border border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none text-base md:text-sm"
                                        required
                                    />
                                </div>
                                <div className="lg:col-span-3">
                                    <label className="block text-sm md:text-xs font-medium text-gray-700 mb-2 md:mb-1">
                                        Descripción de la nota
                                    </label>
                                    <input
                                        type="text"
                                        value={formData.np_ttal_descripcion}
                                        onChange={(e) => handleTransmittalChange('np_ttal_descripcion', e.target.value)}
                                        className="w-full p-3 md:p-2 border border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none text-base md:text-sm"
                                        placeholder="Descripción del transmittal"
                                        required
                                    />
                                </div>
                                <div className="lg:col-span-2">
                                    <label className="block text-sm md:text-xs font-medium text-gray-700 mb-2 md:mb-1">
                                        Archivo del TTAL
                                    </label>
                                    <input
                                        type="file"
                                        onChange={(e) => handleTransmittalChange('np_ttal_file', e.target.files?.[0] || null)}
                                        className="w-full p-3 md:p-2 border border-gray-300 rounded-lg focus:border-blue-500 focus:outline-none text-base md:text-sm"
                                        accept=".pdf,.doc,.docx"
                                        required
                                    />
                                </div>
                                
                            </div>
                        </div>
                    </div>

                    {/* Selector de cantidad de documentos */}
                    <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
                        <div className="bg-green-50 px-6 md:px-4 py-4 md:py-3 border-b border-green-100">
                            <h2 className="text-xl md:text-lg font-semibold text-green-800 flex items-center">
                                <Upload className="w-6 h-6 md:w-5 md:h-5 mr-2" />
                                Ingreso de Documentos Adjuntos (Máximo total 50Mb)
                                <Info className="w-4 h-4 md:w-3 md:h-3 ml-2 text-green-600" />
                            </h2>
                        </div>
                        <div className="p-6 md:p-4">
                            <div className="flex items-center gap-4 md:gap-3 mb-6 md:mb-4">
                                <div className="flex items-center gap-2">
                                    <label className="text-sm md:text-xs font-medium text-gray-700">
                                        Cantidad de documentos adjuntos:
                                    </label>
                                    <button
                                        type="button"
                                        onClick={() => updateDocumentCount(documentCount - 1)}
                                        className="p-1 rounded-full bg-red-100 text-red-600 hover:bg-red-200 transition-colors"
                                        disabled={documentCount <= 1}
                                    >
                                        <Minus className="w-4 h-4 md:w-3 md:h-3" />
                                    </button>
                                    <span className="bg-gray-100 px-4 md:px-3 py-2 md:py-1 rounded-lg font-semibold text-gray-700 min-w-[3rem] md:min-w-[2.5rem] text-center text-base md:text-sm">
                                        {documentCount}
                                    </span>
                                    <button
                                        type="button"
                                        onClick={() => updateDocumentCount(documentCount + 1)}
                                        className="p-1 rounded-full bg-green-100 text-green-600 hover:bg-green-200 transition-colors"
                                        disabled={documentCount >= 10}
                                    >
                                        <Plus className="w-4 h-4 md:w-3 md:h-3" />
                                    </button>
                                </div>
                                <div className="bg-gray-100 px-4 md:px-3 py-2 md:py-1 rounded-lg text-sm md:text-xs text-gray-600">
                                    0Mb de 50Mb
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Lista de documentos adjuntos */}
                    <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
                        <div className="bg-purple-50 px-6 md:px-4 py-4 md:py-3 border-b border-purple-100">
                            <h2 className="text-xl md:text-lg font-semibold text-purple-800 flex items-center">
                                <FileText className="w-6 h-6 md:w-5 md:h-5 mr-2" />
                                Lista de documentos adjuntos
                                <Info className="w-4 h-4 md:w-3 md:h-3 ml-2 text-purple-600" />
                            </h2>
                        </div>
                        <div className="overflow-x-auto">
                            <table className="w-full">
                                <thead className="bg-gray-50">
                                    <tr>
                                        <th className="px-4 md:px-3 py-3 md:py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Item</th>
                                        <th className="px-4 md:px-3 py-3 md:py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Archivo</th>
                                        <th className="px-4 md:px-3 py-3 md:py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Código</th>
                                        <th className="px-4 md:px-3 py-3 md:py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Descripción</th>
                                        <th className="px-4 md:px-3 py-3 md:py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Revisión</th>
                                    </tr>
                                </thead>
                                <tbody className="bg-white divide-y divide-gray-200">
                                    {formData.documentos.map((doc, index) => (
                                        <tr key={index} className="hover:bg-gray-50">
                                            <td className="px-4 md:px-3 py-4 md:py-3 whitespace-nowrap text-sm md:text-xs text-gray-900 font-medium">
                                                {index + 1}
                                            </td>
                                            <td className="px-4 md:px-3 py-4 md:py-3">
                                                <input
                                                    type="file"
                                                    onChange={(e) => handleDocumentChange(index, 'file', e.target.files?.[0] || null)}
                                                    className="w-full p-2 md:p-1 text-sm md:text-xs border border-gray-300 rounded focus:border-purple-500 focus:outline-none"
                                                    accept=".pdf,.doc,.docx,.jpg,.jpeg,.png"
                                                    required
                                                />
                                            </td>
                                            <td className="px-4 md:px-3 py-4 md:py-3">
                                                <input
                                                    type="text"
                                                    value={doc.codigo}
                                                    onChange={(e) => handleDocumentChange(index, 'codigo', e.target.value)}
                                                    className="w-full p-2 md:p-1 text-sm md:text-xs border border-gray-300 rounded focus:border-purple-500 focus:outline-none"
                                                    placeholder="Código"
                                                    required
                                                />
                                            </td>
                                            <td className="px-4 md:px-3 py-4 md:py-3">
                                                <input
                                                    type="text"
                                                    value={doc.descripcion}
                                                    onChange={(e) => handleDocumentChange(index, 'descripcion', e.target.value)}
                                                    className="w-full p-2 md:p-1 text-sm md:text-xs border border-gray-300 rounded focus:border-purple-500 focus:outline-none"
                                                    placeholder="Descripción"
                                                    required
                                                />
                                            </td>
                                            <td className="px-4 md:px-3 py-4 md:py-3">
                                                <input
                                                    type="text"
                                                    value={doc.revision}
                                                    onChange={(e) => handleDocumentChange(index, 'revision', e.target.value)}
                                                    className="w-full p-2 md:p-1 text-sm md:text-xs border border-gray-300 rounded focus:border-purple-500 focus:outline-none"
                                                    placeholder="Rev."
                                                    required
                                                />
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>

                    {/* Botón de envío */}
                    <div className="flex justify-center">
                        <button
                            type="submit"
                            disabled={submitting}
                            className="flex items-center px-8 md:px-6 py-4 md:py-3 bg-gradient-to-r from-green-600 to-green-700 text-white font-semibold rounded-xl shadow-lg hover:from-green-700 hover:to-green-800 focus:outline-none focus:ring-4 focus:ring-green-300 transition-all duration-200 transform hover:scale-[1.02] active:scale-[0.98] disabled:opacity-50 disabled:cursor-not-allowed text-base md:text-sm"
                        >
                            {submitting ? (
                                <>
                                    <div className="animate-spin rounded-full h-5 w-5 md:h-4 md:w-4 border-b-2 border-white mr-2"></div>
                                    Enviando...
                                </>
                            ) : (
                                <>
                                    <Send className="w-5 h-5 md:w-4 md:h-4 mr-2" />
                                    Enviar
                                </>
                            )}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}
