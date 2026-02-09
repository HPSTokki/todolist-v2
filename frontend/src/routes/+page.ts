import type { PageLoad } from "./$types";

export const load: PageLoad = async ({fetch}) => {
    const res = await fetch("http://localhost:8000/");
    const greet = await res.json();
    return greet
}