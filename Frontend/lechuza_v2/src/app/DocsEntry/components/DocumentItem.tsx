import React, { ChangeEvent } from 'react';
import { DocumentData } from '../types/types';

interface DocumentItemProps {
    index: number;
    document: DocumentData;
    onChange: (index: number, e: ChangeEvent<HTMLInputElement>) => void;
}

export const DocumentItem: React.FC<DocumentItemProps> = ({ index, document, onChange }) => {
    return (
        <div className="bg-white border border-gray-200 rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow flex items-start gap-4">
            <div className="flex-none flex items-center justify-center bg-blue-100 text-blue-700 font-bold text-sm rounded-lg px-3 py-2 min-w-[2.5rem] h-fit mt-6">
                {index + 1}
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 flex-1">
                <div className="space-y-1">
                    <label className="block text-xs font-medium text-gray-500 uppercase">Código</label>
                    <input
                        type="text"
                        name="code"
                        value={document.code}
                        onChange={(e) => onChange(index, e)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-1 focus:ring-blue-500 focus:border-blue-500 outline-none text-sm"
                        placeholder="Cód. Doc"
                    />
                </div>
                <div className="space-y-1">
                    <label className="block text-xs font-medium text-gray-500 uppercase">Descripción</label>
                    <input
                        type="text"
                        name="description"
                        value={document.description}
                        onChange={(e) => onChange(index, e)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-1 focus:ring-blue-500 focus:border-blue-500 outline-none text-sm"
                        placeholder="Desc. Doc"
                    />
                </div>
                <div className="space-y-1">
                    <label className="block text-xs font-medium text-gray-500 uppercase">Revisión</label>
                    <input
                        type="text"
                        name="revision"
                        value={document.revision}
                        onChange={(e) => onChange(index, e)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-1 focus:ring-blue-500 focus:border-blue-500 outline-none text-sm"
                        placeholder="Rev"
                    />
                </div>
                <div className="space-y-1">
                    <label className="block text-xs font-medium text-gray-500 uppercase">Archivo</label>
                    <input
                        type="file"
                        name="file"
                        onChange={(e) => onChange(index, e)}
                        className="w-full text-xs text-gray-500 file:mr-2 file:py-1 file:px-2 file:rounded-md file:border-0 file:text-xs file:font-medium file:bg-gray-100 file:text-gray-700 hover:file:bg-gray-200"
                    />
                </div>
            </div>
        </div>
    );
};
