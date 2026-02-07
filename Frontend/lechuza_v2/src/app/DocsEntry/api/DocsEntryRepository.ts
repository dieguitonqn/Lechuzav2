import { TtalData, DocumentData } from '../types/types';

export const DocsEntryRepository = {
    submitDocsEntry: async (ttal: TtalData, documents: DocumentData[]): Promise<void> => {
        // Simulate API call
        console.log('Repository: Submitting data...', { ttal, documents });
        return new Promise((resolve) => {
            setTimeout(() => {
                console.log('Repository: Data submitted successfully');
                resolve();
            }, 500);
        });
    }
};
