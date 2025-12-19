---
date: '2025-12-19'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a2d235e...MicrosoftDocs:38e3c32
summary: このドキュメントは、MicrosoftのAIサービスにおけるLanguage Studioとその関連文書の大幅な整理に関する変更を示しています。特に、記事分類や日付の更新が行われ、多くの手順やガイドラインが削除されたことが強調されています。これにより、特に初心者や詳細な指示を必要とするユーザーにとって、便利なガイドが失われるため、使用体験に影響が出ることが懸念されています。メタデータの更新は一貫性を高める努力ですが、失われた手順によって基本的な機能を利用する際のハードルが上がる可能性があります。総じて、ドキュメントの改訂は効率的な情報検索を考慮したものであり、今後の改善が期待されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a2d235e...MicrosoftDocs:38e3c32){target="_blank"}

<format>
# Highlights
このドキュメントはMicrosoftのAIサービスにおけるLanguage Studioと関連するドキュメントの大幅な整理に関する詳細な変更を加え、最新の情報を反映したものです。特に、多数のファイルにおいて記事分類の更新や日付の更新が行われました。また、Language Studioに関連する幾つかの手順やガイドラインが削除されることでユーザー体験の影響が懸念されます。

## New features
- なし

## Breaking changes
- Language Studioに関連する、トレーニングキャンセル手順、プロジェクト作成、モデルデプロイ、プロジェクト削除等の具体的な手順が完全に削除。
- SVG形式のバナー画像やマイグレーションやアプリケーション選択図の削除。

## Other updates
- 多くのファイルにおいて、メタデータの`ms.topic`フィールドの値が`conceptual`から`concept-article`や`limits-and-quotas`に変更。
- ドキュメント管理用日付の更新。
- `whats-new.md`などで細かい文言の修正とリンクの調整。

# Insights
最新の修正では、Language Studioに関連した手順やガイドライン、関連図面の削除、大幅なコンテンツ削減が行われました。これはドキュメントの情報整理を目的としている可能性がありますが、手順に依存しているユーザーにとっては不便を与えることになります。この中で特筆すべき変更としては、ユーザーガイドが大幅に削除された影響でしょう。これにより、特に初心者や詳細な指示を必要とするユーザーは困惑を招く可能性があります。

メタデータのトピック分類や日付更新は、ドキュメントの一貫性と保守性を高めるための努力として見ることができますが、ユーザーには目立たない側面です。クイックスタートや詳細な手順が失われたことで、関連機能の利用を開始するプロセスは新たなハードルに直面するかもしれません。特に、プロジェクト作成やトレーニング、デプロイといった基礎的な操作のガイドが喪失したことが重要で、再度のドキュメントやサポートが待たれる状況です。

