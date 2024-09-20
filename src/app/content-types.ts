import type { ChainModifiers, Entry, EntryFieldTypes, EntrySkeletonType, LocaleCode } from "contentful";

export interface TypeTextBoxFields {
    body?: EntryFieldTypes.RichText;
}

// export type TypeTextBoxSkeleton = EntrySkeletonType<TypeTextBoxFields, "textBox">;
// export type TypeTextBox<Modifiers extends ChainModifiers, Locales extends LocaleCode = LocaleCode> = Entry<TypeTextBoxSkeleton, Modifiers, Locales>;

export type TypeTextBoxSkeleton = {
    contentTypeId: 'textBox',
    fields: {
        body: EntryFieldTypes.RichText,
    }
}


