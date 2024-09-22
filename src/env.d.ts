interface ImportMeta {
  readonly env: ImportMetaEnv;
}

interface ImportMetaEnv {
  readonly NODE_ENV: string;
  readonly NG_APP_NAME: string;
  readonly NG_APP_CONTENTFUL_ACCESS_TOKEN: string;
  readonly NG_APP_CONTENTFUL_PREVIEW_ACCESS_TOKEN: string;
  readonly NG_APP_CONTENTFUL_SPACE_ID: string;
}
