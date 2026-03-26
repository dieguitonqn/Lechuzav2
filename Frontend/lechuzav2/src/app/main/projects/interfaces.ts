
export interface Document {
    id: string
    codigo: string
    revision: string
    descripcion: string
    document_file?: string
    fecha_ingreso: string
    calificacion?: string
    informe_ingenieria?: string
    fecha_informe?: string
    comunicacion_ingreso?: string
    comunicacion_egreso?: string
    project_id: string
}

export interface Filters {
    codigo: string
    revision: string
    descripcion: string
    comunicacion_ingreso: string
    fecha_ingreso: string
    calificacion: string
    informe_ingenieria: string
    fecha_informe: string
    comunicacion_egreso: string
}

export interface ProjectDocumentsTableProps {
    documents: Document[]
    isAdmin: boolean
    projectId: string
}