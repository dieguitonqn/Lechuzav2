import { notFound } from 'next/navigation'
import { auth } from "@/auth"
import ProjectDocumentsTable from '@/app/components/project-documents-table'
import { Button } from '@/components/ui/button'

// Tipos para los datos
interface Project {
  id: string
  name: string
  code: string
  contractor: string
}

interface Document {
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

interface User {
  id: string
  role: string
  name: string
}

// Función para obtener datos del proyecto
async function getProjectData(projectId: string): Promise<Project | null> {
  try {
    console.log('🔍 Obteniendo datos del proyecto:', projectId)
    const session = await auth()
    
    if (!session?.accessToken) {
      console.log('❌ Sin token de acceso')
      return null
    }

    // 🚧 DATOS SIMULADOS - Comentar cuando el backend esté listo
    await new Promise(resolve => setTimeout(resolve, 500)) // Simular delay de red
    
    const mockProject: Project = {
      id: projectId,
      name: "Construcción Torre Empresarial Plaza Central",
      code: "TEC-2024-001",
      contractor: "Constructora Meridian S.A."
    }
    
    console.log('✅ Proyecto simulado obtenido:', mockProject)
    return mockProject

    /* 🚧 CÓDIGO REAL - Descomentar cuando el backend esté listo
    const url = `${process.env.BACKEND_URL}/api/v1/projects/${projectId}`
    console.log('📡 Fetching:', url)

    const response = await fetch(url, {
      headers: {
        'Authorization': `Bearer ${session.accessToken}`,
        'Content-Type': 'application/json',
      },
      cache: 'no-store', // Para SSR real
    })

    console.log('📡 Response status:', response.status)

    if (!response.ok) {
      console.log('❌ Response not OK:', await response.text())
      return null
    }

    const data = await response.json()
    console.log('✅ Proyecto obtenido:', data)
    return data
    */
  } catch (error) {
    console.error('💥 Error fetching project:', error)
    return null
  }
}

// Función para obtener documentos del proyecto
async function getProjectDocuments(projectId: string): Promise<Document[]> {
  try {
    console.log('📄 Obteniendo documentos del proyecto:', projectId)
    const session = await auth()
    
    if (!session?.accessToken) {
      return []
    }

    // 🚧 DATOS SIMULADOS - Comentar cuando el backend esté listo
    await new Promise(resolve => setTimeout(resolve, 300)) // Simular delay de red
    
    const mockDocuments: Document[] = [
      {
        id: '1',
        codigo: 'PLN-ARQ-001',
        revision: 'Rev-A',
        descripcion: 'Planos Arquitectónicos Nivel 1-5',
        document_file: 'documents/PLN-ARQ-001-A.pdf',
        fecha_ingreso: '2024-01-15T10:30:00Z',
        calificacion: 'Aprobado',
        informe_ingenieria: 'informes/INF-ARQ-001.pdf',
        fecha_informe: '2024-01-20T14:15:00Z',
        comunicacion_ingreso: 'COM-001-2024',
        comunicacion_egreso: 'COM-OUT-001-2024',
        project_id: projectId
      },
      {
        id: '2',
        codigo: 'PLN-EST-002',
        revision: 'Rev-B',
        descripcion: 'Planos Estructurales Fundaciones',
        document_file: 'documents/PLN-EST-002-B.pdf',
        fecha_ingreso: '2024-01-18T09:00:00Z',
        calificacion: 'Observado',
        informe_ingenieria: 'informes/INF-EST-002.pdf',
        fecha_informe: '2024-01-25T16:30:00Z',
        comunicacion_ingreso: 'COM-002-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '3',
        codigo: 'PLN-MEP-003',
        revision: 'Rev-A',
        descripcion: 'Planos de Instalaciones Mecánicas, Eléctricas y Plomería',
        document_file: 'documents/PLN-MEP-003-A.pdf',
        fecha_ingreso: '2024-01-22T11:45:00Z',
        calificacion: 'En Revision',
        informe_ingenieria: '',
        fecha_informe: '',
        comunicacion_ingreso: 'COM-003-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '4',
        codigo: 'ESP-TEC-004',
        revision: 'Rev-A',
        descripcion: 'Especificaciones Técnicas Generales',
        document_file: 'documents/ESP-TEC-004-A.pdf',
        fecha_ingreso: '2024-01-25T13:20:00Z',
        calificacion: 'Aprobado',
        informe_ingenieria: 'informes/INF-TEC-004.pdf',
        fecha_informe: '2024-01-30T10:00:00Z',
        comunicacion_ingreso: 'COM-004-2024',
        comunicacion_egreso: 'COM-OUT-004-2024',
        project_id: projectId
      },
      {
        id: '5',
        codigo: 'DET-CON-005',
        revision: 'Rev-C',
        descripcion: 'Detalles Constructivos Fachada Principal',
        document_file: 'documents/DET-CON-005-C.pdf',
        fecha_ingreso: '2024-02-01T08:30:00Z',
        calificacion: 'Observado',
        informe_ingenieria: 'informes/INF-CON-005.pdf',
        fecha_informe: '2024-02-05T15:45:00Z',
        comunicacion_ingreso: 'COM-005-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '6',
        codigo: 'CAL-EST-006',
        revision: 'Rev-A',
        descripcion: 'Cálculos Estructurales Vigas y Columnas',
        document_file: 'documents/CAL-EST-006-A.pdf',
        fecha_ingreso: '2024-02-08T12:15:00Z',
        calificacion: '',
        informe_ingenieria: '',
        fecha_informe: '',
        comunicacion_ingreso: 'COM-006-2024',
        comunicacion_egreso: '',
        project_id: projectId
      }
    ]
    
    console.log('✅ Documentos simulados obtenidos:', mockDocuments.length)
    return mockDocuments

    /* 🚧 CÓDIGO REAL - Descomentar cuando el backend esté listo
    const response = await fetch(`${process.env.BACKEND_URL}/api/v1/projects/${projectId}/documents`, {
      headers: {
        'Authorization': `Bearer ${session.accessToken}`,
        'Content-Type': 'application/json',
      },
      cache: 'no-store', // Para SSR real
    })

    if (!response.ok) {
      return []
    }

    return await response.json()
    */
  } catch (error) {
    console.error('Error fetching documents:', error)
    return []
  }
}

interface Props {
  params: Promise<{
    project_uuid: string
  }>
}

export default async function ProjectDocumentsPage({ params }: Props) {
  // Await params antes de usar sus propiedades
  const { project_uuid } = await params
  console.log('🔍 Accediendo a proyecto:', project_uuid)
  
  const session = await auth()
  console.log('🔑 Sesión obtenida:', !!session)
  
  if (!session) {
    console.log('❌ Sin sesión, redirigiendo')
    return (
      <div className="container mx-auto py-8">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-destructive">Acceso Denegado</h1>
          <p className="text-muted-foreground mt-2">Debes iniciar sesión para ver esta página.</p>
        </div>
      </div>
    )
  }

  console.log('📡 Obteniendo datos del proyecto...')
  // Obtener datos del proyecto y documentos en paralelo
  const [project, documents] = await Promise.all([
    getProjectData(project_uuid),
    getProjectDocuments(project_uuid)
  ])

  console.log('📋 Proyecto obtenido:', !!project)
  console.log('📄 Documentos obtenidos:', documents.length)

  if (!project) {
    console.log('❌ Proyecto no encontrado, mostrando 404')
    
    // Página temporal para debug en lugar de 404
    return (
      <div className="container mx-auto py-8">
        <div className="text-center space-y-4">
          <h1 className="text-2xl font-bold text-destructive">Proyecto no encontrado</h1>
          <p className="text-muted-foreground">UUID del proyecto: {project_uuid}</p>
          <p className="text-sm text-muted-foreground">
            Backend URL: {process.env.BACKEND_URL}
          </p>
          <div className="text-left max-w-md mx-auto">
            <h3 className="font-semibold mb-2">Debug info:</h3>
            <ul className="text-sm text-muted-foreground space-y-1">
              <li>✅ Sesión autenticada</li>
              <li>❌ Proyecto no encontrado en API</li>
              <li>🔍 Revisar logs del servidor para más detalles</li>
            </ul>
          </div>
        </div>
      </div>
    )
    // notFound()
  }

  const user: User = {
    id: String(session.user?.id) || '1',
    role: session.user?.role || 'admin', // 🚧 SIMULADO - Cambiar a 'user' para ver vista normal
    name: session.user?.name || 'Usuario Demo'
  }

  const isAdmin = user.role === 'admin' || user.role === 'supervisor'

  return (
    <div className="container mx-auto py-8 space-y-8">
      {/* Header del proyecto */}
      <div className="border-b pb-6">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div>
            <h1 className="text-3xl font-bold text-foreground">{project.name}</h1>
            <div className="flex flex-wrap gap-4 mt-2 text-sm text-muted-foreground">
              <span>
                <strong>Código:</strong> {project.code}
              </span>
              <span>
                <strong>Contratista:</strong> {project.contractor}
              </span>
            </div>
          </div>
          
          {isAdmin && (
            <div className="flex gap-2">
              <Button>
                Agregar Documento
              </Button>
            </div>
          )}
        </div>
      </div>

      {/* Tabla de documentos */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-semibold">Documentos del Proyecto</h2>
          <div className="text-sm text-muted-foreground">
            {documents.length} documento{documents.length !== 1 ? 's' : ''} total{documents.length !== 1 ? 'es' : ''}
          </div>
        </div>
        
        <ProjectDocumentsTable 
          documents={documents} 
          isAdmin={isAdmin}
          projectId={project_uuid}
        />
      </div>
    </div>
  )
}

// Metadatos dinámicos para la página
export async function generateMetadata({ params }: Props) {
  const { project_uuid } = await params
  const project = await getProjectData(project_uuid)
  
  return {
    title: project ? `${project.name} - Documentos` : 'Proyecto no encontrado',
    description: project ? `Documentos del proyecto ${project.name} (${project.code})` : 'Proyecto no encontrado'
  }
}
