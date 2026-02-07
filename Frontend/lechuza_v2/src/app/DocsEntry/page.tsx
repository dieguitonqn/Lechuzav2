'use client';

import React from 'react';
import { TtalForm } from './components/TtalForm';
import { DocumentList } from './components/DocumentList';
import { useDocsEntry } from './components/useDocsEntry';

function DocsEntry() {
    const {
        ttal,
        docCount,
        documents,
        handleTtalChange,
        handleDocCountChange,
        handleDocumentChange,
        handleSubmit,
    } = useDocsEntry();

    return (
        <div className="min-h-screen bg-gray-50 p-8 font-sans text-gray-900">
            <div className="max-w-6xl mx-auto bg-white shadow-xl rounded-2xl overflow-hidden">
                <div className="bg-blue-600 p-6">
                    <h1 className="text-3xl font-bold text-white">Ingreso de Documentos</h1>
                    <p className="text-blue-100 mt-2">Complete la información del Ttal y adjunte los documentos necesarios.</p>
                </div>

                <form onSubmit={handleSubmit} className="p-8 space-y-8">
                    <TtalForm ttal={ttal} onChange={handleTtalChange} />

                    <DocumentList
                        documents={documents}
                        docCount={docCount}
                        onCountChange={handleDocCountChange}
                        onDocumentChange={handleDocumentChange}
                    />

                    <div className="pt-6 border-t border-gray-200 flex justify-end">
                        <button
                            type="submit"
                            className="px-8 py-3 bg-blue-600 text-white font-semibold rounded-lg shadow-lg hover:bg-blue-700 focus:ring-4 focus:ring-blue-300 transition-all transform hover:-translate-y-0.5"
                        >
                            Guardar Todo
                        </button>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default DocsEntry;