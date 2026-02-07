import React, { ChangeEvent } from 'react';
import { TtalData } from '../types/types';

interface TtalFormProps {
    ttal: TtalData;
    onChange: (e: ChangeEvent<HTMLInputElement>) => void;
}

export const TtalForm: React.FC<TtalFormProps> = ({ ttal, onChange }) => {
    return (
        <section>
            <h2 className="text-xl font-semibold text-gray-800 border-b pb-2 mb-4">Información Ttal</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="space-y-2">
                    <label htmlFor="ttal-code" className="block text-sm font-medium text-gray-700">Código</label>
                    <input
                        type="text"
                        id="ttal-code"
                        name="code"
                        value={ttal.code}
                        onChange={onChange}
                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all"
                        placeholder="Ej. TT-001"
                    />
                </div>
                <div className="space-y-2">
                    <label htmlFor="ttal-desc" className="block text-sm font-medium text-gray-700">Descripción</label>
                    <input
                        type="text"
                        id="ttal-desc"
                        name="description"
                        value={ttal.description}
                        onChange={onChange}
                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all"
                        placeholder="Descripción del Ttal"
                    />
                </div>
                <div className="space-y-2">
                    <label htmlFor="ttal-file" className="block text-sm font-medium text-gray-700">Archivo</label>
                    <input
                        type="file"
                        id="ttal-file"
                        name="file"
                        onChange={onChange}
                        className="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 transition-all"
                    />
                </div>
            </div>
        </section>
    );
};
