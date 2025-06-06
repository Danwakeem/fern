export function filterObject<T extends object, K extends keyof T>(obj: T, keysToInclude: K[]): Pick<T, K> {
    const keysToIncludeSet = new Set(keysToInclude);
    return Object.entries(obj).reduce(
        (acc, [key, value]) => {
            if (keysToIncludeSet.has(key as K)) {
                acc[key as K] = value as T[K];
            }
            return acc;
            // eslint-disable-next-line @typescript-eslint/prefer-reduce-type-parameter
        },
        {} as Pick<T, K>
    );
}
