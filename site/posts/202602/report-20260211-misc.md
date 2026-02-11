---
date: '2026-02-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dfb83c6...MicrosoftDocs:8eb0165
summary: このコードの変更により、Azure AI Foundryおよび言語サービスのドキュメントで用語の明確化と一貫性が向上しました。「country hint」を「country/region
  hint」に統一し、文書全体での用語を標準化しました。また、目次ファイルから不要な項目を削除して文書構造を簡潔にしました。新機能の追加はなく、用語変更により既存の参照文書で混乱が生じる可能性はありますが、APIの挙動には変更はありません。ドキュメントの用語の一貫性は開発者にとって重要であり、必要な情報に迅速にアクセスできるようになるため、ユーザー体験の向上に寄与します。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:dfb83c6...MicrosoftDocs:8eb0165){target="_blank"}

<format>
# Highlights
このコードの変更では、Azure AI Foundryおよび言語サービスのドキュメントに対し、用語の明確化および一貫性の向上が図られています。特に、「country hint」という表現を「country/region hint」に統一し、関連するドキュメント全体で用語を標準化しています。また、目次ファイルから不要な項目を削除し、文書構造が簡潔になりました。

## New features
- 特に新機能に関する追加はありません。

## Breaking changes
- 既存のドキュメントが利用者によって参照されている場合、「country hint」と「country/region hint」の用語変更により、一部の利用者が混乱する可能性がありますが、API自体の挙動が変更されたわけではありません。

## Other updates
- 目次ファイル（toc.yml）から、QnA Makerに関する項目が削除されました。これにより、関連情報へのアクセスが簡便になります。

# Insights
このコード変更は、主にドキュメントのメンテナンスと改善を目的としています。Azure AI Foundryや言語サービスを利用する開発者にとって、用語が整合性を持っていることは非常に重要です。たとえ機能そのものに変更がなくとも、ドキュメントの用語の一貫性が確保されることで、APIやサービスの利用者は設定や結果をより正確に把握できるようになります。また、目次から不要な情報を削除することで、情報の取捨選択がスムーズに行えるため、実際の開発業務において必要な情報に迅速にアクセス可能になります。このようなドキュメント更新の作業は、ユーザー体験を向上させる上で不可欠な要素です。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [azure-ai-foundry.md](#item-41c23c) | minor update | Azure AI Foundryの言語検出ガイドの更新 | modified | 3 | 3 | 6 | 
| [quickstart.md](#item-636553) | minor update | 言語検出クイックスタートガイドの修正 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-12f1f0) | minor update | 言語サービス目次の整理 | modified | 0 | 6 | 6 | 


# Modified Contents
## articles/ai-services/language-service/language-detection/includes/quickstarts/azure-ai-foundry.md{#item-41c23c}

<details>
<summary>Diff</summary>
````diff
@@ -41,7 +41,7 @@ The **Language playground** consists of four sections:
    | Section | Purpose |
    | --- | --- |
    | **Top banner** | Select the **Detect language** tile. |
-   | **Left pane** | Set **Configuration** options such as API version, model version, and country hint. |
+   | **Left pane** | Set **Configuration** options such as API version, model version, and country/region hint. |
    | **Center pane** | Enter text for processing and review results. |
    | **Right pane** | View **Details** for detected language and script. |
 
@@ -53,7 +53,7 @@ The **Language playground** consists of four sections:
    |--------------------|-----------------------------------------|
    |Select API version  | Select which version of the API to use.    |
    |Select model version| Select which version of the model to use.|
-   |Select country hint| Select the origin country/region of the input text. |
+   |Select country/region hint| Select the origin country/region of the input text. |
 
 1. Select the **Run** button to detect the language.
 
@@ -68,7 +68,7 @@ After the operation completes, the **Details** section displays the following fi
 
   :::image type="content" source="../../media/quickstarts/azure-ai-foundry/language-detection.png" alt-text="A screenshot showing language detection results with confidence scores and ISO codes displayed in the Details pane of the Foundry portal." lightbox="../../media/quickstarts/azure-ai-foundry/language-detection.png":::
 
-Verify that the detected language matches the language of your input text. If the result shows `unknown`, provide a longer text sample or set a **Country hint** for better accuracy.
+Verify that the detected language matches the language of your input text. If the result shows `unknown`, provide a longer text sample or set a **Country/region hint** for better accuracy.
 
 ### [Foundry (new)](#tab/foundry-new)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryの言語検出ガイドの更新"
}
```

### Explanation
このコードの変更は、Azure AI Foundryに関する言語検出ガイドのドキュメントを対象にしたもので、用語を明確化し、一貫性を持たせることを目的としています。具体的には、「country hint」という表現を「country/region hint」に変更することで、地域に関連する設定が明確になるようにしています。また、確認メッセージ内でも同様の表現変更が行われ、全体の文書が一貫した用語を使用するように更新されています。これにより、ユーザーがAPIの設定や結果に関してより理解しやすくなることを狙っています。

## articles/ai-services/language-service/language-detection/quickstart.md{#item-636553}

<details>
<summary>Diff</summary>
````diff
@@ -65,7 +65,7 @@ If you don't have an Azure subscription, create a [free account](https://azure.m
 | You get an error about missing environment variables. | Confirm `LANGUAGE_KEY` and `LANGUAGE_ENDPOINT` are set in your environment before you run the sample. |
 | The Foundry experience doesn't match the steps. | In the Foundry portal, use the version toggle to switch between Foundry (classic) and Foundry (new), then follow the matching tab in the Foundry section. |
 | The API returns `unknown` as the detected language. | The input text might be too short or ambiguous. Provide a longer text sample or set the **Country/region hint** to improve accuracy. |
-| The API returns an `InvalidCountryHint` error. | Confirm the country hint code is a valid ISO 3166-1 alpha-2 code (for example, `US`, `FR`, `JP`). |
+| The API returns an `InvalidCountryHint` error. | Confirm the country/region hint code is a valid ISO 3166-1 alpha-2 code (for example, `US`, `FR`, `JP`). |
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語検出クイックスタートガイドの修正"
}
```

### Explanation
このコードの変更は、Azure AIの言語検出クイックスタートガイドにおける用語の調整を目的としています。具体的には、「Country hint」という用語を「Country/region hint」に変更して、環境変数に関する説明文に一貫性を持たせています。この修正により、利用者は国または地域に関連する設定がより明確に理解できるようになり、正確な情報を反映することが可能になります。全体として、ドキュメントの精度と明確さが向上しています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -163,12 +163,6 @@ items:
         displayName: Data privacy, logging, data retention
     - name: How-to guides
       items:
-      - name: Migrate from QnA Maker to custom question Answering
-        href: question-answering/how-to/migrate-qnamaker-to-question-answering.md
-        displayName: migration, custom question answering
-      - name: Migrate projects from QnA Maker
-        href: question-answering/how-to/migrate-qnamaker.md
-        displayName: migration, transfer
       - name: Create, test, and deploy a knowledge base
         href: question-answering/how-to/create-test-deploy.md
         displayName: knowledge base, test deploy
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語サービス目次の整理"
}
```

### Explanation
このコードの変更は、Azure AIサービスの言語サービスに関する目次（toc.yml）ファイルの修正を示しています。具体的には、QnA Makerからの移行に関するいくつかの項目が削除されています。これにより、目次が簡略化され、不要な情報が削除されることで、利用者が必要な情報へアクセスしやすくなることを目的としています。全体的に、ドキュメントの整合性が向上し、ユーザーが知りたい内容に対して焦点が絞られています。


