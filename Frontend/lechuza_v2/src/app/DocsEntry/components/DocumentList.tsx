import React, { ChangeEvent } from 'react';
import { DocumentData } from '../types/types';
import { DocumentItem } from './DocumentItem';

interface DocumentListProps {
    documents: DocumentData[];
    docCount: number;
    onCountChange: (e: ChangeEvent<HTMLInputElement>) => void;
    onDocumentChange: (index: number, e: ChangeEvent<HTMLInputElement>) => void;
}

export const DocumentList: React.FC<DocumentListProps> = ({ documents, docCount, onCountChange, onDocumentChange }) => {
    return (
        <section>
            <h2 className="text-xl font-semibold text-gray-800 border-b pb-2 mb-4">Documentos Adjuntos</h2>
            <div className="flex items-center space-x-4 mb-6 bg-gray-50 p-4 rounded-lg border border-gray-200">
                <label htmlFor="doc-count" className="font-medium text-gray-700">Cantidad de documentos a cargar:</label>
                <input
                    type="number"
                    id="doc-count"
                    min="0"
                    value={docCount}
                    onChange={onCountChange}
                    className="w-24 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all text-center font-bold text-lg"
                />
            </div>

            <div className="space-y-1">
                {documents.map((doc, index) => (
                    <DocumentItem
                        key={doc.id}
                        index={index}
                        document={doc}
                        onChange={onDocumentChange}
                    />
                ))}
                {documents.length === 0 && (
                    <div className="text-center py-10 text-gray-400 italic bg-gray-50 rounded-lg border border-dashed border-gray-300">
                        No hay documentos adjuntos. Ingrese una cantidad arriba.
                    </div>
                )}
            </div>
        </section>
    );
};
