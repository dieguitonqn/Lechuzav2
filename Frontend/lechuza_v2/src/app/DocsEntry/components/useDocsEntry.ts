import { useState, ChangeEvent, FormEvent } from 'react';
import { TtalData, DocumentData } from '../types/types';
import { DocsEntryRepository } from '../api/DocsEntryRepository';

export const useDocsEntry = () => {
    const [ttal, setTtal] = useState<TtalData>({
        code: '',
        description: '',
        file: null,
    });

    const [docCount, setDocCount] = useState<number>(0);
    const [documents, setDocuments] = useState<DocumentData[]>([]);

    const handleTtalChange = (e: ChangeEvent<HTMLInputElement>) => {
        const { name, value, files } = e.target;
        if (name === 'file') {
            setTtal((prev) => ({ ...prev, file: files ? files[0] : null }));
        } else {
            setTtal((prev) => ({ ...prev, [name]: value }));
        }
    };

    const handleDocCountChange = (e: ChangeEvent<HTMLInputElement>) => {
        const count = parseInt(e.target.value) || 0;
        setDocCount(count);

        setDocuments((prevDocs) => {
            if (count > prevDocs.length) {
                // Add new documents
                const newDocs = [...prevDocs];
                for (let i = prevDocs.length; i < count; i++) {
                    newDocs.push({
                        id: Date.now() + i, // Simple unique ID generation
                        code: '',
                        description: '',
                        revision: '',
                        file: null,
                    });
                }
                return newDocs;
            } else {
                // Remove documents from the end
                return prevDocs.slice(0, count);
            }
        });
    };

    const handleDocumentChange = (index: number, e: ChangeEvent<HTMLInputElement>) => {
        const { name, value, files } = e.target;
        setDocuments((prevDocs) => {
            const newDocs = [...prevDocs];
            if (name === 'file') {
                newDocs[index] = { ...newDocs[index], file: files ? files[0] : null };
            } else {
                newDocs[index] = { ...newDocs[index], [name as keyof DocumentData]: value };
            }
            return newDocs;
        });
    };

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();
        await DocsEntryRepository.submitDocsEntry(ttal, documents);
        alert('Formulario enviado (ver consola)');
    };

    return {
        ttal,
        docCount,
        documents,
        handleTtalChange,
        handleDocCountChange,
        handleDocumentChange,
        handleSubmit,
    };
};
