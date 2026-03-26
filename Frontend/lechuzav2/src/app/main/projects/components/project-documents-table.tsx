'use client'

import { Document, Filters, ProjectDocumentsTableProps } from '../interfaces'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Badge } from '@/components/ui/badge'
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from '@/components/ui/table'
import {
    ChevronLeft,
    ChevronRight,
    Edit,
    ExternalLink,
    X
} from 'lucide-react'
import Link from 'next/link'


const ITEMS_PER_PAGE = 10


export default function ProjectDocumentsTable({
    documents,
    isAdmin,
    projectId
}: ProjectDocumentsTableProps) {
    const [currentPage, setCurrentPage] = useState(1)
    const [documentsFromAPI, setDocumentsFromAPI] = useState<Document[]>([])
    const [filters, setFilters] = useState<Filters>({
        codigo: '',
        revision: '',
        descripcion: '',
        comunicacion_ingreso: '',
        fecha_ingreso: '',
        calificacion: '',
        informe_ingenieria: '',
        fecha_informe: '',
        comunicacion_egreso: ''
    })

    const hasActiveFilters = Object.values(filters).some(filter => filter !== '')
    const documentsToDisplay = hasActiveFilters ? documentsFromAPI : documents

    // Paginación
    const totalPages = Math.ceil(documentsToDisplay.length / ITEMS_PER_PAGE)
    const startIndex = (currentPage - 1) * ITEMS_PER_PAGE
    const paginatedDocuments = documentsToDisplay.slice(startIndex, startIndex + ITEMS_PER_PAGE)

    // Handlers
    const handleFilterChange = async (field: keyof Filters, value: string) => {
        const nextFilters = { ...filters, [field]: value }
        setFilters(nextFilters)
        setCurrentPage(1) // Reset to first page when filtering

        const hasAnyFilter = Object.values(nextFilters).some(filter => filter !== '')
        if (!hasAnyFilter) {
            setDocumentsFromAPI([])
            return
        }

        const params = new URLSearchParams({
            projectId,
            page: '1',
            pageSize: ITEMS_PER_PAGE.toString(),
            nameFilter: nextFilters.descripcion,
            codeFilter: nextFilters.codigo,
            revisionFilter: nextFilters.revision,
            npTtalFilter: nextFilters.comunicacion_ingreso,
            statusFilter: nextFilters.calificacion,
            fechaIngresoFilter: nextFilters.fecha_ingreso,
            correctionReportFilter: nextFilters.informe_ingenieria,
        })

        const filteredDocs = await fetch(`/api/docs?${params.toString()}`)
        if (!filteredDocs.ok) {
            setDocumentsFromAPI([])
            return
        }

        const data = await filteredDocs.json()
        const docs = Array.isArray(data) ? data : data.documents
        setDocumentsFromAPI(Array.isArray(docs) ? docs : [])
    }

    const clearFilters = () => {
        setFilters({
            codigo: '',
            revision: '',
            descripcion: '',
            comunicacion_ingreso: '',
            fecha_ingreso: '',
            calificacion: '',
            informe_ingenieria: '',
            fecha_informe: '',
            comunicacion_egreso: ''
        })
        setDocumentsFromAPI([])
        setCurrentPage(1)
    }

    const formatDate = (dateString: string) => {
        if (!dateString) return '-'
        try {
            return new Date(dateString).toLocaleDateString('es-ES')
        } catch {
            return dateString
        }
    }

    const getFileUrl = (filePath?: string) => {
        if (!filePath) return null
        return `${process.env.NEXT_PUBLIC_BACKEND_URL}/files/${filePath}`
    }

    const getCalificacionBadgeVariant = (calificacion?: string) => {
        switch (calificacion?.toLowerCase()) {
            case 'aprobado':
                return 'default'
            case 'observado':
                return 'destructive'
            case 'en revision':
                return 'secondary'
            default:
                return 'outline'
        }
    }

    const getFileNameFromPath = (filePath?: string) => {
        if (!filePath) return '-'
        // Extraer solo el nombre del archivo sin la ruta
        const fileName = filePath.split('/').pop() || filePath
        // Remover la extensión si existe
        return fileName.replace(/\.[^/.]+$/, '')
    }

    return (
        <div className="space-y-4">
            {/* Toolbar superior */}
            <div className="flex items-center justify-between">
                <div className="flex items-center gap-4">
                    <div className="text-sm text-muted-foreground">
                        Mostrando {paginatedDocuments.length} de {documentsToDisplay.length} documento(s)
                        {hasActiveFilters && ` (filtrados de ${documents.length} total)`}
                    </div>
                    {hasActiveFilters && (
                        <Button
                            variant="outline"
                            size="sm"
                            onClick={clearFilters}
                            className="flex items-center gap-2"
                        >
                            <X className="h-4 w-4" />
                            Limpiar filtros
                        </Button>
                    )}
                </div>
            </div>

            {/* Tabla con filtros integrados */}
            <div className="border rounded-lg">
                <Table>
                    <TableHeader>
                        <TableRow>
                            <TableHead>Código</TableHead>
                            <TableHead>Revisión</TableHead>
                            <TableHead className="w-80">Descripción</TableHead>
                            <TableHead>Comunicación de Ingreso</TableHead>
                            <TableHead>Fecha de Ingreso</TableHead>
                            <TableHead>Calificación</TableHead>
                            <TableHead>Informe de Ingeniería</TableHead>
                            <TableHead>Fecha de Informe</TableHead>
                            <TableHead>Comunicación de Egreso</TableHead>
                            {isAdmin && <TableHead>Acciones</TableHead>}
                        </TableRow>
                        {/* Fila de filtros integrados */}
                        <TableRow>
                            <TableHead className="p-2">
                                <Input
                                    placeholder="Filtrar..."
                                    value={filters.codigo}
                                    onChange={(e) => handleFilterChange('codigo', e.target.value)}
                                    className="h-8 text-xs"
                                />
                            </TableHead>
                            <TableHead className="p-2">
                                <Input
                                    placeholder="Filtrar..."
                                    value={filters.revision}
                                    onChange={(e) => handleFilterChange('revision', e.target.value)}
                                    className="h-8 text-xs"
                                />
                            </TableHead>
                            <TableHead className="p-2 w-80">
                                <Input
                                    placeholder="Filtrar..."
                                    value={filters.descripcion}
                                    onChange={(e) => handleFilterChange('descripcion', e.target.value)}
                                    className="h-8 text-xs"
                                />
                            </TableHead>
                            <TableHead className="p-2">
                                <Input
                                    placeholder="Filtrar..."
                                    value={filters.comunicacion_ingreso}
                                    onChange={(e) => handleFilterChange('comunicacion_ingreso', e.target.value)}
                                    className="h-8 text-xs"
                                />
                            </TableHead>
                            <TableHead className="p-2">
                                <Input
                                    type="date"
                                    value={filters.fecha_ingreso}
                                    onChange={(e) => handleFilterChange('fecha_ingreso', e.target.value)}
                                    className="h-8 text-xs"
                                />
                            </TableHead>
                            <TableHead className="p-2">
                                <Input
                                    placeholder="Filtrar..."
                                    value={filters.calificacion}
                                    onChange={(e) => handleFilterChange('calificacion', e.target.value)}
                                    className="h-8 text-xs"
                                />
                            </TableHead>
                            <TableHead className="p-2">
                                <Input
                                    placeholder="Filtrar..."
                                    value={filters.informe_ingenieria}
                                    onChange={(e) => handleFilterChange('informe_ingenieria', e.target.value)}
                                    className="h-8 text-xs"
                                />
                            </TableHead>
                            <TableHead className="p-2">
                                <Input
                                    type="date"
                                    value={filters.fecha_informe}
                                    onChange={(e) => handleFilterChange('fecha_informe', e.target.value)}
                                    className="h-8 text-xs"
                                />
                            </TableHead>
                            <TableHead className="p-2">
                                <Input
                                    placeholder="Filtrar..."
                                    value={filters.comunicacion_egreso}
                                    onChange={(e) => handleFilterChange('comunicacion_egreso', e.target.value)}
                                    className="h-8 text-xs"
                                />
                            </TableHead>
                            {isAdmin && <TableHead></TableHead>}
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {paginatedDocuments.length === 0 ? (
                            <TableRow>
                                <TableCell
                                    colSpan={isAdmin ? 10 : 9}
                                    className="h-24 text-center text-muted-foreground"
                                >
                                    No se encontraron documentos.
                                </TableCell>
                            </TableRow>
                        ) : (
                            paginatedDocuments.map((document) => (
                                <TableRow key={document.id}>
                                    <TableCell className="font-mono">{document.codigo}</TableCell>
                                    <TableCell className="font-mono">{document.revision}</TableCell>
                                    <TableCell className="w-80">
                                        <Link
                                            href={document.document_file ? getFileUrl(document.document_file) || '#' : '#'}
                                            target="_blank"
                                            className="flex items-start gap-2 text-sm text-blue-600 hover:underline"
                                        >
                                            <span className="whitespace-normal break-words leading-relaxed">{document.descripcion}</span>
                                        </Link>
                                    </TableCell>
                                    <TableCell>{document.comunicacion_ingreso || '-'}</TableCell>
                                    <TableCell>{formatDate(document.fecha_ingreso)}</TableCell>
                                    <TableCell>
                                        {document.calificacion ? (
                                            <Badge variant={getCalificacionBadgeVariant(document.calificacion)}>
                                                {document.calificacion}
                                            </Badge>
                                        ) : (
                                            '-'
                                        )}
                                    </TableCell>
                                    <TableCell>
                                        <div className="flex items-center gap-2">
                                            <span className="text-sm">
                                                {getFileNameFromPath(document.informe_ingenieria)}
                                            </span>
                                            {document.informe_ingenieria && (
                                                <Button
                                                    variant="ghost"
                                                    size="sm"
                                                    asChild
                                                    className="h-6 w-6 p-0"
                                                >
                                                    <a
                                                        href={getFileUrl(document.informe_ingenieria) || undefined}
                                                        target="_blank"
                                                        rel="noopener noreferrer"
                                                    >
                                                        <ExternalLink className="h-3 w-3" />
                                                    </a>
                                                </Button>
                                            )}
                                        </div>
                                    </TableCell>
                                    <TableCell>{formatDate(document.fecha_informe || '')}</TableCell>
                                    <TableCell>{document.comunicacion_egreso || '-'}</TableCell>
                                    {isAdmin && (
                                        <TableCell>
                                            <Button
                                                variant="ghost"
                                                size="sm"
                                                className="h-8 w-8 p-0"
                                                onClick={() => {
                                                    // TODO: Implementar edición
                                                    console.log('Edit document:', document.id)
                                                }}
                                            >
                                                <Edit className="h-4 w-4" />
                                            </Button>
                                        </TableCell>
                                    )}
                                </TableRow>
                            ))
                        )}
                    </TableBody>
                </Table>
            </div>

            {/* Paginación */}
            {totalPages > 1 && (
                <div className="flex items-center justify-between">
                    <div className="text-sm text-muted-foreground">
                        Página {currentPage} de {totalPages}
                    </div>
                    <div className="flex items-center gap-2">
                        <Button
                            variant="outline"
                            size="sm"
                            onClick={() => setCurrentPage(Math.max(1, currentPage - 1))}
                            disabled={currentPage === 1}
                        >
                            <ChevronLeft className="h-4 w-4" />
                            Anterior
                        </Button>
                        <Button
                            variant="outline"
                            size="sm"
                            onClick={() => setCurrentPage(Math.min(totalPages, currentPage + 1))}
                            disabled={currentPage === totalPages}
                        >
                            Siguiente
                            <ChevronRight className="h-4 w-4" />
                        </Button>
                    </div>
                </div>
            )}
        </div>
    )
}