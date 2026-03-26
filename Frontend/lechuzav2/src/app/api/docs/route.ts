import {auth} from "@/auth"


interface FilterForDocuments {
    project_id: string
    page: number
    page_size: number
    name_filter: string
    code_filter: string
    revision_filter: string
    np_ttal_filter: string
    status_filter: string
    fecha_ingreso_filter: string
    correction_report_filter: string
}

export async function GET(request: Request) {

    const session = await auth()
    if (!session) {
        return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 })
    }

    const { searchParams } = new URL(request.url)
    
    const project_id = searchParams.get('projectId')
    const page = searchParams.get('page') || '1'
    const pageSize = searchParams.get('pageSize') || '10'
    const codeFilter = searchParams.get('codeFilter') || ''
    const nameFilter = searchParams.get('nameFilter') || ''
    const revisionFilter = searchParams.get('revisionFilter') || ''
    const npTtalFilter = searchParams.get('npTtalFilter') || ''
    const statusFilter = searchParams.get('statusFilter') || ''
    const fechaIngresoFilter = searchParams.get('fechaIngresoFilter') || ''
    const correctionReportFilter = searchParams.get('correctionReportFilter') || ''

    if (!project_id) {
        return new Response(JSON.stringify({ error: 'project_id is required' }), { status: 400 })
    }

    const filters: FilterForDocuments = {
        project_id,
        page: parseInt(page),
        page_size: parseInt(pageSize),
        code_filter: codeFilter,
        name_filter: nameFilter,
        revision_filter: revisionFilter,
        np_ttal_filter: npTtalFilter,
        status_filter: statusFilter,
        fecha_ingreso_filter: fechaIngresoFilter,
        correction_report_filter: correctionReportFilter
    };

    const response = await fetch(`${process.env.BACKEND_URL}/api/v1/documents/paginated_docs?${new URLSearchParams(filters as any)}`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${session.accessToken}`
        }
    });

    if (!response.ok) {
        const errorData = await response.json();
        return new Response(JSON.stringify({ error: errorData.message || 'Failed to fetch documents' }), { status: response.status });
    }
    const data = await response.json();
    console.log('Fetched documents:', data);
    return new Response(JSON.stringify(data), { status: 200 });
}
