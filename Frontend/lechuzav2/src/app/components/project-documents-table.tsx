'use client'

import { useState, useMemo } from 'react'
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

interface Filters {
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

interface ProjectDocumentsTableProps {
    documents: Document[]
    isAdmin: boolean
    projectId: string
}

const ITEMS_PER_PAGE = 10

export default function ProjectDocumentsTable({
    documents,
    isAdmin,
    projectId
}: ProjectDocumentsTableProps) {
    const [currentPage, setCurrentPage] = useState(1)
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

    // Filtrar documentos
    const filteredDocuments = useMemo(() => {
        return documents.filter(doc => {
            return (
                doc.codigo.toLowerCase().includes(filters.codigo.toLowerCase()) &&
                doc.revision.toLowerCase().includes(filters.revision.toLowerCase()) &&
                doc.descripcion.toLowerCase().includes(filters.descripcion.toLowerCase()) &&
                (doc.comunicacion_ingreso || '').toLowerCase().includes(filters.comunicacion_ingreso.toLowerCase()) &&
                doc.fecha_ingreso.includes(filters.fecha_ingreso) &&
                (doc.calificacion || '').toLowerCase().includes(filters.calificacion.toLowerCase()) &&
                (doc.informe_ingenieria || '').toLowerCase().includes(filters.informe_ingenieria.toLowerCase()) &&
                (doc.fecha_informe || '').includes(filters.fecha_informe) &&
                (doc.comunicacion_egreso || '').toLowerCase().includes(filters.comunicacion_egreso.toLowerCase())
            )
        })
    }, [documents, filters])

    // Paginación
    const totalPages = Math.ceil(filteredDocuments.length / ITEMS_PER_PAGE)
    const startIndex = (currentPage - 1) * ITEMS_PER_PAGE
    const paginatedDocuments = filteredDocuments.slice(startIndex, startIndex + ITEMS_PER_PAGE)

    // Handlers
    const handleFilterChange = (field: keyof Filters, value: string) => {
        setFilters(prev => ({ ...prev, [field]: value }))
        setCurrentPage(1) // Reset to first page when filtering
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
        setCurrentPage(1)
    }

    const hasActiveFilters = Object.values(filters).some(filter => filter !== '')

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
                        Mostrando {paginatedDocuments.length} de {filteredDocuments.length} documento(s)
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