一方で、頻繁なトピックの分類更新は、ナビゲーションと情報検索の効率を考慮したものであり、長期的には利用者にとっての利便性向上が見込まれます。したがって、今後のドキュメントの公開方法への戦略的な適応が期待されます。この変動時期においては、技術者は過去の文献や他のオンラインリソースを活用し、新しいワークフローに適応することが求められます。</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [developer-guide.md](#item-003b09) | minor update | 開発者ガイドのリンク修正 | modified | 2 | 2 | 4 | 
| [migrate.md](#item-42e0a6) | minor update | マイグレーションガイドの内容更新 | modified | 6 | 6 | 12 | 
| [best-practices.md](#item-ae9331) | minor update | ベストプラクティスガイドの更新 | modified | 12 | 13 | 25 | 
| [data-formats.md](#item-8559f6) | minor update | データフォーマットガイドの更新 | modified | 2 | 2 | 4 | 
| [entity-components.md](#item-9168dd) | minor update | エンティティコンポーネントガイドの更新 | modified | 2 | 2 | 4 | 
| [evaluation-metrics.md](#item-d6ba3f) | minor update | 評価指標ガイドの更新 | modified | 2 | 2 | 4 | 
| [multi-turn-conversations.md](#item-95c813) | minor update | マルチターン会話ガイドの更新 | modified | 1 | 1 | 2 | 
| [multiple-languages.md](#item-5de532) | minor update | 複数言語ガイドの更新 | modified | 2 | 2 | 4 | 
| [none-intent.md](#item-63402b) | minor update | None intentガイドの更新 | modified | 1 | 1 | 2 | 
| [faq.md](#item-590d89) | minor update | FAQガイドの更新 | modified | 1 | 1 | 2 | 
| [call-api.md](#item-ce9a73) | minor update | API呼び出しガイドの更新 | modified | 3 | 18 | 21 | 
| [deploy-model.md](#item-b64101) | breaking change | モデルデプロイガイドの大幅な改訂 | modified | 0 | 37 | 37 | 
| [view-model-evaluation.md](#item-f0ecb3) | minor update | モデル評価ガイドの簡素化 | modified | 1 | 28 | 29 | 
| [assign-resources.md](#item-e82d92) | breaking change | リソース割り当てガイドの削除 | removed | 0 | 16 | 16 | 
| [cancel-training.md](#item-c68e58) | breaking change | トレーニングキャンセル手順の削除 | removed | 0 | 11 | 11 | 
| [create-project.md](#item-0172b6) | breaking change | プロジェクト作成手順の削除 | removed | 0 | 26 | 26 | 
| [delete-deployment.md](#item-22b6f8) | breaking change | デプロイメント削除手順の削除 | removed | 0 | 9 | 9 | 
| [delete-model.md](#item-d4b2d9) | breaking change | モデル削除手順の削除 | removed | 0 | 15 | 15 | 
| [delete-project.md](#item-01c6cb) | breaking change | プロジェクト削除手順の削除 | removed | 0 | 9 | 9 | 
| [deploy-model.md](#item-b70ddc) | breaking change | モデルデプロイ手順の削除 | removed | 0 | 28 | 28 | 
| [get-prediction-url.md](#item-566371) | breaking change | 予測URLを取得する手順の削除 | removed | 0 | 19 | 19 | 
| [import-project.md](#item-de782b) | breaking change | プロジェクトのインポート手順の削除 | removed | 0 | 20 | 20 | 
| [load-export-model.md](#item-dfdc28) | breaking change | モデルデータの読み込みおよびエクスポート手順の削除 | removed | 0 | 23 | 23 | 
| [model-performance.md](#item-3a099d) | breaking change | モデルパフォーマンスの手順の削除 | removed | 0 | 64 | 64 | 
| [project-details.md](#item-4baebc) | breaking change | プロジェクト詳細設定手順の削除 | removed | 0 | 18 | 18 | 
| [sign-in-studio.md](#item-6f8bd7) | breaking change | Language Studioサインイン手順の削除 | removed | 0 | 21 | 21 | 
| [swap-deployment.md](#item-251c71) | breaking change | デプロイメントのスワップ手順の削除 | removed | 0 | 15 | 15 | 
| [test-model.md](#item-98e559) | breaking change | モデルテスト手順の削除 | removed | 0 | 23 | 23 | 
| [train-model.md](#item-dd4473) | breaking change | モデルのトレーニング手順の削除 | removed | 0 | 32 | 32 | 
| [unassign-resources.md](#item-446010) | breaking change | リソースの割り当て解除手順の削除 | removed | 0 | 13 | 13 | 
| [language-support.md](#item-6b7b2b) | minor update | トピックの種類の更新 | modified | 1 | 1 | 2 | 
| [banner.svg](#item-c4089a) | breaking change | バナー画像の削除 | removed | 0 | 9 | 9 | 
| [migration-overview.svg](#item-766cbd) | breaking change | マイグレーション概要図の削除 | removed | 0 | 53 | 53 | 
| [migration-progress.svg](#item-395735) | breaking change | マイグレーション進捗図の削除 | removed | 0 | 136 | 136 | 
| [select-applications.svg](#item-f3214c) | breaking change | アプリケーション選択図の削除 | removed | 0 | 291 | 291 | 
| [select-resource.svg](#item-003814) | breaking change | リソース選択図の削除 | removed | 0 | 53 | 53 | 
| [prebuilt-component-reference.md](#item-5af620) | minor update | トピックタイプの更新 | modified | 1 | 1 | 2 | 
| [service-limits.md](#item-0c7212) | minor update | トピックタイプの変更 | modified | 1 | 1 | 2 | 
| [language-studio.md](#item-b7d381) | breaking change | Language Studioのクイックスタートガイドの削除 | removed | 0 | 70 | 70 | 
| [cancel-training.md](#item-b6ec08) | breaking change | トレーニング中止に関するガイドラインの削除 | removed | 0 | 9 | 9 | 
| [create-project.md](#item-9aa401) | breaking change | カスタムテキスト分類プロジェクト作成ガイドの削除 | removed | 0 | 46 | 46 | 
| [delete-deployment.md](#item-8e5067) | breaking change | デプロイメント削除に関するガイドラインの削除 | removed | 0 | 9 | 9 | 
| [delete-model.md](#item-e9b701) | breaking change | モデル削除に関するガイドラインの削除 | removed | 0 | 16 | 16 | 
| [delete-project.md](#item-e2af45) | breaking change | プロジェクト削除に関するガイドラインの削除 | removed | 0 | 9 | 9 | 
| [deploy-model.md](#item-5169f8) | breaking change | モデルデプロイに関するガイドラインの削除 | removed | 0 | 26 | 26 | 
| [get-prediction-url.md](#item-364b8f) | breaking change | 予測URL取得に関するガイドラインの削除 | removed | 0 | 29 | 29 | 
| [import-project.md](#item-8482b0) | breaking change | プロジェクトインポート手順の削除 | removed | 0 | 47 | 47 | 
| [model-evaluation.md](#item-b3ab55) | breaking change | モデル評価に関するガイドラインの削除 | removed | 0 | 81 | 81 | 
| [project-details.md](#item-ba2c45) | breaking change | プロジェクト詳細に関する情報の削除 | removed | 0 | 21 | 21 | 
| [resource-creation-language-studio.md](#item-cad76b) | breaking change | Language Studioにおけるリソース作成手順の削除 | removed | 0 | 31 | 31 | 
| [swap-deployment.md](#item-e26e67) | breaking change | Language Studioにおけるデプロイのスワップ手順の削除 | removed | 0 | 17 | 17 | 
| [test-model.md](#item-b0f78f) | breaking change | Language Studioにおけるモデルテスト手順の削除 | removed | 0 | 27 | 27 | 
| [train-model.md](#item-704d2a) | breaking change | Language Studioにおけるモデルのトレーニング手順の削除 | removed | 0 | 30 | 30 | 
| [language-studio.md](#item-1caefc) | breaking change | Language Studioのクイックスタートガイドの削除 | removed | 0 | 72 | 72 | 
| [data-formats.md](#item-7a72ee) | minor update | データ形式のドキュメントの軽微な修正 | modified | 2 | 2 | 4 | 
| [evaluation-metrics.md](#item-954044) | minor update | 評価メトリクスに関するドキュメントの軽微な修正 | modified | 3 | 3 | 6 | 
| [fail-over.md](#item-ad9d67) | minor update | フェイルオーバーに関するドキュメントの軽微な修正 | modified | 1 | 1 | 2 | 
| [none-intent.md](#item-c47b2f) | minor update | Noneインテントに関するドキュメントの軽微な修正 | modified | 2 | 2 | 4 | 
| [faq.md](#item-30440d) | minor update | FAQドキュメントの軽微な修正 | modified | 11 | 11 | 22 | 
| [glossary.md](#item-386170) | minor update | 用語集ドキュメントの軽微な修正 | modified | 10 | 10 | 20 | 
| [build-schema.md](#item-ea718c) | minor update | スキーマ構築に関する手順の更新 | modified | 8 | 28 | 36 | 
| [call-api.md](#item-f50775) | minor update | API呼び出し手順の簡略化と修正 | modified | 12 | 26 | 38 | 
| [create-project.md](#item-5dadf0) | minor update | プロジェクト作成手順の簡略化とREST APIに関するリファクタリング | modified | 5 | 55 | 60 | 
| [deploy-model.md](#item-36ebf2) | minor update | モデルデプロイ手順の簡略化と表現の改善 | modified | 4 | 43 | 47 | 
| [tag-utterances.md](#item-e80df9) | minor update | 発話追加手順の文言修正と構成の見直し | modified | 11 | 11 | 22 | 
| [train-model.md](#item-012314) | breaking change | トレーニングモデル手順の大幅な削除 | modified | 0 | 24 | 24 | 
| [view-model-evaluation.md](#item-86aee9) | minor update | モデル評価ページの見出し追加と内容の削減 | modified | 1 | 23 | 24 | 
| [cancel-training.md](#item-6dd79a) | breaking change | トレーニングキャンセル手順の削除 | removed | 0 | 9 | 9 | 
| [create-project.md](#item-f34974) | breaking change | プロジェクト作成手順の削除 | removed | 0 | 22 | 22 | 
| [delete-deployment.md](#item-f132cd) | breaking change | デプロイメント削除手順の削除 | removed | 0 | 9 | 9 | 
| [delete-model.md](#item-9ba075) | breaking change | モデル削除手順の削除 | removed | 0 | 15 | 15 | 
| [delete-project.md](#item-3b70d0) | breaking change | プロジェクト削除手順の削除 | removed | 0 | 9 | 9 | 
| [deploy-model.md](#item-8ac056) | breaking change | モデル展開手順の削除 | removed | 0 | 32 | 32 | 
| [get-prediction-url.md](#item-7b738d) | breaking change | 予測URL取得手順の削除 | removed | 0 | 16 | 16 | 
| [model-performance.md](#item-c090d2) | breaking change | モデルパフォーマンスに関する情報の削除 | removed | 0 | 24 | 24 | 
| [project-details.md](#item-74d667) | breaking change | プロジェクト詳細に関する情報の削除 | removed | 0 | 18 | 18 | 
| [sign-in-studio.md](#item-f1b35b) | breaking change | Language Studioへのサインイン手順の削除 | removed | 0 | 21 | 21 | 
| [swap-deployment.md](#item-6eea90) | breaking change | デプロイメントのスワップ手順の削除 | removed | 0 | 13 | 13 | 
| [test-model.md](#item-4322d9) | breaking change | モデルテスト手順の削除 | removed | 0 | 23 | 23 | 
| [train-model.md](#item-d7c75c) | breaking change | モデルトレーニング手順の削除 | removed | 0 | 36 | 36 | 
| [language-studio.md](#item-b78cb6) | breaking change | Language Studio クイックスタートガイドの削除 | removed | 0 | 80 | 80 | 
| [language-support.md](#item-3e4a3b) | minor update | トピック分類の更新 | modified | 1 | 1 | 2 | 
| [overview.md](#item-53d49f) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-bee292) | minor update | クイックスタートガイドの内容修正 | modified | 1 | 12 | 13 | 
| [service-limits.md](#item-144728) | minor update | トピックの分類変更 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-12f1f0) | minor update | ナビゲーション項目の削除 | modified | 0 | 3 | 3 | 
| [whats-new.md](#item-69b272) | minor update | テキストとリンクの修正 | modified | 2 | 2 | 4 | 


# Modified Contents
## articles/ai-services/language-service/concepts/developer-guide.md{#item-003b09}

<details>
<summary>Diff</summary>
````diff
@@ -69,7 +69,7 @@ As you use these features in your application, use the following documentation a
 The `Azure.AI.Language.Conversations` namespace enables you to use the following Language features. Use the following links for articles to help you send API requests using the SDK.
 
 * [Conversational language understanding](../conversational-language-understanding/how-to/call-api.md?tabs=azure-sdk#send-a-conversational-language-understanding-request)
-* [Orchestration workflow](../orchestration-workflow/how-to/call-api.md?tabs=azure-sdk#send-an-orchestration-workflow-request)
+* [Orchestration workflow](../orchestration-workflow/how-to/call-api.md)
 * [Conversation summarization (Python only)](../summarization/quickstart.md?tabs=conversation-summarization&pivots=programming-language-python)
 * [Personally Identifying Information (PII) detection for conversations](../personally-identifiable-information/how-to-call-for-conversations.md?tabs=client-libraries#examples)
 
@@ -113,7 +113,7 @@ For more information, *see* the [reference documentation](/rest/api/language/).
 
 The conversation analysis runtime API enables you to send requests to custom models you create for the following features:
 * [Conversational language understanding](../conversational-language-understanding/how-to/call-api.md?tabs=REST-APIs#send-a-conversational-language-understanding-request)
-* [Orchestration workflow](../orchestration-workflow/how-to/call-api.md?tabs=REST-APIs#send-an-orchestration-workflow-request)
+* [Orchestration workflow](../orchestration-workflow/how-to/call-api.md)
 
 It additionally enables you to use the following features, without creating any models:
 * [Conversation summarization](../summarization/quickstart.md?pivots=rest-api&tabs=conversation-summarization)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "開発者ガイドのリンク修正"
}
```

### Explanation
このコードの差分は、MicrosoftのAIサービスに関する「開発者ガイド」文書の内容に対する小規模な更新を示しています。具体的には、オーケストレーションワークフローに関連するAPIリクエストのリンクが修正されています。修正前は、URLにタブ情報が含まれていましたが、修正後はよりシンプルな形でリンクが提供されるようになりました。

更新の内容は、オーケストレーションワークフローにアクセスするための2つのリンクが変更されており、これによりドキュメントの可読性が向上しています。また、これにより、APIリクエストを行う際のガイダンスがより明確になっています。変更は主に視覚的なものであり、機能的には既存のAPIの利用に影響を与えるものではありません。

## articles/ai-services/language-service/concepts/migrate.md{#item-42e0a6}

<details>
<summary>Diff</summary>
````diff
@@ -5,27 +5,27 @@ description: Use this article to learn if you need to migrate your applications
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ---
 # Migrating to Azure Language in Foundry Tools
 
-On November 2, 2021, Azure Language in Foundry Tools was released into public preview. Azure Language unifies the Text Analytics, QnA Maker, and Language Understanding (LUIS) service offerings, and provides several new features as well. 
+On November 2, 2021, Azure Language in Foundry Tools was released into public preview. Azure Language unifies the Text Analytics, QnA Maker, and Language Understanding (LUIS) service offerings, and provides several new features as well.
 
 ## Do I need to migrate to Azure Language if I'm using Text Analytics?
 
-Text Analytics is incorporated into Azure Language, and its features are still available. If you're using Text Analytics features, your applications should continue to work without breaking changes. If you're using Text Analytics API (v2.x or v3), see the [Text Analytics migration guide](migrate-language-service-latest.md) to migrate your applications to the unified Language endpoint and the latest client library. 
+Text Analytics is incorporated into Azure Language, and its features are still available. If you're using Text Analytics features, your applications should continue to work without breaking changes. If you're using Text Analytics API (v2.x or v3), see the [Text Analytics migration guide](migrate-language-service-latest.md) to migrate your applications to the unified Language endpoint and the latest client library.
 
-Consider using one of the available quickstart articles to see the latest information on service endpoints, and API calls. 
+Consider using one of the available quickstart articles to see the latest information on service endpoints, and API calls.
 
 ## How do I migrate to Azure Language if I'm using Language Understanding (LUIS)?
 
-If you're using Language Understanding (Language Understanding (LUIS)), you can [import your Language Understanding (LUIS) JSON file](../conversational-language-understanding/how-to/migrate-from-Language Understanding (LUIS).md) to the new Conversational language understanding feature. 
+If you're using Language Understanding (Language Understanding (LUIS)), you can [import your Language Understanding (LUIS) JSON file](../conversational-language-understanding/how-to/migrate-from-Language Understanding (LUIS).md) to the new Conversational language understanding feature.
 
 ## How do I migrate to Azure Language if I'm using QnA Maker?
 
-If you're using QnA Maker, see the [migration guide](../question-answering/how-to/migrate-qnamaker.md) for information on migrating knowledge bases from QnA Maker to question answering.
+If you're using QnA Maker, see the [migration guide](/previous-versions/azure/ai-services/qnamaker/overview/overview) for information on migrating knowledge bases from QnA Maker to question answering.
 
 ## See also
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マイグレーションガイドの内容更新"
}
```

### Explanation
このコードの差分は、「Azure Languageに移行する」ためのガイド文書に対する小規模な更新を反映しています。主に文書のメタデータやリンクの修正が行われており、情報の整合性と最新性が保たれています。

具体的には、`ms.topic`の値が`conceptual`から`concept-article`に変更されています。また、QnA Makerに関するマイグレーションガイドのリンクが更新され、より適切なURLに修正されています。これにより、ユーザーが必要な情報に迅速にアクセスできるようになります。全体として、これらの変更は文章の意味や機能には大きな影響を与えないものであり、主に文書の質を向上させるためのものです。

## articles/ai-services/language-service/conversational-language-understanding/concepts/best-practices.md{#item-ae9331}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: best-practice
-ms.date: 11/18/2025
+ms.date: 12/17/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
 ---
@@ -75,7 +75,7 @@ If you require the learned component, make sure that **Ticket Quantity** is only
 
 ## Address model inconsistencies
 
-If your model is overly sensitive to small grammatical changes, like casing or diacritics, you can systematically manipulate your dataset directly in Language Studio. To use these features, select the **Settings** tab on the left pane and locate the **Advanced project settings** section.
+If your model is overly sensitive to small grammatical changes, like casing or diacritics, you can systematically manipulate your dataset directly in Microsoft Foundry. To use these features, select the **Settings** tab on the left pane and locate the **Advanced project settings** section.
 
 :::image type="content" source="../media/advanced-project-settings.png" alt-text="A screenshot that shows an example of Advanced project settings." lightbox="../media/advanced-project-settings.png":::
 
@@ -93,7 +93,7 @@ First, you can enable the setting for **Enable data transformation for casing**,
 ...
 ```
 
-Second, you can also enable the setting for **Enable data augmentation for diacritics** to generate variations of your training data for possible diacritic variations used in natural language. This feature is available for all languages. It's especially useful for Germanic and Slavic languages, where users often write words by using classic English characters instead of the correct characters. For example, the phrase "Navigate to the sports channel" in French is "Accédez à la chaîne sportive." When this feature is enabled, the phrase "Accedez a la chaine sportive" (without diacritic characters) is also included in the training dataset.
+Second, you can also enable the setting for **Enable data augmentation for diacritics** to generate variations of your training data for possible diacritic variations used in natural language. This feature is available for all languages. It's especially useful for Germanic and Slavic languages, where users often write words by using classic English characters instead of the correct characters. For example, the phrase "Navigate to the sports channel" in French is `Accédez à la chaîne sportive.` When this feature is enabled, the phrase `Accedez a la chaine sportive` (without diacritic characters) is also included in the training dataset.
 
 If you enable this feature, the utterance count of your training set increases. For this reason, you might need to adjust your training data size accordingly. The current maximum utterance count after augmentation is 25,000. To access this feature via the API, set the `augmentDiacritics` parameter to `true`. See the following example:
 
@@ -113,10 +113,10 @@ If you enable this feature, the utterance count of your training set increases.
 
 Customers can use the LoraNorm training configuration version if the model is being incorrectly overconfident. An example of this behavior can be like the following scenario where the model predicts the incorrect intent with 100% confidence. This score makes the confidence threshold project setting unusable.
 
-| Text |	Predicted intent |	Confidence score |
+| Text |    Predicted intent |    Confidence score |
 |----|----|----|
-| "Who built the Eiffel Tower?" |	 `Sports` | 1.00 |
-| "Do I look good to you today?" | `QueryWeather` |	1.00 |
+| "Who built the Eiffel Tower?" |     `Sports` | 1.00 |
+| "Do I look good to you today?" | `QueryWeather` |    1.00 |
 | "I hope you have a good evening." | `Alarm` | 1.00 |
 
 To address this scenario, use the `2023-04-15` configuration version that normalizes confidence scores. The confidence threshold project setting can then be adjusted to achieve the desired result.
@@ -137,7 +137,7 @@ curl --location 'https://<your-resource>.cognitiveservices.azure.com/language/au
 }
 ```
 
-After the request is sent, you can track the progress of the training job in Language Studio as usual.
+After the request is sent, you can track the progress of the training job in Microsoft Foundry.
 
 > [!NOTE]
 > You have to retrain your model after you update the `confidenceThreshold` project setting. Afterward, you need to republish the app for the new threshold to take effect.
@@ -203,7 +203,7 @@ curl --request POST \
 
 ## Copy projects across language resources
 
-Often you can copy conversational language understanding projects from one resource to another by using the **Copy** button in Language Studio. In some cases, it might be easier to copy projects by using the API.
+Often you can copy conversational language understanding projects from one resource to another by using the **Copy** button in Microsoft Foundry. In some cases, it might be easier to copy projects by using the API.
 
 First, identify the:
  
@@ -243,10 +243,10 @@ curl --request POST \
 
 Customers can use the newly updated training configuration version `2024-08-01-preview` (previously `2024-06-01-preview`) if the model has poor quality on out-of-domain utterances. An example of this scenario with the default training configuration can be like the following example where the model has three intents: `Sports`, `QueryWeather`, and `Alarm`. The test utterances are out-of-domain utterances and the model classifies them as `InDomain` with a relatively high confidence score.
 
-| Text |	Predicted intent |	Confidence score |
+| Text |    Predicted intent |    Confidence score |
 |----|----|----|
-| "Who built the Eiffel Tower?" |	 `Sports` | 0.90 |
-| "Do I look good to you today?" | `QueryWeather` |	1.00 |
+| "Who built the Eiffel Tower?" |     `Sports` | 0.90 |
+| "Do I look good to you today?" | `QueryWeather` |    1.00 |
 | "I hope you have a good evening." | `Alarm` | 0.80 |
 
 To address this scenario, use the `2024-08-01-preview` configuration version that's built specifically to address this issue while also maintaining reasonably good quality on `InDomain` utterances.
@@ -267,8 +267,7 @@ curl --location 'https://<your-resource>.cognitiveservices.azure.com/language/au
 }
 ```
 
-After the request is sent, you can track the progress of the training job in Language Studio as usual.
-
+After the request is sent, you can track the progress of the training job in Microsoft Foundry.
 Caveats:
 
 - The None score threshold for the app (confidence threshold below which `topIntent` is marked as `None`) when you use this training configuration should be set to 0. This setting is used because this new training configuration attributes a certain portion of the in-domain probabilities to out of domain so that the model isn't incorrectly overconfident about in-domain utterances. As a result, users might see slightly reduced confidence scores for in-domain utterances as compared to the production training configuration.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ベストプラクティスガイドの更新"
}
```

### Explanation
このコードの差分は、会話型言語理解に関する「ベストプラクティス」ガイドの内容に対する小規模な更新を示しています。更新内容には、日付の変更や文書内の特定の用語の修正が含まれています。

まず、メタデータの`ms.date`が`11/18/2025`から`12/17/2025`に変更され、文書の日付が更新されました。また、「Language Studio」という用語が「Microsoft Foundry」に置き換えられ、用語の統一が図られています。

この文書の主要な内容には、モデルの整合性やトレーニングデータの変換に関連した情報が含まれており、ユーザーが会話型アプリケーションを設計する際のベストプラクティスが強調されています。その他の詳細についても数箇所の修正が行われ、文章の明確性が向上しています。全体として、これらの変更は情報の一貫性を高め、ユーザーにとってより役立つガイドとなることを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/concepts/data-formats.md{#item-8559f6}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about the data formats accepted by conversational language un
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-clu
@@ -175,4 +175,4 @@ Conversational language understanding offers the option to upload your utterance
 ## Related content
 
 * For more information on importing your labeled data into your project directly, see [Import project](../how-to/create-project.md#import-an-existing-foundry-project).
-* For more information about labeling your data, see [Label your utterances in Language Studio](../how-to/tag-utterances.md). After you label your data, you can [train your model](../how-to/train-model.md).
+* For more information about labeling your data, see [Label your utterances](../how-to/tag-utterances.md). After you label your data, you can [train your model](../how-to/train-model.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データフォーマットガイドの更新"
}
```

### Explanation
このコードの差分は、「会話型言語理解」の「データフォーマット」に関するガイドに対する小規模な修正を示しています。主な変更点はメタデータと関連リンクの表現方法の修正です。

まず、メタデータにおいて、`ms.topic`の値が`conceptual`から`concept-article`に変更され、文書のカテゴリがより明確になっています。また、最終行の関連コンテンツのリンク説明が短縮され、余分な文言が削除されました。これにより、リンクがより簡潔で理解しやすくなっています。

全体として、これらの変更は文書の整合性を保ちながら、ユーザーにとっての使いやすさを向上させることを目的としています。文書の内容自体には大きな影響を与えないため、情報が引き続き効果的に提供されることを保証しています。

## articles/ai-services/language-service/conversational-language-understanding/concepts/entity-components.md{#item-9168dd}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how conversational language understanding extracts entities f
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
@@ -98,7 +98,7 @@ Sometimes, you can define an entity using multiple components, but the entity re
 
 Required components are most frequently used with learned components because they can restrict the other component types to a specific context, which is commonly associated to *roles*. You can also require all components to make sure that every component is present for an entity.
 
-In Language Studio, every component in an entity has a toggle next to it that allows you to set it as required.
+In Microsoft Foundry, every component in an entity has a toggle next to it that allows you to set it as required.
 
 #### Example
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティコンポーネントガイドの更新"
}
```

### Explanation
このコードの差分は、「会話型言語理解」におけるエンティティコンポーネントに関するガイドの小規模な更新を示しています。主な変更点は、メタデータの修正と用語の統一です。

まず、メタデータにおいて、`ms.topic`の値が`conceptual`から`concept-article`に変更され、文書のカテゴリーがより明確に表現されています。また、文中の「Language Studio」という用語が「Microsoft Foundry」に置き換えられ、用語の一貫性が向上しています。

具体的には、エンティティのコンポーネントの横にあるトグルについての説明が、新しい用語に対応するよう修正されました。これにより、ユーザーに対して最新のプラットフォームに関する正確な情報が提供され、ガイドの信頼性が高まります。

全体として、これらの変更は文書の整合性を保ちつつ、ユーザーがより正確かつ効果的に情報を利用できるようにすることを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/concepts/evaluation-metrics.md{#item-d6ba3f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about evaluation metrics in conversational language understan
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
@@ -172,4 +172,4 @@ After you train your model, you see some guidance and recommendations on how to
 
 ## Related content
 
-* [Train a model in Language Studio](../how-to/train-model.md)
+* [Train a model](../how-to/train-model.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価指標ガイドの更新"
}
```

### Explanation
このコードの差分は、「会話型言語理解」における評価指標に関するガイドの小規模な更新を示しています。主な修正点は、メタデータの変更と関連リンクの表現方法の調整です。

具体的には、メタデータの`ms.topic`が`conceptual`から`concept-article`に変更され、文書のカテゴリーがより具体的に示されるようになりました。また、関連コンテンツのリンク説明が短縮され、タイトルから「in Language Studio」が削除され「Train a model」という簡潔な表現に統一されました。

この変更により、ユーザーはモデルのトレーニングに関する情報をよりシンプルかつ明確に理解できるようになります。全体として、これらの修正は文書の整合性とユーザビリティを向上させることを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/concepts/multi-turn-conversations.md{#item-95c813}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how CLU handles entity slot-filling across multi-turn convers
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/05/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチターン会話ガイドの更新"
}
```

### Explanation
このコードの差分は、「会話型言語理解」におけるマルチターン会話に関するガイドの小規模な変更を示しています。主な変更点は、一貫性を持たせるためのメタデータの更新です。

具体的には、メタデータの`ms.topic`が`conceptual`から`concept-article`に変更され、文書のカテゴリーがより正確に反映されています。これにより、情報の整理が進み、利用者がコンテンツを見つけやすくなります。

全体として、これらの修正は文書の整合性を強化し、ユーザーがマルチターン会話のアイデアを効果的に理解する手助けを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/concepts/multiple-languages.md{#item-5de532}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about how to make use of multilingual projects in conversatio
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ---
@@ -19,7 +19,7 @@ When you enable multiple languages in a project, you can train the project prima
 
 For example, you can train your project entirely with English utterances and query it in French, German, Mandarin, Japanese, Korean, and others. Conversational language understanding makes it easy for you to scale your projects to multiple languages by using multilingual technology to train your models.
 
-Whenever you identify that a particular language isn't performing as well as other languages, you can add utterances for that language in your project. In the [tag utterances](../how-to/tag-utterances.md) page in Language Studio, you can select the language of the utterance you're adding. When you introduce examples for that language to the model, it's introduced to more of the syntax of that language and learns to predict it better.
+Whenever you identify that a particular language isn't performing as well as other languages, you can add utterances for that language in your project. In the [tag utterances](../how-to/tag-utterances.md) page in Microsoft Foundry, you can select the language of the utterance you're adding. When you introduce examples for that language to the model, it's introduced to more of the syntax of that language and learns to predict it better.
 
 You aren't expected to add the same number of utterances for every language. You should build most of your project in one language and only add a few utterances in languages that you observe aren't performing well. If you create a project that's primarily in English and start testing it in French, German, and Spanish, you might observe that German doesn't perform as well as the other two languages. In that case, consider adding 5% of your original English examples in German, train a new model, and test in German again. You should see better results for German queries. The more utterances you add, the more likely the results are going to get better.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "複数言語ガイドの更新"
}
```

### Explanation
このコードの差分は、「会話型言語理解」における複数言語の利用に関するガイドの小規模な更新を示しています。変更の主な焦点は、メタデータの更新と文中の表現の調整です。

具体的には、`ms.topic`の値が`conceptual`から`concept-article`に変更され、文書の内容に対する説明がより正確に反映されています。また、文中の「Language Studio」が「Microsoft Foundry」に変更され、使用されるプラットフォームの名称が最新のものにアップデートされています。この変更は、プラットフォーム名の正確性を保つことで、読者が適切なリソースを見つけやすくすることを意図しています。

全体として、これらの修正は文書の整合性を強化し、ユーザーが複数言語を用いたプロジェクトの管理やトレーニングに関する情報をより効果的に理解するための助けとなることを目指しています。

## articles/ai-services/language-service/conversational-language-understanding/concepts/none-intent.md{#item-63402b}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about the default None intent in conversational language unde
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "None intentガイドの更新"
}
```

### Explanation
このコードの差分は、会話型言語理解におけるデフォルトの「None intent」に関するガイドの小規模な修正を示しています。主にメタデータの更新が行われており、文書のカテゴリーがより正確に定義されています。

具体的には、`ms.topic`というメタデータの値が`conceptual`から`concept-article`に変更されており、文書の意義が明確になっています。この変更により、ユーザーはこのガイドがどのような内容であるかをより理解しやすくなります。

全体として、これらの修正は、None intentに関する情報の整合性を向上させ、読者が会話型AIの応答を管理する際の助けとなることを目指しています。

## articles/ai-services/language-service/conversational-language-understanding/faq.md{#item-590d89}

<details>
<summary>Diff</summary>
````diff
@@ -57,7 +57,7 @@ Unlike LUIS, you can't label the same text as two different entities. Learned co
 
 ## Can I import a LUIS JSON file into conversational language understanding?
 
-Yes, you can [import any LUIS application](./how-to/migrate-from-luis.md) JSON file from the latest version in the service.
+Yes, you can [import any LUIS application](/previous-versions/azure/ai-services/qnamaker/overview/overview) JSON file from the latest version in the service.
 
 ## Can I import a LUIS `.LU` file into conversational language understanding?
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQガイドの更新"
}
```

### Explanation
このコードの差分は、会話型言語理解に関するFAQガイドの小規模な修正を示しています。具体的には、LUIS（Language Understanding Intelligent Service）アプリケーションのインポートについての記述が更新されています。

修正内容としては、「LUISアプリケーションをインポートする」という質問に対する回答で、リンク先のURLが変更されています。元のリンクが`./how-to/migrate-from-luis.md`から`/previous-versions/azure/ai-services/qnamaker/overview/overview`に変更されました。この更新により、ユーザーがLUISアプリケーションのインポートに関する情報をより適切に取得できるように配慮されています。

全体として、これらの修正は文書の精度を向上させ、読者が必要な情報を見つけやすくするためのものです。

## articles/ai-services/language-service/conversational-language-understanding/how-to/call-api.md{#item-ce9a73}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 12/17/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
 ---
@@ -17,19 +17,9 @@ You can query the deployment programmatically through the [prediction API](https
 
 ## Test deployed model
 
-You can use Microsoft Foundry to submit an utterance, get predictions, and visualize the results.
+Once your model is deployed, you can test it by sending prediction requests to evaluate its performance with real utterances. Testing helps you verify that the model accurately identifies intents and extracts entities as expected before integrating it into your production applications. You can test your deployment using either the REST API or the Azure SDK client libraries.
 
-[!INCLUDE [Test model](../includes/language-studio/test-model.md)]
-
----
-
-## Send a conversational language understanding request
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Get prediction URL](../includes/language-studio/get-prediction-url.md)]
-
-# [REST APIs](#tab/REST-APIs)
+###  Send a conversational language understanding request
 
 First you need to get your resource key and endpoint:
 
@@ -39,9 +29,6 @@ First you need to get your resource key and endpoint:
 
 [!INCLUDE [Query model](../includes/rest-api/query-model.md)]
 
-# [Client libraries (Azure SDK)](#tab/azure-sdk)
-
-### Use the client libraries (Azure SDK)
 
 You can also use the client libraries provided by the Azure SDK to send requests to your model.
 
@@ -74,8 +61,6 @@ You can also use the client libraries provided by the Azure SDK to send requests
     * [C#](/dotnet/api/azure.ai.language.conversations)
     * [Python](/python/api/azure-ai-language-conversations/azure.ai.language.conversations.aio)
 
----
-
 ## Next steps
 
 * [Conversational language understanding overview](../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "API呼び出しガイドの更新"
}
```

### Explanation
このコードの差分は、会話型言語理解に関するAPI呼び出しガイドの修正を示しています。主に内容の整理と明確化が行われており、特にモデルのテスト方法やリクエストの送信に関する説明が強化されています。

変更点の一部として、モデルのデプロイ後にテストを行う手順が具体的に記述され、実際の発話を用いてモデルのパフォーマンスを評価する方法が詳述されています。この新しい説明により、読者はテストの重要性を理解し、正確に意図を特定しエンティティを抽出することを確認できるようになります。

さらに、古い情報が削除され、よりスムーズな文書構造が構築されています。特に、APIリクエストの送信に関するセクションが明確に再編成され、リソースキーの取得方法やREST APIおよびAzure SDKの利用法が整理されています。

全体として、これらの修正は、ユーザーが実際のプロダクションアプリケーションに統合する前に、会話型AIモデルの性能を適切に評価できるよう支援することを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/deploy-model.md{#item-b64101}

<details>
<summary>Diff</summary>
````diff
@@ -26,12 +26,6 @@ For more information, *see* [project development lifecycle](../overview.md#proje
 
 After you review the model's performance and decide it can be used in your environment, you need to assign it to a deployment to be able to query it. Assigning the model to a deployment makes it available for use through the [prediction API](/rest/api/language/2023-04-01/conversation-analysis-runtime/analyze-conversation). We recommend creating a deployment named `production` to which you assign the best model you built so far and use it in your system. You can create another deployment called `staging` to which you can assign the model you're currently working on to be able to test it. You can have a maximum on 10 deployments in your project. 
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Deploy a model using Language Studio](../includes/language-studio/deploy-model.md)]
-   
-# [REST APIs](#tab/rest-api)
-
 ### Submit deployment job
 
 [!INCLUDE [deploy model](../includes/rest-api/deploy-model.md)]
@@ -40,7 +34,6 @@ After you review the model's performance and decide it can be used in your envir
 
 [!INCLUDE [get deployment status](../includes/rest-api/get-deployment-status.md)]
 
----
 
 ## Swap deployments
 
@@ -50,56 +43,26 @@ After you're done testing a model assigned to one deployment, you might want to
 
 For example, you can swap your `production` and `staging` deployments when you want to take the model assigned to `staging` and assign it to `production`. 
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Swap deployments](../includes/language-studio/swap-deployment.md)]
-
-# [REST APIs](#tab/rest-api)
-
 [!INCLUDE [Swap deployments](../includes/rest-api/swap-deployment.md)]
 
----
-
 ## Delete deployment
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Delete deployment](../includes/language-studio/delete-deployment.md)]
-
-# [REST APIs](#tab/rest-api)
-
 [!INCLUDE [Delete deployment](../includes/rest-api/delete-deployment.md)]
 
----
 
 ## Assign deployment resources
 
 You can [deploy your project to multiple regions](../../concepts/custom-features/multi-region-deployment.md) by assigning different Language resources that exist in different regions. 
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Assign resource](../includes/language-studio/assign-resources.md)]
-
-# [REST APIs](#tab/rest-api)
-
 [!INCLUDE [Assign resource](../includes/rest-api/assign-resources.md)]
 
----
-
 ## Unassign deployment resources
 
 When unassigning or removing a deployment resource from a project, you also delete all the deployments that are deployed to the resource's region.
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Unassign resource](../includes/language-studio/unassign-resources.md)]
-
-# [REST APIs](#tab/rest-api)
 
 [!INCLUDE [Unassign resource](../includes/rest-api/unassign-resources.md)]
 
----
-
 ## Next steps
 
 * Use [prediction API to query your model](call-api.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルデプロイガイドの大幅な改訂"
}
```

### Explanation
このコードの差分は、会話型言語理解に関するモデルデプロイガイドの大幅な改訂を示しています。主に情報の削除と構成の変更が行われており、特に「Language Studio」に関するサポート情報が多数削除されています。

具体的な変更点として、モデルをデプロイする際の手順から、タブ形式で提供されていた「Language Studio」や「REST API」に関する情報が大幅に削除されました。また、デプロイメントの申請やスワップ、削除に関する説明が可能な限り簡略化されていますが、重要なアクションに関する説明は残されており、モデルの性能を吟味した後に展開するための基本的なガイドラインは引き続き提供されています。

新しい文書構成により、ユーザーはモデルをデプロイする際の具体的な手順や運用方法に焦点を合わせやすくなりましたが、一方で、簡略化された情報により詳細を求めるユーザーにとっては物足りなさを感じるかもしれません。全体として、これらの変更は、ガイドの流れをシンプルにし、主要な手順に対する焦点を明確化することを目的としています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/view-model-evaluation.md{#item-f0ecb3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 11/18/2025
+ms.date: 12/17/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
@@ -28,44 +28,17 @@ See the [project development lifecycle](../overview.md#project-development-lifec
 
 ## Model details
 
-### [Microsoft Foundry](#tab/azure-ai-foundry)
-
-[!INCLUDE [Model performance](../includes/language-studio/model-performance.md)]
-
-### [REST APIs](#tab/REST-APIs)
-
 [!INCLUDE [Evaluate model](../includes/rest-api/model-evaluation.md)]
 
----
-
 ## Load or export model data
 
-### [Foundry](#tab/azure-ai-foundry)
-
-[!INCLUDE [Load export model](../includes/language-studio/load-export-model.md)]
-
-
-### [REST APIs](#tab/REST-APIs)
-
 [!INCLUDE [Load export model](../includes/rest-api/load-export-model.md)]
 
----
-
 ## Delete model
 
-### [Foundry](#tab/azure-ai-foundry)
-
-[!INCLUDE [Delete model](../includes/language-studio/delete-model.md)]
-
-
-### [REST APIs](#tab/REST-APIs)
-
 [!INCLUDE [Delete model](../includes/rest-api/delete-model.md)]
 
 
----
-
-
 ## Next steps
 
 * As you review your how your model performs, learn about the [evaluation metrics](../concepts/evaluation-metrics.md) that are used.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル評価ガイドの簡素化"
}
```

### Explanation
このコードの差分は、会話型言語理解に関するモデル評価ガイドの簡素化を示しています。主な変更は、不要な情報や重複するセクションの削除によるもので、内容が整理されています。

具体的には、モデルの詳細や操作に関するタブ形式の情報が幾つか削除され、よりシンプルな構成に事務がされました。これにより、ユーザーが特定の情報にアクセスしやすくなる一方、情報のボリュームが減少しています。特に、「Microsoft Foundry」や「REST API」に関する情報が削除され、モデル評価に関する内容が中心にまとまっています。

さらに、ドキュメントの日付が更新されており、最新の情報が反映されています。全体の流れとして、使用者がモデルの評価を行う際に必要な情報を速やかに見つけられるよう配慮されていますが、情報の削除により、詳細を求めるユーザーには物足りなさを感じさせる可能性もあります。この変更は、ユーザーの利便性向上を目的として行われたものです。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/assign-resources.md{#item-e82d92}

<details>
<summary>Diff</summary>
````diff
@@ -1,16 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To assign deployment resources in other regions in [Language Studio](https://aka.ms/LanguageStudio):
-  1. Make sure you assign yourself as a [Cognitive Services Language Owner](https://aka.ms/rbac-language) to the resource you used to create the project.
-  2. Go to the **Deploying a model** page in Language Studio.
-  3. Select the **Regions** tab.
-  4. Select **Add deployment resource**.
-  5. Select a Language resource in another region.
-  
-You're now ready to deploy your project to the regions you designated for your resources.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "リソース割り当てガイドの削除"
}
```

### Explanation
このコードの差分は、会話型言語理解の「Language Studio」におけるリソース割り当てに関するガイドが削除されたことを示しています。この変更により、リソースを他の地域に割り当てるための具体的な手順が文書から取り除かれました。

削除された内容には、Cognitive Services Language Ownerとしての権限の取得、Language Studioでのモデルデプロイページへのアクセス、地域の選択、デプロイメントリソースの追加方法などが含まれていました。この情報は、ユーザーがプロジェクトを特定の地域にデプロイするための重要な手順を提供していましたが、現在はすべて削除されています。

この変更は、情報の整理や文書の簡素化を目的としている可能性がありますが、ユーザーにとってはリソース割り当てに関する具体的な情報が欠如し、混乱を招く恐れがあります。全体として、この削除は重大な影響を及ぼす可能性があり、ユーザーが役立つ情報を見つけるのが難しくなるかもしれません。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/cancel-training.md{#item-c68e58}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To cancel a training job from within [Language Studio](https://aka.ms/laguageStudio)
-
-1. In the **Train model** page, select the training job you want to cancel and select **Cancel** from the top menu. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "トレーニングキャンセル手順の削除"
}
```

### Explanation
このコードの差分は、会話型言語理解に関する「Language Studio」におけるトレーニングジョブのキャンセル手順が削除されたことを示しています。この削除により、ユーザーがトレーニングジョブをキャンセルするための具体的な手順が文書から消えています。

削除された内容には、「Train model」ページでキャンセルしたいトレーニングジョブを選択し、上部メニューから「Cancel」を選ぶという明確な手順が含まれていました。この情報は、ユーザーがトレーニングプロセスを管理する上で非常に重要でしたが、現時点ではその手順が提供されなくなったため、ユーザーには不便さをもたらすかもしれません。

この変更は、ドキュメントの整理や情報の簡素化を目的としている可能性がありますが、それによってユーザーが必要な操作を行う際に困難さが生じる可能性があるため、注意が必要です。全体として、この削除は重要な機能に関する情報を失わさせる重大な変更と見なされます。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/create-project.md{#item-0172b6}

<details>
<summary>Diff</summary>
````diff
@@ -1,26 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. In [Language Studio](https://aka.ms/languageStudio), find the section named **Understand questions and conversational language** and select **Conversational Language Understanding**.
-
-    :::image type="content" source="../../media/select-custom-clu.png" alt-text="A screenshot that shows the location of Custom Language Understanding on Azure Language Studio landing page." lightbox="../../media/select-custom-clu.png":::
-
-1. When the **Conversational Language Understanding projects** page opens, select **Create new project**.
-
-    :::image type="content" source="../../media/projects-page.png" alt-text="A screenshot that shows the conversation project page in Language Studio." lightbox="../../media/projects-page.png":::
-
-1. To create a new project, provide the following information:
-
-    |Value  | Description  |
-    |---------|---------|
-    |Name     | A name for your project. After you create it, the name can't be changed.  |
-    |Description    | Optional project description.        |
-    |Utterances primary language     | The primary language of your project. Your training data should primarily be in this language.        |
-    |Enable multiple languages    |  Whether you want to enable your project to support [multiple languages](../../language-support.md#multi-lingual-option) at once.       |
-
-1. After you finish, select **Create**. You should now see the **Getting started** landing page for your project.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト作成手順の削除"
}
```

### Explanation
このコードの差分は、「Language Studio」における新規プロジェクトの作成手順が削除されたことを示しています。この変更により、ユーザーが会話型言語理解で新しいプロジェクトを作成するための具体的な手順が文書から取り除かれました。

削除された内容には、Language Studioでの「Conversational Language Understanding」セクションの選択から始まり、新しいプロジェクト作成の際に必要な情報（プロジェクト名、説明、主言語、複数言語のサポートの有無）を入力する手順が含まれていました。また、プロジェクト作成後に表示される「Getting started」ページについての情報も含まれていました。

この変更は、ドキュメントの整頓や管理の観点から行われた可能性がありますが、ユーザーにとっては新しいプロジェクトを作成する際の貴重な情報が失われてしまうことになります。そのため、利用者がプロジェクト設計を行う上での手助けがなくなり、操作の難易度が上がる恐れがあります。全体として、この削除は重大な影響をもたらす可能性があり、ユーザー体験を損なうリスクがあります。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/delete-deployment.md{#item-22b6f8}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To delete a deployment from within [Language Studio](https://aka.ms/laguageStudio), select the **Deploy model** page. Then select the deployment you want to delete, and select **Delete deployment** from the top menu. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デプロイメント削除手順の削除"
}
```

### Explanation
このコードの差分は、「Language Studio」におけるデプロイメントの削除手順が削除されたことを示しています。この変更により、ユーザーがデプロイしたモデルを削除するための具体的な手順が文書から消えています。

削除された内容には、Language Studio内で「Deploy model」ページを選択し、削除したいデプロイメントを選択して上部メニューから「Delete deployment」を選ぶという操作手順が含まれていました。これらの手順は、ユーザーがデプロイしているモデルの管理において非常に重要な情報でした。

この変更は、ドキュメントの更新や内容の整理を意図して行われた可能性がありますが、ユーザーにとってはデプロイメントを削除する際の具体的なガイダンスが失われているため、利便性が低下する恐れがあります。このため、全体としてこの削除はユーザーエクスペリエンスに影響を及ぼす重大な変更と考えられます。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/delete-model.md{#item-d4b2d9}

<details>
<summary>Diff</summary>
````diff
@@ -1,15 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To delete your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Model performance** from the left side menu.
-
-2. Select the **model name** you want to delete and select **Delete** from the top menu.
-
-3. In the window that appears, select **OK** to delete the model. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル削除手順の削除"
}
```

### Explanation
このコードの差分は、「Language Studio」におけるモデルの削除手順が削除されたことを示しています。この変更により、ユーザーが自分のモデルを削除する際に必要な具体的な手順が文書から消えてしまいました。

削除された内容には、Language Studioの左側メニューから「Model performance」を選択し、削除したいモデルの名前を選択した後、上部メニューから「Delete」を選ぶという手順が含まれていました。さらに、表示されるウィンドウで「OK」を選択することでモデルを削除できるという説明もありました。

この変更は、ドキュメントを整理するために行われた可能性がありますが、ユーザーにとってはモデルを管理するための重要な情報が失われてしまいます。このため、全体としてこの削除はユーザーエクスペリエンスに悪影響を及ぼす恐れがあり、特にモデルの削除を初めて行うユーザーにとっては不便さを感じることになるでしょう。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/delete-project.md{#item-01c6cb}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-When you don't need your project anymore, you can use Language Studio to delete your project. On the left pane, select **Projects**, select the project that you want to delete, and then select **Delete** from the top menu.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト削除手順の削除"
}
```

### Explanation
このコードの差分は、「Language Studio」におけるプロジェクトの削除手順が削除されたことを示しています。この変更により、ユーザーがプロジェクトを削除するための詳細な手順が文書内から消えてしまいました。

削除された内容には、使わなくなったプロジェクトを削除する方法として、左側のパネルから「Projects」を選択し、削除したいプロジェクトを選んだ後、上部メニューから「Delete」を選択するという手順が記載されていました。この説明は、プロジェクト管理を行う上で重要なガイダンスを提供していました。

この変更は、ドキュメントの見直しや更新の一環で行われた可能性がありますが、ユーザーにとってはプロジェクトを削除する際の具体的な指示が欠落するため、利便性が低下する懸念があります。特に新しいユーザーや今までその手順を意識していなかったユーザーにとって、この情報が失われることは大きな影響を及ぼすでしょう。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/deploy-model.md{#item-b70ddc}

<details>
<summary>Diff</summary>
````diff
@@ -1,28 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To deploy your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Deploying a model** from the left side menu.
-
-1. Select **Add deployment** to start the **Add deployment** wizard.
-
-    :::image type="content" source="../../media/add-deployment-model.png" alt-text="A screenshot showing the model deployment button in Language Studio." lightbox="../../media/add-deployment-model.png":::
-
-1. Select **Create a new deployment name** to create a new deployment and assign a trained model from the dropdown below. You can otherwise select **Overwrite an existing deployment name** to effectively replace the model that's used by an existing deployment.
-
-    > [!NOTE]
-    > Overwriting an existing deployment doesn't require changes to your [Prediction API](https://aka.ms/clu-runtime-api) call but the results you get will be based on the newly assigned model.
-    
-    :::image type="content" source="../../media/create-deployment-job.png" alt-text="A screenshot showing the screen for adding a new deployment in Language Studio." lightbox="../../media/create-deployment-job.png":::
-
-1. Select a trained model from the **Model** dropdown. 
-
-1. Select **Deploy** to start the deployment job.
-
-1. After deployment is successful, an expiration date will appear next to it. [Deployment expiration](../../../concepts/model-lifecycle.md#expiration-timeline) is when your deployed model will be unavailable to be used for prediction, which typically happens **twelve** months after a training configuration expires.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルデプロイ手順の削除"
}
```

### Explanation
このコードの差分は、「Language Studio」におけるモデルのデプロイ手順が削除されたことを示しています。この変更により、ユーザーがモデルをデプロイするための具体的な手順が文書から消えてしまいました。

削除された内容には、Language Studioからモデルをデプロイする方法として、左側メニューから「Deploying a model」を選択し、「Add deployment」を選択することでデプロイメントウィザードを開始する手順が説明されていました。また、新しいデプロイメント名を作成し、トレーニングされたモデルを選択する方法や、既存のデプロイメントを上書きする際の注意点も含まれていました。さらに、デプロイメントが成功した後に表示される有効期限に関する説明もありました。

この変更は、文書の整理や更新の一環である可能性がありますが、ユーザーにとってはモデルをデプロイする際の重要な情報が欠落するため、実務上の不便さが生じる恐れがあります。特に、初めてモデルをデプロイしようとするユーザーや、手順に依存していたユーザーにとって、この情報の欠如は大きな影響を及ぼす可能性があります。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/get-prediction-url.md{#item-566371}

<details>
<summary>Diff</summary>
````diff
@@ -1,19 +0,0 @@
----
-titleSuffix: Foundry Tools
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
-ms.custom: language-service-clu 
----
-1. After the deployment job is completed successfully, select the deployment you want to use and from the top menu select **Get prediction URL**.
-
-    :::image type="content" source="../../media/prediction-url.png" alt-text="A screenshot showing the prediction URL in Language Studio." lightbox="../../media/prediction-url.png":::
-
-2. In the window that appears, copy the sample request URL and body into your command line.
-
-3. Replace `<YOUR_QUERY_HERE>` with the actual text you want to send to extract intents and entities from.
-
-4. Submit the `POST` cURL request in your terminal or command prompt. You receive a 202 response with the API results if the request was successful.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "予測URLを取得する手順の削除"
}
```

### Explanation
このコードの差分は、「Language Studio」における予測URLを取得する手順が削除されたことを示しています。この変更により、デプロイメントが完了した後にユーザーが予測URLを取得するための具体的な手順が文書から消えてしまいました。

削除された内容には、デプロイメントが成功した後に使用するデプロイメントを選択し、上部メニューから「Get prediction URL」を選択する方法が説明されていました。また、表示されるウィンドウからサンプルリクエストURLとボディをコマンドラインにコピーし、実際のクエリテキストを指定して`POST`リクエストを送信する手順も含まれていました。このプロセスにより、ユーザーは意図やエンティティを抽出するためのAPIを利用することができるようになっていました。

この変更は、ドキュメントの整理や更新の一環で行われた可能性がありますが、ユーザーにとっては予測URLを取得するための具体的な指示が欠落するため、実務上の不便さが生じる恐れがあります。特に、新規ユーザーやこの手順に依存していたユーザーにとっては、この情報の不足が大きな影響を及ぼすことが考えられます。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/import-project.md{#item-de782b}

<details>
<summary>Diff</summary>
````diff
@@ -1,20 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Under the **Understand questions and conversational language** section of Language Studio, select **Conversational language understanding**.
-
-    :::image type="content" source="../../media/select-custom-clu.png" alt-text="A screenshot showing the location of Custom Language Understanding in Azure Language Studio landing page." lightbox="../../media/select-custom-clu.png":::
-
-
-1. This step navigates you to the **Conversational language understanding projects** page. Next to the **Create new project** button select **Import**.
-
-    :::image type="content" source="../../media/projects-page.png" alt-text="A screenshot showing the conversation project page in Language Studio." lightbox="../../media/projects-page.png":::
-
-
-1. In the window that appears, upload the JSON file you want to import. Make sure that your file follows the [supported JSON format](../../concepts/data-formats.md).
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクトのインポート手順の削除"
}
```

### Explanation
このコードの差分は、Language Studioにおけるプロジェクトのインポート手順が削除されたことを示しています。この変更により、ユーザーが既存のプロジェクトをインポートするための具体的なステップが文書から削除されました。

削除された内容には、「Understand questions and conversational language」セクション内で「Conversational language understanding」を選択し、次に「Create new project」ボタンの隣にある「Import」を選択する方法が記載されていました。また、表示されるウィンドウでインポートしたいJSONファイルをアップロードする手順も含まれており、その際にファイルがサポートされているJSONフォーマットに従っていることを確認する必要があることも説明されていました。

この変更は、文書の簡素化や情報更新の一環で行われた可能性がありますが、ユーザーにとってはプロジェクトをインポートするための重要な手順が欠落するため、実務上の不便が生じる恐れがあります。特に、プロジェクトのインポートを必要とするユーザーにとって、この情報の不足は大きな影響を及ぼす可能性があると考えられます。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/load-export-model.md{#item-dfdc28}

<details>
<summary>Diff</summary>
````diff
@@ -1,23 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To **load** your model data:
-
-1. Select any model in the **model evaluation** page.
-
-2. Select the **Load model data** button. 
-
-3. Confirm that you don't have any unsaved changes you need to capture in window that appears, and select **Load data**. 
-
-4. Wait until your model data finishes loading back into your project. On completion, you're redirected back to the **Schema design** page. 
-
-To **export** your model data:
-
-1. Select any model in the **model evaluation** page.
-
-2.  Select the **Export model data** button. Wait for the JSON snapshot of your model to be downloaded locally. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルデータの読み込みおよびエクスポート手順の削除"
}
```

### Explanation
このコードの差分は、Language Studioにおけるモデルデータの読み込みおよびエクスポート手順が削除されたことを示しています。この変更により、ユーザーがモデルデータを読み込むための具体的な手順およびエクスポートする方法が文書から削除されました。

削除された内容には、モデル評価ページでの任意のモデルを選択し、「Load model data」ボタンをクリックすることでモデルデータを読み込む手順が含まれていました。また、表示されるウィンドウで未保存の変更がないことを確認し、「Load data」を選択すること、そしてモデルデータの読み込みが完了すると「Schema design」ページにリダイレクトされることが記載されていました。

さらに、モデルデータをエクスポートする手順として、同様にモデル評価ページで任意のモデルを選択し、「Export model data」ボタンをクリックすることでJSONスナップショットをローカルにダウンロードする方法も説明されていました。

この変更は、ドキュメントの簡素化や情報の移行を目的として行われた可能性がありますが、ユーザーにとっては重要な操作手順が欠落することにより、実務上の問題が生じることが考えられます。特に、モデルデータの読み込みやエクスポートを必要とするユーザーにとっては、必要な情報の不足が大きな影響を及ぼす可能性があります。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/model-performance.md{#item-3a099d}

<details>
<summary>Diff</summary>
````diff
@@ -1,64 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Go to your project page in [Language Studio](https://aka.ms/languageStudio).
-
-2. Select **Model performance** from the menu on the left side of the screen.
-
-3. On this page, you can only view the successfully trained models, F1 score of each model and [model expiration date](../../../concepts/model-lifecycle.md#expiration-timeline). You can select the model name for more details about its performance. Models only include evaluation details if there was test data selected while training the model.
-
-### [Overview](#tab/overview)
-
-* In this tab you can view the model's details such as: F1 score, precision, recall, date, and time for the training job, total training time, and number of training and testing utterances included in this training job. You can view details between intents or entities by selecting Model Type at the top.
-
-    :::image type="content" source="../../media/overview.png" alt-text="A screenshot that shows the overview page for model evaluation." lightbox="../../media/overview.png":::
-
-* You can also see [guidance](../../concepts/evaluation-metrics.md#guidance) on how to improve the model. When you select the *view details*, a side panel opens to give more guidance on how to improve the model.
-
-    :::image type="content" source="../../media/overview-guidance.png" alt-text="A screenshot that shows the guidance page for model evaluation." lightbox="../../media/overview-guidance.png":::
-
-### [Model type performance](#tab/model-performance)
-
-* This information is a snapshot of how your model performed during testing. The metrics here are static and tied to your model, so they don't update until you train again.
-
-* You can see for each intent or entity the precision, recall, F1 score, number of training and testing labels. Entities that don't include a learned component shows no training labels. A learned component is added only by adding labels in your training set.
-
-
-    :::image type="content" source="../../media/model-type-performance.png" alt-text="A screenshot of model performance." lightbox="../../media/model-type-performance.png":::
-
-### [Test set details](#tab/test-set)
-
-* Here you can see the utterances included in the **test set** and their intent or entity predictions. You can use the *Show errors only* toggle to show only the utterances where there are different predictions from their labels, or unselect the toggle to view all utterances in the test set. You can also toggle the view between **Showing entity labels** as the view for each utterance, or **Showing entity predictions**. Entity predictions show as dotted lines and labels show as solid lines.
-
- * You can expand each row to view its intent or entity predictions, specified by the **Model Type** column. The **Text** column shows the text of the entity that was predicted or labeled. Each row has a **Labeled as** column to indicate the label in the test set, and **Predicted as** column to indicate the actual prediction. Also, you can see whether it's a [true positive](../../concepts/evaluation-metrics.md), [false positive](../../concepts/evaluation-metrics.md), or [false negative](../../concepts/evaluation-metrics.md) in the **Result Type** column. 
-
-    :::image type="content" source="../../media/test-set.png" alt-text="A screenshot of test set details." lightbox="../../media/test-set.png":::    
-
-### [Dataset distribution](#tab/dataset-distribution) 
-
-This snapshot shows how intents or entities are distributed across your training and testing sets. This data is static and tied to your model, so it doesn't update until you train again. Entities that don't include a learned component shows no training labels. A learned component is added only by adding labels in your training set.
-
-  :::image type="content" source="../../media/dataset-table.png" alt-text="A screenshot showing distribution in table view." lightbox="../../media/dataset-table.png":::
-
-### [Confusion matrix](#tab/confusion-matrix) 
-
-A [confusion matrix](../../concepts/evaluation-metrics.md#confusion-matrix) is an N x N matrix used for evaluating the performance of your model, where N is the number of target intents or entities. The matrix compares the expected labels with the data predicted by the model to identify which intents or entities are being misclassified as other intents and entities. You can select into any cell of the confusion matrix to identify exactly which utterances contributed to the values in that cell.
-
-You can view the intent confusion matrix in *raw count* or *normalized* view. Raw count is the actual number of utterances predicted and labeled for a set of intents. Normalized value is the ratio, between 0 and 1, of the predicted and labeled utterances for a set of intents.
-
-You can view the entity confusion matrix in *character overlap count* or *normalized character overlap* view. Character overlap count is the actual number of spans that are predicted and labeled for a set of entities. Normalized character overlap is the ratio, between 0 and 1, of the predicted and labeled spans for a set of entities. Sometimes entities can be predicted or labeled partially, leading to decimal values in the confusion matrix.
-
-  :::image type="content" source="../../media/confusion.png" alt-text="A screenshot of a confusion matrix in Language Studio." lightbox="../../media/confusion.png":::
-
-* All values: It shows the confusion matrix for all intents or entities.
-
-* Only errors: It shows the confusion matrix for intents or entities with errors only.
-
-* Only matches: It shows the confusion matrix for intents or entities with correct predictions only.
-
----
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルパフォーマンスの手順の削除"
}
```

### Explanation
このコードの差分は、Language Studioにおけるモデルパフォーマンスに関する手順および情報が削除されたことを示しています。具体的には、モデルのパフォーマンス情報を表示するための詳細な手順や、評価メトリクス、混同行列の説明が含まれていた文書が取り除かれました。

削除された内容には、ユーザーがプロジェクトページで「Model performance」を選択することでアクセスできる情報が含まれていました。このページでは、成功裏に訓練されたモデルのF1スコア、モデルの有効期限などの詳細を確認できました。また、モデルのパフォーマンスを改善するためのガイダンスや、各意図やエンティティに関連する精度や再現率、混同行列の表示方法についても具体的な説明がなされていました。

これにより、ユーザーはどのようにしてモデルのパフォーマンスを把握し、必要に応じて改善するかの具体的な手順を失うことになります。この変更は、情報の簡素化や再編成を目的としていると思われるものの、モデル評価を行うための重要な情報が欠落することで、ユーザーにとって実務上の課題が生じる可能性があります。特に、モデルのパフォーマンスを評価し、改善点を見出したいユーザーにとっては大きな影響を及ぼすかもしれません。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/project-details.md{#item-4baebc}

<details>
<summary>Diff</summary>
````diff
@@ -1,18 +0,0 @@
----
-titleSuffix: Foundry Tools
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Go to your **Project settings** page in [Language Studio](https://aka.ms/languageStudio).
-
-1. Review your project details.
-
-1. On this page, you can update your project description and enable or disable **Multi-lingual dataset** in project settings.
-
-1. You can also retrieve your resource primary key from this page.
-
-    :::image type="content" source="../../media/project-details.png" alt-text="A screenshot that shows the Project settings page." lightbox="../../media/project-details.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト詳細設定手順の削除"
}
```

### Explanation
このコードの差分は、Language Studioにおけるプロジェクト詳細の設定方法に関する手順が削除されたことを示しています。具体的には、プロジェクト設定ページへのアクセス方法や、プロジェクトの詳細情報を確認する手順が文書から削除されました。

削除された内容には、ユーザーがLanguage Studioの「Project settings」ページに移動し、プロジェクトの説明を更新したり、プロジェクト設定で「Multi-lingual dataset」のオン/オフを切り替えたりできる手順が含まれていました。また、リソースのプライマリキーをこのページから取得できることについても触れられていました。

この変更により、ユーザーはプロジェクト設定の操作に関する具体的な手順を失うことになります。特にプロジェクトの詳細を管理したいユーザーにとって、必要な情報が欠落しているため、実務上の問題が生じるかもしれません。プロジェクトの構成や設定を簡単に管理するためのガイダンスが失われることは、ユーザーの体験に影響を与える可能性があります。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/sign-in-studio.md{#item-6f8bd7}

<details>
<summary>Diff</summary>
````diff
@@ -1,21 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Go to the [Language Studio](https://aka.ms/languageStudio) and sign in with your Azure account. 
-
-1. In the **Choose a language resource** window that appears, find your Azure subscription, and choose your Language resource. If you don't have a resource, you can create a new one.
-
-    |Instance detail  |Required value  |
-    |---------|---------|
-    |Azure subscription | Your Azure subscription.           |
-    |Azure resource group | Your Azure resource group name. |
-    |Azure resource name |  Your Azure resource name.        |
-    |Location | One of the [supported regions](../../service-limits.md#regional-availability) for your Language resource. An example is West US 2.     |
-    |Pricing tier     | One of the valid [pricing tiers](../../service-limits.md#language-resource-limits) for your Language resource. You can use the Free (F0) tier to try the service.  |
-    
-    :::image type="content" source="../../media/quickstart-language-resource.png" alt-text="A screenshot that shows the resource selection screen in Language Studio." lightbox="../../media/quickstart-language-resource.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioサインイン手順の削除"
}
```

### Explanation
このコードの差分は、Language Studioへのサインインに関する手順が削除されたことを示しています。具体的には、ユーザーがAzureアカウントを使用してLanguage Studioにサインインする方法や、適切な言語リソースを選択する手順が文書から除かれました。

削除された内容には、サインイン後に表示される「Choose a language resource」ウィンドウで、Azureのサブスクリプションや言語リソースを選択する際に必要な情報、例えばAzureサブスクリプション名、リソースグループ名、リソース名、地域、価格帯などが含まれていました。また、リソース選択画面を示すスクリーンショットも含まれていました。

この変更により、ユーザーはLanguage Studioにサインインするための具体的な手順や必要な情報を失うことになります。特に新しくAzureを使用するユーザーや、初めてLanguage Studioにアクセスしようとするユーザーにとって、必要なガイダンスが欠如することで、サインインプロセスが混乱を招く可能性があります。これにより、ユーザーの利便性や体験が損なわれる恐れがあります。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/swap-deployment.md{#item-251c71}

<details>
<summary>Diff</summary>
````diff
@@ -1,15 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To swap deployments from within [Language Studio](https://aka.ms/laguageStudio)
-
-1. In the **Deploy model** page, select the two deployments you want to swap and select **Swap deployments** from the top menu. 
-
-2. From the window that appears, select the names of the deployments you want to swap.
-
-    :::image type="content" source="../../media/swap-deployment.png" alt-text="A screenshot showing a swapped deployment in Language Studio." lightbox="../../media/swap-deployment.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デプロイメントのスワップ手順の削除"
}
```

### Explanation
このコードの差分は、Language Studioにおけるデプロイメントのスワップ手順が削除されたことを示しています。具体的には、ユーザーがLanguage Studio内で2つのデプロイメントを交換する方法についての指示が含まれていた部分がなくなりました。

削除された内容には、「Deploy model」ページでデプロイメントを選択し、上部メニューから「Swap deployments」を選ぶ手順や、表示されるウィンドウからスワップしたいデプロイメントの名前を選ぶ方法が含まれていました。また、スワップ操作を示すスクリーンショットも併せて削除されています。

この変更により、ユーザーはデプロイメントを交換するための具体的な手順を失うことになります。特にデプロイメントの管理が重要な役割を果たすユーザーにとって、必要な情報が欠如することは、作業の効率を低下させる原因となる可能性があります。そのため、ユーザーの利便性や操作性に対して悪影響を及ぼすことが懸念されます。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/test-model.md{#item-98e559}

<details>
<summary>Diff</summary>
````diff
@@ -1,23 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To test your deployed models from within the [Language Studio](https://aka.ms/LanguageStudio):
-1. Select **Testing deployments** from the left side menu.
-
-1. For multilingual projects, from the **Select text language** dropdown, select the language of the utterance you're testing.
-
-1. From the **Deployment name** dropdown, select the deployment name corresponding to the model that you want to test. You can only test models that are assigned to deployments.
-
-1. In the text box, enter an utterance to test. For example, if you created an application for email-related utterances you could enter *Delete this email*. 
-
-1. Towards the top of the page, select **Run the test**.
-
-1. After you run the test, you should see the response of the model in the result. You can view the results in entities cards view or view it in JSON format.
-
-    <!--:::image type="content" source="../../media/test-model.png" alt-text="A screenshot showing testing the model." lightbox="../../media/test-model.png":::-->
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルテスト手順の削除"
}
```

### Explanation
このコードの差分は、Language Studio内でデプロイされたモデルをテストする手順が削除されたことを示しています。具体的には、ユーザーが自分のデプロイされたモデルをテストする際の手順についての詳細が含まれていた部分が削除されています。

削除された内容には、左側のメニューから「Testing deployments」を選択することや、マルチリンガルプロジェクトの場合の言語選択、テストするモデルに対応するデプロイメント名の選択、テストのための発話をテキストボックスに入力する方法、テストを実行するための選択肢、そしてモデルの応答や結果を表示する方法が含まれていました。また、テスト手順を示すスクリーンショットも削除されています。

この変更により、ユーザーはモデルテストを行うための具体的な手続きや注意事項に関する情報を失うことになります。特に、自身のアプリケーションの動作を確認したいユーザーにとって、この手順の欠如は大きな障壁となり、新しいユーザーがモデルを正しくテストできない原因となる可能性があります。このため、ユーザーの体験や作業の効率に対して悪影響を及ぼすことが懸念されます。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/train-model.md{#item-dd4473}

<details>
<summary>Diff</summary>
````diff
@@ -1,32 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To start training your model from within the [Language Studio](https://aka.ms/languageStudio):
-
-1. Select **Train model** from the left side menu.
-
-2. Select **Start a training job** from the top menu.
-
-3. Select **Train a new model** and enter a new model name in the text box. Otherwise to replace an existing model with a model trained on the new data, select **Overwrite an existing model** and then select an existing model. Overwriting a trained model is irreversible, but it won't affect your deployed models until you deploy the new model.
-
-4. Select training mode. You can choose **Standard training** for faster training, but it is only available for English. Or you can choose **Advanced training** which is supported for other languages and multilingual projects, but it involves longer training times. Learn more about [training modes](../../how-to/train-model.md#training-modes).
-    
-
-5. Select a [data splitting](../../how-to/train-model.md#data-splitting) method. You can choose **Automatically splitting the testing set from training data** where the system will split your utterances between the training and testing sets, according to the specified percentages. Or you can **Use a manual split of training and testing data**, this option is only enabled if you added utterances to your testing set when you [labeled your utterances](../../how-to/tag-utterances.md). 
-
-6. Select the **Train** button.
-
-    :::image type="content" source="../../media/train-model.png" alt-text="A screenshot showing the training page in Language Studio." lightbox="../../media/train-model.png":::
-
-7. Select the training job ID from the list. A panel will appear where you can check the training progress, job status, and other details for this job.
-
-    > [!NOTE]
-    > * Only successfully completed training jobs will generate models.
-    > * Training can take some time between a couple of minutes and couple of hours based on the count of utterances.
-    > * You can only have one training job running at a time. You can't start other training jobs within the same project until the running job is completed.
-    > * The machine learning used to train models is regularly updated. To train on a previous [configuration version](../../../concepts/model-lifecycle.md), select **Select here to change** from the **Start a training job** page and choose a previous version.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルのトレーニング手順の削除"
}
```

### Explanation
このコードの差分は、Language Studioにおけるモデルのトレーニング手順が削除されたことを示しています。この変更により、ユーザーが自分のモデルをトレーニングするための具体的なステップがなくなりました。

削除された内容には、左側メニューから「Train model」を選択し、「Start a training job」を選ぶ手順、モデルの名前を入力する際の選択肢（新しいモデルを作成するか、既存のモデルを上書きするか）、トレーニングモードの選択肢（標準トレーニングや高度なトレーニング）、データ分割の方法の選択、トレーニングの実行ボタンの選択などが含まれていました。また、トレーニング進捗状況やジョブステータスを確認するための手続きに関する情報も削除されています。

この変更により、ユーザーは言語モデルをトレーニングするための詳細な手引きを失うことになります。特に、トレーニングを行うことが重要なユーザーにとって、この情報の欠如は新しいユーザーにとって非常に困難をもたらす可能性があり、トレーニングプロセスの理解を妨げる要因となる可能性があります。したがって、ユーザー体験や作業の効率に対して悪影響が生じる懸念があります。

## articles/ai-services/language-service/conversational-language-understanding/includes/language-studio/unassign-resources.md{#item-446010}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To unassign or remove deployment resources in other regions using [Language Studio](https://aka.ms/LanguageStudio):
-1. Go to the **Regions** tab in the **Deploy a model** page.
-2. Select the resource you'd like to unassign.
-3. Select the **Remove assignment** button.
-4. In the window that appears, type the name of the resource you want to remove. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "リソースの割り当て解除手順の削除"
}
```

### Explanation
このコードの差分は、Language Studioを使用してデプロイメントリソースを他のリージョンから割り当て解除または削除する手順が削除されたことを示しています。この変更により、ユーザーがリソースを管理する際の具体的なガイダンスが失われました。

削除された内容には、モデルをデプロイするページの「Regions」タブにアクセスすること、割り当て解除したいリソースを選択すること、「Remove assignment」ボタンを選ぶこと、現れるウィンドウに削除したいリソースの名前を入力する手順が含まれていました。

この情報の欠如により、ユーザーは必要なリソースを適切に管理できなくなる可能性があります。特に、他のリージョンでリソースを扱う際には、関連する操作を行うための具体的なステップがないため、未経験のユーザーには深刻な問題を引き起こすと思われます。この変更は、ユーザー体験や作業の効率に対して否定的な影響を与える可能性があります。

## articles/ai-services/language-service/conversational-language-understanding/language-support.md{#item-6b7b2b}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: This article lists the natural languages Azure Language in Foundry
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 12/05/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピックの種類の更新"
}
```

### Explanation
このコードの差分は、ドキュメント内のトピックの種類を「conceptual」から「concept-article」に変更したことを示しています。この変更は、ドキュメントの分類や情報の構造に影響を与え、ユーザーがコンテンツをより正確に理解できるようにします。

具体的には、変更された部分はメタデータセクションにあり、「ms.topic」の値が修正されています。このようなマイナーな更新は、ドキュメントの一貫性を保ち、それに応じた分類が適切に行われることを目的としています。変更後は、ユーザーはこの資料が概念に基づいたアーティクルであることをより明確に理解できるようになります。

## articles/ai-services/language-service/conversational-language-understanding/media/backwards-compatibility/banner.svg{#item-c4089a}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +0,0 @@
-<svg xmlns="http://www.w3.org/2000/svg" width="1034" height="33" fill="none" viewBox="0 0 1034 33">
-  <path fill="#F3F2F1" d="M0 0h1034v33H0z"/>
-  <path fill="#605E5C" d="M19.5 23a7.472 7.472 0 0 1-3.79-1.016 7.757 7.757 0 0 1-1.523-1.172 7.757 7.757 0 0 1-1.171-1.523A7.472 7.472 0 0 1 12 15.5c0-.692.088-1.356.266-1.991.177-.64.427-1.24.75-1.797a7.557 7.557 0 0 1 1.171-1.516 7.374 7.374 0 0 1 1.524-1.172 7.454 7.454 0 0 1 1.789-.757 7.472 7.472 0 0 1 2-.266 7.422 7.422 0 0 1 3.79 1.023 7.192 7.192 0 0 1 1.515 1.172c.458.453.849.959 1.172 1.516A7.424 7.424 0 0 1 27 15.5a7.43 7.43 0 0 1-.266 2 7.456 7.456 0 0 1-.757 1.79 7.378 7.378 0 0 1-1.172 1.523 7.557 7.557 0 0 1-1.516 1.171 7.615 7.615 0 0 1-1.797.75A7.39 7.39 0 0 1 19.5 23Zm0-14a6.31 6.31 0 0 0-1.727.234 6.735 6.735 0 0 0-1.554.657 6.513 6.513 0 0 0-2.985 3.89A6.28 6.28 0 0 0 13 15.5c0 .594.078 1.17.234 1.727.157.552.375 1.07.657 1.554a6.513 6.513 0 0 0 2.328 2.328c.484.282 1.002.5 1.554.657A6.308 6.308 0 0 0 19.5 22a6.28 6.28 0 0 0 1.719-.234 6.548 6.548 0 0 0 3.89-2.985c.282-.484.5-1.002.657-1.554A6.308 6.308 0 0 0 26 15.5a6.28 6.28 0 0 0-.234-1.719 6.548 6.548 0 0 0-1.672-2.875 6.548 6.548 0 0 0-2.875-1.672A6.28 6.28 0 0 0 19.5 9Zm-.5 5h1v5h-1v-5Zm0-2h1v1h-1v-1Z"/>
-  <path fill="#323130" d="M46.535 21h-1.869v-5.027c0-.543.024-1.143.07-1.8h-.046c-.098.517-.186.887-.264 1.114L42.457 21H40.91l-2.004-5.654c-.054-.153-.142-.543-.263-1.172h-.053c.05.828.076 1.555.076 2.18V21h-1.705v-8.402h2.771l1.717 4.98c.137.399.236.799.299 1.201h.035a12.3 12.3 0 0 1 .334-1.213l1.717-4.968h2.701V21Zm2.666-6.95c-.312 0-.568-.091-.767-.275a.906.906 0 0 1-.3-.685c0-.277.1-.504.3-.68.199-.176.455-.264.767-.264.317 0 .572.088.768.264a.866.866 0 0 1 .299.68c0 .281-.1.512-.3.691-.195.18-.45.27-.767.27Zm.914 6.95h-1.851v-6h1.851v6Zm7.442-.686c0 1.114-.323 1.975-.967 2.584-.645.614-1.578.92-2.8.92-.81 0-1.45-.115-1.923-.345v-1.559c.617.36 1.24.54 1.87.54.624 0 1.109-.167 1.453-.499.343-.328.515-.775.515-1.342v-.474h-.023c-.422.672-1.045 1.008-1.87 1.008-.765 0-1.372-.27-1.822-.81-.449-.538-.674-1.26-.674-2.167 0-1.016.25-1.822.75-2.42.5-.598 1.159-.896 1.975-.896.73 0 1.277.28 1.64.843h.024V15h1.852v5.314Zm-1.829-2.197v-.474a1.44 1.44 0 0 0-.34-.967 1.078 1.078 0 0 0-.872-.404c-.41 0-.733.16-.967.48-.234.32-.352.771-.352 1.354 0 .5.112.896.334 1.189.223.289.528.433.914.433.383 0 .692-.146.926-.439.238-.297.357-.687.357-1.172Zm7.29-1.447a1.606 1.606 0 0 0-.78-.182c-.402 0-.716.149-.943.446-.227.293-.34.693-.34 1.2V21h-1.852v-6h1.852v1.113h.023c.294-.812.82-1.218 1.582-1.218.196 0 .348.023.458.07v1.705ZM68.877 21h-1.752v-.861h-.023c-.403.672-.999 1.008-1.788 1.008-.582 0-1.04-.165-1.376-.493-.333-.332-.498-.773-.498-1.324 0-1.164.689-1.836 2.068-2.015l1.629-.217c0-.657-.356-.985-1.067-.985-.714 0-1.394.213-2.039.639v-1.395c.258-.132.61-.25 1.055-.351.45-.102.857-.152 1.225-.152 1.71 0 2.566.853 2.566 2.56V21Zm-1.74-2.438v-.404l-1.09.14c-.602.079-.903.35-.903.815a.69.69 0 0 0 .217.522c.149.133.348.199.598.199.348 0 .63-.12.85-.357.218-.243.328-.547.328-.915Zm6.832 2.368c-.274.144-.686.216-1.237.216-1.304 0-1.957-.677-1.957-2.033v-2.748h-.972V15h.972v-1.295l1.846-.527V15h1.348v1.365H72.62v2.426c0 .625.248.938.744.938.196 0 .397-.057.604-.17v1.37Zm1.986-6.88c-.312 0-.568-.091-.767-.275a.906.906 0 0 1-.3-.685c0-.277.1-.504.3-.68.199-.176.455-.264.767-.264.317 0 .572.088.768.264a.866.866 0 0 1 .299.68c0 .281-.1.512-.3.691-.195.18-.45.27-.767.27ZM76.87 21h-1.851v-6h1.851v6Zm4.418.146c-1 0-1.787-.279-2.361-.837-.57-.563-.856-1.325-.856-2.286 0-.992.297-1.767.89-2.326.595-.562 1.397-.843 2.41-.843.995 0 1.776.28 2.343.843.566.559.85 1.3.85 2.221 0 .996-.294 1.783-.88 2.361-.581.578-1.38.867-2.396.867Zm.047-4.875c-.438 0-.777.15-1.02.452-.242.3-.363.726-.363 1.277 0 1.152.465 1.729 1.395 1.729.886 0 1.33-.592 1.33-1.776 0-1.121-.448-1.681-1.342-1.681ZM91.559 21h-1.846v-3.334c0-.93-.332-1.395-.996-1.395a.988.988 0 0 0-.791.37c-.207.246-.31.558-.31.937V21h-1.852v-6h1.851v.95h.024c.441-.731 1.084-1.096 1.927-1.096 1.328 0 1.993.824 1.993 2.472V21Zm9.779 0h-1.752v-.861h-.023c-.403.672-.999 1.008-1.788 1.008-.582 0-1.04-.165-1.377-.493-.332-.332-.498-.773-.498-1.324 0-1.164.69-1.836 2.069-2.015l1.629-.217c0-.657-.356-.985-1.067-.985-.715 0-1.394.213-2.039.639v-1.395c.258-.132.61-.25 1.055-.351.45-.102.857-.152 1.225-.152 1.71 0 2.566.853 2.566 2.56V21Zm-1.74-2.438v-.404l-1.09.14c-.602.079-.902.35-.902.815a.69.69 0 0 0 .216.522c.149.133.348.199.598.199.348 0 .63-.12.85-.357.218-.243.328-.547.328-.915ZM108.516 15l-2.233 6h-2.109l-2.127-6h1.98l1.043 3.697a5.3 5.3 0 0 1 .205 1.067h.024c.027-.278.099-.621.217-1.032L106.582 15h1.934Zm5.595 6h-1.752v-.861h-.023c-.402.672-.998 1.008-1.787 1.008-.582 0-1.041-.165-1.377-.493-.332-.332-.498-.773-.498-1.324 0-1.164.689-1.836 2.068-2.015l1.629-.217c0-.657-.355-.985-1.066-.985-.715 0-1.395.213-2.039.639v-1.395c.257-.132.609-.25 1.054-.351a5.58 5.58 0 0 1 1.225-.152c1.711 0 2.566.853 2.566 2.56V21Zm-1.74-2.438v-.404l-1.09.14c-.601.079-.902.35-.902.815 0 .211.072.385.217.522.148.133.347.199.597.199.348 0 .631-.12.85-.357.219-.243.328-.547.328-.915Zm4.143-4.511c-.313 0-.569-.092-.768-.276a.907.907 0 0 1-.299-.685c0-.277.1-.504.299-.68.199-.176.455-.264.768-.264.316 0 .572.088.767.264a.865.865 0 0 1 .299.68.89.89 0 0 1-.299.691c-.195.18-.451.27-.767.27Zm.914 6.949h-1.852v-6h1.852v6Zm3.41 0h-1.852v-8.883h1.852V21Zm6.551 0h-1.752v-.861h-.024c-.402.672-.998 1.008-1.787 1.008-.582 0-1.041-.165-1.377-.493-.332-.332-.498-.773-.498-1.324 0-1.164.69-1.836 2.069-2.015l1.628-.217c0-.657-.355-.985-1.066-.985-.715 0-1.394.213-2.039.639v-1.395c.258-.132.609-.25 1.055-.351a5.59 5.59 0 0 1 1.224-.152c1.711 0 2.567.853 2.567 2.56V21Zm-1.741-2.438v-.404l-1.089.14c-.602.079-.903.35-.903.815a.69.69 0 0 0 .217.522c.148.133.348.199.598.199a1.1 1.1 0 0 0 .849-.357c.219-.243.328-.547.328-.915Zm5.081 1.74h-.024V21h-1.851v-8.883h1.851v3.785h.024c.457-.699 1.107-1.048 1.951-1.048.773 0 1.369.265 1.787.796.418.532.627 1.258.627 2.18 0 1-.244 1.803-.733 2.408-.488.606-1.14.909-1.957.909-.738 0-1.297-.282-1.675-.844Zm-.053-2.53v.615c0 .386.111.707.334.96.222.255.508.381.855.381.422 0 .748-.162.979-.486.234-.328.351-.79.351-1.389 0-.496-.107-.882-.322-1.16-.211-.28-.514-.422-.908-.422-.371 0-.68.14-.926.416-.242.278-.363.64-.363 1.084Zm7.47 3.228h-1.851v-8.883h1.851V21Zm6.95-2.473h-3.914c.062.871.611 1.307 1.646 1.307.66 0 1.24-.156 1.74-.469v1.336c-.554.297-1.275.445-2.162.445-.968 0-1.72-.267-2.256-.802-.535-.54-.802-1.29-.802-2.25 0-.996.289-1.785.867-2.367.578-.582 1.289-.873 2.133-.873.875 0 1.55.26 2.027.779.48.52.721 1.224.721 2.115v.78Zm-1.717-1.136c0-.86-.348-1.29-1.043-1.29-.297 0-.555.124-.774.37a1.693 1.693 0 0 0-.392.92h2.209Zm3.346-1.22a.632.632 0 0 1-.463-.192.642.642 0 0 1-.188-.463.641.641 0 0 1 .651-.644c.183 0 .339.062.468.187a.613.613 0 0 1 .194.457c0 .18-.065.334-.194.463a.638.638 0 0 1-.468.193Zm0 4.958a.631.631 0 0 1-.463-.194.642.642 0 0 1-.188-.462c0-.18.063-.334.188-.463a.622.622 0 0 1 .463-.2c.183 0 .339.067.468.2a.632.632 0 0 1 .194.463c0 .18-.065.334-.194.463a.637.637 0 0 1-.468.193Zm5.689-.129v-8.402h2.391c.726 0 1.302.177 1.728.533.426.355.639.818.639 1.389 0 .476-.129.89-.387 1.242a2.085 2.085 0 0 1-1.066.75v.023c.566.067 1.019.281 1.359.645.34.36.51.828.51 1.406 0 .719-.258 1.3-.774 1.746-.515.445-1.166.668-1.951.668h-2.449Zm.984-7.512v2.713h1.008c.539 0 .963-.129 1.272-.386.308-.262.463-.63.463-1.102 0-.816-.537-1.225-1.612-1.225h-1.131Zm0 3.598v3.023h1.336c.578 0 1.026-.136 1.342-.41.32-.273.481-.648.481-1.125 0-.992-.676-1.488-2.028-1.488h-1.131Zm10.588 1.154h-4.236c.016.668.195 1.184.539 1.547.344.363.816.545 1.418.545.676 0 1.297-.223 1.863-.668v.902c-.527.383-1.224.575-2.091.575-.848 0-1.514-.272-1.999-.815-.484-.547-.726-1.314-.726-2.303 0-.933.264-1.693.791-2.279.531-.59 1.189-.885 1.975-.885.785 0 1.392.254 1.822.762.429.508.644 1.213.644 2.115v.504Zm-.984-.814c-.004-.555-.139-.986-.404-1.295-.262-.309-.627-.463-1.096-.463-.453 0-.838.162-1.154.486-.317.325-.512.748-.586 1.272h3.24Zm7.564 3.094c0 2.203-1.054 3.304-3.164 3.304-.742 0-1.39-.14-1.945-.422v-.96c.676.374 1.32.562 1.934.562 1.476 0 2.214-.785 2.214-2.356v-.656h-.023c-.457.766-1.144 1.149-2.062 1.149-.747 0-1.348-.266-1.805-.797-.453-.535-.68-1.252-.68-2.15 0-1.02.244-1.83.733-2.432.492-.602 1.164-.903 2.015-.903.809 0 1.408.325 1.799.973h.023V15h.961v5.52Zm-.961-2.233v-.885c0-.476-.162-.884-.486-1.224-.32-.34-.721-.51-1.201-.51-.594 0-1.059.217-1.395.65-.335.43-.503 1.034-.503 1.81 0 .669.16 1.204.48 1.606.324.399.752.598 1.283.598.539 0 .977-.191 1.313-.574.34-.383.509-.873.509-1.47Zm3.399-4.81a.611.611 0 0 1-.621-.622c0-.18.06-.328.181-.445a.601.601 0 0 1 .44-.181c.176 0 .324.06.445.181a.584.584 0 0 1 .188.445.59.59 0 0 1-.188.44.604.604 0 0 1-.445.182Zm.469 7.523h-.961v-6h.961v6Zm6.925 0h-.96v-3.422c0-1.273-.465-1.91-1.395-1.91-.481 0-.879.182-1.195.545-.313.36-.469.814-.469 1.365V21h-.961v-6h.961v.996h.023c.453-.758 1.11-1.137 1.969-1.137.656 0 1.158.213 1.506.639.348.422.521 1.033.521 1.834V21Zm9.2-.275c-.461.277-1.008.416-1.641.416-.855 0-1.547-.278-2.074-.832-.524-.559-.785-1.282-.785-2.168 0-.989.283-1.782.849-2.38.567-.6 1.323-.902 2.268-.902.527 0 .992.098 1.394.293v.985a2.44 2.44 0 0 0-1.429-.469c-.614 0-1.118.22-1.512.662-.391.438-.586 1.014-.586 1.729 0 .703.184 1.257.551 1.664.371.406.867.609 1.488.609.524 0 1.016-.174 1.477-.521v.914Zm3.961.416c-.887 0-1.596-.28-2.127-.838-.528-.563-.791-1.307-.791-2.233 0-1.008.275-1.795.826-2.361.551-.566 1.295-.85 2.232-.85.895 0 1.592.276 2.092.826.504.551.756 1.315.756 2.292 0 .957-.272 1.724-.815 2.302-.539.575-1.263.862-2.173.862Zm.07-5.473c-.617 0-1.106.21-1.465.633-.359.418-.539.996-.539 1.734 0 .711.182 1.272.545 1.682.363.41.85.615 1.459.615.621 0 1.098-.201 1.43-.604.336-.402.503-.974.503-1.716 0-.75-.167-1.328-.503-1.735-.332-.406-.809-.609-1.43-.609Zm5.437 4.465h-.023v3.627h-.961V15h.961v1.055h.023c.473-.797 1.164-1.196 2.075-1.196.773 0 1.377.27 1.81.809.434.535.651 1.254.651 2.156 0 1.004-.245 1.809-.733 2.414-.488.602-1.156.903-2.004.903-.777 0-1.377-.336-1.799-1.008Zm-.023-2.42v.838c0 .496.16.918.48 1.265.325.344.735.516 1.231.516.582 0 1.037-.223 1.365-.668.332-.445.498-1.064.498-1.857 0-.668-.154-1.192-.463-1.57-.308-.38-.726-.569-1.254-.569-.558 0-1.007.195-1.347.586-.34.387-.51.873-.51 1.459ZM209.912 15l-2.76 6.96c-.492 1.243-1.183 1.864-2.074 1.864-.25 0-.459-.025-.627-.076v-.861c.207.07.397.105.569.105.484 0 .847-.289 1.089-.867l.481-1.137L204.246 15h1.066l1.624 4.617c.019.059.06.211.123.457h.035c.019-.094.058-.242.117-.445L208.916 15h.996Zm1.529-1.523a.609.609 0 0 1-.621-.622c0-.18.061-.328.182-.445a.599.599 0 0 1 .439-.181c.176 0 .325.06.446.181a.583.583 0 0 1 .187.445.589.589 0 0 1-.187.44.607.607 0 0 1-.446.182ZM211.91 21h-.961v-6h.961v6Zm6.926 0h-.961v-3.422c0-1.273-.465-1.91-1.395-1.91-.48 0-.878.182-1.195.545-.312.36-.469.814-.469 1.365V21h-.961v-6h.961v.996h.024c.453-.758 1.109-1.137 1.969-1.137.656 0 1.158.213 1.505.639.348.422.522 1.033.522 1.834V21Zm6.937-.48c0 2.203-1.054 3.304-3.164 3.304-.742 0-1.39-.14-1.945-.422v-.96c.676.374 1.32.562 1.934.562 1.476 0 2.214-.785 2.214-2.356v-.656h-.023c-.457.766-1.144 1.149-2.062 1.149-.747 0-1.348-.266-1.805-.797-.453-.535-.68-1.252-.68-2.15 0-1.02.244-1.83.733-2.432.492-.602 1.164-.903 2.015-.903.809 0 1.408.325 1.799.973h.023V15h.961v5.52Zm-.961-2.233v-.885c0-.476-.162-.884-.486-1.224-.32-.34-.721-.51-1.201-.51-.594 0-1.059.217-1.395.65-.335.43-.503 1.034-.503 1.81 0 .669.16 1.204.48 1.606.324.399.752.598 1.283.598.539 0 .977-.191 1.313-.574.34-.383.509-.873.509-1.47ZM235.787 15l-2.76 6.96c-.492 1.243-1.183 1.864-2.074 1.864-.25 0-.459-.025-.627-.076v-.861c.207.07.397.105.569.105.484 0 .847-.289 1.089-.867l.481-1.137L230.121 15h1.067l1.623 4.617c.019.059.06.211.123.457h.035c.019-.094.058-.242.117-.445L234.791 15h.996Zm3.545 6.14c-.887 0-1.596-.279-2.127-.837-.527-.563-.791-1.307-.791-2.233 0-1.008.275-1.795.826-2.361.551-.566 1.295-.85 2.233-.85.894 0 1.591.276 2.091.826.504.551.756 1.315.756 2.292 0 .957-.271 1.724-.814 2.302-.539.575-1.264.862-2.174.862Zm.07-5.472c-.617 0-1.105.21-1.464.633-.36.418-.54.996-.54 1.734 0 .711.182 1.272.545 1.682.364.41.85.615 1.459.615.621 0 1.098-.201 1.43-.604.336-.402.504-.974.504-1.716 0-.75-.168-1.328-.504-1.735-.332-.406-.809-.609-1.43-.609ZM248.707 21h-.961v-.95h-.023c-.399.727-1.016 1.09-1.852 1.09-1.43 0-2.144-.85-2.144-2.554V15h.955v3.434c0 1.265.484 1.898 1.453 1.898.469 0 .853-.172 1.154-.516.305-.347.457-.8.457-1.359V15h.961v6Zm5.074-5.027c-.168-.13-.41-.194-.726-.194-.41 0-.754.194-1.032.58-.273.387-.41.914-.41 1.582V21h-.961v-6h.961v1.236h.024c.136-.421.345-.75.627-.984a1.42 1.42 0 0 1 .943-.357c.25 0 .441.027.574.082v.996ZM262.605 21h-4.359v-8.402h.984v7.511h3.375V21Zm7.202-3.398c0 2.359-1.065 3.539-3.194 3.539-2.039 0-3.058-1.135-3.058-3.405v-5.138h.984v5.074c0 1.723.727 2.584 2.18 2.584 1.402 0 2.103-.832 2.103-2.496v-5.162h.985v5.004ZM272.895 21h-.985v-8.402h.985V21Zm1.822-.34V19.5c.133.117.291.223.474.316.188.094.383.174.586.24.207.063.414.112.621.147.207.035.399.053.575.053.605 0 1.056-.111 1.353-.334.301-.227.451-.55.451-.973 0-.226-.05-.424-.152-.592a1.605 1.605 0 0 0-.41-.457 3.788 3.788 0 0 0-.627-.398 30.818 30.818 0 0 0-.774-.404 13.19 13.19 0 0 1-.82-.451 3.57 3.57 0 0 1-.662-.504 2.162 2.162 0 0 1-.445-.622 1.974 1.974 0 0 1-.158-.82c0-.383.083-.715.251-.996.168-.285.389-.52.663-.703.273-.184.584-.32.931-.41.352-.09.709-.135 1.072-.135.829 0 1.432.1 1.811.299v1.107c-.496-.343-1.133-.515-1.91-.515-.215 0-.43.023-.645.07a1.775 1.775 0 0 0-.574.217 1.266 1.266 0 0 0-.41.392c-.106.16-.158.356-.158.586 0 .215.039.4.117.557.082.156.201.299.357.428.157.129.346.254.569.375.226.12.486.254.779.398.301.149.586.305.856.469.269.164.505.346.708.545.204.199.364.42.481.662.121.242.182.52.182.832 0 .414-.082.765-.247 1.055a1.96 1.96 0 0 1-.656.697 2.79 2.79 0 0 1-.949.387 5.094 5.094 0 0 1-1.137.123c-.132 0-.297-.012-.492-.035a5.625 5.625 0 0 1-.598-.094 5.046 5.046 0 0 1-.58-.147 1.88 1.88 0 0 1-.433-.205Zm14.226.34h-.961v-.938h-.023c-.418.72-1.033 1.079-1.846 1.079-.597 0-1.066-.159-1.406-.475-.336-.316-.504-.736-.504-1.26 0-1.12.66-1.773 1.981-1.957l1.798-.252c0-1.02-.412-1.529-1.236-1.529-.723 0-1.375.246-1.957.738v-.984c.59-.375 1.27-.563 2.039-.563 1.41 0 2.115.746 2.115 2.239V21Zm-.961-3.035-1.447.2c-.445.062-.781.173-1.008.333-.226.156-.339.436-.339.838 0 .293.103.533.31.72.211.184.49.276.838.276.476 0 .869-.166 1.178-.498.312-.336.468-.76.468-1.271v-.598Zm3.756 2.168h-.023v3.627h-.961V15h.961v1.055h.023c.473-.797 1.164-1.196 2.074-1.196.774 0 1.377.27 1.811.809.434.535.65 1.254.65 2.156 0 1.004-.244 1.809-.732 2.414-.488.602-1.156.903-2.004.903-.777 0-1.377-.336-1.799-1.008Zm-.023-2.42v.838c0 .496.16.918.48 1.265.325.344.735.516 1.231.516.582 0 1.037-.223 1.365-.668.332-.445.498-1.064.498-1.857 0-.668-.154-1.192-.463-1.57-.308-.38-.726-.569-1.254-.569-.558 0-1.008.195-1.347.586-.34.387-.51.873-.51 1.459Zm7.078 2.42h-.023v3.627h-.961V15h.961v1.055h.023c.473-.797 1.164-1.196 2.074-1.196.774 0 1.377.27 1.811.809.433.535.65 1.254.65 2.156 0 1.004-.244 1.809-.732 2.414-.489.602-1.157.903-2.004.903-.778 0-1.377-.336-1.799-1.008Zm-.023-2.42v.838c0 .496.16.918.48 1.265.324.344.734.516 1.23.516.582 0 1.038-.223 1.366-.668.332-.445.498-1.064.498-1.857 0-.668-.155-1.192-.463-1.57-.309-.38-.727-.569-1.254-.569-.559 0-1.008.195-1.348.586-.34.387-.509.873-.509 1.459ZM305.824 21h-.961v-8.883h.961V21Zm2.438-7.523a.61.61 0 0 1-.621-.622c0-.18.06-.328.181-.445a.6.6 0 0 1 .44-.181c.176 0 .324.06.445.181a.584.584 0 0 1 .188.445.59.59 0 0 1-.188.44.604.604 0 0 1-.445.182ZM308.73 21h-.96v-6h.96v6Zm6.036-.275c-.461.277-1.008.416-1.641.416-.855 0-1.547-.278-2.074-.832-.524-.559-.785-1.282-.785-2.168 0-.989.283-1.782.849-2.38.567-.6 1.323-.902 2.268-.902.527 0 .992.098 1.394.293v.985a2.442 2.442 0 0 0-1.429-.469c-.614 0-1.118.22-1.512.662-.391.438-.586 1.014-.586 1.729 0 .703.184 1.257.551 1.664.371.406.867.609 1.488.609.523 0 1.016-.174 1.477-.521v.914Zm5.748.275h-.961v-.938h-.024c-.418.72-1.033 1.079-1.845 1.079-.598 0-1.067-.159-1.407-.475-.336-.316-.504-.736-.504-1.26 0-1.12.661-1.773 1.981-1.957l1.799-.252c0-1.02-.412-1.529-1.237-1.529-.722 0-1.375.246-1.957.738v-.984c.59-.375 1.27-.563 2.039-.563 1.411 0 2.116.746 2.116 2.239V21Zm-.961-3.035-1.448.2c-.445.062-.781.173-1.007.333-.227.156-.34.436-.34.838 0 .293.103.533.31.72.211.184.491.276.838.276.477 0 .869-.166 1.178-.498.312-.336.469-.76.469-1.271v-.598Zm5.554 2.976c-.226.125-.525.188-.896.188-1.051 0-1.576-.586-1.576-1.758v-3.55h-1.031V15h1.031v-1.465l.961-.31V15h1.511v.82h-1.511v3.381c0 .402.068.69.205.861.137.172.363.258.679.258.243 0 .452-.066.627-.199v.82Zm1.776-7.464a.61.61 0 0 1-.621-.622c0-.18.06-.328.181-.445a.6.6 0 0 1 .44-.181c.176 0 .324.06.445.181a.584.584 0 0 1 .188.445.59.59 0 0 1-.188.44.604.604 0 0 1-.445.182Zm.469 7.523h-.961v-6h.961v6Zm4.453.14c-.887 0-1.596-.279-2.127-.837-.528-.563-.791-1.307-.791-2.233 0-1.008.275-1.795.826-2.361.551-.566 1.295-.85 2.232-.85.895 0 1.592.276 2.092.826.504.551.756 1.315.756 2.292 0 .957-.272 1.724-.814 2.302-.54.575-1.264.862-2.174.862Zm.07-5.472c-.617 0-1.105.21-1.465.633-.359.418-.539.996-.539 1.734 0 .711.182 1.272.545 1.682.363.41.85.615 1.459.615.621 0 1.098-.201 1.43-.604.336-.402.504-.974.504-1.716 0-.75-.168-1.328-.504-1.735-.332-.406-.809-.609-1.43-.609ZM341.309 21h-.961v-3.422c0-1.273-.465-1.91-1.395-1.91-.48 0-.879.182-1.195.545-.313.36-.469.814-.469 1.365V21h-.961v-6h.961v.996h.023c.454-.758 1.11-1.137 1.969-1.137.657 0 1.158.213 1.506.639.348.422.522 1.033.522 1.834V21Zm1.453-.217v-1.031a2.84 2.84 0 0 0 1.728.58c.844 0 1.266-.281 1.266-.844a.705.705 0 0 0-.111-.404 1.02 1.02 0 0 0-.293-.299 2.07 2.07 0 0 0-.434-.228c-.164-.07-.342-.143-.533-.217a7.636 7.636 0 0 1-.703-.317c-.2-.109-.368-.23-.504-.363a1.439 1.439 0 0 1-.305-.463 1.679 1.679 0 0 1-.1-.603c0-.282.065-.53.194-.744.129-.22.301-.4.515-.545a2.35 2.35 0 0 1 .733-.334 3.29 3.29 0 0 1 .855-.112c.52 0 .985.09 1.395.27v.973a2.719 2.719 0 0 0-1.524-.434 1.71 1.71 0 0 0-.486.064c-.144.04-.269.096-.375.17a.831.831 0 0 0-.24.27.701.701 0 0 0-.082.34.84.84 0 0 0 .082.392.88.88 0 0 0 .252.282c.109.082.242.156.398.222.156.067.334.139.533.217.266.102.504.207.715.316.211.106.391.227.539.364.149.133.262.287.34.463.082.175.123.384.123.627 0 .296-.066.554-.199.773a1.66 1.66 0 0 1-.521.545 2.41 2.41 0 0 1-.756.322c-.285.07-.584.106-.897.106-.617 0-1.152-.12-1.605-.358Zm11.537.158c-.227.125-.526.188-.897.188-1.05 0-1.576-.586-1.576-1.758v-3.55h-1.031V15h1.031v-1.465l.961-.31V15h1.512v.82h-1.512v3.381c0 .402.068.69.205.861.137.172.363.258.68.258.242 0 .451-.066.627-.199v.82Zm3.791.2c-.887 0-1.596-.28-2.127-.838-.527-.563-.791-1.307-.791-2.233 0-1.008.275-1.795.826-2.361.551-.566 1.295-.85 2.232-.85.895 0 1.592.276 2.092.826.504.551.756 1.315.756 2.292 0 .957-.271 1.724-.814 2.302-.539.575-1.264.862-2.174.862Zm.07-5.473c-.617 0-1.105.21-1.465.633-.359.418-.539.996-.539 1.734 0 .711.182 1.272.545 1.682.363.41.85.615 1.459.615.621 0 1.098-.201 1.43-.604.336-.402.504-.974.504-1.716 0-.75-.168-1.328-.504-1.735-.332-.406-.809-.609-1.43-.609Zm10.529 5.273c-.226.125-.525.188-.896.188-1.051 0-1.576-.586-1.576-1.758v-3.55h-1.031V15h1.031v-1.465l.961-.31V15h1.511v.82h-1.511v3.381c0 .402.068.69.205.861.137.172.363.258.679.258.243 0 .452-.066.627-.199v.82Zm6.264.059h-.961v-3.457c0-1.25-.465-1.875-1.394-1.875-.469 0-.864.182-1.184.545-.32.36-.48.822-.48 1.389V21h-.961v-8.883h.961v3.88h.023c.461-.759 1.117-1.138 1.969-1.138 1.351 0 2.027.815 2.027 2.444V21Zm6.639-2.76h-4.237c.016.668.196 1.184.54 1.547.343.363.816.545 1.417.545.676 0 1.297-.223 1.864-.668v.902c-.528.383-1.225.575-2.092.575-.848 0-1.514-.272-1.998-.815-.484-.547-.727-1.314-.727-2.303 0-.933.264-1.693.791-2.279.532-.59 1.19-.885 1.975-.885.785 0 1.393.254 1.822.762.43.508.645 1.213.645 2.115v.504Zm-.985-.814c-.003-.555-.138-.986-.404-1.295-.262-.309-.627-.463-1.096-.463-.453 0-.837.162-1.154.486-.316.325-.512.748-.586 1.272h3.24ZM391.324 21h-.961v-3.422c0-1.273-.465-1.91-1.394-1.91a1.52 1.52 0 0 0-1.196.545c-.312.36-.468.814-.468 1.365V21h-.961v-6h.961v.996h.023c.453-.758 1.11-1.137 1.969-1.137.656 0 1.158.213 1.506.639.347.422.521 1.033.521 1.834V21Zm6.639-2.76h-4.236c.015.668.195 1.184.539 1.547.343.363.816.545 1.418.545.675 0 1.296-.223 1.863-.668v.902c-.527.383-1.225.575-2.092.575-.848 0-1.514-.272-1.998-.815-.484-.547-.727-1.314-.727-2.303 0-.933.264-1.693.791-2.279.532-.59 1.19-.885 1.975-.885.785 0 1.393.254 1.822.762.43.508.645 1.213.645 2.115v.504Zm-.984-.814c-.004-.555-.139-.986-.405-1.295-.262-.309-.627-.463-1.095-.463-.454 0-.838.162-1.155.486-.316.325-.512.748-.586 1.272h3.241ZM403.805 15l-2.016 3.035L403.77 21h-1.12l-1.177-1.945a11.744 11.744 0 0 1-.264-.457h-.023l-.276.457L399.709 21h-1.107l2.044-2.941L398.689 15h1.12l1.16 2.05c.086.153.17.31.252.47h.023l1.5-2.52h1.061Zm3.908 5.941c-.227.125-.525.188-.897.188-1.05 0-1.576-.586-1.576-1.758v-3.55h-1.031V15h1.031v-1.465l.961-.31V15h1.512v.82h-1.512v3.381c0 .402.069.69.205.861.137.172.364.258.68.258.242 0 .451-.066.627-.199v.82Zm9.697-.421c0 2.203-1.055 3.304-3.164 3.304-.742 0-1.391-.14-1.945-.422v-.96c.676.374 1.32.562 1.933.562 1.477 0 2.215-.785 2.215-2.356v-.656h-.023c-.457.766-1.145 1.149-2.063 1.149-.746 0-1.347-.266-1.804-.797-.454-.535-.68-1.252-.68-2.15 0-1.02.244-1.83.732-2.432.493-.602 1.164-.903 2.016-.903.809 0 1.408.325 1.799.973h.023V15h.961v5.52Zm-.961-2.233v-.885c0-.476-.162-.884-.486-1.224-.32-.34-.721-.51-1.201-.51-.594 0-1.059.217-1.395.65-.336.43-.504 1.034-.504 1.81 0 .669.16 1.204.481 1.606.324.399.752.598 1.283.598.539 0 .977-.191 1.312-.574.34-.383.51-.873.51-1.47Zm7.729-.047h-4.237c.016.668.196 1.184.539 1.547.344.363.817.545 1.418.545.676 0 1.297-.223 1.864-.668v.902c-.528.383-1.225.575-2.092.575-.848 0-1.514-.272-1.998-.815-.484-.547-.727-1.314-.727-2.303 0-.933.264-1.693.791-2.279.532-.59 1.19-.885 1.975-.885.785 0 1.393.254 1.822.762.43.508.645 1.213.645 2.115v.504Zm-.985-.814c-.004-.555-.138-.986-.404-1.295-.262-.309-.627-.463-1.096-.463-.453 0-.838.162-1.154.486-.316.325-.512.748-.586 1.272h3.24ZM430.617 21h-.961v-3.422c0-1.273-.465-1.91-1.394-1.91a1.52 1.52 0 0 0-1.196.545c-.312.36-.468.814-.468 1.365V21h-.961v-6h.961v.996h.023c.453-.758 1.109-1.137 1.969-1.137.656 0 1.158.213 1.506.639.347.422.521 1.033.521 1.834V21Zm6.639-2.76h-4.236c.015.668.195 1.184.539 1.547.343.363.816.545 1.418.545.675 0 1.296-.223 1.863-.668v.902c-.528.383-1.225.575-2.092.575-.848 0-1.514-.272-1.998-.815-.484-.547-.727-1.314-.727-2.303 0-.933.264-1.693.791-2.279.532-.59 1.19-.885 1.975-.885.785 0 1.393.254 1.822.762.43.508.645 1.213.645 2.115v.504Zm-.985-.814c-.003-.555-.138-.986-.404-1.295-.262-.309-.627-.463-1.096-.463-.453 0-.837.162-1.154.486-.316.325-.512.748-.586 1.272h3.24Zm5.573-1.453c-.168-.13-.41-.194-.727-.194-.41 0-.754.194-1.031.58-.274.387-.41.914-.41 1.582V21h-.961v-6h.961v1.236h.023c.137-.421.346-.75.627-.984.281-.238.596-.357.944-.357.25 0 .441.027.574.082v.996ZM447.182 21h-.961v-.938h-.024c-.418.72-1.033 1.079-1.845 1.079-.598 0-1.067-.159-1.407-.475-.336-.316-.504-.736-.504-1.26 0-1.12.661-1.773 1.981-1.957l1.799-.252c0-1.02-.412-1.529-1.237-1.529-.722 0-1.375.246-1.957.738v-.984c.59-.375 1.27-.563 2.039-.563 1.411 0 2.116.746 2.116 2.239V21Zm-.961-3.035-1.448.2c-.445.062-.781.173-1.007.333-.227.156-.34.436-.34.838 0 .293.103.533.31.72.211.184.491.276.838.276.477 0 .869-.166 1.178-.498.312-.336.469-.76.469-1.271v-.598Zm5.554 2.976c-.226.125-.525.188-.896.188-1.051 0-1.576-.586-1.576-1.758v-3.55h-1.032V15h1.032v-1.465l.961-.31V15h1.511v.82h-1.511v3.381c0 .402.068.69.205.861.136.172.363.258.679.258.243 0 .452-.066.627-.199v.82Zm1.776-7.464a.61.61 0 0 1-.621-.622c0-.18.06-.328.181-.445a.6.6 0 0 1 .44-.181c.176 0 .324.06.445.181a.584.584 0 0 1 .188.445.59.59 0 0 1-.188.44.604.604 0 0 1-.445.182ZM454.02 21h-.961v-6h.961v6Zm4.453.14c-.887 0-1.596-.279-2.127-.837-.528-.563-.791-1.307-.791-2.233 0-1.008.275-1.795.826-2.361.551-.566 1.295-.85 2.232-.85.895 0 1.592.276 2.092.826.504.551.756 1.315.756 2.292 0 .957-.272 1.724-.815 2.302-.539.575-1.263.862-2.173.862Zm.07-5.472c-.617 0-1.105.21-1.465.633-.359.418-.539.996-.539 1.734 0 .711.182 1.272.545 1.682.363.41.85.615 1.459.615.621 0 1.098-.201 1.43-.604.336-.402.504-.974.504-1.716 0-.75-.168-1.328-.504-1.735-.332-.406-.809-.609-1.43-.609ZM467.977 21h-.961v-3.422c0-1.273-.465-1.91-1.395-1.91-.48 0-.879.182-1.195.545-.313.36-.469.814-.469 1.365V21h-.961v-6h.961v.996h.023c.454-.758 1.11-1.137 1.969-1.137.656 0 1.158.213 1.506.639.348.422.522 1.033.522 1.834V21Zm4.746-.217v-1.031a2.84 2.84 0 0 0 1.728.58c.844 0 1.266-.281 1.266-.844a.698.698 0 0 0-.112-.404.997.997 0 0 0-.293-.299 2.037 2.037 0 0 0-.433-.228c-.164-.07-.342-.143-.533-.217a7.636 7.636 0 0 1-.703-.317c-.2-.109-.368-.23-.504-.363a1.439 1.439 0 0 1-.305-.463 1.679 1.679 0 0 1-.1-.603c0-.282.065-.53.194-.744.129-.22.301-.4.515-.545a2.35 2.35 0 0 1 .733-.334 3.29 3.29 0 0 1 .855-.112c.52 0 .985.09 1.395.27v.973a2.719 2.719 0 0 0-1.524-.434 1.71 1.71 0 0 0-.486.064c-.145.04-.27.096-.375.17a.82.82 0 0 0-.24.27.701.701 0 0 0-.082.34.84.84 0 0 0 .082.392.88.88 0 0 0 .252.282c.109.082.242.156.398.222.156.067.334.139.533.217.266.102.504.207.715.316.211.106.391.227.539.364.149.133.262.287.34.463.082.175.123.384.123.627 0 .296-.066.554-.199.773-.129.219-.303.4-.522.545-.218.144-.47.252-.755.322-.286.07-.584.106-.897.106-.617 0-1.152-.12-1.605-.358Zm10.283-2.543h-4.236c.015.668.195 1.184.539 1.547.343.363.816.545 1.418.545.675 0 1.296-.223 1.863-.668v.902c-.528.383-1.225.575-2.092.575-.848 0-1.514-.272-1.998-.815-.484-.547-.727-1.314-.727-2.303 0-.933.264-1.693.791-2.279.532-.59 1.19-.885 1.975-.885.785 0 1.393.254 1.822.762.43.508.645 1.213.645 2.115v.504Zm-.985-.814c-.003-.555-.138-.986-.404-1.295-.262-.309-.627-.463-1.096-.463-.453 0-.837.162-1.154.486-.316.325-.512.748-.586 1.272h3.24Zm5.573-1.453c-.168-.13-.41-.194-.727-.194-.41 0-.754.194-1.031.58-.274.387-.41.914-.41 1.582V21h-.961v-6h.961v1.236h.023c.137-.421.346-.75.627-.984.281-.238.596-.357.944-.357.25 0 .441.027.574.082v.996Zm5.76-.973-2.391 6h-.943l-2.274-6h1.055l1.523 4.36c.114.32.184.599.211.837h.024c.039-.3.101-.572.187-.814L492.34 15h1.014Zm1.529-1.523a.61.61 0 0 1-.621-.622c0-.18.06-.328.181-.445a.6.6 0 0 1 .44-.181c.176 0 .324.06.445.181a.584.584 0 0 1 .188.445.59.59 0 0 1-.188.44.604.604 0 0 1-.445.182Zm.469 7.523h-.961v-6h.961v6Zm6.035-.275c-.461.277-1.008.416-1.641.416-.855 0-1.547-.278-2.074-.832-.524-.559-.785-1.282-.785-2.168 0-.989.283-1.782.849-2.38.567-.6 1.323-.902 2.268-.902.527 0 .992.098 1.394.293v.985a2.44 2.44 0 0 0-1.429-.469c-.614 0-1.117.22-1.512.662-.391.438-.586 1.014-.586 1.729 0 .703.184 1.257.551 1.664.371.406.867.609 1.488.609.524 0 1.016-.174 1.477-.521v.914Zm6.275-2.485h-4.236c.015.668.195 1.184.539 1.547.344.363.816.545 1.418.545.676 0 1.297-.223 1.863-.668v.902c-.527.383-1.225.575-2.092.575-.847 0-1.513-.272-1.998-.815-.484-.547-.726-1.314-.726-2.303 0-.933.263-1.693.791-2.279.531-.59 1.189-.885 1.974-.885.785 0 1.393.254 1.823.762.429.508.644 1.213.644 2.115v.504Zm-.984-.814c-.004-.555-.139-.986-.405-1.295-.261-.309-.627-.463-1.095-.463-.453 0-.838.162-1.155.486-.316.325-.511.748-.585 1.272h3.24Zm11.584 3.222c-.621.329-1.395.493-2.321.493-1.195 0-2.152-.385-2.871-1.155-.718-.77-1.078-1.779-1.078-3.029 0-1.344.404-2.43 1.213-3.258.809-.828 1.834-1.242 3.076-1.242.797 0 1.457.115 1.981.346v1.049a4.018 4.018 0 0 0-1.992-.504c-.965 0-1.749.322-2.35.966-.598.645-.897 1.506-.897 2.584 0 1.024.28 1.84.838 2.45.563.605 1.299.908 2.209.908.844 0 1.575-.188 2.192-.563v.955Zm4.09.493c-.887 0-1.596-.28-2.127-.838-.528-.563-.791-1.307-.791-2.233 0-1.008.275-1.795.826-2.361.551-.566 1.295-.85 2.232-.85.895 0 1.592.276 2.092.826.504.551.756 1.315.756 2.292 0 .957-.272 1.724-.815 2.302-.539.575-1.263.862-2.173.862Zm.07-5.473c-.617 0-1.106.21-1.465.633-.359.418-.539.996-.539 1.734 0 .711.182 1.272.545 1.682.363.41.849.615 1.459.615.621 0 1.098-.201 1.43-.604.336-.402.503-.974.503-1.716 0-.75-.167-1.328-.503-1.735-.332-.406-.809-.609-1.43-.609ZM531.855 21h-.96v-3.422c0-1.273-.465-1.91-1.395-1.91-.48 0-.879.182-1.195.545-.313.36-.469.814-.469 1.365V21h-.961v-6h.961v.996h.023c.453-.758 1.11-1.137 1.969-1.137.656 0 1.158.213 1.506.639.348.422.521 1.033.521 1.834V21Zm6.534-6-2.391 6h-.943l-2.274-6h1.055l1.523 4.36c.114.32.184.599.211.837h.024c.039-.3.101-.572.187-.814L537.375 15h1.014Zm5.859 3.24h-4.236c.015.668.195 1.184.539 1.547.344.363.816.545 1.418.545.676 0 1.297-.223 1.863-.668v.902c-.527.383-1.225.575-2.092.575-.847 0-1.513-.272-1.998-.815-.484-.547-.726-1.314-.726-2.303 0-.933.263-1.693.791-2.279.531-.59 1.189-.885 1.974-.885.785 0 1.393.254 1.823.762.429.508.644 1.213.644 2.115v.504Zm-.984-.814c-.004-.555-.139-.986-.405-1.295-.261-.309-.627-.463-1.095-.463-.453 0-.838.162-1.155.486-.316.325-.511.748-.586 1.272h3.241Zm5.572-1.453c-.168-.13-.41-.194-.727-.194-.41 0-.754.194-1.031.58-.273.387-.41.914-.41 1.582V21h-.961v-6h.961v1.236h.023c.137-.421.346-.75.627-.984.282-.238.596-.357.944-.357.25 0 .441.027.574.082v.996Zm.68 4.81v-1.031a2.84 2.84 0 0 0 1.728.58c.844 0 1.266-.281 1.266-.844a.698.698 0 0 0-.112-.404 1.009 1.009 0 0 0-.293-.299 2.037 2.037 0 0 0-.433-.228c-.164-.07-.342-.143-.533-.217a7.636 7.636 0 0 1-.703-.317c-.2-.109-.368-.23-.504-.363a1.439 1.439 0 0 1-.305-.463 1.679 1.679 0 0 1-.1-.603c0-.282.065-.53.194-.744.129-.22.3-.4.515-.545a2.35 2.35 0 0 1 .733-.334 3.29 3.29 0 0 1 .855-.112c.52 0 .985.09 1.395.27v.973a2.719 2.719 0 0 0-1.524-.434 1.71 1.71 0 0 0-.486.064c-.145.04-.27.096-.375.17a.82.82 0 0 0-.24.27.701.701 0 0 0-.082.34.84.84 0 0 0 .082.392.88.88 0 0 0 .252.282c.109.082.242.156.398.222.156.067.334.139.533.217.266.102.504.207.715.316.211.106.391.227.539.364.149.133.262.287.34.463.082.175.123.384.123.627 0 .296-.066.554-.199.773-.129.219-.303.4-.522.545-.218.144-.47.252-.755.322-.286.07-.584.106-.897.106-.617 0-1.152-.12-1.605-.358Zm9.755.217h-.96v-.938h-.024c-.418.72-1.033 1.079-1.846 1.079-.597 0-1.066-.159-1.406-.475-.336-.316-.504-.736-.504-1.26 0-1.12.66-1.773 1.981-1.957l1.799-.252c0-1.02-.413-1.529-1.237-1.529-.722 0-1.375.246-1.957.738v-.984c.59-.375 1.27-.563 2.039-.563 1.41 0 2.115.746 2.115 2.239V21Zm-.96-3.035-1.448.2c-.445.062-.781.173-1.008.333-.226.156-.339.436-.339.838 0 .293.103.533.31.72.211.184.49.276.838.276.477 0 .869-.166 1.178-.498.312-.336.469-.76.469-1.271v-.598Zm5.554 2.976c-.226.125-.525.188-.896.188-1.051 0-1.576-.586-1.576-1.758v-3.55h-1.032V15h1.032v-1.465l.961-.31V15h1.511v.82h-1.511v3.381c0 .402.068.69.205.861.136.172.363.258.679.258.242 0 .451-.066.627-.199v.82Zm1.776-7.464a.61.61 0 0 1-.621-.622c0-.18.06-.328.181-.445a.6.6 0 0 1 .44-.181c.175 0 .324.06.445.181a.583.583 0 0 1 .187.445.589.589 0 0 1-.187.44.606.606 0 0 1-.445.182Zm.468 7.523h-.961v-6h.961v6Zm4.453.14c-.886 0-1.595-.279-2.126-.837-.528-.563-.791-1.307-.791-2.233 0-1.008.275-1.795.826-2.361.55-.566 1.295-.85 2.232-.85.895 0 1.592.276 2.092.826.504.551.756 1.315.756 2.292 0 .957-.272 1.724-.815 2.302-.539.575-1.263.862-2.174.862Zm.071-5.472c-.617 0-1.106.21-1.465.633-.359.418-.539.996-.539 1.734 0 .711.182 1.272.545 1.682.363.41.849.615 1.459.615.621 0 1.097-.201 1.429-.604.336-.402.504-.974.504-1.716 0-.75-.168-1.328-.504-1.735-.332-.406-.808-.609-1.429-.609ZM580.066 21h-.961v-3.422c0-1.273-.464-1.91-1.394-1.91-.481 0-.879.182-1.195.545-.313.36-.469.814-.469 1.365V21h-.961v-6h.961v.996h.023c.453-.758 1.11-1.137 1.969-1.137.656 0 1.158.213 1.506.639.348.422.521 1.033.521 1.834V21Zm6.112 0h-.961v-.938h-.024c-.418.72-1.033 1.079-1.845 1.079-.598 0-1.067-.159-1.407-.475-.336-.316-.503-.736-.503-1.26 0-1.12.66-1.773 1.98-1.957l1.799-.252c0-1.02-.412-1.529-1.237-1.529-.722 0-1.375.246-1.957.738v-.984c.59-.375 1.27-.563 2.039-.563 1.411 0 2.116.746 2.116 2.239V21Zm-.961-3.035-1.447.2c-.446.062-.782.173-1.008.333-.227.156-.34.436-.34.838 0 .293.103.533.31.72.211.184.491.276.838.276.477 0 .869-.166 1.178-.498.313-.336.469-.76.469-1.271v-.598ZM588.949 21h-.961v-8.883h.961V21Zm6.199 0h-.96v-8.883h.96V21Zm6.241 0h-.961v-.938h-.024c-.418.72-1.033 1.079-1.845 1.079-.598 0-1.067-.159-1.407-.475-.336-.316-.504-.736-.504-1.26 0-1.12.661-1.773 1.981-1.957l1.799-.252c0-1.02-.412-1.529-1.237-1.529-.722 0-1.375.246-1.957.738v-.984c.59-.375 1.27-.563 2.039-.563 1.411 0 2.116.746 2.116 2.239V21Zm-.961-3.035-1.448.2c-.445.062-.781.173-1.007.333-.227.156-.34.436-.34.838 0 .293.103.533.31.72.211.184.491.276.838.276.477 0 .869-.166 1.178-.498.312-.336.469-.76.469-1.271v-.598ZM608.18 21h-.961v-3.422c0-1.273-.465-1.91-1.395-1.91-.48 0-.879.182-1.195.545-.313.36-.469.814-.469 1.365V21h-.961v-6h.961v.996h.024c.453-.758 1.109-1.137 1.968-1.137.657 0 1.159.213 1.506.639.348.422.522 1.033.522 1.834V21Zm6.937-.48c0 2.203-1.055 3.304-3.164 3.304-.742 0-1.391-.14-1.945-.422v-.96c.676.374 1.32.562 1.933.562 1.477 0 2.215-.785 2.215-2.356v-.656h-.023c-.457.766-1.145 1.149-2.063 1.149-.746 0-1.347-.266-1.804-.797-.454-.535-.68-1.252-.68-2.15 0-1.02.244-1.83.732-2.432.493-.602 1.164-.903 2.016-.903.809 0 1.408.325 1.799.973h.023V15h.961v5.52Zm-.961-2.233v-.885c0-.476-.162-.884-.486-1.224-.32-.34-.721-.51-1.201-.51-.594 0-1.059.217-1.395.65-.336.43-.504 1.034-.504 1.81 0 .669.16 1.204.481 1.606.324.399.752.598 1.283.598.539 0 .977-.191 1.312-.574.34-.383.51-.873.51-1.47ZM621.914 21h-.961v-.95h-.023c-.399.727-1.016 1.09-1.852 1.09-1.43 0-2.144-.85-2.144-2.554V15h.955v3.434c0 1.265.484 1.898 1.453 1.898.469 0 .853-.172 1.154-.516.305-.347.457-.8.457-1.359V15h.961v6Zm6.24 0h-.961v-.938h-.023c-.418.72-1.033 1.079-1.846 1.079-.597 0-1.066-.159-1.406-.475-.336-.316-.504-.736-.504-1.26 0-1.12.66-1.773 1.981-1.957l1.798-.252c0-1.02-.412-1.529-1.236-1.529-.723 0-1.375.246-1.957.738v-.984c.59-.375 1.27-.563 2.039-.563 1.41 0 2.115.746 2.115 2.239V21Zm-.961-3.035-1.447.2c-.445.062-.781.173-1.008.333-.226.156-.34.436-.34.838a.93.93 0 0 0 .311.72c.211.184.49.276.838.276.476 0 .869-.166 1.178-.498.312-.336.468-.76.468-1.271v-.598Zm7.893 2.555c0 2.203-1.055 3.304-3.164 3.304-.742 0-1.391-.14-1.945-.422v-.96c.675.374 1.32.562 1.933.562 1.477 0 2.215-.785 2.215-2.356v-.656h-.023c-.457.766-1.145 1.149-2.063 1.149-.746 0-1.348-.266-1.805-.797-.453-.535-.679-1.252-.679-2.15 0-1.02.244-1.83.732-2.432.492-.602 1.164-.903 2.016-.903.808 0 1.408.325 1.799.973h.023V15h.961v5.52Zm-.961-2.233v-.885c0-.476-.162-.884-.486-1.224a1.584 1.584 0 0 0-1.201-.51c-.594 0-1.059.217-1.395.65-.336.43-.504 1.034-.504 1.81 0 .669.16 1.204.481 1.606.324.399.751.598 1.283.598.539 0 .976-.191 1.312-.574.34-.383.51-.873.51-1.47Zm7.729-.047h-4.237c.016.668.195 1.184.539 1.547.344.363.817.545 1.418.545.676 0 1.297-.223 1.864-.668v.902c-.528.383-1.225.575-2.092.575-.848 0-1.514-.272-1.998-.815-.485-.547-.727-1.314-.727-2.303 0-.933.264-1.693.791-2.279.531-.59 1.19-.885 1.975-.885.785 0 1.392.254 1.822.762.43.508.645 1.213.645 2.115v.504Zm-.985-.814c-.004-.555-.139-.986-.404-1.295-.262-.309-.627-.463-1.096-.463-.453 0-.838.162-1.154.486-.317.325-.512.748-.586 1.272h3.24ZM651.457 21h-.961v-.95h-.023c-.399.727-1.016 1.09-1.852 1.09-1.43 0-2.144-.85-2.144-2.554V15h.955v3.434c0 1.265.484 1.898 1.453 1.898.469 0 .853-.172 1.154-.516.305-.347.457-.8.457-1.359V15h.961v6Zm6.926 0h-.961v-3.422c0-1.273-.465-1.91-1.395-1.91-.48 0-.879.182-1.195.545-.312.36-.469.814-.469 1.365V21h-.961v-6h.961v.996h.024c.453-.758 1.109-1.137 1.968-1.137.657 0 1.159.213 1.506.639.348.422.522 1.033.522 1.834V21Zm6.937 0h-.961v-1.02h-.023c-.445.774-1.133 1.16-2.063 1.16-.753 0-1.357-.267-1.81-.802-.449-.54-.674-1.272-.674-2.197 0-.993.25-1.787.75-2.385.5-.598 1.166-.897 1.998-.897.824 0 1.424.325 1.799.973h.023v-3.715h.961V21Zm-.961-2.713v-.885c0-.484-.16-.894-.48-1.23-.32-.336-.727-.504-1.219-.504-.586 0-1.047.215-1.383.645-.336.43-.504 1.023-.504 1.78 0 .692.161 1.239.481 1.641.324.399.758.598 1.301.598.535 0 .968-.193 1.3-.58.336-.387.504-.875.504-1.465Zm7.729-.047h-4.236c.015.668.195 1.184.539 1.547.343.363.816.545 1.418.545.675 0 1.296-.223 1.863-.668v.902c-.527.383-1.225.575-2.092.575-.848 0-1.514-.272-1.998-.815-.484-.547-.727-1.314-.727-2.303 0-.933.264-1.693.791-2.279.532-.59 1.19-.885 1.975-.885.785 0 1.393.254 1.822.762.43.508.645 1.213.645 2.115v.504Zm-.984-.814c-.004-.555-.139-.986-.405-1.295-.261-.309-.627-.463-1.095-.463-.454 0-.838.162-1.155.486-.316.325-.511.748-.586 1.272h3.241Zm5.572-1.453c-.168-.13-.41-.194-.727-.194-.41 0-.754.194-1.031.58-.273.387-.41.914-.41 1.582V21h-.961v-6h.961v1.236h.023c.137-.421.346-.75.627-.984.281-.238.596-.357.944-.357.25 0 .441.027.574.082v.996Zm.679 4.81v-1.031c.524.387 1.1.58 1.729.58.844 0 1.266-.281 1.266-.844a.705.705 0 0 0-.112-.404 1.009 1.009 0 0 0-.293-.299 2.037 2.037 0 0 0-.433-.228c-.164-.07-.342-.143-.533-.217a7.787 7.787 0 0 1-.704-.317 2.332 2.332 0 0 1-.504-.363 1.452 1.452 0 0 1-.304-.463 1.657 1.657 0 0 1-.1-.603c0-.282.065-.53.194-.744.128-.22.3-.4.515-.545a2.35 2.35 0 0 1 .733-.334 3.29 3.29 0 0 1 .855-.112c.52 0 .984.09 1.395.27v.973a2.721 2.721 0 0 0-1.524-.434 1.7 1.7 0 0 0-.486.064c-.145.04-.27.096-.375.17a.82.82 0 0 0-.24.27.701.701 0 0 0-.082.34.84.84 0 0 0 .082.392.88.88 0 0 0 .252.282c.109.082.242.156.398.222.156.067.334.139.533.217.266.102.504.207.715.316.211.106.391.227.539.364.149.133.262.287.34.463.082.175.123.384.123.627 0 .296-.066.554-.199.773-.129.219-.303.4-.522.545a2.39 2.39 0 0 1-.756.322 3.73 3.73 0 0 1-.896.106c-.617 0-1.152-.12-1.606-.358Zm8.245.158c-.227.125-.526.188-.897.188-1.051 0-1.576-.586-1.576-1.758v-3.55h-1.031V15h1.031v-1.465l.961-.31V15h1.512v.82h-1.512v3.381c0 .402.068.69.205.861.137.172.363.258.68.258.242 0 .451-.066.627-.199v.82Zm5.578.059h-.961v-.938h-.024c-.418.72-1.033 1.079-1.845 1.079-.598 0-1.067-.159-1.407-.475-.336-.316-.503-.736-.503-1.26 0-1.12.66-1.773 1.98-1.957l1.799-.252c0-1.02-.412-1.529-1.237-1.529-.722 0-1.375.246-1.957.738v-.984c.59-.375 1.27-.563 2.039-.563 1.411 0 2.116.746 2.116 2.239V21Zm-.961-3.035-1.447.2c-.446.062-.782.173-1.008.333-.227.156-.34.436-.34.838 0 .293.103.533.31.72.211.184.491.276.838.276.477 0 .869-.166 1.178-.498.313-.336.469-.76.469-1.271v-.598ZM697.969 21h-.961v-3.422c0-1.273-.465-1.91-1.395-1.91-.48 0-.879.182-1.195.545-.313.36-.469.814-.469 1.365V21h-.961v-6h.961v.996h.024c.453-.758 1.109-1.137 1.968-1.137.657 0 1.159.213 1.506.639.348.422.522 1.033.522 1.834V21Zm6.937 0h-.961v-1.02h-.023c-.445.774-1.133 1.16-2.063 1.16-.754 0-1.357-.267-1.81-.802-.449-.54-.674-1.272-.674-2.197 0-.993.25-1.787.75-2.385.5-.598 1.166-.897 1.998-.897.824 0 1.424.325 1.799.973h.023v-3.715h.961V21Zm-.961-2.713v-.885c0-.484-.16-.894-.48-1.23-.32-.336-.727-.504-1.219-.504-.586 0-1.047.215-1.383.645-.336.43-.504 1.023-.504 1.78 0 .692.161 1.239.481 1.641.324.399.758.598 1.301.598.535 0 .968-.193 1.3-.58.336-.387.504-.875.504-1.465Zm3.399-4.81a.61.61 0 0 1-.621-.622c0-.18.06-.328.181-.445a.6.6 0 0 1 .44-.181c.176 0 .324.06.445.181a.584.584 0 0 1 .188.445.59.59 0 0 1-.188.44.604.604 0 0 1-.445.182Zm.468 7.523h-.96v-6h.96v6Zm6.926 0h-.961v-3.422c0-1.273-.465-1.91-1.394-1.91-.481 0-.879.182-1.195.545-.313.36-.469.814-.469 1.365V21h-.961v-6h.961v.996h.023c.453-.758 1.11-1.137 1.969-1.137.656 0 1.158.213 1.506.639.347.422.521 1.033.521 1.834V21Zm6.938-.48c0 2.203-1.055 3.304-3.164 3.304-.742 0-1.391-.14-1.946-.422v-.96c.676.374 1.321.562 1.934.562 1.477 0 2.215-.785 2.215-2.356v-.656h-.024c-.457.766-1.144 1.149-2.062 1.149-.746 0-1.348-.266-1.805-.797-.453-.535-.679-1.252-.679-2.15 0-1.02.244-1.83.732-2.432.492-.602 1.164-.903 2.016-.903.808 0 1.408.325 1.798.973h.024V15h.961v5.52Zm-.961-2.233v-.885c0-.476-.162-.884-.486-1.224a1.584 1.584 0 0 0-1.202-.51c-.593 0-1.058.217-1.394.65-.336.43-.504 1.034-.504 1.81 0 .669.16 1.204.48 1.606.325.399.752.598 1.284.598.539 0 .976-.191 1.312-.574.34-.383.51-.873.51-1.47Zm3.24 2.842a.631.631 0 0 1-.463-.194.641.641 0 0 1-.187-.462.64.64 0 0 1 .187-.463.622.622 0 0 1 .463-.2.63.63 0 0 1 .469.2.63.63 0 0 1 .193.463.63.63 0 0 1-.193.463.638.638 0 0 1-.469.193Zm66.012 0a.631.631 0 0 1-.463-.194.642.642 0 0 1-.188-.462c0-.18.063-.334.188-.463a.622.622 0 0 1 .463-.2.63.63 0 0 1 .469.2.635.635 0 0 1 .193.463c0 .18-.065.334-.193.463a.64.64 0 0 1-.469.193Z"/>
-  <path fill="#0078D4" d="M734.004 21h-4.359v-8.402h.984v7.511h3.375V21Zm5.982-2.76h-4.236c.016.668.195 1.184.539 1.547.344.363.816.545 1.418.545.676 0 1.297-.223 1.863-.668v.902c-.527.383-1.224.575-2.091.575-.848 0-1.514-.272-1.999-.815-.484-.547-.726-1.314-.726-2.303 0-.933.264-1.693.791-2.279.531-.59 1.189-.885 1.975-.885.785 0 1.392.254 1.822.762.429.508.644 1.213.644 2.115v.504Zm-.984-.814c-.004-.555-.139-.986-.404-1.295-.262-.309-.627-.463-1.096-.463-.453 0-.838.162-1.154.486-.317.325-.512.748-.586 1.272h3.24ZM745.74 21h-.961v-.938h-.023c-.418.72-1.033 1.079-1.846 1.079-.598 0-1.066-.159-1.406-.475-.336-.316-.504-.736-.504-1.26 0-1.12.66-1.773 1.98-1.957l1.799-.252c0-1.02-.412-1.529-1.236-1.529-.723 0-1.375.246-1.957.738v-.984c.59-.375 1.269-.563 2.039-.563 1.41 0 2.115.746 2.115 2.239V21Zm-.961-3.035-1.447.2c-.445.062-.781.173-1.008.333-.226.156-.34.436-.34.838a.93.93 0 0 0 .311.72c.211.184.49.276.838.276.476 0 .869-.166 1.178-.498.312-.336.468-.76.468-1.271v-.598Zm5.901-1.992c-.168-.13-.41-.194-.727-.194-.41 0-.754.194-1.031.58-.274.387-.41.914-.41 1.582V21h-.961v-6h.961v1.236h.023c.137-.421.346-.75.627-.984.281-.238.596-.357.943-.357.25 0 .442.027.575.082v.996ZM756.703 21h-.961v-3.422c0-1.273-.465-1.91-1.394-1.91a1.52 1.52 0 0 0-1.196.545c-.312.36-.468.814-.468 1.365V21h-.961v-6h.961v.996h.023c.453-.758 1.109-1.137 1.969-1.137.656 0 1.158.213 1.506.639.347.422.521 1.033.521 1.834V21Zm13.629 0h-.961v-3.445c0-.664-.103-1.145-.31-1.442-.204-.297-.547-.445-1.032-.445-.41 0-.759.188-1.049.563-.285.374-.427.824-.427 1.347V21h-.961v-3.563c0-1.18-.455-1.769-1.365-1.769-.422 0-.77.178-1.043.533-.274.352-.411.81-.411 1.377V21h-.961v-6h.961v.95h.024c.426-.727 1.047-1.09 1.863-1.09.41 0 .768.115 1.072.345.305.227.514.525.627.897.446-.829 1.11-1.243 1.993-1.243 1.32 0 1.98.815 1.98 2.444V21Zm4.324.14c-.886 0-1.595-.279-2.127-.837-.527-.563-.791-1.307-.791-2.233 0-1.008.276-1.795.826-2.361.551-.566 1.295-.85 2.233-.85.894 0 1.592.276 2.092.826.504.551.756 1.315.756 2.292 0 .957-.272 1.724-.815 2.302-.539.575-1.264.862-2.174.862Zm.071-5.472c-.618 0-1.106.21-1.465.633-.36.418-.539.996-.539 1.734 0 .711.181 1.272.545 1.682.363.41.849.615 1.459.615.621 0 1.097-.201 1.429-.604.336-.402.504-.974.504-1.716 0-.75-.168-1.328-.504-1.735-.332-.406-.808-.609-1.429-.609Zm7.582.305c-.168-.13-.411-.194-.727-.194-.41 0-.754.194-1.031.58-.274.387-.41.914-.41 1.582V21h-.961v-6h.961v1.236h.023c.137-.421.346-.75.627-.984.281-.238.596-.357.943-.357.25 0 .442.027.575.082v.996Zm5.865 2.267h-4.236c.015.668.195 1.184.539 1.547.343.363.816.545 1.418.545.675 0 1.296-.223 1.863-.668v.902c-.528.383-1.225.575-2.092.575-.848 0-1.514-.272-1.998-.815-.484-.547-.727-1.314-.727-2.303 0-.933.264-1.693.791-2.279.532-.59 1.19-.885 1.975-.885.785 0 1.393.254 1.822.762.43.508.645 1.213.645 2.115v.504Zm-.985-.814c-.003-.555-.138-.986-.404-1.295-.262-.309-.627-.463-1.096-.463-.453 0-.837.162-1.154.486-.316.325-.512.748-.586 1.272h3.24Zm-58.646 4.963h60.111v.697h-60.111v-.697Z"/>
-  <path fill="#fff" d="M927 6a2 2 0 0 1 2-2h86c1.1 0 2 .895 2 2v20c0 1.105-.9 2-2 2h-86a2 2 0 0 1-2-2V6Z"/>
-  <path fill="#323130" d="M958.759 22h-1.613v-6.344c0-.52.031-1.155.095-1.907h-.027c-.1.428-.189.736-.267.923L954.021 22H952.9l-2.932-7.273a6.831 6.831 0 0 1-.26-.978h-.027c.036.392.054 1.032.054 1.92V22h-1.504v-9.803h2.29l2.578 6.529c.196.5.323.875.382 1.12h.035c.168-.514.305-.897.41-1.148l2.625-6.5h2.208V22Zm3.042-8.47a.966.966 0 0 1-.67-.253.838.838 0 0 1-.274-.642.86.86 0 0 1 .274-.65.951.951 0 0 1 .67-.26c.269 0 .497.087.683.26a.85.85 0 0 1 .281.65.848.848 0 0 1-.281.636.966.966 0 0 1-.683.26Zm.786 8.47h-1.586v-7h1.586v7Zm8.449-.56c0 2.57-1.292 3.855-3.876 3.855-.911 0-1.707-.153-2.386-.458v-1.45c.766.438 1.493.657 2.181.657 1.663 0 2.495-.818 2.495-2.454v-.766h-.027c-.524.893-1.313 1.34-2.365 1.34-.853 0-1.541-.31-2.065-.93-.519-.624-.779-1.46-.779-2.508 0-1.19.28-2.136.841-2.837.56-.702 1.33-1.053 2.31-1.053.925 0 1.611.378 2.058 1.135h.027V15h1.586v6.44Zm-1.572-2.646v-.91c0-.491-.164-.91-.492-1.257a1.586 1.586 0 0 0-1.217-.526c-.602 0-1.073.223-1.415.67-.337.442-.506 1.061-.506 1.859 0 .688.162 1.24.485 1.654.328.41.761.615 1.299.615.547 0 .991-.196 1.333-.588.342-.396.513-.902.513-1.517Zm7.697-2.283c-.191-.15-.467-.226-.827-.226-.469 0-.861.212-1.176.636-.314.424-.471 1-.471 1.73V22h-1.586v-7h1.586v1.442h.027c.155-.492.392-.875.711-1.148a1.616 1.616 0 0 1 1.08-.417c.287 0 .506.043.656.13v1.504ZM983.655 22h-1.538v-1.094h-.027c-.483.839-1.192 1.258-2.126 1.258-.688 0-1.228-.187-1.62-.56-.388-.374-.581-.869-.581-1.484 0-1.322.761-2.092 2.283-2.31l2.078-.294c0-.998-.474-1.497-1.422-1.497-.834 0-1.586.287-2.256.86v-1.387c.739-.437 1.591-.656 2.557-.656 1.768 0 2.652.87 2.652 2.611V22Zm-1.531-3.439-1.47.206c-.455.059-.8.17-1.032.335-.228.16-.342.442-.342.847 0 .296.105.54.315.732.214.186.499.28.854.28.483 0 .882-.169 1.197-.506.319-.342.478-.77.478-1.285v-.609Zm7.164 3.364c-.31.155-.718.232-1.224.232-1.358 0-2.037-.651-2.037-1.955v-3.958h-1.169V15h1.169v-1.62l1.586-.451V15h1.675v1.244h-1.675v3.5c0 .415.075.711.226.889.15.178.401.266.752.266.269 0 .501-.077.697-.232v1.258Zm7.212-2.994h-4.771c.018.647.216 1.146.594 1.497.383.35.907.526 1.573.526.747 0 1.433-.223 2.057-.67v1.279c-.638.4-1.481.601-2.529.601-1.03 0-1.839-.317-2.427-.95-.583-.638-.875-1.534-.875-2.687 0-1.089.321-1.975.964-2.659.647-.688 1.449-1.032 2.406-1.032.957 0 1.698.308 2.222.923s.786 1.47.786 2.563v.609Zm-1.531-1.121c-.005-.57-.139-1.012-.404-1.327-.264-.319-.628-.478-1.093-.478a1.55 1.55 0 0 0-1.162.499c-.315.333-.509.768-.581 1.306h3.24Z"/>
-  <path fill="#8A8886" d="M929 5h86V3h-86v2Zm87 1v20h2V6h-2Zm-1 21h-86v2h86v-2Zm-87-1V6h-2v20h2Zm1 1a1 1 0 0 1-1-1h-2a3 3 0 0 0 3 3v-2Zm87-1c0 .552-.45 1-1 1v2c1.66 0 3-1.343 3-3h-2Zm-1-21c.55 0 1 .448 1 1h2c0-1.657-1.34-3-3-3v2Zm-86-2a3 3 0 0 0-3 3h2a1 1 0 0 1 1-1V3Z"/>
-</svg>
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "バナー画像の削除"
}
```

### Explanation
このコードの差分は、`banner.svg`というSVGファイルがドキュメントから削除されたことを示しています。具体的には、ファイル内のすべての行が削除されており、合計で9行のコードが削除されています。このバナーは、おそらく「逆互換性」や「サービス」などの情報を伝えるために使用されていましたが、現在は使用されなくなったか、別の形式での表現が求められている可能性があります。

この変更により、ウェブページやアプリケーション内でこのビジュアル要素が失われ、ユーザーにとっての視覚的な情報提供が減少します。この影響は、コンテンツの可読性やユーザー体験に関連しており、特にこのバナーが重要な役割を果たしていた場合、ユーザーにとっての混乱や不便を招くことも考えられます。このため、リファレンスやドキュメント上でのバナーに関する関連情報も見直す必要があるかもしれません。

## articles/ai-services/language-service/conversational-language-understanding/media/backwards-compatibility/migration-overview.svg{#item-766cbd}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "マイグレーション概要図の削除"
}
```

### Explanation
このコードの差分は、`migration-overview.svg`というSVGファイルがドキュメントから削除されたことを示しています。この変更により、53行のコードが削除され、SVGファイルの内容が完全に失われています。このマイグレーション概要図は、ある機能やサービスの移行手順やプロセスを視覚的に示していた可能性があります。

この変更は、ユーザーがマイグレーションに関連する情報を視覚的に理解するための重要なリソースが失われたことを意味します。その結果、ユーザーにとって、マイグレーションに関する理解が難しくなる可能性があります。また、今後の文書やガイドラインを修正する必要が生じるかもしれません。特に、他の図や説明がこのコンテンツを補完するものである場合、情報提供の整合性を保つための対応が必要です。全体的に、この変更はユーザー体験に重要な影響を与える可能性があります。

## articles/ai-services/language-service/conversational-language-understanding/media/backwards-compatibility/migration-progress.svg{#item-395735}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "マイグレーション進捗図の削除"
}
```

### Explanation
このコードの差分は、`migration-progress.svg`というSVGファイルがドキュメントから削除されたことを示しています。この変更により、136行のコードが削除されており、マイグレーションの進捗を示す内容が完全に失われています。

この図は、マイグレーションプロセスにおける各ステージや進捗状況を視覚的に伝えるためのものだったと考えられます。このようなビジュアル要素の削除は、ユーザーがマイグレーションの進捗を把握する手助けを失うことにつながり、特に新しい機能やサービスの導入に関して不安を引き起こす可能性があります。

したがって、この変更は、マイグレーションに関する情報の透明性や理解を低下させ、ユーザー体験において重要な影響を与えることが予想されます。今後は他の方法でこの情報を伝える手段を検討する必要があるでしょう。

## articles/ai-services/language-service/conversational-language-understanding/media/backwards-compatibility/select-applications.svg{#item-f3214c}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "アプリケーション選択図の削除"
}
```

### Explanation
このコードの差分は、`select-applications.svg`というSVGファイルがドキュメントから削除されたことを示しています。この変更により、291行のコンテンツが削除され、アプリケーションの選択に関する視覚的情報が完全に失われています。

この図は、特定のアプリケーションを選択する際のポイントや考慮すべき要素を視覚的に示したものであると推測されます。図の削除により、ユーザーは適切なアプリケーションを選ぶためのガイダンスを失い、理解が難しくなる可能性があります。このような情報がなくなると、特に新規のユーザーにとっては選択肢の評価が困難になることが予想されます。

したがって、この変更はユーザーの体験や情報の理解において重要な影響を及ぼすことが考えられます。今後は、失われた情報を補うための代替手段を提供する必要があるでしょう。

## articles/ai-services/language-service/conversational-language-understanding/media/backwards-compatibility/select-resource.svg{#item-003814}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "リソース選択図の削除"
}
```

### Explanation
このコードの差分は、`select-resource.svg`というSVGファイルがドキュメントから削除されたことを示しています。この変更により、53行のコンテンツが削除され、リソースを選択する際の視覚的情報が失われています。

この図は、リソース選択に関する情報を視覚的に提供するものであり、ユーザーが適切な選択を行うのに役立つものだったと考えられます。図の削除に伴い、ユーザーはリソースを選ぶ際のヒントやガイダンスを失うことになり、特に新しいユーザーにとってはより難易度が増すでしょう。

この変更は、文書の情報の透明性やリソース選択の簡易性に大きな影響を与える可能性があり、今後はこの情報を補うための代替手段の提供が必要です。

## articles/ai-services/language-service/conversational-language-understanding/prebuilt-component-reference.md{#item-5af620}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about which entities can be detected automatically in Convers
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-clu
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピックタイプの更新"
}
```

### Explanation
このコードの差分は、`prebuilt-component-reference.md`というMarkdownファイルに対して小さな変更が行われたことを示しています。具体的には、`ms.topic`の値が`conceptual`から`concept-article`に変更されました。この変更により、ドキュメントのトピックタイプが明確化され、より適切なカテゴリに分類されることになります。

ドキュメントのメタデータを更新することで、検索エンジンやドキュメント管理システムがコンテンツをより正確に理解し、ユーザーが必要な情報を見つけやすくなることが期待されます。このような微調整は、文書全体の質や有用性を向上させるために重要です。

## articles/ai-services/language-service/conversational-language-understanding/service-limits.md{#item-0c7212}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about the data, region, and throughput limits for Conversatio
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: limits-and-quotas
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-clu, references_regions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピックタイプの変更"
}
```

### Explanation
このコードの差分は、`service-limits.md`というMarkdownファイルに対する小さな変更を示しています。具体的には、ファイルの`ms.topic`フィールドが`conceptual`から`limits-and-quotas`に更新されました。この変更により、文書がどのような内容に関するものであるかがより明確に定義され、サービスの制限やクォータに関連する情報を示すものとなります。

この修正は、読者に対して情報の認識を向上させ、関連性のあるドキュメントとして適切に分類されることを助けます。結果的に、ユーザーは必要な情報をより迅速に見つけられるようになり、ドキュメントの利用価値が向上することが期待されます。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/quickstarts/language-studio.md{#item-b7d381}

<details>
<summary>Diff</summary>
````diff
@@ -1,70 +0,0 @@
-<!-- ---
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/05/2025
-ms.author: lajanuar
----
-
-## Prerequisites
-
-* Azure subscription - [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
-
-
-
-## Create a new Azure Language in Foundry Tools resource and Azure storage account
-
-Before you can use custom named entity recognition, you'll need to create a Language resource, which will give you the credentials that you need to create a project and start training a model. You'll also need an Azure storage account, where you can upload your dataset used to build your model.
-
-> [!IMPORTANT]
-> To quickly get started, we recommend creating a new Language resource using the steps provided in this article. Using the steps in this article lets you create Azure Language resource and storage account at the same time, which is easier than doing it later.
->
-> If you have a pre-existing resource that you'd like to use, you need to connect it to storage account. See [guidance to using a pre-existing resource](../../how-to/create-project.md#using-a-preexisting-language-resource) for information.
-
-[!INCLUDE [create a new resource from the Azure portal](../resource-creation-azure-portal.md)]
-
-
-
-## Upload sample data to blob container
-
-[!INCLUDE [Uploading sample data for custom NER](blob-storage-upload.md)]
-
-
-
-## Create a custom named entity recognition project
-
-Once your resource and storage account are configured, create a new custom NER project. A project is a work area for building your custom ML models based on your data. Your project can only be accessed by you and others who have access to Azure Language resource being used.
-
-[!INCLUDE [Create custom NER project](../language-studio/create-project.md)]
-
-
-
-## Train your model
-
-Typically after you create a project, you go ahead and start [tagging the documents](../../how-to/tag-data.md) you have in the container connected to your project. For this quickstart, you have imported a sample tagged dataset and initialized your project with the sample JSON tags file.
-
-[!INCLUDE [Train a model using Language Studio](../language-studio/train-model.md)]
-
-
-
-## Deploy your model
-
-Generally after training a model you would review its [evaluation details](../../how-to/view-model-evaluation.md) and [make improvements](../../how-to/view-model-evaluation.md) if necessary. In this quickstart, you will just deploy your model, and make it available for you to try in Language studio, or you can call the [prediction API](https://aka.ms/ct-runtime-swagger).
-
-[!INCLUDE [Deploy a model using Language Studio](../language-studio/deploy-model.md)]
-
-
-
-
-## Test your model
-
-After your model is deployed, you can start using it to extract entities from your text via [Prediction API](https://aka.ms/ct-runtime-swagger). For this quickstart, you will use the [Language Studio](https://aka.ms/LanguageStudio) to submit the custom entity recognition task and visualize the results. In the sample dataset you downloaded earlier, you can find some test documents that you can use in this step.
-
-[!INCLUDE [Test a model using Language Studio](../../../includes/custom/language-studio/test-model.md)]
-
-:::image type="content" source="../../media/test-model-results.png" alt-text="A screenshot showing the model test results." lightbox="../../media/test-model-results.png":::
-
-## Clean up resources
-
-[!INCLUDE [Delete project using Language Studio](../language-studio/delete-project.md)] -->
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioのクイックスタートガイドの削除"
}
```

### Explanation
このコードの差分は、`language-studio.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、カスタム命名エンティティ認識に関するクイックスタートガイドが含まれていました。具体的な内容としては、Azure Languageリソースの作成、サンプルデータのアップロード、カスタムNERプロジェクトの作成、モデルの訓練、デプロイ、テスト手順が記載されていました。

この削除により、ユーザーはこれまでのクイックスタートガイドにアクセスできなくなり、カスタム命名エンティティ認識の設定方法を学ぶための公式な文書が失われることになります。今後、別のコンテンツや手順が提供される必要があるかもしれません。この変更は、利用者に混乱を招く可能性があるため、適切な代替コンテンツを提示することが重要です。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/cancel-training.md{#item-b6ec08}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To cancel a training job in [Language Studio](https://aka.ms/laguageStudio), go to the **Training jobs** page. Select the training job you want to cancel, and select **Cancel** from the top menu. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "トレーニング中止に関するガイドラインの削除"
}
```

### Explanation
このコードの差分は、`cancel-training.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studioでのトレーニングジョブの中止方法に関する手順が記載されていました。

具体的には、ユーザーは**Training jobs**ページに移動し、中止したいトレーニングジョブを選択して、上部メニューから**Cancel**を選ぶことでトレーニングジョブを中止できる旨が説明されていました。この情報が削除されたことにより、ユーザーはトレーニングジョブを中止するための公式な手順を失うことになります。

この変更は、ユーザーが必要な情報を得ることができず、トレーニングジョブを適切に管理できなくなる可能性があるため、注意が必要です。今後同様の内容を提供するための代替手段を検討することが重要です。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/create-project.md{#item-9aa401}

<details>
<summary>Diff</summary>
````diff
@@ -1,46 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Sign into the [Language Studio](https://aka.ms/languageStudio). A window appears to let you select your subscription and Language resource. Select your Language resource. 
-
-2. Under the **Classify text** section of Language Studio, select **Custom text classification**.
-
-    :::image type="content" source="../../media/select-custom-text-classification.png" alt-text="A screenshot showing the location of custom text classification in Azure Language Studio landing page." lightbox="../../media/select-custom-text-classification.png":::
-        
-
-3. Select **Create new project** from the top menu in your projects page. Creating a project lets you label data, train, evaluate, improve, and deploy your models. 
-
-    :::image type="content" source="../../media/create-project.png" alt-text="A screenshot of the custom text classification project creation page." lightbox="../../media/create-project.png":::
-
-
-4.  After you select, **Create new project**, a window appears to let you connect your storage account. If you already connected a storage account, you can see it connected to your project. If not, choose your storage account from the dropdown that appears and select **Connect storage account**; this selection sets the required roles for your storage account. This step can return an error if you aren't assigned as **owner** on the storage account.
-
-    >[!NOTE]
-    > * You only need to do this step once for each new language resource you use. 
-    > * This process is irreversible, if you connect a storage account to your Language resource you can't disconnect it later.
-    > * You can only connect your Language resource to one storage account.
-
-    :::image type="content" source="../../media/connect-storage.png" alt-text="A screenshot of the storage connection screen for custom classification projects." lightbox="../../media/connect-storage.png":::
-
-5. Select project type. You can either create a **Multi label classification** project where each document can belong to one or more classes or **Single label classification** project where each document can belong to only one class. The selected type can't be changed later. Learn more about [project types](../../glossary.md#project-types)
-    
-    :::image type="content" source="../../media/project-types.png" alt-text="A screenshot of the available custom classification project types." lightbox="../../media/project-types.png":::
-
-5. Enter the project information, including a name, description, and the language of the documents in your project. If you're using the [example dataset](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/language-service/Custom%20text%20classification/Custom%20multi%20classification%20-%20movies%20summary.zip), select **English**. You can't change the name of your project later. Select **Next**.
-       
-    >[!TIP]
-    > Your dataset doesn't have to be entirely in the same language. You can have multiple documents, each with different supported languages. If your dataset contains documents of different languages or if you expect text from different languages during runtime, select **enable multi-lingual dataset** option when you enter the basic information for your project. This option can be enabled later from the **Project settings** page.
-
-6. Select the container where you uploaded your dataset. 
-    
-    >[!Note]
-    > If you have already labeled your data make sure it follows the [supported format](../../concepts/data-formats.md) and select **Yes, my documents are already labeled and I have formatted JSON labels file** and select the labels file from the drop-down menu. 
- 
-    > If you're using one of the example datasets, use the included `webOfScience_labelsFile` or `movieLabels` json file. Then select **Next**.
-    
-7. Review the data you entered and select **Create Project**.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分類プロジェクト作成ガイドの削除"
}
```

### Explanation
このコードの差分は、`create-project.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studioにおけるカスタムテキスト分類プロジェクトの作成手順が詳細に説明されていました。

具体的には、ユーザーがLanguage Studioにサインインし、テキスト分類を選択し、新しいプロジェクトを作成する過程において、必要なストレージアカウントの接続やプロジェクトの設定、データセットのアップロードに関する具体的なステップが含まれていました。この情報の削除により、ユーザーはカスタムテキスト分類プロジェクトを作成するための公式なガイドラインを失います。

この変更は、特に新規のユーザーにとってツールの使用に対する障壁を生む可能性があり、カスタムテキスト分類のプロジェクトを開始する際の混乱を招くことが考えられます。今後、同様の手順を提供する新たなコンテンツの提供が求められます。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/delete-deployment.md{#item-8e5067}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To delete a deployment from within [Language Studio](https://aka.ms/laguageStudio), go to the **Deploying a model** page. Select the deployment you want to delete and select **Delete deployment** from the top menu. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デプロイメント削除に関するガイドラインの削除"
}
```

### Explanation
このコードの差分は、`delete-deployment.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studioにおいてデプロイメントを削除する手順が記載されていました。

具体的には、ユーザーは**Deploying a model**ページにアクセスし、削除したいデプロイメントを選択し、上部メニューから**Delete deployment**を選ぶことでデプロイメントを削除できる方法が説明されていました。この情報が失われることにより、ユーザーはデプロイメントの削除プロセスに関する公式な手順を見失うことになります。

この変更は、特にLanguage Studioを使用するユーザーにとって重要な情報源を失うことから、デプロイメント管理における混乱を引き起こす可能性があります。今後、デプロイメントの削除に関する適切な情報を提供するための新しいコンテンツを準備することが必要です。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/delete-model.md{#item-e9b701}

<details>
<summary>Diff</summary>
````diff
@@ -1,16 +0,0 @@
----
-#services: cognitive-services
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To delete your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Model performance** from the left side menu.
-
-2. Select the **model name** you want to delete and select **Delete** from the top menu.
-
-3. In the window that appears, select **OK** to delete the model. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル削除に関するガイドラインの削除"
}
```

### Explanation
このコードの差分では、`delete-model.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studio内でモデルを削除するための手順が詳しく説明されていました。

具体的には、ユーザーは**Model performance**を左側のメニューから選択し、削除したいモデル名を選択した後、上部メニューから**Delete**を選ぶことでモデルを削除できる方法が記載されていました。また、削除確認のウィンドウが表示され、**OK**を選択することで削除処理が完了することが説明されていました。

この情報の削除により、ユーザーはモデルを効果的に管理する方法についての公式なガイダンスを失い、運用において混乱を招く可能性があります。したがって、今後はモデル削除に関する手続きを提供する新しいコンテンツを追加することが求められます。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/delete-project.md{#item-e2af45}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-When you don't need your project anymore, you can delete your project using [Language Studio](https://aka.ms/custom-classification). Select **Custom text classification** in the top, and then select the project you want to delete. Select **Delete** from the top menu to delete the project.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト削除に関するガイドラインの削除"
}
```

### Explanation
このコードの差分では、`delete-project.md`というMarkdownファイルが完璧に削除されたことを示しています。このファイルには、AzureのLanguage Studio内でプロジェクトを削除する手順が説明されていました。

具体的な手順としては、ユーザーは**Custom text classification**を選択し、削除したいプロジェクトを選択した後、上部メニューから**Delete**を選んでプロジェクトを削除するという流れが伝えられていました。この情報が失われることにより、プロジェクトの管理に関して重要な手順を見失う可能性があります。

この変更は、特にLanguage Studioを使用しているユーザーにとって重要なガイダンスが無くなることを意味し、プロジェクト削除に関する公式情報が提供されなくなるため、適切な手続きを行うための混乱を引き起こす恐れがあります。今後は、プロジェクト削除に関する新たな情報を考慮し、適切なドキュメントの作成が求められます。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/deploy-model.md{#item-5169f8}

<details>
<summary>Diff</summary>
````diff
@@ -1,26 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To deploy your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Deploying a model** from the left side menu.
-
-2. Select **Add deployment** to start a new deployment job.
-
-    :::image type="content" source="../../media/deploy-model.png" alt-text="A screenshot showing the deployment button" lightbox="../../media/deploy-model.png":::
-
-3. Select **Create new deployment** to create a new deployment and assign a trained model from the dropdown below. You can also **Overwrite an existing deployment** by selecting this option and select the trained model you want to assign to it from the dropdown below.
-
-    > [!NOTE]
-    > Overwriting an existing deployment doesn't require changes to your [Prediction API](https://aka.ms/ct-runtime-swagger) call but the results you get will be based on the newly assigned model.
-
-    :::image type="content" source="../../media/add-deployment.png" alt-text="A screenshot showing the deployment screen" lightbox="../../media/add-deployment.png":::
-     
-4. select **Deploy** to start the deployment job.
-
-5. After deployment is successful, an expiration date will appear next to it. [Deployment expiration](../../../concepts/model-lifecycle.md#expiration-timeline) is when your deployed model will be unavailable to be used for prediction, which typically happens **twelve** months after a training configuration expires.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルデプロイに関するガイドラインの削除"
}
```

### Explanation
このコードの差分では、`deploy-model.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studio内でモデルをデプロイするための詳細な手順が記載されていました。

具体的には、ユーザーは**Deploying a model**を選択し、**Add deployment**を選ぶことで新しいデプロイメントジョブを開始できる手順が含まれていました。また、新しいデプロイメントを作成し、トレーニング済みモデルを選択する方法、既存のデプロイメントを上書きするオプション、デプロイメントが成功した後の有効期限についても説明されていました。

この情報が削除されることにより、ユーザーはモデルデプロイメントの管理に関する重要なガイダンスを失い、手続きへの理解が不足する可能性があります。そのため、今後はモデルデプロイに関する新たな文書を作成し、利用者が適切にデプロイ作業を行えるようにすることが求められます。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/get-prediction-url.md{#item-364b8f}

<details>
<summary>Diff</summary>
````diff
@@ -1,29 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. After the deployment job is completed successfully, select the deployment you want to use and from the top menu select **Get prediction URL**.
-
-    :::image type="content" source="../../media/get-prediction-url-1.png" alt-text="A screenshot showing the button to get the prediction URL." lightbox="../../media/get-prediction-url-1.png":::
-
-2. In the window that appears, under the **Submit** pivot, copy the sample request URL and body into your command line.
-
-3. Replace `<YOUR_DOCUMENT_HERE>` with the actual text you want to extract entities from.
-
-    :::image type="content" source="../../media/get-prediction-url-2.png" alt-text="A screenshot showing the prediction URL and sample J SON request." lightbox="../../media/get-prediction-url-2.png":::
-
-4. Submit the `POST` cURL request in your terminal or command prompt. You receive a 202 response with the API results if the request was successful.
-
-5. In the response header you receive extract `{JOB-ID}` from `operation-location`, which has the format: `{ENDPOINT}/text/analytics/v3.2-preview.2/analyze/jobs/<JOB-ID}>`
-
-6. Back to Language Studio; select **Retrieve** pivot from the same window you got the example request you got earlier and copy the sample request into a text editor. 
-
-    :::image type="content" source="../../media/get-prediction-url-3.png" alt-text="A screenshot showing the button to retrieval URL." lightbox="../../media/get-prediction-url-3.png":::
-
-7. Replace `<JOB-ID>` with the `{JOB-ID}` you extracted from the previous step. 
-
-8. Submit the `GET` cURL request in your terminal or command prompt.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "予測URL取得に関するガイドラインの削除"
}
```

### Explanation
このコードの差分では、`get-prediction-url.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studioから予測URLを取得するための具体的な手順が記載されていました。

手順には、デプロイメントジョブが成功裏に完了した後に、使用したいデプロイメントを選択し、**Get prediction URL**を選ぶ方法が含まれていました。その後、表示されるウィンドウでサンプルリクエストのURLとボディを取得し、実際のテキストを使ってエンティティを抽出するための方法が詳細に説明されていました。

この情報が削除されることにより、ユーザーは予測URLを取得する際の重要な手続きを失い、APIを適切に利用できなくなる可能性があります。そのため、予測URL取得に関する新たな文書を作成し、利用者が正しく操作できるようにする必要があります。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/import-project.md{#item-8482b0}

<details>
<summary>Diff</summary>
````diff
@@ -1,47 +0,0 @@
----
-titleSuffix: Foundry Tools
-#services: cognitive-services
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Sign into the [Language Studio](https://aka.ms/languageStudio). A window appears to let you select your subscription and Language resource. Select your Language resource. 
-
-2. Under the **Classify text** section of Language Studio, select **Custom text classification**.
-
-    :::image type="content" source="../../media/select-custom-text-classification.png" alt-text="A screenshot showing the location of custom text classification in Azure Language Studio landing page." lightbox="../../media/select-custom-text-classification.png":::
-        
-
-3. Select **Create new project** from the top menu in your projects page. Creating a project lets you label data, train, evaluate, improve, and deploy your models. 
-
-    :::image type="content" source="../../media/create-project.png" alt-text="A screenshot of the project creation page." lightbox="../../media/create-project.png":::
-
-
-4.  After you select **Create new project**, a screen will appear to let you connect your storage account. If you can’t find your storage account, make sure you created a resource using the recommended steps. If you've already connected a storage account to your Language resource, you can see your storage account connected.
-
-    >[!NOTE]
-    > * You only need to do this step once for each new language resource you use. 
-    > * This process is irreversible, if you connect a storage account to your Language resource you cannot disconnect it later.
-    > * You can only connect your Language resource to one storage account.
-
-    :::image type="content" source="../../media/connect-storage.png" alt-text="A screenshot of the storage connection screen for custom classification projects." lightbox="../../media/connect-storage.png":::
-
-5. Select project type. You can either create a **Multi label classification** project where each document can belong to one or more classes or **Single label classification** project where each document can belong to only one class. The selected type can't be changed later. 
-    
-    :::image type="content" source="../../media/project-types.png" alt-text="A screenshot of the available custom classification project types." lightbox="../../media/project-types.png":::
-
-5. Enter the project information, including a name, description, and the language of the documents in your project. You won’t be able to change the name of your project later. Select **Next**.
-       
-    >[!TIP]
-    > Your dataset doesn't have to be entirely in the same language. You can have multiple documents, each with different supported languages. If your dataset contains documents of different languages or if you expect text from different languages during runtime, select **enable multi-lingual dataset** option when you enter the basic information for your project. This option can be enabled later from the **Project settings** page.
-
-6. Select the container where you uploaded your dataset. 
-
-7. Select **Yes, my documents are already labeled and I have formatted JSON labels file** and select the labels file from the drop-down menu below to import your JSON labels file. Make sure it follows the [supported format](../../concepts/data-formats.md).
-
-7.   Select **Next**.
-
-8. Review the data you entered and select **Create Project**.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクトインポート手順の削除"
}
```

### Explanation
このコードの差分では、`import-project.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studio内でプロジェクトをインポートするための詳細な手順が記載されていました。

手順には、Language Studioにサインインし、言語リソースを選択することから始まり、カスタムテキスト分類のプロジェクトを作成する方法が含まれていました。この過程では、ストレージアカウントの接続、プロジェクトタイプの選択、プロジェクト名や説明、データセットの選択、JSONラベルファイルのインポートなど、複数のステップが詳細に説明されていました。

この情報が削除されることにより、ユーザーはプロジェクトをインポートする手続きを失い、モデルのトレーニングや評価、デプロイに必要な準備ができなくなる可能性があります。そのため、プロジェクトインポートに関する新たな文書を作成し、利用者が正しく操作できるようにする必要があります。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/model-evaluation.md{#item-b3ab55}

<details>
<summary>Diff</summary>
````diff
@@ -1,81 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Go to your project page in [Language Studio](https://aka.ms/languageStudio).
-
-2. Select **Model performance** from the menu on the left side of the screen.
-
-3. On this page, you can only view the successfully trained models, F1 score for each model and [model expiration date](../../../concepts/model-lifecycle.md). You can select the model name for more details about its performance.
-
-> [!NOTE]
-> Classes that aren't labeled or predicted in the test set aren't part of the displayed results.
-
-### [Overview](#tab/overview)
-
-* In this tab you can view the model's details such as: F1 score, precision, recall, date, and time for the training job, total training time, and number of training and testing documents included in this training job.  
-
-    :::image type="content" source="../../media/overview.png" alt-text="Screenshot that shows the overview page for model evaluation." lightbox="../../media/overview.png":::
-
-* You can also see [guidance](../../concepts/evaluation-metrics.md#guidance) on how to improve the model. When you select *view details*, a side panel opens to give more guidance on how to improve the model. In this example, there aren't enough data in training set for these classes. Also, there's unclear distinction between class types in training set, where two classes are confused with each other. By selecting the confused classes, you're taken to the [data labeling](../../how-to/tag-data.md) page to label more data with the correct class.
-
-    :::image type="content" source="../../media/overview-guidance.png" alt-text="A screenshot that shows the guidance page for model evaluation." lightbox="../../media/overview-guidance.png":::
-    
-    Learn more about model guidance and confusion matrix in [model performance](../../concepts/evaluation-metrics.md) concepts.
-
-### [Class type performance](#tab/class-performance)
-
-* This view is a snapshot of how your model performed during testing. The metrics here are static and tied to your model, so they don't update until you train again.
-
-* You can see the precision, recall, F1 score, and number of training and testing labels for each class.
-
-    :::image type="content" source="../../media/class-performance.png" alt-text="A screenshot of entity performance." lightbox="../../media/class-performance.png":::
-
-### [Test set details](#tab/test-set)
-
-* Here you can see the documents included in the **test set** and the result class for each document. You can use the *Show mismatches only* toggle to show only documents with mismatches, or unselect the toggle to view all document in the test set.
-
-* For each document, you can view: labeled text, its respective labeled class and what class it was predicted with. Also, you can see whether it's a [true positive](../../concepts/evaluation-metrics.md), [false positive](../../concepts/evaluation-metrics.md), or [false negative](../../concepts/evaluation-metrics.md). 
-
-    :::image type="content" source="../../media/test-set.png" alt-text="A screenshot of test set details." lightbox="../../media/test-set.png":::
-    
-### [Dataset distribution](#tab/dataset-distribution) 
-
-This snapshot shows how entities are distributed across your training and testing sets. This data is static and tied to your model, so it doesn't update until you train again.
-
-* You can view the dataset distribution in *graph* or *table* view.
-
-**Graph view**
-
-*Documents with at least one label*: This view shows for each class, the number of occurrences for this class across the training and testing sets.
-
-  :::image type="content" source="../../media/graph-view.png" alt-text="A screenshot showing distribution in graph view." lightbox="../../media/graph-view.png":::
-
-**Table view**
-
-For each *class*, you can view: tagged documents in training set, tagged documents in testing set and total tagged documents.
-
-  :::image type="content" source="../../media/table-view.png" alt-text="A screenshot showing distribution in table view." lightbox="../../media/table-view.png":::
-
-### [Confusion matrix](#tab/confusion-matrix) 
-
-> [!NOTE]
-> Confusion matrix isn't available for multi classification projects.
-
-A [confusion matrix](../../concepts/evaluation-metrics.md#confusion-matrix) is an N x N matrix used for evaluating the performance of a classification model, where N is the number of target classes. The matrix compares the actual target values with the values predicted by the machine learning model to show how well the extraction model is performing and what kinds of errors it's making.
-
-You can view the confusion matrix in *normalized* or *raw count* view.
-
-  :::image type="content" source="../../media/confusion.png" alt-text="A screenshot of a confusion matrix in Language Studio." lightbox="../../media/confusion.png":::
-
-* All values: Shows the confusion matrix for all classes.
-
-* Only errors: Shows the confusion matrix for classes with errors only.
-
-* Only matches: Shows the confusion matrix for classes with correct predictions only.
-
----
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル評価に関するガイドラインの削除"
}
```

### Explanation
このコードの差分では、`model-evaluation.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studioにおけるモデルを評価するための手順やガイドラインが詳細に記載されていました。

具体的には、モデルのパフォーマンスを確認するためのステップ、F1スコアや精度、再現率などの評価指標の解説、クラス別のパフォーマンス、テストセットの詳細、データセットの分布状況、混同行列の表示方法について説明されていました。また、各セクションには、視覚的な説明のためのスクリーンショットが含まれており、ユーザーが評価結果を理解しやすくするために役立っていました。

この情報が削除されることにより、ユーザーはモデルの性能を適切に評価する手続きを失い、精度や改善点を把握することが難しくなります。そのため、モデル評価に関する新たな文書を作成し、利用者が正しく評価できるようにする必要があります。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/project-details.md{#item-ba2c45}

<details>
<summary>Diff</summary>
````diff
@@ -1,21 +0,0 @@
----
-titleSuffix: Foundry Tools
-#services: cognitive-services
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Go to your **project settings** page in [Language Studio](https://aka.ms/languageStudio).
-
-1. You can see project details.
-
-1. On this page, you can update project description and enable/disable Multi-lingual dataset in project settings.
-
-1. You can also view the connected storage account and container to your Language resource.
-
-1. You can also retrieve your resource primary key from this page.
-
-    :::image type="content" source="../../media/project-details.png" alt-text="A screenshot of the project settings page." lightbox="../../media/project-details.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト詳細に関する情報の削除"
}
```

### Explanation
このコードの差分では、`project-details.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studioにおけるプロジェクトの詳細設定に関する情報が記載されていました。

具体的には、プロジェクト設定ページにアクセスする方法、プロジェクトの説明を更新する方法、多言語データセットの有効化または無効化、接続されているストレージアカウントとコンテナの表示、リソースのプライマリキーの取得方法などが詳細に説明されていました。この情報は、ユーザーがプロジェクトを適切に管理し、設定を変更するために必要な手助けをしていました。

このコンテンツが削除されることにより、ユーザーはプロジェクトの設定や管理に関する手順を失い、作業の効率が低下する可能性があります。したがって、プロジェクト詳細に関する新たな文書を作成し、利用者が正しく理解できるようにする必要があります。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/resource-creation-language-studio.md{#item-cad76b}

<details>
<summary>Diff</summary>
````diff
@@ -1,31 +0,0 @@
----
-titleSuffix: Foundry Tools
-#services: cognitive-services
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-### Create a new Language resource from Language Studio
-
-If it's your first time logging in, you'll see a window in [Language Studio](https://aka.ms/languageStudio) that lets you choose an existing Language resource or create a new one. You can also create a resource by clicking the settings icon in the top-right corner, selecting **Resources**, then clicking **Create a new resource**.
-
-Create a Language resource with following details.
-
-|Instance detail  |Required value  |
-|---------|---------|
-|Azure subscription| **Your Azure subscription**|
-|Azure resource group| **Your Azure resource group**|
-|Azure resource name| **Your Azure resource name**|
-|Location | The [region](../../service-limits.md#regional-availability) where your Language resource.      |
-|Pricing tier     | The [pricing tier](../../service-limits.md#language-resource-limits) for your Language resource.        |
-
-> [!IMPORTANT]
-> * Make sure to enable **Managed Identity** when you create a Language resource. 
-> * Read and confirm Responsible AI notice
-
-To use custom text classification, you'll need to connect your resource to a storage account. If you don't have one, you can  [create an Azure storage account](/azure/storage/common/storage-account-create). Use the following steps to create your first project and connect your storage account.
-
-[!INCLUDE [Language Studio project creation](create-project.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioにおけるリソース作成手順の削除"
}
```

### Explanation
このコードの差分では、`resource-creation-language-studio.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studioで新しい言語リソースを作成するための具体的な手順が詳しく説明されていました。

具体的には、Language Studioへの初回ログイン時に表示されるウィンドウから既存のリソースを選択したり、新しいリソースを作成したりする方法、リソース作成に必要な詳細（Azureサブスクリプション、リソースグループ、リソース名、ロケーション、価格帯など）が示されていました。また、リソースを作成する際に「Managed Identity」を有効にすることや、責任あるAIに関する注意事項の確認が重要であることも強調されていました。

この情報が削除されることにより、ユーザーはLanguage Studioでのリソース作成手続きを理解する手助けを失い、新しいプロジェクトを作成する際に困難を抱える可能性があります。したがって、リソース作成に関する新たな文書を用意し、利用者が正しく手続きを行えるようにする必要があります。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/swap-deployment.md{#item-e26e67}

<details>
<summary>Diff</summary>
````diff
@@ -1,17 +0,0 @@
----
-titleSuffix: Foundry Tools
-#services: cognitive-services
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To swap deployments from within [Language Studio](https://aka.ms/laguageStudio)
-
-1. In **Deploying a model** page, select the two deployments you want to swap and select **Swap deployments** from the top menu. 
-
-2. From the window that appears, select the names of the deployments you want to swap.
-
-    <!--:::image type="content" source="../media/swap-deployment.png" alt-text="A screenshot showing a swapped deployment in Language Studio." lightbox="../media/swap-deployment.png":::-->
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioにおけるデプロイのスワップ手順の削除"
}
```

### Explanation
このコードの差分では、`swap-deployment.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studio内でのデプロイのスワップ手順に関する具体的な情報が含まれていました。

具体的には、モデルをデプロイするページでスワップしたい2つのデプロイを選択し、メニューから「デプロイのスワップ」を選ぶ方法や、表示されるウィンドウからスワップするデプロイの名前を選択する手順が説明されていました。また、スワップ操作に関連する画像も参照することができました。

この情報が削除されることにより、ユーザーはLanguage Studio内でデプロイをスワップする方法を理解する手助けを失い、それに伴うプロセスを効率的に実行できなくなる可能性があります。したがって、デプロイのスワップに関する新たな文書を作成し、ユーザーが適切に操作できるようにする必要があります。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/test-model.md{#item-b0f78f}

<details>
<summary>Diff</summary>
````diff
@@ -1,27 +0,0 @@
----
-#services: cognitive-services
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
-ms.custom: language-service-custom-classification
----
-To test your deployed models within [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Testing deployments** from the menu on the left side of the screen.
-
-2. Select the deployment you want to test. You can only test models that are assigned to deployments. 
-
-3. For multilingual projects, select the language of the text you're testing using the language dropdown.
-
-4. Select the deployment you want to query/test from the dropdown.
-
-5. Enter the text you want to submit in the request, or upload a `.txt` document to use. If you’re using one of the example datasets, you can use one of the included .txt files.
-
-6. Select **Run the test** from the top menu.
-
-7. In the **Result** tab, you can see the predicted classes for your text. You can also view the JSON response under the **JSON** tab. The following example is for a single label classification project. A multi label classification project can return more than one class in the result. 
-
-    :::image type="content" source="../../media/test-model-results.png" alt-text="A screenshot showing model test results for a single label classification project." lightbox="../../media/test-model-results.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioにおけるモデルテスト手順の削除"
}
```

### Explanation
このコードの差分では、`test-model.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studioでデプロイされたモデルをテストするための具体的な手順が詳述されていました。

具体的には、左側のメニューから「テストのデプロイメント」を選択し、テストしたいデプロイメントを選ぶ手順や、マルチリンガルプロジェクトの場合の言語選択、リクエストに送信するテキストの入力または`.txt`文書のアップロード方法、テストを実行するための操作が説明されていました。また、テストの結果として得られる予測クラスやJSONレスポンスの表示方法についても詳しく記載されていました。

この情報が削除されることにより、ユーザーはLanguage Studio内でモデルをテストする方法を理解する手助けを失い、モデルの性能を評価することが困難になる可能性があります。そのため、ユーザーが適切にモデルをテストできるよう、新しいガイドラインを提供することが必要です。

## articles/ai-services/language-service/custom-text-classification/includes/language-studio/train-model.md{#item-704d2a}

<details>
<summary>Diff</summary>
````diff
@@ -1,30 +0,0 @@
----
-#services: cognitive-services
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
-ms.custom: language-service-custom-classification
----
-To start training your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Training jobs** from the left side menu.
-
-2. Select **Start a training job** from the top menu.
-
-3. Select **Train a new model** and type in the model name in the text box. You can also **overwrite an existing model** by selecting this option and choosing the model you want to overwrite from the dropdown menu. Overwriting a trained model is irreversible, but it won't affect your deployed models until you deploy the new model.
-
-    :::image type="content" source="../../media/train-model.png" alt-text="Create a new training job" lightbox="../../media/train-model.png":::
-    
-4. Select data splitting method. You can choose **Automatically splitting the testing set from training data** where the system will split your labeled data between the training and testing sets, according to the specified percentages. Or you can **Use a manual split of training and testing data**, this option is only enabled if you added documents to your testing set during [data labeling](../../how-to/tag-data.md). See [How to train a model](../../how-to/train-model.md#data-splitting) for more information on data splitting.
-
-4. Select the **Train** button.
-
-5. If you select the training job ID from the list, a side pane will appear where you can check the **Training progress**, **Job status**, and other details for this job.
-
-    > [!NOTE]
-    > * Only successfully completed training jobs will generate models.
-    > * The time to train the model can take anywhere between a few minutes to several hours based on the size of your labeled data.
-    > * You can only have one training job running at a time. You can't start other training job within the same project until the running job is completed.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioにおけるモデルのトレーニング手順の削除"
}
```

### Explanation
このコードの差分では、`train-model.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studio内でモデルをトレーニングするための具体的な手順が詳細に記載されていました。

内容としては、左側のメニューから「トレーニングジョブ」を選択し、「トレーニングジョブを開始」を選ぶ手順、あるいは新しいモデルの名前を入力するセクションや、既存のモデルを上書きするオプションについての説明が含まれていました。また、データの分割方法を選択する方法や、トレーニングの進行状況を確認するための手順についても記載されていました。

この情報が削除されることによって、ユーザーはLanguage Studio内で新しいモデルをトレーニングする方法を理解するための重要なガイドラインを失うことになります。そのため、ユーザーが適切にモデルをトレーニングできるよう、代替のドキュメントを提供する必要があります。

## articles/ai-services/language-service/custom-text-classification/includes/quickstarts/language-studio.md{#item-1caefc}

<details>
<summary>Diff</summary>
````diff
@@ -1,72 +0,0 @@
----
-#services: cognitive-services
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
-ms.custom: language-service-custom-classification
----
-## Prerequisites
-
-* Azure subscription - [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-
-
-
-## Create a new Azure Language in Foundry Tools resource and Azure storage account
-
-Before you can use custom text classification, you need to create a Language resource, which gives you the credentials that you need to create a project and start training a model. You also need an Azure storage account, where you can upload your dataset that is used to build your model.
-
-> [!IMPORTANT]
-> To quickly get started, we recommend creating a new Language resource using the steps provided in this article. Using the steps in this article lets you create Azure Language resource and storage account at the same time, which is easier than doing it later.
->
-> If you have a [preexisting resource](../../how-to/create-project.md#using-a-preexisting-language-resource) that you'd like to use, you need to connect it to storage account.
->
-> Adding the role **Storage Blob Data Contributor** is essential for interacting with *any resource* that utilizes the storage account.
-
-[!INCLUDE [create a new resource from the Azure portal](../resource-creation-azure-portal.md)]
-    
-
-
-## Upload sample data to blob container
-
-[!INCLUDE [Uploading sample data for custom tex classification](blob-storage-upload.md)]
-    
-
-
-## Create a custom text classification project
-
-Once your resource and storage container are configured, create a new custom text classification project. A project is a work area for building your custom ML models based on your data. Your project is only accessible to you and others who have access to Azure Language resource being used.
-
-[!INCLUDE [Create a project using Language Studio](../language-studio/create-project.md)]
-    
-
-
-## Train your model
-
-Typically after you create a project, you go ahead and start [labeling the documents](../../how-to/tag-data.md) you have in the container connected to your project. For this quickstart, you imported a sample labeled dataset and initialized your project with the sample JSON labels file.
-
-[!INCLUDE [Train a model using Language Studio](../language-studio/train-model.md)]
-
-
-
-## Deploy your model
-
-Generally after training a model you would review its [evaluation details](../../how-to/view-model-evaluation.md) and [make improvements](../../how-to/view-model-evaluation.md) if necessary. In this quickstart, you deploy your model, and make it available for you to try in Language Studio, or you can call the [prediction API](https://aka.ms/ct-runtime-swagger).
-
-[!INCLUDE [Deploy a model using Language Studio](../language-studio/deploy-model.md)]
-
-
-
-## Test your model
-
-After your model is deployed, you can start using it to classify your text via [Prediction API](https://aka.ms/ct-runtime-swagger). For this quickstart, you use the [Language Studio](https://aka.ms/LanguageStudio) to submit the custom text classification task and visualize the results. In the sample dataset, you downloaded earlier you can find some test documents that you can use in this step.
-
-[!INCLUDE [Test a model using Language Studio](../language-studio/test-model.md)]
-
-
-
-## Clean up projects
-
-[!INCLUDE [Delete project using Language Studio](../language-studio/delete-project.md)]
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioのクイックスタートガイドの削除"
}
```

### Explanation
このコードの差分では、`language-studio.md`というMarkdownファイルが完全に削除されたことを示しています。このファイルには、AzureのLanguage Studioを用いてカスタムテキスト分類を迅速に開始するための手順が記載されていました。

具体的には、Azureサブスクリプションの作成、LanguageリソースとAzureストレージアカウントの設定、サンプルデータのアップロード、カスタムテキスト分類プロジェクトの作成、モデルのトレーニング、デプロイ、テスト、そしてプロジェクトのクリーンアップに至るまでの一連のプロセスが説明されていました。また、各ステップには関連するインクルードファイルへの参照や重要な注意点も含まれていました。

この情報の削除により、ユーザーはLanguage Studioを使用してカスタムテキスト分類を行うための基本的な手順やガイダンスを失うことになります。そのため、新しいユーザーにとって障壁が高くなり、カスタムモデルを構築する際のサポートが不足する可能性があります。この機能の文書化を継続するために、適切な代替手段を提供することが重要です。

## articles/ai-services/language-service/orchestration-workflow/concepts/data-formats.md{#item-7a72ee}

<details>
<summary>Diff</summary>
````diff
@@ -5,14 +5,14 @@ description: Learn about the data formats accepted by orchestration workflow.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom:  language-service-orchestration
 ---
 # Data formats accepted by orchestration workflow
 
-When data is used by your model for learning, it expects the data to be in a specific format. When you tag your data in Language Studio, it gets converted to the JSON format described in this article. You can also manually tag your files.
+When data is used by your model for learning, it expects the data to be in a specific format. When you tag your data, it gets converted to the JSON format described in this article. You can also manually tag your files.
 
 
 ## JSON file format
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ形式のドキュメントの軽微な修正"
}
```

### Explanation
このコードの差分では、`data-formats.md`というMarkdownファイルが修正されました。具体的には、文書のメタデータと本文の一部に軽微な変更が加えられています。

1. メタデータの更新:
   - `ms.topic`の値が`conceptual`から`concept-article`に変更され、文書の種類がより明確に示されています。これにより、この文書がコンセプトに関連する記事であることが強調されます。

2. 本文の修正:
   - タグ付けの説明において、「Language Studio」に関連する部分が省略され、より簡潔な表現に変更されました。「タグ付けをすると、データがJSON形式に変換される」という内容が、より一般的な文脈で表現されています。

これらの変更は、文書の明確さと一貫性を向上させ、ユーザーがデータフォーマットに関する理解を深めることを目的としています。全体として、内容の正確性や可読性を高めるための小規模な更新と考えられます。

## articles/ai-services/language-service/orchestration-workflow/concepts/evaluation-metrics.md{#item-954044}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about evaluation metrics in orchestration workflow
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-orchestration
@@ -14,7 +14,7 @@ ms.custom: language-service-orchestration
 
 Your dataset is split into two parts: a set for training, and a set for testing. The training set is used to train the model, while the testing set is used as a test for model after training to calculate the model performance and evaluation. The testing set isn't introduced to the model through the training process, to make sure that the model is tested on new data. <!--See [data splitting](../how-to/train-model.md#data-splitting) for more information-->
 
-Model evaluation is triggered automatically after training is completed successfully. The evaluation process starts by using the trained model to predict user defined intents for utterances in the test set, and compares them with the provided tags (which establishes a baseline of truth). The results are returned so you can review the model’s performance. For evaluation, orchestration workflow uses the following metrics:
+Model evaluation is triggered automatically after training is completed successfully. The evaluation process starts by using the trained model to predict user defined intents for utterances in the test set, and compares them with the provided tags (which establishes a baseline of truth). The results are returned so you can review the model's performance. For evaluation, orchestration workflow uses the following metrics:
 
 * **Precision**: Measures how precise/accurate your model is. It's the ratio between the correctly identified positives (true positives) and all identified positives. The precision metric reveals how many of the predicted classes are correctly labeled. 
 
@@ -113,4 +113,4 @@ You can calculate the model-level evaluation metrics from the confusion matrix:
 
 ## Next steps
 
-[Train a model in Language Studio](../how-to/train-model.md)
+[Train a model](../how-to/train-model.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価メトリクスに関するドキュメントの軽微な修正"
}
```

### Explanation
このコードの差分では、`evaluation-metrics.md`というMarkdownファイルが修正されました。変更は主にメタデータと本文の一部に関連しています。

1. メタデータの更新:
   - `ms.topic`の値が`conceptual`から`concept-article`に変更されており、この文書がコンセプトに関する記事として扱われることを示しています。文書の分類がより明確になり、読者にとって内容が理解しやすくなっています。

2. 本文の修正:
   - 本文中の「モデルの評価結果をレビューできる」という部分で、所有格の表現が「モデルの性能」から「モデルの性能」に修正され、文章が一貫性を持つようになっています。
   - 最後のセクションで、リンクテキストが「Language Studioでモデルをトレーニングする」から「モデルをトレーニングする」に簡略化されており、情報が簡潔に伝えられるようになっています。

これらの軽微な修正は、文書の全体的な明瞭性と整合性を向上させる目的で行われています。また、ユーザーが評価メトリクスに関する情報を効率的に取得できるように配慮されています。全体として、内容の質は向上していますが、大きな変更はありません。

## articles/ai-services/language-service/orchestration-workflow/concepts/fail-over.md{#item-ad9d67}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to save and recover your orchestration workflow models.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom:  language-service-orchestration
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フェイルオーバーに関するドキュメントの軽微な修正"
}
```

### Explanation
このコードの差分では、`fail-over.md`というMarkdownファイルが修正されました。変更内容は主にメタデータに関連しています。

1. メタデータの更新:
   - `ms.topic`の値が`conceptual`から`concept-article`に変更されました。この変更により、この文書がコンセプトに関する記事であることが明確になり、読者にとっての理解が容易になっています。

この軽微な修正は、文書の分類をわかりやすくし、関連情報へのアクセスを改善することを目的としています。文書の内容自体には変更がなく、全体としては品質向上のための調整が行われています。

## articles/ai-services/language-service/orchestration-workflow/concepts/none-intent.md{#item-c47b2f}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about the default None intent in orchestration workflow.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom:  language-service-orchestration
@@ -27,7 +27,7 @@ The score should be set according to your own observations of prediction scores,
 
 When you export a project's JSON file, the None score threshold is defined in the _**"settings"**_ parameter of the JSON as the _**"confidenceThreshold"**_, which accepts a decimal value between 0.0 and 1.0.
 
-The default score for Orchestration Workflow projects is set at **0.5** when creating new project in Language Studio.
+The default score for Orchestration Workflow projects is set at **0.5** when creating a new project.
 
 > [!NOTE]
 > During model evaluation of your test set, the None score threshold is not applied.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Noneインテントに関するドキュメントの軽微な修正"
}
```

### Explanation
このコードの差分では、`none-intent.md`というMarkdownファイルが修正されました。変更内容はメタデータと本文の一部に関するものです。

1. メタデータの更新:
   - `ms.topic`の値が`conceptual`から`concept-article`に変更されており、この文書がコンセプトに関する記事として認識されるようになっています。この変更により、文書の分類が明確になり、読者にとっての理解が容易になります。

2. 本文の修正:
   - 文中の「Language Studioで新しいプロジェクトを作成する際には、デフォルトのスコアが**0.5**に設定されています」という部分の表現が変更され、より簡潔な「新しいプロジェクトを作成する際には、デフォルトのスコアが**0.5**に設定されています」となっています。これにより文がより流暢に読めるようになっています。

これらの変更は、文書の明瞭性と一貫性を向上させることを目的としており、内容の質が向上しています。全体として、大きな変更はないものの、文書の可読性が改善されています。

## articles/ai-services/language-service/orchestration-workflow/faq.md{#item-30440d}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: faq
-ms.date: 11/18/2025
+ms.date: 12/17/2025
 ms.author: lajanuar
 ms.custom: mode-other
 ---
@@ -16,21 +16,21 @@ Use this article to quickly get the answers to common questions about orchestrat
 
 ## How do I create a project?
 
-See the [quickstart](./quickstart.md) to quickly create your first project, or the [how-to article](./how-to/create-project.md) for more details. 
+For more information, *see* the [quickstart](./quickstart.md) to quickly create your first project, or the [how-to article](./how-to/create-project.md).
 
 ## How do I connect other service applications in orchestration workflow projects?
 
-See [How to create projects and build schemas](./how-to/create-project.md) for information on connecting another project as an intent.
+For more information, *see* [How to create projects and build schemas](./how-to/create-project.md).
 
-## Which LUIS applications can I connect to in orchestration workflow projects?
+## Which `LUIS` applications can I connect to in orchestration workflow projects?
 
-LUIS applications that use Azure Language resource as their authoring resource will be available for connection. You can only connect to LUIS applications that are owned by the same resource. This option will only be available for resources in West Europe, as it's the only common available region between LUIS and CLU.
+`LUIS` applications that use Azure Language resource as their authoring resource are available for connection. You can only connect to `LUIS` applications that are owned via the same resource. This option is only available for resources in West Europe, as it's the only common available region between `LUIS` and `CLU`.
 
 ## Which question answering project can I connect to in orchestration workflow projects?
 
-Question answering projects that use Azure Language resource will be available for connection. You can only connect to question answering projects that are in the same Language resource.
+Question answering projects that use Azure Language resource are available for connection. You can only connect to question answering projects that are in the same Language resource.
 
-## Training is taking a long time, is this expected?
+## Training is taking a long time, is this time period expected?
 
 For orchestration projects, long training times are expected. Based on the number of examples you have your training times may vary from 5 minutes to 1 hour or more. 
 
@@ -45,19 +45,19 @@ See the [language support](./language-support.md) article.
 -->
 ## How do I get more accurate results for my project?
 
-See [evaluation metrics](./concepts/evaluation-metrics.md) for information on how models are evaluated, and metrics you can use to improve accuracy.
+For more information, *see*  [evaluation metrics](./concepts/evaluation-metrics.md).
 <!--
 ## How many intents, and utterances can I add to a project?
 
 See the [service limits](./service-limits.md) article. 
 -->
-## Can I label the same word as 2 different entities?
+## Can I label the same word as two different entities?
 
-Unlike LUIS, you cannot label the same text as 2 different entities. Learned components across different entities are mutually exclusive, and only one learned span is predicted for each set of characters.
+Unlike `LUIS`, you can't label the same text as two different entities. Learned components across different entities are mutually exclusive, and only one learned span is predicted for each set of characters.
 
 ## Is there any SDK support?
 
-Yes, only for predictions, and [samples are available](https://aka.ms/cluSampleCode). There is currently no authoring support for the SDK.
+Yes, only for predictions, and [samples are available](https://aka.ms/cluSampleCode). There's currently no authoring support for the SDK.
 
 ## Are there APIs for this feature?
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQドキュメントの軽微な修正"
}
```

### Explanation
このコードの差分では、`faq.md`というMarkdownファイルが修正されました。具体的には、文書のメタデータと本文の内容が更新されています。

1. メタデータの変更:
   - `ms.date`の更新が行われ、日付が`11/18/2025`から`12/17/2025`に変更されました。これにより、文書が最新の情報を反映することが強調されています。

2. 本文の変更:
   - いくつかの文の表現が更新され、より明確に、かつ流暢に表現されています。例えば、「See」から「For more information, *see*」に変更され、指示がわかりやすくなっています。
   - `LUIS`という用語がバッククオートで囲まれ、強調されるようになっています。この変更により、技術用語への注意が向けられ、視認性が向上しています。
   - 一部の表現がより自然な日本語に修正され、可読性が高まっています。

これらの修正は、文書全体の明瞭さと一貫性を高め、ユーザーにとって使いやすいFAQを提供することを目的としています。全体として、情報の質が改善されており、ユーザーが質問に対する回答を迅速に得られるように工夫されています。

## articles/ai-services/language-service/orchestration-workflow/glossary.md{#item-386170}

<details>
<summary>Diff</summary>
````diff
@@ -5,47 +5,47 @@ description: Learn about definitions used in orchestration workflow.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
-ms.date: 11/18/2025
+ms.topic: glossary
+ms.date: 12/17/2025
 ms.author: lajanuar
 ms.custom: language-service-orchestration
 ---
 # Terms and definitions used in orchestration workflow 
 Use this article to learn about some of the definitions and terms you may encounter when using orchestration workflow. 
 
 ## F1 score
-The F1 score is a function of Precision and Recall. It's needed when you seek a balance between [precision](#precision) and [recall](#recall).
+The F1 score is a function of Precision and Recall. The score is needed when you seek a balance between [precision](#precision) and [recall](#recall).
 
 ## Intent
-An intent represents a task or action the user wants to perform. It is a purpose or goal expressed in a user's input, such as booking a flight, or paying a bill.
+An intent represents a task or action the user wants to perform. It's a purpose or goal expressed in a user's input, such as booking a flight, or paying a bill.
 
 ## Model
-A model is an object that's trained to do a certain task, in this case conversation understanding tasks. Models are trained by providing labeled data to learn from so they can later be used to understand utterances.
+A model is an object trained to do a certain task, in this case conversation understanding tasks. Models are trained by providing labeled data to learn from so they can later be used to understand utterances.
 
 * **Model evaluation** is the process that happens right after training to know how well does your model perform.
 * **Deployment** is the process of assigning your model to a deployment to make it available for use via the [prediction API](https://aka.ms/ct-runtime-swagger).
 
 ## Overfitting
-Overfitting happens when the model is fixated on the specific examples and is not able to generalize well.
+Overfitting happens when the model is fixated on the specific examples and isn't able to generalize well.
 
 ## Precision
 Measures how precise/accurate your model is. It's the ratio between the correctly identified positives (true positives) and all identified positives. The precision metric reveals how many of the predicted classes are correctly labeled.
 
 ## Project
-A project is a work area for building your custom ML models based on your data. Your project can only be accessed by you and others who have access to the Azure resource being used.
+A project is a work area for building your custom ML models based on your data. Your project is only accessible for you and others who have access to the Azure resource being used.
 
 ## Recall
-Measures the model's ability to predict actual positive classes. It's the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted classes are correct.
+Measures the model's ability to predict actual positive classes. It's the ratio between the predicted true positives and what was tagged. The recall metric reveals how many of the predicted classes are correct.
 
 ## Schema
-Schema is defined as the combination of intents within your project. Schema design is a crucial part of your project's success. When creating a schema, you want think about which intents should be included in your project
+Schema is defined as the combination of intents within your project. Schema design is a crucial part of your project's success. When creating a schema, you want to think about which intents should be included in your project
 
 ## Training data
 Training data is the set of information that is needed to train a model.
 
 ## Utterance
 
-An utterance is user input that is short text representative of a sentence in a conversation. It is a natural language phrase such as "book 2 tickets to Seattle next Tuesday". Example utterances are added to train the model and the model predicts on new utterance at runtime
+An utterance is a short text representative of a sentence in a conversation. It's a natural language phrase such as "book two tickets to Seattle next Tuesday." Example utterances are added to train the model and the model predicts on new utterance at runtime
 
 
 ## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "用語集ドキュメントの軽微な修正"
}
```

### Explanation
このコードの差分では、`glossary.md`というMarkdownファイルが修正され、いくつかの表現が改善されています。以下は主な変更点です。

1. メタデータの更新:
   - `ms.topic`の値が`conceptual`から`glossary`に変更され、文書の内容が用語集としての役割を明確にしています。
   - `ms.date`も`11/18/2025`から`12/17/2025`に更新され、最新の日付が反映されています。

2. 本文の表現改善:
   - 用語定義の説明において、文の流れや自然さが改善されています。たとえば、「The score is needed when you seek a balance between precision and recall」という表現になり、より具体的にポイントが伝わるようになっています。
   - 一部の文に助詞やつなぎ言葉が追加され、文がより自然に読めるようになりました。また、数字や単語の表記（例：`two`から`2`など）が統一されています。

3. 定義の明確化:
   - いくつかの用語（例：`Model`, `Project`, `Utterance`）において、説明がより具体的に改善されており、読み手が直感的に理解しやすくなっています。

これらの変更は、文書の明瞭性と利用価値を向上させており、ユーザーが用語や概念をより簡単に理解できるように工夫されています。全体として、用語集の機能性と役立つ情報がより強化されています。

## articles/ai-services/language-service/orchestration-workflow/how-to/build-schema.md{#item-ea718c}

<details>
<summary>Diff</summary>
````diff
@@ -12,40 +12,20 @@ ms.custom: language-service-orchestration
 ---
 # How to build your project schema for orchestration workflow
  
-In orchestration workflow projects, the *schema* is defined as the combination of intents within your project. Schema design is a crucial part of your project's success. When creating a schema, you want think about which intents that should be included in your project.
+In orchestration workflow projects, the *schema* is defined as the combination of intents within your project. Schema design is a crucial part of your project's success. When creating a schema, you should think about the intents to include in your project.
 
 ## Guidelines and recommendations
 
 Consider the following guidelines and recommendations for your project:
 
-*	Build orchestration projects when you need to manage the NLU for a multi-faceted virtual assistant or chatbot, where the intents, entities, and utterances would begin to be far more difficult to maintain over time in one project.
-*	Orchestrate between different domains. A domain is a collection of intents and entities that serve the same purpose, such as Email commands vs. Restaurant commands.
-*	If there is an overlap of similar intents between domains, create the common intents in a separate domain and removing them from the others for the best accuracy.
-*	For intents that are general across domains, such as “Greeting”, “Confirm”, “Reject”, you can either add them in a separate domain or as direct intents in the Orchestration project. 
-*	Orchestrate to Custom question answering knowledge base when a domain has FAQ type questions with static answers. Ensure that the vocabulary and language used to ask questions is distinctive from the one used in the other Conversational Language Understanding projects and LUIS applications.
-*	If an utterance is being misclassified and routed to an incorrect intent, then add similar utterances to the intent to influence its results. If the intent is connected to a project, then add utterances to the connected project itself. After you retrain your orchestration project, the new utterances in the connected project will influence predictions.
-*	Add test data to your orchestration projects to validate there isn’t confusion between linked projects and other intents.
+*    Build orchestration projects when you need to manage the NLU for a multi-faceted virtual assistant or chatbot.
+*    Orchestrate between different domains. A domain is a collection of intents and entities that serve the same purpose, such as Email commands vs. Restaurant commands.
+*    If there's an overlap of similar intents between domains, create the common intents in a separate domain and removing them from the others for the best accuracy.
+*    For intents that are general across domains, such as `Greeting`, `Confirm`, or `Reject`, you can either add them in a separate domain or as direct intents in the Orchestration project. 
+*    Orchestrate to Custom question answering knowledge base when a domain has FAQ type questions with static answers. Ensure that the vocabulary and language used to ask questions is distinctive from the one used in the other Conversational Language Understanding projects and LUIS applications.
+*    If an utterance is being misclassified and routed to an incorrect intent, then add similar utterances to the intent to influence its results. If the intent is connected to a project, then add utterances to the connected project itself. After you retrain your orchestration project, the new utterances in the connected project will influence predictions.
+*    Add test data to your orchestration projects to validate there isn't confusion between linked projects and other intents.
 
-
-## Add intents
-
-To build a project schema within [Language Studio](https://aka.ms/languageStudio):
-
-1. Select **Schema definition** from the left side menu.
-
-2. To create an intent, select **Add** from the top menu. You will be prompted to type in a name for the intent.
-
-3. To connect your intent to other existing projects, select **Yes, I want to connect it to an existing project** option. You can alternatively create a non-connected intent by selecting the **No, I don't want to connect to a project** option. 
-
-4. If you choose to create a connected intent, choose from **Connected service** the service you're connecting to, then choose the **project name**. You can connect your intent to only one project from the following services: [CLU](../../conversational-language-understanding/overview.md) , [LUIS](../../../luis/what-is-luis.md) or [Question answering](../../question-answering/overview.md).
-  
-   :::image type="content" source="../media/build-schema-page.png" alt-text="A screenshot showing the schema creation page in Language Studio." lightbox="../media/build-schema-page.png":::
-   
-> [!TIP]
-> Use connected intents to connect to other projects (conversational language understanding, LUIS, and question answering)
-   
-5. Select **Add intent** to add your intent.
- 
 ## Next steps
 
 * [Add utterances](tag-utterances.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スキーマ構築に関する手順の更新"
}
```

### Explanation
このコードの差分では、`build-schema.md`というMarkdownファイルに対していくつかの軽微な修正が行われています。主な変更点は次の通りです。

1. **メインコンテンツの整理**:
   - スキーマの定義に関する文がわずかに変更され、「あなたは考えるべきです。」という表現が「あなたは考えるべきです。」に修正され、よりフォーマルなトーンになっています。

2. **ガイドラインと推奨事項の簡素化**:
   - ガイドラインセクション内のリスト項目が短縮され、簡潔に表現されています。前の長い説明が削除され、各ポイントがより明確に記述されています。
   - 具体的な内容（例：Emailコマンドやレストランコマンドの区別など）の説明が保持されているため、使用者が理解しやすくなっています。

3. **不要なセクションの削除**:
   - 「Add intents」というセクションが削除され、手順が簡素化されました。このセクションは詳細すぎて冗長な印象を与える可能性があったため、全体の流れがスムーズになります。

4. **圧縮した指示**:
   - 手順は具体的なアクションの説明を持ったままで簡略化されており、非常に短く、直接的な指示にゆとりがあります。

これらの変更は、文書の可読性を高め、読者が情報を迅速に取得できるようにしており、スキーマ構築に関する理解を促進する効果があります。全体として、より使いやすいと感じられる内容に整えられています。

## articles/ai-services/language-service/orchestration-workflow/how-to/call-api.md{#item-f50775}

<details>
<summary>Diff</summary>
````diff
@@ -15,24 +15,10 @@ ms.custom: language-service-clu
 # Query deployment for intent predictions
 
 After the deployment is added successfully, you can query the deployment for intent and entities predictions from your utterance based on the model you assigned to the deployment.
-You can query the deployment programmatically [Prediction API](https://aka.ms/ct-runtime-swagger) or through the [Client libraries (Azure SDK)](#send-an-orchestration-workflow-request). 
+You can query the deployment programmatically [Prediction API](https://aka.ms/ct-runtime-swagger) or through the [Client libraries (Azure SDK)](#use-the-client-libraries-azure-sdk).
 
 ## Test deployed model
 
-You can use Language Studio to submit an utterance, get predictions and visualize the results.
-
-[!INCLUDE [Test model](../includes/language-studio/test-model.md)]
-
----
-
-## Send an orchestration workflow request
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Get prediction URL](../includes/language-studio/get-prediction-url.md)]
-
-# [REST APIs](#tab/REST-APIs)
-
 First you need to get your resource key and endpoint:
 
 [!INCLUDE [Get keys and endpoint Azure portal](../includes/get-keys-endpoint-azure.md)]
@@ -49,7 +35,7 @@ First you need to get your resource key and endpoint:
 
 ### Use the client libraries (Azure SDK)
 
-You can also use the client libraries provided by the Azure SDK to send requests to your model. 
+You can also use the client libraries provided by the Azure SDK to send requests to your model.
 
 > [!NOTE]
 > The client library for conversational language understanding is only available for:
@@ -58,27 +44,27 @@ You can also use the client libraries provided by the Azure SDK to send requests
 
 1. Go to your resource overview page in the [Azure portal](https://portal.azure.com/#home)
 
-2. From the menu on the left side, select **Keys and Endpoint**. Use endpoint for the API requests and you will need the key for `Ocp-Apim-Subscription-Key` header.
+1. From the menu on the left side, select **Keys and Endpoint**. Use endpoint for the API requests and you will need the key for `Ocp-Apim-Subscription-Key` header.
 
     :::image type="content" source="../../custom-text-classification/media/get-endpoint-azure.png" alt-text="Screenshot showing how to get the Azure endpoint." lightbox="../../custom-text-classification/media/get-endpoint-azure.png":::
 
-3. Download and install the client library package for your language of choice:
-    
+1. Download and install the client library package for your language of choice:
+
     |Language  |Package version  |
     |---------|---------|
     |.NET     | [1.0.0](https://www.nuget.org/packages/Azure.AI.Language.Conversations/1.0.0)        |
     |Python     | [1.0.0](https://pypi.org/project/azure-ai-language-conversations/1.0.0)         |
-    
-4. After you've installed the client library, use the following samples on GitHub to start calling the API.
-    
+
+1. After you've installed the client library, use the following samples on GitHub to start calling the API.
+
     * [C#](https://github.com/Azure/azure-sdk-for-net/tree/Azure.AI.Language.Conversations_1.0.0/sdk/cognitivelanguage/Azure.AI.Language.Conversations)
     * [Python](https://github.com/Azure/azure-sdk-for-python/tree/azure-ai-language-conversations_1.0.0/sdk/cognitivelanguage/azure-ai-language-conversations)
-    
-5. See the following reference documentation for more information:
-    
+
+1. See the following reference documentation for more information:
+
     * [C#](/dotnet/api/azure.ai.language.conversations)
     * [Python](/python/api/azure-ai-language-conversations/azure.ai.language.conversations.aio)
-    
+
 ---
 
 ## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "API呼び出し手順の簡略化と修正"
}
```

### Explanation
このコードの差分では、`call-api.md`というMarkdownファイルに対して行われた修正がいくつかあります。以下は主な変更点です。

1. **リンクの変更**:
   - [Client libraries (Azure SDK)]というリンクの表記が、「[use the client libraries (Azure SDK)]」に更新されました。これにより、より具体的な操作が示され、読者が直感的に内容を理解しやすくなっています。

2. **不要なセクションの削除**:
   - 「Test deployed model」セクション内の詳細な情報を取り除き、関連情報のインクルードが削除されました。これにより、文書がよりすっきりとした印象を与えるようになります。

3. **ステップの整理**:
   - 手順の番号と内容が整理され、無駄な空行が削除されました。これにより、手順がシンプルで読みやすくなっています。
   - ステップの表現が短くなり、より明確な指示を提供する形になっています。

4. **内容の明瞭化**:
   - 「Use the client libraries (Azure SDK)」セクションにおける手順やサンプルリンクが簡素化され、利用者がすぐにAPIを呼び出すためのリソースにアクセスしやすくなっています。

これらの変更により、文書全体が素早く理解でき、読者がAPIを呼び出す手順をよりスムーズに実行できるように工夫されています。全体として、内容が簡潔になり、利用者にとって使いやすくなっています。

## articles/ai-services/language-service/orchestration-workflow/how-to/create-project.md{#item-5dadf0}

<details>
<summary>Diff</summary>
````diff
@@ -34,86 +34,36 @@ Before you start using orchestration workflow, you will need a Language resource
 
 [!INCLUDE [create a new resource from the Azure portal](../includes/resource-creation-azure-portal.md)]
 
-[!INCLUDE [create a new resource from Language Studio](../includes/resource-creation-language-studio.md)]
-
-## Sign in to Language Studio
-
-To create a new intent, select *+Add* button and start by giving your intent a **name**. You can see two options, to connect to a project or not. You can connect to (LUIS, question answering, or Conversational Language Understanding) projects, or choose the **no** option.
-
-
-## Create an orchestration workflow project
+## Create an orchestration workflow project (REST API)
 
 Once you have a Language resource created, create an orchestration workflow project. 
 
-### [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Create project](../includes/language-studio/create-project.md)]
-
-### [REST APIs](#tab/rest-api)
 
 [!INCLUDE [create project](../includes/rest-api/create-project.md)]
 
----
-## Import an orchestration workflow project
-
-### [Language Studio](#tab/language-studio)
-
-You can export an orchestration workflow project as a JSON file at any time by going to the orchestration workflow projects page, selecting a project, and from the top menu, selecting **Export**.
-
-That project can be reimported as a new project. If you import a project with the exact same name, it replaces the project's data with the newly imported project's data.
-
-To import a project, select the arrow button next to **Create a new project** and select **Import**, then select the JSON file.
-
-:::image type="content" source="../media/import-export.png" alt-text="A screenshot showing the Conversational Language Understanding import button." lightbox="../media/import-export.png":::
-
-### [REST APIs](#tab/rest-api)
+## Import an orchestration workflow project (REST API)
 
 You can import an orchestration workflow JSON into the service
 
 [!INCLUDE [Import project](../includes/rest-api/import-project.md)]
 
----
-
-## Export project
-
-### [Language Studio](#tab/language-studio)
-
-You can export an orchestration workflow project as a JSON file at any time by going to the orchestration workflow projects page, selecting a project, and pressing **Export**.
-
-### [REST APIs](#tab/rest-api)
+## Export project (REST API)
 
 You can export an orchestration workflow project as a JSON file at any time.
 
 [!INCLUDE [Export project](../includes/rest-api/export-project.md)]
 
----
-## Get orchestration project details
-
-### [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Language Studio project details](../includes/language-studio/project-details.md)]
-
-### [REST APIs](#tab/rest-api)
+## Get orchestration project details (REST API)
 
 [!INCLUDE [REST APIs project details](../includes/rest-api/project-details.md)]
 
----
-
-## Delete project 
-
-### [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Delete project](../includes/language-studio/delete-project.md)]
 
-### [REST APIs](#tab/rest-api)
+## Delete project (REST API)
 
 When you don't need your project anymore, you can delete your project using the APIs.
 
 [!INCLUDE [Delete project](../includes/rest-api/delete-project.md)]
 
----
-
-
 
 :::image type="content" source="../media/quickstart-intent.png" alt-text="A screenshot showing how to import orchestration project." lightbox="../media/quickstart-intent.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト作成手順の簡略化とREST APIに関するリファクタリング"
}
```

### Explanation
このコードの差分では、`create-project.md`というMarkdownファイルに対していくつかの軽微な変更が行われています。以下は主な変更点です。

1. **セクションの統一化**:
   - それぞれの操作に関する詳細が「(REST API)」という形で明示され、REST API使用時の具体的な手順がわかりやすくなっています。

2. **冗長な情報の削除**:
   - 記事からかなりの行が削除され、冗長な情報が取り除かれました。これにより、重要な情報に焦点を当てつつ、全体の流れが整理され、読みやすくなっています。

3. **手順の簡略化**:
   - 「Sign in to Language Studio」や「Create an orchestration workflow project」などのセクションが簡潔になり、必要な情報が明確に伝わる形式に改善されています。

4. **手順の可視化**:
   - 各手順の説明が短縮されつつも、関連するインクルードファイルのリンクが保持されているため、読者が必要な情報を適切に参照できるようになっています。具体的な画像のリンクもそのまま残されており、視覚的な理解を助ける要素が維持されています。

これらの変更により、文書はより明快で目的を達成しやすくなっています。結果的に、ユーザーがプロジェクトを作成する際のステップが簡単に追える内容になっています。

## articles/ai-services/language-service/orchestration-workflow/how-to/deploy-model.md{#item-36ebf2}

<details>
<summary>Diff</summary>
````diff
@@ -20,17 +20,11 @@ Once you're satisfied with how your model performs, it's ready to be deployed, a
 * [Labeled utterances](tag-utterances.md) and successfully [trained model](train-model.md)
 <!--* Reviewed the [model evaluation details](view-model-evaluation.md) to determine how your model is performing.-->
 
-See [project development lifecycle](../overview.md#project-development-lifecycle) for more information.
+For more information, *see*  [project development lifecycle](../overview.md#project-development-lifecycle).
 
 ## Deploy model
 
-After you have reviewed the model's performance and decide it's fit to be used in your environment, you need to assign it to a deployment to be able to query it. Assigning the model to a deployment makes it available for use through the [prediction API](https://aka.ms/clu-apis). It is recommended to create a deployment named `production` to which you assign the best model you have built so far and use it in your system. You can create another deployment called `staging` to which you can assign the model you're currently working on to be able to test it. You can have a maximum on 10 deployments in your project. 
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Deploy a model using Language Studio](../includes/language-studio/deploy-model.md)]
-   
-# [REST APIs](#tab/rest-api)
+After you reviewed the model's performance and decide it's a good fit for use in your environment, you need to assign it to a deployment to be able to query it. Assigning the model to a deployment makes it available for use through the [prediction API](https://aka.ms/clu-apis). We recommended that you create a deployment named `production` to which you assign the best model you built so far and use it in your system. You can create another deployment called `staging` to which you can assign the model you're currently working on to be able to test it. You can have a maximum on 10 deployments in your project. 
 
 ### Submit deployment job
 
@@ -40,66 +34,33 @@ After you have reviewed the model's performance and decide it's fit to be used i
 
 [!INCLUDE [get deployment status](../includes/rest-api/get-deployment-status.md)]
 
----
-
 ## Swap deployments
 
 After you're done testing a model assigned to one deployment, you might want to assign it to another deployment. Swapping deployments involves:
 * Taking the model assigned to the first deployment, and assigning it to the second deployment. 
 * taking the model assigned to second deployment and assign it to the first deployment. 
 
-This can be used to swap your `production` and `staging` deployments when you want to take the model assigned to `staging` and assign it to `production`. 
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Swap deployments](../includes/language-studio/swap-deployment.md)]
-
-# [REST APIs](#tab/rest-api)
+This step can be used to swap your `production` and `staging` deployments when you want to take the model assigned to `staging` and assign it to `production`. 
 
 [!INCLUDE [Swap deployments](../includes/rest-api/swap-deployment.md)]
 
----
-
 ## Delete deployment
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Delete deployment](../includes/language-studio/delete-deployment.md)]
-
-# [REST APIs](#tab/rest-api)
-
 [!INCLUDE [Delete deployment](../includes/rest-api/delete-deployment.md)]
 
----
-
 ## Assign deployment resources
 
 You can [deploy your project to multiple regions](../../concepts/custom-features/multi-region-deployment.md) by assigning different Language resources that exist in different regions.
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Assign resource](../../conversational-language-understanding/includes/language-studio/assign-resources.md)]
-
-# [REST APIs](#tab/rest-api)
 
 [!INCLUDE [Assign resource](../../conversational-language-understanding/includes/rest-api/assign-resources.md)]
 
----
-
 ## Unassign deployment resources
 
-When unassigning or removing a deployment resource from a project, you will also delete all the deployments that have been deployed to that resource's region.
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Unassign resource](../../conversational-language-understanding/includes/language-studio/unassign-resources.md)]
-
-# [REST APIs](#tab/rest-api)
+When unassigning or removing a deployment resource from a project, you can also delete all the deployments that are deployed to that resource region.
 
 [!INCLUDE [Unassign resource](../../conversational-language-understanding/includes/rest-api/unassign-resources.md)]
 
----
-
 ## Next steps
 
 Use [prediction API to query your model](call-api.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルデプロイ手順の簡略化と表現の改善"
}
```

### Explanation
このコードの差分では、`deploy-model.md`というMarkdownファイルに関する変更が行われています。以下は主な変更点です。

1. **テキストの簡潔化**:
   - モデルのパフォーマンスを評価した後の手順が、冗長な表現から簡潔な説明に更新されました。具体的には、手順や推奨事項がより明瞭に提示され、読者にとって理解しやすくなりました。

2. **セクションの整理**:
   - 「Swap deployments」や「Delete deployment」などのセクションで冗長な情報が削除され、リンクが統合されました。このことにより、文書が整理され、必要な情報が一箇所に集中するようになっています。

3. **表現の統一性**:
   - "[Language Studio]"や"[REST APIs]"の見出しが削除され、情報が自然に流れる形になっています。この改善により、セクション間のつながりが強調され、ユーザーが順序を追いやすくなっています。

4. **注意喚起の強化**:
   - デプロイメントのリソースを削除する際の注意点が強調され、これにより読者がリスクを理解できるようになっています。

全体として、この更新は文書の可読性を向上させ、ユーザーがモデルをデプロイする際の手順をよりスムーズに理解できるよう配慮されています。

## articles/ai-services/language-service/orchestration-workflow/how-to/tag-utterances.md{#item-e80df9}

<details>
<summary>Diff</summary>
````diff
@@ -10,17 +10,17 @@ ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-orchestration
 ---
-# Add utterances in Language Studio
+# Add utterances
 
-Once you have [built a schema](build-schema.md), you should add training and testing utterances to your project. The utterances should be similar to what your users will use when interacting with the project. When you add an utterance, you have to assign which intent it belongs to.
+Once you [build a schema](build-schema.md), you should add training and testing utterances to your project. The utterances should be similar to what your users use when interacting with the project. When you add an utterance, you have to assign which intent it belongs to.
 
-Adding utterances is a crucial step in project development lifecycle; this data is used in the next step when training your model so that your model can learn from the added data. If you already have utterances, you can directly [import it into your project](create-project.md#import-an-orchestration-workflow-project), but you need to make sure that your data follows the [accepted data format](../concepts/data-formats.md). Labeled data informs the model how to interpret text, and is used for training and evaluation.
+Adding utterances is a crucial step in project development lifecycle; this data is used in the next step when training your model so that your model can learn from the added data. If you already have utterances, you can directly [import it into your project](create-project.md#import-an-orchestration-workflow-project-rest-api), but you need to make sure that your data follows the [accepted data format](../concepts/data-formats.md). Labeled data informs the model how to interpret text, and is used for training and evaluation.
 
 ## Prerequisites
 
 * A successfully [created project](create-project.md).
 
-See the [project development lifecycle](../overview.md#project-development-lifecycle) for more information.
+For more information, *see* [project development lifecycle](../overview.md#project-development-lifecycle).
 
 
 ## How to add utterances
@@ -31,19 +31,19 @@ Use the following steps to add utterances:
 
 2. From the left side menu, select **Add utterances**.
 
-3. From the top pivots, you can change the view to be **training set** or **testing set**.  Learn more about [training and testing sets](train-model.md#data-splitting) and how they're used for model training and evaluation.
+3. From the top pivots, you can change the view to be **training set** or **testing set**. Learn more about [training and testing sets](train-model.md#data-splitting) and how they're used for model training and evaluation.
+
+3. From the **Select intent** dropdown menu, select one of the intents. Type in your utterance, and select the `enter` key in the utterance's text box to add the utterance. You can also upload your utterances directly by selecting **Upload utterance file** from the top menu. Make sure the utterances follow the [accepted format](../concepts/data-formats.md#utterance-format).
 
-3. From the **Select intent** dropdown menu, select one of the intents. Type in your utterance, and press the enter key in the utterance's text box to add the utterance. You can also upload your utterances directly by selecting **Upload utterance file** from the top menu, make sure it follows the [accepted format](../concepts/data-formats.md#utterance-format).
-    
     > [!Note]
     > If you're planning on using **Automatically split the testing set from training data** splitting, add all your utterances to the training set.
-    > You can add training utterances to **non-connected** intents only.
-        
+    > You can add training utterances to **nonconnected** intents only.
+
     :::image type="content" source="../media/tag-utterances.png" alt-text="A screenshot of the page for tagging utterances in Language Studio." lightbox="../media/tag-utterances.png":::
-   
+
 5. Under **Distribution** you can view the distribution across training and testing sets. You can **view utterances per intent**:
 
-* Utterance per non-connected intent
+* Utterance per nonconnected intent
 * Utterances per connected intent
 
 ## Next Steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "発話追加手順の文言修正と構成の見直し"
}
```

### Explanation
このコードの差分では、`tag-utterances.md`というMarkdownファイルにおいて、発話を追加する手順に関していくつかの軽微な変更が行われています。以下は主な変更点です。

1. **見出しの簡略化**:
   - モードタイトルを「Add utterances in Language Studio」から「Add utterances」に変更し、内容の明確化と簡潔化が図られています。

2. **表現の改善**:
   - 一部の文末の表現が改善され、「but you need to make sure that your data follows」から「but you need to make sure that your data follows the accepted data format」のように、情報が明確に伝わるようになりました。このように、必要な情報が明示的に伝わるように文面が見直されています。

3. **手順の整頓**:
   - 発話を追加する手順について、特にステップ3の部分が整理され、手順が一貫して分かりやすく記述されています。また、`non-connected`から`nonconnected`への用語の統一も図られています。

4. **注意喚起の強化**:
   - 「Note」セクションの内容が強調され、ユーザーが重要な点を見逃すことないように工夫されています。

全体として、これらの変更により文書は一貫性が増し、発話を追加する際の手順がより明確に伝わる内容となっています。ユーザーが必要な情報を効率よく理解しやすくなることを目指した改善です。

## articles/ai-services/language-service/orchestration-workflow/how-to/train-model.md{#item-012314}

<details>
<summary>Diff</summary>
````diff
@@ -53,40 +53,16 @@ Orchestration workflow supports two methods for data splitting:
 
 ### Start training job
 
-#### [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Train model](../includes/language-studio/train-model.md)]
-
-#### [REST APIs](#tab/rest-api)
-
 [!INCLUDE [train model](../includes/rest-api/train-model.md)]
 
----
-
 ### Get training job status
 
-#### [Language Studio](#tab/language-studio)
-
-Select the training job ID from the list, a side pane appears where you can check the **Training progress**, **Job status**, and other details for this job.
-
-<!--:::image type="content" source="../../../media/train-pane.png" alt-text="A screenshot showing the training job details." lightbox="../../../media/train-pane.png":::-->
-
-
-#### [REST APIs](#tab/rest-api)
-
 Training could take sometime depending on the size of your training data and complexity of your schema. You can use the following request to keep polling the status of the training job until it successfully completes.
 
 [!INCLUDE [get training model status](../includes/rest-api/get-training-status.md)]
 
----
 ### Cancel training job
 
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Cancel training](../includes/language-studio/cancel-training.md)]
-
-# [REST APIs](#tab/rest-api)
-
 [!INCLUDE [Cancel training](../includes/rest-api/cancel-training.md)]
 
 ---
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "トレーニングモデル手順の大幅な削除"
}
```

### Explanation
このコードの差分では、`train-model.md`というMarkdownファイルにおいて、大幅な内容の削除が行われており、特にトレーニングモデルに関連する手順や情報が削除されています。以下は主な変更点です。

1. **手順の削除**:
   - トレーニングジョブの開始に関する手順が大部分削除され、「Language Studio」や「REST APIs」に関連する具体的な手順がなくなりました。これにより、読者はトレーニングを開始する方法に関する情報を得ることができなくなっています。

2. **進行状況の確認方法の削除**:
   - トレーニングジョブの進行状況やステータスを確認するための詳細な説明や手順も削除されています。これにより、トレーニングプロセスの監視に関する情報が失われています。

3. **ジョブのキャンセル方法の削除**:
   - トレーニングジョブをキャンセルするための手順や関連する情報も削除されており、ユーザーがトレーニングを中止する際のガイダンスが提供されなくなりました。

これらの変更により、`train-model.md`ファイルはトレーニングプロセスに関しての重要な情報を欠いた状態となっています。この更新は、ドキュメントの構造的な変化を示しており、ユーザーはモデルのトレーニングに取り組む際の手順について明確な指示を受けられなくなってしまいました。全体的に、この変更はユーザーが直面する情報の不足を引き起こすものであり、注意が必要です。

## articles/ai-services/language-service/orchestration-workflow/how-to/view-model-evaluation.md{#item-86aee9}

<details>
<summary>Diff</summary>
````diff
@@ -10,6 +10,7 @@ ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-custom-classification
 ---
+
 # View orchestration workflow model details
 
 After model training is completed, you can view your model details and see how well it performs against the test set. Observing how well your model performed is called evaluation. The test set consists of data that wasn't introduced to the model during the training process.
@@ -29,40 +30,17 @@ See the [project development lifecycle](../overview.md#project-development-lifec
 
 ## Model details
 
-### [Language studio](#tab/Language-studio)
-
-In the **view model details** page, you'll be able to see all your models, with their current training status, and the date they were last trained.
-
-[!INCLUDE [Model performance](../includes/language-studio/model-performance.md)]
-
-### [REST APIs](#tab/REST-APIs)
 
 [!INCLUDE [Evaluate model](../includes/rest-api/model-evaluation.md)]
 
----
-
 ## Load or export model data
 
-### [Language studio](#tab/Language-studio)
-
-[!INCLUDE [Load export model](../../conversational-language-understanding/includes/language-studio/load-export-model.md)]
-
-
-### [REST APIs](#tab/REST-APIs)
-
 [!INCLUDE [Load export model](../../conversational-language-understanding/includes/rest-api/load-export-model.md)]
 
 ---
 
 ## Delete model
 
-### [Language studio](#tab/Language-studio)
-
-[!INCLUDE [Delete model](../includes/language-studio/delete-model.md)]
-
-
-### [REST APIs](#tab/REST-APIs)
-
 [!INCLUDE [Delete model](../includes/rest-api/delete-model.md)]
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル評価ページの見出し追加と内容の削減"
}
```

### Explanation
このコードの差分では、`view-model-evaluation.md`というMarkdownファイルにおいて、モデル評価に関する情報が変更され、内容が一部削減されています。以下は主な変更点です。

1. **新しい見出しの追加**:
   - ファイルの冒頭に「View orchestration workflow model details」という新しい見出しが追加され、モデル詳細の閲覧に関する説明が前面に出されました。これにより、ユーザーがどのような情報を得られるかが明確になりました。

2. **詳細情報の削減**:
   - 元々存在していた「Language Studio」および「REST APIs」に関する詳細な説明が大幅に削除されています。具体的には、モデルの詳細、評価結果の確認方法、データの読み込みやエクスポート、モデルの削除に関する手順がすべて削除されています。

3. **評価の重要性の記載**:
   - モデル訓練が完了した後に、そのモデルがテストセットに対してどのようにパフォーマンスを発揮するかを確認することの重要性を示すための説明が残されています。この部分は、モデルの評価を行う意義を強調するものです。

全体として、変更された内容はモデルの評価ページをよりシンプルにし、見出しの明確化を図りますが、一方で利用者に必要な詳細な操作手順が削減されているため、その点が懸念されます。この更新により、ユーザーはモデル評価の基本概念は理解できるものの、具体的なステップや方法については別のリソースを参照する必要があるかもしれません。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/cancel-training.md{#item-6dd79a}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To cancel a training job from within [Language Studio](https://aka.ms/laguageStudio), go to the **Train model** page. Select the training job you want to cancel, and select **Cancel** from the top menu. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "トレーニングキャンセル手順の削除"
}
```

### Explanation
このコードの差分では、`cancel-training.md`というMarkdownファイルが削除され、トレーニングジョブをキャンセルする方法に関する情報が完全になくなっています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `cancel-training.md`ファイルが完全に削除され、これによってトレーニングジョブのキャンセルに関する手順がなくなりました。この手順は「Language Studio」での操作に関するものであり、ユーザーにとって重要な情報源でした。

2. **キャンセル手順の不在**:
   - 元のドキュメントでは、トレーニングジョブをキャンセルするための具体的な手順が含まれており、ユーザーは「Train model」ページに行き、キャンセルしたいジョブを選択してからキャンセルボタンをクリックするという流れが説明されていました。このプロセスが削除されたため、ユーザーはトレーニングを中止する方法についての具体的な案内を失っています。

この変更は、関連ドキュメントにおいて重要な情報が欠如することを意味し、ユーザーがトレーニングプロセスを管理する上でのサポートが著しく減少します。トレーニングをキャンセルする必要があるユーザーは、代替のリソースやサポートを探す必要が出てくるでしょう。全体として、この変更はキャンセル手順に関するリファレンスを大幅に欠如させるものであり、注意が必要です。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/create-project.md{#item-f34974}

<details>
<summary>Diff</summary>
````diff
@@ -1,22 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. In [Language Studio](https://aka.ms/languageStudio), find the section labeled **Understand questions and conversational language** and select **Orchestration Workflow**.  
-   
-   :::image type="content" source="../../media/select-orchestration.png" alt-text="A screenshot showing the location of the orchestration workflow section in Azure Language Studio landing page." lightbox="../../media/select-orchestration.png"::: 
-    
-
-2. This will bring you to the **Orchestration workflow project** page. Select **Create new project**. To create a project, you need to provide the following details:
-
-|Value  | Description  |
-|---------|---------|
-|Name     | A name for your project.        |
-|Description    | Optional project description.        |
-|Utterances primary language | The primary language of your project. Your training data should primarily be in this language.|
-
-Once you're done, select **Next** and review the details. Select **create project** to complete the process. You should now see the **Build Schema** screen in your project.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト作成手順の削除"
}
```

### Explanation
このコードの差分では、`create-project.md`というMarkdownファイルが削除され、プロジェクトを作成する方法に関する情報が完全に失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - フィアル`create-project.md`が完全に削除され、これは「Language Studio」の中で新しいプロジェクトを作成するための指導が失われたことを意味しています。このドキュメントは、プロジェクトを作成するための具体的な手順を含んでいました。

2. **プロジェクト作成手順の詳細**:
   - 元の内容では、ユーザーが「Language Studio」で「Orchestration Workflow」セクションを見つけ、新しいプロジェクトを作成するために必要なステップ（プロジェクト名、説明、主言語など）について具体的な指示が示されていました。この手順が削除されたことで、ユーザーはプロジェクトを作成する方法に関する具体的なガイダンスを失っています。

3. **ユーザーへの影響**:
   - プロジェクト作成に関する情報の消失は、新しいユーザー、またはプロジェクトを始めようとするユーザーにとって重大な影響を及ぼす可能性があります。これにより、ユーザーは独自に情報を探さなければならず、プロジェクト作成の効率が低下する恐れがあります。

全体として、この変更はプロジェクト作成に関する重要な手順を削除するものであり、特に初心者や必要なガイダンスを必要とするユーザーへの重大な障害となる可能性があります。情報があまりにも欠落するため、別のリソースを探す必要があり、ユーザー体験が著しく悪化します。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/delete-deployment.md{#item-f132cd}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To delete a deployment from within [Language Studio](https://aka.ms/laguageStudio), go to the **Deploy model** page. Select the deployment you want to delete, and select **Delete deployment** from the top menu. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デプロイメント削除手順の削除"
}
```

### Explanation
このコードの差分では、`delete-deployment.md`というMarkdownファイルが削除され、デプロイメントを削除する方法に関する情報がなくなっています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `delete-deployment.md`ファイルが完全に削除され、これによりユーザーは「Language Studio」におけるデプロイメントの削除手順についての情報を失いました。この手順は、ユーザーが特定のデプロイメントを選んで削除する方法を説明していました。

2. **削除手順の不在**:
   - 元のファイルには、ユーザーが「Deploy model」ページに移動し、削除したいデプロイメントを選択してから「Delete deployment」オプションを選ぶという具体的な手順が含まれていました。この手順が削除されたことで、ユーザーはデプロイメントを削除する方法を知ることができなくなります。

3. **ユーザーへの影響**:
   - デプロイメント削除に関する情報の消失は、デプロイメントを管理する際にユーザーにとって大きな障壁となる可能性があります。特に初心者やそれに関する知識が乏しいユーザーは、操作方法がわからなくなる可能性が高いです。

全体として、この変更はデプロイメントを削除するための重要な手順を省くものであり、ユーザーが必要なアクションを適切に実行するにあたっての重大な障害となります。これにより、ユーザー体験が悪化し、必要な情報を求めて他のリソースを探さざるを得なくなるでしょう。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/delete-model.md{#item-9ba075}

<details>
<summary>Diff</summary>
````diff
@@ -1,15 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To delete your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Model performance** from the left side menu.
-
-2. Select the **model name** you want to delete and select **Delete** from the top menu.
-
-3. In the window that appears, select **OK** to delete the model. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル削除手順の削除"
}
```

### Explanation
このコードの差分では、`delete-model.md`というMarkdownファイルが削除され、モデルを削除する方法に関する情報が失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `delete-model.md`ファイルが完全に削除され、これによってユーザーは「Language Studio」にてモデルを削除する手順に関する情報を失いました。このファイルには、モデル削除に必要な具体的なプロセスが記載されていました。

2. **削除手順の不在**:
   - 元の内容では、ユーザーが左側のメニューから「Model performance」を選択し、削除したいモデルを選んでから「Delete」オプションを選ぶという明確な手順が示されていました。これらの手順が削除されたことで、ユーザーはモデルを削除する方法を知ることができなくなります。

3. **ユーザーへの影響**:
   - モデル削除に関する情報の消失は、特に初心者やその手順への理解が乏しいユーザーにとっての大きな障害となります。これにより、必要な操作ができず、ユーザーは不便を感じることが予想されます。

全体として、この変更はモデルを削除するための重要な手順を削除するものであり、ユーザーが必要な操作を行ううえで重大な障害となります。これによってユーザー体験が悪化し、新たに他のリソースを探す必要が生じる可能性があります。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/delete-project.md{#item-3b70d0}

<details>
<summary>Diff</summary>
````diff
@@ -1,9 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
- When you don't need your project anymore, you can delete your project using Language Studio. Select **Projects** from the left pane, select the project you want to delete, and then select **Delete** from the top menu.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト削除手順の削除"
}
```

### Explanation
このコードの差分では、`delete-project.md`というMarkdownファイルが削除され、プロジェクトを削除する方法に関する情報が失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `delete-project.md`ファイルが完全に削除され、これによりユーザーは「Language Studio」でプロジェクトを削除する手順についての情報を失いました。元のファイルには、プロジェクト削除に必要な具体的な手順が詳細に記載されていました。

2. **削除手順の不在**:
   - 元の内容では、プロジェクトを削除するために、左側のパネルから「Projects」を選択し、削除したいプロジェクトを選んでから「Delete」オプションを選ぶという明確な手順が説明されていました。これらの手順が削除されたため、ユーザーはプロジェクトを効果的に削除する方法を知らなくなります。

3. **ユーザーへの影響**:
   - プロジェクト削除に関する情報の消失は、特にその操作に不安を感じる初心者にとって大きな障壁となる可能性があります。ユーザーは必要なアクションを実行できず、困難を感じることが予想されます。

全体として、この変更はプロジェクトを削除するための重要な手順を削除するものであり、ユーザーが必要な操作を達成する上での重大な障がいとなります。これによりユーザー体験が悪化し、他のリソースを探すことを余儀なくされることが考えられます。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/deploy-model.md{#item-8ac056}

<details>
<summary>Diff</summary>
````diff
@@ -1,32 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To deploy your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Deploying a model** from the left side menu.
-
-2. Select **Add deployment** to start a new deployment job.
-
-    :::image type="content" source="../../media/add-deployment-model.png" alt-text="A screenshot showing the model deployment button in Language Studio." lightbox="../../media/add-deployment-model.png":::
-
-3. Select **Create new deployment** to create a new deployment and assign a trained model from the dropdown below. You can also **Overwrite an existing deployment** by selecting this option and select the trained model you want to assign to it from the dropdown below.
-
-    > [!NOTE]
-    > Overwriting an existing deployment doesn't require changes to your [prediction API](https://aka.ms/clu-apis) call, but the results you get will be based on the newly assigned model.
-    
-    :::image type="content" source="../../media/create-deployment-job.png" alt-text="A screenshot showing the screen for adding a new deployment in Language Studio." lightbox="../../media/create-deployment-job.png":::
-
-4. If you're connecting one or more [LUIS](https://aka.ms/luis-docs) applications or [conversational language understanding](https://aka.ms/clu-docs) projects, you have to specify the deployment name.
-    
-    * No configurations are required for custom question answering or unlinked intents.
-    
-    * LUIS projects **must be published** to the slot configured during the Orchestration deployment, and custom question answering KBs must also be published to their Production slots.
-
-5. Select **Deploy** to submit your deployment job
-
-6. After deployment is successful, an expiration date will appear next to it. [Deployment expiration](../../../concepts/model-lifecycle.md#expiration-timeline) is when your deployed model will be unavailable to be used for prediction, which typically happens **twelve** months after a training configuration expires.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル展開手順の削除"
}
```

### Explanation
このコードの差分では、`deploy-model.md`というMarkdownファイルが削除され、モデルを展開する方法に関する情報が失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `deploy-model.md`ファイルが完全に削除され、ユーザーは「Language Studio」内でモデルを展開するための手順に関する情報を失いました。このファイルには、モデルを正しく展開するために必要な具体的な手順が詳述されていました。

2. **展開手順の不在**:
   - 元の内容では、新しい展開ジョブを開始するために「Deploying a model」を選択し、必要に応じて新しい展開を作成する方法や既存の展開を上書きする方法などが説明されていました。これらの手順が削除されたため、ユーザーはモデルを展開する方法についての明確なガイダンスを欠くことになります。

3. **ユーザーへの影響**:
   - モデル展開に関する情報の消失は、特にそのプロセスに不安を感じる初心者や、手順に従って作業を行う必要があるユーザーにとって大きな障害となるでしょう。これにより、ユーザーはモデルを正しく展開することができず、業務に支障をきたす恐れがあります。

全体として、この変更はモデルを展開するための重要な手順を削除するものであり、ユーザーが必要な操作を達成するための重大な障がいとなります。結果として、ユーザー体験が悪化し、新たに情報を探し直さなければならない状況が生じる可能性があります。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/get-prediction-url.md{#item-7b738d}

<details>
<summary>Diff</summary>
````diff
@@ -1,16 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
-ms.custom: language-service-orchestration 
----
-1. After the deployment job is completed successfully, select the deployment you want to use and from the top menu select **Get prediction URL**.
-
-    :::image type="content" source="../../media/get-prediction-url.png" alt-text="Screenshot showing how to get a prediction U R L." lightbox="../../media/get-prediction-url.png":::
-
-2. In the window that appears, copy the sample request URL and body into your command line. Replace `<YOUR_QUERY_HERE>` with the actual text you want to send to extract intents and entities from.
-
-4. Submit the `POST` cURL request in your terminal or command prompt. You receive a 202 response with the API results if the request was successful.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "予測URL取得手順の削除"
}
```

### Explanation
このコードの差分では、`get-prediction-url.md`というMarkdownファイルが削除され、予測URLを取得するための手順に関する情報が失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `get-prediction-url.md`ファイルが完全に削除され、ユーザーはデプロイメント後に予測URLを取得する方法についての情報を失いました。このファイルには、予測APIの使用に必要な具体的な手順が詳述されていました。

2. **予測URL取得手順の不在**:
   - 元の内容では、デプロイメントジョブが正常に完了した後、予測URLを取得するための具体的な手順が詳細に説明されていました。ユーザーはメニューから「Get prediction URL」を選択し、表示されるウィンドウからサンプルリクエストURLとボディをコマンドラインにコピーする手順を踏む必要がありました。この手順が削除されたため、ユーザーは予測サービスを利用するための方法を把握できなくなります。

3. **ユーザーへの影響**:
   - 予測URL取得に関する情報の消失は、特にそのプロセスに不安を感じる初心者や、手順に従って作業を行う必要があるユーザーにとって大きな障害となるでしょう。これにより、正しいAPIリクエストを送信できず、予測機能を活用できなくなる可能性があります。

全体として、この変更は予測URLを取得するための重要な手順を削除するものであり、ユーザーが必要な操作を達成するための重大な障がいとなります。結果として、ユーザー体験が悪化し、新たに情報を探し直さなければならない状況が生じる可能性があります。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/model-performance.md{#item-c090d2}

<details>
<summary>Diff</summary>
````diff
@@ -1,24 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Go to your project page in [Language Studio](https://aka.ms/languageStudio).
-
-2. Select **Model performance** from the menu on the left side of the screen.
-
-3. On this page, you can only view the successfully trained models, F1 score for each model and [model expiration date](../../../concepts/model-lifecycle.md#expiration-timeline).
-You can select the model name for more details about its performance.
-
-4. You can find the *model-level evaluation metrics* under **Overview**, and the *intent-level* evaluation metrics. See [Evaluation metrics](../../concepts/evaluation-metrics.md) for more information.
-
-    :::image type="content" source="../../media/model-details.png" alt-text="A screenshot of the model performance metrics in Language Studio" lightbox="../../media/model-details.png":::
-    
-5. The [confusion matrix](../../concepts/evaluation-metrics.md#confusion-matrix) for the model is located under **Test set confusion matrix**. You can see the confusion matrix for intents.
-
-     
-    > [!NOTE] 
-    > If you don't see any of the intents you have in your model displayed here, it is because they weren't in any of the utterances that were used for the test set.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルパフォーマンスに関する情報の削除"
}
```

### Explanation
このコードの差分では、`model-performance.md`というMarkdownファイルが削除され、モデルのパフォーマンスに関する情報が失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `model-performance.md`ファイルが完全に削除され、ユーザーは「Language Studio」におけるモデルパフォーマンスの分析方法に関する情報を失いました。このファイルには、モデルのパフォーマンス指標や評価方法に関する具体的な手順が詳述されていました。

2. **モデルパフォーマンスの確認方法の不在**:
   - 元の内容では、プロジェクトページにアクセスし、成功裏に訓練されたモデルのF1スコアやモデルの有効期限の確認方法、及び詳細なパフォーマンスに関する情報へのアクセス手順が示されていました。これらの手順が削除されたため、ユーザーはどのようにモデルのパフォーマンスを確認すればよいか分からなくなります。

3. **ユーザーへの影響**:
   - モデルパフォーマンスに関する情報の消失は、特にモデルの評価を行いたいユーザーや、モデルの信頼性を測るためのデータが必要な開発者にとって大きな妨げとなります。これにより、正しい判断を下すための情報が得られず、プロジェクトの進行に支障をきたす可能性があります。

全体として、この変更はモデルパフォーマンスを評価するための重要な情報を削除するものであり、ユーザーが必要な操作を達成するための重大な障がいとなります。結果として、ユーザー体験が悪化し、パフォーマンスを把握するための新たな情報源を探し直さなければならない状況が生じる可能性があります。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/project-details.md{#item-74d667}

<details>
<summary>Diff</summary>
````diff
@@ -1,18 +0,0 @@
----
-titleSuffix: Foundry Tools
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Go to your project settings page in [Language Studio](https://aka.ms/languageStudio).
-
-2. You can see project details.
-
-3. On this page, you can update project description.
-
-4. You can also retrieve your resource primary key from this page.
-
-    :::image type="content" source="../../media/project-settings.png" alt-text="A screenshot of the project settings page." lightbox="../../media/project-settings.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト詳細に関する情報の削除"
}
```

### Explanation
このコードの差分では、`project-details.md`というMarkdownファイルが削除され、Language Studioにおけるプロジェクトの詳細に関する情報が失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `project-details.md`ファイルが完全に削除され、ユーザーはプロジェクト設定のページにアクセスしてプロジェクトの詳細を確認する方法についての情報を失いました。このファイルには、プロジェクトの設定を確認および更新するための具体的な手順が詳述されていました。

2. **プロジェクト設定の確認方法の不在**:
   - 元の内容では、ユーザーがLanguage Studio内でプロジェクト設定ページにアクセスし、プロジェクトの詳細や説明を更新する方法、さらにはリソースのプライマリキーを取得する方法が記載されていました。これらの手順が削除されたため、ユーザーはプロジェクト管理のための重要な情報にアクセスできなくなります。

3. **ユーザーへの影響**:
   - プロジェクト詳細に関する情報の消失は、特にプロジェクト設定やリソース管理を行いたいユーザーにとって、重要な妨げとなります。これにより、プロジェクトの適切な管理が難しくなり、ユーザーは必要な操作を実行するための情報を再度探し直さなければならなくなる可能性があります。

全体として、この変更はプロジェクト管理における重要な機能を削除するものであり、ユーザーが必要な操作を達成するための重大な障がいとなります。結果として、ユーザー体験が悪化し、プロジェクトの運営に支障をきたす可能性が高まります。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/sign-in-studio.md{#item-f1b35b}

<details>
<summary>Diff</summary>
````diff
@@ -1,21 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-1. Go to the [Language Studio](https://aka.ms/languageStudio) and sign in with your Azure account. 
-
-2. In the **Choose a language resource** window that appears, find your Azure subscription, and choose your Language resource. If you don't have a resource, you can create a new one.
-
-    |Instance detail  |Required value  |
-    |---------|---------|
-    |Azure subscription | Your Azure subscription.           |
-    |Azure resource group | Your Azure resource group. |
-    |Azure resource name |  Your Azure resource name.        |
-    |Location | A [valid location](../../service-limits.md#regional-availability) for your Azure resource. For example, "West US 2".       |
-    |Pricing tier     | A supported [pricing tier](../../service-limits.md#language-resource-limits) for your Azure resource. You can use the Free (F0) tier to try the service.       |
-    
-    :::image type="content" source="../../media/quickstart-language-resource.png" alt-text="A screenshot showing the resource selection screen in Language Studio." lightbox="../../media/quickstart-language-resource.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioへのサインイン手順の削除"
}
```

### Explanation
このコードの差分では、`sign-in-studio.md`というMarkdownファイルが削除され、Language Studioへのサインイン手順に関する情報が失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `sign-in-studio.md`ファイルが完全に削除され、ユーザーはAzureアカウントを使用してLanguage Studioにサインインする方法に関する具体的な手順を失いました。このファイルには、サインインプロセスや必要なリソースの選択についての詳細が含まれていました。

2. **サインイン手順の不在**:
   - 元の内容では、ユーザーがLanguage Studioにアクセスし、自分のAzureサブスクリプションやリソースを選択する手順が明示されていました。これには、必要な値（サブスクリプション、リソースグループ、リソース名、地域、プライシングプラン）を指定するための情報も含まれていました。これらの手順が削除されたため、ユーザーはサインインして使用するための重要な情報にアクセスできなくなります。

3. **ユーザーへの影響**:
   - サインイン手順に関する情報の消失は、Language Studioを利用したいユーザーにとって大きな支障となります。特に新規ユーザーやリソースを作成する必要があるユーザーは、適切な手順がないためにサインインできず、サービスを開始できない可能性があります。

全体として、この変更はLanguage Studioの利用開始に向けた重要な手順を削除するものであり、ユーザーが必要な操作を達成するための障がいとなります。結果として、ユーザー体験が悪化し、Language Studioの利用に対する元々の障壁がさらに高まる可能性があります。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/swap-deployment.md{#item-6eea90}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To swap deployments from within [Language Studio](https://aka.ms/laguageStudio)
-
-1. In the **Deploy model** page, select the two deployments you want to swap and select **Swap deployments** from the top menu. 
-
-2. From the window that appears, select the names of the deployments you want to swap.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デプロイメントのスワップ手順の削除"
}
```

### Explanation
このコードの差分では、`swap-deployment.md`というMarkdownファイルが削除され、Language Studio内でのデプロイメントのスワップ手順に関する情報が失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `swap-deployment.md`ファイルが完全に削除され、ユーザーはLanguage Studioを使用してデプロイメントをスワップする方法に関する具体的な手順にアクセスできなくなりました。この元のドキュメントには、デプロイするモデルを選択し、それをスワップするための手続きが明示されていました。

2. **デプロイメントスワップ手順の不在**:
   - 元の情報では、「デプロイモデル」ページ内で2つのデプロイメントを選択し、メニューから「デプロイメントをスワップ」を選ぶ方法が詳しく説明されていました。この手順が削除されたことにより、ユーザーはデプロイメントをスワップするための重要な指示を失ってしまいます。

3. **ユーザーへの影響**:
   - デプロイメントスワップ手順の削除は、Language Studioを利用しているユーザーにとって大きな不便をもたらします。特に、デプロイメントの管理や運用を行おうとするユーザーにとって、スワップ操作が必要な際にその手順が分からず、正確な操作が行えない可能性があります。

全体として、この変更はLanguage Studioの機能の一部を削除するものであり、ユーザーが必要なデプロイメントの操作を達成するための障害となります。これにより、ユーザーエクスペリエンスが著しく悪化し、デプロイメント管理において支障をきたす可能性が高まります。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/test-model.md{#item-4322d9}

<details>
<summary>Diff</summary>
````diff
@@ -1,23 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To test your model from Language Studio
-
-1. Select **Testing deployments** from the left side menu.
-
-3. Select the model you want to test. You can only test models that are assigned to deployments.
-
-4. From deployment name dropdown, select your deployment name.
-
-5. In the text box, enter an utterance to test.
-
-6. From the top menu, select **Run the test**.
-
-7. After you run the test, you should see the response of the model in the result. You can view the results in entities cards view, or view it in JSON format.
-
-    :::image type="content" source="../../media/test-model.png" alt-text="A screenshot showing how to test a model in Language Studio." lightbox="../../media/test-model.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルテスト手順の削除"
}
```

### Explanation
このコードの差分では、`test-model.md`というMarkdownファイルが削除され、Language Studioでモデルをテストするための手順に関する情報が失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `test-model.md`ファイルが完全に削除され、ユーザーはLanguage Studio内でモデルをテストする方法に関する具体的な手順を参照できなくなりました。このファイルには、テストを実行するための各ステップが記載されていました。

2. **テスト手順の不在**:
   - 元の内容では、「テストデプロイメント」を選択し、テストしたいモデルを選び、デプロイメント名をドロップダウンから選択する方法、テストする発話を入力する方法、そしてテストを実行する方法が含まれていました。これらの手順が削除されたため、ユーザーはモデルをテストするための重要な指示を失ってしまいます。

3. **ユーザーへの影響**:
   - モデルテスト手順の削除は、Language Studioを利用しているユーザーにとって大きな不便をもたらします。特に、モデルの性能を確認したいユーザーにとって、これらの指示がなくなることで具体的な操作ができず、結果としてモデルの評価や調整が行えなくなる可能性があります。

全体として、この変更はLanguage Studioの機能の一部を削除するものであり、ユーザーがモデルを正確にテストするための手段を奪う結果となります。このことはユーザーエクスペリエンスを著しく低下させ、モデル開発や運用における支障をきたす可能性があります。

## articles/ai-services/language-service/orchestration-workflow/includes/language-studio/train-model.md{#item-d7c75c}

<details>
<summary>Diff</summary>
````diff
@@ -1,36 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-To start training your model from within the [Language Studio](https://aka.ms/languageStudio):
-
-1. Select **Training jobs** from the left side menu.
-
-2. Select **Start a training job** from the top menu.
-
-3. Select **Train a new model** and type in the model name in the text box. You can also **overwrite an existing model** by selecting this option and choosing the model you want to overwrite from the dropdown menu. Overwriting a trained model is irreversible, but it won't affect your deployed models until you deploy the new model.
-
-    If you have enabled [your project to manually split your data](../../how-to/tag-utterances.md) when tagging your utterances, you can see two data splitting options:
-    
-    * **Automatically splitting the testing set from training data**: Your tagged utterances will be randomly split between the training and testing sets, according to the percentages you choose. The default percentage split is 80% for training and 20% for testing. To change these values, choose which set you want to change and type in the new value.
-        
-    > [!NOTE]
-    > If you choose the **Automatically splitting the testing set from training data** option, only the utterances in your training set will be split according to the percentages provided.
-        
-    * **Use a manual split of training and testing data**: Assign each utterance to either the training or testing set during the [tagging](../../how-to/tag-utterances.md) step of the project.
-        
-    > [!NOTE]
-    > **Use a manual split of training and testing data** option will only be enabled if you add utterances to the testing set in the tag data page. Otherwise, it will be disabled.
-        
-    :::image type="content" source="../../media/train-model.png" alt-text="A screenshot showing the train model page for conversational language understanding projects." lightbox="../../media/train-model.png":::
-
-5. Select the **Train** button.
-
-> [!NOTE]
-> * Only successfully completed training jobs will generate models.
-> * Training can take some time between a couple of minutes and couple of hours based on the size of your tagged data.
-> * You can only have one training job running at a time. You cannot start other training job wihtin the same project until the running job is completed.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルトレーニング手順の削除"
}
```

### Explanation
このコードの差分では、`train-model.md`というMarkdownファイルが削除され、Language Studioでモデルをトレーニングするための手順に関する情報が失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `train-model.md`ファイルが完全に削除され、ユーザーはLanguage Studio内でモデルのトレーニングを開始するための具体的な手順にアクセスできなくなりました。このファイルには、トレーニングジョブの開始方法やモデル名の設定方法などが記載されていました。

2. **トレーニング手順の不在**:
   - 元の内容では、トレーニングジョブを開始するための流れが詳述されており、特に新しいモデルのトレーニングや既存モデルの上書き方法、データの自動分割や手動分割の選択についての情報が含まれていました。これにより、ユーザーはモデルを効果的にトレーニングするための理解を得ていましたが、これらが削除されたため、ユーザーは手順を知ることができません。

3. **ユーザーへの影響**:
   - モデルトレーニング手順の削除は、Language Studioを利用しているユーザーにとって深刻な不便をもたらします。特に、新しいモデルをトレーニングしたり、既存のモデルを更新したりしたいユーザーにとって、必要な情報がなくなることでトレーニング作業ができなくなります。また、トレーニングの進行状況や管理に関する注意点も失われるため、ユーザーは不明確な状況に直面することになります。

全体として、この変更はLanguage Studioの機能の一部を削除するものであり、ユーザーのモデルトレーニングに関する能力を著しく制限します。これにより、ユーザーエクスペリエンスが低下し、AIモデルの開発や管理における支障が生じる可能性があります。

## articles/ai-services/language-service/orchestration-workflow/includes/quickstarts/language-studio.md{#item-b78cb6}

<details>
<summary>Diff</summary>
````diff
@@ -1,80 +0,0 @@
----
-author: laujan
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 11/18/2025
-ms.author: lajanuar
----
-## Prerequisites
-
-* Azure subscription - [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* A [conversational language understanding](../../../conversational-language-understanding/quickstart.md) project.
-
-
-
-## Sign in to Language Studio
-
-[!INCLUDE [Sign in to Language studio](../language-studio/sign-in-studio.md)]
-
-
-
-## Create an orchestration workflow project
-
-Once you have a Language resource created, create an orchestration workflow project. A project is a work area for building your custom ML models based on your data. Your project can only be accessed by you and others who have access to Azure Language resource being used.
-
-For this quickstart, complete the [conversational language understanding](../../../conversational-language-understanding/quickstart.md) quickstart to create a conversational language understanding project used later.
-
-[!INCLUDE [Sign in to Language studio](../language-studio/create-project.md)]
-
-
-
-## Build schema
-
-After you complete the conversational language understanding quickstart and create an orchestration project, the next step is to add intents.
-
-To connect to the previously created conversational language understanding project:
-
-* In the **build schema** page in your orchestration project, select **Add**, to add an intent.
-* In the window that appears, give your intent a name.
-* Select **Yes, I want to connect it to an existing project**.
-* From the connected services dropdown, select **Conversational Language Understanding**.
-* From the project name dropdown, select your conversational language understanding project.
-* Select **Add intent** to create your intent.
-
-
-
-
-## Train your model
- 
-To train a model, you need to start a training job. The output of a successful training job is your trained model.
-
-[!INCLUDE [Train model](../language-studio/train-model.md)]
-
-
-
-
-## Deploy your model
-
-Generally after training a model you would review its evaluation details. In this quickstart, you will just deploy your model, and make it available for you to try in Language Studio, or you can call the [prediction API](https://aka.ms/clu-apis).
-
-[!INCLUDE [Deploy model](../language-studio/deploy-model.md)]
-
-
-
-
-
-## Test model
-
-After your model is deployed, you can start using it to make predictions through [Prediction API](https://aka.ms/clu-apis). For this quickstart, you will use the [Language Studio](https://aka.ms/LanguageStudio) to submit an utterance, get predictions and visualize the results.
-
-
-[!INCLUDE [Test model](../language-studio/test-model.md)]
-
-
-
-## Clean up resources
-
-[!INCLUDE [Delete project using Language studio](../language-studio/delete-project.md)]
-
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studio クイックスタートガイドの削除"
}
```

### Explanation
このコードの差分では、`language-studio.md`というMarkdownファイルが削除され、Language Studioでのクイックスタートに関する手順が完全に失われています。以下は主な変更点です。

1. **ドキュメントの削除**:
   - `language-studio.md`ファイルが完全に削除され、このファイルに含まれていた言語スタジオを利用したオーケストレーションワークフローの作成手順が参照できなくなります。このファイルには、プロジェクト作成、スキーマ構築、モデルのトレーニング、デプロイ、モデルのテストなど、多くの基本的なガイドラインが含まれていました。

2. **クイックスタート内容の不在**:
   - 元の内容には、Azureサブスクリプションの作成方法や、会話型言語理解プロジェクトのクイックスタート、トレーニングジョブの開始、モデルのデプロイ手順、結果のテスト方法などが記載されていました。これにより、ユーザーはLanguage Studioを使って効果的にモデルを構築・運用する手助けを得ることができたが、これが削除されたため、ユーザーは基礎的なステップを見失うことになります。

3. **ユーザーへの影響**:
   - この変更により、Language Studioを利用するユーザーは、必要な情報を欠くことになり、プロジェクトの初期設定やモデルの構築が困難になります。特に、新規ユーザーやこれから学ぶユーザーにとっては、具体的な手順が不明なまま進めざるを得なくなり、結果としてモデル開発の障害となる可能性があります。

全体として、この変更はLanguage Studioの機能の一部を削除するものであり、ユーザーの新しいプロジェクトやモデルの構築に対する能力を大きく制限することになります。このことは、学習や実践の機会を損ない、AIモデルの開発効率を低下させる結果に繋がるでしょう。

## articles/ai-services/language-service/orchestration-workflow/language-support.md{#item-3e4a3b}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about the languages supported by orchestration workflow.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: concept-article
 ms.date: 11/18/2025
 ms.custom: references_regions, language-service-custom-ner
 ms.author: lajanuar
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピック分類の更新"
}
```

### Explanation
このコードの差分では、`language-support.md`というMarkdownファイルが修正され、トピックの分類が変更されました。以下は主な変更点です。

1. **トピックの分類の変更**:
   - `ms.topic`の値が`conceptual`から`concept-article`に変更されました。この変更は、ドキュメントの内容や目的に対する分類をより明確にするもので、ユーザーが関連情報を見つけやすくなることを意図しています。

2. **影響の範囲**:
   - この修正は、主にドキュメントの分類に関するものであり、内容自体には大きな変更はありません。トピックの指定を改善することで、Azure AI サービスやオーケストレーションワークフローを利用する者に対し、文書がどのような観点からのものであるかをより良く理解してもらうことが期待されます。

全体として、これらの変更は、ドキュメントの整理やナビゲーションの向上に寄与し、利用者にとっての情報アクセスの質を向上させることを目的としています。

## articles/ai-services/language-service/orchestration-workflow/overview.md{#item-53d49f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 11/18/2025
+ms.date: 12/17/2025
 ms.author: lajanuar
 ms.custom: language-service-orchestration
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
このコードの差分では、`overview.md`というMarkdownファイルが修正され、更新された日付が記載されています。以下は主な変更点です。

1. **日付の更新**:
   - `ms.date`の値が`11/18/2025`から`12/17/2025`に変更されました。この変更はドキュメントの最終更新日を更新するものであり、最新の情報が反映されていることを示しています。

2. **影響の範囲**:
   - 日付の変更は主に文書の管理やバージョン管理に関わるものであり、実際のコンテンツや他の情報に対する修正はありません。そのため、ユーザーに直接的な影響は少ないですが、最新の更新日を示すことで、文書が継続的に管理されていることを示す重要な要素です。

この変更は、各ドキュメントがどれだけ新しい内容を持っているかを示すためのものであり、特にユーザーが最新の情報を入手したい場合において、その重要性が際立ちます。

## articles/ai-services/language-service/orchestration-workflow/quickstart.md{#item-bee292}

<details>
<summary>Diff</summary>
````diff
@@ -9,24 +9,13 @@ ms.topic: quickstart
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-clu, mode-other
-zone_pivot_groups: usage-custom-language-features
 ---
 # Quickstart: Orchestration workflow
 
-Use this article to get started with Orchestration workflow projects using Language Studio and the REST API. Follow these steps to try out an example.
-
-::: zone pivot="language-studio"
-
-[!INCLUDE [Language Studio quickstart](includes/quickstarts/language-studio.md)]
-
-::: zone-end
-
-::: zone pivot="rest-api"
+Use this article to get started with Orchestration workflow projects using the REST API. Follow these steps to try out an example.
 
 [!INCLUDE [REST API quickstart](includes/quickstarts/rest-api.md)]
 
-::: zone-end
-
 ## Next steps
 
 * [Learn about orchestration workflows](overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドの内容修正"
}
```

### Explanation
このコードの差分では、`quickstart.md`というMarkdownファイルが修正され、主に内容の整理と簡潔化が行われました。以下は主な変更点です。

1. **テキストの修正と簡潔化**:
   - 初めの説明文が変更され、Language Studioに関する部分が削除されて、REST APIに焦点を当てるようになりました。この変更により、より明確にREST APIに基づいたクイックスタートガイドの目的を示す内容になっています。

2. **ゾーンの構造の削除**:
   - Language Studioに関連するゾーン構造が削除され、REST APIに関連する部分のみが残されています。この構造の変更は、クイックスタートを利用するユーザーが、必要な情報に素早くアクセスできるようにすることを意図しています。

3. **次のステップのセクション**:
   - 次のステップのリンクが変更され、オーケストレーションワークフローに関する情報がある他の文書への導線が示されていますが、具体的な内容は残っています。

この変更は、ユーザーがクイックスタートを通じてREST APIの利用を迅速に理解しやすくするためのものであり、情報の精度と明確性を向上させることを目指しています。

## articles/ai-services/language-service/orchestration-workflow/service-limits.md{#item-144728}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn about the data, region, and throughput limits for Orchestrati
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
-ms.topic: conceptual
+ms.topic: limits-and-quotas
 ms.date: 11/18/2025
 ms.author: lajanuar
 ms.custom: language-service-clu, mentions_regions
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "トピックの分類変更"
}
```

### Explanation
このコードの差分では、`service-limits.md`というMarkdownファイルが修正され、トピックの分類が変更されました。主な変更点は次の通りです。

1. **トピックの分類の変更**:
   - `ms.topic`の値が`conceptual`から`limits-and-quotas`に変更されました。この変更により、文書がオーケストレーションワークフローに関連するサービスの制限や割り当てに特化していることが明示され、内容に対する正確な理解が得やすくなります。

2. **文書の目的の明確化**:
   - 新しいトピック分類により、ユーザーがこの文書を検討したときに、その内容がどのような情報を提供するかがより分かりやすくなり、データの制限、地域、スループット制限などの情報を探しているユーザーに対して適切なリソースであることが示されます。

この変更は、文書の利用性を向上させ、関連する情報を迅速に見つける手助けをすることを目的としています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -98,9 +98,6 @@ items:
         - name: Back up and recover your models
           href: conversational-language-understanding/how-to/fail-over.md
           displayName: disaster recovery, failover, clu
-        - name: Migrate from LUIS
-          href: conversational-language-understanding/how-to/migrate-from-luis.md
-          displayName: language understanding, luis to clu
     - name: Concepts
       items:
         - name: Multi-turn conversations 🆕
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ナビゲーション項目の削除"
}
```

### Explanation
このコードの差分では、`toc.yml`という構成ファイルが修正され、ナビゲーション項目が削除されました。主な変更点は次の通りです。

1. **項目の削除**:
   - `Migrate from LUIS`というナビゲーション項目が削除されました。この項目は、LUISからCLUに移行する方法に関する情報を提供していましたが、現在はリストから外されています。

2. **ナビゲーションの簡素化**:
   - この変更により、ナビゲーションが簡素化され、ユーザーが探索可能な情報が凝縮されました。これにより、ユーザーは重要なトピックにより簡単にアクセスできるようになります。

この更新は、ドキュメントのナビゲーションの整理を目指しており、情報の見つけやすさを向上させることを目的としています。

## articles/ai-services/language-service/whats-new.md{#item-69b272}

<details>
<summary>Diff</summary>
````diff
@@ -34,7 +34,7 @@ Azure Language in Foundry Tools is updated on an ongoing basis. Bookmark this pa
 * [Conversational Language Understanding multi-turn conversations](conversational-language-understanding/concepts/multi-turn-conversations.md). Enable natural, context-aware dialogues through entity slot filling → Microsoft Foundry (new).
 * [Language detection](conversational-language-understanding/concepts/multiple-languages.md). Automatically detect the language of user utterances in conversational applications → Microsoft Foundry (new).
  * [PII detection for text](personally-identifiable-information/how-to/redact-text-pii.md). Detect and redact personally identifiable information in text documents → Microsoft Foundry (new).
-* [Custom Named Entity Recognition](custom-named-entity-recognition/quickstart.md). Test, train, and deploy custom NER models directly in the Foundry playground → Microsoft Foundry (classic).
+* [Custom Named Entity Recognition](custom-named-entity-recognition/quickstart.md). You can test, train, and deploy custom NER models directly in the Foundry playground → Microsoft Foundry (classic).
 * [PII detection for conversations](personally-identifiable-information/how-to/redact-conversation-pii.md). Identify and redact personally identifiable information in conversations → Microsoft Foundry (classic).
 
 **Text PII detection enhancements (2025-11-15-preview API)**. The preview API introduces several new feature parameters for [PII detection](personally-identifiable-information/overview.md):
@@ -431,7 +431,7 @@ Azure Language in Foundry Tools is updated on an ongoing basis. Bookmark this pa
     ```
 
 ## June 2022
-* v1.0 client libraries for [conversational language understanding](./conversational-language-understanding/how-to/call-api.md?tabs=azure-sdk#send-a-conversational-language-understanding-request) and [orchestration workflow](./orchestration-workflow/how-to/call-api.md?tabs=azure-sdk#send-an-orchestration-workflow-request) are Generally Available for the following languages:
+* v1.0 client libraries for [conversational language understanding](./conversational-language-understanding/how-to/call-api.md#send-a-conversational-language-understanding-request) and [orchestration workflow](orchestration-workflow/how-to/call-api.md) are Generally Available for the following languages:
     * [C#](https://github.com/Azure/azure-sdk-for-net/tree/Azure.AI.Language.Conversations_1.0.0/sdk/cognitivelanguage/Azure.AI.Language.Conversations)
     * [Python](https://github.com/Azure/azure-sdk-for-python/tree/azure-ai-language-conversations_1.0.0/sdk/cognitivelanguage/azure-ai-language-conversations)
 * v1.1.0b1 client library for [conversation summarization](summarization/quickstart.md?tabs=conversation-summarization&pivots=programming-language-python) is available as a preview for:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキストとリンクの修正"
}
```

### Explanation
このコードの差分では、`whats-new.md`というドキュメントが修正され、いくつかの内容が更新されました。主な変更点は次の通りです。

1. **文言の調整**:
   - `Custom Named Entity Recognition`の説明部分が若干修正され、「You can」というフレーズが追加されました。これにより、ユーザーがこの機能を使用することが明確に伝わります。

2. **リンクの変更**:
   - `conversational-language-understanding`および`orchestration workflow`に関するリンク部分が、URLの構成が変更されており、一部修正が加えられました。これにより、正しいドキュメントへのリンクが確保され、ユーザーが必要な情報にスムーズにアクセスできるようになります。

この更新は、情報の明瞭さを向上させることを目的としており、ユーザーが提供される機能や利用可能なリソースを理解しやすくするための調整です。


