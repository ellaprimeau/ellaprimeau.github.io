import type { ChainModifiers, Entry, EntryFieldTypes, EntrySkeletonType, LocaleCode } from "contentful";
import * as Contentful from "contentful";

export interface TypeTextBoxFields {
    body?: EntryFieldTypes.RichText;
}

export interface TypeMapPostFields {
    title?: EntryFieldTypes.Symbol;
    description?: EntryFieldTypes.RichText;
    tags?: EntryFieldTypes.Object;
    attachment?: EntryFieldTypes.Array<EntryFieldTypes.AssetLink>;
}

// export type TypeTextBoxSkeleton = EntrySkeletonType<TypeTextBoxFields, "textBox">;
// export type TypeTextBox<Modifiers extends ChainModifiers, Locales extends LocaleCode = LocaleCode> = Entry<TypeTextBoxSkeleton, Modifiers, Locales>;

// export type TypeMapPostSkeleton = EntrySkeletonType<TypeMapPostFields, "MapPost">;
// export type TypeMapPost<Modifiers extends ChainModifiers, Locales extends LocaleCode = LocaleCode> = Entry<TypeMapPostSkeleton>

export type TypeMapPostSkeleton = Contentful.EntrySkeletonType<TypeMapPostFields>;


