import React from "react";
import Link from "next/link";
import { Project } from "@/app/main/interfaces";
import { FileText, Calendar, Building2, ChevronRight, Pencil, FileCheck } from "lucide-react";

interface ProjectCardsProps {
    projects: Project[];
    isAdmin?: boolean;
}

export default function ProjectCards({ projects, isAdmin }: ProjectCardsProps) {
    const formatDate = (dateString: string | null) => {
        if (!dateString) return "N/A";
        return new Date(dateString).toLocaleDateString("es-ES", {
            year: "numeric",
            month: "long",
            day: "numeric",
        });
    };

    const getStatusColor = (status: string) => {
        const colors: Record<string, string> = {
            activo: "bg-green-100 text-green-800 border-green-200",
            inactivo: "bg-gray-100 text-gray-800 border-gray-200",
            completado: "bg-blue-100 text-blue-800 border-blue-200",
            "en progreso": "bg-yellow-100 text-yellow-800 border-yellow-200",
        };
        return colors[status.toLowerCase()] || "bg-gray-100 text-gray-800 border-gray-200";
    };

    if ('detail' in projects && projects.detail === "Invalid or expired token") {
        return (
            <div className="flex flex-col items-center justify-center py-16 px-4">
                <Building2 className="w-16 h-16 text-gray-300 mb-4" />
                <h3 className="text-xl font-semibold text-gray-700 mb-2">
                    No hay proyectos disponibles
                </h3>
                <p className="text-gray-500 text-center max-w-md">
                    Aún no tienes proyectos asignados. Contacta a tu administrador para obtener acceso.
                </p>
            </div>
        );
    }

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
            {Array.isArray(projects) && projects.length > 0 && projects.map((project) => (
                <div
                    key={project.id}
                    className={`group bg-white rounded-xl shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-200 hover:border-${project.card_color}-300 overflow-hidden flex flex-col`}
                >
                    {/* Header con gradiente */}
                    <div className={`bg-gradient-to-r from-${project.card_color}-200 to-${project.card_color}-600 p-6 text-black relative`}>
                        <div className="mb-5">
                            {/* Botón de edición */}
                            {isAdmin && (
                                <Link
                                    href={`/main/projects/${project.id}/edit`}
                                    className="absolute top-4 right-4 p-2 rounded-lg bg-white/10 hover:bg-white/50 backdrop-blur-sm transition-all duration-200 hover:scale-110"
                                    title="Editar proyecto"
                                >
                                    <Pencil className="w-4 h-4" />
                                </Link>
                            )}
                        </div>

                        <div className="flex items-start justify-between mb-3 pr-8">
                            <div className="flex-1">
                                <h2 className="text-3xl font-bold mb-1 line-clamp-1">
                                    {project.nombre}
                                </h2>
                                <p className="text-slate-600 text-sm font-mono">{project.codigo}</p>
                            </div>
                            <Building2 className="w-8 h-8 opacity-80 flex-shrink-0 ml-2" />
                        </div>

                        {/* Estado */}
                        <span
                            className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold border ${getStatusColor(
                                project.estado_proyecto
                            )}`}
                        >
                            {project.estado_proyecto}
                        </span>
                        <div>
                            {project.companies && project.companies.length > 0 && (
                                project.companies.map((company) => (
                                    <span className="text-gray-500 text-sm m-2" key={company.id}>
                                        {company.nombre} : {company.codigo || "Sin código asociado"}
                                    </span>
                                ))
                            )}
                        </div>
                        {/* <span className="text-gray-500 text-sm m-2">
                            {project.companies && project.companies.length > 0 ? `${project.companies[0].nombre} : ${project.companies[0].codigo}` : "Sin empresa asignada"}
                        </span> */}
                    </div>

                    {/* Contenido */}
                    <div className="p-6 flex-1 flex flex-col">
                        {/* Descripción */}
                        <p className="text-gray-600 text-sm mb-4 line-clamp-3 flex-1">
                            {project.descripcion || "Sin descripción disponible"}
                        </p>

                        {/* Fechas */}
                        <div className="space-y-2 mb-6">
                            <div className="flex items-center text-sm text-gray-500">
                                <Calendar className="w-4 h-4 mr-2 text-gray-400" />
                                <span className="font-medium mr-2">Inicio:</span>
                                <span>{formatDate(project.fecha_inicio)}</span>
                            </div>
                            {project.fecha_fin && (
                                <div className="flex items-center text-sm text-gray-500">
                                    <Calendar className="w-4 h-4 mr-2 text-gray-400" />
                                    <span className="font-medium mr-2">Fin:</span>
                                    <span>{formatDate(project.fecha_fin)}</span>
                                </div>
                            )}
                        </div>

                        {/* Botones de acción */}
                        <div className="space-y-3">
                            {/* Link al contrato */}
                            {project.contrato_url && (
                                <Link
                                    href={project.contrato_url || "#"}
                                    target="_blank"
                                    className={`flex items-center justify-center w-full px-4 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium rounded-lg transition-all duration-200 transform hover:scale-[1.01] border border-slate-200 hover:border-slate-300 group`}
                                >
                                    <FileCheck className="w-4 h-4 mr-2" />
                                    Ver Contrato EPEN
                                    <ChevronRight className="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" />
                                </Link>
                            )}
                            
                            {/* Botón principal */}
                            <Link
                                href={`/main/projects/${project.id}/documents`}
                                className={`flex items-center justify-center w-full px-4 py-3 bg-${project.card_color}-600 hover:bg-${project.card_color}-700 text-white font-semibold rounded-lg transition-all duration-200 transform hover:scale-[1.02] active:scale-[0.98] shadow-md hover:shadow-lg group`}
                            >
                                <FileText className="w-5 h-5 mr-2" />
                                Ver Documentos
                                <ChevronRight className="w-5 h-5 ml-1 group-hover:translate-x-1 transition-transform" />
                            </Link>
                        </div>
                    </div>

                    {/* Indicador de hover */}
                    <div className={`h-3 bg-gradient-to-r from-${project.card_color}-200 to-${project.card_color}-600 transform scale-x-0 group-hover:scale-x-100 transition-transform duration-800 origin-left`}></div>
                </div>
            ))}
        </div>
    );
}