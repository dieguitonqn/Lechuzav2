export interface Project 
     {
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