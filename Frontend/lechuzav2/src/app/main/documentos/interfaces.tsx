import { UUID } from "crypto";

export interface Project {
    id: string,
    descripcion: string,
    fecha_fin: string | null,
    emails_notificacion: string | null,
    contrato: string | null,
    nombre: string,
    codigo: string,
    card_color: string,
    fecha_inicio: string,
    estado_proyecto: string,
    company_id: string | null,
    companies: Company[] | null,
    contrato_url: string | null
}

export interface Company {
    id: string,
    nombre: string,
    codigo: string | null
}

export interface DocsIn{
    codigo:string;
    revision:string;
    file:File;
    descripcion:string;
}

export interface IngresoDocs {
    obra_id: string;
    obra_codigo:string;
    obra_descripcion:string;
    np_ttal:string;
    np_ttal_file:File;
    np_ttal_descripcion:string;
    documentos:DocsIn[];
}