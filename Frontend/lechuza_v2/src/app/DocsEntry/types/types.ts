export interface TtalData {
    code: string;
    description: string;
    file: File | null;
}

export interface DocumentData {
    id: number;
    code: string;
    description: string;
    revision: string;
    file: File | null;
}
