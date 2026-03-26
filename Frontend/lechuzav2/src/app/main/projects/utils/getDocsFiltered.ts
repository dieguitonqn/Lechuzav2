import {Filters} from "../interfaces";

export interface GetDocsFiltered {
    ProjectId: number;
    filters: Filters;
}

export const getDocsFiltered = (filtersPros: GetDocsFiltered) => {
    const {ProjectId, filters} = filtersPros;
    const queryParams = new URLSearchParams();
    queryParams.append("ProjectId", ProjectId.toString());
}