import {error} from "@sveltejs/kit";

const modules = import.meta.glob("$lib/*.js", {eager: true});
const WORDLISTS = new Map(
    Object.entries(modules).map(([path, mod]) => {
        const match = /\/([^/]+)\.js$/.exec(path);
        const slug = match ? match[1] : path;
        return [slug, mod.words];
    })
);

export function load({params}) {
    const words = WORDLISTS.get(params.slug);

    if (!words) {
        throw error(404, "Word list not found");
    }

    return {words};
}
