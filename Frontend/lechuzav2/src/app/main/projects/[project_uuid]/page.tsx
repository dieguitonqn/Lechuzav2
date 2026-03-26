import { auth } from "@/auth"
import ProjectDocumentsTable from '@/app/main/projects/components/project-documents-table'
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
    // await new Promise(resolve => setTimeout(resolve, 500)) // Simular delay de red
    
    // const mockProject: Project = {
    //   id: projectId,
    //   name: "Construcción Torre Empresarial Plaza Central",
    //   code: "TEC-2024-001",
    //   contractor: "Constructora Meridian S.A."
    // }
    
    // console.log('✅ Proyecto simulado obtenido:', mockProject)
    // return mockProject

    // 🚧  CÓDIGO REAL - Descomentar cuando el backend esté listo
    const url = `${process.env.BACKEND_URL}/api/v1/documents/paginated_docs?project_id=${projectId}`
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
    //
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
      },
      {
        id: '7',
        codigo: 'MEM-CAL-007',
        revision: 'Rev-A',
        descripcion: 'Memoria de Cálculo Estructural',
        document_file: 'documents/MEM-CAL-007-A.pdf',
        fecha_ingreso: '2024-02-10T09:30:00Z',
        calificacion: 'Aprobado',
        informe_ingenieria: 'informes/INF-MEM-007.pdf',
        fecha_informe: '2024-02-15T11:00:00Z',
        comunicacion_ingreso: 'COM-007-2024',
        comunicacion_egreso: 'COM-OUT-007-2024',
        project_id: projectId
      },
      {
        id: '8',
        codigo: 'DWG-HID-008',
        revision: 'Rev-B',
        descripcion: 'Planos de Instalaciones Hidráulicas',
        document_file: 'documents/DWG-HID-008-B.pdf',
        fecha_ingreso: '2024-02-12T14:20:00Z',
        calificacion: 'En Revision',
        informe_ingenieria: '',
        fecha_informe: '',
        comunicacion_ingreso: 'COM-008-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '9',
        codigo: 'ESP-CON-009',
        revision: 'Rev-A',
        descripcion: 'Especificaciones de Construcción',
        document_file: 'documents/ESP-CON-009-A.pdf',
        fecha_ingreso: '2024-02-14T10:45:00Z',
        calificacion: 'Aprobado',
        informe_ingenieria: 'informes/INF-CON-009.pdf',
        fecha_informe: '2024-02-18T16:30:00Z',
        comunicacion_ingreso: 'COM-009-2024',
        comunicacion_egreso: 'COM-OUT-009-2024',
        project_id: projectId
      },
      {
        id: '10',
        codigo: 'PLN-ELE-010',
        revision: 'Rev-C',
        descripcion: 'Planos Eléctricos Nivel 6-10',
        document_file: 'documents/PLN-ELE-010-C.pdf',
        fecha_ingreso: '2024-02-16T08:15:00Z',
        calificacion: 'Observado',
        informe_ingenieria: 'informes/INF-ELE-010.pdf',
        fecha_informe: '2024-02-20T12:00:00Z',
        comunicacion_ingreso: 'COM-010-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '11',
        codigo: 'DET-ARQ-011',
        revision: 'Rev-A',
        descripcion: 'Detalles Arquitectónicos Especiales',
        document_file: 'documents/DET-ARQ-011-A.pdf',
        fecha_ingreso: '2024-02-18T13:30:00Z',
        calificacion: '',
        informe_ingenieria: '',
        fecha_informe: '',
        comunicacion_ingreso: 'COM-011-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '12',
        codigo: 'CAL-SIS-012',
        revision: 'Rev-A',
        descripcion: 'Cálculos Sísmicos y Análisis Dinámico',
        document_file: 'documents/CAL-SIS-012-A.pdf',
        fecha_ingreso: '2024-02-20T11:00:00Z',
        calificacion: 'Aprobado',
        informe_ingenieria: 'informes/INF-SIS-012.pdf',
        fecha_informe: '2024-02-24T15:45:00Z',
        comunicacion_ingreso: 'COM-012-2024',
        comunicacion_egreso: 'COM-OUT-012-2024',
        project_id: projectId
      },
      {
        id: '13',
        codigo: 'PLN-TOP-013',
        revision: 'Rev-A',
        descripcion: 'Levantamiento Topográfico del Terreno',
        document_file: 'documents/PLN-TOP-013-A.pdf',
        fecha_ingreso: '2024-02-22T09:15:00Z',
        calificacion: 'Aprobado',
        informe_ingenieria: 'informes/INF-TOP-013.pdf',
        fecha_informe: '2024-02-26T16:45:00Z',
        comunicacion_ingreso: 'COM-013-2024',
        comunicacion_egreso: 'COM-OUT-013-2024',
        project_id: projectId
      },
      {
        id: '14',
        codigo: 'EST-GEO-014',
        revision: 'Rev-B',
        descripcion: 'Estudio Geotécnico del Suelo',
        document_file: 'documents/EST-GEO-014-B.pdf',
        fecha_ingreso: '2024-02-25T14:30:00Z',
        calificacion: 'En Revision',
        informe_ingenieria: '',
        fecha_informe: '',
        comunicacion_ingreso: 'COM-014-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '15',
        codigo: 'PLN-SAN-015',
        revision: 'Rev-A',
        descripcion: 'Planos de Red Sanitaria y Aguas Lluvias',
        document_file: 'documents/PLN-SAN-015-A.pdf',
        fecha_ingreso: '2024-02-28T11:20:00Z',
        calificacion: 'Observado',
        informe_ingenieria: 'informes/INF-SAN-015.pdf',
        fecha_informe: '2024-03-02T10:30:00Z',
        comunicacion_ingreso: 'COM-015-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '16',
        codigo: 'ESP-MAT-016',
        revision: 'Rev-A',
        descripcion: 'Especificaciones de Materiales',
        document_file: 'documents/ESP-MAT-016-A.pdf',
        fecha_ingreso: '2024-03-01T15:45:00Z',
        calificacion: 'Aprobado',
        informe_ingenieria: 'informes/INF-MAT-016.pdf',
        fecha_informe: '2024-03-05T09:15:00Z',
        comunicacion_ingreso: 'COM-016-2024',
        comunicacion_egreso: 'COM-OUT-016-2024',
        project_id: projectId
      },
      {
        id: '17',
        codigo: 'DET-ESC-017',
        revision: 'Rev-C',
        descripcion: 'Detalles de Escaleras de Emergencia',
        document_file: 'documents/DET-ESC-017-C.pdf',
        fecha_ingreso: '2024-03-03T12:00:00Z',
        calificacion: '',
        informe_ingenieria: '',
        fecha_informe: '',
        comunicacion_ingreso: 'COM-017-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '18',
        codigo: 'PLN-CLI-018',
        revision: 'Rev-A',
        descripcion: 'Planos de Sistema de Climatización',
        document_file: 'documents/PLN-CLI-018-A.pdf',
        fecha_ingreso: '2024-03-05T08:30:00Z',
        calificacion: 'En Revision',
        informe_ingenieria: '',
        fecha_informe: '',
        comunicacion_ingreso: 'COM-018-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '19',
        codigo: 'CAL-VIE-019',
        revision: 'Rev-B',
        descripcion: 'Cálculo de Resistencia al Viento',
        document_file: 'documents/CAL-VIE-019-B.pdf',
        fecha_ingreso: '2024-03-07T16:20:00Z',
        calificacion: 'Aprobado',
        informe_ingenieria: 'informes/INF-VIE-019.pdf',
        fecha_informe: '2024-03-10T14:00:00Z',
        comunicacion_ingreso: 'COM-019-2024',
        comunicacion_egreso: 'COM-OUT-019-2024',
        project_id: projectId
      },
      {
        id: '20',
        codigo: 'MAN-OPR-020',
        revision: 'Rev-A',
        descripcion: 'Manual de Operación y Mantenimiento',
        document_file: 'documents/MAN-OPR-020-A.pdf',
        fecha_ingreso: '2024-03-09T13:45:00Z',
        calificacion: 'Observado',
        informe_ingenieria: 'informes/INF-OPR-020.pdf',
        fecha_informe: '2024-03-12T11:30:00Z',
        comunicacion_ingreso: 'COM-020-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '21',
        codigo: 'PLN-SEG-021',
        revision: 'Rev-A',
        descripcion: 'Planos de Sistema de Seguridad y CCTV',
        document_file: 'documents/PLN-SEG-021-A.pdf',
        fecha_ingreso: '2024-03-11T10:15:00Z',
        calificacion: '',
        informe_ingenieria: '',
        fecha_informe: '',
        comunicacion_ingreso: 'COM-021-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '22',
        codigo: 'EST-IMP-022',
        revision: 'Rev-B',
        descripcion: 'Estudio de Impacto Ambiental',
        document_file: 'documents/EST-IMP-022-B.pdf',
        fecha_ingreso: '2024-03-13T09:00:00Z',
        calificacion: 'Aprobado',
        informe_ingenieria: 'informes/INF-IMP-022.pdf',
        fecha_informe: '2024-03-15T16:20:00Z',
        comunicacion_ingreso: 'COM-022-2024',
        comunicacion_egreso: 'COM-OUT-022-2024',
        project_id: projectId
      },
      {
        id: '23',
        codigo: 'PLN-PAR-023',
        revision: 'Rev-A',
        descripcion: 'Planos de Estacionamiento Subterráneo',
        document_file: 'documents/PLN-PAR-023-A.pdf',
        fecha_ingreso: '2024-03-15T14:30:00Z',
        calificacion: 'En Revision',
        informe_ingenieria: '',
        fecha_informe: '',
        comunicacion_ingreso: 'COM-023-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '24',
        codigo: 'DET-FAS-024',
        revision: 'Rev-C',
        descripcion: 'Detalles de Fachada Ventilada',
        document_file: 'documents/DET-FAS-024-C.pdf',
        fecha_ingreso: '2024-03-17T11:45:00Z',
        calificacion: 'Observado',
        informe_ingenieria: 'informes/INF-FAS-024.pdf',
        fecha_informe: '2024-03-19T13:15:00Z',
        comunicacion_ingreso: 'COM-024-2024',
        comunicacion_egreso: '',
        project_id: projectId
      },
      {
        id: '25',
        codigo: 'PRE-OBR-025',
        revision: 'Rev-A',
        descripcion: 'Presupuesto General de la Obra',
        document_file: 'documents/PRE-OBR-025-A.pdf',
        fecha_ingreso: '2024-03-19T15:00:00Z',
        calificacion: 'Aprobado',
        informe_ingenieria: 'informes/INF-OBR-025.pdf',
        fecha_informe: '2024-03-21T10:45:00Z',
        comunicacion_ingreso: 'COM-025-2024',
        comunicacion_egreso: 'COM-OUT-025-2024',
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
