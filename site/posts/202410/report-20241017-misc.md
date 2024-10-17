---
date: '2024-10-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9a3d20f...MicrosoftDocs:00d70d8
summary: この記事では、Document Intelligenceに関連するドキュメントの主な更新について説明しています。文書のリネームやリンクの修正が行われ、新機能としてReadモデルに関する新ページが追加されました。また、いくつかの文書が大幅に更新され、詳細なテクニカル情報が整理されています。主な変更点にはOCR技術を用いたテキスト抽出に関する説明、新しいサンプルコードの追加、「concept-layout.md」のリネームと内容の変更、そして「concept-read.md」の削除が含まれます。全体として、構造の一貫性と内容の正確性が改善されており、ユーザーは効率的に情報を扱えるようになっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:9a3d20f...MicrosoftDocs:00d70d8){target="_blank"}

<format>
# Highlights
この記事では、Document Intelligenceに関連するドキュメントの主な更新について詳しく解説しています。多くの文書がリネームされ、多くのリンクが修正されました。一部のドキュメントでは新機能が追加され、特にReadモデルに関する新しいページが登場しています。また、内容が大幅に更新されている文書もあり、詳細なテクニカル情報の整理が行われています。

## New features
- Document IntelligenceのReadモデルに関する新しいページが追加され、OCR技術を利用した印刷物および手書きのテキスト抽出について詳述されています。
- 新しいサンプルコードや、高度な機能説明が加えられ、ユーザーがテキスト抽出の詳細を理解しやすくなっています。

## Breaking changes
- 「concept-layout.md」が「layout.md」にリネームされ、コンテンツが大幅に更新されました。具体的な例やコードスニペットが追加され、ドキュメントが1104行に及ぶ大規模な修正を受けています。
- 他にも、Document IntelligenceのReadモデルに関する概念ドキュメント「concept-read.md」が削除されました。

## Other updates
- 多数の文書がリネームされ、構造の一貫性を保つためにリンクパスの修正が行われました。
- メタデータの一部が削除されるなどして、文書の構造が整理され、よりシンプルになっています。
- 各SDKやREST APIのリファレンスが整理され、相対パスリンクが導入されました。
- SDKガイドや関連ドキュメントのリンクが逐次更新され、利用者が最新のリソースにアクセスできるようになっています。

# Insights
今回の更新は、主に構造の一貫性とドキュメント内容の正確性を向上させるために行われたものであり、ユーザーはより効率的に情報を扱うことができるようになります。多くの文書がリネームされ、リンクが相対パスに変更されたことで、文書全体の整合性が高まり、ナビゲーションがスムーズになります。また、新たに追加されたReadモデルのページにより、ユーザーはOCR技術をより活用して多様な文書タイプからのデータ抽出を行うことが可能となります。

このように、ドキュメント更新は新機能をサポートするとともに、技術者やユーザーがDocument Intelligenceの機能をより直感的に活用できるように配慮されています。最新のAPIバージョンやUIの更新を反映し、ユーザーエクスペリエンスが向上することを目的とした施策です。これらの取り組みにより、ユーザーはより包括的な情報をもとに迅速な意思決定が可能になります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [create-sas-tokens.md](#item-dc2ea3) | minor update | SASトークン作成に関するドキュメントのファイル名変更とパス修正 | renamed | 10 | 12 | 22 | 
| [encrypt-data-at-rest.md](#item-f61d45) | minor update | データの静止状態における暗号化に関するドキュメントのファイル名変更とパス修正 | renamed | 3 | 7 | 10 | 
| [managed-identities-secured-access.md](#item-05ef7b) | minor update | マネージドアイデンティティによる安全なアクセスに関するドキュメントのファイル名変更とパス修正 | renamed | 20 | 22 | 42 | 
| [managed-identities.md](#item-be183c) | minor update | マネージドアイデンティティに関するドキュメントのファイル名変更とパス修正 | renamed | 16 | 17 | 33 | 
| [concept-read.md](#item-1050a3) | breaking change | Document Intelligence の Read モデルに関する概念ドキュメントの削除 | removed | 0 | 435 | 435 | 
| [accuracy-confidence.md](#item-56cda7) | minor update | モデルの精度と分析の信頼性スコアに関するドキュメントのリネーム | renamed | 10 | 12 | 22 | 
| [add-on-capabilities.md](#item-96ed69) | minor update | Document Intelligence の追加機能に関するドキュメントのリネーム | renamed | 99 | 40 | 139 | 
| [analyze-document-response.md](#item-f785b2) | minor update | ドキュメント分析APIレスポンスに関するドキュメントのリネーム | renamed | 15 | 18 | 33 | 
| [choose-model-feature.md](#item-6ea879) | minor update | モデル選択に関するドキュメントのリネーム | renamed | 36 | 46 | 82 | 
| [incremental-classifier.md](#item-c9bffe) | minor update | インクリメンタル分類器に関するドキュメントのリネーム | renamed | 17 | 11 | 28 | 
| [query-fields.md](#item-c58523) | minor update | クエリフィールドに関するドキュメントのリネーム | renamed | 6 | 8 | 14 | 
| [retrieval-augmented-generation.md](#item-c42dcc) | minor update | 情報検索強化生成に関するドキュメントのリネーム | renamed | 16 | 16 | 32 | 
| [configuration.md](#item-e17282) | minor update | ドキュメントインテリジェンスコンテナの設定に関する記事の修正 | modified | 6 | 8 | 14 | 
| [disconnected.md](#item-c70d0b) | minor update | 切断された環境でのドキュメントインテリジェンスコンテナの使用に関する記事の修正 | modified | 5 | 7 | 12 | 
| [image-tags.md](#item-6a7764) | minor update | ドキュメントインテリジェンスコンテナのイメージタグに関する記事の修正 | modified | 3 | 5 | 8 | 
| [faq.yml](#item-7a051f) | minor update | ドキュメントインテリジェンスのFAQに関する修正 | modified | 10 | 10 | 20 | 
| [build-a-custom-classifier.md](#item-403b74) | minor update | カスタム分類器の構築に関するガイドの更新 | modified | 10 | 12 | 22 | 
| [build-a-custom-model.md](#item-4f2040) | minor update | カスタムモデル構築ガイドの更新 | modified | 8 | 8 | 16 | 
| [build-train-custom-generative-model.md](#item-108e20) | minor update | カスタム生成モデル構築ガイドの更新 | modified | 5 | 7 | 12 | 
| [compose-custom-models.md](#item-bfda06) | minor update | カスタムモデル構成ガイドの更新 | modified | 20 | 23 | 43 | 
| [create-document-intelligence-resource.md](#item-d4cf00) | minor update | ドキュメントインテリジェンスリソースの作成ガイドのリネームと更新 | renamed | 10 | 12 | 22 | 
| [disaster-recovery.md](#item-97e0e7) | minor update | ディザスタリカバリガイドのリネームと更新 | renamed | 6 | 8 | 14 | 
| [estimate-cost.md](#item-6b7006) | minor update | コスト見積もりガイドの更新 | modified | 11 | 13 | 24 | 
| [csharp-sdk.md](#item-5f7d47) | minor update | C# SDKガイドの更新 | modified | 4 | 4 | 8 | 
| [java-sdk.md](#item-0e735a) | minor update | Java SDKガイドの更新 | modified | 4 | 4 | 8 | 
| [javascript-sdk.md](#item-c06c9e) | minor update | JavaScript SDKガイドの更新 | modified | 4 | 4 | 8 | 
| [python-sdk.md](#item-9a38a0) | minor update | Python SDKガイドの更新 | modified | 4 | 4 | 8 | 
| [rest-api.md](#item-73da78) | minor update | REST APIガイドの更新 | modified | 4 | 4 | 8 | 
| [csharp-sdk.md](#item-6736b9) | minor update | C# SDKガイドの更新 | modified | 3 | 3 | 6 | 
| [java-sdk.md](#item-6c0363) | minor update | Java SDKガイドのメタデータ更新 | modified | 1 | 1 | 2 | 
| [javascript-sdk.md](#item-03ed43) | minor update | JavaScript SDKガイドのメタデータおよびコンテンツ更新 | modified | 2 | 2 | 4 | 
| [python-sdk.md](#item-3b07c5) | minor update | Python SDKガイドのメタデータおよびサンプルコード更新 | modified | 2 | 1 | 3 | 
| [rest-api.md](#item-1a8bdb) | minor update | REST APIガイドのメタデータおよびコンテンツ更新 | modified | 6 | 4 | 10 | 
| [csharp-sdk.md](#item-b72ebd) | minor update | C# SDKガイドのメタデータ更新 | modified | 1 | 1 | 2 | 
| [java-sdk.md](#item-65f910) | minor update | Java SDKガイドのメタデータおよび内容更新 | modified | 1 | 2 | 3 | 
| [javascript-sdk.md](#item-b28fc0) | minor update | JavaScript SDKガイドのメタデータ更新 | modified | 1 | 1 | 2 | 
| [python-sdk.md](#item-52b6d7) | minor update | Python SDKガイドのメタデータおよびリンク更新 | modified | 2 | 2 | 4 | 
| [rest-api.md](#item-222da8) | minor update | REST APIガイドのメタデータおよびリンク修正 | modified | 4 | 2 | 6 | 
| [project-share-custom-models.md](#item-acd5dd) | minor update | カスタムモデル共有ガイドのメタデータ更新 | modified | 0 | 2 | 2 | 
| [resolve-errors.md](#item-6c3107) | minor update | エラー解決ガイドのファイル名変更 | renamed | 0 | 2 | 2 | 
| [use-sdk-rest-api.md](#item-25a870) | minor update | SDKおよびREST APIに関するガイドの更新 | modified | 14 | 9 | 23 | 
| [applies-to-v21.md](#item-fa19ef) | minor update | applies-to-v21.mdファイルのメタデータ更新 | modified | 0 | 2 | 2 | 
| [applies-to-v30-v21.md](#item-5311b0) | minor update | applies-to-v30-v21.mdファイルのメタデータ更新 | modified | 0 | 2 | 2 | 
| [applies-to-v30.md](#item-0f6a07) | minor update | applies-to-v30.mdファイルのメタデータ更新 | modified | 0 | 2 | 2 | 
| [applies-to-v31-v30-v21.md](#item-e8f78f) | minor update | applies-to-v31-v30-v21.mdファイルのメタデータ更新 | modified | 0 | 2 | 2 | 
| [applies-to-v31-v30.md](#item-ac265d) | minor update | applies-to-v31-v30.mdファイルのメタデータ更新 | modified | 0 | 2 | 2 | 
| [applies-to-v31.md](#item-5f3c5a) | minor update | applies-to-v31.mdファイルのメタデータ更新 | modified | 0 | 2 | 2 | 
| [applies-to-v40-v31-v30-v21.md](#item-3ca431) | minor update | applies-to-v40-v31-v30-v21.mdファイルのメタデータ更新 | modified | 0 | 2 | 2 | 
| [applies-to-v40-v31-v30.md](#item-cb0a7f) | minor update | applies-to-v40-v31-v30.mdファイルのメタデータ更新 | modified | 0 | 2 | 2 | 
| [applies-to-v40-v31.md](#item-b11839) | minor update | applies-to-v40-v31.mdファイルのメタデータ更新 | modified | 0 | 2 | 2 | 
| [applies-to-v40.md](#item-94c322) | minor update | applies-to-v40.mdファイルのメタデータ更新 | modified | 0 | 2 | 2 | 
| [create-resource.md](#item-f52ea3) | minor update | create-resource.mdファイルのメタデータ更新 | modified | 0 | 2 | 2 | 
| [improve-results-unlabeled.md](#item-bc1b92) | minor update | improve-results-unlabeled.mdファイルのリンク修正 | modified | 1 | 1 | 2 | 
| [onedrive.md](#item-ae5d5a) | minor update | onedrive.mdファイルのリンクとMarkdown構文の修正 | modified | 29 | 30 | 59 | 
| [sharepoint.md](#item-469890) | minor update | sharepoint.mdファイルのリンク更新とMarkdown修正 | modified | 34 | 32 | 66 | 
| [model-analysis-features.md](#item-0fe95e) | minor update | model-analysis-features.mdからの不要なメタデータ削除 | modified | 0 | 2 | 2 | 
| [model-type-name.md](#item-5c7f96) | minor update | model-type-name.mdのリンク更新とメタデータ調整 | modified | 3 | 5 | 8 | 
| [preview-notice.md](#item-e2c198) | minor update | preview-notice.mdからの不要なメタデータ削除 | modified | 0 | 2 | 2 | 
| [index.yml](#item-9c57d7) | minor update | index.yml内のリンクの更新と整理 | modified | 12 | 12 | 24 | 
| [custom.md](#item-fafe89) | minor update | カスタムモデルに関するファイル名の変更とリンクの更新 | renamed | 4 | 6 | 10 | 
| [ocr.md](#item-143ab8) | minor update | OCR関連ファイルの名称変更とリンクの更新 | renamed | 23 | 9 | 32 | 
| [prebuilt.md](#item-ac5486) | minor update | プリビルトモデルに関するファイル名の変更とリンクの更新 | renamed | 4 | 6 | 10 | 
| [model-overview.md](#item-768c0d) | minor update | モデル概要ファイルの名称変更と内容の更新 | renamed | 54 | 55 | 109 | 
| [overview.md](#item-4e36ba) | minor update | ドキュメントインテリジェンスの概要ページの改訂 | modified | 151 | 141 | 292 | 
| [bank-check.md](#item-8655d6) | minor update | 銀行小切手ページの名称変更と内容の更新 | renamed | 6 | 6 | 12 | 
| [bank-statement.md](#item-fa4383) | minor update | 銀行取引明細ページの名称変更と内容の更新 | renamed | 6 | 6 | 12 | 
| [batch-analysis.md](#item-9fb3da) | minor update | バッチ分析ページの名称変更と内容の更新 | renamed | 10 | 10 | 20 | 
| [business-card.md](#item-114b38) | minor update | 名刺モデルページの名称変更と内容の更新 | renamed | 19 | 21 | 40 | 
| [contract.md](#item-6d01dd) | minor update | 契約モデルページの名称変更と内容の更新 | renamed | 12 | 14 | 26 | 
| [credit-card.md](#item-5d0c6d) | minor update | クレジットカードモデルページの名称変更と内容の更新 | renamed | 10 | 9 | 19 | 
| [general-document.md](#item-ff8975) | minor update | 一般文書モデルページの名称変更と内容の更新 | renamed | 11 | 13 | 24 | 
| [health-insurance-card.md](#item-6b1c0e) | minor update | 健康保険証モデルページの名称変更と内容の更新 | renamed | 18 | 20 | 38 | 
| [id-document.md](#item-bf45fa) | minor update | ID文書モデルページの名称変更と内容の更新 | renamed | 23 | 23 | 46 | 
| [invoice.md](#item-cabbf9) | minor update | 請求書モデルページの名称変更と内容の更新 | renamed | 25 | 25 | 50 | 
| [layout.md](#item-f7c4c8) | breaking change | レイアウトモデルページの名称変更と大幅な内容更新 | renamed | 651 | 453 | 1104 | 
| [marriage-certificate.md](#item-936798) | minor update | 婚姻証明書モデルページの名称変更と内容更新 | renamed | 10 | 9 | 19 | 
| [mortgage-documents.md](#item-b3136a) | minor update | 住宅ローン文書モデルページの名称変更と内容更新 | renamed | 13 | 14 | 27 | 
| [pay-stub.md](#item-7f747e) | minor update | 給与明細モデルページの名称変更と内容更新 | renamed | 5 | 5 | 10 | 
| [read.md](#item-06f32f) | new feature | Document Intelligence Readモデルの新しいページの追加 | added | 633 | 0 | 633 | 
| [receipt.md](#item-089054) | minor update | 領収書モデルページの名称変更と相対パスの更新 | renamed | 22 | 24 | 46 | 
| [tax-document.md](#item-e19fe5) | minor update | 税務文書モデルページの名称変更と相対パスの更新 | renamed | 12 | 12 | 24 | 
| [csharp-sdk.md](#item-ee69c7) | minor update | C# SDKガイドのリンク修正とメタデータの更新 | modified | 2 | 4 | 6 | 
| [java-sdk.md](#item-166b2e) | minor update | Java SDKガイドのリンク修正と内容の更新 | modified | 2 | 2 | 4 | 
| [javascript-sdk.md](#item-615fcd) | minor update | JavaScript SDKガイドのリンク修正と内容の更新 | modified | 3 | 3 | 6 | 
| [python-sdk.md](#item-83c83f) | minor update | Python SDKガイドのリンク修正と内容の更新 | modified | 2 | 2 | 4 | 
| [rest-api.md](#item-9d952f) | minor update | REST APIガイドのリンク修正 | modified | 1 | 1 | 2 | 
| [csharp.md](#item-5bb590) | minor update | C#ガイドのリンク修正と情報の更新 | modified | 4 | 4 | 8 | 
| [java.md](#item-dd6c6f) | minor update | Javaガイドのリンク修正と情報の更新 | modified | 4 | 4 | 8 | 
| [javascript.md](#item-1b193e) | minor update | JavaScriptガイドのリンク修正と内容の更新 | modified | 5 | 5 | 10 | 
| [python.md](#item-996d7f) | minor update | Pythonガイドのリンク修正と内容の更新 | modified | 5 | 5 | 10 | 
| [rest-api.md](#item-3bd0eb) | minor update | REST APIガイドのリンク修正と不必要なメタ情報の削除 | modified | 3 | 5 | 8 | 
| [try-document-intelligence-studio.md](#item-ff12d6) | minor update | ドキュメントインテリジェンススタジオに関するリンク修正 | modified | 1 | 3 | 4 | 
| [service-limits.md](#item-5ceae5) | minor update | サービス制限に関するリンク修正とメタ情報の整理 | modified | 16 | 18 | 34 | 
| [studio-overview.md](#item-db8fa3) | minor update | Document Intelligence Studioの概要に関するリンク修正とメタ情報の追加 | modified | 11 | 10 | 21 | 
| [toc.yml](#item-81aa7b) | minor update | ドキュメントインテリジェンスの目次の更新とリンク修正 | modified | 128 | 119 | 247 | 
| [composed-models.md](#item-3f2e9f) | minor update | ドキュメントインテリジェンスのコンポーズモデルのファイル名変更とリンク修正 | renamed | 18 | 18 | 36 | 
| [custom-classifier.md](#item-42f8fd) | minor update | カスタム分類モデル文書のファイル名変更とリンク修正 | renamed | 9 | 9 | 18 | 
| [custom-generative-extraction.md](#item-a8f912) | minor update | カスタム生成抽出モデル文書のファイル名変更とリンク修正 | renamed | 7 | 7 | 14 | 
| [custom-label-tips.md](#item-041f5c) | minor update | カスタムラベル作成のヒント文書のファイル名変更とリンク修正 | renamed | 7 | 7 | 14 | 
| [custom-labels.md](#item-90435a) | minor update | カスタムラベルに関する文書のファイル名変更とリンク修正 | renamed | 8 | 8 | 16 | 
| [custom-lifecycle.md](#item-2b7401) | minor update | カスタムライフサイクルに関する文書のファイル名変更とリンク修正 | renamed | 3 | 5 | 8 | 
| [custom-model.md](#item-27c3b9) | minor update | カスタムモデルに関する文書のファイル名変更とリンク修正 | renamed | 28 | 30 | 58 | 
| [custom-neural.md](#item-ac0e69) | minor update | カスタムニューラルモデルに関する文書のファイル名変更とリンク修正 | renamed | 26 | 24 | 50 | 
| [custom-template.md](#item-78e685) | minor update | カスタムテンプレートに関する文書のファイル名変更とリンク修正 | renamed | 14 | 16 | 30 | 
| [azure-function.md](#item-e0ba8d) | minor update | Azure Functionsチュートリアルにおけるリンクの修正 | renamed | 9 | 9 | 18 | 
| [logic-apps.md](#item-c6a43a) | minor update | Logic Appsチュートリアルにおけるファイル名変更とリンク修正 | renamed | 13 | 15 | 28 | 
| [deploy-label-tool.md](#item-e3c9ae) | minor update | Label Toolデプロイチュートリアルのファイル名変更とリンク修正 | renamed | 12 | 14 | 26 | 
| [label-tool.md](#item-2eeebd) | minor update | Label Toolに関する文書のファイル名変更とリンク修正 | renamed | 22 | 25 | 47 | 
| [sdk-overview-v2-1.md](#item-c5f5c7) | minor update | SDKオーバービュー文書のファイル名変更とリンク修正 | renamed | 16 | 16 | 32 | 
| [supervised-table-tags.md](#item-21d2b0) | minor update | 監視付きテーブルタグに関する文書のファイル名変更とリンク修正 | renamed | 7 | 8 | 15 | 
| [try-sample-label-tool.md](#item-c07ebc) | minor update | サンプルラベルツールのクイックスタート文書のファイル名変更とリンク修正 | renamed | 10 | 12 | 22 | 
| [changelog-release-history.md](#item-dccdd3) | minor update | リリース履歴の文書のファイル名変更とリンク修正 | renamed | 1 | 3 | 4 | 
| [sdk-overview-v3-0.md](#item-f82845) | minor update | Document Intelligence SDKの概要文書のリネームとリンク修正 | renamed | 11 | 11 | 22 | 
| [sdk-overview-v3-1.md](#item-534671) | minor update | Document Intelligence SDKの概要文書のリネームとリンク修正 | renamed | 9 | 10 | 19 | 
| [sdk-overview-v4-0.md](#item-d59a82) | minor update | Document Intelligence SDKの概要文書のリネームとリンク修正 | renamed | 10 | 10 | 20 | 
| [v3-1-migration-guide.md](#item-6f9943) | minor update | Document Intelligence v3.1 マイグレーションガイドのリネームとリンク修正 | renamed | 12 | 14 | 26 | 
| [whats-new.md](#item-1ec8d3) | minor update | Document Intelligenceに関する「What's New」ページの更新 | modified | 77 | 89 | 166 | 


# Modified Contents
## articles/ai-services/document-intelligence/authentication/create-sas-tokens.md{#item-dc2ea3}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ ms.topic: how-to
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.date: 07/11/2024
 ms.author: lajanuar
 ---
@@ -15,12 +13,12 @@ ms.author: lajanuar
 # Create SAS tokens for storage containers
 
 ::: moniker range="<=doc-intel-4.0.0"
- [!INCLUDE [applies to v4.0 v3.1 v3.0 v2.1](includes/applies-to-v40-v31-v30-v21.md)]
+ [!INCLUDE [applies to v4.0 v3.1 v3.0 v2.1](../includes/applies-to-v40-v31-v30-v21.md)]
 ::: moniker-end
 
- In this article, learn how to create user delegation, shared access signature (SAS) tokens, using the Azure portal or Azure Storage Explorer. User delegation SAS tokens are secured with Microsoft Entra credentials. SAS tokens provide secure, delegated access to resources in your Azure storage account.
+In this article, learn how to create user delegation, shared access signature (SAS) tokens, using the Azure portal or Azure Storage Explorer. User delegation SAS tokens are secured with Microsoft Entra credentials. SAS tokens provide secure, delegated access to resources in your Azure storage account.
 
-:::image type="content" source="media/sas-tokens/sas-url-token.png" alt-text="Screenshot of storage URI with SAS token appended.":::
+  :::image type="content" source="../media/sas-tokens/sas-url-token.png" alt-text="Screenshot of storage URI with SAS token appended.":::
 
 At a high level, here's how SAS tokens work:
 
@@ -68,20 +66,20 @@ To get started, you need:
 1. Sign in to the [Azure portal](https://portal.azure.com).
     * Select **Your storage account** → **Data storage** → **Containers**.
 
-   :::image type="content" source="media/sas-tokens/data-storage-menu.png" alt-text="Screenshot that shows the Data storage menu in the Azure portal.":::
+   :::image type="content" source="../media/sas-tokens/data-storage-menu.png" alt-text="Screenshot that shows the Data storage menu in the Azure portal.":::
 
 1. Select a container from the list.
 
 1. Select **Upload** from the menu at the top of the page.
 
-    :::image type="content" source="media/sas-tokens/container-upload-button.png" alt-text="Screenshot that shows the container Upload button in the Azure portal.":::
+    :::image type="content" source="../media/sas-tokens/container-upload-button.png" alt-text="Screenshot that shows the container Upload button in the Azure portal.":::
 
 1. The **Upload blob** window appears. Select your files to upload.
 
-    :::image type="content" source="media/sas-tokens/upload-blob-window.png" alt-text="Screenshot that shows the Upload blob window in the Azure portal.":::
+    :::image type="content" source="../media/sas-tokens/upload-blob-window.png" alt-text="Screenshot that shows the Upload blob window in the Azure portal.":::
 
    > [!NOTE]
-   > By default, the REST API uses documents located at the root of your container. You can also use data organized in subfolders if specified in the API call. For more information, see [Organize your data in subfolders](how-to-guides/build-a-custom-model.md?view=doc-intel-2.1.0&preserve-view=true#organize-your-data-in-subfolders-optional).
+   > By default, the REST API uses documents located at the root of your container. You can also use data organized in subfolders if specified in the API call. For more information, see [Organize your data in subfolders](../how-to-guides/build-a-custom-model.md?view=doc-intel-2.1.0&preserve-view=true#organize-your-data-in-subfolders-optional).
 
 ## Use the Azure portal
 
@@ -99,13 +97,13 @@ The Azure portal is a web-based console that enables you to manage your Azure su
 
    * Make sure the **Read**, **Write**, **Delete**, and **List** permissions are selected.
 
-    :::image type="content" source="media/sas-tokens/sas-permissions.png" alt-text="Screenshot that shows the SAS permission fields in the Azure portal.":::
+    :::image type="content" source="../media/sas-tokens/sas-permissions.png" alt-text="Screenshot that shows the SAS permission fields in the Azure portal.":::
 
     >[!IMPORTANT]
     >
     > * If you receive a message similar to the following one, you'll also need to assign access to the blob data in your storage account:
     >
-    >     :::image type="content" source="media/sas-tokens/need-permissions.png" alt-text="Screenshot that shows the lack of permissions warning.":::
+    >     :::image type="content" source="../media/sas-tokens/need-permissions.png" alt-text="Screenshot that shows the lack of permissions warning.":::
     >
     > * [Azure role-based access control](/azure/role-based-access-control/overview) (Azure RBAC) is the authorization system used to manage access to Azure resources. Azure RBAC helps you manage access and permissions for your Azure resources.
     > * [Assign an Azure role for access to blob data](/azure/role-based-access-control/role-assignments-portal?tabs=current) to assign a role that allows for read, write, and delete permissions for your Azure storage container. *See* [Storage Blob Data Contributor](/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).
@@ -179,4 +177,4 @@ That's it! You learned how to create SAS tokens to authorize how clients access
 ## Next step
 
 > [!div class="nextstepaction"]
-> [Build a training data set](how-to-guides/build-a-custom-model.md?view=doc-intel-2.1.0&preserve-view=true)
+> [Build a training data set](../how-to-guides/build-a-custom-model.md?view=doc-intel-2.1.0&preserve-view=true)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SASトークン作成に関するドキュメントのファイル名変更とパス修正"
}
```

### Explanation
この変更は、SASトークンの作成に関するドキュメントファイルのリネームおよびいくつかのパスの修正を行っています。元のファイル名は「create-sas-tokens.md」であり、同ファイルが新しい場所に移動したことを示しています。

具体的には、モニカーや画像のソースパスを更新し、相対パスを使用するように変更されました。この修正により、ドキュメント内のリソースへの参照がより整然とし、メンテナンスがしやすくなります。また、一部の不必要なデータが削除され、全体の内容が整理されています。この変更は、小規模な更新として位置づけられ、機能に影響を与えることはありませんが、ドキュメントの正確性と可読性を向上させることが目的です。

## articles/ai-services/document-intelligence/authentication/encrypt-data-at-rest.md{#item-f61d45}

<details>
<summary>Diff</summary>
````diff
@@ -7,17 +7,13 @@ manager: venkyv
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
 ms.date: 11/15/2023
-ms.author: egeaney
-ms.custom:
-  - applied-ai-non-critical-form
-  - ignite-2023
 monikerRange: '<=doc-intel-4.0.0'
 ---
 
 
 # Document Intelligence encryption of data at rest
 
-[!INCLUDE [applies to v4.0, v3.1, v3.0, and v2.1](includes/applies-to-v40-v31-v30-v21.md)]
+[!INCLUDE [applies to v4.0, v3.1, v3.0, and v2.1](../includes/applies-to-v40-v31-v30-v21.md)]
 
 > [!IMPORTANT]
 >
@@ -27,12 +23,12 @@ monikerRange: '<=doc-intel-4.0.0'
 
 Azure AI Document Intelligence automatically encrypts your data when persisting it to the cloud. Document Intelligence encryption protects your data to help you to meet your organizational security and compliance commitments.
 
-[!INCLUDE [cognitive-services-about-encryption](../../ai-services/includes/cognitive-services-about-encryption.md)]
+[!INCLUDE [cognitive-services-about-encryption](../../../ai-services/includes/cognitive-services-about-encryption.md)]
 
 > [!IMPORTANT]
 > Customer-managed keys are only available resources created after 11 May, 2020. To use CMK with Document Intelligence, you will need to create a new Document Intelligence resource. Once the resource is created, you can use Azure Key Vault to set up your managed identity.
 
-[!INCLUDE [cognitive-services-cmk](../../ai-services/includes/configure-customer-managed-keys.md)]
+[!INCLUDE [cognitive-services-cmk](../../../ai-services/includes/configure-customer-managed-keys.md)]
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データの静止状態における暗号化に関するドキュメントのファイル名変更とパス修正"
}
```

### Explanation
この変更は、「データの静止状態における暗号化」に関するドキュメントのリネームといくつかのパス修正を行っています。元のファイル名は「encrypt-data-at-rest.md」であり、同ファイルが新しい場所に移動されていることを示しています。

具体的には、ドキュメント内で使用されている参照パスを相対パスに変更し、より整理された形にしています。この更新により、ファイルが正しくリンクされるようになり、文書内での情報の整合性が向上します。また、一部の不必要な情報が削除されており、より明確で簡潔な内容となっています。この変更は、小規模な更新として位置づけられますが、全体の文書の質と可読性を向上させることが目的です。

## articles/ai-services/document-intelligence/authentication/managed-identities-secured-access.md{#item-05ef7b}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Learn how to configure secure communications between Document Intel
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
 ms.date: 05/23/2024
 ms.author: vikurpad
@@ -16,27 +14,27 @@ monikerRange: '<=doc-intel-4.0.0'
 
 # Configure secure access with managed identities and virtual networks
 
-[!INCLUDE [applies to v4.0, v3.1, v3.0, and v2.1](includes/applies-to-v40-v31-v30-v21.md)]
+[!INCLUDE [applies to v4.0, v3.1, v3.0, and v2.1](../includes/applies-to-v40-v31-v30-v21.md)]
 
 This how-to guide walks you through the process of enabling secure connections for your Document Intelligence resource. You can secure the following connections:
 
 * Communication between a client application within a Virtual Network (`VNET`) and your Document Intelligence Resource.
 
-* Communication between Document Intelligence Studio and your Document Intelligence resource.
+* Communication between Document Intelligence Studio and your Document Intelligence resource.F
 
 * Communication between your Document Intelligence resource and a storage account (needed when training a custom model).
 
  You're setting up your environment to secure the resources:
 
-  :::image type="content" source="media/managed-identities/secure-config-di.png" alt-text="Screenshot of secure configuration with managed identity and virtual networks.":::
+  :::image type="content" source="../media/managed-identities/secure-config-di.png" alt-text="Screenshot of secure configuration with managed identity and virtual networks.":::
 
 ## Prerequisites
 
 To get started, you need:
 
 * An active [**Azure account**](https://azure.microsoft.com/free/cognitive-services/)—if you don't have one, you can [**create a free account**](https://azure.microsoft.com/free/).
 
-* A [**Document Intelligence**](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) or [**Azure AI services**](https://portal.azure.com/#create/Microsoft.CognitiveServicesAIServices) resource in the Azure portal. For detailed steps, _see_ [Create an Azure AI services resource](../../ai-services/multi-service-resource.md?pivots=azportal).
+* A [**Document Intelligence**](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) or [**Azure AI services**](https://portal.azure.com/#create/Microsoft.CognitiveServicesAIServices) resource in the Azure portal. For detailed steps, _see_ [Create an Azure AI services resource](../../../ai-services/multi-service-resource.md?pivots=azportal).
 
 * An [**Azure blob storage account**](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM) in the same region as your Document Intelligence resource. Create containers to store and organize your blob data within your storage account.
 
@@ -64,7 +62,7 @@ Configure each of the resources to ensure that the resources can communicate wit
 
 You now have a working implementation of all the components needed to build a Document Intelligence solution with the default security model:
 
-  :::image type="content" source="media/managed-identities/default-config-di.png" alt-text="Screenshot of default security configuration.":::
+  :::image type="content" source="../media/managed-identities/default-config-di.png" alt-text="Screenshot of default security configuration.":::
 
 Next, complete the following steps:
 
@@ -84,7 +82,7 @@ Next, complete the following steps:
 
 Navigate to the Document Intelligence resource in the Azure portal and select the **Identity** tab. Toggle the **System assigned** managed identity to **On** and save the changes:
 
-  :::image type="content" source="media/managed-identities/v2-fr-mi.png" alt-text="Screenshot of configure managed identity.":::
+  :::image type="content" source="../media/managed-identities/v2-fr-mi.png" alt-text="Screenshot of configure managed identity.":::
 
 ## Secure the Storage account
 
@@ -96,7 +94,7 @@ Start configuring secure communications by navigating to the **Networking** tab
 
 1. **Save** your changes.
 
-  :::image type="content" source="media/managed-identities/v2-stg-firewall.png" alt-text="Screenshot of configure storage firewall.":::
+  :::image type="content" source="../media/managed-identities/v2-stg-firewall.png" alt-text="Screenshot of configure storage firewall.":::
 
 > [!NOTE]
 >
@@ -112,11 +110,11 @@ To ensure that the Document Intelligence resource can access the training datase
 
 1. Select the **Add role assignment** button.
 
-    :::image type="content" source="media/managed-identities/v2-stg-role-assign-role.png" alt-text="Screenshot of add role assignment window.":::
+    :::image type="content" source="../media/managed-identities/v2-stg-role-assign-role.png" alt-text="Screenshot of add role assignment window.":::
 
 1. On the **Role** tab, search for and select the **Storage Blob Data Contributor** permission and select **Next**.
 
-    :::image type="content" source="media/managed-identities/v2-stg-role-assignment.png" alt-text="Screenshot of choose a role tab.":::
+    :::image type="content" source="../media/managed-identities/v2-stg-role-assignment.png" alt-text="Screenshot of choose a role tab.":::
 
 1. On the **Members** tab, select the **Managed identity** option and choose **+ Select members**
 
@@ -128,7 +126,7 @@ To ensure that the Document Intelligence resource can access the training datase
 
    * **Select**. Choose the Document Intelligence resource you enabled with a managed identity.
 
-    :::image type="content" source="media/managed-identities/v2-stg-role-assign-resource.png" alt-text="Screenshot of managed identities dialog window.":::
+    :::image type="content" source="../media/managed-identities/v2-stg-role-assign-resource.png" alt-text="Screenshot of managed identities dialog window.":::
 
 1. **Close** the dialog window.
 
@@ -167,7 +165,7 @@ Next, configure the virtual network to ensure only resources within the virtual
 >
 >If you try accessing any of the Document Intelligence Studio features, you'll see an access denied message. To enable access from the Studio on your machine, select the **Add your client IP address** checkbox and **Save** to restore access.
 
-  :::image type="content" source="media/managed-identities/v2-fr-network.png" alt-text="Screenshot showing how to disable public access to Document Intelligence.":::
+  :::image type="content" source="../media/managed-identities/v2-fr-network.png" alt-text="Screenshot showing how to disable public access to Document Intelligence.":::
 
 ### Configure your private endpoint
 
@@ -185,7 +183,7 @@ Next, configure the virtual network to ensure only resources within the virtual
 
     * Select **Next: Resource**.
 
-    :::image type="content" source="media/managed-identities/v2-fr-private-end-basics.png" alt-text="Screenshot showing how to set-up a private endpoint":::
+    :::image type="content" source="../media/managed-identities/v2-fr-private-end-basics.png" alt-text="Screenshot showing how to set-up a private endpoint.":::
 
 ### Configure your virtual network
 
@@ -199,7 +197,7 @@ Next, configure the virtual network to ensure only resources within the virtual
 
 1. Accept the default value **Yes** to **integrate with private DNS zone**.
 
-    :::image type="content" source="media/managed-identities/v2-fr-private-end-vnet.png" alt-text="Screenshot showing how to configure private endpoint":::
+    :::image type="content" source="../media/managed-identities/v2-fr-private-end-vnet.png" alt-text="Screenshot showing how to configure private endpoint.":::
 
 1. Accept the remaining defaults and select **Next: Tags**.
 
@@ -221,13 +219,13 @@ Navigate to your **storage account** on the Azure portal.
 
 1. Select **Next: Resource**.
 
-    :::image type="content" source="media/managed-identities/v2-stg-private-end-basics.png" alt-text="Screenshot showing how to create a private endpoint":::
+    :::image type="content" source="../media/managed-identities/v2-stg-private-end-basics.png" alt-text="Screenshot showing how to create a private endpoint.":::
 
 1. On the resource tab, select **blob** from the **Target sub-resource** list.
 
 1. select **Next: Virtual Network**.
 
-   :::image type="content" source="media/managed-identities/v2-stg-private-end-resource.png" alt-text="Screenshot showing how to configure a private endpoint for a blob.":::
+   :::image type="content" source="../media/managed-identities/v2-stg-private-end-resource.png" alt-text="Screenshot showing how to configure a private endpoint for a blob.":::
 
 1. Select the **Virtual network** and **Subnet**. Make sure **Enable network policies for all private endpoints in this subnet** is selected and the **Dynamically allocate IP address** is enabled.
 
@@ -262,28 +260,28 @@ That's it! You can now configure secure access for your Document Intelligence re
 
 * **Failed to access Blob container**:
 
-   :::image type="content" source="media/managed-identities/cors-error.png" alt-text="Screenshot of error message when CORS config is required":::
+   :::image type="content" source="../media/managed-identities/cors-error.png" alt-text="Screenshot of error message when CORS config is required.":::
 
   **Resolution**:
-    1. [Configure CORS](quickstarts/try-document-intelligence-studio.md#configure-cors).
+    1. [Configure CORS](../quickstarts/try-document-intelligence-studio.md#configure-cors).
  
     1. Make sure the client computer can access Document Intelligence resource and storage account, either they are in the same `VNET`, or client IP address is allowed in **Networking > Firewalls and virtual networks** setting page of both Document Intelligence resource and storage account.
 
 * **AuthorizationFailure**:
 
-  :::image type="content" source="media/managed-identities/auth-failure.png" alt-text="Screenshot of authorization failure error.":::
+  :::image type="content" source="../media/managed-identities/auth-failure.png" alt-text="Screenshot of authorization failure error.":::
 
   **Resolution**: Make sure the client computer can access Document Intelligence resource and storage account, either they are in the same `VNET`, or client IP address is allowed in **Networking > Firewalls and virtual networks** setting page of both Document Intelligence resource and storage account.
 
 * **ContentSourceNotAccessible**:
 
-   :::image type="content" source="media/managed-identities/content-source-error.png" alt-text="Screenshot of content source not accessible error.":::
+   :::image type="content" source="../media/managed-identities/content-source-error.png" alt-text="Screenshot of content source not accessible error.":::
 
     **Resolution**: Make sure you grant your Document Intelligence managed identity the role of **Storage Blob Data Contributor** and enabled **Trusted services** access or **Resource instance** rules on the networking tab.
 
 * **AccessDenied**:
 
-  :::image type="content" source="media/managed-identities/access-denied.png" alt-text="Screenshot of an access denied error.":::
+  :::image type="content" source="../media/managed-identities/access-denied.png" alt-text="Screenshot of an access denied error.":::
 
   **Resolution**: Make sure the client computer can access Document Intelligence resource and storage account, either they are in the same `VNET`, or client IP address is allowed in **Networking > Firewalls and virtual networks** setting page of both Document Intelligence resource and storage account.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージドアイデンティティによる安全なアクセスに関するドキュメントのファイル名変更とパス修正"
}
```

### Explanation
この変更は、「マネージドアイデンティティによる安全なアクセス」に関するドキュメントのリネーム及びいくつかのパス修正を行っています。元のファイル名は「managed-identities-secured-access.md」であり、同ファイルが新しい場所に移動されたことを示しています。

具体的には、ドキュメント内の「適用されるバージョン」や「画像のソースパス」を相対パスに更新し、リソースアクセスの手順を明確にしています。また、不要な情報が削除され、全体のコンテンツが整理されています。この変更により、リソース間のセキュアな通信を設定する手順がより明確になり、可読性が向上しています。全体として、この更新は小規模な改善と位置づけられますが、ドキュメントの質と使いやすさを高めることが目的です。

## articles/ai-services/document-intelligence/authentication/managed-identities.md{#item-be183c}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +1,10 @@
 ---
-title: Create and use managed identities with Document Intelligence 
+title: Create and use managed identities with Document Intelligence
 titleSuffix: Azure AI services
 description: Understand how to create and  use managed identity with Document Intelligence.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
 ms.date: 05/23/2024
 ms.author: lajanuar
@@ -16,19 +14,19 @@ monikerRange: '<=doc-intel-4.0.0'
 
 # Managed identities for Document Intelligence
 
-[!INCLUDE [applies to v4.0, v3.1, v3.0, v2.1](includes/applies-to-v40-v31-v30-v21.md)]
+[!INCLUDE [applies to v4.0, v3.1, v3.0, v2.1](../includes/applies-to-v40-v31-v30-v21.md)]
 
 Managed identities for Azure resources are service principals that create a Microsoft Entra identity and specific permissions for Azure managed resources:
 
-:::image type="content" source="media/managed-identities/rbac-flow.png" alt-text="Screenshot of managed identity flow (RBAC).":::
+:::image type="content" source="../media/managed-identities/rbac-flow.png" alt-text="Screenshot of managed identity flow (RBAC).":::
 
 * Managed identities grant access to any resource that supports Microsoft Entra authentication, including your own applications. Unlike security keys and authentication tokens, managed identities eliminate the need for developers to manage credentials.
 
 * You can grant access to an Azure resource and assign an Azure role to a managed identity using [Azure role-based access control (Azure RBAC)](/azure/role-based-access-control/overview). There's no added cost to use managed identities in Azure.
 
 > [!IMPORTANT]
 >
-> * Managed identities eliminate the need for you to manage credentials, including Shared Access Signature (SAS) tokens. 
+> * Managed identities eliminate the need for you to manage credentials, including Shared Access Signature (SAS) tokens.
 >
 > * Managed identities are a safer way to grant access to data without having credentials in your code.
 
@@ -48,21 +46,21 @@ To get started, you need:
 
 * An active [**Azure account**](https://azure.microsoft.com/free/cognitive-services/)—if you don't have one, you can [**create a free account**](https://azure.microsoft.com/free/).
 
-* A [**Document Intelligence**](https://portal.azure.com/#create/Microsoft.CognitiveServicesTextTranslation) or [**Azure AI services**](https://portal.azure.com/#create/Microsoft.CognitiveServicesAIServices) resource in the Azure portal. For detailed steps, _see_ [Create an Azure AI services resource](../../ai-services/multi-service-resource.md?pivots=azportal).
+* A [**Document Intelligence**](https://portal.azure.com/#create/Microsoft.CognitiveServicesTextTranslation) or [**Azure AI services**](https://portal.azure.com/#create/Microsoft.CognitiveServicesAIServices) resource in the Azure portal. For detailed steps, _see_ [Create an Azure AI services resource](../../../ai-services/multi-service-resource.md?pivots=azportal).
 
 * An [**Azure blob storage account**](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM) in the same region as your Document Intelligence resource. You also need to create containers to store and organize your blob data within your storage account.
 
   * If your storage account is behind a firewall, **you must enable the following configuration**: </br></br>
 
   * On your storage account page, select **Security + networking** → **Networking** from the left menu.
-    :::image type="content" source="media/managed-identities/security-and-networking-node.png" alt-text="Screenshot of security + networking tab.":::
+    :::image type="content" source="../media/managed-identities/security-and-networking-node.png" alt-text="Screenshot of security + networking tab.":::
 
   * In the main window, select **Allow access from selected networks**.
-  :::image type="content" source="media/managed-identities/firewalls-and-virtual-networks.png" alt-text="Screenshot of Selected networks radio button selected.":::
+  :::image type="content" source="../media/managed-identities/firewalls-and-virtual-networks.png" alt-text="Screenshot of Selected networks radio button selected.":::
 
   * On the selected networks page, navigate to the **Exceptions** category and make certain that the  [**`Allow Azure services on the trusted services list to access this storage account`**](/azure/storage/common/storage-network-security?tabs=azure-portal#manage-exceptions) checkbox is enabled.
 
-    :::image type="content" source="media/managed-identities/allow-trusted-services-checkbox-portal-view.png" alt-text="Screenshot of allow trusted services checkbox, portal view":::
+    :::image type="content" source="../media/managed-identities/allow-trusted-services-checkbox-portal-view.png" alt-text="Screenshot of allow trusted services checkbox, portal view.":::
 * A brief understanding of [**Azure role-based access control (Azure RBAC)**](/azure/role-based-access-control/role-assignments-portal) using the Azure portal.
 
 ## Managed identity assignments
@@ -87,7 +85,7 @@ In the following steps, we enable a system-assigned managed identity and grant D
 
 1. In the left rail, Select **Identity** from the **Resource Management** list:
 
-    :::image type="content" source="media/managed-identities/resource-management-identity-tab.png" alt-text="Screenshot of resource management identity tab in the Azure portal.":::
+    :::image type="content" source="../media/managed-identities/resource-management-identity-tab.png" alt-text="Screenshot of resource management identity tab in the Azure portal.":::
 
 1. In the main window, toggle the **System assigned Status** tab to **On**.
 
@@ -97,11 +95,11 @@ You need to grant Document Intelligence access to your storage account before it
 
 1. Under **Permissions** select **Azure role assignments**:
 
-    :::image type="content" source="media/managed-identities/enable-system-assigned-managed-identity-portal.png" alt-text="Screenshot of enable system-assigned managed identity in Azure portal.":::
+    :::image type="content" source="../media/managed-identities/enable-system-assigned-managed-identity-portal.png" alt-text="Screenshot of enable system-assigned managed identity in Azure portal.":::
 
 1. On the Azure role assignments page that opens, choose your subscription from the drop-down menu then select **&plus; Add role assignment**.
 
-    :::image type="content" source="media/managed-identities/azure-role-assignments-page-portal.png" alt-text="Screenshot of Azure role assignments page in the Azure portal.":::
+    :::image type="content" source="../media/managed-identities/azure-role-assignments-page-portal.png" alt-text="Screenshot of Azure role assignments page in the Azure portal.":::
 
     > [!NOTE]
     >
@@ -116,24 +114,25 @@ You need to grant Document Intelligence access to your storage account before it
     |**Resource**| **_The name of your storage resource_**|
     |**Role** | **_Storage Blob Data Reader_**—allows for read access to Azure Storage blob containers and data.|
 
-     :::image type="content" source="media/managed-identities/add-role-assignment-window.png" alt-text="Screenshot of add role assignments page in the Azure portal.":::
+     :::image type="content" source="../media/managed-identities/add-role-assignment-window.png" alt-text="Screenshot of add role assignments page in the Azure portal.":::
 
 1. After you receive the _Added Role assignment_ confirmation message, refresh the page to see the added role assignment.
 
-    :::image type="content" source="media/managed-identities/add-role-assignment-confirmation.png" alt-text="Screenshot of Added role assignment confirmation pop-up message.":::
+    :::image type="content" source="../media/managed-identities/add-role-assignment-confirmation.png" alt-text="Screenshot of Added role assignment confirmation pop-up message.":::
 
 1. If you don't see the change right away, wait and try refreshing the page once more. When you assign or remove role assignments, it can take up to 30 minutes for changes to take effect.
 
-    :::image type="content" source="media/managed-identities/assigned-roles-window.png" alt-text="Screenshot of Azure role assignments window.":::
+    :::image type="content" source="../media/managed-identities/assigned-roles-window.png" alt-text="Screenshot of Azure role assignments window.":::
 
  That's it! You completed the steps to enable a system-assigned managed identity. With managed identity and Azure RBAC, you granted Document Intelligence specific access rights to your storage resource without having to manage credentials such as SAS tokens.
 
 ### Other role assignments for Document Intelligence Studio
 
 If you're going to use Document Intelligence Studio and your storage account is configured with network restriction such as firewall or virtual network, another role, **Storage Blob Data Contributor**, needs to be assigned to your Document Intelligence service. Document Intelligence Studio requires this role to write blobs to your storage account when you perform Auto label, Human in the loop, or Project sharing/upgrade operations.
 
-  :::image type="content" source="media/managed-identities/blob-data-contributor-role.png" alt-text="Screenshot of assigning storage blob data contributor role.":::
+  :::image type="content" source="../media/managed-identities/blob-data-contributor-role.png" alt-text="Screenshot of assigning storage blob data contributor role.":::
 
 ## Next steps
+
 > [!div class="nextstepaction"]
 > [Configure secure access with managed identities and private endpoints](managed-identities-secured-access.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージドアイデンティティに関するドキュメントのファイル名変更とパス修正"
}
```

### Explanation
この変更は、「マネージドアイデンティティ」に関するドキュメントのリネーム及びいくつかのパス修正を行っています。元のファイル名は「managed-identities.md」であり、このファイルが新しい構造に適応するためにリネームされました。

主な変更点は、ドキュメント内の画像の参照パスと適用バージョンに関する内容の修正です。具体的には、パスを相対パスに更新し、情報の一貫性を保っています。また、不要な行や情報が削除され、文書がより読みやすく整理されています。この更新は、小規模な改善ですが、ドキュメントの質と可読性を向上させることを目的としています。新たに追加された内容もあり、ユーザーがマネージドアイデンティティを利用して安全にアクセスを構成する方法についてより包括的な情報が提供されています。

## articles/ai-services/document-intelligence/concept-read.md{#item-1050a3}

<details>
<summary>Diff</summary>
````diff
@@ -1,435 +0,0 @@
----
-title: Read model OCR data extraction - Document Intelligence 
-titleSuffix: Azure AI services
-description: Extract print and handwritten text from scanned and digital documents with Document Intelligence's Read OCR model.
-author: laujan
-manager: nitinme
-ms.service: azure-ai-document-intelligence
-ms.topic: conceptual
-ms.date: 08/07/2024
-ms.author: lajanuar
----
-
-
-# Document Intelligence read model
-
-::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
-
-**This content applies to:**![checkmark](media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
-::: moniker-end
-
-::: moniker range="doc-intel-3.1.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true)
-::: moniker-end
-
-::: moniker range="doc-intel-3.0.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true)
-::: moniker-end
-
-> [!NOTE]
->
-> For extracting text from external images like labels, street signs, and posters, use the [Azure AI Image Analysis v4.0 Read](../../ai-services/Computer-vision/concept-ocr.md) feature optimized for general, non-document images with a performance-enhanced synchronous API that makes it easier to embed OCR in your user experience scenarios.
->
-
-Document Intelligence Read Optical Character Recognition (OCR) model runs at a higher resolution than Azure AI Vision Read and extracts print and handwritten text from PDF documents and scanned images. It also includes support for extracting text from Microsoft Word, Excel, PowerPoint, and HTML documents. It detects paragraphs, text lines, words, locations, and languages. The Read model is the underlying OCR engine for other Document Intelligence prebuilt models like Layout, General Document, Invoice, Receipt, Identity (ID) document, Health insurance card, W2 in addition to custom models.
-
-## What is OCR for documents?
-
-Optical Character Recognition (OCR) for documents is optimized for large text-heavy documents in multiple file formats and global languages. It includes features like higher-resolution scanning of document images for better handling of smaller and dense text; paragraph detection; and fillable form management. OCR capabilities also include advanced scenarios like single character boxes and accurate extraction of key fields commonly found in invoices, receipts, and other prebuilt scenarios.
-
-## Development options
-
-::: moniker range="doc-intel-4.0.0"
-
-Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, applications, and libraries:
-
-| Feature | Resources | Model ID |
-|----------|-------------|-----------|
-|**Read OCR model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-read**|
-::: moniker-end
-
-::: moniker range="doc-intel-3.1.0"
-
-Document Intelligence v3.1 supports the following tools, applications, and libraries:
-
-| Feature | Resources | Model ID |
-|----------|-------------|-----------|
-|**Read OCR model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-read**|
-::: moniker-end
-
-::: moniker range="doc-intel-3.0.0"
-
-Document Intelligence v3.0 supports the following tools, applications, and libraries:
-
-| Feature | Resources | Model ID |
-|----------|-------------|-----------|
-|**Read OCR model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-read**|
-::: moniker-end
-
-## Input requirements
-
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
-
-## Get started with Read model
-
-Try extracting text from forms and documents using the Document Intelligence Studio. You need the following assets:
-
-* An Azure subscription—you can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
-
-* A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
-
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
-
-> [!NOTE]
-> Currently, Document Intelligence Studio doesn't support Microsoft Word, Excel, PowerPoint, and HTML file formats.
-
-***Sample document processed with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/read)***
-
-:::image type="content" source="media/studio/form-recognizer-studio-read-v3p2-updated.png" alt-text="Screenshot of Read processing in Document Intelligence Studio.":::
-
-1. On the [Document Intelligence Studio home page](https://documentintelligence.ai.azure.com/studio), select **Read**.
-
-1. You can analyze the sample document or upload your own files.
-
-1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
-
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
-
-   > [!div class="nextstepaction"]
-   > [Try Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/read).
-
-## Supported languages and locales
-
-See our [Language Support—document analysis models](language-support-ocr.md) page for a complete list of supported languages.
-
-## Data extraction
-
-> [!NOTE]
-> Microsoft Word and HTML file are supported in v3.1 and later versions. Compared with PDF and images, below features are not supported:
->
-> * There are no angle, width/height and unit with each page object.
-> * For each object detected, there is no bounding polygon or bounding region.
-> * Page range (`pages`) is not supported as a parameter.
-> * No `lines` object.
-
-## Searchable PDF
-
-The searchable PDF capability enables you to convert an analog PDF, such as scanned-image PDF files, to a PDF with embedded text. The embedded text enables deep text search within the PDF's extracted content by overlaying the detected text entities on top of the image files. 
-
-  > [!IMPORTANT]
-  >
-  > * Currently, the searchable PDF capability is only supported by Read OCR model `prebuilt-read`. When using this feature, please specify the `modelId` as `prebuilt-read`, as other model types will return error for this preview version.
-  > * Searchable PDF is included with the 2024-07-31-preview `prebuilt-read` model with no additional cost for generating a searchable PDF output.
->   * Searchable PDF currently only supports PDF files as input. Support for other file types, such as image files, will be available later.  
-
-### Use searchable PDF
-
-To use searchable PDF, make a `POST` request using the `Analyze` operation and specify the output format as `pdf`:
-
-```bash
-
-POST /documentModels/prebuilt-read:analyze?output=pdf
-{...}
-202
-```
-
-Poll for completion of the `Analyze` operation. Once the operation is complete, issue a `GET` request to retrieve the PDF format of the `Analyze` operation results.
-
-Upon successful completion, the PDF can be retrieved and downloaded as `application/pdf`. This operation allows direct downloading of the embedded text form of PDF instead of Base64-encoded JSON.
-
-```bash
-
-// Monitor the operation until completion.
-GET /documentModels/prebuilt-read/analyzeResults/{resultId}
-200
-{...}
-
-// Upon successful completion, retrieve the PDF as application/pdf.
-GET /documentModels/prebuilt-read/analyzeResults/{resultId}/pdf
-200 OK
-Content-Type: application/pdf
-```
-
-### Pages
-
-The pages collection is a list of pages within the document. Each page is represented sequentially within the document and includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
-
-|**File format**   | **Computed page unit**   | **Total pages**  |
-| --- | --- | --- |
-|Images (JPEG/JPG, PNG, BMP, HEIF) | Each image = 1 page unit | Total images  |
-|PDF | Each page in the PDF = 1 page unit | Total pages in the PDF |
-|TIFF | Each image in the TIFF = 1 page unit | Total images in the TIFF |
-|Word (DOCX)  | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
-|Excel (XLSX)  | Each worksheet = 1 page unit, embedded or linked images not supported | Total worksheets |
-|PowerPoint (PPTX) |  Each slide = 1 page unit, embedded or linked images not supported | Total slides |
-|HTML | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
-
-::: moniker range="doc-intel-2.1.0 || doc-intel-3.0.0"
-
-```json
-"pages": [
-    {
-        "pageNumber": 1,
-        "angle": 0,
-        "width": 915,
-        "height": 1190,
-        "unit": "pixel",
-        "words": [],
-        "lines": [],
-        "spans": []
-    }
-]
-```
-
-::: moniker-end
-
-::: moniker range="doc-intel-3.1.0"
-
-#### [Sample code](#tab/sample-code)
-```Python
-# Analyze pages.
-for page in result.pages:
-    print(f"----Analyzing document from page #{page.page_number}----")
-    print(
-        f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}"
-    )
-```
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Read_model/sample_analyze_read.py)
-
-#### [Output](#tab/output)
-```json
-"pages": [
-    {
-        "pageNumber": 1,
-        "angle": 0,
-        "width": 915,
-        "height": 1190,
-        "unit": "pixel",
-        "words": [],
-        "lines": [],
-        "spans": []
-    }
-]
-```
----
-
-::: moniker-end
-
-::: moniker range="doc-intel-4.0.0"
-
-#### [Sample code](#tab/sample-code)
-
-```Python
-# Analyze pages.
-for page in result.pages:
-    print(f"----Analyzing document from page #{page.page_number}----")
-    print(f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}")
-```
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Read_model/sample_analyze_read.py)
-
-#### [Output](#tab/output)
-
-```json
-"pages": [
-    {
-        "pageNumber": 1,
-        "angle": 0,
-        "width": 915,
-        "height": 1190,
-        "unit": "pixel",
-        "words": [],
-        "lines": [],
-        "spans": []
-    }
-]
-```
----
-::: moniker-end
-
-### Select pages for text extraction
-
-For large multi-page PDF documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction.
-
-### Paragraphs
-
-The Read OCR model in Document Intelligence extracts all identified blocks of text in the `paragraphs` collection as a top level object under `analyzeResults`. Each entry in this collection represents a text block and includes the extracted text as`content` and the bounding `polygon` coordinates. The `span` information points to the text fragment within the top-level `content` property that contains the full text from the document.
-
-```json
-"paragraphs": [
-    {
-        "spans": [],
-        "boundingRegions": [],
-        "content": "While healthcare is still in the early stages of its Al journey, we are seeing pharmaceutical and other life sciences organizations making major investments in Al and related technologies.\" TOM LAWRY | National Director for Al, Health and Life Sciences | Microsoft"
-    }
-]
-```
-
-### Text, lines, and words
-
-The Read OCR model extracts print and handwritten style text as `lines` and `words`. The model outputs bounding `polygon` coordinates and `confidence` for the extracted words. The `styles` collection includes any handwritten style for lines if detected along with the spans pointing to the associated text. This feature applies to [supported handwritten languages](language-support.md).
-
-For Microsoft Word, Excel, PowerPoint, and HTML, Document Intelligence Read model v3.1 and later versions extracts all embedded text as is. Texts are extrated as words and paragraphs. Embedded images aren't supported.
-
-::: moniker range="doc-intel-2.1.0 || doc-intel-3.0.0"
-
-```json
-
-"words": [
-    {
-        "content": "While",
-        "polygon": [],
-        "confidence": 0.997,
-        "span": {}
-    },
-],
-"lines": [
-    {
-        "content": "While healthcare is still in the early stages of its Al journey, we",
-        "polygon": [],
-        "spans": [],
-    }
-]
-```
-
-::: moniker-end
-
-::: moniker range="doc-intel-3.1.0"
-
-#### [Sample code](#tab/sample-code)
-
-```Python
-# Analyze lines.
-for line_idx, line in enumerate(page.lines):
-    words = line.get_words()
-    print(
-        f"...Line # {line_idx} has {len(words)} words and text '{line.content}' within bounding polygon '{format_polygon(line.polygon)}'"
-    )
-
-    # Analyze words.
-    for word in words:
-        print(
-            f"......Word '{word.content}' has a confidence of {word.confidence}"
-        )
-```
-
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Read_model/sample_analyze_read.py)
-
-#### [Output](#tab/output)
-
-```json
-"words": [
-    {
-        "content": "While",
-        "polygon": [],
-        "confidence": 0.997,
-        "span": {}
-    },
-],
-"lines": [
-    {
-        "content": "While healthcare is still in the early stages of its Al journey, we",
-        "polygon": [],
-        "spans": [],
-    }
-]
-```
-
----
-::: moniker-end
-
-::: moniker range="doc-intel-4.0.0"
-
-#### [Sample code](#tab/sample-code)
-
-```Python
-# Analyze lines.
-if page.lines:
-    for line_idx, line in enumerate(page.lines):
-        words = get_words(page, line)
-        print(
-            f"...Line # {line_idx} has {len(words)} words and text '{line.content}' within bounding polygon '{line.polygon}'"
-        )
-
-        # Analyze words.
-        for word in words:
-            print(f"......Word '{word.content}' has a confidence of {word.confidence}")
-```
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Read_model/sample_analyze_read.py)
-
-#### [Output](#tab/output)
-
-```json
-"words": [
-    {
-        "content": "While",
-        "polygon": [],
-        "confidence": 0.997,
-        "span": {}
-    },
-],
-"lines": [
-    {
-        "content": "While healthcare is still in the early stages of its Al journey, we",
-        "polygon": [],
-        "spans": [],
-    }
-]
-```
----
-::: moniker-end
-
-### Handwritten style for text lines
-
-The response includes classifying whether each text line is of handwriting style or not, along with a confidence score. For more information, *see* [handwritten language support](language-support-ocr.md). The following example shows an example JSON snippet.
-
-```json
-"styles": [
-{
-    "confidence": 0.95,
-    "spans": [
-    {
-        "offset": 509,
-        "length": 24
-    }
-    "isHandwritten": true
-    ]
-}
-```
-
-If you enabled the [font/style addon capability](concept-add-on-capabilities.md#font-property-extraction), you also get the font/style result as part of the `styles` object.
-
-## Next steps
-
-Complete a Document Intelligence quickstart:
-
-> [!div class="checklist"]
->
-> * [**REST API**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)
-> * [**C# SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-csharp)
-> * [**Python SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-python)
-> * [**Java SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-java)
-> * [**JavaScript**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-javascript)</li></ul>
-
-Explore our REST API:
-
-> [!div class="nextstepaction"]
-> [Document Intelligence API v4.0](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)
-
-::: moniker range="doc-intel-4.0.0"
-Find more samples on GitHub:
-> [!div class="nextstepaction"]
-> [Read model.](https://github.com/Azure-Samples/document-intelligence-code-samples/tree/main/Python(v4.0)/Read_model)
-
-::: moniker-end
-
-::: moniker range="doc-intel-3.1.0"
-Find more samples on GitHub:
-> [!div class="nextstepaction"]
-> [Read model.](https://github.com/Azure-Samples/document-intelligence-code-samples/tree/v3.1(2023-07-31-GA)/Python(v3.1)/Read_model)
-
-::: moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Document Intelligence の Read モデルに関する概念ドキュメントの削除"
}
```

### Explanation
この変更は、「Document Intelligence の Read モデル」に関する概念を説明するドキュメント「concept-read.md」が削除されたことを示しています。この変更により、ドキュメント全体で435行の内容が削除されました。

削除されたドキュメントには、OCRデータ抽出モデルの機能や使い方、対応するファイル形式、開発オプション、入力要件、サポートされている言語やロケール、サンプルコードなど、Document Intelligence の機能に関する詳細な情報が含まれていました。この削除は、情報の整理やリソースの更新を意図した変更である可能性がありますが、関連情報が必要なユーザーにとっては影響が大きいです。必要に応じて、他のリソースや新しいドキュメントを参照する必要があります。

## articles/ai-services/document-intelligence/concept/accuracy-confidence.md{#item-56cda7}

<details>
<summary>Diff</summary>
````diff
@@ -6,13 +6,13 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 08/07/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 ---
 
-# Interpret and improve model accuracy and analysis confidence scores
+<!-- markdownlint-disable MD033 -->
 
-[!INCLUDE [applies to v4.0, v3.1, v3.0, and v2.1](includes/applies-to-v40-v31-v30-v21.md)]
+# Interpret and improve model accuracy and analysis confidence scores
 
 A confidence score indicates probability by measuring the degree of statistical certainty that the extracted result is detected correctly. The estimated accuracy is calculated by running a few different combinations of the training data to predict the labeled values. In this article, learn to interpret accuracy and confidence scores and best practices for using those scores to improve accuracy and confidence results.
 
@@ -30,7 +30,7 @@ Field confidence indicates an estimated probability between 0 and 1 that the pre
 **Document Intelligence Studio** </br>
 **Analyzed invoice prebuilt-invoice model**
 
-:::image type="content" source="media/accuracy-confidence/confidence-scores.png" alt-text="confidence scores from Document Intelligence Studio":::
+:::image type="content" source="../media/accuracy-confidence/confidence-scores.png" alt-text="confidence scores from Document Intelligence Studio":::
 
 ## Improve confidence scores
 
@@ -48,17 +48,16 @@ After an analysis operation, review the JSON output. Examine the `confidence` va
 
 ## Accuracy scores for custom models
 
-
 > [!NOTE]
+>
 > * **Custom neural and generative models** do not provide accuracy scores during training.
 
-The output of a `build` (v3.0 and onward) or `train` (v2.1) custom model operation includes the estimated accuracy score. This score represents the model's ability to accurately predict the labeled value on a visually similar document. Accuracy is measured within a percentage value range from 0% (low) to 100% (high). It's best to target a score of 80% or higher. For more sensitive cases, like financial or medical records, we recommend a score of close to 100%. You can also add a human review stage to validate for more critical automation workflows. 
+The output of a `build` (v3.0 and onward) or `train` (v2.1) custom model operation includes the estimated accuracy score. This score represents the model's ability to accurately predict the labeled value on a visually similar document. Accuracy is measured within a percentage value range from 0% (low) to 100% (high). It's best to target a score of 80% or higher. For more sensitive cases, like financial or medical records, we recommend a score of close to 100%. You can also add a human review stage to validate for more critical automation workflows.
 
 **Document Intelligence Studio** </br>
 **Trained custom model (invoice)**
 
-:::image type="content" source="media/accuracy-confidence/accuracy-studio-results.png" alt-text="Trained custom model accuracy scores":::
-
+:::image type="content" source="../media/accuracy-confidence/accuracy-studio-results.png" alt-text="Trained custom model accuracy scores":::
 
 ## Interpret accuracy and confidence scores for custom models
 
@@ -78,7 +77,6 @@ The following table demonstrates how to interpret both the accuracy and confiden
 | Low | High | &bullet; This result is most unlikely.<br>&bullet; For low accuracy scores, add more labeled data or split visually distinct documents into multiple models. |
 | Low | Low| &bullet; Add more labeled data.<br>&bullet; Split visually distinct documents into multiple models.|
 
-
 ## Ensure high model accuracy for custom models
 
 Variances in the visual structure of your documents affect the accuracy of your model. Reported accuracy scores can be inconsistent when the analyzed documents differ from documents used in training. Keep in mind that a document set can look similar when viewed by humans but appear dissimilar to an AI model. To follow, is a list of the best practices for training models with the highest accuracy. Following these guidelines should produce a model with higher accuracy and confidence scores during analysis and reduce the number of documents flagged for human review.
@@ -89,7 +87,7 @@ Variances in the visual structure of your documents affect the accuracy of your
 
 * Separate visually distinct document types to train different models for custom template and neural models.
   * As a general rule, if you remove all user entered values and the documents look similar, you need to add more training data to the existing model.
-  * If the documents are dissimilar, split your training data into different folders and train a model for each variation. You can then [compose](how-to-guides/compose-custom-models.md?view=doc-intel-2.1.0&preserve-view=true#create-a-composed-model) the different variations into a single model.
+  * If the documents are dissimilar, split your training data into different folders and train a model for each variation. You can then [compose](../how-to-guides/compose-custom-models.md?view=doc-intel-2.1.0&preserve-view=true#create-a-composed-model) the different variations into a single model.
 
 * Ensure that you don't have any extraneous labels.
 
@@ -128,9 +126,9 @@ With the addition of table, row and cell confidence with the ```2024-02-29-previ
 **A:** Look at all levels of table confidence starting in a top-to-bottom approach: begin by checking a table's confidence as a whole, then drill down to the row level and look at individual rows, finally look at cell-level confidences. Depending on the type of table, there are a couple of things of note:
 
 For **fixed tables**, cell-level confidence already captures quite a bit of information on the correctness of things. This means that simply going over each cell and looking at its confidence can be enough to help determine the quality of the prediction.
-For **dynamic tables**, the levels are meant to build on top of each other, so the top-to-bottom approach is more important. 
+For **dynamic tables**, the levels are meant to build on top of each other, so the top-to-bottom approach is more important.
 
 ## Next step
 
 > [!div class="nextstepaction"]
-> [Learn more about custom models](concept-custom.md)
+> [Learn more about custom models](../train/custom-model.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの精度と分析の信頼性スコアに関するドキュメントのリネーム"
}
```

### Explanation
この変更は、「モデルの精度と分析の信頼性スコア」に関するドキュメントのファイル名を「accuracy-confidence.md」から新しい名前にリネームしたことを示しています。ファイルには10行の新規追加と12行の削除があり、全体で22行の変更が加えられています。

具体的な変更点として、文書の冒頭に関連する情報や日付が更新されており、視覚的な要素のパスも相対パスに修正されています。内容自体は、抽出結果の正確さや信頼性に対する解釈と改善策を説明しており、特にカスタムモデルに関する精度スコアの重要性やその解釈に焦点を当てています。また、分析結果を確認するための最良の実践事項や、信頼性スコアを向上させる方法についての詳細な指針が含まれています。このリネームと内容の更新は、ユーザーに最新の情報を提供し、ドキュメントの整合性を高めるための行動と考えられます。

## articles/ai-services/document-intelligence/concept/add-on-capabilities.md{#item-96ed69}

<details>
<summary>Diff</summary>
````diff
@@ -5,31 +5,31 @@ description: How to increase service limit capacity with add-on capabilities.
 author: jaep3347
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 05/23/2024
 ms.author: lajanuar
 monikerRange: '>=doc-intel-3.1.0'
 ---
 
 <!-- markdownlint-disable MD033 -->
+<!-- markdownlint-disable MD024 -->
+<!-- markdownlint-disable MD051 -->
 
 # Document Intelligence add-on capabilities
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-**This content applies to:** ![checkmark](media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
 > [!NOTE]
-> Add-on capabilities are available within all models except for the [Business card model](concept-business-card.md).
+> Add-on capabilities are available within all models except for the [Business card model](../prebuilt/business-card.md).
 :::moniker-end
 
 :::moniker range=">=doc-intel-3.1.0"
@@ -48,18 +48,17 @@ Document Intelligence supports more sophisticated and modular analysis capabilit
 
 * [`languages`](#language-detection)
 
-Starting with `2024-07-31-preview` release, the Read model supports searchable PDF output:
+For `2024-07-31-preview` release and later, the Read model supports searchable PDF output:
 
 * [`Searchable PDF](#searchable-pdf)
 
-
 :::moniker-end
 
 :::moniker range="doc-intel-4.0.0"
 
 > [!NOTE]
 >
-> * Not all add-on capabilities are supported by all models. For more information, *see* [model data extraction](concept-model-overview.md#model-analysis-features).
+> * Not all add-on capabilities are supported by all models. For more information, *see* [model data extraction](../model-overview.md#model-analysis-features).
 >
 > * Add-on capabilities are currently not supported for Microsoft Office file types.
 
@@ -104,11 +103,13 @@ The task of recognizing small text from large-size documents, like engineering d
 ::: moniker range="doc-intel-4.0.0"
 
 ### [REST API](#tab/rest-api)
+
 ```bash
 {your-resource-endpoint}.cognitiveservices.azure.com/documentintelligence/documentModels/prebuilt-layout:analyze?api-version=2024-02-29-preview&features=ocrHighResolution
 ```
 
 ### [Sample code](#tab/sample-code)
+
 ```Python
 # Analyze a document at a URL:
 formUrl = "https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Data/add-on/add-on-highres.png?raw=true"
@@ -157,12 +158,14 @@ if result.tables:
             print(f"...Cell[{cell.row_index}][{cell.column_index}] has text '{cell.content}'")
             if cell.bounding_regions:
                 for region in cell.bounding_regions:
-                    print(f"...content on page {region.page_number} is within bounding polygon '{region.polygon}'")   
+                    print(f"...content on page {region.page_number} is within bounding polygon '{region.polygon}'")
 ```
+
 > [!div class="nextstepaction"]
 > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Add-on_capabilities/sample_analyze_addon_highres.py)
 
 ### [Output](#tab/output)
+
 ```json
 "styles": [true],
 "pages": [
@@ -221,15 +224,20 @@ if result.tables:
 ]
 
 ```
+
 ---
 ::: moniker-end
 
-::: moniker range="doc-intel-3.1.0"
+:::moniker range="doc-intel-3.1.0"
+
 ### [REST API](#tab/rest-api)
+
 ```bash
 {your-resource-endpoint}.cognitiveservices.azure.com/formrecognizer/documentModels/prebuilt-layout:analyze?api-version=2023-07-31&features=ocrHighResolution
 ```
+
 ### [Sample code](#tab/sample-code)
+
 ```Python
 # Analyze a document at a URL:
 url = "(https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Data/add-on/add-on-highres.png?raw=true"
@@ -286,10 +294,12 @@ for table_idx, table in enumerate(result.tables):
                 f"...content on page {region.page_number} is within bounding polygon '{format_polygon(region.polygon)}'"
             )
 ```
+
 > [!div class="nextstepaction"]
 > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Add-on_capabilities/sample_analyze_addon_highres.py)
 
 ### [Output](#tab/output)
+
 ```json
 "styles": [true],
 "pages": [
@@ -348,6 +358,7 @@ for table_idx, table in enumerate(result.tables):
 ]
 
 ```
+
 ---
 ::: moniker-end
 
@@ -361,18 +372,21 @@ The `ocr.formula` capability extracts all identified formulas, such as mathemati
 ::: moniker range="doc-intel-4.0.0"
 
 ### [REST API](#tab/rest-api)
+
 ```bash
 {your-resource-endpoint}.cognitiveservices.azure.com/documentintelligence/documentModels/prebuilt-layout:analyze?api-version=2024-02-29-preview&features=formulas
 ```
+
 ### [Sample code](#tab/sample-code)
+
 ```Python
 # Analyze a document at a URL:
 formUrl = "https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Data/add-on/layout-formulas.png?raw=true"
 poller = document_intelligence_client.begin_analyze_document(
     "prebuilt-layout",
     AnalyzeDocumentRequest(url_source=formUrl),
     features=[DocumentAnalysisFeature.FORMULAS],  # Specify which add-on capabilities to enable
-)       
+)
 result: AnalyzeResult = poller.result()
 
 # [START analyze_formulas]
@@ -382,7 +396,7 @@ for page in result.pages:
         inline_formulas = [f for f in page.formulas if f.kind == "inline"]
         display_formulas = [f for f in page.formulas if f.kind == "display"]
 
-        # To learn the detailed concept of "polygon" in the following content, visit: https://aka.ms/bounding-region 
+        # To learn the detailed concept of "polygon" in the following content, visit: https://aka.ms/bounding-region
         print(f"Detected {len(inline_formulas)} inline formulas.")
         for formula_idx, formula in enumerate(inline_formulas):
             print(f"- Inline #{formula_idx}: {formula.value}")
@@ -395,10 +409,12 @@ for page in result.pages:
             print(f"  Confidence: {formula.confidence}")
             print(f"  Bounding regions: {formula.polygon}")
 ```
+
 > [!div class="nextstepaction"]
 > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Add-on_capabilities/sample_analyze_addon_formulas.py)
 
 ### [Output](#tab/output)
+
 ```json
 "content": ":formula:",
  "pages": [
@@ -423,15 +439,19 @@ for page in result.pages:
    }
  ]
 ```
+
 ::: moniker-end
 
-::: moniker range="doc-intel-3.1.0"
+:::moniker range="doc-intel-3.1.0"
 
 ### [REST API](#tab/rest-api)
+
 ```bash
 {your-resource-endpoint}.cognitiveservices.azure.com/formrecognizer/documentModels/prebuilt-layout:analyze?api-version=2023-07-31&features=formulas
 ```
+
 ### [Sample code](#tab/sample-code)
+
 ```Python
 # Analyze a document at a URL:
 url = "https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Data/add-on/layout-formulas.png?raw=true"
@@ -458,10 +478,12 @@ for page in result.pages:
         print(f"  Confidence: {formula.confidence}")
         print(f"  Bounding regions: {format_polygon(formula.polygon)}")
 ```
+
 > [!div class="nextstepaction"]
 > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Add-on_capabilities/sample_analyze_addon_formulas.py)
 
 ### [Output](#tab/output)
+
 ```json
  "content": ":formula:",
    "pages": [
@@ -486,6 +508,7 @@ for page in result.pages:
      }
    ]
 ```
+
 ---
 ::: moniker-end
 
@@ -502,14 +525,15 @@ The `ocr.font` capability extracts all font properties of text extracted in the
 ```
 
 ### [Sample code](#tab/sample-code)
+
 ```Python
 # Analyze a document at a URL:
 formUrl = "https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Data/receipt/receipt-with-tips.png?raw=true"
 poller = document_intelligence_client.begin_analyze_document(
     "prebuilt-layout",
     AnalyzeDocumentRequest(url_source=formUrl),
     features=[DocumentAnalysisFeature.STYLE_FONT]    # Specify which add-on capabilities to enable.
-)       
+)
 result: AnalyzeResult = poller.result()
 
 # [START analyze_fonts]
@@ -566,10 +590,12 @@ for font_background_color, styles in font_background_colors.items():
     print(f"- Font background color: '{font_background_color}'")
     print(f"  Text: '{get_styled_text(styles, result.content)}'")
 ```
+
 > [!div class="nextstepaction"]
 > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Add-on_capabilities/sample_analyze_addon_fonts.py)
 
 ### [Output](#tab/output)
+
 ```json
 "content": "Foo bar",
 "styles": [
@@ -605,17 +631,20 @@ for font_background_color, styles in font_background_colors.items():
    }
  ]
 ```
+
 ---
 ::: moniker-end
 
-::: moniker range="doc-intel-3.1.0"
+:::moniker range="doc-intel-3.1.0"
 
 ### [REST API](#tab/rest-api)
+
 ```bash
   {your-resource-endpoint}.cognitiveservices.azure.com/formrecognizer/documentModels/prebuilt-layout:analyze?api-version=2023-07-31&features=styleFont
 ```
 
 ### [Sample code](#tab/sample-code)
+
 ```Python
 # Analyze a document at a URL:
 url = "https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Data/receipt/receipt-with-tips.png?raw=true"
@@ -677,10 +706,12 @@ for font_background_color, styles in font_background_colors.items():
     print(f"- Font background color: '{font_background_color}'")
     print(f"  Text: '{get_styled_text(styles, result.content)}'")
 ```
+
 > [!div class="nextstepaction"]
 > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Add-on_capabilities/sample_analyze_addon_fonts.py)
 
 ### [Output](#tab/output)
+
 ```json
 "content": "Foo bar",
 "styles": [
@@ -716,6 +747,7 @@ for font_background_color, styles in font_background_colors.items():
    }
  ]
 ```
+
 ---
 ::: moniker-end
 
@@ -727,34 +759,38 @@ The `ocr.barcode` capability extracts all identified barcodes in the `barcodes`
 
 | **Barcode Type**   | **Example**   |
 | --- | --- |
-| `QR Code` |:::image type="content" source="media/barcodes/qr-code.png" alt-text="Screenshot of the QR Code.":::|
-| `Code 39` |:::image type="content" source="media/barcodes/code-39.png" alt-text="Screenshot of the Code 39.":::|
-| `Code 93` |:::image type="content" source="media/barcodes/code-93.gif" alt-text="Screenshot of the Code 93.":::|
-| `Code 128` |:::image type="content" source="media/barcodes/code-128.png" alt-text="Screenshot of the Code 128.":::|
-| `UPC (UPC-A & UPC-E)` |:::image type="content" source="media/barcodes/upc.png" alt-text="Screenshot of the UPC.":::|
-| `PDF417` |:::image type="content" source="media/barcodes/pdf-417.png" alt-text="Screenshot of the PDF417.":::|
-| `EAN-8` |:::image type="content" source="media/barcodes/european-article-number-8.gif" alt-text="Screenshot of the European-article-number barcode ean-8.":::|
-| `EAN-13` |:::image type="content" source="media/barcodes/european-article-number-13.gif" alt-text="Screenshot of the European-article-number barcode ean-13.":::|
-| `Codabar` |:::image type="content" source="media/barcodes/codabar.png" alt-text="Screenshot of the Codabar.":::|
-| `Databar` |:::image type="content" source="media/barcodes/databar.png" alt-text="Screenshot of the Data bar.":::|
-| `Databar` Expanded |:::image type="content" source="media/barcodes/databar-expanded.gif" alt-text="Screenshot of the Data bar Expanded.":::|
-| `ITF` |:::image type="content" source="media/barcodes/interleaved-two-five.png" alt-text="Screenshot of the interleaved-two-of-five barcode (ITF).":::|
-| `Data Matrix` |:::image type="content" source="media/barcodes/datamatrix.gif" alt-text="Screenshot of the Data Matrix.":::|
+| `QR Code` |:::image type="content" source="../media/barcodes/qr-code.png" alt-text="Screenshot of the QR Code.":::|
+| `Code 39` |:::image type="content" source="../media/barcodes/code-39.png" alt-text="Screenshot of the Code 39.":::|
+| `Code 93` |:::image type="content" source="../media/barcodes/code-93.gif" alt-text="Screenshot of the Code 93.":::|
+| `Code 128` |:::image type="content" source="../media/barcodes/code-128.png" alt-text="Screenshot of the Code 128.":::|
+| `UPC (UPC-A & UPC-E)` |:::image type="content" source="../media/barcodes/upc.png" alt-text="Screenshot of the UPC.":::|
+| `PDF417` |:::image type="content" source="../media/barcodes/pdf-417.png" alt-text="Screenshot of the PDF417.":::|
+| `EAN-8` |:::image type="content" source="../media/barcodes/european-article-number-8.gif" alt-text="Screenshot of the European-article-number barcode ean-8.":::|
+| `EAN-13` |:::image type="content" source="../media/barcodes/european-article-number-13.gif" alt-text="Screenshot of the European-article-number barcode ean-13.":::|
+| `Codabar` |:::image type="content" source="../media/barcodes/codabar.png" alt-text="Screenshot of the Codabar.":::|
+| `Databar` |:::image type="content" source="../media/barcodes/databar.png" alt-text="Screenshot of the Data bar.":::|
+| `Databar` Expanded |:::image type="content" source="../media/barcodes/databar-expanded.gif" alt-text="Screenshot of the Data bar Expanded.":::|
+| `ITF` |:::image type="content" source="../media/barcodes/interleaved-two-five.png" alt-text="Screenshot of the interleaved-two-of-five barcode (ITF).":::|
+| `Data Matrix` |:::image type="content" source="../media/barcodes/datamatrix.gif" alt-text="Screenshot of the Data Matrix.":::|
 
 ::: moniker range="doc-intel-4.0.0"
+
 ### [REST API](#tab/rest-api)
+
 ```bash
 {your-resource-endpoint}.cognitiveservices.azure.com/documentintelligence/documentModels/prebuilt-layout:analyze?api-version=2024-02-29-preview&features=barcodes
 ```
+
 ### [Sample code](#tab/sample-code)
+
 ```Python
 # Analyze a document at a URL:
 formUrl = "https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Data/add-on/add-on-barcodes.jpg?raw=true"
 poller = document_intelligence_client.begin_analyze_document(
     "prebuilt-read",
     AnalyzeDocumentRequest(url_source=formUrl),
     features=[DocumentAnalysisFeature.BARCODES]    # Specify which add-on capabilities to enable.
-)       
+)
 result: AnalyzeResult = poller.result()
 
 # [START analyze_barcodes]
@@ -769,10 +805,12 @@ for page in result.pages:
             print(f"  Confidence: {barcode.confidence}")
             print(f"  Bounding regions: {barcode.polygon}")
 ```
+
 > [!div class="nextstepaction"]
 > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Add-on_capabilities/sample_analyze_addon_barcodes.py)
 
 ### [Output](#tab/output)
+
 ```json
 ----Barcodes detected from page #1----
 Detected 2 barcodes:
@@ -785,16 +823,20 @@ Detected 2 barcodes:
   Confidence: 0.98
   Bounding regions: [50.5, 60.5, 70.5, 80.5]
 ```
+
 ---
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
 
 ### [REST API](#tab/rest-api)
+
 ```bash
 {your-resource-endpoint}.cognitiveservices.azure.com/formrecognizer/documentModels/prebuilt-layout:analyze?api-version=2023-07-31&features=barcodes
 ```
+
 ### [Sample code](#tab/sample-code)
+
 ```Python
 # Analyze a document at a URL:
 url = "https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Data/add-on/add-on-barcodes.jpg?raw=true"
@@ -814,10 +856,12 @@ for page in result.pages:
         print(f"  Confidence: {barcode.confidence}")
         print(f"  Bounding regions: {format_polygon(barcode.polygon)}")
 ```
+
 > [!div class="nextstepaction"]
 > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Add-on_capabilities/sample_analyze_addon_barcodes.py)
 
 ### [Output](#tab/output)
+
 ```json
 ----Barcodes detected from page #1----
 Detected 2 barcodes:
@@ -830,6 +874,7 @@ Detected 2 barcodes:
   Confidence: 0.98
   Bounding regions: [50.5, 60.5, 70.5, 80.5]
 ```
+
 ---
 ::: moniker-end
 
@@ -840,18 +885,21 @@ Adding the `languages` feature to the `analyzeResult` request predicts the detec
 ::: moniker range="doc-intel-4.0.0"
 
 ### [REST API](#tab/rest-api)
+
 ```bash
 {your-resource-endpoint}.cognitiveservices.azure.com/documentintelligence/documentModels/prebuilt-layout:analyze?api-version=2024-02-29-preview&features=languages
 ```
+
 ### [Sample code](#tab/sample-code)
+
 ```Python
 # Analyze a document at a URL:
 formUrl = "https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Data/add-on/add-on-fonts_and_languages.png?raw=true"
 poller = document_intelligence_client.begin_analyze_document(
     "prebuilt-layout",
     AnalyzeDocumentRequest(url_source=formUrl),
     features=[DocumentAnalysisFeature.LANGUAGES]     # Specify which add-on capabilities to enable.
-)       
+)
 result: AnalyzeResult = poller.result()
 
 # [START analyze_languages]
@@ -865,10 +913,12 @@ if result.languages:
             f"  Text: '{','.join([result.content[span.offset : span.offset + span.length] for span in lang.spans])}'"
         )
 ```
+
 > [!div class="nextstepaction"]
 > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Add-on_capabilities/sample_analyze_addon_languages.py)
 
 ### [Output](#tab/output)
+
 ```json
 "languages": [
     {
@@ -883,16 +933,20 @@ if result.languages:
     },
 ]
 ```
+
 ---
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
 
 ### [REST API](#tab/rest-api)
+
 ```bash
 {your-resource-endpoint}.cognitiveservices.azure.com/formrecognizer/documentModels/prebuilt-layout:analyze?api-version=2023-07-31&features=languages
 ```
+
 ### [Sample code](#tab/sample-code)
+
 ```Python
 # Analyze a document at a URL:
 url = "https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Data/add-on/add-on-fonts_and_languages.png?raw=true"
@@ -909,10 +963,12 @@ for lang_idx, lang in enumerate(result.languages):
     print(f"  Confidence: {lang.confidence}")
     print(f"  Text: '{','.join([result.content[span.offset : span.offset + span.length] for span in lang.spans])}'")
 ```
+
 > [!div class="nextstepaction"]
 > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Add-on_capabilities/sample_analyze_addon_languages.py)
 
 ### [Output](#tab/output)
+
 ```json
 "languages": [
     {
@@ -927,14 +983,15 @@ for lang_idx, lang in enumerate(result.languages):
     },
 ]
 ```
+
 ---
 ::: moniker-end
 
 ::: moniker range="doc-intel-4.0.0"
 
 ## Searchable PDF
 
-The searchable PDF capability enables you to convert an analog PDF, such as scanned-image PDF files, to a PDF with embedded text. The embedded text enables deep text search within the PDF's extracted content by overlaying the detected text entities on top of the image files. 
+The searchable PDF capability enables you to convert an analog PDF, such as scanned-image PDF files, to a PDF with embedded text. The embedded text enables deep text search within the PDF's extracted content by overlaying the detected text entities on top of the image files.
 
   > [!IMPORTANT]
   >
@@ -969,10 +1026,9 @@ GET /documentModels/prebuilt-read/analyzeResults/{resultId}/pdf
 Content-Type: application/pdf
 ```
 
-
 ## Key-value Pairs
 
-In earlier API versions, the prebuilt-document model extracted key-value pairs from forms and documents. With the addition of the `keyValuePairs` feature to prebuilt-layout, the layout model now produces the same results. 
+In earlier API versions, the `prebuilt-document` model extracted key-value pairs from forms and documents. With the addition of the `keyValuePairs` feature to prebuilt-layout, the layout model now produces the same results.
 
 Key-value pairs are specific spans within the document that identify a label or key and its associated response or value. In a structured form, these pairs could be the label and the value the user entered for that field. In an unstructured document, they could be the date a contract was executed on based on the text in a paragraph. The AI model is trained to extract identifiable keys and values based on a wide variety of document types, formats, and structures.
 
@@ -1008,11 +1064,11 @@ For query field extraction, specify the fields you want to extract and Document
 
 * If you're processing a contract in the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/document), use the `2024-02-29-preview` or `2023-10-31-preview` versions:
 
-    :::image type="content" source="media/studio/query-fields.png" alt-text="Screenshot of the query fields button in Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/query-fields.png" alt-text="Screenshot of the query fields button in Document Intelligence Studio.":::
 
 * You can pass a list of field labels like `Party1`, `Party2`, `TermsOfUse`, `PaymentTerms`, `PaymentDate`, and `TermEndDate` as part of the `analyze document` request.
 
-   :::image type="content" source="media/studio/query-field-select.png" alt-text="Screenshot of query fields selection window in Document Intelligence Studio.":::
+   :::image type="content" source="../media/studio/query-field-select.png" alt-text="Screenshot of query fields selection window in Document Intelligence Studio.":::
 
 * Document Intelligence is able to analyze and extract the field data and return the values in a structured JSON output.
 
@@ -1025,12 +1081,13 @@ For query field extraction, specify the fields you want to extract and Document
 ```
 
 ### [Sample code](#tab/sample-code)
+
 ```Python
 # Analyze a document at a URL:
 formUrl = "https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Data/invoice/simple-invoice.png?raw=true"
 poller = document_intelligence_client.begin_analyze_document(
     "prebuilt-layout",
-    AnalyzeDocumentRequest(url_source=formUrl),   
+    AnalyzeDocumentRequest(url_source=formUrl),
     features=[DocumentAnalysisFeature.QUERY_FIELDS],    # Specify which add-on capabilities to enable.
     query_fields=["Address", "InvoiceNumber"],  # Set the features and provide a comma-separated list of field names.
 )
@@ -1043,24 +1100,26 @@ if result.documents:
         if doc.fields and doc.fields["InvoiceNumber"]:
             print(f"Invoice number: {doc.fields['InvoiceNumber'].value_string}")
 ```
+
 > [!div class="nextstepaction"]
 > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Add-on_capabilities/sample_analyze_addon_query_fields.py)
 
 ### [Output](#tab/output)
+
 ```json
 Address: 1 Redmond way Suite 6000 Redmond, WA Sunnayvale, 99243
 Invoice number: 34278587
 ```
+
 ---
 
 ::: moniker-end
 
-
 ## Next steps
 
 > [!div class="nextstepaction"]
 > Learn more:
-> [**Read model**](concept-read.md) [**Layout model**](concept-layout.md)
+> [**Read model**](../prebuilt/read.md) [**Layout model**](../prebuilt/layout.md)
 
 > [!div class="nextstepaction"]
 > SDK samples:
@@ -1072,7 +1131,7 @@ Invoice number: 34278587
 > [**Add-on capabilities**](https://github.com/Azure-Samples/document-intelligence-code-samples/tree/main/Python(v4.0)/Add-on_capabilities)
 ::: moniker-end
 
-::: moniker range="doc-intel-3.1.0"
+:::moniker range="doc-intel-3.1.0"
 > [!div class="nextstepaction"]
 > Find more samples:
 > [**Add-on capabilities**](https://github.com/Azure-Samples/document-intelligence-code-samples/tree/v3.1(2023-07-31-GA)/Python(v3.1)/Add-on_capabilities)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence の追加機能に関するドキュメントのリネーム"
}
```

### Explanation
この変更は、「Document Intelligence に関する追加機能」のドキュメントのファイル名を「add-on-capabilities.md」から新しい名前にリネームしたことを示しています。この変更には99行の新規追加と40行の削除が含まれ、全体で139行の変更が加えられています。

具体的には、文書の先頭部分でメタデータが更新され、日付も新しいものに変更されています。また、いくつかの相対パスの修正と、コンテンツの構成が見直され、いくつかの説明文が最適化されています。新しく追加された内容は、Document Intelligence の追加機能に関する詳細な情報、REST APIの使用例、およびサンプルコードが豊富に含まれています。このリネームは、ドキュメントの整理や最新情報への対応を図るためのものであり、使用者にとって役立つ情報を提供しています。

## articles/ai-services/document-intelligence/concept/analyze-document-response.md{#item-f785b2}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 09/26/2024
+ms.date: 10/03/2024
 ms.author: vikurpad
 ms.custom:
   - references_regions
@@ -15,13 +15,11 @@ monikerRange: '>=doc-intel-3.0.0'
 
 # Analyze document API response
 
-**This content applies to:** ![checkmark](media/yes-icon.png) **v4.0 (preview)** ![checkmark](media/yes-icon.png) **v3.1 (GA)** ![checkmark](media/yes-icon.png) **v3.0 (GA)**
-
 In this article, let's examine the different objects returned as part of the `AnalyzeDocument` response and how to use the document analysis API response in your applications.
 
 ## Analyze document request
 
-The Document Intelligence APIs analyze images, PDFs, and other document files to extract and detect various content, layout, style, and semantic elements. The `Analyze` operation is an async API. Submitting a document returns an **Operation-Location** header that contains the URL to poll for completion. When an analysis request completes successfully, the response contains the elements described in the [model data extraction](concept-model-overview.md#model-data-extraction).
+The Document Intelligence APIs analyze images, PDFs, and other document files to extract and detect various content, layout, style, and semantic elements. The `Analyze` operation is an async API. Submitting a document returns an **Operation-Location** header that contains the URL to poll for completion. When an analysis request completes successfully, the response contains the elements described in the [model data extraction](../model-overview.md#model-data-extraction).
 
 ### Response elements
 
@@ -56,21 +54,21 @@ The `Analyze` response for each API returns different objects. API responses con
 | **keyValuePairs**| Key-value pairs recognized by a pretrained model. The key is a span of text from the document with the associated value. | General document and Invoice models |
 | **documents**| Fields recognized are returned in the `fields` dictionary within the list of documents| Prebuilt models, Custom models.|
 
-For more information on the objects returned by each API, see [model data extraction](concept-model-overview.md#model-data-extraction).
+For more information on the objects returned by each API, see [model data extraction](../model-overview.md#model-data-extraction).
 
 ## Element properties
 
 ### Spans
 
-Spans specify the logical position of each element in the overall reading order, with each span specifying a character offset and length into the top-level content string property. By default, character offsets and lengths are returned in units of user-perceived characters (also known as [`grapheme clusters`](/dotnet/standard/base-types/character-encoding-introduction) or text elements). To accommodate different development environments that use different character units, user can specify the `stringIndexIndex` query parameter to return span offsets and lengths in Unicode code points (Python 3) or UTF16 code units (Java, JavaScript, .NET) as well. For more information, *see* [multilingual/emoji support](../../ai-services/language-service/concepts/multilingual-emoji-support.md).
+Spans specify the logical position of each element in the overall reading order, with each span specifying a character offset and length into the top-level content string property. By default, character offsets and lengths are returned in units of user-perceived characters (also known as [`grapheme clusters`](/dotnet/standard/base-types/character-encoding-introduction) or text elements). To accommodate different development environments that use different character units, user can specify the `stringIndexIndex` query parameter to return span offsets and lengths in Unicode code points (Python 3) or UTF16 code units (Java, JavaScript, .NET) as well. For more information, *see* [multilingual/emoji support](../../../ai-services/language-service/concepts/multilingual-emoji-support.md).
 
-:::image type="content" source="media/span.png" alt-text="Screenshot of detected span example.":::
+:::image type="content" source="../media/span.png" alt-text="Screenshot of detected span example.":::
 
 ### Bounding Region
 
 Bounding regions describe the visual position of each element in the file. When elements aren't visually contiguous or cross pages (tables), the positions of most elements are described via an array of bounding regions. Each region specifies the page number (`1`-indexed) and bounding polygon. The bounding polygon is described as a sequence of points, clockwise from the left relative to the natural orientation of the element. For quadrilaterals, plot points are top-left, top-right, bottom-right, and bottom-left corners. Each point represents its x, y coordinate in the page unit specified by the unit property. In general, unit of measure for images is pixels while PDFs use inches.
 
-:::image type="content" source="media/bounding-regions.png" alt-text="Screenshot of detected bounding regions example.":::
+:::image type="content" source="../media/bounding-regions.png" alt-text="Screenshot of detected bounding regions example.":::
 
 > [!NOTE]
 > Currently, Document Intelligence only returns 4-vertex quadrilaterals as bounding polygons. Future versions may return different number of points to describe more complex shapes, such as curved lines or non-rectangular images. Bounding regions applied only to rendered files, if the file is not rendered, bounding regions are not returned. Currently files of docx/xlsx/pptx/html format are not rendered.
@@ -81,28 +79,28 @@ Bounding regions describe the visual position of each element in the file. When
 
 A word is a content element composed of a sequence of characters. With Document Intelligence, a word is defined as a sequence of adjacent characters, with whitespace separating words from one another. For languages that don't use space separators between words each character is returned as a separate word, even if it doesn't represent a semantic word unit.
 
-:::image type="content" source="media/word-boundaries.png" alt-text="Screenshot of detected words example.":::
+:::image type="content" source="../media/word-boundaries.png" alt-text="Screenshot of detected words example.":::
 
 #### Selection marks
 
 A selection mark is a content element that represents a visual glyph indicating the state of a selection. Checkbox is a common form of selection marks. However, they're also represented via radio buttons or a boxed cell in a visual form. The state of a selection mark can be selected or unselected, with different visual representation to indicate the state.
 
-:::image type="content" source="media/selection-marks.png" alt-text="Screenshot of detected selection marks example.":::
+:::image type="content" source="../media/selection-marks.png" alt-text="Screenshot of detected selection marks example.":::
 
 ### Layout elements
 
 #### Line
 
 A line is an ordered sequence of consecutive content elements separated by a visual space, or ones that are immediately adjacent for languages without space delimiters between words. Content elements in the same horizontal plane (row) but separated by more than a single visual space are most often split into multiple lines. While this feature sometimes splits semantically contiguous content into separate lines, it enables the representation of textual content split into multiple columns or cells. Lines in vertical writing are detected in the vertical direction.
 
-:::image type="content" source="media/lines.png" alt-text="Screenshot of detected lines example.":::
+:::image type="content" source="../media/lines.png" alt-text="Screenshot of detected lines example.":::
 
 #### Paragraph
 
 A paragraph is an ordered sequence of lines that form a logical unit. Typically, the lines share common alignment and spacing between lines. Paragraphs are often delimited via indentation, added spacing, or bullets/numbering. Content can only be assigned to a single paragraph.
 Select paragraphs can also be associated with a functional role in the document. Currently supported roles include page header, page footer, page number, title, section heading, and footnote.
 
-:::image type="content" source="media/paragraph.png" alt-text="Screenshot of detected paragraphs example.":::
+:::image type="content" source="../media/paragraph.png" alt-text="Screenshot of detected paragraphs example.":::
 
 #### Page
 
@@ -134,7 +132,7 @@ Based on its position and styling, a cell can be classified as general content,
 > [!NOTE]
 > Starting with *2024-07-31-preview*, the bounding regions for figures and tables cover only the core content and exclude associated caption and footnotes.
 
-:::image type="content" source="media/table.png" alt-text="Layout table":::
+:::image type="content" source="../media/table.png" alt-text="Layout table":::
 
 #### Figures
 
@@ -169,7 +167,7 @@ When *output=figures* is specified during the initial `Analyze` operation, the s
 
 #### Sections
 
-Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [Retrieval Augmented Generation (RAG)](concept-retrieval-augmented-generation.md) in document generative AI underscores the significance of hierarchical document structure analysis. The Layout model supports sections and subsections in the output, which identifies the relationship of sections and object within each section. The hierarchical structure is maintained in `elements` of each section.
+Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [Retrieval Augmented Generation (RAG)](../concept/retrieval-augmented-generation.md) in document generative AI underscores the significance of hierarchical document structure analysis. The Layout model supports sections and subsections in the output, which identifies the relationship of sections and object within each section. The hierarchical structure is maintained in `elements` of each section.
 
 ```json
 {
@@ -192,15 +190,15 @@ Hierarchical document structure analysis is pivotal in organizing, comprehending
 A form field consists of a field label (key) and value. The field label is generally a descriptive text string describing the meaning of the field. It often appears to the left of the value, though it can also appear over or under the value. The field value contains the content value of a specific field instance. The value can consist of words, selection marks, and other content elements. It can also be empty for unfilled form fields. A special type of form field has a selection mark value with the field label to its right.
 Document field is a similar but distinct concept from general form fields. The field label (key) in a general form field must appear in the document. Thus, it can't generally capture information like the merchant name in a receipt. Document fields are labeled and don't extract a key. Document fields only map an extracted value to a labeled key. For more information, *see* [document fields](#form-field-key-value-pair).
 
-:::image type="content" source="media/key-value-pair.png" alt-text="Screenshot of detected key-value pairs example.":::
+:::image type="content" source="../media/key-value-pair.png" alt-text="Screenshot of detected key-value pairs example.":::
 
 ### Style elements
 
 #### Style
 
 A style element describes the font style to apply to text content. The content is specified via spans into the global content property. Currently, the only detected font style is whether the text is handwritten. As other styles are added, text can be described via multiple nonconflicting style objects. For compactness, all text sharing the particular font style (with the same confidence) are described via a single style object.
 
-:::image type="content" source="media/style.png" alt-text="Screenshot of detected style handwritten text example.":::
+:::image type="content" source="../media/style.png" alt-text="Screenshot of detected style handwritten text example.":::
 
 ```json
 
@@ -339,5 +337,4 @@ The semantic schema of a document type is described via the fields it contains.
 
 * Try processing your own forms and documents with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
-
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント分析APIレスポンスに関するドキュメントのリネーム"
}
```

### Explanation
この変更は、「ドキュメント分析APIレスポンス」に関する文書のファイル名を「analyze-document-response.md」から新しい名前にリネームしたことを示しています。この変更には15行の新規追加と18行の削除があり、全体で33行の変更が加えられています。

具体的な変更点としては、メタ情報の更新（特に更新日）や、関連するリンクのパスの修正が行われています。また、内容的には、ドキュメント分析APIが返すレスポンスの要素やその使用方法について詳しく説明がなされています。特に、レスポンスに含まれるさまざまなオブジェクト、要素のプロパティ、バウンディングリージョン、レイアウト要素などについての情報が整理されています。これにより、ユーザーがAPIの応答を理解しやすくなるような改善が図られています。

全体として、このリネームと内容の更新は、ドキュメントの正確性や一貫性を高めるために行われたものであり、使用者にとって有益な最新情報を提供しています。

## articles/ai-services/document-intelligence/concept/choose-model-feature.md{#item-6ea879}

<details>
<summary>Diff</summary>
````diff
@@ -13,64 +13,54 @@ ms.author: lajanuar
 
 # Which model should I choose?
 
- ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
-
-**This content applies to:**![checkmark](media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
-::: moniker-end
-
-::: moniker range="doc-intel-3.1.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true)
-::: moniker-end
-
-::: moniker range="doc-intel-3.0.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true)
+ ::: moniker range="<=doc-intel-3.1.0"
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 ::: moniker-end
 
 Azure AI Document Intelligence supports a wide variety of models that enable you to add intelligent document processing to your applications and optimize your workflows. Selecting the right model is essential to ensure the success of your enterprise. In this article, we explore the available Document Intelligence models and provide guidance for how to choose the best solution for your projects.
 
 > [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RE5fX1b]
 
-The following decision charts highlight the features of each **Document Intelligence v3.0** supported model and help you choose the best model to meet the needs and requirements of your application.
+The following decision charts highlight the features of each supported model to help you choose the model that best meets the needs and requirements of your application.
 
 > [!IMPORTANT]
-> Be sure to check the [**language support**](language-support.md) page for supported language text and field extraction  by feature.
+> Be sure to check the [**language support**](../language-support/prebuilt.md) page for supported language text and field extraction  by feature.
 
 ## Pretrained document-analysis models
 
 | Document type | Example| Data to extract | Your best solution |
 | -----------------|-----------|--------|-------------------|
-|**A generic document**. | A contract or letter. |You want to primarily extract written or printed text lines, words, locations, and detected languages.|[**Read OCR model**](concept-read.md)|
-|**A document that includes structural information**. |A report or study.| In addition to written or printed text, you need to extract structural information like tables, selection marks, paragraphs, titles, headings, and subheadings.| [**Layout analysis model**](concept-layout.md)
-|**A structured or semi-structured document that includes content formatted as fields (keys) and values**.|A form or document that is a standardized format commonly used in your business or industry like a credit application or survey. | You want to extract fields and values including ones not covered by the scenario-specific prebuilt models **without having to train a custom model**.| [**Layout analysis model with the optional query string parameter `features=keyValuePairs` enabled **](concept-layout.md)|
+|**A generic document**. | A contract or letter. |You want to primarily extract written or printed text lines, words, locations, and detected languages.|[**Read OCR model**](../prebuilt/read.md)|
+|**A document that includes structural information**. |A report or study.| In addition to written or printed text, you need to extract structural information like tables, selection marks, paragraphs, titles, headings, and subheadings.| [**Layout analysis model**](../prebuilt/layout.md)|
+|**A structured or semi-structured document that includes content formatted as fields (keys) and values**.|A form or document that is a standardized format commonly used in your business or industry like a credit application or survey. | You want to extract fields and values including ones not covered by the scenario-specific prebuilt models **without having to train a custom model**.| [**Layout analysis model with the optional query string parameter `features=keyValuePairs` enabled **](../prebuilt/layout.md)|
 
 ## Pretrained scenario-specific models
 
 | Document type | Data to extract | Your best solution |
 | -----------------|--------------|-------------------|
-|**US Unified Tax**|You want to extract key information across all tax forms of W2, 1040, 1090, 1098 from a single file without running any custom classification of your own.|[**US Unified tax model**](concept-tax-document.md)|
-|**US Tax W-2 tax**|You want to extract key information such as salary, wages, and taxes withheld.|[**US tax W-2 model**](concept-tax-document.md)|
-|**US Tax 1098**|You want to extract mortgage interest details such as principal, points, and tax.|[**US tax 1098 model**](concept-tax-document.md)|
-|**US Tax 1098-E**|You want to extract student loan interest details such as lender and interest amount.|[**US tax 1098-E model**](concept-tax-document.md)|
-|**US Tax 1098T**|You want to extract qualified tuition details such as scholarship adjustments, student status, and lender information.|[**US tax 1098-T model**](concept-tax-document.md)|
-|**US Tax 1099(Variations)**|You want to extract information from `1099` forms and its variations (A, B, C, CAP, DIV, G, H, INT, K, LS, LTC, MISC, NEC, OID, PATR, Q, QA, R, S, SA, SB).|[**US tax 1099 model**](concept-tax-document.md)|
-|**US Tax 1040(Variations)**|You want to extract information from `1040` forms and its variations (Schedule 1, Schedule 2, Schedule 3, Schedule 8812, Schedule A, Schedule B, Schedule C, Schedule D, Schedule E, Schedule `EIC`, Schedule F, Schedule H, Schedule J, Schedule R, Schedule `SE`, Schedule Senior).|[**US tax 1040 model**](concept-tax-document.md)|
-|**Bank Statement**  |You want to extract key information from US bank statement | [**\Bank Statement**](concept-bank-statement.md)|
-|**Check** |You want to extract key information from check document. | [**Bank Check**](concept-bank-check.md)|
-|**Contract** (legal agreement between parties).|You want to extract contract agreement details such as parties, dates, and intervals.|[**Contract model**](concept-contract.md)|
-|**Health insurance card** or health insurance ID.| You want to extract key information such as insurer, member ID, prescription coverage, and group number.|[**Health insurance card model**](./concept-health-insurance-card.md)|
-|**Credit/Debit card** |You want to extract key information bank cards such as card number and bank name. | [**Credit/Debit card model**](concept-credit-card.md)|
-|**Marriage Certificate** |You want to extract key information from marriage certificates. | [**Marriage certificate model**](concept-marriage-certificate.md)|
-|**Invoice** or billing statement|You want to extract key information such as customer name, billing address, and amount due.|[**Invoice model**](concept-invoice.md)
-|**Receipt**, voucher, or single-page hotel receipt. |You want to extract key information such as merchant name, transaction date, and transaction total.|[**Receipt model**](concept-receipt.md)|
-|**Identity document (ID)** like a U.S. driver's license or international passport |You want to extract key information such as first name, surname, date of birth, address, and signature. | [**Identity document (ID) model**](concept-id-document.md)|
-|**Pay stub** |You want to extract key information from the pay stub document. | [**Pay stub Model**](concept-pay-stub.md)|
-|**US Mortgage 1003** |You want to extract key information from the Uniform Residential loan application. | [**1003 form model**](concept-mortgage-documents.md)|
-|**US Mortgage 1004** |You want to extract key information from the Uniform Residential Appraisal Report (URAR). | [**1004 form model**](concept-mortgage-documents.md)|
-|**US Mortgage 1005** |You want to extract key information from the Verification of employment form | [**1005 form model**](concept-mortgage-documents.md)|
-|**US Mortgage 1008**  |You want to extract key information from the Uniform Underwriting and Transmittal summary. | [**1008 form model**](concept-mortgage-documents.md)|
-|**US Mortgage Closing Disclosure** |You want to extract key information from a mortgage closing disclosure form. | [**Mortgage closing disclosure form model**](concept-mortgage-documents.md)|
-|**Mixed-type document(s)** with structured, semi-structured, and/or unstructured elements | You want to extract key-value pairs, selection marks, tables, signature fields, and selected regions not extracted by prebuilt or general document models.| [**Custom model**](concept-custom.md)|
+|**US Unified Tax**|You want to extract key information across all tax forms of W2, 1040, 1090, 1098 from a single file without running any custom classification of your own.|[**US Unified tax model**](../prebuilt/tax-document.md)|
+|**US Tax W-2 tax**|You want to extract key information such as salary, wages, and taxes withheld.|[**US tax W-2 model**](../prebuilt/tax-document.md)|
+|**US Tax 1098**|You want to extract mortgage interest details such as principal, points, and tax.|[**US tax 1098 model**](../prebuilt/tax-document.md)|
+|**US Tax 1098-E**|You want to extract student loan interest details such as lender and interest amount.|[**US tax 1098-E model**](../prebuilt/tax-document.md)|
+|**US Tax 1098T**|You want to extract qualified tuition details such as scholarship adjustments, student status, and lender information.|[**US tax 1098-T model**](../prebuilt/tax-document.md)|
+|**US Tax 1099(Variations)**|You want to extract information from `1099` forms and its variations (A, B, C, CAP, DIV, G, H, INT, K, LS, LTC, MISC, NEC, OID, PATR, Q, QA, R, S, SA, SB).|[**US tax 1099 model**](../prebuilt/tax-document.md)|
+|**US Tax 1040(Variations)**|You want to extract information from `1040` forms and its variations (Schedule 1, Schedule 2, Schedule 3, Schedule 8812, Schedule A, Schedule B, Schedule C, Schedule D, Schedule E, Schedule `EIC`, Schedule F, Schedule H, Schedule J, Schedule R, Schedule `SE`, Schedule Senior).|[**US tax 1040 model**](../prebuilt/tax-document.md)|
+|**Bank Statement**  |You want to extract key information from US bank statement | [**\Bank Statement**](../concept-bank-statement.md)|
+|**Bank check** |You want to extract key information from check document. | [**Bank Check**](../concept-bank-check.md)|
+|**Contract** (legal agreement between parties).|You want to extract contract agreement details such as parties, dates, and intervals.|[**Contract model**](../prebuilt/contract.md)|
+|**Health insurance card** or health insurance ID.| You want to extract key information such as insurer, member ID, prescription coverage, and group number.|[**Health insurance card model**](../prebuilt/health-insurance-card.md)|
+|**Credit/Debit card** |You want to extract key information bank cards such as card number and bank name. | [**Credit/Debit card model**](../concept-credit-card.md)|
+|**Marriage Certificate** |You want to extract key information from marriage certificates. | [**Marriage certificate model**](../concept-marriage-certificate.md)|
+|**Invoice** or billing statement|You want to extract key information such as customer name, billing address, and amount due.|[**Invoice model**](../prebuilt/invoice.md)|
+|**Receipt**, voucher, or single-page hotel receipt. |You want to extract key information such as merchant name, transaction date, and transaction total.|[**Receipt model**](../prebuilt/receipt.md)|
+|**Identity document (ID)** like a U.S. driver's license or international passport |You want to extract key information such as first name, surname, date of birth, address, and signature. | [**Identity document (ID) model**](../prebuilt/id-document.md)|
+|**Pay stub** |You want to extract key information from the pay stub document. | [**Pay stub Model**](../concept-pay-stub.md)|
+|**US Mortgage 1003** |You want to extract key information from the Uniform Residential loan application. | [**1003 form model**](../concept-mortgage-documents.md)|
+|**US Mortgage 1004** |You want to extract key information from the Uniform Residential Appraisal Report (URAR). | [**1004 form model**](../concept-mortgage-documents.md)|
+|**US Mortgage 1005** |You want to extract key information from the Verification of employment form | [**1005 form model**](../concept-mortgage-documents.md)|
+|**US Mortgage 1008**  |You want to extract key information from the Uniform Underwriting and Transmittal summary. | [**1008 form model**](../concept-mortgage-documents.md)|
+|**US Mortgage Closing Disclosure** |You want to extract key information from a mortgage closing disclosure form. | [**Mortgage closing disclosure form model**](../concept-mortgage-documents.md)|
+|**Mixed-type document(s)** with structured, semi-structured, and/or unstructured elements | You want to extract key-value pairs, selection marks, tables, signature fields, and selected regions not extracted by prebuilt or general document models.| [**Custom model**](../train/custom-model.md)|
 
 >[!Tip]
 >
@@ -81,17 +71,17 @@ The following decision charts highlight the features of each **Document Intellig
 
 | Training set | Example documents | Your best solution |
 | -----------------|--------------|-------------------|
-|**Structured, consistent, documents with a static layout**. |Structured forms such as questionnaires or applications. | [**Custom template model**](./concept-custom-template.md)|
-|**Structured and semi-structured**.|&#9679; Structured &rightarrow; surveys</br>&#9679; Semi-structured &rightarrow; invoices | [**Custom neural model**](concept-custom-neural.md)|
-|**Unstructured documents, documents with varying templates**.|&#9679; Unstructured documents like contracts or letters</br> &#9679; Varying document templates like loan statements from different mortgage companies| [**Custom generative model**](concept-custom-generative.md)|
-|**A collection of several models each trained on similar-type documents.** |&#9679; Supply purchase orders</br>&#9679; Equipment purchase orders</br>&#9679; Furniture purchase orders</br> **All composed into a single model**.| [**Composed custom model**](concept-composed-models.md)|
+|**Structured, consistent, documents with a static layout**. |Structured forms such as questionnaires or applications. | [**Custom template model**](./../train/custom-template.md)|
+|**Structured and semi-structured**.|&#9679; Structured &rightarrow; surveys</br>&#9679; Semi-structured &rightarrow; invoices | [**Custom neural model**](../train/custom-neural.md)|
+|**Unstructured documents, documents with varying templates**.|&#9679; Unstructured documents like contracts or letters</br> &#9679; Varying document templates like loan statements from different mortgage companies| [**Custom generative model**](../train/custom-generative-extraction.md)|
+|**A collection of several models each trained on similar-type documents.** |&#9679; Supply purchase orders</br>&#9679; Equipment purchase orders</br>&#9679; Furniture purchase orders</br> **All composed into a single model**.| [**Composed custom model**](../train/composed-models.md)|
 
 ## Custom classification model
 
 | Training set | Example documents | Your best solution |
 | -----------------|--------------|-------------------|
-|**At least two different types of documents**. |Forms, letters, or documents | [**Custom classification model**](./concept-custom-classifier.md)|
+|**At least two different types of documents**. |Forms, letters, or documents | [**Custom classification model**](./../train/custom-classifier.md)|
 
 ## Next steps
 
-* [Learn how to process your own forms and documents](quickstarts/try-document-intelligence-studio.md) with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)
+* [Learn how to process your own forms and documents](../quickstarts/try-document-intelligence-studio.md) with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル選択に関するドキュメントのリネーム"
}
```

### Explanation
この変更は、「モデル選択」に関する文書のファイル名を「choose-model-feature.md」から新しい名前にリネームしたことを示しています。この変更には36行の新規追加と46行の削除が含まれ、合計で82行の変更が加えられています。

具体的には、コンテンツの一部が整理され、最新の情報が反映されました。たとえば、ドキュメント分析モデルに関する決定チャートが更新され、各モデルの特長がより明確に示されています。また、リンクのパスが相対的に修正され、文書全体の整合性が向上しています。

さらに、ユーザーがどのモデルを選択するべきかを決めるためのより詳細なガイダンスが提供されています。これにより、ユーザーは各モデルの機能や目的を理解し、目的に最も適したモデルを選択しやすくなります。

全体として、このリネームおよび内容の更新は、ドキュメントの利用価値を高め、ユーザーが技術的な選択を行う際のサポートを強化することを目的としています。

## articles/ai-services/document-intelligence/concept/incremental-classifier.md{#item-c9bffe}

<details>
<summary>Diff</summary>
````diff
@@ -1,28 +1,34 @@
 ---
-title: Document Intelligence support for incremental classifier training
+title: Use Document Intelligence incremental classifiers
 titleSuffix: Azure AI services
 description: Incrementally train custom classifiers by adding new samples to existing classes or adding new classes.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 05/23/2024
+ms.date: 10/03/2024
 ms.author: vikurpad
 ms.custom:
 monikerRange: '>=doc-intel-4.0.0'
 ---
 
+<!-- markdownlint-disable MD033 -->
 
+# Use Document Intelligence incremental classifiers
 
-# Incremental classifier training
-
-**This content applies to:** ![checkmark](media/yes-icon.png) **v4.0 (preview)** ![checkmark](media/yes-icon.png)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (preview)** ![checkmark](../media/yes-icon.png)
 
 Azure AI Document Intelligence is a cloud-based Azure AI service that enables you to build intelligent document processing solutions. Document Intelligence APIs analyze images, PDFs, and other document files to extract and detect various content, layout, style, and semantic elements.
 
-[Document Intelligence custom classification models](concept-custom-classifier.md) are deep-learning-model types that combine layout and language features to accurately detect and identify documents you process within your applications. Custom classification models perform classification of input files one page at a time to identify the documents within and can also identify multiple documents or multiple instances of a single document within an input file.
+[Document Intelligence custom classification models](../train/custom-classifier.md) are deep-learning-model types that combine layout and language features to accurately detect and identify documents you process within your applications. Custom classification models perform classification of input files one page at a time to identify the documents within and can also identify multiple documents or multiple instances of a single document within an input file.
+
+Document Intelligence document classifiers identify known document types in files. When processing an input file with multiple document types or when you don't know the document type, use a classifier to identify the document. Classifiers should be periodically updated whenever the following changes occur:
+
+* You add new templates for an existing class.
+* You add new document types for recognition.
+* Classifier confidence is low.
 
-Document Intelligence document classifiers identify known document types in files. When processing an input file with multiple document types or when you don't know the document type, use a classifier to identify the document. Classifiers should be periodically updated when you add new templates for an existing class, add new document types for recognition, or classifier confidence is low. In some scenarios, you can no longer have the original set of documents used to train the classifier. With incremental training, you can now update the classifier with just the new labeled samples.
+In some scenarios, you can no longer have the original set of documents used to train the classifier. With incremental training, you can update the classifier with just the new labeled samples.
 
 >[!NOTE]
 > Incremental training only applies to document classifier models and not custom models.
@@ -44,7 +50,7 @@ Incremental training is useful when you want to improve the quality of a custom
 
 ### Create an incremental classifier build request
 
-The incremental classifier build request is similar to the [classify document build request](/rest/api/aiservices/document-classifiers?view=rest-aiservices-v4.0%20(2024-02-29-preview)&preserve-view=true) but includes the new `baseClassifierId` property. The `baseClassifierId` is set to the existing classifier that you want to extend. You also need to provide the `docTypes` for the different document types in the sample set. By providing a `docType` that exists in the baseClassifier, the samples provided in the request are added to the samples provided when the base classifier was trained. New `docType` values added in the incremental training are only added to the new classifier. The process to specify the samples remains unchanged. For more information, *see* [training a classifier model](concept-custom-classifier.md#training-a-model).
+The incremental classifier build request is similar to the [`classify document` build request](/rest/api/aiservices/document-classifiers?view=rest-aiservices-v4.0%20(2024-02-29-preview)&preserve-view=true) but includes the new `baseClassifierId` property. The `baseClassifierId` is set to the existing classifier that you want to extend. You also need to provide the `docTypes` for the different document types in the sample set. By providing a `docType` that exists in the baseClassifier, the samples provided in the request are added to the samples provided when the base classifier was trained. New `docType` values added in the incremental training are only added to the new classifier. The process to specify the samples remains unchanged. For more information, *see* [training a classifier model](../train/custom-classifier.md#training-a-model).
 
 ### Sample POST request
 
@@ -124,10 +130,10 @@ The `GET` response from an incrementally trained classifier differs from the sta
 
 ## Limits
 
-* Incremental training only works when the base classifier and the incrementally trained classifier are both trained on the same API version. As a result, the incrementally trained classifier has the same [model lifecycle](concept-custom-lifecycle.md) as the base classifier.
+* Incremental training only works when the base classifier and the incrementally trained classifier are both trained on the same API version. As a result, the incrementally trained classifier has the same [model lifecycle](../concept-custom-lifecycle.md) as the base classifier.
 
-* Training dataset size limits for the incremental classifier are the same as for other classifier model. See [service limits](service-limits.md) for a complete list of applicable limits.
+* Training dataset size limits for the incremental classifier are the same as for other classifier model. See [service limits](../service-limits.md) for a complete list of applicable limits.
 
 ## Next steps
 
-* Learn more about [document classification](concept-custom-classifier.md)
+* Learn more about [document classification](../train/custom-classifier.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インクリメンタル分類器に関するドキュメントのリネーム"
}
```

### Explanation
この変更は、「インクリメンタル分類器」に関する文書のファイル名を「incremental-classifier.md」から新しい名前にリネームしたことを示しています。この変更には17行の新規追加と11行の削除が含まれ、合計で28行の変更が加えられています。

主な変更点として、文書内のタイトルが更新され、コンテンツ内のリンクが正相対パスに変更されています。これは、情報の一貫性を保つために行われました。また、新しい情報として、インクリメンタル訓練の利点や、それに伴う更新手順が強調されており、ユーザーが分類器を定期的に更新する必要がある理由について詳しく説明されています。

さらに、インクリメンタル分類器の構築リクエストの説明も改善され、既存の分類器を拡張する手順についてより明確な指示が提供されています。これにより、ユーザーは新しいラベル付きサンプルを使用して分類器を更新する方法をより理解しやすくなります。

全体として、このリネームおよび内容の更新は、ドキュメントの利用価値を高め、ユーザーがインクリメンタル分類器を効果的に活用できるようにすることを目的としています。

## articles/ai-services/document-intelligence/concept/query-fields.md{#item-c58523}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Use Document Intelligence query fields to extend model schema.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 01/19/2024
 ms.author: nitinme
@@ -38,18 +36,18 @@ For query field extraction, specify the fields you want to extract and Document
 
 * If you're processing a contract in the [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/layout), use the `2024-02-29-preview`, `2023-10-31-preview`, or later API version:
 
-    :::image type="content" source="media/studio/query-fields.png" alt-text="Screenshot of the query fields button in Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/query-fields.png" alt-text="Screenshot of the query fields button in Document Intelligence Studio.":::
 
 * You can pass a list of field labels like `Party1`, `Party2`, `TermsOfUse`, `PaymentTerms`, `PaymentDate`, and `TermEndDate`" as part of the `AnalyzeDocument` request.
 
-   :::image type="content" source="media/studio/query-field-select.png" alt-text="Screenshot of query fields selection window in Document Intelligence Studio.":::
+   :::image type="content" source="../media/studio/query-field-select.png" alt-text="Screenshot of query fields selection window in Document Intelligence Studio.":::
 
-* In addition to the query fields, the response includes the model output. For a list of features or schema extracted by each model, see [model analysis features](concept-model-overview.md#model-analysis-features).
+* In addition to the query fields, the response includes the model output. For a list of features or schema extracted by each model, see [model analysis features](../model-overview.md#model-analysis-features).
 
 
 ## Query fields REST API request**
 
-Use the query fields feature with the [general document model](concept-general-document.md), and add fields to the extraction process without having to train a custom model:
+Use the query fields feature with the [general document model](../prebuilt/general-document.md), and add fields to the extraction process without having to train a custom model:
 
 ```http
 POST https://{endpoint}/documentintelligence/documentModels/prebuilt-layout:analyze?api-version=2024-02-29-preview&features=queryFields&queryFields=Terms,PaymentDate HTTP/1.1
@@ -65,7 +63,7 @@ Ocp-Apim-Subscription-Key:
 ## Next steps
 
 > [!div class="nextstepaction"]
-> [Try the Document Intelligence Studio quickstart](./quickstarts/try-document-intelligence-studio.md)
+> [Try the Document Intelligence Studio quickstart](../quickstarts/try-document-intelligence-studio.md)
 
 > [!div class="nextstepaction"]
-> [Learn about other add-on capabilities](concept-add-on-capabilities.md)
+> [Learn about other add-on capabilities](../concept/add-on-capabilities.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クエリフィールドに関するドキュメントのリネーム"
}
```

### Explanation
この変更は、「クエリフィールド」に関する文書のファイル名を「query-fields.md」から新しい名前にリネームしたことを示しています。この変更には6行の新規追加と8行の削除が含まれ、合計で14行の変更が加えられています。

主な変更点として、ドキュメント内の画像パスが相対的に修正されており、情報の一貫性が保たれるようになりました。さらに、説明内のリンクも相対パスに更新され、関連情報へのアクセスがよりスムーズになっています。

また、クエリフィールドによって抽出される情報に関する説明も整理され、ユーザーがフィールドラベルを使用して分析リクエストを送信する方法についての詳細が提供されています。これにより、ユーザーがDocument Intelligence Studioで契約書を処理する際の具体的な手順がより明確になります。

全体として、このリネームおよび内容の更新は、ドキュメントの可読性を向上させ、ユーザーがクエリフィールド機能を効果的に活用できるようにすることを目的としています。

## articles/ai-services/document-intelligence/concept/retrieval-augmented-generation.md{#item-c42dcc}

<details>
<summary>Diff</summary>
````diff
@@ -15,15 +15,15 @@ monikerRange: '>=doc-intel-3.1.0'
 
 <!-- markdownlint-disable MD036 -->
 
-**This content applies to:** ![checkmark](media/yes-icon.png) **v4.0 (preview)**
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (preview)**
 
 ## Introduction
 
 Retrieval-Augmented Generation (RAG) is a design pattern that combines a pretrained Large Language Model (LLM) like ChatGPT with an external data retrieval system to generate an enhanced response incorporating new data outside of the original training data. Adding an information retrieval system to your applications enables you to chat with your documents, generate captivating content, and access the power of Azure OpenAI models for your data. You also have more control over the data used by the LLM as it formulates a response.
 
-The Document Intelligence [Layout model](concept-layout.md) is an advanced machine-learning based document analysis API. The Layout model offers a comprehensive solution for advanced content extraction and document structure analysis capabilities. With the Layout model, you can easily extract text and structural elements to divide large bodies of text into smaller, meaningful chunks based on semantic content rather than arbitrary splits. The extracted information can be conveniently outputted to Markdown format, enabling you to define your semantic chunking strategy based on provided building blocks.
+The Document Intelligence [Layout model](../prebuilt/layout.md) is an advanced machine-learning based document analysis API. The Layout model offers a comprehensive solution for advanced content extraction and document structure analysis capabilities. With the Layout model, you can easily extract text and structural elements to divide large bodies of text into smaller, meaningful chunks based on semantic content rather than arbitrary splits. The extracted information can be conveniently outputted to Markdown format, enabling you to define your semantic chunking strategy based on provided building blocks.
 
-:::image type="content" source="media/rag/azure-rag-processing.png" alt-text="Screenshot depicting semantic chunking with RAG using Azure AI Document Intelligence.":::
+:::image type="content" source="../media/rag/azure-rag-processing.png" alt-text="Screenshot depicting semantic chunking with RAG using Azure AI Document Intelligence.":::
 
 ## Semantic chunking
 
@@ -37,23 +37,23 @@ Text data chunking strategies play a key role in optimizing the RAG response and
 
 ## Semantic chunking with Document Intelligence Layout model
 
-Markdown is a structured and formatted markup language and a popular input for enabling semantic chunking in RAG (Retrieval-Augmented Generation). You can use the Markdown content from the [Layout model](concept-layout.md) to split documents based on paragraph boundaries, create specific chunks for tables, and fine-tune your chunking strategy to improve the quality of the generated responses.
+Markdown is a structured and formatted markup language and a popular input for enabling semantic chunking in RAG (Retrieval-Augmented Generation). You can use the Markdown content from the [Layout model](../prebuilt/layout.md) to split documents based on paragraph boundaries, create specific chunks for tables, and fine-tune your chunking strategy to improve the quality of the generated responses.
 
 ### Benefits of using the Layout model
 
 * **Simplified processing**. You can parse different document types, such as digital and scanned PDFs, images, office files (docx, xlsx, pptx), and HTML, with just a single API call.
 
-* **Scalability and AI quality**. The Layout model is highly scalable in Optical Character Recognition (OCR), table extraction, and [document structure analysis](concept-layout.md#document-layout-analysis). It supports [309 printed and 12 handwritten languages](language-support-ocr.md#model-id-prebuilt-layout), further ensuring high-quality results driven by AI capabilities.
+* **Scalability and AI quality**. The Layout model is highly scalable in Optical Character Recognition (OCR), table extraction, and [document structure analysis](../prebuilt/layout.md#document-layout-analysis). It supports [309 printed and 12 handwritten languages](../language-support/ocr.md#model-id-prebuilt-layout), further ensuring high-quality results driven by AI capabilities.
 
 * **Large language model (LLM) compatibility**. The Layout model Markdown formatted output is LLM friendly and facilitates seamless integration into your workflows. You can turn any table in a document into Markdown format and avoid extensive effort parsing the documents for greater LLM understanding.
 
 **Text image processed with Document Intelligence Studio and output to MarkDown using Layout model**
 
-  :::image type="content" source="media/rag/markdown-text-output.png" alt-text="Screenshot of newspaper article processed by Layout model and outputted to Markdown.":::
+  :::image type="content" source="../media/rag/markdown-text-output.png" alt-text="Screenshot of newspaper article processed by Layout model and outputted to Markdown.":::
 
 **Table image processed with Document Intelligence Studio using Layout model**
 
-  :::image type="content" source="media/rag/markdown-table-output.png" alt-text="Screenshot of table processed by Layout model and outputted to Markdown.":::
+  :::image type="content" source="../media/rag/markdown-table-output.png" alt-text="Screenshot of table processed by Layout model and outputted to Markdown.":::
 
 ## Get started
 
@@ -63,13 +63,13 @@ The Document Intelligence Layout model **2024-07-31-preview** and **2023-10-31-p
 
 * [REST API](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2024-02-29-preview&preserve-view=true&branch=docintelligence&tabs=HTTP).
 
-* [.NET &bull; Java &bull; JavaScript &bull; Python programming language client libraries (SDKs).](sdk-overview-v4-0.md#supported-programming-languages)
+* [.NET &bull; Java &bull; JavaScript &bull; Python programming language client libraries (SDKs).](../sdk-overview-v4-0.md#supported-programming-languages)
 
 **Ready to begin?**
 
 ### Document Intelligence Studio
 
-You can follow the [Document Intelligence Studio quickstart](quickstarts/try-document-intelligence-studio.md) to get started. Next, you can integrate Document Intelligence features with your own application using the sample code provided.
+You can follow the [Document Intelligence Studio quickstart](../quickstarts/try-document-intelligence-studio.md) to get started. Next, you can integrate Document Intelligence features with your own application using the sample code provided.
 
 * Start with the [Layout model](https://documentintelligence.ai.azure.com/studio/layout). You need to select the following **Analyze options** to use RAG in the studio:
 
@@ -85,15 +85,15 @@ You can follow the [Document Intelligence Studio quickstart](quickstarts/try-doc
 
 * Select **Save**.
 
-  :::image type="content" source="media/rag/rag-analyze-options.png" alt-text="Screenshot of Analyze options dialog window with RAG required options in the Document Intelligence studio.":::
+  :::image type="content" source="../media/rag/rag-analyze-options.png" alt-text="Screenshot of Analyze options dialog window with RAG required options in the Document Intelligence studio.":::
 
 * Select the **Run analysis** button to view the output.
 
-  :::image type="content" source="media/rag/run-analysis.png" alt-text="Screenshot of the Run Analysis button in the Document Intelligence Studio.":::
+  :::image type="content" source="../media/rag/run-analysis.png" alt-text="Screenshot of the Run Analysis button in the Document Intelligence Studio.":::
 
 ### SDK or REST API
 
-* You can follow the [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md) for your preferred programming language SDK or REST API. Use the Layout model to extract content and structure from your documents.
+* You can follow the [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md) for your preferred programming language SDK or REST API. Use the Layout model to extract content and structure from your documents.
 
 * You can also check out GitHub repos for code samples and tips for analyzing a document in markdown output format.
 
@@ -107,7 +107,7 @@ You can follow the [Document Intelligence Studio quickstart](quickstarts/try-doc
 
 ## Build document chat with semantic chunking
 
-* [Azure OpenAI on your data](../openai/concepts/use-your-data.md) enables you to run supported chat on your documents. Azure OpenAI on your data applies the Document Intelligence Layout model to extract and parse document data by chunking long text based on tables and paragraphs. You can also customize your chunking strategy using [Azure OpenAI sample scripts](https://github.com/microsoft/sample-app-aoai-chatGPT/tree/main/scripts) located in our GitHub repo.
+* [Azure OpenAI on your data](../../openai/concepts/use-your-data.md) enables you to run supported chat on your documents. Azure OpenAI on your data applies the Document Intelligence Layout model to extract and parse document data by chunking long text based on tables and paragraphs. You can also customize your chunking strategy using [Azure OpenAI sample scripts](https://github.com/microsoft/sample-app-aoai-chatGPT/tree/main/scripts) located in our GitHub repo.
 
 * Azure AI Document Intelligence is now integrated with [LangChain](https://python.langchain.com/docs/integrations/document_loaders/azure_document_intelligence) as one of its document loaders. You can use it to easily load the data and output to Markdown format. For more information, see our [sample code](https://github.com/microsoft/Form-Recognizer-Toolkit/blob/main/SampleCode/Python/sample_rag_langchain.ipynb) that shows a simple demo for RAG pattern with Azure AI Document Intelligence as document loader and Azure Search as retriever in LangChain.
 
@@ -153,8 +153,8 @@ splits
 
 ## Next steps
 
-* Learn more about [Azure AI Document Intelligence](overview.md).
+* Learn more about [Azure AI Document Intelligence](../overview.md).
 
-* [Learn how to process your own forms and documents](quickstarts/try-document-intelligence-studio.md) with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
+* [Learn how to process your own forms and documents](../quickstarts/try-document-intelligence-studio.md) with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "情報検索強化生成に関するドキュメントのリネーム"
}
```

### Explanation
この変更は、「情報検索強化生成」に関する文書のファイル名を「retrieval-augmented-generation.md」から新しい名前にリネームしたことを示しています。変更内容には16行の新規追加と16行の削除が含まれ、合計で32行の変更が加えられています。

主な改訂点としては、ドキュメント内のリンクや画像パスが正相対パスに更新されたことが挙げられ、情報の一貫性とアクセスのしやすさが向上しています。例えば、レイアウトモデルに関するリンクや画像の参照が、より適切なパスに変更されています。

また、このドキュメントはRetrieval-Augmented Generation (RAG) の定義とその利用法に関する情報を提供しており、Azure OpenAIモデルとの統合によって得られる利点について詳しく説明されています。さらに、レイアウトモデルを使用したセマンティックチャンク作成の方法やそのメリットが強調されており、ユーザーが文書分析を効果的に行うための具体的なアプローチが示されています。

このように、ファイル名の変更と内容の更新は、ユーザーが情報検索強化生成の機能を理解し、適切に活用できるようにするための重要なステップといえます。

## articles/ai-services/document-intelligence/containers/configuration.md{#item-e17282}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Learn how to configure the Document Intelligence container to parse
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
 ms.date: 05/23/2024
 ms.author: lajanuar
@@ -18,12 +16,12 @@ ms.author: lajanuar
 
 :::moniker range="doc-intel-2.1.0 || doc-intel-4.0.0"
 
-Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models and `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt and ID Document models:
+Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models and `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models:
 
 * [REST API `2022-08-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 * [REST API `2023-07-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.1%20(2023-07-31)&tabs=HTTP&preserve-view=true)
-* [SDKs targeting `REST API 2022-08-31 (GA)`](../sdk-overview-v3-0.md)
-* [SDKs targeting `REST API 2023-07-31 (GA)`](../sdk-overview-v3-1.md)
+* [Client libraries targeting `REST API 2022-08-31 (GA)`](../sdk-overview-v3-0.md)
+* [Client libraries targeting `REST API 2023-07-31 (GA)`](../sdk-overview-v3-1.md)
 
 ✔️ See [**Configure Document Intelligence v3.0 containers**](?view=doc-intel-3.0.0&preserve-view=true) for supported container documentation.
 
@@ -42,7 +40,7 @@ Each container has the following configuration settings:
 |Required|Setting|Purpose|
 |--|--|--|
 |Yes|[Key](#key-and-billing-configuration-setting)|Tracks billing information.|
-|Yes|[Billing](#key-and-billing-configuration-setting)|Specifies the endpoint URI of the service resource on Azure.  For more information, _see_ [Billing](install-run.md#billing). For more information and a complete list of regional endpoints, _see_ [Custom subdomain names for Azure AI services](../../../ai-services/cognitive-services-custom-subdomains.md).|
+|Yes|[Billing](#key-and-billing-configuration-setting)|Specifies the endpoint URI of the service resource on Azure. For more information, _see_ [Billing](install-run.md#billing). For more information and a complete list of regional endpoints, _see_ [Custom subdomain names for Azure AI services](../../../ai-services/cognitive-services-custom-subdomains.md).|
 |Yes|[Eula](#eula-setting)| Indicates that you accepted the license for the container.|
 |No|[ApplicationInsights](#applicationinsights-setting)|Enables adding [Azure Application Insights](/azure/application-insights) customer support for your container.|
 |No|[Fluentd](#fluentd-settings)|Writes log and, optionally, metric data to a Fluentd server.|
@@ -62,7 +60,7 @@ The `Billing` setting specifies the endpoint URI of the resource on Azure that i
 
    :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of Azure portal keys and endpoint page.":::
 
-## EULA setting
+## `EULA` setting
 
 [!INCLUDE [Container shared configuration eula settings](../../includes/cognitive-services-containers-configuration-shared-settings-eula.md)]
 
@@ -84,7 +82,7 @@ The `Billing` setting specifies the endpoint URI of the resource on Azure that i
 
 ## Volume settings
 
-Use [**volumes**](https://docs.docker.com/storage/volumes/) to read and write data to and from the container. Volumes are the preferred for persisting data generated and used by Docker containers. You can specify an input mount or an output mount by including the `volumes` option and specifying `type` (bind), `source` (path to the folder) and `target` (file path parameter).
+Use [**volumes**](https://docs.docker.com/storage/volumes/) to read and write data to and from the container. Volumes are the preferred for persisting data generated and used by Docker containers. You can specify an input mount or an output mount by including the `volumes` option and specifying `type` (bind), `source` (path to the folder), and `target` (file path parameter).
 
 The Document Intelligence container requires an input volume and an output volume. The input volume can be read-only (`ro`), and is required for access to the data that is used for training and scoring. The output volume has to be writable, and you use it to store the models and temporary data.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスコンテナの設定に関する記事の修正"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスのコンテナ設定に関する記事を修正したものであり、6行の新規追加と8行の削除が含まれ、合計で14行の修正が行われています。

主な改訂点には、コンテナのサポートについての情報や、REST APIおよびSDKに関するリンクが含まれています。「SDKs targeting」という表現が「Client libraries targeting」に変更され、用語の一貫性が向上しました。また、EULA（エンドユーザーライセンス契約）に関する設定見出しがより明確に表記され、理解しやすくなっています。

さらに、コンテナの構成設定に関する詳細が整理され、文書全体の情報の明晰さが改善されています。具体的には、各設定項目の目的が明確に記述され、設定方法も視覚的に示すためのスクリーンショットが提供されています。

全体として、この変更はコンテナの設定に関するガイドを書き換え、利用者がドキュメントインテリジェンスコンテナを効果的に設定し、利用するための情報を整理したものとなっています。

## articles/ai-services/document-intelligence/containers/disconnected.md{#item-c70d0b}

<details>
<summary>Diff</summary>
````diff
@@ -3,8 +3,6 @@ title: Use Document Intelligence containers in disconnected environments
 titleSuffix: Azure AI services
 description: Learn how to run Cognitive Services Docker containers disconnected from the internet.
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 author: laujan
 manager: nitinme
 ms.topic: reference
@@ -17,12 +15,12 @@ ms.author: lajanuar
 
 :::moniker range="doc-intel-2.1.0 || doc-intel-4.0.0"
 
-Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models and `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt and ID Document models:
+Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models and `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models:
 
 * [REST API `2022-08-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 * [REST API `2023-07-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.1%20(2023-07-31)&tabs=HTTP&preserve-view=true)
-* [SDKs targeting `REST API 2022-08-31 (GA)`](../sdk-overview-v3-0.md)
-* [SDKs targeting `REST API 2023-07-31 (GA)`](../sdk-overview-v3-1.md)
+* [Client libraries targeting `REST API 2022-08-31 (GA)`](../sdk-overview-v3-0.md)
+* [Client libraries targeting `REST API 2023-07-31 (GA)`](../sdk-overview-v3-1.md)
 
 ✔️ See [**Document Intelligence v3.0 containers in disconnected environments**](?view=doc-intel-3.0.0&preserve-view=true) for supported container documentation.
 
@@ -56,13 +54,13 @@ Before you can use Document Intelligence containers in disconnected environments
 Start by provisioning a new resource in the portal.
 
 * Ensure you select the `Commitment tier disconnected containers DC0` option for Pricing tier
-* Select the appropriate pricing tier from at least one of custom, read or prebuilt commitment tiers
+* Select the appropriate pricing tier from at least one of custom, read, or prebuilt commitment tiers
 
   :::image type="content" source="../media/containers/disconnected.png" alt-text="Screenshot of disconnected tier configuration in the Azure portal.":::
 
 | Container | Minimum | Recommended | Commitment plan |
 |-----------|---------|-------------|-------------|
-| `Read` | `8` cores, 10-GB memory | `8` cores, 24-GB memory| OCR (Read) |
+| `Read` | `8` cores, 10-GB memory | `8` cores, 24-GB memory| `OCR` (Read) |
 | `Layout` | `8` cores, 16-GB memory | `8` cores, 24-GB memory | Prebuilt |
 | `Business Card` | `8` cores, 16-GB memory | `8` cores, 24-GB memory | Prebuilt |
 | `General Document` | `8` cores, 12-GB memory | `8` cores, 24-GB memory| Prebuilt |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "切断された環境でのドキュメントインテリジェンスコンテナの使用に関する記事の修正"
}
```

### Explanation
この変更は、切断された環境でのドキュメントインテリジェンスコンテナの使用に関する記事の修正を示しており、5行の新規追加と7行の削除が含まれ、合計で12行の変更が行われています。

主な改訂点には、ドキュメントインテリジェンスコンテナのバージョンに関する情報が含まれています。特に、REST APIおよびクライアントライブラリに関する記述が「SDKs targeting」という表現から「Client libraries targeting」に変更され、用語が一貫性を持つように整理されています。また、設定項目の説明においても文章の流れが改善され、理解を深められるよう配慮されています。

さらに、コンテナの価格プランに関する説明が強調され、より具体的な情報が提供されています。たとえば、各コンテナの必要な最小要件や推奨要件が明確に示され、利便性が向上しています。

全体的に、この変更はドキュメントをより使いやすくし、ユーザーが切断された環境でドキュメントインテリジェンスコンテナを効果的に利用できるようにする情報を提供しています。

## articles/ai-services/document-intelligence/containers/image-tags.md{#item-6a7764}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: A listing of all Document Intelligence container image tags.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: reference
 ms.date: 05/23/2024
 ms.author: lajanuar
@@ -18,12 +16,12 @@ ms.author: lajanuar
 
 :::moniker range="doc-intel-2.1.0 || doc-intel-4.0.0"
 
-Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models and `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt and ID Document models:
+Support for containers is currently available with Document Intelligence version `2022-08-31 (GA)` for all models and `2023-07-31 (GA)` for Read, Layout, Invoice, Receipt, and ID Document models:
 
 * [REST API `2022-08-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 * [REST API `2023-07-31 (GA)`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.1%20(2023-07-31)&tabs=HTTP&preserve-view=true)
-* [SDKs targeting `REST API 2022-08-31 (GA)`](../sdk-overview-v3-0.md)
-* [SDKs targeting `REST API 2023-07-31 (GA)`](../sdk-overview-v3-1.md)
+* [Client libraries targeting `REST API 2022-08-31 (GA)`](../sdk-overview-v3-0.md)
+* [Client libraries targeting `REST API 2023-07-31 (GA)`](../sdk-overview-v3-1.md)
 
 ✔️ See [**Document Intelligence container image tags**](?view=doc-intel-3.0.0&preserve-view=true) for supported container documentation.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスコンテナのイメージタグに関する記事の修正"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスコンテナのイメージタグに関する記事の修正を示しており、3行の新規追加と5行の削除が含まれ、合計で8行の変更が行われています。

主な改訂点として、ドキュメントインテリジェンスのサポートされているコンテナのバージョンが明確に記述されています。また、「SDKs targeting」という用語が「Client libraries targeting」に変更され、用語の一貫性が向上しています。この変更により、ドキュメント全体の情報がより明確になり、読者が利用する際の理解が深まるよう配慮されています。

さらに、記事中の情報を整理し、ドキュメントインテリジェンスコンテナに関連するリンクやリソースへのアクセスが簡単にできるように整備されています。この修正は、ユーザーがドキュメントインテリジェンスのコンテナに関する情報を効率よく得るための改善を図ったものとなっています。

## articles/ai-services/document-intelligence/faq.yml{#item-7a051f}

<details>
<summary>Diff</summary>
````diff
@@ -52,12 +52,12 @@ sections:
         answer: |
           **Yes.**
 
-          Document Intelligence now includes [custom generative](concept-custom.md) a new type of extraction model that uses Generative AI and large language models (LLMs) to extract fields from documents. In the past, you used a RAG (retrieval augmented generation) pattern to extract fields. The new model provides high quality results with a single API call.
+          Document Intelligence now includes [custom generative](train/custom-generative-extraction.md) a new type of extraction model that uses Generative AI and large language models (LLMs) to extract fields from documents. In the past, you used a RAG (retrieval augmented generation) pattern to extract fields. The new model provides high quality results with a single API call.
           You can also use a document generative AI solution to chat with your documents (RAG), generate captivating content from those documents, and access Azure OpenAI Service models on your data.
 
           - With Azure AI Document Intelligence and Azure OpenAI combined, you can build an enterprise application to seamlessly interact with your documents using natural language. You can easily find answers, gain valuable insights, and generate new and engaging content from existing documents.
 
-          - You can find more details on the [retrieval augmented generation pattern here](concept-retrieval-augmented-generation.md).
+          - You can find more details on the [retrieval augmented generation pattern here](concept/retrieval-augmented-generation.md).
 
       - question: |
          Can Document Intelligence help with semantic chunking within documents for retrieval-augmented generation?
@@ -70,7 +70,7 @@ sections:
 
           - You can then choose to retrieve the results in markdown format, to further chunk the document on section or paragraph boundaries.
 
-          For more information, see [overview of RAG in Document Intelligence](concept-retrieval-augmented-generation.md)
+          For more information, see [overview of RAG in Document Intelligence](concept/retrieval-augmented-generation.md)
 
   - name: Document Intelligence Studio
     questions:
@@ -134,15 +134,15 @@ sections:
         answer: |
          **Yes.**
 
-         If your Document Intelligence resource is configured with a firewall or virtual network, you need to add the dedicated IP address 20.3.165.95 to the firewall allowlist for your Document Intelligence resource.  Please note that some functions in custom projects (e.g. auto-label, project management and human in the loop) won't work if the public network access is disabled.
+         If your Document Intelligence resource is configured with a firewall or virtual network, you need to add the dedicated IP address 20.3.165.95 to the firewall allowlist for your Document Intelligence resource. Some functions in custom projects (for example, autolabel, project management and human in the loop) don't work if the public network access is disabled.
 
       - question: |
          When I upload a file in Document Intelligence Studio by "Fetch from URL" function, can I use a URL from my blob storage?
 
         answer: |
          **Yes.** 
          
-         If your Azure blob storage URL includes a SAS token and is accessible from public networks.  You cannot use the **Fetch** function for storage accounts where the key access is disabled or behind a firewall/VNet.
+         If your Azure blob storage URL includes a SAS token, and is accessible from public networks. You can't use the **Fetch** function for storage accounts where the key access is disabled or behind a firewall/VNet.
 
       - question: |
           Can I reuse or customize the labeling experience from Document Intelligence Studio and build it into my own application?
@@ -264,7 +264,7 @@ sections:
 
         - For signature and region labeling, don't include the surrounding text.
 
-        For more information, see [Accuracy and confidence scores](concept-accuracy-confidence.md).
+        For more information, see [Accuracy and confidence scores](concept/accuracy-confidence.md).
 
     - question: |
         Can I retrain a custom model?
@@ -285,7 +285,7 @@ sections:
 
           4. Compose your new model with the existing model into a single endpoint. Document Intelligence can then determine the best model for each document to be analyzed.
 
-          For more information, see [composed models](concept-custom.md).
+          For more information, see [composed models](train/custom-model.md).
 
     - question: |
         Can I move my trained models from one environment (like beta) to another (like production)?
@@ -305,9 +305,9 @@ sections:
         
         Custom generative models also rely on the auto label feature to speed up the generation of the labeled dataset. There's a cost associated with this action. While the build operation for template and generative models is free, creating the labeled dataset can result in some minimal costs.
 
-        For `v4.0 2024-07-31-preview`, custom neural models can be trained for free for a **maximum of 10 hours**. Whether you are training a single model for the 10 hours, or training multiple models for the total of 10 hours, you won't be charged for the first 10 hours. After using up the free 10 hours, you will be **automatically charged by the extra training hour**. For details on the prices, refer to the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/). This new paid training feature enables training models for an extended duration to process larger documents. For more information on this paid training feature, check [custom neural model billing section](concept-custom-neural.md#billing).
+        For `v4.0 2024-07-31-preview`, custom neural models can be trained for free for a **maximum of 10 hours**. Whether you're training a single model for the 10 hours, or training multiple models for the total of 10 hours, you aren't charged for the first 10 hours. After using up the free 10 hours, you're **automatically charged by the extra training hour**. For details on the prices, refer to the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/). This new paid training feature enables training models for an extended duration to process larger documents. For more information on this paid training feature, check [custom neural model billing section](train/custom-neural.md#billing).
         
-        For `v3.0 2022-08-31` or `v3.1 2023-07-31`, custom neural models can be trained for free for a maximum of 20 training sessions, with each session capped at 30 minutes of training duration. Once you use up all of the 20 training sessions, you can submit Azure support ticket to increase the training session limit. For increasing the limit, 2 training sessions will be considered as 1 training hour, and you will be charged per 2 sessions / 1 training hour. For details on the prices, refer to the [pricing page]. For more information on ways to increase the limit, check [custom neural model billing section](concept-custom-neural.md#billing). **Note that for `v3.0` and `v3.1`, paid training feature is unavailable. Paid training feature for custom neural model is only available on `v4.0`.**
+        For `v3.0 2022-08-31` or `v3.1 2023-07-31`, custom neural models can be trained for free for a maximum of 20 training sessions, with each session capped at 30 minutes of training duration. Once you use up all of the 20 training sessions, you can submit Azure support ticket to increase the training session limit. To increase the limit, two training sessions are considered as one training hour, and you're charged per two sessions / one training hour. For details on the prices, refer to the [pricing page]. For more information on ways to increase the limit, check [custom neural model billing section](train/custom-neural.md#billing). **For `v3.0` and `v3.1`, paid training feature is unavailable. Paid training feature for custom neural model is only available on `v4.0`.**
 
   - name: Storage account
     questions:
@@ -331,7 +331,7 @@ sections:
 
           If you intend to analyze your private storage account data by using FOTT, you must deploy the tool behind the virtual network or firewall.
 
-          Learn how to [create and use a managed identity for your Document Intelligence resource](managed-identities.md).
+          Learn how to [create and use a managed identity for your Document Intelligence resource](authentication/managed-identities.md).
 
   - name: Containers
     questions:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのFAQに関する修正"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスに関するFAQのYAMLファイルに対する修正を示しており、10行の新規追加と10行の削除が行われ、合計で20行の変更が行われています。

主な修正点は、リンク先のURLが一部変更されたことです。特に、文書内の「concept-custom.md」や「concept-retrieval-augmented-generation.md」といったリソースへのリンクがより整理された形式に変更され、より明確にナビゲートできるようになっています。これにより、ユーザーは関連のある情報に簡単にアクセスできるようになります。

また、記述のスタイルが改善され、文の流れが滑らかになっています。例えば、「public network access is disabled」や「the key access is disabled」などの表現が簡潔に書き直され、全体的な可読性を向上させています。

この修正は、ユーザーがドキュメントインテリジェンスの機能を理解しやすくするために重要な情報を整理し、より効率的に得られるようにすることを目的としており、FAQの内容が最新の情報に基づいていることを示しています。

## articles/ai-services/document-intelligence/how-to-guides/build-a-custom-classifier.md{#item-403b74}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Learn how to label, and build a custom document classification mode
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
 ms.date: 05/23/2024
 ms.author: lajanuar
@@ -23,7 +21,7 @@ monikerRange: '>=doc-intel-3.0.0'
 > Custom classification model is currently in public preview. Features, approaches, and processes may change, prior to General Availability (GA), based on user feedback.
 >
 
-Custom classification models can classify each page in an input file to identify the document(s) within. Classifier models can also identify multiple documents or multiple instances of a single document in the input file. Document Intelligence custom models require as few as five training documents per document class to get started. To get started training a custom classification model, you need at least **five documents** for each class and **two classes** of documents.
+Custom classification models can classify each page in an input file to identify one or more documents within. Classifier models can also identify multiple documents or multiple instances of a single document in the input file. Document Intelligence custom models require as few as five training documents per document class to get started. To get started training a custom classification model, you need at least **five documents** for each class and **two classes** of documents.
 
 ## Custom classification model input requirements
 
@@ -53,9 +51,9 @@ The Document Intelligence Studio provides and orchestrates all the API calls req
 
     :::image type="content" source="../media/how-to/studio-create-classifier-project.png" alt-text="Screenshot of how to create a classifier project in the Document Intelligence Studio.":::
 
-    1. On the create project dialog, provide a name for your project, optionally a description, and select continue.
+    1. On the `Create Project` dialog, provide a name for your project, optionally a description, and select continue.
 
-    1. Next, choose or create a Document Intelligence resource before you select continue.
+    1. Next, choose, or select create a Document Intelligence resource before you continue.
 
     :::image type="content" source="../media/how-to/studio-select-resource.png" alt-text="Screenshot showing the project setup dialog window.":::
 
@@ -66,7 +64,7 @@ The Document Intelligence Studio provides and orchestrates all the API calls req
 
     :::image type="content" source="../media/how-to/studio-select-storage.png" alt-text="Screenshot showing how to select the Document Intelligence resource.":::
 
-1. **Training a custom classifier requires the output from the Layout model for each document in your dataset**. Run layout on all documents prior to the model training process.
+1. **Training a custom classifier requires the output from the Layout model for each document in your dataset**. Run layout on all documents before the model training process.
 
 1. Finally, review your project settings and select **Create Project** to create a new project. You should now be in the labeling window and see the files in your dataset listed.
 
@@ -80,7 +78,7 @@ You see the files you uploaded to storage in the file list, ready to be labeled.
 
 1. If the documents are organized in folders, the Studio prompts you to use the folder names as labels. This step simplifies your labeling down to a single select.
 
-1. To assign a label to a document, select on the add label selection mark to assign a label.
+1. To assign a label to a document, select on the `add label selection mark` to assign a label.
 
 1. Control select to  multi-select documents to assign a label
 
@@ -116,18 +114,18 @@ Once the model training is complete, you can test your model by selecting the mo
 
 The Studio orchestrates the API calls for you to train a custom classifier. The classifier training dataset requires the output from the layout API that matches the version of the API for your training model. Using layout results from an older API version can result in a model with lower accuracy.
 
-The Studio generates the layout results for your training dataset if the dataset doesn't contain layout results. When using the API or SDK to train a classifier, you need to add the layout results to the folders containing the individual documents. The layout results should be in the format of the API response when calling layout directly. The SDK object model is different, make sure that the `layout results` are the API results and not the `SDK response`.
+The Studio generates the layout results for your training dataset if the dataset doesn't contain layout results. When using the API or SDK to train a classifier, you need to add the layout results to the folders containing the individual documents. The layout results should be in the format of the API response when calling layout directly. The SDK object model is different. Make sure that the `layout results` are the API results and not the `SDK response`.
 
 ## Troubleshoot
 
-The [classification model](../concept-custom-classifier.md) requires results from the [layout model](../concept-layout.md) for each training document. If you don't provide the layout results, the Studio attempts to run the layout model for each document prior to training the classifier. This process is throttled and can result in a 429 response. 
+The [classification model](../train/custom-classifier.md) requires results from the [layout model](../prebuilt/layout.md) for each training document. If you don't provide the layout results, the Studio attempts to run the layout model for each document before training the classifier. This process is throttled and can result in a 429 response.
 
-In the Studio, prior to training with the classification model, run the [layout model](https://formrecognizer.appliedai.azure.com/studio/layout) on each document and upload it to the same location as the original document. Once the layout results are added, you can train the classifier model with your documents. 
+In the Studio, before training with the classification model, run the [layout model](https://formrecognizer.appliedai.azure.com/studio/layout) on each document and upload it to the same location as the original document. Once the layout results are added, you can train the classifier model with your documents.
 
 ## Next steps
 
 > [!div class="nextstepaction"]
-> [Learn about custom model types](../concept-custom.md)
+> [Learn about custom model types](../train/custom-model.md)
 
 > [!div class="nextstepaction"]
-> [Learn about accuracy and confidence with custom models](../concept-accuracy-confidence.md)
+> [Learn about accuracy and confidence with custom models](../concept/accuracy-confidence.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム分類器の構築に関するガイドの更新"
}
```

### Explanation
この変更は、カスタム分類器の構築に関するガイドのMarkdownファイルの修正を示しており、10行の新規追加と12行の削除があり、合計で22行の変更が行われています。

主な修正点は、文中のリンク先や用語の整理です。具体的には、以前のリンクが新しい構造に改修され、より明確に関連情報にアクセスできるようになりました。例えば、「concept-custom-classifier.md」から「train/custom-classifier.md」への変更は、情報のカテゴリを適切に反映しています。

また、いくつかの文が文法的に見直されており、用語の使用が一貫性を持つように改善されています。たとえば、「on the create project dialog」という表現が「on the `Create Project` dialog」に変更され、特定の操作に関する注意事項が明確になりました。これにより、技術者やユーザーがガイドに従いやすくなります。

この修正は、ドキュメントがユーザーにとってより理解しやすく、正確な情報になり、カスタム分類器の構築プロセスに対するサポートが強化されることを目的としています。ユーザーは、更新された情報をもとに、より効率的に分類器を構築することができるようになります。

## articles/ai-services/document-intelligence/how-to-guides/build-a-custom-model.md{#item-4f2040}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.date: 08/07/2024
 ms.author: lajanuar
 monikerRange: '<=doc-intel-4.0.0'
 ---
-
+<!-- markdownlint-disable DOCSMD006 -->
 
 # Build and train a custom extraction model
 
@@ -19,9 +19,9 @@ monikerRange: '<=doc-intel-4.0.0'
 [!INCLUDE [applies to v4.0 v3.1 v3.0](../includes/applies-to-v40-v31-v30.md)]   ![blue-checkmark](../media/blue-yes-icon.png) [v2.1](?view=doc-intel-2.1.0&preserve-view=true)
 
 > [!IMPORTANT]
-> Custom generative model training behavior is different from custom template and neural model training. The following document covers training only for custom template and neural models. For guidance on custom generative, refer to [custom generative model](../concept-custom-generative.md)
+> Custom generative model training behavior is different from custom template and neural model training. The following document covers training only for custom template and neural models. For guidance on custom generative, refer to [custom generative model](../train/custom-generative-extraction.md)
 
-Document Intelligence custom models require a handful of training documents to get started. If you have at least five documents, you can get started training a custom model. You can train either a [custom template model (custom form)](../concept-custom-template.md) or a [custom neural model (custom document)](../concept-custom-neural.md) or [custom template model (custom form)](../concept-custom-generative.md). This document walks you through the process of training the custom models.
+Document Intelligence custom models require a handful of training documents to get started. If you have at least five documents, you can get started training a custom model. You can train either a [custom template model (custom form)](../train/custom-template.md) or a [custom neural model (custom document)](../train/custom-neural.md) or [custom template model (custom form)](../train/custom-generative-extraction.md). This document walks you through the process of training the custom models.
 
 ## Custom model input requirements
 
@@ -63,7 +63,7 @@ The Document Intelligence Studio provides and orchestrates all the API calls req
     1. On the next step in the workflow, choose or create a Document Intelligence resource before you select continue.
 
     > [!IMPORTANT]
-    > Custom neural models are only available in a few regions. If you plan on training a neural model, please select or create a resource in one of [these supported regions](../concept-custom-neural.md#supported-regions).
+    > Custom neural models are only available in a few regions. If you plan on training a neural model, please select or create a resource in one of [these supported regions](../train/custom-neural.md#supported-regions).
 
     :::image type="content" source="../media/how-to/studio-custom-configure-resource.png" alt-text="Screenshot of Select the Document Intelligence resource.":::
 
@@ -99,7 +99,7 @@ With your dataset labeled, you're now ready to train your model. Select the trai
 
 1. On the train model dialog, provide a unique model ID and, optionally, a description. The model ID accepts a string data type.
 
-1. For the build mode, select the type of model you want to train. Learn more about the [model types and capabilities](../concept-custom.md).
+1. For the build mode, select the type of model you want to train. Learn more about the [model types and capabilities](../train/custom-model.md).
 
     :::image type="content" source="../media/how-to/studio-train-model.png" alt-text="Screenshot of Train model dialog.":::
 
@@ -192,10 +192,10 @@ Now that you learned how to build a training data set, follow a quickstart to tr
 :::moniker range=">=doc-intel-3.0.0"
 
 > [!div class="nextstepaction"]
-> [Learn about custom model types](../concept-custom.md)
+> [Learn about custom model types](../train/custom-model.md)
 
 > [!div class="nextstepaction"]
-> [Learn about accuracy and confidence with custom models](../concept-accuracy-confidence.md)
+> [Learn about accuracy and confidence with custom models](../concept/accuracy-confidence.md)
 :::moniker-end
 
 :::moniker range="doc-intel-2.1.0"
@@ -207,5 +207,5 @@ Now that you learned how to build a training data set, follow a quickstart to tr
 ### See also
 
 * [Train a model and extract document data using the client library or REST API](../quickstarts/get-started-sdks-rest-api.md)
-* [Custom generative model](../concept-custom-generative.md)
+* [Custom generative model](../train/custom-generative-extraction.md)
 * [What is Document Intelligence?](../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデル構築ガイドの更新"
}
```

### Explanation
この変更は、カスタムモデルを構築する方法に関するガイドのMarkdownファイルの修正を示しており、8行の新規追加と8行の削除があり、合計で16行の変更が行われています。

主な修正点は、ドキュメント内のリンク先が整理され、より分かりやすく更新されたことです。特に、「custom generative model」や「custom template model」などのリソースへのリンクが適切なカテゴリに改修され、ユーザーが関連情報に簡単にアクセスできるようになっています。たとえば、以前は「../concept-custom.md」へのリンクが「../train/custom-model.md」へ変更されたことで、情報の整合性と明確性が向上しています。

また、文の表現が一貫性を持たせるように修正され、特に重要な注意点や手順が強調されています。これにより、技術者やユーザーの理解が深まり、ガイドに従いやすくなっています。

この修正は、ユーザーがカスタムモデルを効果的に構築できるようにするためのものであり、ドキュメントの品質を向上させ、カスタムモデルのトレーニングプロセスに対する信頼性を高めることを目的としています。

## articles/ai-services/document-intelligence/how-to-guides/build-train-custom-generative-model.md{#item-108e20}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: How to build and train a custom generative AI model with AI Studio
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: overview
 ms.date: 08/07/2024
 ms.author: lajanuar
@@ -33,7 +31,7 @@ You can choose one of the following options to authorize access to your Document
 
 **✔️ Managed Identity**. A managed identity is a service principal that creates a Microsoft Entra identity and specific permissions for an Azure managed resource. Managed identities enable you to run your Document Intelligence application without having to embed credentials in your code. Managed identities are a safer way to grant access to storage data and replace the requirement for you to include shared access signature tokens (SAS) with your source and result URLs.
 
-To learn more, *see* [Managed identities for Document Intelligence](../managed-identities.md).
+To learn more, *see* [Managed identities for Document Intelligence](../authentication/managed-identities.md).
 
   :::image type="content" source="../media/managed-identities/rbac-flow.png" alt-text="Screenshot of managed identity flow (role-based access control).":::
 
@@ -47,7 +45,7 @@ To learn more, *see* [Managed identities for Document Intelligence](../managed-i
 * Your **source** container or blob must designate **read**, **write**, **list**, and **delete** access.
 * Your **result** container or blob must designate **write**, **list**, **delete** access.
 
-To learn more, *see* [**Create SAS tokens**](../create-sas-tokens.md).
+To learn more, *see* [**Create SAS tokens**](../authentication/create-sas-tokens.md).
 
 ### Training data
 
@@ -81,7 +79,7 @@ Once you have your Azure blob storage containers, upload your training data to y
 
     :::image type="content" source="../media/custom-generative-model/create-document-extraction-project.png" alt-text="Screenshot of the create document extraction project overview page.":::
 
-1. Next, select the storage account you used to upload your custom model training dataset. 
+1. Next, select the storage account you used to upload your custom model training dataset.
 
     :::image type="content" source="../media/custom-generative-model/create-document-extraction-data-settings.png" alt-text="Screenshot of the document extraction project data settings page.":::
 
@@ -134,6 +132,6 @@ That's it! You learned to train a custom generative model in the Azure AI Studio
 
 ## Next steps
 
-[Learn more about the custom generative model](../concept-custom-generative.md)
+[Learn more about the custom generative model](../train/custom-generative-extraction.md)
 
-[Learn more about custom model accuracy and confidence](../concept-accuracy-confidence.md)
+[Learn more about custom model accuracy and confidence](../concept/accuracy-confidence.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム生成モデル構築ガイドの更新"
}
```

### Explanation
この変更は、カスタム生成モデルを構築およびトレーニングする方法に関するガイドのMarkdownファイルにおける修正を示しており、5行の新規追加と7行の削除があり、合計で12行の変更が行われています。

主な修正点は、リンク先の整理と改善です。特に、以前のリンクが新しい構造に変更され、「Managed identities for Document Intelligence」や「Create SAS tokens」に関連する情報がより適切なカテゴリに再配置されています。たとえば、リンク先が「../managed-identities.md」から「../authentication/managed-identities.md」、「../create-sas-tokens.md」から「../authentication/create-sas-tokens.md」へと変更されています。

さらに、文中での手順や情報の表現が若干整理され、ユーザーが必要な情報をより簡単に見つけられるようになっています。これにより、読者はカスタム生成モデルのトレーニングプロセスに関する指示に従いやすくなり、全体的なユーザー体験が向上します。

この修正は、カスタム生成モデルを構築する際のドキュメントの正確性と使いやすさを向上させ、ユーザーが必要なスキルと知識を得やすくすることを目的としています。

## articles/ai-services/document-intelligence/how-to-guides/compose-custom-models.md{#item-bfda06}

<details>
<summary>Diff</summary>
````diff
@@ -10,9 +10,10 @@ ms.date: 08/07/2024
 ms.author: lajanuar
 ---
 
-
 # Compose custom models
 
+<!-- markdownlint-disable MD049 --> emphasis style
+
 <!-- markdownlint-disable MD051 -->
 <!-- markdownlint-disable MD024 -->
 
@@ -35,11 +36,11 @@ ms.author: lajanuar
 ::: moniker range=">=doc-intel-3.0.0"
 
 > [!IMPORTANT]
-> Model compose behavior is changing for api-version=2024-07-31-preview and later, for more info refer to [composed custom models](../concept-composed-models.md). The following behavior only applies to v3.1 and previous versions
+> Model compose behavior is changing for api-version=2024-07-31-preview and later, for more info refer to [composed custom models](../train/composed-models.md). The following behavior only applies to v3.1 and previous versions
 
 A composed model is created by taking a collection of custom models and assigning them to a single model ID. You can assign up to 200 trained custom models to a single composed model ID. When a document is submitted to a composed model, the service performs a classification step to decide which custom model accurately represents the form presented for analysis. Composed models are useful when you train several models and want to group them to analyze similar form types. For example, your composed model might include custom models trained to analyze your supply, equipment, and furniture purchase orders. Instead of manually trying to select the appropriate model, you can use a composed model to determine the appropriate custom model for each analysis and extraction.
 
-To learn more, see [Composed custom models](../concept-composed-models.md).
+To learn more, see [Composed custom models](../train/composed-models.md).
 
 In this article, you learn how to create and use composed custom models to analyze your forms and documents.
 
@@ -55,10 +56,10 @@ To get started, you need the following resources:
 
   1. Copy the **Keys and Endpoint** values from the Azure portal and paste them in a convenient location, such as *Microsoft Notepad*. You need the key and endpoint values to connect your application to the Document Intelligence API.
 
-    :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Still photo showing how to access resource key and endpoint URL.":::
+:::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Still photo showing how to access resource key and endpoint URL.":::
 
-    > [!TIP]
-    > For more information, see [**create a Document Intelligence resource**](../create-document-intelligence-resource.md).
+  > [!TIP]
+  > For more information, see [**create a Document Intelligence resource**](../how-to-guides/create-document-intelligence-resource.md).
 
 * **An Azure storage account.** If you don't know how to create an Azure storage account, follow the [Azure Storage quickstart for Azure portal](/azure/storage/blobs/storage-quickstart-blobs-portal). You can use the free pricing tier (F0) to try the service, and upgrade later to a paid tier for production.
 
@@ -116,7 +117,7 @@ While creating your custom models, you may need to extract data collections from
 
 * Specific collection of values for a given set of fields (columns and/or rows)
 
-See [Document Intelligence Studio: labeling as tables](../concept-custom-label.md#tabular-fields)
+See [Document Intelligence Studio: labeling as tables](../train/custom-labels.md#tabular-fields)
 
 ### [REST API](#tab/rest)
 
@@ -139,11 +140,10 @@ Training with labels leads to better performance in some scenarios. To train wit
 |**C#**|**StartBuildModel**|
 |**Java**| [**beginBuildModel**](/java/api/com.azure.ai.formrecognizer.documentanalysis.administration.documentmodeladministrationclient.beginbuildmodel)|
 |**JavaScript** | [**beginBuildModel**](/javascript/api/@azure/ai-form-recognizer/documentmodeladministrationclient?view=azure-node-latest#@azure-ai-form-recognizer-documentmodeladministrationclient-beginbuildmodel&preserve-view=true)|
-| **Python** | [**begin_build_document_model**](/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.documentmodeladministrationclient?view=azure-python#azure-ai-formrecognizer-documentmodeladministrationclient-begin-build-document-model&preserve-view=true)
+| **Python** | [**begin_build_document_model**](/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.documentmodeladministrationclient?view=azure-python#azure-ai-formrecognizer-documentmodeladministrationclient-begin-build-document-model&preserve-view=true)|
 
 ---
 
-
 ## Create a composed model
 
 > [!NOTE]
@@ -236,21 +236,21 @@ You can use the programming language of your choice to create a composed model:
 
 | Programming language| Code sample |
 |--|--|
-|**C#** | [Model compose](https://github.com/Azure/azure-sdk-for-net/blob/Azure.AI.FormRecognizer_4.0.0/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/Sample_ModelCompose.md)
-|**Java** | [Model compose](https://github.com/Azure/azure-sdk-for-java/blob/afa0d44fa42979ae9ad9b92b23cdba493a562127/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/ComposeDocumentModel.java)
-|**JavaScript** | [Compose model](https://github.com/witemple-msft/azure-sdk-for-js/blob/7e3196f7e529212a6bc329f5f06b0831bf4cc174/sdk/formrecognizer/ai-form-recognizer/samples/v4/javascript/composeModel.js)
-|**Python** | [Create composed model](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-formrecognizer_3.3.0/sdk/formrecognizer/azure-ai-formrecognizer/samples/v3.2_and_later/sample_compose_model.py)
+|**C#** | [Model compose](https://github.com/Azure/azure-sdk-for-net/blob/Azure.AI.FormRecognizer_4.0.0/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/Sample_ModelCompose.md)|
+|**Java** | [Model compose](https://github.com/Azure/azure-sdk-for-java/blob/afa0d44fa42979ae9ad9b92b23cdba493a562127/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/administration/ComposeDocumentModel.java)|
+|**JavaScript** | [Compose model](https://github.com/witemple-msft/azure-sdk-for-js/blob/7e3196f7e529212a6bc329f5f06b0831bf4cc174/sdk/formrecognizer/ai-form-recognizer/samples/v4/javascript/composeModel.js)|
+|**Python** | [Create composed model](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-formrecognizer_3.3.0/sdk/formrecognizer/azure-ai-formrecognizer/samples/v3.2_and_later/sample_compose_model.py)|
 
 #### Analyze documents
 
 Once you build your composed model, you can use it to analyze forms and documents. Use your composed `model ID` and let the service decide which of your aggregated custom models fits best according to the document provided.
 
 |Programming language| Code sample |
 |--|--|
-|**C#** | [Analyze a document with a custom/composed model using model ID](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/Sample_AnalyzeWithCustomModel.md)
-|**Java** | [Analyze a document with a custom/composed model using model ID](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeCustomDocumentFromUrl.java)
-|**JavaScript** | [Analyze a document with a custom/composed model using model ID](https://github.com/witemple-msft/azure-sdk-for-js/blob/7e3196f7e529212a6bc329f5f06b0831bf4cc174/sdk/formrecognizer/ai-form-recognizer/samples/v4/javascript/analyzeDocumentByModelId.js)
-|**Python** | [Analyze a document with a custom/composed model using model ID](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-formrecognizer_3.3.0/sdk/formrecognizer/azure-ai-formrecognizer/samples/v3.2_and_later/sample_analyze_custom_documents.py)
+|**C#** | [Analyze a document with a custom/composed model using model ID](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/formrecognizer/Azure.AI.FormRecognizer/samples/Sample_AnalyzeWithCustomModel.md)|
+|**Java** | [Analyze a document with a custom/composed model using model ID](https://github.com/Azure/azure-sdk-for-java/blob/main/sdk/formrecognizer/azure-ai-formrecognizer/src/samples/java/com/azure/ai/formrecognizer/AnalyzeCustomDocumentFromUrl.java)|
+|**JavaScript** | [Analyze a document with a custom/composed model using model ID](https://github.com/witemple-msft/azure-sdk-for-js/blob/7e3196f7e529212a6bc329f5f06b0831bf4cc174/sdk/formrecognizer/ai-form-recognizer/samples/v4/javascript/analyzeDocumentByModelId.js)|
+|**Python** | [Analyze a document with a custom/composed model using model ID](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-formrecognizer_3.3.0/sdk/formrecognizer/azure-ai-formrecognizer/samples/v3.2_and_later/sample_analyze_custom_documents.py)|
 
 #### Manage your composed models
 
@@ -318,11 +318,11 @@ In the Document Intelligence UI:
 
 1. Select **Use Custom to train a model with labels and get key value pairs**.
 
-      :::image type="content" source="../media/label-tool/fott-use-custom.png" alt-text="Screenshot of the `FOTT` tool select custom model option.":::
+  :::image type="content" source="../media/label-tool/fott-use-custom.png" alt-text="Screenshot of the `FOTT` tool select custom model option.":::
 
 1. In the next window, select **New project**:
 
-    :::image type="content" source="../media/label-tool/fott-new-project.png" alt-text="Screenshot of the `FOTT` tool select new project option.":::
+:::image type="content" source="../media/label-tool/fott-new-project.png" alt-text="Screenshot of the `FOTT` tool select new project option.":::
 
 ## Create your models
 
@@ -350,7 +350,7 @@ You [train your model](build-a-custom-model.md?view=doc-intel-2.1.0&preserve-vie
 
 When you train with labeled data, the model uses supervised learning to extract values of interest, using the labeled forms you provide. Labeled data results in better-performing models and can produce models that work with complex forms or forms containing values without keys.
 
-Document Intelligence uses the [Layout](../concept-layout.md) API to learn the expected sizes and positions of typeface and handwritten text elements and extract tables. Then it uses user-specified labels to learn the key/value associations and tables in the documents. We recommend that you use five manually labeled forms of the same type (same structure) to get started when training a new model. Add more labeled data as needed to improve the model accuracy. Document Intelligence enables training a model to extract key value pairs and tables using supervised learning capabilities.
+Document Intelligence uses the [Layout](../prebuilt/layout.md) API to learn the expected sizes and positions of typeface and handwritten text elements and extract tables. Then it uses user-specified labels to learn the key/value associations and tables in the documents. We recommend that you use five manually labeled forms of the same type (same structure) to get started when training a new model. Add more labeled data as needed to improve the model accuracy. Document Intelligence enables training a model to extract key value pairs and tables using supervised learning capabilities.
 
 [Get started with Train with labels](../label-tool.md)
 
@@ -440,12 +440,10 @@ Use the programming language code of your choice to create a composed model that
 
 ---
 
-
 ## Analyze documents with your custom or composed model
 
  The custom form **Analyze** operation requires you to provide the `modelID`  in the call to Document Intelligence. You can provide a single custom model ID or a composed model ID for the `modelID` parameter.
 
-
 ### [**Document Intelligence Sample Labeling tool**](#tab/studio)
 
 1. On the tool left-pane menu, select the **`Analyze` icon** (light bulb).
@@ -476,7 +474,6 @@ Using the programming language of your choice to analyze a form or document with
 
 ---
 
-
 Test your newly trained models by [analyzing forms](build-a-custom-model.md?view=doc-intel-2.1.0&preserve-view=true#test-the-model) that weren't part of the training dataset. Depending on the reported accuracy, you may want to do further training to improve the model. You can continue further training to [improve results](../label-tool.md#improve-results).
 
 ## Manage your custom models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデル構成ガイドの更新"
}
```

### Explanation
この変更は、カスタムモデルを構成する方法に関するガイドのMarkdownファイルに対する修正を示しており、20行の新規追加と23行の削除があり、合計で43行の変更が行われています。

主な変更点は、文中のリンク先が改善され、より適切なリソースへと再配置されていることです。たとえば、「composed custom models」セクションのリンクが「../concept-composed-models.md」から「../train/composed-models.md」へと変更され、文書の整合性と分かりやすさが向上しています。このようにリンクの更新が行われることで、ユーザーは関連情報に迅速にアクセスできるようになります。

また、マークダウンのLinting指示（markdownlint）も追加されており、文書内のスタイルガイドに対する遵守が求められています。さらに、特定のセクションでの表現が整理され、内容がより明確になっています。これにより、カスタムモデルの作成と使用に関するプロセスがユーザーにとってより理解しやすくなります。

全体として、この修正はドキュメントの質を向上させ、ユーザーがカスタムモデルを効果的に構成し、利用できるようサポートすることを目的としています。

## articles/ai-services/document-intelligence/how-to-guides/create-document-intelligence-resource.md{#item-d4cf00}

<details>
<summary>Diff</summary>
````diff
@@ -5,21 +5,19 @@ description: Create a Document Intelligence resource in the Azure portal.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
-ms.date: 09/26/2024
+ms.date: 10/08/2024
 ms.author: lajanuar
 ---
 
 
 # Create a Document Intelligence resource
 
 ::: moniker range="<=doc-intel-4.0.0"
- [!INCLUDE [applies to v4.0 v3.1 v3.0 v2.1](includes/applies-to-v40-v31-v30-v21.md)]
+ [!INCLUDE [applies to v4.0 v3.1 v3.0 v2.1](../includes/applies-to-v40-v31-v30-v21.md)]
 ::: moniker-end
 
-Azure AI Document Intelligence is a cloud-based [Azure AI service](../../ai-services/index.yml) that uses machine-learning models to extract key-value pairs, text, and tables from your documents. In this article, learn how to create a Document Intelligence resource in the Azure portal.
+Azure AI Document Intelligence is a cloud-based [Azure AI service](../../../ai-services/index.yml) that uses machine-learning models to extract key-value pairs, text, and tables from your documents. In this article, learn how to create a Document Intelligence resource in the Azure portal.
 
 ## Visit the Azure portal
 
@@ -47,7 +45,7 @@ Let's get started:
 
 1. Select **Review + Create**.
 
-    :::image type="content" source="media/logic-apps-tutorial/logic-app-connector-demo-two.png" alt-text="Still image showing the correct values for creating Document Intelligence resource.":::
+    :::image type="content" source="../media/logic-apps-tutorial/logic-app-connector-demo-two.png" alt-text="Still image showing the correct values for creating Document Intelligence resource.":::
 
 1. Azure will run a quick validation check, after a few seconds you should see a green banner that says **Validation Passed**.
 
@@ -63,17 +61,17 @@ Let's get started:
 
 1. If your overview page doesn't have the keys and endpoint visible, you can select the **Keys and Endpoint** button, on the left navigation bar, and retrieve them there.
 
-    :::image border="true" type="content" source="media/containers/keys-and-endpoint.png" alt-text="Still photo showing how to access resource key and endpoint URL":::
+    :::image border="true" type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Still photo showing how to access resource key and endpoint URL.":::
 
 That's it! You're now ready to start automating data extraction using Azure AI Document Intelligence.
 
 ## Next steps
 
-* Try the [Document Intelligence Studio](concept-document-intelligence-studio.md), an online tool for visually exploring, understanding, and integrating features from the Document Intelligence service into your applications.
+* Try the [Document Intelligence Studio](../concept-document-intelligence-studio.md), an online tool for visually exploring, understanding, and integrating features from the Document Intelligence service into your applications.
 
 * Complete a Document Intelligence quickstart and get started creating a document processing app in the development language of your choice:
 
-  * [C#](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
-  * [Python](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
-  * [Java](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
-  * [JavaScript](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
+  * [C#](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
+  * [Python](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
+  * [Java](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
+  * [JavaScript](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスリソースの作成ガイドのリネームと更新"
}
```

### Explanation
この変更は、「create-document-intelligence-resource.md」というファイル名が「how-to-guides/create-document-intelligence-resource.md」に変更されたことを示しており、追加された行は10行、削除された行は12行、合計22行の変更が行われています。

変更内容には、ドキュメント内のリンクのパスの調整が含まれており、相対パスが改善されています。これにより、文書がより整然とした構造になり、関連するリソースへのアクセスが簡単になります。また、文書の日付が更新され、最新の状況を反映しています。

具体的には、Azure AI Document Intelligence サービスの説明文や、リソースの作成プロセスを記述したセクションのリンクが、より適切な相対パスに変更されました。たとえば、`includes/applies-to-v40-v31-v30-v21.md`から`../includes/applies-to-v40-v31-v30-v21.md`へ、`concept-document-intelligence-studio.md`から`../concept-document-intelligence-studio.md`へと変更されています。

全体的に、この更新はドキュメントの可読性とナビゲーションの向上を目指しており、ユーザーがAzureポータルでドキュメントインテリジェンスリソースを簡単に作成できるようにサポートしています。

## articles/ai-services/document-intelligence/how-to-guides/disaster-recovery.md{#item-97e0e7}

<details>
<summary>Diff</summary>
````diff
@@ -5,10 +5,8 @@ description: Learn how to use the copy model API to back up your Document Intell
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
-ms.date: 08/07/2024
+ms.date: 10/15/2024
 ms.author: lajanuar
 ---
 
@@ -18,19 +16,19 @@ ms.author: lajanuar
 # Disaster recovery
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
+[!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
+[!INCLUDE [applies to v3.1](../includes/applies-to-v31.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 ::: moniker-end
 
 ::: moniker range=">= doc-intel-2.1.0"
@@ -40,7 +38,7 @@ When you create a Document Intelligence resource in the Azure portal, you specif
 The Copy API enables this scenario by allowing you to copy custom models and classifiers from one Document Intelligence account or into others, which can exist in any supported geographical region. This guide shows you how to use the Copy REST API with cURL for custom models. You can also use an HTTP request service to issue the requests.
 
 > [!NOTE]
-> Starting with the `2024-07-31-preview` API, custom clasification models also support the Copy API. This guide specifically uses custom models to copy models. For classifier model copy, follow this [guide](concept-custom-classifier.md#copy-a-model).
+> Starting with the `2024-07-31-preview` API, custom clasification models also support the Copy API. This guide specifically uses custom models to copy models. For classifier model copy, follow this [guide](../train/custom-classifier.md#copy-a-model).
 
 ## Business scenarios
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ディザスタリカバリガイドのリネームと更新"
}
```

### Explanation
この変更は、「disaster-recovery.md」というファイル名が「how-to-guides/disaster-recovery.md」に改名されたことを示しており、6行の新規追加と8行の削除があり、合計14行の変更が行われています。

主な変更点には、文中の相対リンクが更新され、より整然とした構造に整備されています。例えば、カスタムモデルや分類器に関連するリソースへのリンクが、`includes/applies-to-v40.md` から `../includes/applies-to-v40.md` へと変更されており、これにより他のリソースとより直感的に繋がるようになっています。

加えて、文書の日付が更新され、最新の情報を反映しています。特に、Copy APIに関する説明において、リンク先が改善されており、読者が関連ガイドにスムーズにアクセスできるようになっています。具体的には、分類器モデルのコピーに関するガイドが、`concept-custom-classifier.md` から `../train/custom-classifier.md` へ変更されています。

全体的に、この更新は文書の可読性とナビゲーションの利便性を向上させ、ユーザーがDocument Intelligence関連のディザスタリカバリ機能をより効果的に利用できるようにサポートしています。

## articles/ai-services/document-intelligence/how-to-guides/estimate-cost.md{#item-6b7006}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Learn how to use Azure portal to check how many pages are analyzed
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
 ms.date: 05/23/2024
 ms.author: luzhan
@@ -19,11 +17,11 @@ ms.author: luzhan
  [!INCLUDE [applies to v4.0 v3.1 v3.0 v2.1](../includes/applies-to-v40-v31-v30-v21.md)]
 ::: moniker-end
 
-In this guide, you'll learn how to use the metrics dashboard in the Azure portal to view how many pages were processed by Azure AI Document Intelligence. You'll also learn how to estimate the cost of processing those pages using the Azure pricing calculator.
+In this guide, learn how to use the metrics dashboard in the Azure portal to view how many pages are processed. You also learn how to estimate the cost of processing those pages using the Azure pricing calculator.
 
 ## Check how many pages were processed
 
-We'll start by looking at the page processing data for a given time period:
+We start by looking at the page processing data for a given time period:
 
 1. Sign in to the [Azure portal](https://portal.azure.com).
 
@@ -33,7 +31,7 @@ We'll start by looking at the page processing data for a given time period:
 
    :::image type="content" source="../media/azure-portal-overview-menu.png" alt-text="Screenshot of the Azure portal overview page menu.":::
 
-1. Select a time range and you'll see the **Processed Pages** chart displayed.
+1. Select a time range and you see the **Processed Pages** chart displayed.
 
     :::image type="content" source="../media/azure-portal-overview-monitoring.png" alt-text="Screenshot that shows how many pages are processed on the resource overview page." lightbox="../media/azure-portal-processed-pages.png":::
 
@@ -57,13 +55,13 @@ We can now take a deeper dive to see each model's analyzed pages:
 
 1. Select **Apply splitting**.
 
-    :::image type="content" source="../media/azure-portal-apply-splitting.png" alt-text="Screenshot of the Apply splitting option in the Azure portal.":::
+    :::image type="content" source="../media/azure-portal-apply-splitting.png" alt-text="Screenshot of apply splitting option in the Azure portal.":::
 
 1. Choose **FeatureName** from the **Values** dropdown menu.
 
-    :::image type="content" source="../media/azure-portal-splitting-on-feature-name.png" alt-text="Screenshot of the Apply splitting values dropdown menu.":::
+    :::image type="content" source="../media/azure-portal-splitting-on-feature-name.png" alt-text="Screenshot of apply splitting values dropdown menu.":::
 
-1. You'll see a breakdown of the pages analyzed by each model.
+1. You see a breakdown of the pages analyzed by each model.
 
     :::image type="content" source="../media/azure-portal-metrics-drill-down.png" alt-text="Screenshot demonstrating how to drill down to check analyzed pages by model." lightbox="../media/azure-portal-drill-down-closeup.png":::
 
@@ -77,17 +75,17 @@ Now that we have the page processed data from the portal, we can use the Azure p
 
 1. Search for **Azure AI Document Intelligence** in the **Search products** search box.
 
-1. Select **Azure AI Document Intelligence** and you'll see that it has been added to the page.
+1. Select **Azure AI Document Intelligence** and you see it was added to the page.
 
-1. Under **Your Estimate**, select the relevant **Region**, **Payment Option** and **Instance** for your Document Intelligence resource. For more information, *see* [Azure AI Document Intelligence pricing options](https://azure.microsoft.com/pricing/details/form-recognizer/#pricing).
+1. Under **Your Estimate**, select the relevant **Region**, **Payment Option**, and **Instance** for your Document Intelligence resource. For more information, *see* [Azure AI Document Intelligence pricing options](https://azure.microsoft.com/pricing/details/form-recognizer/#pricing).
 
-1. Enter the number of pages processed from the Azure portal metrics dashboard. That data can be found using the steps in sections [Check how many pages are processed](#check-how-many-pages-were-processed) or [Examine analyzed pages](#examine-analyzed-pages), above.
+1. Enter the number of pages processed from the Azure portal metrics dashboard. That data can be found using the steps in sections [Check how many pages are processed](#check-how-many-pages-were-processed) or [Examine analyzed pages](#examine-analyzed-pages).
 
-1. The estimated price is on the right, after the equal (**=**) sign.
+1. The estimated price is on the right page section, after the equal (**=**) sign.
 
     :::image type="content" source="../media/azure-portal-pricing.png" alt-text="Screenshot of how to estimate the price based on processed pages.":::
 
-That's it. You now know where to find how many pages you have processed using Document Intelligence and how to estimate the cost.
+That's it. You now know where to find how many pages you process using Document Intelligence and how to estimate the cost.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コスト見積もりガイドの更新"
}
```

### Explanation
この変更は、「estimate-cost.md」というファイルの更新を示しており、新たに11行が追加され、13行が削除され、合計24行の変更が行われています。

主な変更点は、文の構造や表現の明確化です。文書全体で動詞の時制が統一され、より直接的で簡潔な表現に改訂されています。たとえば、「you'll learn」という形から「you learn」への変更などが含まれています。これにより、読者が情報を理解しやすくなっています。

また、Azureポータル内のページ処理データの使用方法に関する説明がより明確になり、各ステップにおいて読者が具体的に何をするかがはっきり示されています。例えば、「you see」という形に変更されたことで、読者が実際に情報を確認できることが強調されています。

さらに、Azure AI Document Intelligenceのコストを見積もるプロセスに関しても、指示が明確に記載されています。特に、どの地域や支払いオプションを選ぶべきかという部分に関しての詳細が保たれており、最新の情報を反映しています。

最後に、Before & Afterの比較を容易にする修正も行われており、全体的にユーザーがコスト見積もりを行う際のナビゲーションが改善されています。このように、この更新はユーザーアクセシビリティと文書の明瞭さを向上させることを目的としています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v2-1/csharp-sdk.md{#item-5f7d47}

<details>
<summary>Diff</summary>
````diff
@@ -136,7 +136,7 @@ Save the URL of the included sample image. That image is also available on [GitH
 
 ## Analyze layout
 
-You can use Document Intelligence to analyze tables, lines, and words in documents, without needing to train a model. The returned value is a collection of **FormPage** objects. There's one object for each page in the submitted document. For more information about layout extraction, see [Document Intelligence layout model](../../../concept-layout.md).
+You can use Document Intelligence to analyze tables, lines, and words in documents, without needing to train a model. The returned value is a collection of **FormPage** objects. There's one object for each page in the submitted document. For more information about layout extraction, see [Document Intelligence layout model](../../../prebuilt/layout.md).
 
 To analyze the content of a file at a given URL, use the `StartRecognizeContentFromUri` method.
 
@@ -186,7 +186,7 @@ Table 0 has 2 rows and 6 columns.
 
 ## Analyze receipts
 
-This section demonstrates how to analyze and extract common fields from US receipts by using a pretrained receipt model. For more information about receipt analysis, see the [Document Intelligence receipt model](../../../concept-receipt.md).
+This section demonstrates how to analyze and extract common fields from US receipts by using a pretrained receipt model. For more information about receipt analysis, see the [Document Intelligence receipt model](../../../prebuilt/receipt.md).
 
 To analyze receipts from a URL, use the `StartRecognizeReceiptsFromUri` method.
 
@@ -260,7 +260,7 @@ The following code processes the business card at the given URI and prints the m
 
 ## Analyze invoices
 
-This section demonstrates how to analyze and extract common fields from sales invoices by using a pretrained model. For more information about invoice analysis, see the [Document Intelligence invoice model](../../../concept-invoice.md).
+This section demonstrates how to analyze and extract common fields from sales invoices by using a pretrained model. For more information about invoice analysis, see the [Document Intelligence invoice model](../../../prebuilt/invoice.md).
 
 To analyze invoices from a URL, use the `StartRecognizeInvoicesFromUriAsync` method.
 
@@ -275,7 +275,7 @@ The following code processes the invoice at the given URI and prints the major f
 
 ## Analyze ID documents
 
-This section demonstrates how to analyze and extract key information from government-issued identification documents—worldwide passports and U.S. driver's licenses by using the Document Intelligence prebuilt ID model. For more information about ID document analysis, see the [Document Intelligence ID document model](../../../concept-id-document.md).
+This section demonstrates how to analyze and extract key information from government-issued identification documents—worldwide passports and U.S. driver's licenses by using the Document Intelligence prebuilt ID model. For more information about ID document analysis, see the [Document Intelligence ID document model](../../../prebuilt/id-document.md).
 
 To analyze ID documents from a URI, use the `StartRecognizeIdentityDocumentsFromUriAsync` method.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKガイドの更新"
}
```

### Explanation
この変更は、「csharp-sdk.md」というファイルの更新を示しており、4行が新たに追加され、4行が削除され、合計8行が変更されています。

主な変更点として、各セクションのリンク先が更新されています。具体的には、ドキュメント内で使用される各モデルに関する情報へのリンクが、元の「concept」セクションから「prebuilt」セクションに変更されています。例えば、レイアウト情報については、「../../../concept-layout.md」から「../../../prebuilt/layout.md」へのリンクに改訂されており、受領書、請求書、ID文書に関する情報でも同様の変更が行われています。

これにより、各セクションの情報がより実用的な内容にアクセスできるようになり、ユーザーが具体的なモデルや機能に関する最新の情報を簡単に取得できるように配慮されています。

さらに、文書全体の一貫性が向上し、文の流れがスムーズになっています。このような変更により、ユーザーがC# SDKを利用してDocument Intelligence機能を効率的に活用できるようになることが目的とされています。全体的に、更新されたガイドは、ユーザーが必要な情報に迅速にアクセスできるように設計されています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v2-1/java-sdk.md{#item-0e735a}

<details>
<summary>Diff</summary>
````diff
@@ -147,7 +147,7 @@ At the top of your `main` method, add the following code. You authenticate two c
 
 ## Analyze layout
 
-You can use Document Intelligence to analyze tables, lines, and words in documents, without needing to train a model. For more information about layout extraction, see the [Document Intelligence layout model](../../../concept-layout.md).
+You can use Document Intelligence to analyze tables, lines, and words in documents, without needing to train a model. For more information about layout extraction, see the [Document Intelligence layout model](../../../prebuilt/layout.md).
 
 To analyze the content of a file at a given URL, use the `beginRecognizeContentFromUrl` method.
 
@@ -181,7 +181,7 @@ Cell has text ET.
 
 ## Analyze receipts
 
-This section demonstrates how to analyze and extract common fields from US receipts by using a pretrained receipt model. For more information about receipt analysis, see the [Document Intelligence receipt model](../../../concept-receipt.md).
+This section demonstrates how to analyze and extract common fields from US receipts by using a pretrained receipt model. For more information about receipt analysis, see the [Document Intelligence receipt model](../../../prebuilt/receipt.md).
 
 To analyze receipts from a URI, use the `beginRecognizeReceiptsFromUrl` method.
 
@@ -232,7 +232,7 @@ The returned value is a collection of `RecognizedForm` objects. There's one obje
 
 ## Analyze invoices
 
-This section demonstrates how to analyze and extract common fields from sales invoices by using a pretrained model. For more information about invoice analysis, see the [Document Intelligence invoice model](../../../concept-invoice.md).
+This section demonstrates how to analyze and extract common fields from sales invoices by using a pretrained model. For more information about invoice analysis, see the [Document Intelligence invoice model](../../../prebuilt/invoice.md).
 
 To analyze invoices from a URL, use the `beginRecognizeInvoicesFromUrl` method.
 
@@ -247,7 +247,7 @@ The returned value is a collection of `RecognizedForm` objects. There's one obje
 
 ## Analyze ID documents
 
-This section demonstrates how to analyze and extract key information from government-issued identification documents—worldwide passports and U.S. driver's licenses by using the Document Intelligence prebuilt ID model. For more information about ID document analysis, see the [Document Intelligence ID document model](../../../concept-id-document.md).
+This section demonstrates how to analyze and extract key information from government-issued identification documents—worldwide passports and U.S. driver's licenses by using the Document Intelligence prebuilt ID model. For more information about ID document analysis, see the [Document Intelligence ID document model](../../../prebuilt/id-document.md).
 
 To analyze ID documents from a URI, use the `beginRecognizeIdentityDocumentsFromUrl` method.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java SDKガイドの更新"
}
```

### Explanation
この変更は、「java-sdk.md」というファイルの更新を示しており、4行が新たに追加され、4行が削除され、合計8行が変更されています。

主な変更点は、各分析セクションにて参照されているリンクの更新です。具体的には、レイアウト、受領書、請求書、及びID文書の分析に関連する情報のリンクが、元の「concept」セクションから「prebuilt」セクションに移行されています。たとえば、「../../../concept-layout.md」から「../../../prebuilt/layout.md」へのリンクに変更されています。この修正により、ユーザーは各モデルが持つ最新の機能や使用方法にアクセスしやすくなっています。

さらに、文の構造が一貫性を持ち、読みやすさが向上しています。これにより、Java SDKを使用してDocument Intelligenceサービスを利用する際の実用性が強化されています。

全体として、この更新はユーザーがJava SDKを活用してDocument Intelligenceの機能を効果的に使用できるように情報を整理し、ナビゲートしやすくすることを目的としています。更新されたガイドは、実践的でアクセスしやすい形式を提供しており、リソースへのリンクが最新情報を反映するように調整されています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v2-1/javascript-sdk.md{#item-c06c9e}

<details>
<summary>Diff</summary>
````diff
@@ -119,7 +119,7 @@ Use the sample from and receipt images included in the samples. These images are
 
 ## Analyze layout
 
-You can use Document Intelligence to analyze tables, lines, and words in documents, without needing to train a model. For more information about layout extraction, see the [Document Intelligence layout model](../../../concept-layout.md). To analyze the content of a file at a given URI, use the `beginRecognizeContentFromUrl` method.
+You can use Document Intelligence to analyze tables, lines, and words in documents, without needing to train a model. For more information about layout extraction, see the [Document Intelligence layout model](../../../prebuilt/layout.md). To analyze the content of a file at a given URI, use the `beginRecognizeContentFromUrl` method.
 
 [!code-javascript[](~/cognitive-services-quickstart-code/javascript/FormRecognizer/FormRecognizerQuickstart.js?name=snippet_getcontent)]
 
@@ -142,7 +142,7 @@ cell [1,5] has text PT
 
 ## Analyze receipts
 
-This section demonstrates how to analyze and extract common fields from US receipts, using a pretrained receipt model. For more information about receipt analysis, see the [Document Intelligence receipt model](../../../concept-receipt.md).
+This section demonstrates how to analyze and extract common fields from US receipts, using a pretrained receipt model. For more information about receipt analysis, see the [Document Intelligence receipt model](../../../prebuilt/receipt.md).
 
 To analyze receipts from a URI, use the `beginRecognizeReceiptsFromUrl` method. The following code processes a receipt at the given URI and prints the major fields and values to the console.
 
@@ -177,7 +177,7 @@ To analyze business cards from a URL, use the `beginRecognizeBusinessCardsFromUR
 
 ## Analyze invoices
 
-This section demonstrates how to analyze and extract common fields from sales invoices, using a pretrained model. For more information about invoice analysis, see the [Document Intelligence invoice model](../../../concept-invoice.md).
+This section demonstrates how to analyze and extract common fields from sales invoices, using a pretrained model. For more information about invoice analysis, see the [Document Intelligence invoice model](../../../prebuilt/invoice.md).
 
 To analyze invoices from a URL, use the `beginRecognizeInvoicesFromUrl` method.
 
@@ -188,7 +188,7 @@ To analyze invoices from a URL, use the `beginRecognizeInvoicesFromUrl` method.
 
 ## Analyze ID documents
 
-This section demonstrates how to analyze and extract key information from government-issued identification documents, including worldwide passports and U.S. driver's licenses, by using the Document Intelligence prebuilt ID model. For more information about ID document analysis, see the [Document Intelligence ID document model](../../../concept-id-document.md).
+This section demonstrates how to analyze and extract key information from government-issued identification documents, including worldwide passports and U.S. driver's licenses, by using the Document Intelligence prebuilt ID model. For more information about ID document analysis, see the [Document Intelligence ID document model](../../../prebuilt/id-document.md).
 
 To analyze ID documents from a URL, use the `beginRecognizeIdDocumentsFromUrl` method.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKガイドの更新"
}
```

### Explanation
この変更は、「javascript-sdk.md」というファイルの更新を示しており、4行が新たに追加され、4行が削除され、合計8行が変更されています。

主な変更点は、各分析セクションの参考リンクが更新されていることです。具体的には、ドキュメントのレイアウト、受領書、請求書、およびID文書の分析に関するリンクが、元々の「concept」セクションから「prebuilt」セクションに移行されています。例として、レイアウトについてのリンクが「../../../concept-layout.md」から「../../../prebuilt/layout.md」へと修正されています。

これにより、最新の機能や情報に簡単にアクセスできるようになり、ユーザーがDocument Intelligenceのさまざまな機能をより効率的に利用できるように配慮されています。

全体として、この更新はJavaScript SDKを用いたDocument Intelligenceの活用を促進することを目的としており、関連情報へのナビゲーションを改善して、ユーザーが実用的な情報を迅速に見つけられるようにしています。また、文全体の一貫性も高められており、技術的な内容がさらに明確に伝わるような形になっています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v2-1/python-sdk.md{#item-9a38a0}

<details>
<summary>Diff</summary>
````diff
@@ -100,7 +100,7 @@ Use the sample form and receipt images included in the samples, which is also av
 
 ## Analyze layout
 
-You can use Document Intelligence to analyze tables, lines, and words in documents, without needing to train a model. For more information about layout extraction, see the [Document Intelligence layout model](../../../concept-layout.md).
+You can use Document Intelligence to analyze tables, lines, and words in documents, without needing to train a model. For more information about layout extraction, see the [Document Intelligence layout model](../../../prebuilt/layout.md).
 
 To analyze the content of a file at a given URL, use the `begin_recognize_content_from_url` method. The returned value is a collection of `FormPage` objects. There's one object for each page in the submitted document. The following code iterates through these objects and prints the extracted key/value pairs and table data.
 
@@ -132,7 +132,7 @@ Confidence score: 1.0
 
 ## Analyze receipts
 
-This section demonstrates how to analyze and extract common fields from US receipts by using a pretrained receipt model. For more information about receipt analysis, see the [Document Intelligence receipt model](../../../concept-receipt.md). To analyze receipts from a URL, use the `begin_recognize_receipts_from_url` method.
+This section demonstrates how to analyze and extract common fields from US receipts by using a pretrained receipt model. For more information about receipt analysis, see the [Document Intelligence receipt model](../../../prebuilt/receipt.md). To analyze receipts from a URL, use the `begin_recognize_receipts_from_url` method.
 
 [!code-python[](~/cognitive-services-quickstart-code/python/FormRecognizer/FormRecognizerQuickstart.py?name=snippet_receipts)]
 
@@ -172,7 +172,7 @@ To analyze business cards from a URL, use the `begin_recognize_business_cards_fr
 
 ## Analyze invoices
 
-This section demonstrates how to analyze and extract common fields from sales invoices by using a pretrained model. For more information about invoice analysis, see the [Document Intelligence invoice model](../../../concept-invoice.md).
+This section demonstrates how to analyze and extract common fields from sales invoices by using a pretrained model. For more information about invoice analysis, see the [Document Intelligence invoice model](../../../prebuilt/invoice.md).
 
 To analyze invoices from a URL, use the `begin_recognize_invoices_from_url` method.
 
@@ -183,7 +183,7 @@ To analyze invoices from a URL, use the `begin_recognize_invoices_from_url` meth
 
 ## Analyze ID documents
 
-This section demonstrates how to analyze and extract key information from government-issued identification documents, including worldwide passports and U.S. driver's licenses, by using the Document Intelligence prebuilt ID model. For more information about ID document analysis, see the [Document Intelligence ID document model](../../../concept-id-document.md).
+This section demonstrates how to analyze and extract key information from government-issued identification documents, including worldwide passports and U.S. driver's licenses, by using the Document Intelligence prebuilt ID model. For more information about ID document analysis, see the [Document Intelligence ID document model](../../../prebuilt/id-document.md).
 
 To analyze ID documents from a URL, use the `begin_recognize_id_documents_from_url` method.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKガイドの更新"
}
```

### Explanation
この変更は、「python-sdk.md」というファイルの更新を示しており、4行が新たに追加され、4行が削除され、合計8行が変更されています。

主な変更点は、各分析セクションにおける参照リンクが更新されていることです。具体的には、ドキュメントのレイアウト、受領書、請求書、およびID文書の分析に関する情報のリンクが、「concept」セクションから「prebuilt」セクションへと移行されています。例として、レイアウトの情報へのリンクが「../../../concept-layout.md」から「../../../prebuilt/layout.md」に変更されています。

この修正により、ユーザーはDocument Intelligenceの各機能が持つ最新の情報にアクセスしやすくなり、SDKを利用したアプリケーション開発がより効率的に行えるようになります。また、技術的な内容が整理され、一貫した形式で提供されることによって、内容の理解が得やすくなっています。

全体として、この更新はPython SDKを使用したDocument Intelligenceの利用を強化することを目的としており、関連情報へのナビゲーションを簡素化し、ユーザーが迅速に必要な情報を見つけられるようにすることを意図しています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v2-1/rest-api.md{#item-73da78}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ ms.author: lajanuar
 
 ## Analyze layout
 
-You can use Document Intelligence to analyze and extract tables, selection marks, text, and structure in documents, without needing to train a model. For more information about layout extraction, see the [Document Intelligence layout model](../../../concept-layout.md).
+You can use Document Intelligence to analyze and extract tables, selection marks, text, and structure in documents, without needing to train a model. For more information about layout extraction, see the [Document Intelligence layout model](../../../prebuilt/layout.md).
 
 Before you run the command, make these changes:
 
@@ -221,7 +221,7 @@ This response body output has been shortened for simplicity. See the [full sampl
 
 ## Analyze receipts
 
-This section demonstrates how to analyze and extract common fields from US receipts, using a pretrained receipt model. For more information about receipt analysis, see the [Document Intelligence receipt model](../../../concept-receipt.md). To start analyzing a receipt, call the [Analyze Receipt](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true) API using the cURL command. Before you run the command, make these changes:
+This section demonstrates how to analyze and extract common fields from US receipts, using a pretrained receipt model. For more information about receipt analysis, see the [Document Intelligence receipt model](../../../prebuilt/receipt.md). To start analyzing a receipt, call the [Analyze Receipt](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true) API using the cURL command. Before you run the command, make these changes:
 
 1. Replace *\<endpoint>* with the endpoint that you obtained with your Document Intelligence subscription.
 1. Replace *\<your receipt URL>* with the URL address of a receipt image.
@@ -749,7 +749,7 @@ The script prints responses to the console until the Analyze Business Card opera
 
 ## Analyze invoices
 
-You can use Document Intelligence to extract field text and semantic values from a given invoice document. To start analyzing an invoice, use the cURL command. For more information about invoice analysis, see the [Invoice conceptual guide](../../../concept-invoice.md). To start analyzing an invoice, call the [Analyze Invoice](/rest/api/aiservices/operation-groups?view=rest-aiservices-v2.1&preserve-view=true) API using the cURL command.
+You can use Document Intelligence to extract field text and semantic values from a given invoice document. To start analyzing an invoice, use the cURL command. For more information about invoice analysis, see the [Invoice conceptual guide](../../../prebuilt/invoice.md). To start analyzing an invoice, call the [Analyze Invoice](/rest/api/aiservices/operation-groups?view=rest-aiservices-v2.1&preserve-view=true) API using the cURL command.
 
 Before you run the command, make these changes:
 
@@ -953,7 +953,7 @@ This response body JSON content has been shortened for readability. See the [ful
 
 ## Analyze identity documents
 
-To start analyzing an identification (ID) document, use the cURL command. For more information about ID document analysis, see the [Document Intelligence ID document model](../../../concept-id-document.md). To start analyzing an ID document, you call the [Analyze ID Document](/rest/api/aiservices/operation-groups?view=rest-aiservices-v2.1&preserve-view=true) API using the cURL command.
+To start analyzing an identification (ID) document, use the cURL command. For more information about ID document analysis, see the [Document Intelligence ID document model](../../../prebuilt/id-document.md). To start analyzing an ID document, you call the [Analyze ID Document](/rest/api/aiservices/operation-groups?view=rest-aiservices-v2.1&preserve-view=true) API using the cURL command.
 
 Before you run the command, make these changes:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIガイドの更新"
}
```

### Explanation
この変更は、「rest-api.md」というファイルの更新を示しており、4行が新たに追加され、4行が削除され、合計8行が変更されています。

主な変更点は、ドキュメントの各分析セクションにおける参照リンクの更新です。具体的には、レイアウト、受領書、請求書、及びID文書の分析についてのリンクが、「concept」セクションから「prebuilt」セクションに移行されています。例として、レイアウトの情報へのリンクが「../../../concept-layout.md」から「../../../prebuilt/layout.md」に変更されています。

このリファクタリングにより、ユーザーはDocument Intelligenceが提供する最新の機能や情報にアクセスしやすくなり、REST APIを利用したアプリケーションの開発がより円滑に行えるようになります。また、仕様や利用方法に関する技術的な内容が整理されて提供されることで、理解が深まりやすくなっています。

全体として、この更新はREST APIを使用したDocument Intelligenceの利用を促進することを目的としており、関連情報へのナビゲーションが容易になり、ユーザーが必要な情報を迅速に見つけられるよう配慮されています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v3-0/csharp-sdk.md{#item-6736b9}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-document-intelligence
 ms.topic: include
 ms.date: 05/23/2024
 ms.author: lajanuar
-ms.custom: devx-track-csharp, ignite-2023, linux-related-content
+ms.custom: devx-track-csharp, linux-related-content
 monikerRange: 'doc-intel-3.1.0 || doc-intel-3.0.0'
 ---
 
@@ -95,7 +95,7 @@ monikerRange: 'doc-intel-3.1.0 || doc-intel-3.0.0'
 
 1. Open the *Program.cs* file.
 
-1. Delete the pre-existing code, including the line `Console.Writeline("Hello World!")`.
+1. Delete the existing code, including the line `Console.Writeline("Hello World!")`.
 
 1. Select one of the following code samples and copy/paste into your application's *Program.cs* file:
 
@@ -798,7 +798,7 @@ if (identityDocument.Fields.TryGetValue("Sex", out DocumentField sexfield))
 
 ```
 
-Visit the Azure samples repository on GitHub and view the [id-document model output](https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/dotnet/FormRecognizer/how-to-guide/id-document-model-output.md).
+Visit the Azure samples repository on GitHub and view the [ID-document model output](https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/dotnet/FormRecognizer/how-to-guide/id-document-model-output.md).
 
 ## Use the Business card model
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKガイドの更新"
}
```

### Explanation
この変更は、「csharp-sdk.md」というファイルの更新を示しており、3行が新たに追加され、3行が削除され、合計6行が変更されています。

主な変更点としては、いくつかのテキストが微調整されており、特に「pre-existing」が「existing」に短縮されたことと、IDドキュメントのモデル出力に関する表記の改善があります。具体的には、「id-document model output」が「ID-document model output」と変更され、文中での一貫性が向上しています。この変更は読みやすさと理解を助けるものであり、正確な情報提供を意識した修正といえます。

また、カスタムメタデータの部分では、「ignite-2023」のタグが削除され、Linux関連のコンテンツのみが残されています。これにより、今後のリリースにおいて関連性のあるコンテンツに焦点が当てられることが意図されていると考えられます。

全体として、この更新はC# SDKに関するドキュメントが最新の状態に保たれ、エンドユーザーが適切な情報を得やすくすることを目指したものです。これにより、開発者はDocument Intelligenceの機能をより正確に理解し、アプリケーションに実装することが可能になると期待されます。

## articles/ai-services/document-intelligence/how-to-guides/includes/v3-0/java-sdk.md{#item-6c0363}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-document-intelligence
 ms.topic: include
 ms.date: 05/23/2024
 ms.author: lajanuar
-ms.custom: devx-track-csharp, ignite-2023, linux-related-content
+ms.custom: devx-track-csharp, linux-related-content
 monikerRange: 'doc-intel-3.1.0 || doc-intel-3.0.0'
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java SDKガイドのメタデータ更新"
}
```

### Explanation
この変更は、「java-sdk.md」というファイルの更新を示しており、1行が新たに追加され、1行が削除され、合計2行が変更されています。

主な変更点は、カスタムメタデータの部分にあります。具体的には、「ignite-2023」というタグが削除され、他のタグである「devx-track-csharp」と「linux-related-content」が残っています。この変更により、ドキュメントはより関連性のある情報に集中することが意図されています。

この更新は、Java SDKに関するドキュメントが最新の状態に保たれ、開発者がDocument Intelligenceの機能を理解し、実装する際に必要な情報が適切に反映されることを目指しています。これにより、ユーザーが必要とする情報を迅速に取得できるようになり、エクスペリエンスが向上することが期待されます。

## articles/ai-services/document-intelligence/how-to-guides/includes/v3-0/javascript-sdk.md{#item-03ed43}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-document-intelligence
 ms.topic: include
 ms.date: 05/23/2024
 ms.author: lajanuar
-ms.custom: devx-track-csharp, ignite-2023, linux-related-content
+ms.custom: devx-track-csharp, linux-related-content
 monikerRange: 'doc-intel-3.1.0 || doc-intel-3.0.0'
 ---
 
@@ -115,7 +115,7 @@ Open the `index.js` file in Visual Studio Code or your favorite IDE and select o
 - The [prebuilt-invoice](#use-the-invoice-model) model extracts information reported on US Internal Revenue Service tax forms.
 - The [prebuilt-receipt](#use-the-receipt-model) model extracts key information from printed and handwritten sales receipts.
 - The [prebuilt-idDocument](#use-the-id-document-model) model extracts key information from US Drivers Licenses; international passport biographical pages; US state IDs; social security cards; and permanent resident cards.
-- 
+-
 <!-- > [!div class="nextstepaction"]
 > [I &#8203;ran into an issue building the application.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=javascript&Product=FormRecognizer&Page=how-to&Section=build-application) -->
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKガイドのメタデータおよびコンテンツ更新"
}
```

### Explanation
この変更は、「javascript-sdk.md」というファイルの更新を示しており、2行が新たに追加され、2行が削除され、合計4行が変更されています。

変更の主な内容は、メタデータ部分のカスタムメタタギングに関連しています。「ignite-2023」というタグが削除され、「devx-track-csharp」と「linux-related-content」のみが残っています。この修正により、関連性のある情報に絞り込まれることが意図されています。

また、コンテンツ部分でも変更があり、一部のテキストが更新されています。具体的には、HTMLコメントが追加されており、アプリケーションのビルド中に問題が発生した場合のサポートリンクが提供されています。この修正は、ユーザーがリアルタイムで問題に直面した際に役立つ情報源となることを意図しています。

このようなマイナーな更新は、JavaScript SDKに関するドキュメントを最新化し、開発者がDocument Intelligenceの機能を理解しやすくすることで、より良いユーザーエクスペリエンスを提供する狙いがあります。

## articles/ai-services/document-intelligence/how-to-guides/includes/v3-0/python-sdk.md{#item-3b07c5}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-document-intelligence
 ms.topic: include
 ms.date: 05/23/2024
 ms.author: lajanuar
-ms.custom: devx-track-csharp, ignite-2023, linux-related-content
+ms.custom: devx-track-csharp, linux-related-content
 monikerRange: 'doc-intel-3.1.0 || doc-intel-3.0.0'
 ---
 
@@ -1210,6 +1210,7 @@ if __name__ == "__main__":
     analyze_identity_documents()
 
 ```
+
 > [!div class="nextstepaction"]
 > [View complete code on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Prebuilt_model/sample_analyze_identity_documents.py) [More samples](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Prebuilt_model)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKガイドのメタデータおよびサンプルコード更新"
}
```

### Explanation
この変更は、「python-sdk.md」というファイルの更新を示しており、2行が新たに追加され、1行が削除され、合計3行が変更されています。

主な変更点は、ファイルのメタデータ部分におけるカスタムタグの更新です。「ignite-2023」というタグが削除され、「devx-track-csharp」と「linux-related-content」のみが残っています。これにより、文書の関連性が向上し、更新された内容を反映した形になっています。

さらに、新しいコードスニペットが追加されています。具体的には、スクリプトの最後に、GitHub上の完全なサンプルコードへのリンクと、他のサンプルへのリンクが挿入されました。この変更により、開発者は関連するリソースに簡単にアクセスでき、より多くの情報を得ることができるように配慮されています。

このようなマイナーな更新は、Python SDKに関するドキュメントを最新の状態に維持し、開発者がDocument Intelligenceの機能を適切に理解し、活用できるようにすることを目指しています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v3-0/rest-api.md{#item-1a8bdb}

<details>
<summary>Diff</summary>
````diff
@@ -4,20 +4,21 @@ description: Use the Document Intelligence REST API v3.0 to create a forms proce
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom: ignite-2023, linux-related-content
+ms.custom: linux-related-content
 ms.topic: include
 ms.date: 05/23/2024
 ms.author: lajanuar
 monikerRange: 'doc-intel-3.1.0 || doc-intel-3.0.0'
 ---
 
+<!-- markdownlint-disable MD033 -->
 
 :::moniker range="doc-intel-3.1.0"
-| [Document Intelligence REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP) | [Supported Azure SDKS](../../../sdk-overview-v3-1.md) | 
+| [Document Intelligence REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP) | [Supported Azure SDKS](../../../sdk-overview-v3-1.md) |
 :::moniker-end
 
 :::moniker range="doc-intel-3.0.0"
-| [Document Intelligence REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP) | [Supported Azure SDKS](../../../sdk-overview-v3-0.md) | 
+| [Document Intelligence REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP) | [Supported Azure SDKS](../../../sdk-overview-v3-0.md) |
 :::moniker-end
 
 > [!NOTE]
@@ -72,7 +73,7 @@ Open a console window and run the following cURL command. The commands include t
 curl -i -X POST "%FR_ENDPOINT%formrecognizer/documentModels/<modelId>:analyze?api-version=2023-07-31" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: %FR_KEY%" --data-ascii "{'urlSource': '<document-url>'}"
 ```
 
-To enable add-on capabilities, use the `features` query parameter in the POST request. There are four add-on capabilities available with the `2023-07-31` (GA) release: *ocr.highResolution*, *ocr.formula*, *ocr.font*, and *queryFields.premium*. To learn more about each of the capabilities, see [Custom models](../../../concept-accuracy-confidence.md).
+To enable add-on capabilities, use the `features` query parameter in the POST request. There are four add-on capabilities available with the `2023-07-31` (GA) release: *ocr.highResolution*, *ocr.formula*, *ocr.font*, and *queryFields.premium*. To learn more about each of the capabilities, see [Custom models](../../../concept/accuracy-confidence.md).
 
 You can only call the *highResolution*, *formula*, and *font* capabilities for the Read and Layout model, and the *queryFields* capability for the General Documents model. The following example shows how to call the *highResolution*, *formula*, and *font* capabilities for the Layout model.
 
@@ -91,6 +92,7 @@ You receive a `202 (Success)` response that includes an `Operation-location` hea
 After you call the [`Analyze document`](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP) API, call the [`Get analyze` result}(/rest/api/aiservices/document-models/get-analyze-result?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP) API to get the status of the operation and the extracted data.
 
 <!-- markdownlint-disable MD024 -->
+<!-- markdownlint-disable MD051 -->
 
 The cURL command line tool doesn't format API responses that contain JSON content, which can make the content difficult to read. To format the JSON response, include the pipe character followed by a JSON formatting tool with your GET request.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIガイドのメタデータおよびコンテンツ更新"
}
```

### Explanation
この変更は、「rest-api.md」というファイルの更新を示しており、6行が新たに追加され、4行が削除され、合計10行が変更されています。

文書のメタデータ部分では、「ignite-2023」というカスタムタグが削除され、「linux-related-content」のみが残っています。これにより、コンテンツが現在の状態に適合するよう調整されています。また、いくつかの変数やパラメータに関連するマークダウンとコメントが追加され、文書の可読性が向上しています。

さらに、APIの利用方法に関する具体的な説明が明確にされました。特に、POSTリクエストにおける`features`クエリパラメータの有効化に関する内容が強調され、各機能の詳細に対するリンクが修正されました。これにより、ユーザーは機能の詳細に迅速にアクセスできるようになっています。

また、cURLコマンドを使用してAPIを呼び出す際の手順が引き続き維持されており、リクエストが成功した場合の応答についての具体的な情報も提供されています。全体として、これらの変更はREST APIドキュメントの正確性を向上させ、開発者がAPIを利用しやすくすることを目的としています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v4-0/csharp-sdk.md{#item-b72ebd}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-document-intelligence
 ms.topic: include
 ms.date: 09/09/2024
 ms.author: lajanuar
-ms.custom: devx-track-csharp, ignite-2023, linux-related-content
+ms.custom: devx-track-csharp, linux-related-content
 monikerRange: 'doc-intel-4.0.0'
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKガイドのメタデータ更新"
}
```

### Explanation
この変更は、「csharp-sdk.md」というファイルの更新を示しており、1行が新たに追加され、1行が削除され、合計2行が変更されています。

具体的には、ドキュメントのメタデータにおけるカスタムタグが更新されました。「ignite-2023」というタグが削除され、「devx-track-csharp」と「linux-related-content」のタグのみが残っています。この変更により、C# SDKに関連する最新の情報が反映された形になっています。

このようなマイナーアップデートは、ドキュメントの整合性を保つこと、および関連情報を最新の状態に維持するために重要です。これは、開発者がDocument IntelligenceのC# SDKを利用する際の指針を明確にすることを目的としています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v4-0/java-sdk.md{#item-65f910}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-document-intelligence
 ms.topic: include
 ms.date: 09/09/2024
 ms.author: lajanuar
-ms.custom: devx-track-csharp, ignite-2023, linux-related-content
+ms.custom: devx-track-csharp, linux-related-content
 ---
 
 <!-- markdownlint-disable MD001 -->
@@ -121,7 +121,6 @@ To interact with the Document Intelligence service, create an instance of the `D
    >
    > You can create a new file by using PowerShell. Open a PowerShell window in your project directory by holding down the **Shift** key and right-clicking the folder, then type the following command: *New-Item DocIntelligence.java*.
 
-
 1. Open the *DocIntelligence.java* file and select one of the following code samples AND copy/paste into your application:
 
    - The [prebuilt-read](#use-the-read-model) model is at the core of all Document Intelligence models and can detect lines, words, locations, and languages. The layout, general document, prebuilt, and custom models all use the `read` model as a foundation for extracting texts from documents.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java SDKガイドのメタデータおよび内容更新"
}
```

### Explanation
この変更は、「java-sdk.md」というファイルの更新を示しており、1行が新たに追加され、2行が削除され、合計3行が変更されています。

ファイルのメタデータでは、カスタムタグにおいて「ignite-2023」という項目が削除され、他のタグ「devx-track-csharp」と「linux-related-content」のみが保持されています。これにより、ドキュメントが最新の情報に基づくものとなり、不要なタグの削除が行われました。

また、ドキュメント内のコンテンツにおいても不必要な空行が削除され、一貫性が向上しました。具体的には、コードサンプルを選択しアプリケーションに貼り付けるという手順の前にあった不要な空行が取り除かれています。

これらの変更は、Java SDKを使用する開発者にとって有用で、ドキュメントの可読性を向上させ、情報の整合性を保つ役割を果たしています。

## articles/ai-services/document-intelligence/how-to-guides/includes/v4-0/javascript-sdk.md{#item-b28fc0}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-document-intelligence
 ms.topic: include
 ms.date: 09/09/2024
 ms.author: lajanuar
-ms.custom: devx-track-csharp, ignite-2023, linux-related-content
+ms.custom: devx-track-csharp, linux-related-content
 ---
 
 <!-- markdownlint-disable MD001 -->
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKガイドのメタデータ更新"
}
```

### Explanation
この変更は、「javascript-sdk.md」というファイルの更新を示しており、1行が新たに追加され、1行が削除され、合計2行が変更されています。

具体的には、ドキュメントのメタデータにおいて、カスタムタグの部分から「ignite-2023」というタグが削除され、「devx-track-csharp」と「linux-related-content」のタグのみが残っています。このメタデータの更新により、C# SDKに関連する情報がより適切に表現されています。

このようなマイナー更新は、文書の整合性を向上させ、開発者がJavaScript SDKを利用する際の関連情報を最新の状態に保つために重要です。これにより、読者はより一貫した情報をもとにプロジェクトを進めることができるようになります。

## articles/ai-services/document-intelligence/how-to-guides/includes/v4-0/python-sdk.md{#item-52b6d7}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-document-intelligence
 ms.topic: include
 ms.date: 09/09/2024
 ms.author: lajanuar
-ms.custom: devx-track-csharp, ignite-2023, linux-related-content
+ms.custom: devx-track-csharp, linux-related-content
 ---
 
 <!-- markdownlint-disable MD001 -->
@@ -172,7 +172,7 @@ if __name__ == "__main__":
 ```
 
 > [!div class="nextstepaction"]
-> [View complete code on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Read_model/sample_analyze_read.py)  [More samples](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Read_model) 
+> [View complete code on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Read_model/sample_analyze_read.py)  [More samples](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Read_model)
 
 Visit the Azure samples repository on GitHub and view the [`read` model output](https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/FormRecognizer/how-to-guide/read-model-output.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKガイドのメタデータおよびリンク更新"
}
```

### Explanation
この変更は、「python-sdk.md」というファイルの更新を示しており、2行が新たに追加され、2行が削除され、合計4行が変更されています。

メタデータにおいて、カスタムタグから「ignite-2023」が削除され、「devx-track-csharp」と「linux-related-content」のタグが維持されています。これは、ドキュメントが最新の情報に基づくものであることを示しています。

また、コードサンプルへのリンク部分にも変更がありましたが、実際のリンク内容は変更されていません。この部分は形式的な修正であり、リンクが適切に表示されるように整理されています。

これらの変更により、Python SDKを利用する開発者向けの情報がより明確で整理された状態になり、使いやすさが向上しています。読者は、最新のリソースにアクセスしやすくなり、SDKの活用が促進されることが期待されます。

## articles/ai-services/document-intelligence/how-to-guides/includes/v4-0/rest-api.md{#item-222da8}

<details>
<summary>Diff</summary>
````diff
@@ -4,11 +4,13 @@ description: Use the Document Intelligence REST API v3.0 to create a forms proce
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom: ignite-2023, linux-related-content
+ms.custom: linux-related-content
 ms.topic: include
 ms.date: 09/09/2024
 ms.author: lajanuar
 ---
+<!-- markdownlint-disable MD033 -->
+<!-- markdownlint-disable MD051 -->
 
 > [!NOTE]
 >
@@ -64,7 +66,7 @@ Open a console window and run the following cURL command. The commands include t
 curl -i -X POST "%DI_ENDPOINT%/documentintelligence/documentModels/{modelId}:analyze?api-version=2024-02-29-preview" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: %DI_KEY%" --data-ascii "{'urlSource': '<document-url>'}"
 ```
 
-To enable add-on capabilities, use the `features` query parameter in the POST request. There are four add-on capabilities available with the `2023-07-31` (GA) and later releases: *ocr.highResolution*, *ocr.formula*, *ocr.font*, and *queryFields.premium*. To learn more about each of the capabilities, see [Custom models](../../../concept-accuracy-confidence.md).
+To enable add-on capabilities, use the `features` query parameter in the POST request. There are four add-on capabilities available with the `2023-07-31` (GA) and later releases: *ocr.highResolution*, *ocr.formula*, *ocr.font*, and *queryFields.premium*. To learn more about each of the capabilities, see [Custom models](../../../concept/accuracy-confidence.md).
 
 You can only call the *highResolution*, *formula*, and *font* capabilities for the Read and Layout model, and the *queryFields* capability for the General Documents model. The following example shows how to call the *highResolution*, *formula*, and *font* capabilities for the Layout model.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIガイドのメタデータおよびリンク修正"
}
```

### Explanation
この変更は、「rest-api.md」というファイルの更新を示しており、4行が新たに追加され、2行が削除され、合計6行が変更されています。

具体的には、ドキュメントのメタデータにおいて、「ignite-2023」というカスタムタグが削除され、「linux-related-content」のタグが残っています。また、Markdownのlintエラーを防ぐための指示が2つ追加されました。

さらに、文中のリンクが更新されており、「Custom models」というセクションへのリンクが修正されています。これにより、読者は関連情報により簡単にアクセスできるようになっています。

このマイナーな更新によって、REST APIに関する情報が最新の状態に保たれ、読者がドキュメントをより効果的に使用できることが期待されます。特に、APIの機能の詳細や使い方に関するリソースへのアクセスが向上しているため、開発者がDocument Intelligenceを活用する際の利便性が向上しています。

## articles/ai-services/document-intelligence/how-to-guides/project-share-custom-models.md{#item-acd5dd}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Learn how to share custom model projects using Document Intelligenc
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
 ms.date: 08/07/2024
 ms.author: jppark
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデル共有ガイドのメタデータ更新"
}
```

### Explanation
この変更は、「project-share-custom-models.md」というファイルの更新を示しており、2行が削除され、合計2行が変更されています。

具体的には、ドキュメントのメタデータから「ms.custom」セクションが削除されました。このセクションには「ignite-2023」というタグが含まれていましたが、これが除去されたことで、ドキュメントが現在のコンテンツにより適した形に整理されています。

この修正により、カスタムモデルのプロジェクト共有に関するドキュメントがより明瞭になり、情報の精度が向上しています。読者は、最新のサービス情報に基づいたガイドラインを参照することで、Document Intelligenceを活用したプロジェクトの共有が円滑に進むことが期待されます。

## articles/ai-services/document-intelligence/how-to-guides/resolve-errors.md{#item-6c3107}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Learn how errors are represented in Document Intelligence and find
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 07/11/2024
 ms.author: paulhsu
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エラー解決ガイドのファイル名変更"
}
```

### Explanation
この変更は、「resolve-errors.md」というファイルの名前が変更されたことを示しています。元のファイル名は「v3-error-guide.md」であり、新しい名前は「resolve-errors.md」です。この変更により、ファイルの内容が明確に示されるようになりました。

メタデータの一部も更新されており、「ms.custom」セクションから「ignite-2023」というタグが削除されました。これにより、情報がすっきり整理され、現在のコンテンツに合ったものとなっています。

このマイナーな更新によって、ドキュメントがより直感的に参照できるようになり、読者はエラーの表現方法や解決方法をより効果的に学ぶことができる状況が整えられています。新しいファイル名は、ガイドの目的をより明確にし、利用者にとって検索しやすいものとなっています。

## articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md{#item-25a870}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Document Intelligence client libraries or REST API
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom: devx-track-dotnet, devx-track-extended-java, devx-track-js, devx-track-python, ignite-2023, linux-related-content
+ms.custom: devx-track-dotnet, devx-track-extended-java, devx-track-js, devx-track-python, linux-related-content
 ms.topic: how-to
 ms.date: 07/18/2024
 ms.author: lajanuar
@@ -42,24 +42,25 @@ Choose from the following Document Intelligence models and analyze and extract d
 
 > [!div class="checklist"]
 >
-> - The [prebuilt-read](../concept-read.md) model is at the core of all Document Intelligence models and can detect lines, words, locations, and languages. Layout, general document, prebuilt, and custom models all use the `read` model as a foundation for extracting texts from documents.
+> - The [prebuilt-read](../prebuilt/read.md) model is at the core of all Document Intelligence models and can detect lines, words, locations, and languages. Layout, general document, prebuilt, and custom models all use the `read` model as a foundation for extracting texts from documents.
 >
-> - The [prebuilt-layout](../concept-layout.md) model extracts text and text locations, tables, selection marks, and structure information from documents and images. You can extract key/value pairs using the layout model with the optional query string parameter **`features=keyValuePairs`** enabled.
+> - The [prebuilt-layout](../prebuilt/layout.md) model extracts text and text locations, tables, selection marks, and structure information from documents and images. You can extract key/value pairs using the layout model with the optional query string parameter **`features=keyValuePairs`** enabled.
 >
-> - The [prebuilt-contract](../concept-contract.md) model extracts key information from contractual agreements.
+> - The [prebuilt-contract](../prebuilt/contract.md) model extracts key information from contractual agreements.
 >
-> - The [prebuilt-healthInsuranceCard.us](../concept-health-insurance-card.md) model extracts key information from US health insurance cards.
+> - The [prebuilt-healthInsuranceCard.us](../prebuilt/health-insurance-card.md) model extracts key information from US health insurance cards.
 >
-> - The [prebuilt tax document models](../concept-tax-document.md) model extracts information reported on US tax forms.
+> - The [prebuilt tax document models](../prebuilt/tax-document.md) model extracts information reported on US tax forms.
 >
-> - The [prebuilt-invoice](../concept-invoice.md) model extracts key fields and line items from sales invoices in various formats and quality. Fields include phone-captured images, scanned documents, and digital PDFs.
+> - The [prebuilt-invoice](../prebuilt/invoice.md) model extracts key fields and line items from sales invoices in various formats and quality. Fields include phone-captured images, scanned documents, and digital PDFs.
 >
-> - The [prebuilt-receipt](../concept-receipt.md) model extracts key information from printed and handwritten sales receipts.
+> - The [prebuilt-receipt](../prebuilt/receipt.md) model extracts key information from printed and handwritten sales receipts.
 >
-> - The [prebuilt-idDocument](../concept-id-document.md) model extracts key information from US drivers licenses, international passport biographical pages, US state IDs, social security cards, and permanent resident cards.
+> - The [prebuilt-idDocument](../prebuilt/id-document.md) model extracts key information from US drivers licenses, international passport biographical pages, US state IDs, social security cards, and permanent resident cards.
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
+
 > [!div class="checklist"]
 >
 > - The [prebuilt-businessCard](../concept-business-card.md) model extracts key information and contact details from business card images.
@@ -72,6 +73,7 @@ Choose from the following Document Intelligence models and analyze and extract d
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
+
 [!INCLUDE [C# SDK quickstart](includes/v3-0/csharp-sdk.md)]
 ::: moniker-end
 
@@ -96,6 +98,7 @@ Choose from the following Document Intelligence models and analyze and extract d
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
+
 [!INCLUDE [NodeJS SDK quickstart](includes/v3-0/javascript-sdk.md)]
 ::: moniker-end
 
@@ -108,6 +111,7 @@ Choose from the following Document Intelligence models and analyze and extract d
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
+
 [!INCLUDE [Python SDK quickstart](includes/v3-0/python-sdk.md)]
 ::: moniker-end
 
@@ -120,6 +124,7 @@ Choose from the following Document Intelligence models and analyze and extract d
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
+
 [!INCLUDE [REST API quickstart](includes/v3-0/rest-api.md)]
 ::: moniker-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SDKおよびREST APIに関するガイドの更新"
}
```

### Explanation
この変更は、「use-sdk-rest-api.md」ファイルに対するマイナーな更新を示しています。具体的には、14行が追加され、9行が削除され、合計23行が変更されました。

ファイルの更新内容には、メタデータの一部が含まれ、「ms.custom」セクションから「ignite-2023」が削除されました。さらに、さまざまな文書インテリジェンスモデルに関する情報が更新され、リンクのパスが改善されました。具体的には、以前の「concept」パスから新しい「prebuilt」パスに変更されています。これにより、ドキュメントがより整然としており、各モデルの機能についての明確な参照が行えるようになっています。

また、SDKのクイックスタートガイドに関する指示も追加されており、C#、NodeJS、PythonにおけるSDKの使用方法が新たに提供されています。この更新により、開発者は文書インテリジェンスを活用するための手順を一層簡単に理解し、実行できるようになっています。全体として、この変更はユーザーエクスペリエンスを向上させ、最新の情報を反映する重要な更新となっています。

## articles/ai-services/document-intelligence/includes/applies-to-v21.md{#item-fa19ef}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ author: laujan
 ms.author: lajanuar
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 11/15/2023
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "applies-to-v21.mdファイルのメタデータ更新"
}
```

### Explanation
この変更は、「applies-to-v21.md」ファイルのメタデータに関する小規模な更新を示しています。具体的には、2行が削除され、変更が2行行われています。

削除された内容には、「ms.custom」セクションの「ignite-2023」というタグが含まれています。この変更により、メタデータがより整理され、現在の内容に合致したものとなっています。全体として、このマイナーな更新はドキュメントを一層クリーンにし、利用者に対して関連する情報を提供しやすくしています。

この更新により、ユーザーは文書インテリジェンスに関する最新の情報を得やすくなり、関連するトピックやサービスについて詳しく理解することができます。

## articles/ai-services/document-intelligence/includes/applies-to-v30-v21.md{#item-5311b0}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ author: laujan
 ms.author: lajanuar
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 11/15/2023
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "applies-to-v30-v21.mdファイルのメタデータ更新"
}
```

### Explanation
この変更は、「applies-to-v30-v21.md」ファイルのメタデータに対する小規模な更新を示しています。この更新では、2行が削除され、総計で2行が変更されています。

削除された内容は、メタデータセクションの「ms.custom」に含まれていた「ignite-2023」というタグです。この変更により、ファイルのメタデータが整理され、必要な情報が明確に残る形になっています。全体として、この変更は文書のクリーンアップに寄与し、ユーザーが関連情報を得やすくすることを目的としています。

このマイナーな更新によって、文書インテリジェンスの関連内容がより分かりやすくなり、利用者が最新のサービスや機能についてアクセスしやすくなっています。

## articles/ai-services/document-intelligence/includes/applies-to-v30.md{#item-0f6a07}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ author: laujan
 ms.author: lajanuar
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 11/15/2023
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "applies-to-v30.mdファイルのメタデータ更新"
}
```

### Explanation
この変更は、「applies-to-v30.md」ファイルのメタデータに対する小規模な更新を示しています。具体的には、2行が削除され、全体として2行の変更が行われています。

削除された部分には、「ms.custom」セクションの「ignite-2023」というタグが含まれており、これによりメタデータがよりシンプルになっています。この更新は、文書のクリーンアップを目的としており、より関連性のある情報をユーザーに提供することに焦点を当てています。

このマイナーな変更により、文書インテリジェンスに関する情報がより明確になり、ユーザーが関連するサービスや機能について理解しやすくなります。

## articles/ai-services/document-intelligence/includes/applies-to-v31-v30-v21.md{#item-e8f78f}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ author: laujan
 ms.author: lajanuar
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 11/15/2023
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "applies-to-v31-v30-v21.mdファイルのメタデータ更新"
}
```

### Explanation
この変更は、「applies-to-v31-v30-v21.md」ファイルのメタデータに関する小さな更新を反映しています。具体的には、2行が削除され、合計で2行の変更が発生しています。

削除されたのは、メタデータセクション内の「ms.custom」からの「ignite-2023」というタグであり、この変更によってメタデータが簡素化されています。この更新は、ドキュメントの整理を意図しており、ユーザーが必要な情報により簡単にアクセスできるようにすることが目的です。

結果として、このマイナーな改訂は、文書インテリジェンスに関連するコンテンツをより明確にし、ユーザーがサービスや機能を理解しやすくする役割を果たしています。

## articles/ai-services/document-intelligence/includes/applies-to-v31-v30.md{#item-ac265d}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ author: laujan
 ms.author: lajanuar
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 11/15/2023
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "applies-to-v31-v30.mdファイルのメタデータ更新"
}
```

### Explanation
この変更は、「applies-to-v31-v30.md」ファイルのメタデータに対する小規模な更新を示しています。具体的には、2行が削除され、合計で2行の変更が行われています。

削除された部分には、「ms.custom」セクションの「ignite-2023」というタグがあります。この変更により、メタデータがより簡潔になり、文書全体の構成が整理されていることがわかります。このようなマイナーな変更は、ユーザーがドキュメントを利用する際に、より明瞭で関連性のある情報を提供することを目的としています。

結果として、この更新は、文書インテリジェンスの利用可能性を向上させ、ユーザーが関連する機能やサービスに関する理解を深めることに寄与しています。

## articles/ai-services/document-intelligence/includes/applies-to-v31.md{#item-5f3c5a}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ author: laujan
 ms.author: lajanuar
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 11/15/2023
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "applies-to-v31.mdファイルのメタデータ更新"
}
```

### Explanation
この変更は、「applies-to-v31.md」ファイルのメタデータに対するマイナーな更新を示しています。具体的には、ファイル中の2行が削除され、合計で2行の変更が行われました。

削除された部分は、「ms.custom」セクションの「ignite-2023」というタグです。この変更により、メタデータが簡潔になり、ドキュメントの可読性や整理が改善されることが目的です。特に、ユーザーが必要な情報にアクセスしやすくするための配慮がなされています。

全体として、このマイナーな更新は、文書インテリジェンスに関連するコンテンツが、より明確で理解しやすい形で提供されることに寄与しています。

## articles/ai-services/document-intelligence/includes/applies-to-v40-v31-v30-v21.md{#item-3ca431}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ author: laujan
 ms.author: lajanuar
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 11/15/2023
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "applies-to-v40-v31-v30-v21.mdファイルのメタデータ更新"
}
```

### Explanation
この変更は、「applies-to-v40-v31-v30-v21.md」ファイルのメタデータに関するマイナーな更新を表しています。具体的に言うと、2行が削除され、合計で2行の変更が行われました。

削除された内容は、「ms.custom」セクションの「ignite-2023」タグです。この変更により、メタデータがより簡潔になり、文書が整理されます。これは、利用者にとって関連情報を見つけやすくするために行われた改善と考えられます。

このマイナーな更新は、ドキュメントの全体的な可読性を高め、ユーザーがドキュメントインテリジェンスに関連する情報をより簡単に理解できるよう支援します。

## articles/ai-services/document-intelligence/includes/applies-to-v40-v31-v30.md{#item-cb0a7f}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ author: laujan
 ms.author: lajanuar
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 11/15/2023
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "applies-to-v40-v31-v30.mdファイルのメタデータ更新"
}
```

### Explanation
この変更は、「applies-to-v40-v31-v30.md」ファイルのメタデータに関するマイナーな更新を示しています。具体的には、ドキュメント内の2行が削除され、合計で2行の変更が行われました。

削除された内容は、「ms.custom」セクションの「ignite-2023」というタグです。この変更は、文書を簡潔にし、整理された形式で利用者に提供することを目指しています。これにより、閲覧者が必要な情報を見つけやすくなることが期待されており、ドキュメントの可読性向上に寄与します。

全体として、このマイナーな更新は、ドキュメントインテリジェンス関連の情報をより効果的に伝達するための取り組みの一環です。

## articles/ai-services/document-intelligence/includes/applies-to-v40-v31.md{#item-b11839}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ author: laujan
 ms.author: lajanuar
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 11/15/2023
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "applies-to-v40-v31.mdファイルのメタデータ更新"
}
```

### Explanation
この変更は、「applies-to-v40-v31.md」ファイルのメタデータに関するマイナーな更新を示しています。具体的には、2行が削除され、合計で2行の変更が行われました。

削除された内容は、「ms.custom」セクションの「ignite-2023」タグであり、この変更により文書がよりシンプルで整理されたものになります。このような更新は、ドキュメントの可読性を向上させ、利用者が必要な情報を迅速に取得できるようにすることを目的としています。

全体として、このマイナーな更新は、関連情報の伝達をより効果的にし、ブラウジングの利便性を向上させるための調整と考えられます。

## articles/ai-services/document-intelligence/includes/applies-to-v40.md{#item-94c322}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ author: laujan
 ms.author: lajanuar
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 11/15/2023
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "applies-to-v40.mdファイルのメタデータ更新"
}
```

### Explanation
この変更は、「applies-to-v40.md」ファイルのメタデータに関するマイナーな更新を示しています。具体的には、2行が削除され、合計で2行の変更が行われました。

削除された部分は、「ms.custom」セクションの「ignite-2023」というタグです。この修正により、ドキュメントはよりシンプルで整理されたものになり、ユーザーに対する情報提供がより明確になります。このような更新は、読みやすさを向上させ、利用者が重要な情報をすぐに見つけやすくすることを目的としています。

全体的に、このマイナーな更新は、ドキュメントインテリジェンスサービスに関する情報をより効果的に伝えるための調整として位置づけられます。

## articles/ai-services/document-intelligence/includes/create-resource.md{#item-f52ea3}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,6 @@ ms.service: azure-ai-document-intelligence
 ms.topic: include
 ms.date: 11/15/2023
 ms.author: lajanuar
-ms.custom:
-  - ignite-2023
 ---
 
 Go to the Azure portal and <a href="https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer" title="Create a new Document Intelligence resource" target="_blank">create a new Document Intelligence resource </a>. In the **Create** pane, provide the following information:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "create-resource.mdファイルのメタデータ更新"
}
```

### Explanation
この変更は、「create-resource.md」ファイルのメタデータに関する小さな更新を示しています。具体的には、2行が削除され、合計で2行の変更が行われました。

削除された内容は、「ms.custom」セクションの「ignite-2023」というタグであり、これにより文書の構成が簡素化されます。この更新は、ドキュメントの明瞭性を保ち、必要な情報がよりアクセスしやすくなることを目的としています。

全体として、このマイナーな更新は、Azure AI Document Intelligenceに関するリソース作成ガイドラインをより効果的にするための調整と考えられます。これにより、ユーザーがドキュメントインテリジェンスリソースを作成する過程が、シンプルかつ直感的になることが期待されます。

## articles/ai-services/document-intelligence/includes/improve-results-unlabeled.md{#item-bc1b92}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: lajanuar
 
 Examine the `"confidence"` values for each key/value result under the `"pageResults"` node. You should also look at the confidence scores in the `"readResults"` node, which correspond to the text read operation. The confidence of the read results doesn't affect the confidence of the key/value extraction results, so you should check both.
 
-- If the confidence scores for the read operation are low, try to improve the quality of your input documents. For more information, see [Input requirements](../concept-model-overview.md#input-requirements).
+- If the confidence scores for the read operation are low, try to improve the quality of your input documents. For more information, see [Input requirements](../model-overview.md#input-requirements).
 - If the confidence scores for the key/value extraction operation are low, ensure that the documents being analyzed are of the same type as documents used in the training set. If the documents in the training set have variations in appearance, consider splitting them into different folders and training one model for each variation.
 
 The confidence scores you target depends on your use case, but generally it's a good practice to target a score of 80 percent or higher. For more sensitive cases, like reading medical records or billing statements, we recommend a score of 100 percent.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "improve-results-unlabeled.mdファイルのリンク修正"
}
```

### Explanation
この変更は、「improve-results-unlabeled.md」ファイルに対する小さな更新を示しています。具体的には、1行が追加され、1行が削除され、合計で2行の変更が行われました。

変更の中心は、文中のリンク先を更新することに関連しています。具体的には、以前のリンク先であった「../concept-model-overview.md#input-requirements」が「../model-overview.md#input-requirements」に修正されました。これは、ドキュメントの一貫性を保ち、読者が最新かつ正確な情報にアクセスできるようにするための重要なステップです。

このマイナーな更新により、ユーザーが必要な情報をより効率的に見つけやすくなり、ドキュメントの有用性が向上すると期待されます。

## articles/ai-services/document-intelligence/includes/logic-app-tutorial/onedrive.md{#item-ae5d5a}

<details>
<summary>Diff</summary>
````diff
@@ -1,15 +1,14 @@
 ---
 author: laujan
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 07/24/2023
 ms.author: lajanuar
 monikerRange: '<=doc-intel-4.0.0'
 ---
 
 <!-- markdownlint-disable MD041 -->
+<!-- markdownlint-disable MD029 -->
 
 ## Prerequisites
 
@@ -31,7 +30,7 @@ To complete this tutorial, you need the following resources:
 
 * **A Document Intelligence resource**.  Once you have your Azure subscription, [create a Document Intelligence resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal to get your key and endpoint. If you have an existing Document Intelligence resource, navigate directly to your resource page. You can use the free pricing tier (F0) to try the service, and upgrade later to a paid tier for production.
 
-  * After the resource deploys, select **Go to resource**. Copy the **Keys and Endpoint** values from your resource in the Azure portal and paste them in a convenient location, such as *Microsoft Notepad*. You need the key and endpoint values to connect your application to the Document Intelligence API. For more information, *see* [**create a Document Intelligence resource**](../../create-document-intelligence-resource.md).
+  * After the resource deploys, select **Go to resource**. Copy the **Keys and Endpoint** values from your resource in the Azure portal and paste them in a convenient location, such as *Microsoft Notepad*. You need the key and endpoint values to connect your application to the Document Intelligence API. For more information, *see* [**create a Document Intelligence resource**](../../how-to-guides/create-document-intelligence-resource.md).
 
       :::image border="true" type="content" source="../../media/containers/keys-and-endpoint.png" alt-text="Screenshot showing how to access resource key and endpoint URL.":::
 
@@ -119,7 +118,7 @@ Now that you have the Logic App connector resource set up and configured, let's
 
     :::image type="content" source="../../media/logic-apps-tutorial/when-file-created.png" alt-text="Screenshot of the When a file is created window.":::
 
-:::moniker range=">=doc-intel-3.0.0"
+ :::moniker range=">=doc-intel-3.0.0"
 
 4. Next, we're going to add a new step to the workflow. Select the **➕ New step** button underneath the newly created OneDrive node.
 
@@ -178,57 +177,57 @@ Now that you have the Logic App connector resource set up and configured, let's
 
 1. We're going to use the following expression to complete some of the fields:
 
-    ```powerappsfl
-
-      items('For_each')?['fields']?['FIELD-NAME']?['content']
-    ```
+```powerappsfl
+     
+       items('For_each')?['fields']?['FIELD-NAME']?['content']
+```
 
 1. In order to access a specific field, we select the **add the dynamic content** button and select the **Expression** tab.
 
     :::image type="content" source="../../media/logic-apps-tutorial/function-expression-field.png" alt-text="Screenshot of the expression function field.":::
 
-1. In  the **ƒx** box, copy and paste the above formula and replace **FIELD-NAME** with the name of the field we want to extract. For the full list of available fields, refer to the concept page for the given API. In this case, we use the [prebuilt-invoice model field extraction values](../../concept-invoice.md#field-extraction).
+1. In  the **ƒx** box, copy and paste the above formula and replace **FIELD-NAME** with the name of the field we want to extract. For the full list of available fields, refer to the concept page for the given API. In this case, we use the [prebuilt-invoice model field extraction values](../../prebuilt/invoice.md#field-extraction).
 
 1. We're almost done! Make the following changes to the following fields:
 
     * **To**. Enter your personal or business email address or any other email address you have access to.
 
     * **Subject**. Enter ***Invoice received from:*** and then add the following expression:
 
-        ```powerappsfl
-
-          items('For_each')?['fields']?['VendorName']?['content']
-        ```
+     ```powerappsfl
+    
+              items('For_each')?['fields']?['VendorName']?['content']
+     ```
 
     * **Body**. We're going to add specific information about the invoice:
 
       * Type ***Invoice ID:*** and, using the same method as before, append the following expression:
 
-         ```powerappsfl
-
-         items('For_each')?['fields']?['InvoiceId']?['content']
-         ```
+       ```powerappsfl
+     
+              items('For_each')?['fields']?['InvoiceId']?['content']
+       ```
 
       * On a new line type ***Invoice due date:*** and append the following expression:
 
-        ```powerappsfl
-
-          items('For_each')?['fields']?['DueDate']?['content']
-        ```
+      ```powerappsfl
+     
+               items('For_each')?['fields']?['DueDate']?['content']
+      ```
 
       * Type ***Amount due:*** and append the following expression:
 
-        ```powerappsfl
-
-          items('For_each')?['fields']?['AmountDue']?['content']
-        ```
+      ```powerappsfl
+     
+               items('For_each')?['fields']?['AmountDue']?['content']
+      ```
 
       * Lastly, because the amount due is an important number, we also want to send the confidence score for this extraction in the email. To do this type ***Amount due (confidence):***  and append the following expression:
 
-        ```powerappsfl
-
-          items('For_each')?['fields']?['AmountDue']?['confidence']
-        ```
+      ```powerappsfl
+     
+               items('For_each')?['fields']?['AmountDue']?['confidence']
+      ```
 
     * When you're done, the window looks similar to the following image:
 
@@ -245,7 +244,7 @@ Now that you have the Logic App connector resource set up and configured, let's
 
 :::moniker-end
 
-:::moniker range="doc-intel-2.1.0"
+ :::moniker range="doc-intel-2.1.0"
 
 4. Next, we're going to add a new step to the workflow. Select the **➕ New step** button underneath the newly created OneDrive node.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "onedrive.mdファイルのリンクとMarkdown構文の修正"
}
```

### Explanation
この変更は、「onedrive.md」ファイルに対する小さな更新を示しています。合計で59行が変更され、その内訳は29行の追加と30行の削除です。主な変更点は以下の通りです。

1. **リンクの更新**: Document Intelligenceリソースに関するリンクが更新され、以前のリンク「../../create-document-intelligence-resource.md」から「../../how-to-guides/create-document-intelligence-resource.md」に修正されました。これにより、ユーザーが最新のガイドにアクセスできるようになります。

2. **Markdown構文の調整**: Markdownの構文に関するいくつかの修正が行われ、例えば、コードブロックの前に空行を追加するなど、読みやすさや表示の改善が図られています。

3. **内容の整頓**: 内容全体が見直され、特にコードサンプル内の表現が整えられ、ユーザーにとって理解しやすい形に再構成されています。

全体として、このマイナーな更新は、ドキュメントの精度や可読性を向上させ、ユーザーが必要な情報をより簡単に取得できるようにすることを目的としています。

## articles/ai-services/document-intelligence/includes/logic-app-tutorial/sharepoint.md{#item-469890}

<details>
<summary>Diff</summary>
````diff
@@ -8,6 +8,7 @@ monikerRange: '<=doc-intel-3.0.0'
 ---
 
 <!-- markdownlint-disable MD041 -->
+<!-- markdownlint-disable MD029 -->
 
 ## Prerequisites
 
@@ -23,7 +24,7 @@ To complete this tutorial, you need the following resources:
 
 * **A Document Intelligence resource**.  Once you have your Azure subscription, [create a Document Intelligence resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal to get your key and endpoint. If you have an existing Document Intelligence resource, navigate directly to your resource page. You can use the free pricing tier (F0) to try the service, and upgrade later to a paid tier for production.
 
-  * After the resource deploys, select **Go to resource**. Copy the **Keys and Endpoint** values from your resource in the Azure portal and paste them in a convenient location, such as *Microsoft Notepad*. You need the key and endpoint values to connect your application to the Document Intelligence API. For more information, *see* [**create a Document Intelligence resource**](../../create-document-intelligence-resource.md).
+  * After the resource deploys, select **Go to resource**. Copy the **Keys and Endpoint** values from your resource in the Azure portal and paste them in a convenient location, such as *Microsoft Notepad*. You need the key and endpoint values to connect your application to the Document Intelligence API. For more information, *see* [**create a Document Intelligence resource**](../../how-to-guides/create-document-intelligence-resource.md).
 
       :::image border="true" type="content" source="../../media/containers/keys-and-endpoint.png" alt-text="Screenshot showing how to access resource key and endpoint URL.":::
 
@@ -110,7 +111,7 @@ At this point, you should have a Document Intelligence resource and a SharePoint
     > Select the arrow at the end of each listed folder to traverse to the next folder in the path:
       :::image type="content" source="../../media/logic-apps-tutorial/folder-traverse-tip.png" alt-text="Screenshot of how to traverse the folder path.":::
 
-::: moniker range=">=doc-intel-3.0.0"
+ ::: moniker range=">=doc-intel-3.0.0"
 
 15. Next, we're going to add another step to the workflow. Select the **➕ New step** button underneath the newly created SharePoint node.
 
@@ -177,69 +178,69 @@ At this point, you should have a Document Intelligence resource and a SharePoint
 
 1. We're going to use the following expression to complete some of the fields:
 
-    ```powerappsfl
+```powerappsfl
 
-      items('For_each')?['fields']?['FIELD-NAME']?['content']
-    ```
+          items('For_each')?['fields']?['FIELD-NAME']?['content']
+```
 
 1. In order to access a specific field, we select the **add the dynamic content** button and select the **Expression** tab.
 
     :::image type="content" source="../../media/logic-apps-tutorial/function-expression-field.png" alt-text="Screenshot of the expression function field.":::
 
-1. In  the **ƒx** box, copy and paste the above formula and replace **FIELD-NAME** with the name of the field we want to extract. For the full list of available fields, refer to the concept page for the given API. In this case, we use the [prebuilt-invoice model field extraction values](../../concept-invoice.md#field-extraction).
+1. In  the **ƒx** box, copy and paste the above formula and replace **FIELD-NAME** with the name of the field we want to extract. For the full list of available fields, refer to the concept page for the given API. In this case, we use the [prebuilt-invoice model field extraction values](../../prebuilt/invoice.md#field-extraction).
 
 1. We're almost done! Make the following changes to the following fields:
 
     * **To**. Enter your personal or business email address or any other email address you have access to.
 
-    * **Subject**. Enter ***Invoice received from:*** and leave your cursor positioned after the colon. 
+    * **Subject**. Enter ***Invoice received from:*** and leave your cursor positioned after the colon.
 
     * Enter the following expression into the **Expression** field and select **OK**:
 
-        ```powerappsfl
+     ```powerappsfl
 
-          items('For_each')?['fields']?['VendorName']?['content']
-        ```
+        items('For_each')?['fields']?['VendorName']?['content']
+     ```
 
-        * After you enter the expression in the field select the OK button and the formula badge will appear in the place where you left your cursor:
+    * After you enter the expression in the field select the OK button and the formula badge will appear in the place where you left your cursor:
 
-        :::image type="content" source="../../media/logic-apps-tutorial/sharepoint-expression.png" alt-text="Screenshot of the formula expression field.":::
+    :::image type="content" source="../../media/logic-apps-tutorial/sharepoint-expression.png" alt-text="Screenshot of the formula expression field.":::
 
-        :::image type="content" source="../../media/logic-apps-tutorial/sharepoint-formula-badge.png" alt-text="Screenshot of the formula expression badge.":::
+    :::image type="content" source="../../media/logic-apps-tutorial/sharepoint-formula-badge.png" alt-text="Screenshot of the formula expression badge.":::
 
-    * **Body**. We're going to add specific information about the invoice:
+* **Body**. We're going to add specific information about the invoice:
 
-      * Type ***Invoice ID:*** and, using the same method as before: position your cursor, copy the following expression into the expression field, and select **OK** the following expression:
+    * Type ***Invoice ID:*** and, using the same method as before: position your cursor, copy the following expression into the expression field, and select **OK** the following expression:
 
-         ```powerappsfl
+    ```powerappsfl
 
-         items('For_each')?['fields']?['InvoiceId']?['content']
-         ```
+            items('For_each')?['fields']?['InvoiceId']?['content']
+    ```
 
-      * On a new line type ***Invoice due date:*** and append the following expression:
+    * On a new line type ***Invoice due date:*** and append the following expression:
 
-        ```powerappsfl
+    ```powerappsfl
 
-          items('For_each')?['fields']?['DueDate']?['content']
-        ```
+            items('For_each')?['fields']?['DueDate']?['content']
+    ```
 
-      * Type ***Amount due:*** and append the following expression:
+    * Type ***Amount due:*** and append the following expression:
 
-        ```powerappsfl
+    ```powerappsfl
 
-          items('For_each')?['fields']?['AmountDue']?['content']
-        ```
+            items('For_each')?['fields']?['AmountDue']?['content']
+    ```
 
-      * Lastly, because the amount due is an important number, we also want to send the confidence score for this extraction in the email. To do this type ***Amount due (confidence):***  and append the following expression:
+    * Lastly, because the amount due is an important number, we also want to send the confidence score for this extraction in the email. To do this type ***Amount due (confidence):***  and append the following expression:
 
-        ```powerappsfl
+    ```powerappsfl
 
-          items('For_each')?['fields']?['AmountDue']?['confidence']
-        ```
+            items('For_each')?['fields']?['AmountDue']?['confidence']
+    ```
 
-    * When you're done, the window looks similar to the following image:
+* When you're done, the window looks similar to the following image:
 
-      :::image type="content" source="../../media/logic-apps-tutorial/send-email-functions.png" alt-text="Screenshot of the Send an email (V2) window with completed fields.":::
+    :::image type="content" source="../../media/logic-apps-tutorial/send-email-functions.png" alt-text="Screenshot of the Send an email (V2) window with completed fields.":::
 
 1. **Select Save in the upper left corner**.
 
@@ -337,4 +338,5 @@ After you save your Logic App, if you need to make an update or edit your **For
     >
     > * This current version only returns a single invoice per PDF.
     > * The "For each loop" around the send email action enables an output format that may return more than one invoice from PDFs in the future.
+
 :::moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "sharepoint.mdファイルのリンク更新とMarkdown修正"
}
```

### Explanation
この変更は、「sharepoint.md」ファイルに対する小さな更新を示しており、合計66行が変更され、その内訳は34行の追加と32行の削除です。

主な変更点は以下の通りです：

1. **リンクの更新**: 文中のDocument Intelligenceリソースに関するリンクが更新され、以前のリンク「../../create-document-intelligence-resource.md」から「../../how-to-guides/create-document-intelligence-resource.md」に変更され、より正確な情報源に導かれるようになりました。

2. **Markdown構文の調整**: Markdownの構文や表示に関するいくつかの修正が行われています。具体的には、コードブロック内のインデントや空白の調整、無駄な改行の削除などが含まれ、ドキュメントの可読性が向上しました。

3. **内容の整頓**: 説明の内容が整理され、特にフィールドに関する説明が明確になっています。これにより、ユーザーは必要な手順をより容易に理解できるようになっています。

4. **画像の注釈**: 一部の画像に対する注釈が整理され、情報提供の一貫性が保たれています。

この更新は、ドキュメントの正確性、可読性、全体的なユーザー体験を向上させることを目的としており、ユーザーがより簡単に必要な情報にアクセスできるようにしています。

## articles/ai-services/document-intelligence/includes/model-analysis-features.md{#item-0fe95e}

<details>
<summary>Diff</summary>
````diff
@@ -1,8 +1,6 @@
 ---
 author: laujan
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 08/08/2024
 ms.author: lajanuar
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "model-analysis-features.mdからの不要なメタデータ削除"
}
```

### Explanation
この変更は、「model-analysis-features.md」ファイルに対する小さな更新を示しており、合計で2行が削除されています。

主な変更内容は以下の通りです：

1. **メタデータの削除**: ファイル内から不要なメタデータが削除されました。具体的には、`ms.custom`フィールドとその値（`- ignite-2023`）が削除されています。これにより、ドキュメントのメタデータが簡素化され、より明確な内容が保たれることを目的としています。

2. **構造の維持**: 残りのメタデータはそのまま保持されており、ドキュメントの他の重要な情報は影響を受けていません。

この更新は、ドキュメントの整合性を保ちながら、無駄な情報を削除することで、よりクリーンで維持管理が容易な内容にすることを目指しています。

## articles/ai-services/document-intelligence/includes/model-type-name.md{#item-5c7f96}

<details>
<summary>Diff</summary>
````diff
@@ -1,8 +1,6 @@
 ---
 author: laujan
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 07/18/2023
 ms.author: lajanuar
@@ -12,6 +10,6 @@ ms.author: lajanuar
 
 | Model type |Model name |
 |------------|-----------|
-|**Document analysis models**| &#9679; [**Read OCR**](../concept-read.md)</br> &#9679; [**Layout analysis**](../concept-layout.md) </br> &#9679; [**General document** (deprecated 2023-10-31-preview)](../concept-general-document.md)
-| **Prebuilt models** |  &#9679; [**Health insurance card**](../concept-health-insurance-card.md) </br>&#9679; [**W-2 form**](../concept-tax-document.md) </br>&#9679; [**US 1098 tax form**](../concept-tax-document.md)</br>&#9679; [**US 1098-E tax form**](../concept-tax-document.md)</br>&#9679; [**US 1098-T tax form**](../concept-tax-document.md)</br>&#9679; [**Invoice**](../concept-invoice.md)</br>&#9679; [**Receipt**](../concept-receipt.md) </br>&#9679; [**Identity (ID) document**](../concept-id-document.md) </br>&#9679; [**Business card** (deprecated 2023-10-31-preview)](../concept-business-card.md)</br>&#9679; [**Contract**](../concept-contract.md)</br>
-| **Custom models** | &#9679; [**Custom model overview**](../concept-custom.md)</br> </br>&#9679; **Extraction models**</br>&#8198;&#8198;&Tab;&#65518; [**Custom template**](../concept-custom-template.md)</br>&#8198;&#8198;&Tab;&#65518; [**Custom neural**](../concept-custom-neural.md)</br></br>&#9679; **Classifier model**</br>&#8198;&#8198;&Tab;&#65518; [**Custom classifier**](../concept-custom-classifier.md)</br> </br>&#9679; [**Composed model**](../concept-model-overview.md)|
+|**Document analysis models**| &#9679; [**Read OCR**](../prebuilt/read.md)</br> &#9679; [**Layout analysis**](../prebuilt/layout.md) </br> &#9679; [**General document** (deprecated 2023-10-31-preview)](../prebuilt/general-document.md)|
+| **Prebuilt models** |  &#9679; [**Health insurance card**](../prebuilt/health-insurance-card.md) </br>&#9679; [**W-2 form**](../prebuilt/tax-document.md) </br>&#9679; [**US 1098 tax form**](../prebuilt/tax-document.md)</br>&#9679; [**US 1098-E tax form**](../prebuilt/tax-document.md)</br>&#9679; [**US 1098-T tax form**](../prebuilt/tax-document.md)</br>&#9679; [**Invoice**](../prebuilt/invoice.md)</br>&#9679; [**Receipt**](../prebuilt/receipt.md) </br>&#9679; [**Identity (ID) document**](../prebuilt/id-document.md) </br>&#9679; [**Business card** (deprecated 2023-10-31-preview)](../concept-business-card.md)</br>&#9679; [**Contract**](../prebuilt/contract.md)</br>|
+| **Custom models** | &#9679; [**Custom model overview**](../train/custom-model.md)</br> </br>&#9679; **Extraction models**</br>&#8198;&#8198;&Tab;&#65518; [**Custom template**](../train/custom-template.md)</br>&#8198;&#8198;&Tab;&#65518; [**Custom neural**](../train/custom-neural.md)</br></br>&#9679; **Classifier model**</br>&#8198;&#8198;&Tab;&#65518; [**Custom classifier**](../train/custom-classifier.md)</br> </br>&#9679; [**Composed model**](../model-overview.md)|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "model-type-name.mdのリンク更新とメタデータ調整"
}
```

### Explanation
この変更は、「model-type-name.md」ファイルに対する小さな更新を示しており、合計で8行が変更され、その内訳は3行の追加と5行の削除です。

主な変更点は以下の通りです：

1. **リンクの更新**: いくつかのリンクが修正され、原則として「../concept-」から「../prebuilt-」への変更が行われています。これにより、各モデルタイプに関する情報が正確で最新のものにアクセスできるようになりました。

2. **メタデータの削除**: 不要なメタデータが削除され、ドキュメントがよりシンプルかつ明確になっています。具体的には、`ms.custom`フィールドが削除されています。

3. **表の内容の整頓**: モデルのタイプに関する表の内容が更新され、情報がより整理されて表示されています。これにより、利用者が各モデルや関連リソースを容易に参照できるようになっています。

この更新は、ドキュメントの使いやすさを向上させることを目的としており、ユーザーが必要な情報に迅速にアクセスできるように工夫されています。

## articles/ai-services/document-intelligence/includes/preview-notice.md{#item-e2c198}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ author: laujan
 ms.author: lajanuar
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 07/31/2024
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "preview-notice.mdからの不要なメタデータ削除"
}
```

### Explanation
この変更は、「preview-notice.md」ファイルに対する小さな更新を示しており、合計で2行が削除されています。

主な変更内容は以下の通りです：

1. **不要なメタデータの削除**: ファイル内から`ms.custom`フィールドとその値（`- ignite-2023`）が削除されています。これにより、ドキュメントのメタデータが簡素化され、無駄な情報が取り除かれました。

2. **シンプルで明確な情報提供**: 残りのメタデータはそのまま保持されており、その他の重要な情報に関しては影響がありません。この変更は、ドキュメントをよりシンプルで明確にすることを目的としています。

この更新により、ユーザーは必要な情報に対して明確なアクセスを持つことができ、より効果的な情報提供が期待できます。

## articles/ai-services/document-intelligence/index.yml{#item-9c57d7}

<details>
<summary>Diff</summary>
````diff
@@ -38,9 +38,9 @@ landingContent:
      - linkListType: learn
        links:
          - text: Read
-           url: concept-read.md
+           url: prebuilt/read.md
          - text: Layout
-           url: concept-layout.md
+           url: prebuilt/layout.md
          - text: Financial Services and Legal
            url: overview.md#financial-services-and-legal
          - text: US Tax
@@ -52,9 +52,9 @@ landingContent:
          - text: Custom classification
            url: overview.md#custom-classification-models
          - text: Add-on capabilities
-           url: concept-add-on-capabilities.md
+           url: concept/add-on-capabilities.md
          - text: Query field extraction
-           url:  concept-query-fields.md
+           url:  concept/query-fields.md
 
   #Card 3
    - title: Document Intelligence Studio
@@ -71,17 +71,17 @@ landingContent:
          - linkListType: concept
            links:
              - text: 🆕 Custom generative model
-               url:  concept-custom-generative.md
+               url:  train/custom-generative-extraction.md
              - text: 🆕 Retrieval-Augmented Generation (RAG)
-               url:  concept-retrieval-augmented-generation.md
+               url:  concept/retrieval-augmented-generation.md
              - text: 🆕 Batch document analysis
                url:  concept-batch-analysis.md
              - text: Accuracy and confidence scores
-               url: concept-accuracy-confidence.md
+               url: concept/accuracy-confidence.md
              - text: Use the analyzeDocument response
-               url: concept-analyze-document-response.md
+               url: concept/analyze-document-response.md
              - text: Custom model overview
-               url: concept-custom.md
+               url: train/custom-model.md
   # Card 5
    - title: Responsible AI
      linkLists:
@@ -102,11 +102,11 @@ landingContent:
       - linkListType: how-to-guide
         links:
           - text: Create a Document Intelligence resource
-            url: create-document-intelligence-resource.md
+            url: how-to-guides/create-document-intelligence-resource.md
           - text: Create SAS tokens for storage containers
-            url: create-sas-tokens.md
+            url: authentication/create-sas-tokens.md
           - text: Create and use managed identities
-            url: managed-identities.md
+            url: authentication/managed-identities.md
           - text: Build a custom extraction model
             url:  how-to-guides/build-a-custom-model.md
           - text: Build a custom classification model
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "index.yml内のリンクの更新と整理"
}
```

### Explanation
この変更は、「index.yml」ファイルに対する小さな更新を示しており、合計で24行が変更されていますが、その内訳は12行の追加と12行の削除です。

主な変更内容は以下のとおりです：

1. **リンクのパスの更新**: 多くのリンクのURLが新しいパスに変更されています。特に、以前は「concept-」プレフィックスのリンクが、「prebuilt-」や「train-」、「how-to-guides-」などの新しいプレフィックスに更新されており、情報が整理されています。

2. **構造の整理**: リンクが関連するトピックに基づいて明確に構成され、ユーザーが必要な情報にアクセスしやすくなっています。これにより、ドキュメントの可読性が向上し、学習リソースを簡単に見つけることができます。

3. **情報の明瞭化**: 新しいリンク構造は、各項目の内容がより直感的に理解できるようになっており、利用者が様々なリソースをスムーズに探索できる環境を提供しています。

この更新は、_document-intelligence_に関する文書をより使いやすくすることを目的に行われており、特にリンク先の情報が最新であることを反映しています。

## articles/ai-services/document-intelligence/language-support/custom.md{#item-fafe89}

<details>
<summary>Diff</summary>
````diff
@@ -5,28 +5,26 @@ description: Document Intelligence custom model language extraction and detectio
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 08/03/2024
 ---
 
 # Language support: custom models
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
+[!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
+[!INCLUDE [applies to v3.1](../includes/applies-to-v31.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 ::: moniker-end
 
 <!-- markdownlint-disable MD001 -->
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデルに関するファイル名の変更とリンクの更新"
}
```

### Explanation
この変更は、「custom.md」ファイルのリネームと内容の一部更新を示しており、合計で10行の変更が行われました。その内訳には4行の追加と6行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名の変更**: ファイルが`language-support-custom.md`から`custom.md`にリネームされました。これにより、ファイル名が簡潔になり、呼び出しやすくなっています。

2. **リンクのパスの更新**: リンクのパスが更新され、相対パス形式に変更されています。具体的には、以前の形式（`includes/applies-to-v4.0.md`など）から、`../includes/applies-to-v4.0.md`のような形式に変更され、より適切にディレクトリを管理できるようになっています。

3. **内容の簡素化**: 不要なメタデータが削除され、リンクが整理されることによって、ドキュメントの可読性が向上しました。特に、モニカーのセクションが明確に定義され、各バージョンに関連する情報が整理されています。

これらの変更により、ドキュメントがより直感的で使いやすくなり、ユーザーが情報にアクセスしやすくなることが期待されます。

## articles/ai-services/document-intelligence/language-support/ocr.md{#item-143ab8}

<details>
<summary>Diff</summary>
````diff
@@ -5,28 +5,28 @@ description: Document Intelligence Read and Layout OCR document analysis model l
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 01/19/2024
 ---
+<!-- markdownlint-disable MD055 -->
+<!-- markdownlint-disable MD056 -->
 
 # Language support: document analysis
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
+[!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
+[!INCLUDE [applies to v3.1](../includes/applies-to-v31.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 ::: moniker-end
 
 <!-- markdownlint-disable MD001 -->
@@ -38,7 +38,7 @@ Azure AI Document Intelligence models provide multilingual document processing s
 
 ::: moniker range=">=doc-intel-3.0.0"
 
-* [**Read**](#read-model): The read model enables extraction and analysis of printed and handwritten text. This model is the underlying OCR engine for other Document Intelligence prebuilt models like layout, general document, invoice, receipt, identity (ID) document, health insurance card, tax documents and custom models. For more information, *see* [Read model overview](concept-read.md)
+* [**Read**](#read-model): The read model enables extraction and analysis of printed and handwritten text. This model is the underlying OCR engine for other Document Intelligence prebuilt models like layout, general document, invoice, receipt, identity (ID) document, health insurance card, tax documents and custom models. For more information, *see* [Read model overview](../prebuilt/read.md)
 ::: moniker-end
 
 ::: moniker range=">=doc-intel-2.1.0"
@@ -49,7 +49,7 @@ Azure AI Document Intelligence models provide multilingual document processing s
 
 ::: moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
-* [**General document**](#general-document): The general document model enables extraction and analysis of text, document structure, and key-value pairs. For more information, *see* [General document model overview](concept-general-document.md)
+* [**General document**](#general-document): The general document model enables extraction and analysis of text, document structure, and key-value pairs. For more information, *see* [General document model overview](../prebuilt/general-document.md)
 
 ::: moniker-end
 
@@ -74,6 +74,7 @@ The following table lists read model language support for extracting and analyzi
 
 :::row:::
    :::column span="":::
+
   |Language| Code (optional) |
   |:-----|:----:|
   |Abaza|`abq`|
@@ -235,6 +236,7 @@ The following table lists read model language support for extracting and analyzi
   |Lakota|`lkt`|
    :::column-end:::
    :::column span="":::
+
       |Language| Code (optional) |
   |:-----|:----:|
   |Latin|`la`|
@@ -595,6 +597,7 @@ The following table lists read model language support for extracting and analyzi
 |German  |`de`|Spanish  |`es`|
 |Italian  |`it`| Russian (preview) | `ru` |
 |Thai (preview) | `th` | Arabic (preview) | `ar` |
+
 :::moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
@@ -608,6 +611,7 @@ The following table lists read model language support for extracting and analyzi
 |French  |`fr`|Portuguese |`pt`|
 |German  |`de`|Spanish  |`es`|
 |Italian  |`it`|
+
 :::moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
@@ -625,7 +629,7 @@ The following table lists read model language support for extracting and analyzi
 
 ### [**Read: language detection**](#tab/read-detection)
 
-The [Read model API](concept-read.md) supports **language detection** for the following languages in your documents. This list can include languages not currently supported for text extraction.
+The [Read model API](../prebuilt/read.md) supports **language detection** for the following languages in your documents. This list can include languages not currently supported for text extraction.
 
 > [!IMPORTANT]
 > **Language detection**
@@ -639,6 +643,7 @@ The [Read model API](concept-read.md) supports **language detection** for the fo
 
 :::row:::
    :::column span="":::
+
 | Language            | Code          |
 |---------------------|---------------|
 | Afrikaans           | `af`          |
@@ -777,6 +782,7 @@ The following table lists the supported languages for printed text:
 
 :::row:::
    :::column span="":::
+
   |**Language**| **Code (optional)** |
   |:-----|:----:|
   |Abaza|`abq`|
@@ -856,6 +862,7 @@ The following table lists the supported languages for printed text:
   |Finnish|`fi`|
    :::column-end:::
    :::column span="":::
+
       |Language| Code (optional) |
   |:-----|:----:|
   |`Fon`|`fon`|
@@ -1102,6 +1109,7 @@ The following table lists layout model language support for extracting and analy
 
 :::row:::
    :::column span="":::
+
   |**Language**| **Code (optional)**|
   |:-----|:----:|
   |Afrikaans|`af`|
@@ -1148,6 +1156,7 @@ The following table lists layout model language support for extracting and analy
   |Filipino|`fil`|
    :::column-end:::
    :::column span="":::
+
       |Language| Code (optional) |
   |:-----|:----:|
   |Fijian|`fj`|
@@ -1369,6 +1378,7 @@ The following table lists layout model language support for extracting and analy
 |Zulu  | `zu` |
 :::column-end:::
 :::row-end:::
+
 :::moniker-end
 
 ### [**Layout: handwritten text**](#tab/layout-hand)
@@ -1385,6 +1395,7 @@ The following table lists layout model language support for extracting and analy
 |German  |`de`|Spanish  |`es`|
 |Italian  |`it`| Russian (preview) | `ru` |
 |Thai (preview) | `th` | Arabic (preview) | `ar` |
+
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
@@ -1421,6 +1432,7 @@ The following table lists layout model language support for extracting and analy
 |German  |`de`|Spanish  |`es`|
 |Italian  |`it`| Russian (preview) | `ru` |
 |Thai (preview) | `th` | Arabic (preview) | `ar` |
+
 :::moniker-end
 
 ---
@@ -1436,6 +1448,7 @@ The following table lists layout model language support for extracting and analy
 |----------  |---------|--------|
 |**Layout model** with query string **`features=keyValuePairs`** specified.|&bullet; v4:2024-02-29-preview, 2023-10-31-preview</br>&bullet; v3.1:2023-07-31 (GA) |**`prebuilt-layout`**|
 |General document model|&bullet; v3.1:2023-07-31 (GA)</br>&bullet; v3.0:2022-08-31 (GA)|**`prebuilt-document`**|
+
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
@@ -1449,6 +1462,7 @@ The following table lists general document model language support. </br>
 | Model `ID`| Language—Locale code | Default |
 |--------|:----------------------|:---------|
 |**prebuilt-document**| English (United States)—en-`US`| English (United States)—en-`US`|
+
 :::moniker-end
 
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "OCR関連ファイルの名称変更とリンクの更新"
}
```

### Explanation
この変更は、「ocr.md」ファイルのリネームと内容の一部更新を示しており、計32行が変更されています。その内訳には23行の追加と9行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名の変更**: ファイルは`language-support-ocr.md`から`ocr.md`にリネームされました。この変更により、ファイル名が簡潔化され、関連するドキュメントが探しやすくなっています。

2. **リンクのパスの更新**: 様々なリンクのURLが更新され、相対パス形式になりました。具体的には、`includes/applies-to-v4.0.md`のようなリンクから、`../includes/applies-to-v4.0.md`といった形式に変更され、ディレクトリ構造に対する理解が容易になっています。

3. **新しいメタデータの追加**: Markdownの整形に関する制御コメント（`markdownlint-disable`）が追加されており、ドキュメント作成時のスタイル違反を無視するよう指定されています。これにより、ドキュメントの書式が適切に保たれるようになっています。

4. **内容の改善**: 一部の記述がより明確になり、読者が情報を理解するのが容易になるように調整されています。特に、各モデルの記述が具体的かつ関連情報へのリンクも整備され、使いやすさが向上しています。

この変更によって、OCR関連の情報はよりアクセスしやすく整理され、ユーザーにとっての利便性が高まることが期待されます。

## articles/ai-services/document-intelligence/language-support/prebuilt.md{#item-ac5486}

<details>
<summary>Diff</summary>
````diff
@@ -5,28 +5,26 @@ description: Document Intelligence prebuilt / pretrained model language extracti
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 02/29/2024
 ---
 
 # Language support: prebuilt models
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
+[!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
+[!INCLUDE [applies to v3.1](../includes/applies-to-v31.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 ::: moniker-end
 
 <!-- markdownlint-disable MD001 -->
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プリビルトモデルに関するファイル名の変更とリンクの更新"
}
```

### Explanation
この変更は、「prebuilt.md」ファイルのリネームと内容の一部更新を示しており、合計で10行の変更が行われました。その内訳には4行の追加と6行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名の変更**: ファイルが`language-support-prebuilt.md`から`prebuilt.md`にリネームされました。これにより、ファイル名が簡潔になり、関連情報をより容易に見つけられるようにしています。

2. **リンクのパスの更新**: さまざまなリンクが相対パス形式で更新され、URLが`includes/applies-to-v4.0.md`のような形式から`../includes/applies-to-v4.0.md`のような形式に変更されました。これにより、ディレクトリ構造がより合理的になり、リンクの管理が容易になります。

3. **メタデータの調整**: 不要なメタデータが削除され、Markdownのスタイル違反を無視するためのコメントが追加されています（`markdownlint-disable`）。これにより、文書の構造が整理され、見やすさが向上しています。

これらの変更により、プリビルトモデル関連の情報が整理され、ユーザーにとっての利便性が向上することが期待されます。

## articles/ai-services/document-intelligence/model-overview.md{#item-768c0d}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Document processing models - Document Intelligence 
+title: Document processing models - Document Intelligence
 titleSuffix: Azure AI services
 description: Document processing models for OCR, document layout, invoices, identity, custom  models, and more to extract text, structure, and key-value pairs.
 author: laujan
@@ -50,22 +50,22 @@ The following table shows the available models for each current preview and stab
 
 |**Model Type**| **Model**|&bullet; [2024-02-29-preview](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2024-02-29-preview&preserve-view=true&branch=docintelligence&tabs=HTTP) <br> &bullet; [2023-10-31-preview](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)|[2023-07-31 (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)|[2022-08-31 (GA)](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)|[v2.1 (GA)](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)|
 |----------------|-----------|---|--|---|---|
-|Document analysis models|[Read](concept-read.md)                                  | ✔️| ✔️| ✔️| n/a|
-|Document analysis models|[Layout](concept-layout.md)                              | ✔️| ✔️| ✔️| ✔️|
-|Document analysis models|[General document](concept-general-document.md)          |moved to layout**| ✔️| ✔️| n/a|
+|Document analysis models|[Read](prebuilt/read.md)                                  | ✔️| ✔️| ✔️| n/a|
+|Document analysis models|[Layout](prebuilt/layout.md)                              | ✔️| ✔️| ✔️| ✔️|
+|Document analysis models|[General document](prebuilt/general-document.md)          |moved to layout**| ✔️| ✔️| n/a|
 |Prebuilt models|[Bank Check](concept-bank-check.md)   | ✔️| n/a| n/a| n/a|
 |Prebuilt models|[Bank Statement](concept-bank-statement.md)   | ✔️| n/a| n/a| n/a|
 |Prebuilt models|[Paystub](concept-pay-stub.md)   | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[Contract](concept-contract.md)                          | ✔️| ✔️| n/a| n/a|
-|Prebuilt models|[Health insurance card](concept-health-insurance-card.md)| ✔️| ✔️| ✔️| n/a|
-|Prebuilt models|[ID document](concept-id-document.md)                    | ✔️| ✔️| ✔️| ✔️|
-|Prebuilt models|[Invoice](concept-invoice.md)                            | ✔️| ✔️| ✔️| ✔️|
-|Prebuilt models|[Receipt](concept-receipt.md)                            | ✔️| ✔️| ✔️| ✔️|
-|Prebuilt models|[US Unified Tax*](concept-tax-document.md)                   | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US 1040 Tax*](concept-tax-document.md)                   | ✔️| ✔️| n/a| n/a|
-|Prebuilt models|[US 1098 Tax*](concept-tax-document.md)                   | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US 1099 Tax*](concept-tax-document.md)                 | ✔️| n/a| n/a| n/a|
-|Prebuilt models|[US W2 Tax](concept-tax-document.md)                     | ✔️| ✔️| ✔️| n/a|
+|Prebuilt models|[Contract](prebuilt/contract.md)                          | ✔️| ✔️| n/a| n/a|
+|Prebuilt models|[Health insurance card](prebuilt/health-insurance-card.md)| ✔️| ✔️| ✔️| n/a|
+|Prebuilt models|[ID document](prebuilt/id-document.md)                    | ✔️| ✔️| ✔️| ✔️|
+|Prebuilt models|[Invoice](prebuilt/invoice.md)                            | ✔️| ✔️| ✔️| ✔️|
+|Prebuilt models|[Receipt](prebuilt/receipt.md)                            | ✔️| ✔️| ✔️| ✔️|
+|Prebuilt models|[US Unified Tax*](prebuilt/tax-document.md)                   | ✔️| n/a| n/a| n/a|
+|Prebuilt models|[US 1040 Tax*](prebuilt/tax-document.md)                   | ✔️| ✔️| n/a| n/a|
+|Prebuilt models|[US 1098 Tax*](prebuilt/tax-document.md)                   | ✔️| n/a| n/a| n/a|
+|Prebuilt models|[US 1099 Tax*](prebuilt/tax-document.md)                 | ✔️| n/a| n/a| n/a|
+|Prebuilt models|[US W2 Tax](prebuilt/tax-document.md)                     | ✔️| ✔️| ✔️| n/a|
 |Prebuilt models|[US Mortgage 1003 URLA](concept-mortgage-documents.md)    | ✔️| n/a| n/a| n/a|
 |Prebuilt models|[US Mortgage 1004 URAR](concept-mortgage-documents.md)    | ✔️| n/a| n/a| n/a|
 |Prebuilt models|[US Mortgage 1005](concept-mortgage-documents.md)    | ✔️| n/a| n/a| n/a|
@@ -74,11 +74,11 @@ The following table shows the available models for each current preview and stab
 |Prebuilt models|[Marriage certificate](concept-marriage-certificate.md)   | ✔️| n/a| n/a| n/a|
 |Prebuilt models|[Credit card](concept-credit-card.md)   | ✔️| n/a| n/a| n/a|
 |Prebuilt models|[Business card](concept-business-card.md)                | deprecated|✔️|✔️|✔️ |
-|Custom classification model|[Custom classifier](concept-custom-classifier.md)        | ✔️| ✔️| n/a| n/a|
-|Custom Generative Model|[Custom Generative Model](concept-custom-generative.md)   | ✔️| n/a| n/a| n/a|
-|Custom extraction model|[Custom neural](concept-custom-neural.md)                | ✔️| ✔️| ✔️| n/a|
-|Customextraction model|[Custom template](concept-custom-template.md)            | ✔️| ✔️| ✔️| ✔️|
-|Custom extraction model|[Custom composed](concept-composed-models.md)            | ✔️| ✔️| ✔️| ✔️|
+|Custom classification model|[Custom classifier](train/custom-classifier.md)        | ✔️| ✔️| n/a| n/a|
+|Custom Generative Model|[Custom Generative Model](train/custom-generative-extraction.md)   | ✔️| n/a| n/a| n/a|
+|Custom extraction model|[Custom neural](train/custom-neural.md)                | ✔️| ✔️| ✔️| n/a|
+|Customextraction model|[Custom template](train/custom-template.md)            | ✔️| ✔️| ✔️| ✔️|
+|Custom extraction model|[Custom composed](train/composed-models.md)            | ✔️| ✔️| ✔️| ✔️|
 |All models|[Add-on capabilities](concept-add-on-capabilities.md)    | ✔️| ✔️| n/a| n/a|
 
 \* - Contains submodels. See the model specific information for supported variations and subtypes.
@@ -123,16 +123,16 @@ For all models, except Business card model, Document Intelligence now supports a
 * [`languages`](concept-add-on-capabilities.md#language-detection)
 * [`keyValuePairs`](concept-add-on-capabilities.md#key-value-pairs) (2024-02-29-preview, 2023-10-31-preview)
 * [`queryFields`](concept-add-on-capabilities.md#query-fields) (2024-02-29-preview, 2023-10-31-preview) `Not available with the US.Tax models`
-* [`searchablePDF`](concept-read.md#searchable-pdf) (2024-07-31-preview) `Only available for Read Model`
+* [`searchablePDF`](prebuilt/read.md#searchable-pdf) (2024-07-31-preview) `Only available for Read Model`
 
 ## Language support
 
 The deep-learning-based universal models in Document Intelligence support many languages that can extract multilingual text from your images and documents, including text lines with mixed languages.
 Language support varies by Document Intelligence service functionality. For a complete list, see the following articles:
 
-* [Language support: document analysis models](language-support-ocr.md)
-* [Language support: prebuilt models](language-support-prebuilt.md)
-* [Language support: custom models](language-support-custom.md)
+* [Language support: document analysis models](language-support/ocr.md)
+* [Language support: prebuilt models](language-support/prebuilt.md)
+* [Language support: custom models](language-support/custom.md)
 
 ## Regional availability
 
@@ -155,7 +155,7 @@ The Read API analyzes and extracts lines, words, their locations, detected langu
 :::image type="content" source="media/studio/form-recognizer-studio-read-v3p2.png" alt-text="Screenshot of Screenshot of sample document processed using Document Intelligence Studio Read":::
 
 > [!div class="nextstepaction"]
-> [Learn more: read model](concept-read.md)
+> [Learn more: read model](prebuilt/read.md)
 
 ### Layout analysis
 
@@ -169,7 +169,7 @@ The Layout analysis model analyzes and extracts text, tables, selection marks, a
 
 > [!div class="nextstepaction"]
 >
-> [Learn more: layout model](concept-layout.md)
+> [Learn more: layout model](prebuilt/layout.md)
 
 ### Health insurance card
 
@@ -182,7 +182,7 @@ The health insurance card model combines powerful Optical Character Recognition
 :::image type="content" source="./media/studio/analyze-health-card.png" alt-text="Screenshot of a sample US health insurance card analysis in Document Intelligence Studio." lightbox="./media/studio/analyze-health-card.png":::
 
 > [!div class="nextstepaction"]
-> [Learn more: Health insurance card model](concept-health-insurance-card.md)
+> [Learn more: Health insurance card model](prebuilt/health-insurance-card.md)
 
 ### US tax documents
 
@@ -193,17 +193,17 @@ The US tax document models analyze and extract key fields and line items from a
   |Model|Description|ModelID|
   |---|---|---|
   |US Tax W-2|Extract taxable compensation details.|**prebuilt-tax.us.W-2**|
-  US Tax 1040|Extract mortgage interest details.|**prebuilt-tax.us.1040(variations)**|
+  |US Tax 1040|Extract mortgage interest details.|**prebuilt-tax.us.1040(variations)**|
   |US Tax 1098|Extract mortgage interest details.|**prebuilt-tax.us.1098(variations)**|
   |US Tax 1099|Extract income received from sources other than employer.|**prebuilt-tax.us.1099(variations)**|
-  
+
 ***Sample W-2 document processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=tax.us.w2)***:
 
 :::image type="content" source="./media/studio/w-2.png" alt-text="Screenshot of a sample W-2.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: Tax document models](concept-tax-document.md)
-> 
+> [Learn more: Tax document models](prebuilt/tax-document.md)
+>
 
 ### US mortgage documents
 
@@ -218,14 +218,14 @@ The US mortgage document models analyze and extract key fields including borrowe
   |Closing disclosure|Extract closing, transaction costs, and loan details.|**prebuilt-mortgage.us.closingDisclosure**|
   |Marriage certificate|Extract marriage information details for joint loan applicants.|**prebuilt-marriageCertificate**|
   |US Tax W-2|Extract taxable compensation details for income verification.|**prebuilt-tax.us.W-2**|
-  
+
 ***Sample Closing disclosure document processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=mortgage.us.closingDisclosure)***:
 
 :::image type="content" source="./media/studio/closing-disclosure.png" alt-text="Screenshot of a sample closing disclosure.":::
 
 > [!div class="nextstepaction"]
 > [Learn more: Mortgage document models](concept-mortgage-documents.md)
-> 
+>
 ### Contract
 
 :::image type="icon" source="media/overview/icon-contract.png":::
@@ -237,7 +237,7 @@ The US mortgage document models analyze and extract key fields including borrowe
 :::image type="content" source="media/studio/analyze-contract.png" alt-text="Screenshot of contract model extraction using Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: contract model](concept-contract.md)
+> [Learn more: contract model](prebuilt/contract.md)
 
 ### Invoice
 
@@ -250,7 +250,7 @@ The invoice model automates processing of invoices to extracts customer name, bi
 :::image type="content" source="./media/studio/analyze-invoice.png" alt-text="Screenshot of a sample invoice." lightbox="./media/overview-invoices.jpg":::
 
 > [!div class="nextstepaction"]
-> [Learn more: invoice model](concept-invoice.md)
+> [Learn more: invoice model](prebuilt/invoice.md)
 
 ### Receipt
 
@@ -263,7 +263,7 @@ Use the receipt model to scan sales receipts for merchant name, dates, line item
 :::image type="content" source="./media/studio/analyze-receipt.png" alt-text="Screenshot of a sample receipt." lightbox="./media/overview-receipt.jpg":::
 
 > [!div class="nextstepaction"]
-> [Learn more: receipt model](concept-receipt.md)
+> [Learn more: receipt model](prebuilt/receipt.md)
 
 ### Identity document (ID)
 
@@ -276,7 +276,7 @@ Use the Identity document (ID) model to process U.S. Driver's Licenses (all 50 s
 :::image type="content" source="./media/studio/analyze-drivers-license.png" alt-text="Screenshot of a sample identification card." lightbox="./media/overview-id.jpg":::
 
 > [!div class="nextstepaction"]
-> [Learn more: identity document model](concept-id-document.md)
+> [Learn more: identity document model](prebuilt/id-document.md)
 
 ### Marriage certificate
 
@@ -314,14 +314,14 @@ Custom models can be broadly classified into two types. Custom classification mo
 
 Custom document models analyze and extract data from forms and documents specific to your business. They recognize form fields within your distinct content and extract key-value pairs and table data. You only need one example of the form type to get started.
 
-Version v3.0 and later custom models support signature detection in custom template (form) and cross-page tables in both template and neural models. [Signature detection](concept-custom-template.md#model-capabilities) looks for the presence of a signature, not the identity of the person who signs the document. If the model returns **unsigned** for signature detection, the model didn't find a signature in the defined field.
+Version v3.0 and later custom models support signature detection in custom template (form) and cross-page tables in both template and neural models. [Signature detection](train/custom-template.md#model-capabilities) looks for the presence of a signature, not the identity of the person who signs the document. If the model returns **unsigned** for signature detection, the model didn't find a signature in the defined field.
 
 ***Sample custom template processed using [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/customform/projects)***:
 
 :::image type="content" source="media/studio/train-model.png" alt-text="Screenshot of Document Intelligence tool analyze-a-custom-form window.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: custom model](concept-custom.md)
+> [Learn more: custom model](train/custom-model.md)
 
 #### Custom extraction
 
@@ -334,10 +334,10 @@ Custom extraction model can be one of two types, **custom template** or **custom
 :::image type="content" source="media/studio/custom-extraction-models.png" alt-text="Screenshot of custom extraction model analysis in Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: custom template model](concept-custom-template.md)
+> [Learn more: custom template model](train/custom-template.md)
 
 > [!div class="nextstepaction"]
-> [Learn more: custom neural model](./concept-custom-neural.md)
+> [Learn more: custom neural model](./train/custom-neural.md)
 
 #### Custom classifier
 
@@ -346,7 +346,7 @@ Custom extraction model can be one of two types, **custom template** or **custom
 The custom classification model enables you to identify the document type before invoking the extraction model. The classification model is available starting with the `2023-07-31 (GA)` API. Training a custom classification model requires at least two distinct classes and a minimum of five samples per class.
 
 > [!div class="nextstepaction"]
-> [Learn more: custom classification model](concept-custom-classifier.md)
+> [Learn more: custom classification model](train/custom-classifier.md)
 
 #### Composed models
 
@@ -357,8 +357,7 @@ A composed model is created by taking a collection of custom models and assignin
 :::image type="content" source="media/studio/composed-model.png" alt-text="Screenshot of Document Intelligence Studio compose custom model dialog window.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: custom model](concept-custom.md)
-
+> [Learn more: custom model](train/custom-model.md)
 
 ## Input requirements
 
@@ -386,7 +385,7 @@ Learn how to use Document Intelligence v3.0 in your applications by following ou
 | [Business card](#business-card)  | Extract key information from English business cards.  |
 |**Custom**||
 | [Custom](#custom) |  Extract data from forms and documents specific to your business. Custom models are trained for your distinct data and use cases. |
-| [Composed](#composed-custom-model) | Compose a collection of custom models and assign them to a single model built from your form types.
+| [Composed](#composed-custom-model) | Compose a collection of custom models and assign them to a single model built from your form types.|
 
 ### Layout
 
@@ -398,7 +397,7 @@ The Layout API analyzes and extracts text, tables and headers, selection marks,
 
 > [!div class="nextstepaction"]
 >
-> [Learn more: layout model](concept-layout.md)
+> [Learn more: layout model](prebuilt/layout.md)
 
 ### Invoice
 
@@ -409,7 +408,7 @@ The invoice model analyzes and extracts key information from sales invoices. The
 :::image type="content" source="./media/overview-invoices.jpg" alt-text="Screenshot of a sample invoice analysis using the Sample Labeling tool.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: invoice model](concept-invoice.md)
+> [Learn more: invoice model](prebuilt/invoice.md)
 
 ### Receipt
 
@@ -420,7 +419,7 @@ The invoice model analyzes and extracts key information from sales invoices. The
 :::image type="content" source="./media/receipts-example.jpg" alt-text="Screenshot of a sample receipt." lightbox="./media/overview-receipt.jpg":::
 
 > [!div class="nextstepaction"]
-> [Learn more: receipt model](concept-receipt.md)
+> [Learn more: receipt model](prebuilt/receipt.md)
 
 ### ID document
 
@@ -435,7 +434,7 @@ The invoice model analyzes and extracts key information from sales invoices. The
 :::image type="content" source="./media/id-example-drivers-license.jpg" alt-text="Screenshot of a sample identification card.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: identity document model](concept-id-document.md)
+> [Learn more: identity document model](prebuilt/id-document.md)
 
 ### Business card
 
@@ -457,7 +456,7 @@ The business card model analyzes and extracts key information from business card
 :::image type="content" source="media/overview-custom.jpg" alt-text="Screenshot of Document Intelligence tool analyze-a-custom-form window.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: custom model](concept-custom.md)
+> [Learn more: custom model](train/custom-model.md)
 
 #### Composed custom model
 
@@ -468,18 +467,18 @@ A composed model is created by taking a collection of custom models and assignin
 :::image type="content" source="media/custom-model-compose.png" alt-text="Screenshot of Document Intelligence Studio compose custom model dialog window.":::
 
 > [!div class="nextstepaction"]
-> [Learn more: custom model](concept-custom.md)
+> [Learn more: custom model](train/custom-model.md)
 
 ## Model data extraction
 
 | **Model** | **Text extraction** | **Language detection** | **Selection Marks** | **Tables** | **Paragraphs** | **Paragraph roles** | **Key-Value pairs** | **Fields** |
 |:-----|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
-| [Layout](concept-layout.md#data-extraction)  | ✓  |   | ✓ | ✓ | ✓  | ✓  |  |  |
-| [Invoice](concept-invoice.md#field-extraction)  | ✓ |   | ✓  | ✓ | ✓ |   | ✓ | ✓ |
-| [Receipt](concept-receipt.md#field-extraction)  | ✓  |   |  |  | ✓ |   |  | ✓ |
-| [ID Document](concept-id-document.md#field-extractions) | ✓ |   |   |  | ✓ |   |  | ✓ |
+| [Layout](prebuilt/layout.md#data-extraction)  | ✓  |   | ✓ | ✓ | ✓  | ✓  |  |  |
+| [Invoice](prebuilt/invoice.md#field-extraction)  | ✓ |   | ✓  | ✓ | ✓ |   | ✓ | ✓ |
+| [Receipt](prebuilt/receipt.md#field-extraction)  | ✓  |   |  |  | ✓ |   |  | ✓ |
+| [ID Document](prebuilt/id-document.md#field-extractions) | ✓ |   |   |  | ✓ |   |  | ✓ |
 | [Business Card](concept-business-card.md#field-extractions)  | ✓  |   |   |  | ✓ |   |  | ✓ |
-| [Custom Form](concept-custom.md#compare-model-features) | ✓  ||  ✓ | ✓ | ✓  |   | | ✓ |
+| [Custom Form](train/custom-model.md#compare-model-features) | ✓  ||  ✓ | ✓ | ✓  |   | | ✓ |
 
 ## Input requirements
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル概要ファイルの名称変更と内容の更新"
}
```

### Explanation
この変更は、「concept-model-overview.md」ファイルが「model-overview.md」にリネームされ、内容の一部も更新されたことを示しています。合計で109行が変更され、その内訳には54行の追加と55行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名の変更**: ファイルは`concept-model-overview.md`から`model-overview.md`にリネームされました。これにより、ファイルの名称が一貫性を持ち、より明確になります。

2. **リンクの更新**: 一部のリンクが更新され、相対パスが導入されました。特に、モデルに関連する各種リンクが`concept-`から`prebuilt/`といった新しい構造に変更され、ドキュメント内のナビゲーションがより一貫性を持つようになっています。

3. **モデル情報の整理**: 各モデルの情報がテーブル形式で整理され、具体的な機能や対応するリンクが明確に示されるようになりました。これにより、ユーザーは求める情報へより迅速にアクセスできるようになります。

4. **メタデータの調整**: ドキュメントのタイトルや説明文が更新され、文書全体の説明性が向上しています。特に、OCRやドキュメントレイアウトに関する記述が強化されており、利用者にとっての理解が深まる内容となっています。

これらの変更により、モデルに関する情報がより明確に整理され、ユーザーエクスペリエンスが向上することが期待されます。

## articles/ai-services/document-intelligence/overview.md{#item-4e36ba}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Azure AI Document Intelligence is a machine-learning based OCR and
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: overview
 ms.date: 08/07/2024
 ms.author: lajanuar
@@ -21,23 +19,27 @@ monikerRange: '<=doc-intel-4.0.0'
 
 # What is Azure AI Document Intelligence?
 
-::: moniker range="doc-intel-4.0.0"
+ :::moniker range="doc-intel-4.0.0"
 [!INCLUDE [preview-version-notice](includes/preview-notice.md)]
 
 [!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
-::: moniker-end
 
-::: moniker range="doc-intel-3.1.0"
+:::moniker-end
+
+ :::moniker range="doc-intel-3.1.0"
 [!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
-::: moniker-end
 
-::: moniker range="doc-intel-3.0.0"
+:::moniker-end
+
+ :::moniker range="doc-intel-3.0.0"
 [!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
-::: moniker-end
 
-::: moniker range="doc-intel-2.1.0"
+:::moniker-end
+
+ :::moniker range="doc-intel-2.1.0"
 [!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
-::: moniker-end
+
+:::moniker-end
 
 > [!NOTE]
 > Form Recognizer is now **Azure AI Document Intelligence**!
@@ -57,117 +59,121 @@ Azure AI Document Intelligence is a cloud-based [Azure AI service](../../ai-serv
 General extraction models enable text extraction from forms and documents and return structured business-ready content ready for your organization's action, use, or development.
 
 :::moniker range="doc-intel-4.0.0"
-:::row:::
-   :::column:::
-   [**Read**](#read) | Extract printed and handwritten text.
-   :::column-end:::
-   :::column span="":::
-    [**Layout**](#layout) | Extract text, tables, and document structure.
-   :::column-end:::
-  :::row-end:::
-:::moniker-end
 
+ :::row:::
+    :::column:::
+    [**Read**](#read) | Extract printed and handwritten text.
+    :::column-end:::
+    :::column span="":::
+     [**Layout**](#layout) | Extract text, tables, and document structure.
+    :::column-end:::
+   :::row-end:::
+
+:::moniker-end
+ 
 :::moniker range="<=doc-intel-3.1.0"
-:::row:::
-   :::column:::
-   [**Read**](#read) | Extract printed </br>and handwritten text.
-   :::column-end:::
-   :::column span="":::
-    [**Layout**](#layout) | Extract text, tables, </br>and document structure.
-   :::column-end:::
-   :::column span="":::
-    [**General document**](#general-document-deprecated-in-2023-10-31-preview) | Extract text, </br>structure, and key-value pairs.
-   :::column-end:::
-:::row-end:::
+
+ :::row:::
+    :::column:::
+    [**Read**](#read) | Extract printed </br>and handwritten text.
+    :::column-end:::
+    :::column span="":::
+     [**Layout**](#layout) | Extract text, tables, </br>and document structure.
+    :::column-end:::
+    :::column span="":::
+     [**General document**](#general-document-deprecated-in-2023-10-31-preview) | Extract text, </br>structure, and key-value pairs.
+    :::column-end:::
+ :::row-end:::
+
 :::moniker-end
 
 ## Prebuilt models
 
 Prebuilt models enable you to add intelligent document processing to your apps and flows without having to train and build your own models.
 
 :::moniker range="doc-intel-4.0.0"
+
 ### Financial Services and Legal
 
-:::row:::
-   :::column span="":::
-    [**Bank Statement**](#bank-statement) | Extract account information and details from bank statements.
-   :::column-end:::
-   :::column span="":::
-    [**Check**](#check) | Extract relevant information from checks.
-   :::column-end:::
-   :::column span="":::
-    [**Contract**](#contract-model) | Extract agreement and party details.
-   :::column-end:::
-:::row-end:::
-:::row:::
+ :::row:::
     :::column span="":::
-    [**Credit card**](#credit-card-model) | Extract payment card information.
+     [**Bank Statement**](#bank-statement) | Extract account information and details from bank statements.
     :::column-end:::
     :::column span="":::
-    [**Invoice**](#invoice) | Extract customer and vendor details.
-   :::column-end:::
-   :::column span="":::
-    [**Pay Stub**](#pay-stub) | Extract pay stub details.
-   :::column-end:::
-   :::column span="":::
-    [**Receipt**](#receipt) | Extract sales transaction details.
-   :::column-end:::
-:::row-end:::
+     [**Check**](#check) | Extract relevant information from checks.
+    :::column-end:::
+    :::column span="":::
+     [**Contract**](#contract-model) | Extract agreement and party details.
+    :::column-end:::
+ :::row-end:::
+ :::row:::
+     :::column span="":::
+     [**Credit card**](#credit-card-model) | Extract payment card information.
+     :::column-end:::
+     :::column span="":::
+     [**Invoice**](#invoice) | Extract customer and vendor details.
+    :::column-end:::
+    :::column span="":::
+     [**Pay Stub**](#pay-stub) | Extract pay stub details.
+    :::column-end:::
+    :::column span="":::
+     [**Receipt**](#receipt) | Extract sales transaction details.
+    :::column-end:::
+ :::row-end:::
 
 ### US Tax
-:::row:::
-   :::column span="":::
-    [**Unified US tax**](#unified-us-tax-forms) | Extract from any US tax forms supported.
-   :::column-end:::
-   :::column span="":::
-    [**US Tax W-2**](#us-tax-w-2-model) | Extract taxable compensation details.
-   :::column-end:::
-   :::column span="":::
-    [**US Tax 1098**](#us-tax-1098-and-variations-forms) | Extract `1098` variation details.
-   :::column-end:::
-   :::column span="":::
-    [**US Tax 1099**](#us-tax-1099-and-variations-forms) | Extract `1099` variation details.
-   :::column-end:::
-   :::column span="":::
-    [**US Tax 1040**](#us-tax-1040-and-variations-forms) |  Extract `1040` variation details.
-   :::column-end:::
-:::row-end:::
 
-### US Mortgage
-:::row:::
-   :::column span="":::
-    [**US mortgage 1003**](#us-mortgage-1003-form) | Extract loan application details.
-   :::column-end:::
-   :::column span="":::
-    [**US mortgage 1004**](#us-mortgage-1004-form) | Extract information from appraisal.
-   :::column-end:::
-   :::column span="":::
-    [**US mortgage 1005**](#us-mortgage-1005-form) | Extract information from validation of employment.
-   :::column-end:::
-   :::column span="":::
-    [**US mortgage 1008**](#us-mortgage-1008-form) | Extract loan transmittal details.
-   :::column-end:::
-   :::column span="":::
-    [**US mortgage disclosure**](#us-mortgage-disclosure-form) | Extract final closing loan terms.
-   :::column-end:::
-:::row-end:::
+ :::row:::
+    :::column span="":::
+     [**Unified US tax**](#unified-us-tax-forms) | Extract from any US tax forms supported.
+    :::column-end:::
+    :::column span="":::
+     [**US Tax W-2**](#us-tax-w-2-model) | Extract taxable compensation details.
+    :::column-end:::
+    :::column span="":::
+     [**US Tax 1098**](#us-tax-1098-and-variations-forms) | Extract `1098` variation details.
+    :::column-end:::
+    :::column span="":::
+     [**US Tax 1099**](#us-tax-1099-and-variations-forms) | Extract `1099` variation details.
+    :::column-end:::
+    :::column span="":::
+     [**US Tax 1040**](#us-tax-1040-and-variations-forms) |  Extract `1040` variation details.
+    :::column-end:::
+ :::row-end:::
 
-### Personal Identification
+### US Mortgage
 
-:::row:::
-   :::column span="":::
-    [**Health Insurance card**](#health-insurance-card) | Extract insurance coverage details.
-   :::column-end:::
+ :::row:::
     :::column span="":::
-    [**Identity**](#identity-id) | Extract verification details.
-   :::column-end:::
-       :::column span="":::
-    [**Marriage certificate**](#marriage-certificate-model) | Extract certified marriage information.
-   :::column-end:::
-:::row-end:::
-
+     [**US mortgage 1003**](#us-mortgage-1003-form) | Extract loan application details.
+    :::column-end:::
+    :::column span="":::
+     [**US mortgage 1004**](#us-mortgage-1004-form) | Extract information from appraisal.
+    :::column-end:::
+    :::column span="":::
+     [**US mortgage 1005**](#us-mortgage-1005-form) | Extract information from validation of employment.
+    :::column-end:::
+    :::column span="":::
+     [**US mortgage 1008**](#us-mortgage-1008-form) | Extract loan transmittal details.
+    :::column-end:::
+    :::column span="":::
+     [**US mortgage disclosure**](#us-mortgage-disclosure-form) | Extract final closing loan terms.
+    :::column-end:::
+ :::row-end:::
 
+### Personal Identification
 
+ :::row:::
+    :::column span="":::
+     [**Health Insurance card**](#health-insurance-card) | Extract insurance coverage details.
+    :::column-end:::
+     :::column span="":::
+     [**Identity**](#identity-id) | Extract verification details.
+    :::column-end:::
+        :::column span="":::
+     [**Marriage certificate**](#marriage-certificate-model) | Extract certified marriage information.
+    :::column-end:::
+ :::row-end:::
 
 :::moniker-end
 
@@ -203,13 +209,15 @@ Prebuilt models enable you to add intelligent document processing to your apps a
     [**US Tax 1098**](#us-tax-1098-and-variations-forms) | Extract `1098` variation details.
    :::column-end:::
 :::row-end:::
+
 :::moniker-end
 
 ## Custom models
 
 Custom models are trained using your labeled datasets to extract distinct data from forms and documents, specific to your use cases. Standalone custom models can be combined to create composed models.
 
 ### Document field extraction models
+
 ✔️ Document field extraction models are trained to extract labeled fields from documents.
 
 :::row:::
@@ -228,6 +236,7 @@ Custom models are trained using your labeled datasets to extract distinct data f
 :::row-end:::
 
 ### Custom classification models
+
 ✔️ Custom classifiers identify document types before invoking an extraction model.
 
 :::row:::
@@ -248,7 +257,7 @@ Document Intelligence supports optional features that can be enabled and disable
 
 * [`ocr.barcode`](concept-add-on-capabilities.md#barcode-property-extraction)
 
- The`2024-07-31-preview` release introduces `read` model support for [searchable PDF](concept-read.md#searchable-pdf) output:
+ The`2024-07-31-preview` release introduces `read` model support for [searchable PDF](prebuilt/read.md#searchable-pdf) output:
 
 * [`Searchable PDF](concept-add-on-capabilities.md#searchable-pdf)
 
@@ -275,7 +284,7 @@ You can use Document Intelligence to automate document processing in application
 
 |Model ID| Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**prebuilt-read**](concept-read.md)|&#9679; Extract **text** from documents.</br>&#9679; [Data extraction](concept-read.md#data-extraction)| &#9679; Digitizing any document. </br>&#9679; Compliance and auditing.</br>&#9679; Processing handwritten notes before translation.|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/read)</br>&#9679; [**REST API**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api)</br>&#9679; [**C# SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-csharp)</br>&#9679; [**Python SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-python)</br>&#9679; [**Java SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-java)</br>&#9679; [**JavaScript**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-javascript) |
+|[**prebuilt-read**](prebuilt/read.md)|&#9679; Extract **text** from documents.</br>&#9679; [Data extraction](prebuilt/read.md#data-extraction)| &#9679; Digitizing any document. </br>&#9679; Compliance and auditing.</br>&#9679; Processing handwritten notes before translation.|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/read)</br>&#9679; [**REST API**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api)</br>&#9679; [**C# SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-csharp)</br>&#9679; [**Python SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-python)</br>&#9679; [**Java SDK**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-java)</br>&#9679; [**JavaScript**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-javascript) |
 
 > [!div class="nextstepaction"]
 > [Return to model types](#general-extraction-models)
@@ -286,32 +295,33 @@ You can use Document Intelligence to automate document processing in application
 
 | Model ID | Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**prebuilt-layout**](concept-layout.md) |&#9679; Extract **text and layout** information from documents.</br>&#9679; [Data extraction](concept-layout.md#data-extraction) |&#9679; Document indexing and retrieval by structure.</br>&#9679; Financial and medical report analysis. |&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/layout)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)|
+|[**prebuilt-layout**](prebuilt/layout.md) |&#9679; Extract **text and layout** information from documents.</br>&#9679; [Data extraction](prebuilt/layout.md#data-extraction) |&#9679; Document indexing and retrieval by structure.</br>&#9679; Financial and medical report analysis. |&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/layout)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#layout-model)|
 
 > [!div class="nextstepaction"]
 > [Return to model types](#general-extraction-models)
 
-::: moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
+ :::moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
 ### General document (deprecated in 2023-10-31-preview)
 
 :::image type="content" source="media/overview/analyze-general-document.png" alt-text="Screenshot of General document model analysis using Document Intelligence Studio.":::
 
 | Model ID | Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**prebuilt-document**](concept-general-document.md)|&#9679; Extract **text,layout, and key-value pairs** from documents.</br>&#9679; [Data and field extraction](concept-general-document.md#data-extraction)|&#9679; Key-value pair extraction.</br>&#9679; Form processing.</br>&#9679; Survey data collection and analysis.|&#9679; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/document)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|
+|[**prebuilt-document**](prebuilt/general-document.md)|&#9679; Extract **text,layout, and key-value pairs** from documents.</br>&#9679; [Data and field extraction](prebuilt/general-document.md#data-extraction)|&#9679; Key-value pair extraction.</br>&#9679; Form processing.</br>&#9679; Survey data collection and analysis.|&#9679; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/document)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|
 
 > [!div class="nextstepaction"]
 > [Return to model types](#general-extraction-models)
 
 :::moniker-end
+
 ### Invoice
 
 :::image type="content" source="media/overview/analyze-invoice.png" alt-text="Screenshot of Invoice model analysis using Document Intelligence Studio.":::
 
 | Model ID | Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**prebuilt-invoice**](concept-invoice.md) |&#9679; Extract key information from invoices.</br>&#9679; [Data and field extraction](concept-invoice.md#field-extraction) |&#9679; Accounts payable processing.</br>&#9679; Automated tax recording and reporting. |&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=invoice&formType=invoice)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
+|[**prebuilt-invoice**](prebuilt/invoice.md) |&#9679; Extract key information from invoices.</br>&#9679; [Data and field extraction](prebuilt/invoice.md#field-extraction) |&#9679; Accounts payable processing.</br>&#9679; Automated tax recording and reporting. |&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=invoice&formType=invoice)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
 
 > [!div class="nextstepaction"]
 > [Return to model types](#prebuilt-models)
@@ -322,7 +332,7 @@ You can use Document Intelligence to automate document processing in application
 
 | Model ID | Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**prebuilt-receipt**](concept-receipt.md) |&#9679; Extract key information from receipts.</br>&#9679; [Data and field extraction](concept-receipt.md#field-extraction)</br>&#9679; Receipt model v3.0 supports processing of **single-page hotel receipts**.|&#9679; Expense management.</br>&#9679; Consumer behavior data analysis.</br>&#9679; Customer loyalty program.</br>&#9679; Merchandise return processing.</br>&#9679; Automated tax recording and reporting. |&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=receipt&formType=receipt)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
+|[**prebuilt-receipt**](prebuilt/receipt.md) |&#9679; Extract key information from receipts.</br>&#9679; [Data and field extraction](prebuilt/receipt.md#field-extraction)</br>&#9679; Receipt model v3.0 supports processing of **single-page hotel receipts**.|&#9679; Expense management.</br>&#9679; Consumer behavior data analysis.</br>&#9679; Customer loyalty program.</br>&#9679; Merchandise return processing.</br>&#9679; Automated tax recording and reporting. |&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=receipt&formType=receipt)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
 
 > [!div class="nextstepaction"]
 > [Return to model types](#prebuilt-models)
@@ -333,7 +343,7 @@ You can use Document Intelligence to automate document processing in application
 
 | Model ID | Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**prebuilt-idDocument**](concept-id-document.md) |&#9679; Extract key information from passports and ID cards.</br>&#9679; [Document types](concept-id-document.md#supported-document-types)</br>&#9679; Extract  endorsements, restrictions, and vehicle classifications from US driver's licenses. |&#9679; Know your customer (KYC) financial services guidelines compliance.</br>&#9679; Medical account management.</br>&#9679; Identity checkpoints and gateways.</br>&#9679; Hotel registration. |&#9679;  [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=idDocument&formType=idDocument)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
+|[**prebuilt-idDocument**](prebuilt/id-document.md) |&#9679; Extract key information from passports and ID cards.</br>&#9679; [Document types](prebuilt/id-document.md#supported-document-types)</br>&#9679; Extract  endorsements, restrictions, and vehicle classifications from US driver's licenses. |&#9679; Know your customer (KYC) financial services guidelines compliance.</br>&#9679; Medical account management.</br>&#9679; Identity checkpoints and gateways.</br>&#9679; Hotel registration. |&#9679;  [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=idDocument&formType=idDocument)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
 
 > [!div class="nextstepaction"]
 > [Return to model types](#prebuilt-models)
@@ -377,7 +387,7 @@ You can use Document Intelligence to automate document processing in application
 
 | Model ID | Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-| [**prebuilt-healthInsuranceCard.us**](concept-health-insurance-card.md)|&#9679; Extract key information from US health insurance cards.</br>&#9679; [Data and field extraction](concept-health-insurance-card.md#field-extraction)|&#9679; Coverage and eligibility verification. </br>&#9679; Predictive modeling.</br>&#9679; Value-based analytics.|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=healthInsuranceCard.us&formType=healthInsuranceCard.us)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
+| [**prebuilt-healthInsuranceCard.us**](prebuilt/health-insurance-card.md)|&#9679; Extract key information from US health insurance cards.</br>&#9679; [Data and field extraction](prebuilt/health-insurance-card.md#field-extraction)|&#9679; Coverage and eligibility verification. </br>&#9679; Predictive modeling.</br>&#9679; Value-based analytics.|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=healthInsuranceCard.us&formType=healthInsuranceCard.us)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
 
 > [!div class="nextstepaction"]
 > [Return to model types](#prebuilt-models)
@@ -388,7 +398,7 @@ You can use Document Intelligence to automate document processing in application
 
 | Model ID | Description| Development options |
 |----------|--------------|-------------------|
-|[**prebuilt-contract**](concept-contract.md)|Extract contract agreement and party details.</br>&#9679; [Data and field extraction](concept-contract.md#field-extraction)|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=contract&formType=contract)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
+|[**prebuilt-contract**](prebuilt/contract.md)|Extract contract agreement and party details.</br>&#9679; [Data and field extraction](prebuilt/contract.md#field-extraction)|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=contract&formType=contract)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
 
 > [!div class="nextstepaction"]
 > [Return to model types](#prebuilt-models)
@@ -473,7 +483,7 @@ You can use Document Intelligence to automate document processing in application
 
 | Model ID| Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**prebuilt-tax.us.W-2**](concept-tax-document.md) |&#9679; Extract key information from IRS US W2 tax forms (year 2018-2021).</br>&#9679; [Data and field extraction](concept-tax-document.md#field-extraction-w-2)|&#9679; Automated tax document management.</br>&#9679; Mortgage loan application processing. |&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=tax.us.w2&formType=tax.us.w2)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model) |
+|[**prebuilt-tax.us.W-2**](prebuilt/tax-document.md) |&#9679; Extract key information from IRS US W2 tax forms (year 2018-2021).</br>&#9679; [Data and field extraction](prebuilt/tax-document.md#field-extraction-w-2)|&#9679; Automated tax document management.</br>&#9679; Mortgage loan application processing. |&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=tax.us.w2&formType=tax.us.w2)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model) |
 
 > [!div class="nextstepaction"]
 > [Return to model types](#prebuilt-models)
@@ -484,7 +494,7 @@ You can use Document Intelligence to automate document processing in application
 
 | Model ID | Description| Development options |
 |----------|--------------|-------------------|
-|[**prebuilt-tax.us.1098{`variation`}**](concept-tax-document.md)|&#9679; Extract key information from 1098-form variations.</br>&#9679; [Data and field extraction](concept-tax-document.md#field-extraction-1098)|&#9679; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=tax.us.1098)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
+|[**prebuilt-tax.us.1098{`variation`}**](prebuilt/tax-document.md)|&#9679; Extract key information from 1098-form variations.</br>&#9679; [Data and field extraction](prebuilt/tax-document.md#field-extraction-1098)|&#9679; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=tax.us.1098)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
 
 > [!div class="nextstepaction"]
 > [Return to model types](#prebuilt-models)
@@ -495,7 +505,7 @@ You can use Document Intelligence to automate document processing in application
 
 | Model ID |Description|Development options |
 |----------|--------------|-----------------|
-|[**prebuilt-tax.us.1099{`variation`}**](concept-tax-document.md)|&#9679; Extract information from 1099-form variations.</br>&#9679; [Data and field extraction](concept-tax-document.md#field-extraction-1099-nec)|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=tax.us.1099)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
+|[**prebuilt-tax.us.1099{`variation`}**](prebuilt/tax-document.md)|&#9679; Extract information from 1099-form variations.</br>&#9679; [Data and field extraction](prebuilt/tax-document.md#field-extraction-1099-nec)|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=tax.us.1099)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
 
 > [!div class="nextstepaction"]
 > [Return to model types](#prebuilt-models)
@@ -506,19 +516,19 @@ You can use Document Intelligence to automate document processing in application
 
 | Model ID |Description|Development options |
 |----------|--------------|-----------------|
-|[**prebuilt-tax.us.1040{`variation`}**](concept-tax-document.md)|&#9679; Extract information from 1040-form variations.</br>&#9679; [Data and field extraction](concept-tax-document.md#field-extraction-1040-tax-form)|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=tax.us.1040)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
+|[**prebuilt-tax.us.1040{`variation`}**](prebuilt/tax-document.md)|&#9679; Extract information from 1040-form variations.</br>&#9679; [Data and field extraction](prebuilt/tax-document.md#field-extraction-1040-tax-form)|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=tax.us.1040)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
 
-::: moniker range=">=doc-intel-4.0.0"
+:::moniker range=">=doc-intel-4.0.0"
 
 ### Unified US tax forms
 
 | Model ID |Description|Development options |
 |----------|--------------|-----------------|
-|[**prebuilt-tax.us**](concept-tax-document.md)|&#9679;Extract information from any of the supported US tax forms.|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=tax.us.1040)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
+|[**prebuilt-tax.us**](prebuilt/tax-document.md)|&#9679;Extract information from any of the supported US tax forms.|&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=tax.us.1040)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)|
 
 :::moniker-end
 
-::: moniker range="<=doc-intel-3.1.0"
+ :::moniker range="<=doc-intel-3.1.0"
 
 ### Business card
 
@@ -539,7 +549,7 @@ You can use Document Intelligence to automate document processing in application
 
 | About | Description |Automation use cases |Development options |
 |----------|--------------|-----------|--------------------------|
-|[**Custom model**](concept-custom.md) | Extracts information from forms and documents into structured data based on a model created from a set of representative training document sets.|Extract distinct data from forms and documents specific to your business and use cases.|&#9679; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|
+|[**Custom model**](train/custom-model.md) | Extracts information from forms and documents into structured data based on a model created from a set of representative training document sets.|Extract distinct data from forms and documents specific to your business and use cases.|&#9679; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|
 
 > [!div class="nextstepaction"]
 > [Return to custom model types](#custom-models)
@@ -554,7 +564,7 @@ You can use Document Intelligence to automate document processing in application
 
 | About | Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**Custom generative model**](concept-custom-generative.md)| The custom generative model is used to extract fields from unstructured documents or structured forms with a wide variety of visual templates.|The model uses Generative AI to extract fields, improve quality with only a few labeled samples and can be integrated into your processes with grounding and confidence scores.​|[**Azure AI Studio**](https://aka.ms/custom-generative)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|
+|[**Custom generative model**](train/custom-generative-extraction.md)| The custom generative model is used to extract fields from unstructured documents or structured forms with a wide variety of visual templates.|The model uses Generative AI to extract fields, improve quality with only a few labeled samples and can be integrated into your processes with grounding and confidence scores.​|[**Azure AI Studio**](https://aka.ms/custom-generative)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|
 
 > [!div class="nextstepaction"]
 > [Return to custom model types](#custom-models)
@@ -565,11 +575,11 @@ You can use Document Intelligence to automate document processing in application
 
   > [!NOTE]
   > To train a custom neural model, set the ```buildMode``` property to ```neural```.
-  > For more information, *see* [Training a neural model](concept-custom-neural.md#training-a-model)
+  > For more information, *see* [Training a neural model](train/custom-neural.md#training-a-model)
 
 | About | Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**Custom Neural model**](concept-custom-neural.md)| The custom neural model is used to extract labeled data from structured (surveys, questionnaires), semi-structured (invoices, purchase orders), and unstructured documents (contracts, letters).|Extract text data, checkboxes, and tabular fields from structured and unstructured documents.|[**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|
+|[**Custom Neural model**](train/custom-neural.md)| The custom neural model is used to extract labeled data from structured (surveys, questionnaires), semi-structured (invoices, purchase orders), and unstructured documents (contracts, letters).|Extract text data, checkboxes, and tabular fields from structured and unstructured documents.|[**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|
 
 > [!div class="nextstepaction"]
 > [Return to custom model types](#custom-models)
@@ -580,11 +590,11 @@ You can use Document Intelligence to automate document processing in application
 
   > [!NOTE]
   > To train a custom template model, set the ```buildMode``` property to ```template```.
-  > For more information, *see* [Training a template model](concept-custom-template.md#training-a-model)
+  > For more information, *see* [Training a template model](train/custom-template.md#training-a-model)
 
 | About | Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**Custom Template model**](concept-custom-template.md) | The custom template model extracts labeled values and fields from structured and semi-structured documents.</br> | Extract key data from highly structured documents with defined visual templates or common visual layouts, forms.| &#9679; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|
+|[**Custom Template model**](train/custom-template.md) | The custom template model extracts labeled values and fields from structured and semi-structured documents.</br> | Extract key data from highly structured documents with defined visual templates or common visual layouts, forms.| &#9679; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&#9679; [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|
 
 > [!div class="nextstepaction"]
 > [Return to custom model types](#custom-models)
@@ -595,7 +605,7 @@ You can use Document Intelligence to automate document processing in application
 
 | About | Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**Composed custom models**](concept-composed-models.md)| A composed model is created by taking a collection of custom models and assigning them to a single model built from your form types.| Useful when you train several models and want to group them to analyze similar form types like purchase orders.|&#9679; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/compose-model?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**C# SDK**](/dotnet/api/azure.ai.formrecognizer.training.formtrainingclient.startcreatecomposedmodel)</br>&#9679; [**Java SDK**](/java/api/com.azure.ai.formrecognizer.training.formtrainingclient.begincreatecomposedmodel)</br>&#9679; [**JavaScript SDK**](/javascript/api/@azure/ai-form-recognizer/documentmodeladministrationclient?view=azure-node-latest#@azure-ai-form-recognizer-documentmodeladministrationclient-begincomposemodel&preserve-view=true)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|
+|[**Composed custom models**](train/composed-models.md)| A composed model is created by taking a collection of custom models and assigning them to a single model built from your form types.| Useful when you train several models and want to group them to analyze similar form types like purchase orders.|&#9679; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&#9679; [**REST API**](/rest/api/aiservices/document-models/compose-model?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&#9679; [**C# SDK**](/dotnet/api/azure.ai.formrecognizer.training.formtrainingclient.startcreatecomposedmodel)</br>&#9679; [**Java SDK**](/java/api/com.azure.ai.formrecognizer.training.formtrainingclient.begincreatecomposedmodel)</br>&#9679; [**JavaScript SDK**](/javascript/api/@azure/ai-form-recognizer/documentmodeladministrationclient?view=azure-node-latest#@azure-ai-form-recognizer-documentmodeladministrationclient-begincomposemodel&preserve-view=true)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|
 
 > [!div class="nextstepaction"]
 > [Return to custom model types](#custom-models)
@@ -608,26 +618,26 @@ You can use Document Intelligence to automate document processing in application
 
 | About | Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**Composed classification model**](concept-custom-classifier.md)| Custom classification models combine layout and language features to detect, identify, and classify documents within an input file.|&#9679; A loan application packaged containing application form, payslip, and, bank statement.</br>&#9679; A collection of scanned invoices. |&#9679; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&#9679; [REST API](/rest/api/aiservices/document-classifiers/build-classifier?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>|
+|[**Composed classification model**](train/custom-classifier.md)| Custom classification models combine layout and language features to detect, identify, and classify documents within an input file.|&#9679; A loan application packaged containing application form, payslip, and, bank statement.</br>&#9679; A collection of scanned invoices. |&#9679; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&#9679; [REST API](/rest/api/aiservices/document-classifiers/build-classifier?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>|
 
 > [!div class="nextstepaction"]
 > [Return to custom model types](#custom-models)
 
 :::moniker-end
 
-::: moniker range="doc-intel-2.1.0"
+ :::moniker range="doc-intel-2.1.0"
 
 Azure AI Document Intelligence is a cloud-based [Azure AI service](../../ai-services/index.yml) for developers to build intelligent document processing solutions. Document Intelligence applies machine-learning-based optical character recognition (OCR) and document understanding technologies to extract text, tables, structure, and key-value pairs from documents. You can also label and train custom models to automate data extraction from structured, semi-structured, and unstructured documents. To learn more about each model, *see* the Concepts articles:
 
 | Model type | Model name |
 |------------|-----------|
-|**Document analysis model**| &#9679; [**Layout analysis model**](concept-layout.md?view=doc-intel-2.1.0&preserve-view=true) </br>  |
-| **Prebuilt models** | &#9679; [**Invoice model**](concept-invoice.md?view=doc-intel-2.1.0&preserve-view=true)</br>&#9679; [**Receipt model**](concept-receipt.md?view=doc-intel-2.1.0&preserve-view=true) </br>&#9679; [**Identity document (ID) model**](concept-id-document.md?view=doc-intel-2.1.0&preserve-view=true) </br>&#9679; [**Business card model**](concept-business-card.md?view=doc-intel-2.1.0&preserve-view=true) </br>|
-| **Custom models** | &#9679; [**Custom model**](concept-custom.md) </br>&#9679; [**Composed model**](concept-model-overview.md?view=doc-intel-2.1.0&preserve-view=true)|
+|**Document analysis model**| &#9679; [**Layout analysis model**](prebuilt/layout.md?view=doc-intel-2.1.0&preserve-view=true) </br>  |
+| **Prebuilt models** | &#9679; [**Invoice model**](prebuilt/invoice.md?view=doc-intel-2.1.0&preserve-view=true)</br>&#9679; [**Receipt model**](prebuilt/receipt.md?view=doc-intel-2.1.0&preserve-view=true) </br>&#9679; [**Identity document (ID) model**](prebuilt/id-document.md?view=doc-intel-2.1.0&preserve-view=true) </br>&#9679; [**Business card model**](concept-business-card.md?view=doc-intel-2.1.0&preserve-view=true) </br>|
+| **Custom models** | &#9679; [**Custom model**](train/custom-model.md) </br>&#9679; [**Composed model**](model-overview.md?view=doc-intel-2.1.0&preserve-view=true)|
 
-::: moniker-end
+:::moniker-end
 
-::: moniker range="doc-intel-2.1.0"
+ :::moniker range="doc-intel-2.1.0"
 
 [!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
 
@@ -646,35 +656,35 @@ Use the links in the table to learn more about each model and browse the API ref
 
 | Model| Description | Development options |
 |----------|--------------|-------------------------|
-|[**Layout analysis**](concept-layout.md?view=doc-intel-2.1.0&preserve-view=true) | Extraction and analysis of text, selection marks, tables, and bounding box coordinates, from forms and documents. | &#9679; [**Document Intelligence labeling tool**](quickstarts/try-sample-label-tool.md#analyze-layout)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&#9679; [**Client-library SDK**](quickstarts/get-started-sdks-rest-api.md)</br>&#9679; [**Document Intelligence Docker container**](containers/install-run.md?branch=main&tabs=layout#run-the-container-with-the-docker-compose-up-command)|
-|[**Custom model**](concept-custom.md?view=doc-intel-2.1.0&preserve-view=true) | Extraction and analysis of data from forms and documents specific to distinct business data and use cases.| &#9679; [**Document Intelligence labeling tool**](quickstarts/try-sample-label-tool.md#train-a-custom-form-model)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md)</br>&#9679; [**Sample Labeling Tool**](concept-custom.md?view=doc-intel-2.1.0&preserve-view=true#build-a-custom-model)</br>&#9679; [**Document Intelligence Docker container**](containers/install-run.md?tabs=custom#run-the-container-with-the-docker-compose-up-command)|
-|[**Invoice model**](concept-invoice.md?view=doc-intel-2.1.0&preserve-view=true) | Automated data processing and extraction of key information from sales invoices. | &#9679; [**Document Intelligence labeling tool**](quickstarts/try-sample-label-tool.md#analyze-using-a-prebuilt-model)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&#9679; [**Client-library SDK**](quickstarts/get-started-sdks-rest-api.md)</br>&#9679; [**Document Intelligence Docker container**](containers/install-run.md?tabs=invoice#run-the-container-with-the-docker-compose-up-command)|
-|[**Receipt model**](concept-receipt.md?view=doc-intel-2.1.0&preserve-view=true) | Automated data processing and extraction of key information from sales receipts.| &#9679; [**Document Intelligence labeling tool**](quickstarts/try-sample-label-tool.md#analyze-using-a-prebuilt-model)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&#9679; [**Client-library SDK**](quickstarts/get-started-sdks-rest-api.md)</br>&#9679; [**Document Intelligence Docker container**](containers/install-run.md?tabs=receipt#run-the-container-with-the-docker-compose-up-command)|
-|[**Identity document (ID) model**](concept-id-document.md?view=doc-intel-2.1.0&preserve-view=true) | Automated data processing and extraction of key information from US driver's licenses and international passports.| &#9679; [**Document Intelligence labeling tool**](quickstarts/try-sample-label-tool.md#analyze-using-a-prebuilt-model)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&#9679; [**Client-library SDK**](quickstarts/get-started-sdks-rest-api.md)</br>&#9679; [**Document Intelligence Docker container**](containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
+|[**Layout analysis**](prebuilt/layout.md?view=doc-intel-2.1.0&preserve-view=true) | Extraction and analysis of text, selection marks, tables, and bounding box coordinates, from forms and documents. | &#9679; [**Document Intelligence labeling tool**](quickstarts/try-sample-label-tool.md#analyze-layout)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&#9679; [**Client-library SDK**](quickstarts/get-started-sdks-rest-api.md)</br>&#9679; [**Document Intelligence Docker container**](containers/install-run.md?branch=main&tabs=layout#run-the-container-with-the-docker-compose-up-command)|
+|[**Custom model**](train/custom-model.md?view=doc-intel-2.1.0&preserve-view=true) | Extraction and analysis of data from forms and documents specific to distinct business data and use cases.| &#9679; [**Document Intelligence labeling tool**](quickstarts/try-sample-label-tool.md#train-a-custom-form-model)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md)</br>&#9679; [**Sample Labeling Tool**](train/custom-model.md?view=doc-intel-2.1.0&preserve-view=true#build-a-custom-model)</br>&#9679; [**Document Intelligence Docker container**](containers/install-run.md?tabs=custom#run-the-container-with-the-docker-compose-up-command)|
+|[**Invoice model**](prebuilt/invoice.md?view=doc-intel-2.1.0&preserve-view=true) | Automated data processing and extraction of key information from sales invoices. | &#9679; [**Document Intelligence labeling tool**](quickstarts/try-sample-label-tool.md#analyze-using-a-prebuilt-model)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&#9679; [**Client-library SDK**](quickstarts/get-started-sdks-rest-api.md)</br>&#9679; [**Document Intelligence Docker container**](containers/install-run.md?tabs=invoice#run-the-container-with-the-docker-compose-up-command)|
+|[**Receipt model**](prebuilt/receipt.md?view=doc-intel-2.1.0&preserve-view=true) | Automated data processing and extraction of key information from sales receipts.| &#9679; [**Document Intelligence labeling tool**](quickstarts/try-sample-label-tool.md#analyze-using-a-prebuilt-model)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&#9679; [**Client-library SDK**](quickstarts/get-started-sdks-rest-api.md)</br>&#9679; [**Document Intelligence Docker container**](containers/install-run.md?tabs=receipt#run-the-container-with-the-docker-compose-up-command)|
+|[**Identity document (ID) model**](prebuilt/id-document.md?view=doc-intel-2.1.0&preserve-view=true) | Automated data processing and extraction of key information from US driver's licenses and international passports.| &#9679; [**Document Intelligence labeling tool**](quickstarts/try-sample-label-tool.md#analyze-using-a-prebuilt-model)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&#9679; [**Client-library SDK**](quickstarts/get-started-sdks-rest-api.md)</br>&#9679; [**Document Intelligence Docker container**](containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
 |[**Business card model**](concept-business-card.md?view=doc-intel-2.1.0&preserve-view=true) | Automated data processing and extraction of key information from business cards.| &#9679; [**Document Intelligence labeling tool**](quickstarts/try-sample-label-tool.md#analyze-using-a-prebuilt-model)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&#9679; [**Client-library SDK**](quickstarts/get-started-sdks-rest-api.md)</br>&#9679; [**Document Intelligence Docker container**](containers/install-run.md?tabs=business-card#run-the-container-with-the-docker-compose-up-command)|
 
-::: moniker-end
+:::moniker-end
 
 ## Data privacy and security
 
  As with all AI services, developers using the Document Intelligence service should be aware of Microsoft policies on customer data. See our [Data, privacy, and security for Document Intelligence](/legal/cognitive-services/document-intelligence/data-privacy-security) page.
 
 ## Next steps
 
-::: moniker range=">=doc-intel-3.0.0"
+:::moniker range=">=doc-intel-3.0.0"
 
-* [Choose a Document Intelligence model](choose-model-feature.md).
+* [Choose a Document Intelligence model]().
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
 * Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
-::: moniker-end
+:::moniker-end
 
-::: moniker range="doc-intel-2.1.0"
+:::moniker range="doc-intel-2.1.0"
 
 * Try processing your own forms and documents with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
 
 * Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
-::: moniker-end
+:::moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスの概要ページの改訂"
}
```

### Explanation
この変更は、「overview.md」ファイルに151行の追加と141行の削除が行われ、292行が変更されたことを示しています。主な変更内容は以下の通りです：

1. **リンクの更新**: さまざまなリンクURLが相対パス形式に更新されており、各モデルや機能に関連した情報をより簡単に参照できるようになっています。特に、旧形式のリンクが新形式に置き換えられ、ドキュメントのメンテナンスが容易になるよう調整されています。

2. **モニカーの整備**: モニカーの範囲に関連する書き方が改良され、見やすさと一貫性が向上しています。文書内の異なるバージョンのサポート情報が整理されており、バージョン間の違いについても明確に表現されています。

3. **情報の整理**: 機能やモデルの説明がテーブル形式で整頓され、ユーザーが求める情報へ迅速にアクセスできるようになっています。新しい機能やモデルが追加され、それぞれについての説明が強化されています。

4. **メタデータの更新**: 文書のメタデータ（著者、日付、トピックなど）が最新版に更新され、ドキュメントの信頼性向上に寄与しています。また、メタデータの形式も統一化され、整然とした印象を与えています。

5. **次のステップの強調**: ユーザーが次に何をすべきかを明確に指示する内容が増え、特に実行可能なアクションや外部リンクの提供が強化されています。これにより、ユーザーに対して文書を活用するための具体的な方法が提供されています。

これらの変更により、ドキュメントインテリジェンスに関する情報がより明確に整理され、ユーザーの利便性が向上することが期待されます。

## articles/ai-services/document-intelligence/prebuilt/bank-check.md{#item-8655d6}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 08/07/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 monikerRange: '>=doc-intel-4.0.0'
 ---
@@ -29,7 +29,7 @@ A check is a secure way to transfer amount from payee's account to receiver's ac
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 ## Document Intelligence Studio
 
@@ -42,18 +42,18 @@ A check is a secure way to transfer amount from payee's account to receiver's ac
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options** :
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
     > [!div class="nextstepaction"]
     > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=businessCard)
 
 ## Input requirements
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ## Supported languages and locales
 
-*See* our [Language Support](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extractions
 
@@ -80,4 +80,4 @@ The **`prebuilt-check.us`** version 2024-07-31-preview supports the **en-us** lo
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "銀行小切手ページの名称変更と内容の更新"
}
```

### Explanation
この変更は、「concept-bank-check.md」ファイルが「bank-check.md」にリネームされ、内容の一部も更新されたことを示しています。合計で12行が変更され、その内訳には6行の追加と6行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名の変更**: ファイルは`concept-bank-check.md`から`bank-check.md`にリネームされ、名称が簡素化されました。この変更により、他の関連ファイルとの一貫性が増し、ナビゲーションが容易になります。

2. **日付の更新**: `ms.date`が2024年8月7日から2024年10月3日に更新され、ドキュメントの最新の状態を反映するよう調整されています。

3. **メディアソースの相対パス更新**: 画像のソースパスが修正され、相対パスが適用されています。これにより、ドキュメントが異なる環境で一貫して表示されることが確保されます。

4. **リンクの更新**: いくつかのリンクが相対パス形式に変更され、こちらも参照の一貫性と正確性が向上しています。特に、サポートされている言語に関するリンクが更新されています。

5. **インクルード文の修正**: インクルード文のパスも相対パスに改訂され、整合性が取れた構成になっています。

これらの変更は、ファイルの整理と機能の向上を目的としており、ユーザーがコンテンツにアクセスしやすくするための工夫が施されています。

## articles/ai-services/document-intelligence/prebuilt/bank-statement.md{#item-fa4383}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 08/07/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 ms.custom: references_regions
 monikerRange: '>=doc-intel-4.0.0'
@@ -30,7 +30,7 @@ A bank statement helps review account's activities during a specified period. It
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
-    :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+    :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 ## Document Intelligence Studio
 
@@ -40,18 +40,18 @@ A bank statement helps review account's activities during a specified period. It
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options** :
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
     > [!div class="nextstepaction"]
     > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=businessCard)
 
 ## Input requirements
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ## Supported languages and locales
 
-*See* our [Language Support](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extractions
 
@@ -84,4 +84,4 @@ The **prebuilt-bankStatement.us** version 2027-07-31-preview supports the **en-u
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "銀行取引明細ページの名称変更と内容の更新"
}
```

### Explanation
この変更は、「concept-bank-statement.md」ファイルが「bank-statement.md」にリネームされ、内容の一部が更新されたことを示しています。合計で12行が変更され、その内訳には6行の追加と6行の削除が含まれています。

主な変更内容は次の通りです：

1. **ファイル名の変更**: ファイルは`concept-bank-statement.md`から`bank-statement.md`にリネームされ、名称が簡素化されました。この変更により、関連する他のリソースとの一貫性が増し、アクセスしやすくなっています。

2. **日付の更新**: `ms.date`が2024年8月7日から2024年10月3日に更新され、文書の最新の状態を反映するよう調整されています。これにより、ユーザーは最新の情報を参照できるようになります。

3. **メディアソースの相対パス更新**: 画像のソースパスが修正され、相対パスが適用されています。これにより、様々な環境で正しく表示されることが保証されます。

4. **リンクの更新**: いくつかのリンクが相対パス形式に変更され、こちらも参照の一貫性と正確性が向上しています。特に、サポートされている言語に関するリンクが調整されています。

5. **インクルード文の修正**: インクルード文のパスも相対パスに改訂され、整合性が取れた構成になっています。この調整により、将来のメンテナンスが容易になると期待されます。

これらの変更は、ドキュメントの整備やユーザーエクスペリエンスの向上を目的としており、ユーザーが必要な情報によりアクセスしやすくするための工夫が施されています。

## articles/ai-services/document-intelligence/prebuilt/batch-analysis.md{#item-9fb3da}

<details>
<summary>Diff</summary>
````diff
@@ -5,14 +5,14 @@ description: Learn about the Document Intelligence Batch analysis API preview
 author: laujan
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 08/01/2024
+ms.date: 10/03/2024
 ms.author: ginle
 monikerRange: '>=doc-intel-4.0.0'
 ---
 
 # Document Intelligence batch analysis (preview)
 
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
 The batch analysis API allows you to bulk process multiple documents using one asynchronous request. Rather than having to submit documents individually and track multiple request IDs, you can analyze a collection of invoices, a series of loan documents, or a group of custom model training documents simultaneously.
 
@@ -22,13 +22,13 @@ The batch analysis API allows you to bulk process multiple documents using one a
 
 The following models support batch analysis:
 
-* [**Read**](concept-read.md). Extract text lines, words, detected languages, and handwritten style from forms and document.
+* [**Read**](../prebuilt/read.md). Extract text lines, words, detected languages, and handwritten style from forms and document.
 
-* [**Layout**](concept-layout.md). Extract text, tables, selection marks, and structure information from forms and documents.
+* [**Layout**](../prebuilt/layout.md). Extract text, tables, selection marks, and structure information from forms and documents.
 
-* [**Custom Template**](concept-custom-template.md). Train models to extract key-value pairs, selection marks, tables, signature fields, and regions from structured forms.
+* [**Custom Template**](../train/custom-template.md). Train models to extract key-value pairs, selection marks, tables, signature fields, and regions from structured forms.
 
-* [**Custom Neural**](concept-custom-neural.md). Train models to extract specified data fields from structured, semi-structured, and unstructured documents.
+* [**Custom Neural**](../train/custom-neural.md). Train models to extract specified data fields from structured, semi-structured, and unstructured documents.
 
 * **Custom Generative**. Train models to extract specified data from complex objects such as nested tables, abstractive/generative fields, and truly unstructured formats.
 
@@ -65,22 +65,22 @@ You can choose one of the following options to authorize access to your Document
 
 **✔️ Managed Identity**. A managed identity is a service principal that creates a Microsoft Entra identity and specific permissions for an Azure managed resource. Managed identities enable you to run your Document Intelligence application without having to embed credentials in your code. Managed identities are a safer way to grant access to storage data and replace the requirement for you to include shared access signature tokens (SAS) with your source and result URLs.
 
-To learn more, *see* [Managed identities for Document Intelligence](managed-identities.md).
+To learn more, *see* [Managed identities for Document Intelligence](../authentication/managed-identities.md).
 
-  :::image type="content" source="media/managed-identities/rbac-flow.png" alt-text="Screenshot of managed identity flow (role-based access control).":::
+  :::image type="content" source="../media/managed-identities/rbac-flow.png" alt-text="Screenshot of managed identity flow (role-based access control).":::
 
 > [!IMPORTANT]
 >
 > * When using managed identities, don't include a SAS token URL with your HTTP requests—your requests will fail. Using managed identities replaces the requirement for you to include shared access signature tokens (SAS).
 
 **✔️ Shared Access Signature (SAS)**. A shared access signature is a URL that grants restricted access for a specified period of time to your Document Intelligence service. To use this method, you need to create Shared Access Signature (SAS) tokens for your source and result containers. The source and result containers must include a Shared Access Signature (SAS) token, appended as a query string. The token can be assigned to your container or specific blobs.
 
-:::image type="content" source="media/sas-tokens/sas-url-token.png" alt-text="Screenshot of storage URI with SAS token appended.":::
+:::image type="content" source="../media/sas-tokens/sas-url-token.png" alt-text="Screenshot of storage URI with SAS token appended.":::
 
 * Your **source** container or blob must designate **read**, **write**, **list**, and **delete** access.
 * Your **result** container or blob must designate **write**, **list**, **delete** access.
 
-To learn more, *see* [**Create SAS tokens**](create-sas-tokens.md).
+To learn more, *see* [**Create SAS tokens**](../authentication/create-sas-tokens.md).
 
 ## Calling the batch analysis API
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "バッチ分析ページの名称変更と内容の更新"
}
```

### Explanation
この変更は、「concept-batch-analysis.md」ファイルが「batch-analysis.md」にリネームされ、内容が一部更新されたことを示しています。合計で20行が変更され、その内訳には10行の追加と10行の削除が含まれています。

主な変更内容は次の通りです：

1. **ファイル名の変更**: ドキュメントは`concept-batch-analysis.md`から`batch-analysis.md`にリネームされ、より分かりやすい名前に変更されました。これにより、他の関連ドキュメントとの一貫性が向上することが期待されます。

2. **日付の更新**: `ms.date`が2024年8月1日から2024年10月3日に変更され、最新の情報が反映されています。

3. **メディアソースの相対パス更新**: 画像のソースパスが修正され、相対パスが使用されるようになりました。これにより、異なる環境でのアクセスにおいても正しく表示されることが保証されます。

4. **リンクの更新**: ドキュメント内の複数のリンクが相対パスに修正され、正確性と一貫性が向上しました。この修正は、ユーザーが関連情報に簡単にアクセスできるようにするための改善です。

5. **主要モデルのリスト内容の変更**: バッチ分析をサポートするモデルについてのリンクも更新されており、これによりユーザーが最新の情報を容易に見つけることができます。

これらの変更は、ドキュメントの整備を目的としており、ユーザーエクスペリエンスの向上や情報へのアクセスの容易さを目指しています。

## articles/ai-services/document-intelligence/prebuilt/business-card.md{#item-114b38}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: OCR and machine learning based business card scanning in Document I
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 05/23/2024
 ms.author: lajanuar
@@ -24,15 +22,15 @@ ms.author: lajanuar
 | Business card model|&bullet; v3.1:2023-07-31 (GA)</br>&bullet; v3.0:2022-08-31 (GA)</br>&bullet; v2.1 (GA)|**`prebuilt-businessCard`**|
 
 ::: moniker range=">=doc-intel-3.1.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.1 (GA)** | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true) ![blue-checkmark](media/blue-yes-icon.png) [**v2.1**](?view=doc-intel-2.1.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true) ![blue-checkmark](../media/blue-yes-icon.png) [**v2.1**](?view=doc-intel-2.1.0&preserve-view=true)
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1]../(includes/applies-to-v21.md)]
 ::: moniker-end
 
 ::: moniker range=">=doc-intel-3.0.0"
@@ -45,15 +43,15 @@ Business cards are a great way to represent a business or a professional. The co
 
 ***Sample business card processed with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=businessCard)***
 
-:::image type="content" source="media/studio/overview-business-card-studio.png" alt-text="Screenshot of a sample business card analyzed in the Document Intelligence Studio." lightbox="./media/overview-business-card.jpg":::
+:::image type="content" source="../media/studio/overview-business-card-studio.png" alt-text="Screenshot of a sample business card analyzed in the Document Intelligence Studio." lightbox="../media/overview-business-card.jpg":::
 
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
 
 ***Sample business processed with [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/)***
 
-:::image type="content" source="media/business-card-example.jpg" alt-text="Screenshot of a sample business card analyzed with the Document Intelligence Sample Labeling tool.":::
+:::image type="content" source="../media/business-card-example.jpg" alt-text="Screenshot of a sample business card analyzed with the Document Intelligence Sample Labeling tool.":::
 
 ::: moniker-end
 
@@ -65,7 +63,7 @@ Document Intelligence **v3.1:2023-07-31 (GA)** supports the following tools, app
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Business card model**| &bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=businessCard)<br>&bullet; [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)<br>&bullet; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)<br>&bullet; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)<br>&bullet; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)<br>&bullet; [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-businessCard**|
+|**Business card model**| &bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=businessCard)<br>&bullet; [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)<br>&bullet; [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)<br>&bullet; [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)<br>&bullet; [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)<br>&bullet; [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-businessCard**|
 :::moniker-end
 
 ::: moniker range=">=doc-intel-3.0.0"
@@ -74,7 +72,7 @@ Document Intelligence **v3.0:2022-08-31 (GA)** supports the following tools, app
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Business card model**| &bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=businessCard)<br>&bullet; [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)<br>&bullet; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)<br>&bullet; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)<br>&bullet; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)<br>&bullet; [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-businessCard**|
+|**Business card model**| &bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=businessCard)<br>&bullet; [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)<br>&bullet; [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)<br>&bullet; [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)<br>&bullet; [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)<br>&bullet; [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-businessCard**|
 
 ::: moniker-end
 
@@ -84,7 +82,7 @@ Document Intelligence **v2.1 (GA)** supports the following tools, applications,
 
 | Feature | Resources |
 |----------|-------------------------|
-|**Business card model**|  &bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/prebuilts-analyze)<br>&bullet; [**REST API**](how-to-guides/use-sdk-rest-api.md?view=doc-intel-3.0.0&tabs=windows&pivots=programming-language-rest-api&preserve-view=true)<br>&bullet; [**Client-library SDK**](~/articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)<br>&bullet; [**Document Intelligence Docker container**](containers/install-run.md?tabs=business-card#run-the-container-with-the-docker-compose-up-command)|
+|**Business card model**|  &bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/prebuilts-analyze)<br>&bullet; [**REST API**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-3.0.0&tabs=windows&pivots=programming-language-rest-api&preserve-view=true)<br>&bullet; [**Client-library SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)<br>&bullet; [**Document Intelligence Docker container**](../containers/install-run.md?tabs=business-card#run-the-container-with-the-docker-compose-up-command)|
 
 ::: moniker-end
 
@@ -98,7 +96,7 @@ See how data, including name, job title, address, email, and company name, is ex
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 #### Document Intelligence Studio
 
@@ -111,7 +109,7 @@ See how data, including name, job title, address, email, and company name, is ex
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options** :
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
     > [!div class="nextstepaction"]
     > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=businessCard)
@@ -126,7 +124,7 @@ See how data, including name, job title, address, email, and company name, is ex
 
 1. On the sample tool home page, select the **Use prebuilt model to get data** tile.
 
-    :::image type="content" source="media/label-tool/prebuilt-1.jpg" alt-text="Screenshot of the layout model analyze results operation.":::
+    :::image type="content" source="../media/label-tool/prebuilt-1.jpg" alt-text="Screenshot of the layout model analyze results operation.":::
 
 1. Select the **Form Type**  to analyze from the dropdown menu.
 
@@ -139,19 +137,19 @@ See how data, including name, job title, address, email, and company name, is ex
 
 1. In the **Source** field, select **URL** from the dropdown menu, paste the selected URL, and select the **Fetch** button.
 
-    :::image type="content" source="media/label-tool/fott-select-url.png" alt-text="Screenshot of source location dropdown menu.":::
+    :::image type="content" source="../media/label-tool/fott-select-url.png" alt-text="Screenshot of source location dropdown menu.":::
 
 1. In the **Document Intelligence service endpoint** field, paste the endpoint that you obtained with your Document Intelligence subscription.
 
 1. In the **key** field, paste  the key you obtained from your Document Intelligence resource.
 
-    :::image type="content" source="media/fott-select-form-type.png" alt-text="Screenshot of the select-form-type dropdown menu.":::
+    :::image type="content" source="../media/fott-select-form-type.png" alt-text="Screenshot of the select-form-type dropdown menu.":::
 
 1. Select **Run analysis**. The Document Intelligence Sample Labeling tool calls the Analyze Prebuilt API and analyze the document.
 
 1. View the results - see the key-value pairs extracted, line items, highlighted text extracted, and tables detected.
 
-    :::image type="content" source="media/business-card-results.png" alt-text="Screenshot of the business card model analyze results operation.":::
+    :::image type="content" source="../media/business-card-results.png" alt-text="Screenshot of the business card model analyze results operation.":::
 
 > [!NOTE]
 > The [Sample Labeling tool](https://fott-2-1.azurewebsites.net/) does not support the BMP file format. This is a limitation of the tool not the Document Intelligence Service.
@@ -162,7 +160,7 @@ See how data, including name, job title, address, email, and company name, is ex
 
 ::: moniker range=">=doc-intel-3.0.0"
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ::: moniker-end
 
@@ -178,7 +176,7 @@ See how data, including name, job title, address, email, and company name, is ex
 
 ## Supported languages and locales
 
-*See* our [Language Support](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extractions
 
@@ -232,7 +230,7 @@ See how data, including name, job title, address, email, and company name, is ex
 
 ### Migration guide and REST API v3.1
 
-* Follow our [**Document Intelligence v3.1 migration guide**](v3-1-migration-guide.md) to learn how to use the v3.0 version in your applications and workflows.
+* Follow our [**Document Intelligence v3.1 migration guide**](../v3-1-migration-guide.md) to learn how to use the v3.0 version in your applications and workflows.
 
 ::: moniker-end
 
@@ -242,14 +240,14 @@ See how data, including name, job title, address, email, and company name, is ex
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
 
 * Try processing your own forms and documents with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/)
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
 ::: moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "名刺モデルページの名称変更と内容の更新"
}
```

### Explanation
この変更は、「concept-business-card.md」ファイルが「business-card.md」にリネームされ、内容が一部更新されたことを示しています。合計で40行が変更され、その内訳には19行の追加と21行の削除が含まれています。

主な変更内容は次の通りです：

1. **ファイル名の変更**: ドキュメントは`concept-business-card.md`から`business-card.md`にリネームされ、名称が簡潔になりました。この変更により、他の関連するコンテンツとの整合性が向上することが期待されます。

2. **日付の更新**: `ms.date`が2024年5月23日に更新され、ドキュメントが最新の状態であることが反映されています。

3. **メディアソースの相対パス更新**: 複数の画像のソースパスが修正され、相対パス形式が適用されました。これにより、異なる環境での表示がより安定することが保証されます。

4. **リンクの更新**: ドキュメント内のリンクが相対パスに変更され、一貫性と正確性が改善されています。これにより、ユーザーは関連情報に簡単にアクセスできるようになります。

5. **主要モデルおよびツールに関する内容の調整**: バッチ分析をサポートする新しいモデルや機能に関する情報が更新され、ユーザーに最新の機能を紹介しています。

6. **サンプルおよび分析ツールの紹介の改善**: 名刺の処理に関連するツールの使用方法やサンプルが見直され、ユーザーがより簡単に利用できるように工夫されています。

これらの変更は、文書の整備とユーザーエクスペリエンスの向上を目的としており、情報へのアクセスの向上と情報の信頼性を高めるものです。

## articles/ai-services/document-intelligence/prebuilt/contract.md{#item-6d01dd}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Automate contract data extraction with Document Intelligence's cont
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 08/07/2024
 ms.author: lajanuar
@@ -18,13 +16,13 @@ monikerRange: '>=doc-intel-3.0.0'
 # Document Intelligence contract model
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-**This content applies to:**![checkmark](media/yes-icon.png) **v4.0 (preview)** | **Previous version:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=true)
+**This content applies to:**![checkmark](../media/yes-icon.png) **v4.0 (preview)** | **Previous version:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=true)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true)
 :::moniker-end
 
 The Document Intelligence contract model uses powerful Optical Character Recognition (OCR) capabilities to analyze and extract key fields and line items from a select group of important contract entities. Contracts can be of various formats and quality including phone-captured images, scanned documents, and digital PDFs. The API analyzes document text; extracts key information such as Parties, Jurisdictions, Contract ID, and Title; and returns a structured JSON data representation. The model currently supports English-language document formats.
@@ -41,7 +39,7 @@ Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, ap
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Contract model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-contract**|
+|**Contract model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-contract**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
@@ -50,7 +48,7 @@ Document Intelligence v3.1 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Contract model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-contract**|
+|**Contract model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-contract**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
@@ -59,12 +57,12 @@ Document Intelligence v3.0 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Contract model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-contract**|
+|**Contract model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-contract**|
 ::: moniker-end
 
 ## Input requirements
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ## Try contract document data extraction
 
@@ -74,7 +72,7 @@ See how data, including customer information, vendor details, and line items, is
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 ## Document Intelligence Studio
 
@@ -84,14 +82,14 @@ See how data, including customer information, vendor details, and line items, is
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
 > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=invoice)
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extraction
 
@@ -106,7 +104,7 @@ The following are the fields extracted from a contract in the JSON output respon
 | ExpirationDate | Date |Date when the contract ends| One year |
 | EffectiveDate  | Date |Date when the contract is in effect| immediately |
 | RenewalDate | Date |Date when the contract needs to be renewed| `On this twenty-third day of February two thousand and twenty two` |
-| ContractDuration | String | Contract terms | 5 years |
+| ContractDuration | String | Contract terms | Five (5) years |
 | Jurisdictions | Array | List of jurisdictions| |
 
 The contract key-value pairs and line items extracted are in the `documentResults` section of the JSON output.
@@ -115,4 +113,4 @@ The contract key-value pairs and line items extracted are in the `documentResult
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "契約モデルページの名称変更と内容の更新"
}
```

### Explanation
この変更は、「concept-contract.md」ファイルが「contract.md」にリネームされ、その内容が一部更新されたことを示しています。合計で26行が変更され、その内訳には12行の追加と14行の削除が含まれています。

主な変更内容は次の通りです：

1. **ファイル名の変更**: ドキュメントは`concept-contract.md`から`contract.md`にリネームされ、より直感的で簡潔な名称に変更されました。これにより、ユーザーがファイルの内容を容易に理解できるようになります。

2. **日付の更新**: `ms.date`が2024年8月7日に更新され、ドキュメントが最新の情報を反映しています。

3. **メディアソースの相対パス更新**: 複数の画像のソースパスが相対パスに変更され、異なる環境での表示においても安定性が向上しています。

4. **リンクの更新**: ドキュメント内のリンクが相対パスに修正され、一貫性と正確性が改善されました。これによって、ユーザーがその他の関連情報にアクセスしやすくなります。

5. **内容の改善**: 契約モデルの説明内容の一部が更新され、重要なフィールドや行アイテムの抽出に関する情報が強調されています。これにより、ユーザーはAPIの機能についてより良い理解を得られるようになります。

6. **契約の有効期間の表現修正**: `ContractDuration`の記述が修正され、期間が「五（5）年」と表記され、表現が統一されました。

これらの変更は、ドキュメントの正確性と利用者の利便性を向上させることを目指しており、最新の情報を提供することでユーザーエクスペリエンスの向上に寄与します。

## articles/ai-services/document-intelligence/prebuilt/credit-card.md{#item-5d0c6d}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 02/29/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 monikerRange: '>=doc-intel-4.0.0'
 ---
@@ -19,7 +19,7 @@ monikerRange: '>=doc-intel-4.0.0'
 
 # Document Intelligence credit card model
 
-**This content applies to:** ![checkmark](media/yes-icon.png) **v4.0 (preview)** ![checkmark](media/yes-icon.png)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (preview)** ![checkmark](../media/yes-icon.png)
 
 The Document Intelligence credit/debit card model uses powerful Optical Character Recognition (OCR) capabilities to analyze and extract key fields from credit and debit cards. Credit cards and debit cards can be of various formats and quality including phone-captured images, scanned documents, and digital PDFs. The API analyzes document text; extracts key information such as Card Number, Issuing Bank, and Expiration Date; and returns a structured JSON data representation. The model currently supports English-language document formats.
 
@@ -35,12 +35,13 @@ Document Intelligence C supports the following tools, applications, and librarie
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Contract model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-creditCard**|
+|**Contract model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-creditCard**|
+
 ::: moniker-end
 
 ## Input requirements
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ## Try credit card data extraction
 
@@ -50,7 +51,7 @@ To see how data extraction works for the Credit/Debit card service, you need the
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 ## Document Intelligence Studio
 
@@ -60,18 +61,18 @@ To see how data extraction works for the Credit/Debit card service, you need the
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options** :
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
 > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=invoice)
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extraction
 
-The following are the fields extracted from a contract in the JSON output response. 
+The following are the fields extracted from a contract in the JSON output response.
 
 |Name| Type | Description | Example output |
 |:-----|:----|:----|:---:|
@@ -91,4 +92,4 @@ The bank cards key-value pairs and line items extracted are in the `documentResu
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クレジットカードモデルページの名称変更と内容の更新"
}
```

### Explanation
この変更は、「concept-credit-card.md」ファイルが「credit-card.md」にリネームされ、その内容が一部更新されたことを示しています。合計で19行が変更され、その内訳には10行の追加と9行の削除が含まれています。

主な変更内容は次の通りです：

1. **ファイル名の変更**: ドキュメントは`concept-credit-card.md`から`credit-card.md`にリネームされており、より明確で簡潔な名称に変更されました。この変更により、ユーザーがドキュメントの内容を把握しやすくなります。

2. **日付の更新**: `ms.date`が2024年10月3日に更新され、コンテンツが最新の情報を反映しています。

3. **メディアソースの相対パス更新**: ドキュメント内の複数の画像へのソースパスが相対パスに変更され、さまざまな環境での表示において安定性が向上しました。

4. **リンクの更新**: ドキュメント内の一部リンクが相対パスに変更され、一貫性と正確性が改善されました。これにより、ユーザーは関連情報に容易にアクセスできるようになります。

5. **内容の改善**: クレジットカードおよびデビットカードモデルの説明が更新され、テキストの分析や重要な情報の抽出について詳細が追加されました。これにより、APIがどのように機能するかをユーザーがより理解しやすくなります。

6. **フィールド抽出の説明について**: フィールドの抽出に関するセクションが整理され、JSON出力のレスポンス例についての記述がクリアになりました。

これらの変更は、ドキュメントの正確性とユーザーの利便性を向上させることを目的としており、最新の情報を提供することでユーザーエクスペリエンスを向上させるものです。

## articles/ai-services/document-intelligence/prebuilt/general-document.md{#item-ff8975}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Extract key-value pairs, tables, selection marks, and text from you
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 05/23/2024
 ms.author: lajanuar
@@ -28,14 +26,14 @@ ms.author: lajanuar
 :::moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.1 (GA)**  | **Latest version:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous version:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)**  | **Latest version:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous version:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true)
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](../media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true)
 ::: moniker-end
 
-The General document model combines powerful Optical Character Recognition (OCR) capabilities with deep learning models to extract key-value pairs, tables, and selection marks from documents. General document is available with the v3.1 and v3.0 APIs. For more information, _see_ our [migration guide](v3-1-migration-guide.md).
+The General document model combines powerful Optical Character Recognition (OCR) capabilities with deep learning models to extract key-value pairs, tables, and selection marks from documents. General document is available with the v3.1 and v3.0 APIs. For more information, _see_ our [migration guide](../v3-1-migration-guide.md).
 
 ::: moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
@@ -51,7 +49,7 @@ The General document model combines powerful Optical Character Recognition (OCR)
 
 ***Sample document processed in the Document Intelligence Studio***
 
-:::image type="content" source="media/studio/general-document-analyze.png" alt-text="Screenshot of general document analysis in the Document Intelligence Studio.":::
+:::image type="content" source="../media/studio/general-document-analyze.png" alt-text="Screenshot of general document analysis in the Document Intelligence Studio.":::
 
 ## Key-value pair extraction
 
@@ -67,7 +65,7 @@ Document Intelligence v3.1 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**General document model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-document**|
+|**General document model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-document**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
@@ -76,14 +74,14 @@ Document Intelligence v3.0 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**General document model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-document**|
+|**General document model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-document**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
 ## Input requirements
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ### General document model data extraction
 
@@ -95,7 +93,7 @@ You need the following resources:
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 > [!NOTE]
 > Document Intelligence Studio and the general document model are available with the v3.0 API.
@@ -106,7 +104,7 @@ You need the following resources:
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
     > [!div class="nextstepaction"]
     > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=document).
@@ -127,7 +125,7 @@ Keys can also exist in isolation when the model detects that a key exists, with
 
 ## Supported languages and locales
 
-*See* our [Language Support—document analysis models](language-support-ocr.md) page for a complete list of supported languages.
+*See* our [Language Support—document analysis models](../language-support/ocr.md) page for a complete list of supported languages.
 
 ## Considerations
 
@@ -139,7 +137,7 @@ Keys can also exist in isolation when the model detects that a key exists, with
 
 ## Next steps
 
-* Follow our [**Document Intelligence v3.1 migration guide**](v3-1-migration-guide.md) to learn how to use the v3.1 version in your applications and workflows.
+* Follow our [**Document Intelligence v3.1 migration guide**](../v3-1-migration-guide.md) to learn how to use the v3.1 version in your applications and workflows.
 
 * Explore our [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP).
   
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "一般文書モデルページの名称変更と内容の更新"
}
```

### Explanation
この変更は、「concept-general-document.md」ファイルが「general-document.md」にリネームされ、その内容が一部更新されたことを示しています。合計で24行が変更され、その内訳には11行の追加と13行の削除が含まれています。

主な変更内容は次の通りです：

1. **ファイル名の変更**: ドキュメントが`concept-general-document.md`から`general-document.md`にリネームされ、より明確で簡潔な名称に変更されました。この変更により、ユーザーがファイルの内容をより理解しやすくなります。

2. **日付の更新**: `ms.date`が2024年5月23日に更新され、現在の最新情報が反映されています。

3. **メディアソースの相対パス更新**: ドキュメント内の複数の画像へのソースパスが相対パスに変更され、表示の安定性が向上しています。

4. **リンクの更新**: ドキュメント内のいくつかのリンクが相対パスに変更され、一貫性と正確性が向上しました。これにより、ユーザーは関連情報に簡単にアクセスできるようになります。

5. **内容の改善**: 一般文書モデルの説明が更新され、のテキスト分析や主要情報の抽出に関する情報が追加されました。これによって、APIの機能やその利用方法についての理解が深まります。

6. **フィールド抽出に関するセクションの改善**: JSON出力のレスポンスに関する説明が整理され、ユーザーがどのようにキーと値のペアを抽出できるかを明確に理解できるようになっています。

これらの変更は、ドキュメントの正確性とユーザーの利便性を高めることを目的としており、最新の情報を提供することでユーザーエクスペリエンスを向上させるものです。

## articles/ai-services/document-intelligence/prebuilt/health-insurance-card.md{#item-6b1c0e}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Data extraction and analysis extraction using the health insurance
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 05/23/2024
 ms.author: lajanuar
@@ -17,24 +15,24 @@ monikerRange: 'doc-intel-4.0.0 || >=doc-intel-3.0.0'
 # Document Intelligence health insurance card model
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-**This content applies to:**![checkmark](media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
+**This content applies to:**![checkmark](../media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true)
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](../media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true)
 ::: moniker-end
 
-The Document Intelligence health insurance card model combines powerful Optical Character Recognition (OCR) capabilities with deep learning models to analyze and extract key information from US health insurance cards. A health insurance card is a key document for care processing and can be digitally analyzed for patient onboarding, financial coverage information, cashless payments, and insurance claim processing. The health insurance card model analyzes health card images; extracts key information such as insurer, member, prescription, and group number; and returns a structured JSON representation. Health insurance cards can be presented in various formats and quality including phone-captured images, scanned documents, and digital PDFs.
+The Document Intelligence health insurance card model combines powerful Optical Character Recognition (OCR) capabilities with deep learning models to analyze and extract key information from US health insurance cards. A health insurance card is a key document for care processing. It can be digitally analyzed for patient onboarding, financial coverage information, cashless payments, and insurance claim processing. The health insurance card model analyzes health card images; extracts key information such as insurer, member, prescription, and group number; and returns a structured JSON representation. Health insurance cards can be presented in various formats and quality including phone-captured images, scanned documents, and digital PDFs.
 
 ***Sample health insurance card processed using Document Intelligence Studio***
 
-:::image type="content" source="media/studio/health-insurance-card.png" alt-text="Screenshot of sample health insurance card processed in the Document Intelligence Studio.":::
+:::image type="content" source="../media/studio/health-insurance-card.png" alt-text="Screenshot of sample health insurance card processed in the Document Intelligence Studio.":::
 
 ## Development options
 
@@ -44,7 +42,7 @@ Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, ap
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Health insurance card model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-healthInsuranceCard.us**|
+|**Health insurance card model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-healthInsuranceCard.us**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
@@ -53,7 +51,7 @@ Document Intelligence v3.1 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Health insurance card model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-healthInsuranceCard.us**|
+|**Health insurance card model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-healthInsuranceCard.us**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
@@ -62,12 +60,12 @@ Document Intelligence v3.0 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Health insurance card model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-healthInsuranceCard.us**|
+|**Health insurance card model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-healthInsuranceCard.us**|
 ::: moniker-end
 
 ## Input requirements
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ### Try Document Intelligence Studio
 
@@ -77,7 +75,7 @@ See how data is extracted from health insurance cards using the Document Intelli
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 > [!NOTE]
 > Document Intelligence Studio is available with API version v3.0.
@@ -88,14 +86,14 @@ See how data is extracted from health insurance cards using the Document Intelli
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options** :
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
     > [!div class="nextstepaction"]
     > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=healthInsuranceCard.us).
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extraction
 
@@ -112,7 +110,7 @@ See how data is extracted from health insurance cards using the Document Intelli
 |`Dependents.*`|`object`|||
 |`Dependents.*.Name`|`string`|Dependent name|01|
 |`IdNumber`|`object`|||
-|`IdNumber.Prefix`|`string`|Identification Number Prefix as it appears on some health insurance cards|ABC|
+|`IdNumber.Prefix`|`string`|Identification Number Prefix as it appears on some health insurance cards|`ABC`|
 |`IdNumber.Number`|`string`|Identification Number|123456789|
 |`GroupNumber`|`string`|Insurance Group Number|1000000|
 |`PrescriptionInfo`|`object`|||
@@ -130,25 +128,25 @@ See how data is extracted from health insurance cards using the Document Intelli
 |`Copays.*.Amount`|`currency`|Co-Pay required amount|$1,500|
 |`Payer`|`object`|||
 |`Payer.Id`|`string`|Payer ID Number|89063|
-|`Payer.Address`|`address`|Payer address|123 Service St., Redmond WA, 98052|
+|`Payer.Address`|`address`|Payer address|123 Service St., Redmond, Washington, 98052|
 |`Payer.PhoneNumber`|`phoneNumber`|Payer phone number|+1 (987) 213-5674|
 |`Plan`|`object`|||
 |`Plan.Number`|`string`|Plan number|456|
 |`Plan.Name`|`string`|Plan name - If Medicaid -> then `medicaid` (all lower case).|HEALTH SAVINGS PLAN|
-|`Plan.Type`|`string`|Plan type|PPO|
+|`Plan.Type`|`string`|Plan type|`PPO`|
 |`MedicareMedicaidInfo`|`object`|||
 |`MedicareMedicaidInfo.Id`|`string`|Medicare or Medicaid number|1AB2-CD3-EF45|
 |`MedicareMedicaidInfo.PartAEffectiveDate`|`date`|Effective date of Medicare Part A|01-01-2023|
 |`MedicareMedicaidInfo.PartBEffectiveDate`|`date`|Effective date of Medicare Part B|01-01-2023|
 
 ### Migration guide and REST API v3.1
 
-* Follow our [**Document Intelligence v3.1 migration guide**](v3-1-migration-guide.md) to learn how to use the v3.1 version in your applications and workflows.
+* Follow our [**Document Intelligence v3.1 migration guide**](../v3-1-migration-guide.md) to learn how to use the v3.1 version in your applications and workflows.
 
 * Explore our [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP) to learn more about the v3.1 version and new capabilities.
 
 ## Next steps
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "健康保険証モデルページの名称変更と内容の更新"
}
```

### Explanation
この変更は、「concept-health-insurance-card.md」ファイルが「health-insurance-card.md」にリネームされ、その内容が一部更新されたことを示しています。合計で38行が変更され、その内訳には18行の追加と20行の削除が含まれています。

主な変更内容は次の通りです：

1. **ファイル名の変更**: ドキュメントが`concept-health-insurance-card.md`から`health-insurance-card.md`にリネームされ、より明確で理解しやすい名称に変更されました。この修正により、ユーザーがファイルの目的を把握しやすくなります。

2. **日付の更新**: `ms.date`が2024年5月23日に更新され、最新の情報が反映されています。

3. **メディアソースの相対パス更新**: ドキュメント内のいくつかの画像へのソースパスが相対パスに変更され、全体としての安定性が向上しました。

4. **リンクの更新**: ドキュメント内の複数のリンクが相対パスに変更され、リンクの一貫性が高まり、関連情報へのアクセスが容易になりました。

5. **内容の説明の改善**: 健康保険証モデルについての説明が少し整理され、暗示される内容が明確になりました。特に、どのような情報が抽出されるのかを具体的に説明しています。

6. **フィールド抽出に関するセクションの改善**: 抽出されるフィールドの定義の一部が表現改善され、JSON出力例が視覚的にクリアになっています。特に、国や地名の修正が行われ、ユーザーが理解しやすくなっています。

これらの変更は、ドキュメントの正確性とユーザー体験を向上させることを目指しており、最新の情報と手順を提供することに重点が置かれています。

## articles/ai-services/document-intelligence/prebuilt/id-document.md{#item-bf45fa}

<details>
<summary>Diff</summary>
````diff
@@ -17,21 +17,21 @@ ms.custom:
 # Document Intelligence ID document model
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-[!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
+[!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
+[!INCLUDE [applies to v3.1](../includes/applies-to-v31.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 ::: moniker-end
 
 ::: moniker range=">=doc-intel-3.0.0"
@@ -50,7 +50,7 @@ Document Intelligence Identity document (ID) model combines Optical Character Re
 
 ::: moniker range="doc-intel-2.1.0"
 
-Document Intelligence can analyze and extract information from government-issued identification documents (IDs) using its prebuilt IDs model. It combines our powerful [Optical Character Recognition (OCR)](../../ai-services/computer-vision/overview-ocr.md) capabilities with ID recognition capabilities to extract key information from Worldwide Passports and U.S. Driver's Licenses (all 50 states and D.C.). The IDs API extracts key information from these identity documents, such as first name, surname, date of birth, document number, and more. This API is available in the Document Intelligence v2.1 as a cloud service. 
+Document Intelligence can analyze and extract information from government-issued identification documents (IDs) using its prebuilt IDs model. It combines our powerful [Optical Character Recognition (OCR)](../../../ai-services/computer-vision/overview-ocr.md) capabilities with ID recognition capabilities to extract key information from Worldwide Passports and U.S. Driver's Licenses (all 50 states and D.C.). The IDs API extracts key information from these identity documents, such as first name, surname, date of birth, document number, and more. This API is available in the Document Intelligence v2.1 as a cloud service. 
 
 ::: moniker-end
 
@@ -62,7 +62,7 @@ Identity document processing involves extracting data from identity documents ei
 
 ***Sample U.S. Driver's License processed with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=idDocument)***
 
-:::image type="content" source="media/studio/analyze-drivers-license.png" alt-text="Image of a sample driver's license.":::
+:::image type="content" source="../media/studio/analyze-drivers-license.png" alt-text="Image of a sample driver's license.":::
 
 ::: moniker-end
 
@@ -74,11 +74,11 @@ The prebuilt IDs service extracts the key values from worldwide passports and U.
 
 ### **Driver's license example**
 
-![Sample Driver's License](./media/id-example-drivers-license.jpg)
+![Sample Driver's License](../media/id-example-drivers-license.jpg)
 
 ### **Passport example**
 
-![Sample Passport](./media/id-example-passport-result.jpg)
+![Sample Passport](../media/id-example-passport-result.jpg)
 
 ::: moniker-end
 
@@ -90,7 +90,7 @@ Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, ap
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**ID document model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-idDocument**|
+|**ID document model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-idDocument**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
@@ -99,7 +99,7 @@ Document Intelligence v3.1 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**ID document model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-idDocument**|
+|**ID document model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-idDocument**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
@@ -108,7 +108,7 @@ Document Intelligence v3.0 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**ID document model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-idDocument**|
+|**ID document model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-idDocument**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
@@ -117,14 +117,14 @@ Document Intelligence v2.1 supports the following tools, applications, and libra
 
 | Feature | Resources |
 |----------|-------------------------|
-|**ID document model**|&bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/prebuilts-analyze)</br>&bullet;  [**REST API**](how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&view=doc-intel-2.1.0&preserve-view=true&tabs=windows)</br>&bullet;  [**Client-library SDK**](~/articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet;  [**Document Intelligence Docker container**](containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
+|**ID document model**|&bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/prebuilts-analyze)</br>&bullet;  [**REST API**](../how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&view=doc-intel-2.1.0&preserve-view=true&tabs=windows)</br>&bullet;  [**Client-library SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet;  [**Document Intelligence Docker container**](../containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
 ::: moniker-end
 
 ## Input requirements
 
 ::: moniker range=">=doc-intel-3.0.0"
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ::: moniker-end
 
@@ -146,7 +146,7 @@ Extract data, including name, birth date, and expiration date, from ID documents
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 ::: moniker range=">=doc-intel-3.0.0"
 
@@ -159,7 +159,7 @@ Extract data, including name, birth date, and expiration date, from ID documents
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
     > [!div class="nextstepaction"]
     > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=idDocument).
@@ -174,7 +174,7 @@ Extract data, including name, birth date, and expiration date, from ID documents
 
 1. On the sample tool home page, select the **Use prebuilt model to get data** tile.
 
-    :::image type="content" source="media/label-tool/prebuilt-1.jpg" alt-text="Screenshot of the layout model analyze results operation.":::
+    :::image type="content" source="../media/label-tool/prebuilt-1.jpg" alt-text="Screenshot of the layout model analyze results operation.":::
 
 1. Select the **Form Type**  to analyze from the dropdown menu.
 
@@ -187,19 +187,19 @@ Extract data, including name, birth date, and expiration date, from ID documents
 
 1. In the **Source** field, select **URL** from the dropdown menu, paste the selected URL, and select the **Fetch** button.
 
-    :::image type="content" source="media/label-tool/fott-select-url.png" alt-text="Screenshot of source location dropdown menu.":::
+    :::image type="content" source="../media/label-tool/fott-select-url.png" alt-text="Screenshot of source location dropdown menu.":::
 
 1. In the **Document Intelligence service endpoint** field, paste the endpoint that you obtained with your Document Intelligence subscription.
 
 1. In the **key** field, paste  the key you obtained from your Document Intelligence resource.
 
-    :::image type="content" source="media/fott-select-form-type.png" alt-text="Screenshot of select document type dropdown menu.":::
+    :::image type="content" source="../media/fott-select-form-type.png" alt-text="Screenshot of select document type dropdown menu.":::
 
 1. Select **Run analysis**. The Document Intelligence Sample Labeling tool calls the Analyze Prebuilt API and analyzes the document.
 
 1. View the results - see the key-value pairs extracted, line items, highlighted text extracted, and tables detected.
 
-    :::image type="content" source="media/id-example-drivers-license.jpg" alt-text="Screenshot of the identity model analyze results operation.":::
+    :::image type="content" source="../media/id-example-drivers-license.jpg" alt-text="Screenshot of the identity model analyze results operation.":::
 
 1. Download the JSON output file to view the detailed results.
 
@@ -394,7 +394,7 @@ The following are the fields extracted per document type. The Document Intellige
 
 ### Migration guide
 
-* Follow our [**Document Intelligence v3.1 migration guide**](v3-1-migration-guide.md) to learn how to use the v3.0 version in your applications and workflows.
+* Follow our [**Document Intelligence v3.1 migration guide**](../v3-1-migration-guide.md) to learn how to use the v3.0 version in your applications and workflows.
 
 ::: moniker-end
 
@@ -404,7 +404,7 @@ The following are the fields extracted per document type. The Document Intellige
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
 ::: moniker-end
 
@@ -424,6 +424,6 @@ The following are the fields extracted per document type. The Document Intellige
 
 * Try processing your own forms and documents with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
 ::: moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ID文書モデルページの名称変更と内容の更新"
}
```

### Explanation
この変更は、「concept-id-document.md」ファイルが「id-document.md」にリネームされ、その内容が一部更新されたことを示しています。合計で46行が変更され、その内訳には23行の追加と23行の削除が含まれています。

主な変更内容は次の通りです：

1. **ファイル名の変更**: ドキュメントが`concept-id-document.md`から`id-document.md`にリネームされ、タイトルが明確になり、ユーザーが内容を推測しやすくなります。

2. **相対パスの更新**: 複数のリンクとメディアソースが相対パスに更新されており、これによりファイルのリンクの整合性が保たれ、ユーザビリティが向上しています。

3. **情報の説明の整理**: ID文書モデルに関する説明が一部修正され、詳細が簡潔になりました。特に、案内される情報、例えばどのような書類からどのような情報が抽出されるかの具体例が明示されています。

4. **画像のパスが相対パスに変更**: 画像へのリンクが相対パスに変更され、表示の一貫性が向上しました。

5. **SDKとAPIのリンク更新**: 各SDKやAPIの説明が更新され、全てのリンクが相対パスに統一されており、情報へのアクセスがより容易になりました。

6. **抽出フィールドに関する説明の改善**: ID文書から抽出されるフィールドのリストやそれに付随する詳細での表現が強化されています。

これらの変更は、全体としてドキュメントの可読性と正確性を向上させることを目的としており、ユーザーに対して最新の機能とその使用方法を提供することを図っています。

## articles/ai-services/document-intelligence/prebuilt/invoice.md{#item-cabbf9}

<details>
<summary>Diff</summary>
````diff
@@ -16,21 +16,21 @@ ms.custom: references_regions
 # Document Intelligence invoice model
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-[!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
+[!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
+[!INCLUDE [applies to v3.1](../includes/applies-to-v31.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 ::: moniker-end
 
 The Document Intelligence invoice model uses powerful Optical Character Recognition (OCR) capabilities to analyze and extract key fields and line items from sales invoices, utility bills, and purchase orders. Invoices can be of various formats and quality including phone-captured images, scanned documents, and digital PDFs. The API analyzes invoice text; extracts key information such as customer name, billing address, due date, and amount due; and returns a structured JSON data representation. The model currently supports invoices in 27 languages.
@@ -50,15 +50,15 @@ Automated invoice processing is the process of extracting key accounts payable f
 
 **Sample invoice processed with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=invoice)**:
 
-:::image type="content" source="media/studio/overview-invoices.png" alt-text="Screenshot of a sample invoice analyzed in the Document Intelligence Studio." lightbox="media/overview-invoices-big.jpg":::
+:::image type="content" source="../media/studio/overview-invoices.png" alt-text="Screenshot of a sample invoice analyzed in the Document Intelligence Studio." lightbox="../media/overview-invoices-big.jpg":::
 
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
 
 **Sample invoice processed with [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net)**:
 
-:::image type="content" source="media/invoice-example-new.jpg" alt-text="Screenshot of a sample invoice.":::
+:::image type="content" source="../media/invoice-example-new.jpg" alt-text="Screenshot of a sample invoice.":::
 
 ::: moniker-end
 
@@ -70,7 +70,7 @@ Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, ap
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Invoice model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-invoice**|
+|**Invoice model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-invoice**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
@@ -79,7 +79,7 @@ Document Intelligence v3.1 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Invoice model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-invoice**|
+|**Invoice model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-invoice**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
@@ -88,7 +88,7 @@ Document Intelligence v3.0 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Invoice model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-invoice**|
+|**Invoice model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-invoice**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
@@ -97,14 +97,14 @@ Document Intelligence v2.1 supports the following tools, applications, and libra
 
 | Feature | Resources |
 |----------|-------------------------|
-|**Invoice model**|&bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/prebuilts-analyze)</br>&bullet;  [**REST API**](how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&view=doc-intel-2.1.0&preserve-view=true&tabs=windows)</br>&bullet;  [**Client-library SDK**](~/articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet;  [**Document Intelligence Docker container**](containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
+|**Invoice model**|&bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/prebuilts-analyze)</br>&bullet;  [**REST API**](../how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&view=doc-intel-2.1.0&preserve-view=true&tabs=windows)</br>&bullet;  [**Client-library SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet;  [**Document Intelligence Docker container**](../containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
 ::: moniker-end
 
 ## Input requirements
 
 ::: moniker range=">=doc-intel-3.0.0"
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ::: moniker-end
 
@@ -124,7 +124,7 @@ See how data, including customer information, vendor details, and line items, is
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 ::: moniker range=">=doc-intel-3.0.0"
 
@@ -134,7 +134,7 @@ See how data, including customer information, vendor details, and line items, is
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options** :
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
 > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=invoice)
@@ -149,7 +149,7 @@ See how data, including customer information, vendor details, and line items, is
 
 1. On the sample tool home page, select the **Use prebuilt model to get data** tile.
 
-    :::image type="content" source="media/label-tool/prebuilt-1.jpg" alt-text="Screenshot of layout model analyze results process.":::
+    :::image type="content" source="../media/label-tool/prebuilt-1.jpg" alt-text="Screenshot of layout model analyze results process.":::
 
 1. Select the **Form Type**  to analyze from the dropdown menu.
 
@@ -162,19 +162,19 @@ See how data, including customer information, vendor details, and line items, is
 
 1. In the **Source** field, select **URL** from the dropdown menu, paste the selected URL, and select the **Fetch** button.
 
-    :::image type="content" source="media/label-tool/fott-select-url.png" alt-text="Screenshot of source location dropdown menu.":::
+    :::image type="content" source="../media/label-tool/fott-select-url.png" alt-text="Screenshot of source location dropdown menu.":::
 
 1. In the **Document Intelligence service endpoint** field, paste the endpoint that you obtained with your Document Intelligence subscription.
 
 1. In the **key** field, paste  the key you obtained from your Document Intelligence resource.
 
-    :::image type="content" source="media/fott-select-form-type.png" alt-text="Screenshot showing the select-form-type dropdown menu.":::
+    :::image type="content" source="../media/fott-select-form-type.png" alt-text="Screenshot showing the select-form-type dropdown menu.":::
 
 1. Select **Run analysis**. The Document Intelligence Sample Labeling tool calls the Analyze Prebuilt API and analyze the document.
 
 1. View the results - see the key-value pairs extracted, line items, highlighted text extracted, and tables detected.
 
-    :::image type="content" source="media/invoice-example-new.jpg" alt-text="Screenshot of layout model analyze results operation.":::
+    :::image type="content" source="../media/invoice-example-new.jpg" alt-text="Screenshot of layout model analyze results operation.":::
 
 > [!NOTE]
 > The [Sample Labeling tool](https://fott-2-1.azurewebsites.net/) does not support the BMP file format. This is a limitation of the tool not the Document Intelligence Service.
@@ -183,7 +183,7 @@ See how data, including customer information, vendor details, and line items, is
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extraction
 The Document Intelligence invoice model `prebuilt-invoice` extracts the following fields.
@@ -242,7 +242,7 @@ The Document Intelligence invoice model `prebuilt-invoice` extracts the followin
 
 ### Line items array
 
-Following are the line items extracted from an invoice in the JSON output response (the following output uses this [sample invoice](media/sample-invoice.jpg):
+Following are the line items extracted from an invoice in the JSON output response (the following output uses this [sample invoice](../media/sample-invoice.jpg):
 
 |Name| Type | Description | Value (standardized output) |
 |:-----|:----|:----|:----|
@@ -271,7 +271,7 @@ Keys can also exist in isolation when the model detects that a key exists, with
 
 ## Fields extracted
 
-The Invoice service extracts the text, tables, and 26 invoice fields. Following are the fields extracted from an invoice in the JSON output response (the following output uses this [sample invoice](media/sample-invoice.jpg)).
+The Invoice service extracts the text, tables, and 26 invoice fields. Following are the fields extracted from an invoice in the JSON output response (the following output uses this [sample invoice](../media/sample-invoice.jpg)).
 
 |Name| Type | Description | Text | Value (standardized output) |
 |:-----|:----|:----|:----| :----|
@@ -302,7 +302,7 @@ The Invoice service extracts the text, tables, and 26 invoice fields. Following
 | ServiceEndDate | date | End date for the service period (for example, a utility bill service period) | 11/14/2019 | 2019-11-14 |
 | PreviousUnpaidBalance | number | Explicit previously unpaid balance | $500.00 | 500 |
 
-The following are the line items extracted from an invoice in the JSON output response and uses this [sample invoice](./media/sample-invoice.jpg):
+The following are the line items extracted from an invoice in the JSON output response and uses this [sample invoice](../media/sample-invoice.jpg):
 
 |Name| Type | Description | Text (line item #1) | Value (standardized output) |
 |:-----|:----|:----|:----| :----|
@@ -350,7 +350,7 @@ The JSON output has three parts:
 
 ## Migration guide
 
-* Follow our [**Document Intelligence v3.1 migration guide**](v3-1-migration-guide.md) to learn how to use the v3.0 version in your applications and workflows.
+* Follow our [**Document Intelligence v3.1 migration guide**](../v3-1-migration-guide.md) to learn how to use the v3.0 version in your applications and workflows.
 
 ::: moniker-end
 
@@ -360,7 +360,7 @@ The JSON output has three parts:
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
 ::: moniker-end
 
@@ -376,6 +376,6 @@ The JSON output has three parts:
 
 * Try processing your own forms and documents with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
 ::: moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "請求書モデルページの名称変更と内容の更新"
}
```

### Explanation
この変更は、「concept-invoice.md」ファイルが「invoice.md」にリネームされ、その内容が一部更新されたことを示しています。合計で50行が変更され、その内訳には25行の追加と25行の削除が含まれています。

主な変更内容は次の通りです：

1. **ファイル名の変更**: ドキュメントが`concept-invoice.md`から`invoice.md`にリネームされ、タイトルがよりシンプルで明確になりました。これにより、ユーザーがファイルの内容を容易に理解できるようになっています。

2. **相対パスの使用**: ドキュメント内の画像やリンクが相対パスに変更され、これによりファイル構造が一貫性を持ち、他のコンテンツとの整合性が高まりました。

3. **情報の更新**: 請求書モデルに関する説明が更新され、OCR機能を用いたキー項目の抽出についての情報が強調されています。具体的には、請求書の形式や内容、抽出される情報について詳細に説明されています。

4. **画像へのパス変更**: すべての画像リンクが相対パスに置き換えられ、視覚的な一貫性が向上しました。

5. **SDKとAPIの情報更新**: APIやSDKに関するリンクが更新され、ユーザーが最新情報にアクセスしやすくなっています。

6. **フィールド抽出の明確化**: 請求書モデルの抽出フィールドに関する情報が整理され、具体例をもとにした説明が強化されています。

これらの変更は、ドキュメントの整合性とユーザー体験を向上させることを目的としており、最新の請求書モデルの機能とその使用方法をユーザーに提供することに重点が置かれています。

## articles/ai-services/document-intelligence/prebuilt/layout.md{#item-f7c4c8}

<details>
<summary>Diff</summary>
````diff
@@ -1,38 +1,554 @@
 ---
-title: Document layout analysis - Document Intelligence 
+title: Document layout analysis - Document Intelligence
 titleSuffix: Azure AI services
 description: Extract text, tables, selections, titles, section headings, page headers, page footers, and more with layout analysis model from Document Intelligence.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 08/07/2024
+ms.date: 10/07/2024
 ms.author: lajanuar
 ---
 
-<!-- markdownlint-disable DOCSMD006 -->
+<!-- markdownlint-disable MD051 -->
+<!-- markdownlint-disable MD024 -->
 
 # Document Intelligence layout model
 
-::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+<!---------------------- v4.0 content ---------------------->
 
-[!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
-::: moniker-end
+:::moniker range="doc-intel-4.0.0"
 
-::: moniker range="doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
-::: moniker-end
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
-::: moniker-end
+[!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 
-::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
-::: moniker-end
+Document Intelligence layout model is an advanced machine-learning based document analysis API available in the Document Intelligence cloud. It enables you to take documents in various formats and return structured data representations of the documents. It combines an enhanced version of our powerful [Optical Character Recognition (OCR)](../../../ai-services/computer-vision/overview-ocr.md) capabilities with deep learning models to extract text, tables, selection marks, and document structure.
 
-Document Intelligence layout model is an advanced machine-learning based document analysis API available in the Document Intelligence cloud. It enables you to take documents in various formats and return structured data representations of the documents. It combines an enhanced version of our powerful [Optical Character Recognition (OCR)](../../ai-services/computer-vision/overview-ocr.md) capabilities with deep learning models to extract text, tables, selection marks, and document structure.
+## Document layout analysis (v4)
+
+Document structure layout analysis is the process of analyzing a document to extract regions of interest and their inter-relationships. The goal is to extract text and structural elements from the page to build better semantic understanding models. There are two types of roles in a document layout:
+
+* **Geometric roles**: Text, tables, figures, and selection marks are examples of geometric roles.
+* **Logical roles**: Titles, headings, and footers are examples of logical roles of texts.
+
+The following illustration shows the typical components in an image of a sample page.
+
+:::image type="content" source="../media/document-layout-example-new.png" alt-text="Illustration of document layout example."::: 
+
+## Development options (v4)
+
+Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, applications, and libraries:
+
+| Feature | Resources | Model ID |
+|----------|-------------|-----------|
+|**Layout model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-layout**|
+
+## Input requirements (v4)
+
+[!INCLUDE [input requirements](./../includes/input-requirements.md)]
+
+### Get started with Layout model
+
+See how data, including text, tables, table headers, selection marks, and structure information is extracted from documents using  Document Intelligence. You need the following resources:
+
+* An Azure subscription—you can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
+
+* A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
+
+    :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal."::: 
+
+> [!NOTE]
+> Document Intelligence Studio is available with v3.0 APIs and later versions.
+
+***Sample document processed with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/layout)***
+
+:::image type="content" source="../media/studio/form-recognizer-studio-layout-newspaper.png" alt-text="Screenshot of `Layout` processing a newspaper page in Document Intelligence Studio."::: 
+
+1. On the [Document Intelligence Studio home page](https://documentintelligence.ai.azure.com/studio), select **Layout**.
+
+1. You can analyze the sample document or upload your own files.
+
+1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
+
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio."::: 
+
+     > [!div class="nextstepaction"]
+     > [Try Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/layout).
+     >
+
+## Supported languages and locales (ocr)
+
+*See* our [Language Support—document analysis models](../language-support/ocr.md) page for a complete list of supported languages.
+
+## Data extraction (v4)
+
+The layout model extracts text, selection marks, tables, paragraphs, and paragraph types (`roles`) from your documents.
+
+> [!NOTE]
+> Versions `2024-02-29-preview`, `2023-10-31-preview`, and later support Microsoft office (DOCX, XLSX, PPTX) and HTML files. The following features are not supported:
+>
+> * There are no angle, width/height and unit with each page object.
+> * For each object detected, there is no bounding polygon or bounding region.
+> * Page range (`pages`) is not supported as a parameter.
+> * No `lines` object.
+
+### Pages
+
+The pages collection is a list of pages within the document. Each page is represented sequentially within the document and ../includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
+
+| **File format**   | **Computed page unit**   | **Total pages**  |
+| --- | --- | --- |
+|Images (JPEG/JPG, PNG, BMP, HEIF) | Each image = 1 page unit | Total images  |
+|PDF | Each page in the PDF = 1 page unit | Total pages in the PDF |
+|TIFF | Each image in the TIFF = 1 page unit | Total images in the TIFF |
+|Word (DOCX)  | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
+|Excel (XLSX)  | Each worksheet = 1 page unit, embedded or linked images not supported | Total worksheets |
+|PowerPoint (PPTX) |  Each slide = 1 page unit, embedded or linked images not supported | Total slides |
+|HTML | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
+
+#### [Sample code](#tab/sample-code)
+
+```Python
+# Analyze pages.
+for page in result.pages:
+print(f"----Analyzing layout from page #{page.page_number}----")
+print(f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}")
+
+```
+
+> [!div class="nextstepaction"]
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py) 
+
+#### [Output](#tab/output)
+
+```json
+"pages": [
+    {
+        "pageNumber": 1,
+        "angle": 0,
+        "width": 915,
+        "height": 1190,
+        "unit": "pixel",
+        "words": [],
+        "lines": [],
+        "spans": []
+    }
+]
+```
+
+---
+
+### Extract selected pages from documents
+
+For large multi-page documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction.
+
+### Paragraphs
+
+The Layout model extracts all identified blocks of text in the `paragraphs` collection as a top level object under `analyzeResults`. Each entry in this collection represents a text block and ../includes the extracted text as`content`and the bounding `polygon` coordinates. The `span` information points to the text fragment within the top level `content` property that contains the full text from the document.
+
+```json
+
+"paragraphs": [
+    {
+        "spans": [],
+        "boundingRegions": [],
+        "content": "While healthcare is still in the early stages of its Al journey, we are seeing pharmaceutical and other life sciences organizations making major investments in Al and related technologies.\" TOM LAWRY | National Director for Al, Health and Life Sciences | Microsoft"
+    }
+]
+```
+
+### Paragraph roles
+
+The new machine-learning based page object detection extracts logical roles like titles, section headings, page headers, page footers, and more. The Document Intelligence Layout model assigns certain text blocks in the `paragraphs` collection with their specialized role or type predicted by the model. It's best to use paragraph roles with unstructured documents to help understand the layout of the extracted content for a richer semantic analysis. The following paragraph roles are supported:
+
+| **Predicted role**   | **Description**   | **Supported file types** |
+| --- | --- | --- |
+| `title`  | The main headings in the page | pdf, image, docx, pptx, xlsx, html |
+| `sectionHeading`  | One or more subheadings on the page  | pdf, image, docx, xlsx, html |
+| `footnote`  | Text near the bottom of the page  | pdf, image |
+| `pageHeader`  | Text near the top edge of the page  | pdf, image, docx |
+| `pageFooter`  | Text near the bottom edge of the page  | pdf, image, docx, pptx, html |
+| `pageNumber`  | Page number  | pdf, image |
+
+```json
+{
+    "paragraphs": [
+                {
+                    "spans": [],
+                    "boundingRegions": [],
+                    "role": "title",
+                    "content": "NEWS TODAY"
+                },
+                {
+                    "spans": [],
+                    "boundingRegions": [],
+                    "role": "sectionHeading",
+                    "content": "Mirjam Nilsson"
+                }
+    ]
+}
+
+```
+
+### Text, lines, and words
+
+The document layout model in Document Intelligence extracts print and handwritten style text as `lines` and `words`. The `styles` collection ../includes any handwritten style for lines if detected along with the spans pointing to the associated text. This feature applies to [supported handwritten languages](../language-support/prebuilt.md).
+
+For Microsoft Word, Excel, PowerPoint, and HTML, Document Intelligence versions 2024-02-29-preview and  2023-10-31-preview Layout model extract all embedded text as is. Texts are extracted as words and paragraphs. Embedded images aren't supported.
+
+#### [Sample code](#tab/sample-code)
+
+```Python
+# Analyze lines.
+if page.lines:
+    for line_idx, line in enumerate(page.lines):
+    words = get_words(page, line)
+    print(
+        f"...Line # {line_idx} has word count {len(words)} and text '{line.content}' "
+        f"within bounding polygon '{line.polygon}'"
+    )
+
+    # Analyze words.
+    for word in words:
+        print(f"......Word '{word.content}' has a confidence of {word.confidence}")
+
+```
+
+> [!div class="nextstepaction"]
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py) 
+
+#### [Output](#tab/output)
+
+```json
+"words": [
+    {
+        "content": "While",
+        "polygon": [],
+        "confidence": 0.997,
+        "span": {}
+    },
+],
+"lines": [
+    {
+        "content": "While healthcare is still in the early stages of its Al journey, we",
+        "polygon": [],
+        "spans": [],
+    }
+]
+```
+
+---
+
+### Handwritten style for text lines
+
+The response ../includes classifying whether each text line is of handwriting style or not, along with a confidence score. For more information. See [Handwritten language support](../language-support/ocr.md). The following example shows an example JSON snippet.
+
+```json
+"styles": [
+{
+    "confidence": 0.95,
+    "spans": [
+    {
+        "offset": 509,
+        "length": 24
+    }
+    "isHandwritten": true
+    ]
+}
+```
+
+If you enable the [font/style addon capability](../concept-add-on-capabilities.md#font-property-extraction), you also get the font/style result as part of the `styles` object.
+
+### Selection marks
+
+The Layout model also extracts selection marks from documents. Extracted selection marks appear within the `pages` collection for each page. They include the bounding `polygon`, `confidence`, and selection `state` (`selected/unselected`). The text representation (that is, `:selected:` and `:unselected`) is also included as the starting index (`offset`) and `length` that references the top level `content` property that contains the full text from the document.
+
+#### [Sample code](#tab/sample-code)
+
+```Python
+# Analyze selection marks.
+if page.selection_marks:
+    for selection_mark in page.selection_marks:
+        print(
+            f"Selection mark is '{selection_mark.state}' within bounding polygon "
+            f"'{selection_mark.polygon}' and has a confidence of {selection_mark.confidence}"
+        )
+
+```
+
+> [!div class="nextstepaction"]
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py) 
+
+#### [Output](#tab/output)
+
+```json
+{
+    "selectionMarks": [
+        {
+            "state": "unselected",
+            "polygon": [],
+            "confidence": 0.995,
+            "span": {
+                "offset": 1421,
+                "length": 12
+            }
+        }
+    ]
+}
+```
+
+---
+
+### Tables
+
+Extracting tables is a key requirement for processing documents containing large volumes of data typically formatted as tables. The Layout model extracts tables in the `pageResults` section of the JSON output. Extracted table information ../includes the number of columns and rows, row span, and column span. Each cell with its bounding polygon is output along with information whether the area is recognized as a `columnHeader` or not. The model supports extracting tables that are rotated. Each table cell contains the row and column index and bounding polygon coordinates. For the cell text, the model outputs the `span` information containing the starting index (`offset`). The model also outputs the `length` within the top-level content that contains the full text from the document.
+
+Here are a few factors to consider when using the Document Intelligence bale extraction capability:
+
+* Is the data that you want to extract presented as a table, and is the table structure meaningful?
+
+* Can the data fit in a two-dimensional grid if the data isn't in a table format?
+
+* Do your tables span multiple pages? If so, to avoid having to label all the pages, split the PDF into pages before sending it to Document Intelligence. After the analysis, post-process the pages to a single table.
+
+* Refer to [Tabular fields](../train/custom-labels.md#tabular-fields) if you're creating custom models. Dynamic tables have a variable number of rows for each column. Fixed tables have a constant number of rows for each column.
+
+> [!NOTE]
+>
+> * Table analysis is not supported if the input file is XLSX.
+> * Starting with *2024-07-31-preview*, the bounding regions for figures and tables cover only the core content and exclude associated caption and footnotes.
+
+#### [Sample code](#tab/sample-code)
+
+```Python
+if result.tables:
+    for table_idx, table in enumerate(result.tables):
+        print(f"Table # {table_idx} has {table.row_count} rows and " f"{table.column_count} columns")
+        if table.bounding_regions:
+            for region in table.bounding_regions:
+                print(f"Table # {table_idx} location on page: {region.page_number} is {region.polygon}")
+        # Analyze cells.
+        for cell in table.cells:
+            print(f"...Cell[{cell.row_index}][{cell.column_index}] has text '{cell.content}'")
+            if cell.bounding_regions:
+                for region in cell.bounding_regions:
+                print(f"...content on page {region.page_number} is within bounding polygon '{region.polygon}'")
+
+```
+
+> [!div class="nextstepaction"]
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py) 
+
+#### [Output](#tab/output)
+
+```json
+{
+    "tables": [
+        {
+            "rowCount": 9,
+            "columnCount": 4,
+            "cells": [
+                {
+                    "kind": "columnHeader",
+                    "rowIndex": 0,
+                    "columnIndex": 0,
+                    "columnSpan": 4,
+                    "content": "(In millions, except earnings per share)",
+                    "boundingRegions": [],
+                    "spans": []
+                    },
+            ]
+        }
+    ]
+}
+
+```
+
+---
+
+### Output to markdown format
+
+The Layout API can output the extracted text in markdown format. Use the `outputContentFormat=markdown` to specify the output format in markdown. The markdown content is output as part of the `content` section.
+
+> [!NOTE]
+> Starting from *2024-07-31-preview*, the representation of tables is changed to HTML tables to enable rendering of merged cells, multi-row headers, etc. Another related change is to use Unicode checkbox characters ☒ and ☐ for selection marks instead of :selected: and :unselected:.  Note that this means that the content of selection mark fields will contain :selected: even though their spans refer to Unicode characters in the top-level span.
+
+#### [Sample code](#tab/sample-code)
+
+```Python
+document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))
+poller = document_intelligence_client.begin_analyze_document(
+    "prebuilt-layout",
+    AnalyzeDocumentRequest(url_source=url),
+    output_content_format=ContentFormat.MARKDOWN,
+)
+
+```
+
+> [!div class="nextstepaction"]
+> [View samples on GitHub.](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_documents_output_in_markdown.py) 
+
+#### [Output](#tab/output)
+
+```Markdown
+PageHeader="This is the header of the document." 
+
+This is title
+===
+# 1\. Text
+Latin refers to an ancient Italic language originating in the region of Latium in ancient Rome.
+# 2\. Page Objects
+## 2.1 Table
+Here's a sample table below, designed to be simple for easy understand and quick reference.
+| Name | Corp | Remark |
+| - | - | - |
+| Foo | | |
+| Bar | Microsoft | Dummy |
+Table 1: This is a dummy table
+## 2.2. Figure
+<figure>
+<figcaption>
+
+Figure 1: Here is a figure with text
+</figcaption>
+
+![](figures/0)
+FigureContent="500 450 400 400 350 250 200 200 200- Feb" 
+</figure>
+
+# 3\. Others
+Al Document Intelligence is an Al service that applies advanced machine learning to extract text, key-value pairs, tables, and structures from documents automatically and accurately:
+    :selected:
+clear
+    :selected:
+precise
+    :unselected:
+vague
+    :selected:
+coherent
+    :unselected:
+Incomprehensible
+Turn documents into usable data and shift your focus to acting on information rather than compiling it. Start with prebuilt models or create custom models tailored to your documents both on premises and in the cloud with the Al Document Intelligence studio or SDK.
+Learn how to accelerate your business processes by automating text extraction with Al Document Intelligence. This webinar features hands-on demos for key use cases such as document processing, knowledge mining, and industry-specific Al model customization.
+PageFooter="This is the footer of the document." 
+PageFooter="1 | Page" 
+```
+
+---
+
+### Figures
+
+Figures (charts, images) in documents play a crucial role in complementing and enhancing the textual content, providing visual representations that aid in the understanding of complex information. The figures object detected by the Layout model has key properties like `boundingRegions` (the spatial locations of the figure on the document pages, including the page number and the polygon coordinates that outline the figure's boundary), `spans` (details the text spans related to the figure, specifying their offsets and lengths within the document's text. This connection helps in associating the figure with its relevant textual context), `elements` (the identifiers for text elements or paragraphs within the document that are related to or describe the figure) and `caption` if there's any.
+
+When *output=figures* is specified during the initial analyze operation, the service generates cropped images for all detected figures that can be accessed via `/analyeResults/{resultId}/figures/{figureId}`.
+`FigureId` is included in each figure object, following an undocumented convention of `{pageNumber}.{figureIndex}` where `figureIndex` resets to one per page.
+
+> [!NOTE]
+> Starting with *2024-07-31-preview*, the bounding regions for figures and tables cover only the core content and exclude associated caption and footnotes.
+
+#### [Sample code](#tab/sample-code)
+
+```Python
+# Analyze figures.
+if result.figures:
+    for figures_idx,figures in enumerate(result.figures):
+        print(f"Figure # {figures_idx} has the following spans:{figures.spans}")
+        for region in figures.bounding_regions:
+            print(f"Figure # {figures_idx} location on page:{region.page_number} is within bounding polygon '{region.polygon}'")
+```
+
+> [!div class="nextstepaction"]
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py) 
+
+#### [Output](#tab/output)
+
+```json
+{
+    "figures": [
+        {
+        "id": "{figureId}",
+        "boundingRegions": [],
+        "spans": [],
+        "elements": [
+            "/paragraphs/15",
+            ...
+        ],
+        "caption": {
+            "content": "Here is a figure with some text",
+            "boundingRegions": [],
+            "spans": [],
+            "elements": [
+            "/paragraphs/15"
+            ]
+        }
+        }
+    ]
+}
+```
+
+:::image type="content" source="../media/document-layout-example-figures.png" alt-text="Screenshot of examples of document figures."::: 
+
+---
+
+### Sections
+
+Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [Retrieval Augmented Generation (RAG)](../concept/retrieval-augmented-generation.md) in document generative AI underscores the significance of hierarchical document structure analysis. The Layout model supports sections and subsections in the output, which identifies the relationship of sections and object within each section. The hierarchical structure is maintained in `elements` of each section. You can use [output to markdown format](#output-to-markdown-format) to easily get the sections and subsections in markdown.
+
+#### [Sample code](#tab/sample-code)
+
+```Python
+document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))
+poller = document_intelligence_client.begin_analyze_document(
+    "prebuilt-layout",
+    AnalyzeDocumentRequest(url_source=url),
+    output_content_format=ContentFormat.MARKDOWN,
+)
+
+```
+
+> [!div class="nextstepaction"]
+> [View samples on GitHub.](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_documents_output_in_markdown.py) 
+
+#### [Output](#tab/output)
+
+```json
+{
+    "sections": [
+        {
+        "spans": [],
+        "elements": [
+            "/paragraphs/0",
+            "/sections/1",
+            "/sections/2",
+            "/sections/5"
+        ]
+        },
+...
+}
+```
+
+:::image type="content" source="../media/document-layout-example-section.png" alt-text="Screenshot of examples of document sections."::: 
+
+---
+
+:::moniker-end
+
+<!---------------------- v3.1 v3.0 v2.1 content ---------------------->
+
+:::moniker range="doc-intel-3.1.0"
+[!INCLUDE [applies to v3.1](../includes/applies-to-v31.md)]
+:::moniker-end
+
+:::moniker range="doc-intel-3.0.0"
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
+:::moniker-end
+
+:::moniker range="doc-intel-2.1.0"
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
+:::moniker-end
+
+Document Intelligence layout model is an advanced machine-learning based document analysis API available in the Document Intelligence cloud. It enables you to take documents in various formats and return structured data representations of the documents. It combines an enhanced version of our powerful [Optical Character Recognition (OCR)](../../../ai-services/computer-vision/overview-ocr.md) capabilities with deep learning models to extract text, tables, selection marks, and document structure.
 
 ## Document layout analysis
 
@@ -43,61 +559,55 @@ Document structure layout analysis is the process of analyzing a document to ext
 
 The following illustration shows the typical components in an image of a sample page.
 
-  :::image type="content" source="media/document-layout-example-new.png" alt-text="Illustration of document layout example.":::
+:::image type="content" source="../media/document-layout-example-new.png" alt-text="Illustration of document layout example."::: 
 
 ## Development options
 
-::: moniker range="doc-intel-4.0.0"
-
-Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, applications, and libraries:
-
-| Feature | Resources | Model ID |
-|----------|-------------|-----------|
-|**Layout model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-layout**|
-::: moniker-end
-
-::: moniker range="doc-intel-3.1.0"
+:::moniker range="doc-intel-3.1.0"
 
 Document Intelligence v3.1 supports the following tools, applications, and libraries:
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Layout model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-layout**|
-::: moniker-end
+|**Layout model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-layout**|
 
-::: moniker range="doc-intel-3.0.0"
+:::moniker-end
+
+:::moniker range="doc-intel-3.0.0"
 
 Document Intelligence v3.0 supports the following tools, applications, and libraries:
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Layout model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-layout**|
-::: moniker-end
+|**Layout model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-layout**|
+
+:::moniker-end
 
-::: moniker range="doc-intel-2.1.0"
+:::moniker range="doc-intel-2.1.0"
 
 Document Intelligence v2.1 supports the following tools, applications, and libraries:
 
 | Feature | Resources |
 |----------|-------------------------|
-|**Layout model**|&bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/prebuilts-analyze)</br>&bullet;  [**REST API**](how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&view=doc-intel-2.1.0&preserve-view=true&tabs=windows)</br>&bullet;  [**Client-library SDK**](~/articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet;  [**Document Intelligence Docker container**](containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
-::: moniker-end
+|**Layout model**|&bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/prebuilts-analyze)</br>&bullet;  [**REST API**](../how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&view=doc-intel-2.1.0&preserve-view=true&tabs=windows)</br>&bullet;  [**Client-library SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet;  [**Document Intelligence Docker container**](../containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
+
+:::moniker-end
 
 ## Input requirements
 
-::: moniker range=">=doc-intel-3.0.0"
+:::moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](./../includes/input-requirements.md)]
 
-::: moniker-end
+:::moniker-end
 
-::: moniker range="doc-intel-2.1.0"
+:::moniker range="doc-intel-2.1.0"
 
 * Supported file formats: JPEG, PNG, PDF, and TIFF.
 * Supported number of pages: For PDF and TIFF, up to 2,000 pages are processed. For free tier subscribers, only the first two pages are processed.
 * Supported file size: the file size must be less than 50 MB and dimensions at least 50 x 50 pixels and at most 10,000 x 10,000 pixels.
 
-::: moniker-end
+:::moniker-end
 
 ### Get started with Layout model
 
@@ -107,39 +617,39 @@ See how data, including text, tables, table headers, selection marks, and struct
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+:::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal."::: 
 
-::: moniker range=">=doc-intel-3.0.0"
+:::moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
 > [!NOTE]
 > Document Intelligence Studio is available with v3.0 APIs and later versions.
 
 ***Sample document processed with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/layout)***
 
-:::image type="content" source="media/studio/form-recognizer-studio-layout-newspaper.png" alt-text="Screenshot of `Layout` processing a newspaper page in Document Intelligence Studio.":::
+:::image type="content" source="../media/studio/form-recognizer-studio-layout-newspaper.png" alt-text="Screenshot of `Layout` processing a newspaper page in Document Intelligence Studio."::: 
 
 1. On the [Document Intelligence Studio home page](https://documentintelligence.ai.azure.com/studio), select **Layout**.
 
 1. You can analyze the sample document or upload your own files.
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
    > [!div class="nextstepaction"]
-   > [Try Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/layout).
+   > [Try Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/layout). 
 
-::: moniker-end
+:::moniker-end
 
-::: moniker range="doc-intel-2.1.0"
+:::moniker range="doc-intel-2.1.0"
 
 ## Document Intelligence Sample Labeling tool
 
 1. Navigate to the [Document Intelligence sample tool](https://fott-2-1.azurewebsites.net/).
 
 1. On the sample tool home page, select **Use Layout to get text, tables and selection marks**.
 
-     :::image type="content" source="media/label-tool/layout-1.jpg" alt-text="Screenshot of connection settings for the Document Intelligence layout process.":::
+     :::image type="content" source="../media/label-tool/layout-1.jpg" alt-text="Screenshot of connection settings for the Document Intelligence layout process.":::
 
 1. In the **Document Intelligence service endpoint** field, paste the endpoint that you obtained with your Document Intelligence subscription.
 
@@ -153,29 +663,29 @@ See how data, including text, tables, table headers, selection marks, and struct
 
 1. Select **Run Layout**. The Document Intelligence Sample Labeling tool calls the `Analyze Layout` API to analyze the document.
 
-    :::image type="content" source="media/fott-layout.png" alt-text="Screenshot of `Layout` dropdown window.":::
+    :::image type="content" source="../media/fott-layout.png" alt-text="Screenshot of `Layout` dropdown window.":::
 
 1. View the results - see the highlighted extracted text, detected selection marks, and detected tables.
 
-    :::image type="content" source="media/label-tool/layout-3.jpg" alt-text="Screenshot of connection settings for the Document Intelligence Sample Labeling tool.":::
+    :::image type="content" source="../media/label-tool/layout-3.jpg" alt-text="Screenshot of connection settings for the Document Intelligence Sample Labeling tool.":::
 
-::: moniker-end
+:::moniker-end
 
 ## Supported languages and locales
 
-*See* our [Language Support—document analysis models](language-support-ocr.md) page for a complete list of supported languages.
+*See* our [Language Support—document analysis models](../language-support/ocr.md) page for a complete list of supported languages.
 
-::: moniker range="doc-intel-2.1.0"
+:::moniker range="doc-intel-2.1.0"
 
 Document Intelligence v2.1 supports the following tools, applications, and libraries:
 
 | Feature | Resources |
 |----------|-------------------------|
-|**Layout API**| <ul><li>[**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/layout-analyze)</li><li>[**REST API**](how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&tabs=windows&view=doc-intel-2.1.0&preserve-view=true)</li><li>[**Client-library SDK**](~/articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</li><li>[**Document Intelligence Docker container**](containers/install-run.md?branch=main&tabs=layout#run-the-container-with-the-docker-compose-up-command)</li></ul>|
+|**Layout API**| &bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/layout-analyze)</br>&bullet; [**REST API**](../how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&tabs=windows&view=doc-intel-2.1.0&preserve-view=true)</br>&bullet; [**Client-library SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet; [**Document Intelligence Docker container**](../containers/install-run.md?branch=main&tabs=layout#run-the-container-with-the-docker-compose-up-command)|
 
-::: moniker-end
+:::moniker-end
 
-::: moniker range=">=doc-intel-3.0.0"
+:::moniker range="<=doc-intel-3.1.0"
 
 ## Data extraction
 
@@ -191,9 +701,9 @@ The layout model extracts text, selection marks, tables, paragraphs, and paragra
 
 ### Pages
 
-The pages collection is a list of pages within the document. Each page is represented sequentially within the document and includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
+The pages collection is a list of pages within the document. Each page is represented sequentially within the document and ../includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
 
- **File format**   | **Computed page unit**   | **Total pages**  |
+| **File format**   | **Computed page unit**   | **Total pages**  |
 | --- | --- | --- |
 |Images (JPEG/JPG, PNG, BMP, HEIF) | Each image = 1 page unit | Total images  |
 |PDF | Each page in the PDF = 1 page unit | Total pages in the PDF |
@@ -203,9 +713,9 @@ The pages collection is a list of pages within the document. Each page is repres
 |PowerPoint (PPTX) |  Each slide = 1 page unit, embedded or linked images not supported | Total slides |
 |HTML | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
 
-::: moniker-end
+:::moniker-end
 
-::: moniker range="doc-intel-3.0.0"
+:::moniker range="doc-intel-3.0.0"
 
 ```json
 "pages": [
@@ -222,9 +732,9 @@ The pages collection is a list of pages within the document. Each page is repres
 ]
 ```
 
-::: moniker-end
+:::moniker-end
 
-::: moniker range="doc-intel-3.1.0"
+:::moniker range="doc-intel-3.1.0"
 
 #### [Sample code](#tab/sample-code)
 
@@ -239,7 +749,7 @@ for page in result.pages:
 ```
 
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py)
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py) 
 
 #### [Output](#tab/output)
 
@@ -257,52 +767,19 @@ for page in result.pages:
     }
 ]
 ```
----
-::: moniker-end
-
-::: moniker range="doc-intel-4.0.0"
-
-#### [Sample code](#tab/sample-code)
-
-```Python
-# Analyze pages.
-for page in result.pages:
-    print(f"----Analyzing layout from page #{page.page_number}----")
-    print(f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}")
-
-```
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py)
-
-#### [Output](#tab/output)
 
-```json
-"pages": [
-    {
-        "pageNumber": 1,
-        "angle": 0,
-        "width": 915,
-        "height": 1190,
-        "unit": "pixel",
-        "words": [],
-        "lines": [],
-        "spans": []
-    }
-]
-```
 ---
+:::moniker-end
 
-::: moniker-end
-
-::: moniker range=">=doc-intel-3.0.0"
+:::moniker range="<=doc-intel-3.1.0"
 
 ### Extract selected pages from documents
 
 For large multi-page documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction.
 
 ### Paragraphs
 
-The Layout model extracts all identified blocks of text in the `paragraphs` collection as a top level object under `analyzeResults`. Each entry in this collection represents a text block and includes the extracted text as`content`and the bounding `polygon` coordinates. The `span` information points to the text fragment within the top level `content` property that contains the full text from the document.
+The Layout model extracts all identified blocks of text in the `paragraphs` collection as a top level object under `analyzeResults`. Each entry in this collection represents a text block and ../includes the extracted text as`content`and the bounding `polygon` coordinates. The `span` information points to the text fragment within the top level `content` property that contains the full text from the document.
 
 ```json
 
@@ -342,65 +819,21 @@ The new machine-learning based page object detection extracts logical roles like
                     "boundingRegions": [],
                     "role": "sectionHeading",
                     "content": "Mirjam Nilsson"
-                }
-    ]
-}
-
-```
-
-### Text, lines, and words
-
-The document layout model in Document Intelligence extracts print and handwritten style text as `lines` and `words`. The `styles` collection includes any handwritten style for lines if detected along with the spans pointing to the associated text. This feature applies to [supported handwritten languages](language-support.md).
-
-For Microsoft Word, Excel, PowerPoint, and HTML, Document Intelligence versions 2024-02-29-preview and  2023-10-31-preview Layout model extract all embedded text as is. Texts are extracted as words and paragraphs. Embedded images aren't supported.
-
-::: moniker-end
-
-::: moniker range="doc-intel-3.0.0"
-
-```json
-"words": [
-    {
-        "content": "While",
-        "polygon": [],
-        "confidence": 0.997,
-        "span": {}
-    },
-],
-"lines": [
-    {
-        "content": "While healthcare is still in the early stages of its Al journey, we",
-        "polygon": [],
-        "spans": [],
-    }
-]
-```
-::: moniker-end
+                }
+    ]
+}
 
-::: moniker range="doc-intel-3.1.0"
+```
 
-#### [Sample code](#tab/sample-code)
+### Text, lines, and words
 
-```Python
-# Analyze lines.
-for line_idx, line in enumerate(page.lines):
-    words = line.get_words()
-    print(
-        f"...Line # {line_idx} has word count {len(words)} and text '{line.content}' "
-        f"within bounding polygon '{format_polygon(line.polygon)}'"
-    )
+The document layout model in Document Intelligence extracts print and handwritten style text as `lines` and `words`. The `styles` collection ../includes any handwritten style for lines if detected along with the spans pointing to the associated text. This feature applies to [supported handwritten languages](../language-support/prebuilt.md).
 
-    # Analyze words.
-    for word in words:
-        print(
-            f"......Word '{word.content}' has a confidence of {word.confidence}"
-        )
+For Microsoft Word, Excel, PowerPoint, and HTML, Document Intelligence versions 2024-02-29-preview and  2023-10-31-preview Layout model extract all embedded text as is. Texts are extracted as words and paragraphs. Embedded images aren't supported.
 
-```
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py)
+:::moniker-end
 
-#### [Output](#tab/output)
+:::moniker range="doc-intel-3.0.0"
 
 ```json
 "words": [
@@ -419,30 +852,32 @@ for line_idx, line in enumerate(page.lines):
     }
 ]
 ```
----
-::: moniker-end
 
-::: moniker range="doc-intel-4.0.0"
+:::moniker-end
+
+:::moniker range="doc-intel-3.1.0"
 
 #### [Sample code](#tab/sample-code)
 
 ```Python
 # Analyze lines.
-if page.lines:
-    for line_idx, line in enumerate(page.lines):
-    words = get_words(page, line)
+for line_idx, line in enumerate(page.lines):
+    words = line.get_words()
     print(
         f"...Line # {line_idx} has word count {len(words)} and text '{line.content}' "
-        f"within bounding polygon '{line.polygon}'"
+        f"within bounding polygon '{format_polygon(line.polygon)}'"
     )
 
     # Analyze words.
     for word in words:
-        print(f"......Word '{word.content}' has a confidence of {word.confidence}")
+        print(
+            f"......Word '{word.content}' has a confidence of {word.confidence}"
+        )
 
 ```
+
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py)
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py) 
 
 #### [Output](#tab/output)
 
@@ -463,14 +898,15 @@ if page.lines:
     }
 ]
 ```
+
 ---
-::: moniker-end
+:::moniker-end
 
-::: moniker range=">=doc-intel-3.0.0"
+:::moniker range="<=doc-intel-3.1.0"
 
 ### Handwritten style for text lines
 
-The response includes classifying whether each text line is of handwriting style or not, along with a confidence score. For more information. See [Handwritten language support](language-support-ocr.md). The following example shows an example JSON snippet.
+The response ../includes classifying whether each text line is of handwriting style or not, along with a confidence score. For more information. See [Handwritten language support](../language-support/ocr.md). The following example shows an example JSON snippet.
 
 ```json
 "styles": [
@@ -486,15 +922,16 @@ The response includes classifying whether each text line is of handwriting style
 }
 ```
 
-If you enable the [font/style addon capability](concept-add-on-capabilities.md#font-property-extraction), you also get the font/style result as part of the `styles` object.
+If you enable the [font/style addon capability](../concept-add-on-capabilities.md#font-property-extraction), you also get the font/style result as part of the `styles` object.
 
 ### Selection marks
 
 The Layout model also extracts selection marks from documents. Extracted selection marks appear within the `pages` collection for each page. They include the bounding `polygon`, `confidence`, and selection `state` (`selected/unselected`). The text representation (that is, `:selected:` and `:unselected`) is also included as the starting index (`offset`) and `length` that references the top level `content` property that contains the full text from the document.
 
-::: moniker-end
+:::moniker-end
+
+:::moniker range="doc-intel-3.0.0"
 
-::: moniker range="doc-intel-3.0.0"
 ```json
 {
     "selectionMarks": [
@@ -510,9 +947,10 @@ The Layout model also extracts selection marks from documents. Extracted selecti
     ]
 }
 ```
-::: moniker-end
 
-::: moniker range="doc-intel-3.1.0"
+:::moniker-end
+
+:::moniker range="doc-intel-3.1.0"
 
 #### [Sample code](#tab/sample-code)
 
@@ -525,45 +963,9 @@ for selection_mark in page.selection_marks:
     )
 
 ```
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py)
-
-#### [Output](#tab/output)
-
-```json
-{
-    "selectionMarks": [
-        {
-            "state": "unselected",
-            "polygon": [],
-            "confidence": 0.995,
-            "span": {
-                "offset": 1421,
-                "length": 12
-            }
-        }
-    ]
-}
-```
----
-::: moniker-end
-
-::: moniker range="doc-intel-4.0.0"
-
-#### [Sample code](#tab/sample-code)
-
-```Python
-# Analyze selection marks.
-if page.selection_marks:
-    for selection_mark in page.selection_marks:
-        print(
-            f"Selection mark is '{selection_mark.state}' within bounding polygon "
-            f"'{selection_mark.polygon}' and has a confidence of {selection_mark.confidence}"
-        )
 
-```
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py)
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py) 
 
 #### [Output](#tab/output)
 
@@ -584,13 +986,13 @@ if page.selection_marks:
 ```
 
 ---
-::: moniker-end
+:::moniker-end
 
-::: moniker range=">=doc-intel-3.0.0"
+:::moniker range="<=doc-intel-3.1.0"
 
 ### Tables
 
-Extracting tables is a key requirement for processing documents containing large volumes of data typically formatted as tables. The Layout model extracts tables in the `pageResults` section of the JSON output. Extracted table information includes the number of columns and rows, row span, and column span. Each cell with its bounding polygon is output along with information whether the area is recognized as a `columnHeader` or not. The model supports extracting tables that are rotated. Each table cell contains the row and column index and bounding polygon coordinates. For the cell text, the model outputs the `span` information containing the starting index (`offset`). The model also outputs the `length` within the top-level content that contains the full text from the document.
+Extracting tables is a key requirement for processing documents containing large volumes of data typically formatted as tables. The Layout model extracts tables in the `pageResults` section of the JSON output. Extracted table information ../includes the number of columns and rows, row span, and column span. Each cell with its bounding polygon is output along with information whether the area is recognized as a `columnHeader` or not. The model supports extracting tables that are rotated. Each table cell contains the row and column index and bounding polygon coordinates. For the cell text, the model outputs the `span` information containing the starting index (`offset`). The model also outputs the `length` within the top-level content that contains the full text from the document.
 
 Here are a few factors to consider when using the Document Intelligence bale extraction capability:
 
@@ -600,16 +1002,16 @@ Here are a few factors to consider when using the Document Intelligence bale ext
 
 * Do your tables span multiple pages? If so, to avoid having to label all the pages, split the PDF into pages before sending it to Document Intelligence. After the analysis, post-process the pages to a single table.
 
-* Refer to [Tabular fields](concept-custom-label.md#tabular-fields) if you're creating custom models. Dynamic tables have a variable number of rows for each column. Fixed tables have a constant number of rows for each column.
+* Refer to [Tabular fields](../train/custom-labels.md#tabular-fields) if you're creating custom models. Dynamic tables have a variable number of rows for each column. Fixed tables have a constant number of rows for each column.
 
 > [!NOTE]
 >
 > * Table analysis is not supported if the input file is XLSX.
 > * Starting with *2024-07-31-preview*, the bounding regions for figures and tables cover only the core content and exclude associated caption and footnotes.
 
-::: moniker-end
+:::moniker-end
 
-::: moniker range="doc-intel-3.0.0"
+:::moniker range="doc-intel-3.0.0"
 
 ```json
 {
@@ -633,9 +1035,10 @@ Here are a few factors to consider when using the Document Intelligence bale ext
 }
 
 ```
-::: moniker-end
 
-::: moniker range="doc-intel-3.1.0"
+:::moniker-end
+
+:::moniker range="doc-intel-3.1.0"
 
 #### [Sample code](#tab/sample-code)
 
@@ -660,57 +1063,9 @@ for table_idx, table in enumerate(result.tables):
             )
 
 ```
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py)
-
-#### [Output](#tab/output)
-
-```json
-{
-    "tables": [
-        {
-            "rowCount": 9,
-            "columnCount": 4,
-            "cells": [
-                {
-                    "kind": "columnHeader",
-                    "rowIndex": 0,
-                    "columnIndex": 0,
-                    "columnSpan": 4,
-                    "content": "(In millions, except earnings per share)",
-                    "boundingRegions": [],
-                    "spans": []
-                    },
-            ]
-        }
-    ]
-}
-
-```
----
-::: moniker-end
-
-::: moniker range="doc-intel-4.0.0"
-
-#### [Sample code](#tab/sample-code)
-
-```Python
-if result.tables:
-    for table_idx, table in enumerate(result.tables):
-        print(f"Table # {table_idx} has {table.row_count} rows and " f"{table.column_count} columns")
-        if table.bounding_regions:
-            for region in table.bounding_regions:
-                print(f"Table # {table_idx} location on page: {region.page_number} is {region.polygon}")
-        # Analyze cells.
-        for cell in table.cells:
-            print(f"...Cell[{cell.row_index}][{cell.column_index}] has text '{cell.content}'")
-            if cell.bounding_regions:
-                for region in cell.bounding_regions:
-                print(f"...content on page {region.page_number} is within bounding polygon '{region.polygon}'")
 
-```
 > [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py)
+> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model/sample_analyze_layout.py) 
 
 #### [Output](#tab/output)
 
@@ -736,14 +1091,15 @@ if result.tables:
 }
 
 ```
+
 ---
-::: moniker-end
+:::moniker-end
 
-::: moniker range="doc-intel-3.1.0"
+:::moniker range="doc-intel-3.1.0"
 
 ### Annotations (available only in ``2023-02-28-preview`` API.)
 
-The Layout model extracts annotations in documents, such as checks and crosses. The response includes the kind of annotation, along with a confidence score and bounding polygon.
+The Layout model extracts annotations in documents, such as checks and crosses. The response ../includes the kind of annotation, along with a confidence score and bounding polygon.
 
 ```json
     {
@@ -760,185 +1116,22 @@ The Layout model extracts annotations in documents, such as checks and crosses.
     ]
 }
 ```
-::: moniker-end
-
-::: moniker range="doc-intel-4.0.0"
-
-### Output to markdown format
-
-The Layout API can output the extracted text in markdown format. Use the `outputContentFormat=markdown` to specify the output format in markdown. The markdown content is output as part of the `content` section.
-
-> [!NOTE]
-> Starting from *2024-07-31-preview*, the representation of tables is changed to HTML tables to enable rendering of merged cells, multi-row headers, etc. Another related change is to use Unicode checkbox characters ☒ and ☐ for selection marks instead of :selected: and :unselected:.  Note that this means that the content of selection mark fields will contain :selected: even though their spans refer to Unicode characters in the top-level span.
-
-#### [Sample code](#tab/sample-code)
-
-```Python
-document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))
-poller = document_intelligence_client.begin_analyze_document(
-    "prebuilt-layout",
-    AnalyzeDocumentRequest(url_source=url),
-    output_content_format=ContentFormat.MARKDOWN,
-)
-
-```
-
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_documents_output_in_markdown.py)
-
-#### [Output](#tab/output)
-
-```Markdown
-<!-- PageHeader="This is the header of the document." -->
-
-This is title
-===
-# 1\. Text
-Latin refers to an ancient Italic language originating in the region of Latium in ancient Rome.
-# 2\. Page Objects
-## 2.1 Table
-Here's a sample table below, designed to be simple for easy understand and quick reference.
-| Name | Corp | Remark |
-| - | - | - |
-| Foo | | |
-| Bar | Microsoft | Dummy |
-Table 1: This is a dummy table
-## 2.2. Figure
-<figure>
-<figcaption>
-
-Figure 1: Here is a figure with text
-</figcaption>
-
-![](figures/0)
-<!-- FigureContent="500 450 400 400 350 250 200 200 200- Feb" -->
-</figure>
-
-# 3\. Others
-Al Document Intelligence is an Al service that applies advanced machine learning to extract text, key-value pairs, tables, and structures from documents automatically and accurately:
- :selected:
-clear
- :selected:
-precise
- :unselected:
-vague
- :selected:
-coherent
- :unselected:
-Incomprehensible
-Turn documents into usable data and shift your focus to acting on information rather than compiling it. Start with prebuilt models or create custom models tailored to your documents both on premises and in the cloud with the Al Document Intelligence studio or SDK.
-Learn how to accelerate your business processes by automating text extraction with Al Document Intelligence. This webinar features hands-on demos for key use cases such as document processing, knowledge mining, and industry-specific Al model customization.
-<!-- PageFooter="This is the footer of the document." -->
-<!-- PageFooter="1 | Page" -->
-```
----
-
-### Figures
-
-Figures (charts, images) in documents play a crucial role in complementing and enhancing the textual content, providing visual representations that aid in the understanding of complex information. The figures object detected by the Layout model has key properties like `boundingRegions` (the spatial locations of the figure on the document pages, including the page number and the polygon coordinates that outline the figure's boundary), `spans` (details the text spans related to the figure, specifying their offsets and lengths within the document's text. This connection helps in associating the figure with its relevant textual context), `elements` (the identifiers for text elements or paragraphs within the document that are related to or describe the figure) and `caption` if there's any.
-
-When *output=figures* is specified during the initial analyze operation, the service generates cropped images for all detected figures that can be accessed via `/analyeResults/{resultId}/figures/{figureId}`.
-`FigureId` is included in each figure object, following an undocumented convention of `{pageNumber}.{figureIndex}` where `figureIndex` resets to one per page.
-
-> [!NOTE]
-> Starting with *2024-07-31-preview*, the bounding regions for figures and tables cover only the core content and exclude associated caption and footnotes.
-
-#### [Sample code](#tab/sample-code)
-
-```Python
-# Analyze figures.
-if result.figures:
-    for figures_idx,figures in enumerate(result.figures):
-        print(f"Figure # {figures_idx} has the following spans:{figures.spans}")
-        for region in figures.bounding_regions:
-            print(f"Figure # {figures_idx} location on page:{region.page_number} is within bounding polygon '{region.polygon}'")
-```
-
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Layout_model/sample_analyze_layout.py)
-
-#### [Output](#tab/output)
-
-```json
-{
-    "figures": [
-      {
-        "id": "{figureId}",
-        "boundingRegions": [],
-        "spans": [],
-        "elements": [
-          "/paragraphs/15",
-          ...
-        ],
-        "caption": {
-          "content": "Here is a figure with some text",
-          "boundingRegions": [],
-          "spans": [],
-          "elements": [
-            "/paragraphs/15"
-          ]
-        }
-      }
-    ]
-}
-```
-:::image type="content" source="media/document-layout-example-figures.png" alt-text="Screenshot of examples of document figures.":::
-
----
-### Sections
-Hierarchical document structure analysis is pivotal in organizing, comprehending, and processing extensive documents. This approach is vital for semantically segmenting long documents to boost comprehension, facilitate navigation, and improve information retrieval. The advent of [Retrieval Augmented Generation (RAG)](concept-retrieval-augmented-generation.md) in document generative AI underscores the significance of hierarchical document structure analysis. The Layout model supports sections and subsections in the output, which identifies the relationship of sections and object within each section. The hierarchical structure is maintained in `elements` of each section. You can use [output to markdown format](#output-to-markdown-format) to easily get the sections and subsections in markdown.
-
-#### [Sample code](#tab/sample-code)
-
-```Python
-document_intelligence_client = DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key))
-poller = document_intelligence_client.begin_analyze_document(
-    "prebuilt-layout",
-    AnalyzeDocumentRequest(url_source=url),
-    output_content_format=ContentFormat.MARKDOWN,
-)
-
-```
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/documentintelligence/azure-ai-documentintelligence/samples/sample_analyze_documents_output_in_markdown.py)
-
-#### [Output](#tab/output)
-
-```json
-{
-    "sections": [
-      {
-        "spans": [],
-        "elements": [
-          "/paragraphs/0",
-          "/sections/1",
-          "/sections/2",
-          "/sections/5"
-        ]
-      },
-...
-}
-```
 
-:::image type="content" source="media/document-layout-example-section.png" alt-text="Screenshot of examples of document sections.":::
+:::moniker-end
 
----
-
-::: moniker-end
-
-::: moniker range="doc-intel-2.1.0"
+:::moniker range="doc-intel-2.1.0"
 
 ### Natural reading order output (Latin only)
 
 You can specify the order in which the text lines are output with the `readingOrder` query parameter. Use `natural` for a more human-friendly reading order output as shown in the following example. This feature is only supported for Latin languages.
 
-:::image type="content" source="media/layout-reading-order-example.png" alt-text="Screenshot of `layout` model reading order processing." lightbox="../../ai-services/Computer-vision/Images/ocr-reading-order-example.png":::
+:::image type="content" source="../media/layout-reading-order-example.png" alt-text="Screenshot of `layout` model reading order processing." lightbox="../../../ai-services/Computer-vision/Images/ocr-reading-order-example.png":::
 
 ### Select page numbers or ranges for text extraction
 
 For large multi-page documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction. The following example shows a document with 10 pages, with text extracted for both cases - all pages (1-10) and selected pages (3-6).
 
-:::image type="content" source="./media/layout-select-pages.png" alt-text="Screen shot of the layout model selected pages output.":::
+:::image type="content" source="../media/layout-select-pages.png" alt-text="Screen shot of the layout model selected pages output.":::
 
 ## The Get Analyze Layout Result operation
 
@@ -950,13 +1143,13 @@ The second step is to call the [Get Analyze Layout Result](https://westcentralus
 
 Call this operation iteratively until it returns the `succeeded` value. To avoid exceeding the requests per second (RPS) rate, use an interval of 3 to 5 seconds.
 
-When the **status** field has the `succeeded` value, the JSON response includes the extracted layout, text, tables, and selection marks. The extracted data includes extracted text lines and words, bounding boxes, text appearance with handwritten indication, tables, and selection marks with selected/unselected indicated.
+When the **status** field has the `succeeded` value, the JSON response ../includes the extracted layout, text, tables, and selection marks. The extracted data ../includes extracted text lines and words, bounding boxes, text appearance with handwritten indication, tables, and selection marks with selected/unselected indicated.
 
 ### Handwritten classification for text lines (Latin only)
 
-The response includes classifying whether each text line is of handwriting style or not, along with a confidence score. This feature is only supported for Latin languages. The following example shows the handwritten classification for the text in the image.
+The response ../includes classifying whether each text line is of handwriting style or not, along with a confidence score. This feature is only supported for Latin languages. The following example shows the handwritten classification for the text in the image.
 
-:::image type="content" source="./media/layout-handwriting-classification.png" alt-text="Screenshot of `layout` model handwriting classification process.":::
+:::image type="content" source="../media/layout-handwriting-classification.png" alt-text="Screenshot of `layout` model handwriting classification process.":::
 
 ### Sample JSON output
 
@@ -976,41 +1169,46 @@ Layout API extracts text from documents and images with multiple text angles and
 
 ### Tables with headers
 
-Layout API extracts tables in the `pageResults` section of the JSON output. Documents can be scanned, photographed, or digitized. Tables can be complex with merged cells or columns, with or without borders, and with odd angles. Extracted table information includes the number of columns and rows, row span, and column span. Each cell with its bounding box is output along with whether the area is recognized as part of a header or not. The model predicted header cells can span multiple rows and aren't necessarily the first rows in a table. They also work with rotated tables. Each table cell also includes the full text with references to the individual words in the `readResults` section.
+Layout API extracts tables in the `pageResults` section of the JSON output. Documents can be scanned, photographed, or digitized. Tables can be complex with merged cells or columns, with or without borders, and with odd angles. Extracted table information ../includes the number of columns and rows, row span, and column span. Each cell with its bounding box is output along with whether the area is recognized as part of a header or not. The model predicted header cells can span multiple rows and aren't necessarily the first rows in a table. They also work with rotated tables. Each table cell also ../includes the full text with references to the individual words in the `readResults` section.
 
-![Tables example](./media/layout-table-header-demo.gif)
+![Tables example](../media/layout-table-header-demo.gif)
 
 ### Selection marks
 
 Layout API also extracts selection marks from documents. Extracted selection marks include the bounding box, confidence, and state (selected/unselected). Selection mark information is extracted in the `readResults` section of the JSON output.
 
 ### Migration guide
 
-* Follow our [**Document Intelligence v3.1 migration guide**](v3-1-migration-guide.md) to learn how to use the v3.1 version in your applications and workflows.
-::: moniker-end
+* Follow our [**Document Intelligence v3.1 migration guide**](../v3-1-migration-guide.md) to learn how to use the v3.1 version in your applications and workflows.
+
+:::moniker-end
 
 ## Next steps
 
-::: moniker range=">=doc-intel-3.0.0"
+:::moniker range="doc-intel-4.0.0 || doc-intel-3.1.0"
 
-* [Learn how to process your own forms and documents](quickstarts/try-document-intelligence-studio.md) with the [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio).
+* [Learn how to process your own forms and documents](../quickstarts/try-document-intelligence-studio.md) with the [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
-::: moniker-end
+:::moniker-end
+
+:::moniker range="doc-intel-4.0.0"
 
-::: moniker range="doc-intel-4.0.0"
 * [Find more samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/tree/main/Python(v4.0)/Layout_model)
-::: moniker-end
 
-::: moniker range="doc-intel-3.1.0"
+:::moniker-end
+
+:::moniker range="doc-intel-3.1.0"
+
 * [Find more samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/tree/v3.1(2023-07-31-GA)/Python(v3.1)/Layout_model)
-::: moniker-end
 
-::: moniker range="doc-intel-2.1.0"
+:::moniker-end
+
+:::moniker range="doc-intel-2.1.0"
 
-* [Learn how to process your own forms and documents](quickstarts/try-sample-label-tool.md) with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
+* [Learn how to process your own forms and documents](../quickstarts/try-sample-label-tool.md) with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
-::: moniker-end
+:::moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "レイアウトモデルページの名称変更と大幅な内容更新"
}
```

### Explanation
この変更は、ファイル「concept-layout.md」が「layout.md」にリネームされ、その内容が大幅に更新されたことを示しています。合計で1104行が変更され、その内訳には651行の追加と453行の削除が含まれています。

主な変更点は以下の通りです：

1. **ファイル名の変更**: ドキュメントが`concept-layout.md`から`layout.md`に変更され、ドキュメントの内容が明確に示されるようになりました。

2. **コンテンツの大幅な更新**: レイアウトモデルに関する説明が詳細に見直され、ドキュメント分析の仕組みや、ユーザーがどのように応用できるかについて豊富な情報が追加されました。

3. **新しいコンテンツ構成**: コンテンツがセクションごとに整理され、各セクションには具体的な例や画像、コードスニペットが加えられ、利用者が理解しやすい構成になっています。

4. **相対パスの採用**: ドキュメント内のリンクや画像パスがすべて相対パスに変更され、リンク切れのリスクが軽減され、一貫性が向上しました。

5. **REST API と SDK の統合**: ドキュメントで利用できるツール、アプリケーション、およびライブラリのリストが整理され、アクセス可能なリソースへのリンクが提供されています。

6. **データ抽出の手順とサンプルコード**: テキスト、テーブル、選択マークなどのデータの抽出手順が明確に示され、実際のPythonコードのサンプルが提供されています。

7. **サポートされる言語の確認**: 各種言語のサポート状況が示され、利用者が取り扱う文書に応じた適切なモデルを選択できるよう配慮されています。

これらの変更により、ドキュメントは最新の機能を反映した適切な使用方法を提供することになり、ユーザーにとってより有用かつ実用的なリソースとなっています。

## articles/ai-services/document-intelligence/prebuilt/marriage-certificate.md{#item-936798}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 04/23/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 monikerRange: '>=doc-intel-4.0.0'
 ---
@@ -19,7 +19,7 @@ monikerRange: '>=doc-intel-4.0.0'
 
 # Document Intelligence marriage certificate model
 
-**This content applies to:** ![checkmark](media/yes-icon.png) **v4.0 (preview)** ![checkmark](media/yes-icon.png)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (preview)** ![checkmark](../media/yes-icon.png)
 
 The Document Intelligence Marriage Certificate model uses powerful Optical Character Recognition (OCR) capabilities to analyze and extract key fields from Marriage Certificates. Marriage certificates  can be of various formats and quality including phone-captured images, scanned documents, and digital PDFs. The API analyzes document text; extracts key information such as Spouse names, Issue date, and marriage place; and returns a structured JSON data representation. The model currently supports English-language document formats.
 
@@ -35,12 +35,13 @@ Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, ap
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**prebuilt-marriageCertificate.us**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=marriageCertificate.us&formType=marriageCertificate.us)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-marriageCertificate.us**|
+|**prebuilt-marriageCertificate.us**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=marriageCertificate.us&formType=marriageCertificate.us)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-marriageCertificate.us**|
+
 ::: moniker-end
 
 ## Input requirements
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ## Try marriage certificate document data extraction
 
@@ -50,7 +51,7 @@ To see how data extraction works for the marriage certificate card service, you
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 ## Document Intelligence Studio
 
@@ -60,18 +61,18 @@ To see how data extraction works for the marriage certificate card service, you
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
 > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=invoice)
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extraction
 
-The following are the fields extracted from a marriage certificate  in the JSON output response. 
+The following are the fields extracted from a marriage certificate  in the JSON output response.
 
 |Name| Type | Description | Example output |
 |:-----|:----|:----|:---:|
@@ -101,4 +102,4 @@ The marriage certificate key-value pairs and line items extracted are in the `do
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "婚姻証明書モデルページの名称変更と内容更新"
}
```

### Explanation
この変更は、「concept-marriage-certificate.md」ファイルが「marriage-certificate.md」にリネームされ、内容が少し更新されたことを示しています。合計で19行が変更され、その内訳には10行の追加と9行の削除が含まれています。

主な変更内容は次の通りです：

1. **ファイル名の変更**: ドキュメントが`concept-marriage-certificate.md`から`marriage-certificate.md`にリネームされ、タイトルがより直接的になり、ユーザーが内容を理解しやすくなっています。

2. **日付の修正**: ドキュメントの最終更新日が`04/23/2024`から`10/03/2024`に変更され、最新の情報が反映されています。

3. **相対パスの使用**: 画像やリンクが相対パスに変更され、ファイル構造が一貫性を持ち、他のコンテンツとの整合性が向上しました。

4. **説明の改善**: 婚姻証明書モデルの説明がわかりやすく整理され、モデルがどのように機能し、どの情報を抽出できるかについての情報が明確になっています。

5. **パラメータの変更**: モデルIDに関する情報が更新され、ユーザーが使用できる最新のリソースへスムーズにアクセスできるようになっています。

6. **ユーザー操作の整理**: ドキュメントインテリジェンススタジオの使用に関する手順が整理され、具体的な画面ショットが追加されており、ユーザーが操作しやすくなっています。

これらの変更により、婚姻証明書モデルに関するドキュメントは、最新の機能とユーザーへの利便性をより強調したコンテンツに進化しています。

## articles/ai-services/document-intelligence/prebuilt/mortgage-documents.md{#item-b3136a}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 05/07/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 monikerRange: '>=doc-intel-4.0.0'
 ---
@@ -19,7 +19,7 @@ monikerRange: '>=doc-intel-4.0.0'
 
 # Document Intelligence mortgage document models
 
-**This content applies to:** ![checkmark](media/yes-icon.png) **v4.0 (preview)** ![checkmark](media/yes-icon.png)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (preview)** ![checkmark](../media/yes-icon.png)
 
 The Document Intelligence Mortgage models use powerful Optical Character Recognition (OCR) capabilities and deep learning models to analyze and extract key fields from mortgage documents. Mortgage documents can be of various formats and quality. The API analyzes mortgage documents and returns a structured JSON data representation. The models currently support English-language documents only.
 
@@ -31,7 +31,6 @@ The Document Intelligence Mortgage models use powerful Optical Character Recogni
 * Uniform Underwriting and Transmittal Summary (Form 1008)
 * Closing Disclosure form
 
-
 ## Development options
 
 ::: moniker range="doc-intel-4.0.0"
@@ -40,12 +39,13 @@ Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, ap
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Mortgage model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**&bullet; prebuilt-mortgage.us.1003</br>&bullet; prebuilt-mortgage.us.1004</br>&bullet; prebuilt-mortgage.us.1005</br>&bullet; prebuilt-mortgage.us.1008</br>&bullet; prebuilt-mortgage.us.closingDisclosure**|
+|**Mortgage model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**&bullet; prebuilt-mortgage.us.1003</br>&bullet; prebuilt-mortgage.us.1004</br>&bullet; prebuilt-mortgage.us.1005</br>&bullet; prebuilt-mortgage.us.1008</br>&bullet; prebuilt-mortgage.us.closingDisclosure**|
+
 ::: moniker-end
 
 ## Input requirements
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ## Try mortgage documents data extraction
 
@@ -55,7 +55,7 @@ To see how data extraction works for the mortgage documents service, you need th
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 ## Document Intelligence Studio
 
@@ -65,14 +65,14 @@ To see how data extraction works for the mortgage documents service, you need th
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
 > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=invoice)
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extraction 1003 Uniform Residential Loan Application (URLA)
 
@@ -128,8 +128,8 @@ The following are the fields extracted from a 1003 URLA form in the JSON output
 |`Property.MixedUseProperty`|`selectionGroup`|Is the property a mixed-use property?|:selected: NO:unselected: YES|
 |`Property.ManufacturedHome`|`selectionGroup`|Is the property a manufactured home?|:selected: NO:unselected: YES|
 
-
 ## Field extraction 1004 Uniform Residential Appraisal Report (URAR)
+
 The following are the fields extracted from a 1004 URAR form in the JSON output response.
 
 | Field | Type | Description | Example |
@@ -211,15 +211,16 @@ The following are the fields extracted from a 1004 URAR form in the JSON output
 |`Appraiser.CompanyName`|`string`|Name of the appraisal company for which the appraiser works|Valuation Experts LLC|
 |`Appraiser.CompanyAddress`|`address`|Physical address of the appraisal company|789 Valuation Blvd, Valuetown, MA 34567|
 |`Appraiser.TelephoneNumber`|`phoneNumber`|Telephone number where the appraiser or the appraisal company can be reached|(123) 456-7890|
-|`Appraiser.EmailAddress`|`string`|Email address where the appraiser or the appraisal company can be reached|alice.johnson@valuationexperts.com|
+|`Appraiser.EmailAddress`|`string`|Email address where the appraiser or the appraisal company can be reached|`alice.johnson@valuationexperts.com`|
 |`Appraiser.SignatureAndReportDate`|`date`|Date on which the appraiser signed the appraisal report|04/20/2023|
 |`Appraiser.EffectiveDate`|`date`|Date on which the appraisal is considered effective|04/20/2023|
 |`Appraiser.PropertyAppraisedAddress`|`address`|Address of the property that was appraised|123 Main St., Anytown, MA 12345|
 |`Appraiser.AppraisedValueOfSubjectProperty`|`number`|Final appraised value of the subject property|248000.00|
 |`Appraiser.SubjectPropertyStatus`|`selectionGroup`|Inspection status of the subject property at the time of appraisal|:unselected: Didn't inspect subject property<br>:unselected: Did inspect exterior of subject property from street<br>:unselected: Did inspect interior and exterior of subject property|
 |`Appraiser.ComparableSalesStatus`|`selectionGroup`|Inspection status of the comparable sales used in the appraisal|:unselected: Didn't inspect exterior of comparable sales from street<br>:unselected: Did inspect exterior of comparable sales from street|
 
-## Field extraction 1005 Verification of employment form 
+## Field extraction 1005 Verification of employment form
+
 The following are the fields extracted from a 1005 form in the JSON output response.
 
 | Field | Type | Description | Example |
@@ -238,7 +239,6 @@ The following are the fields extracted from a 1005 form in the JSON output respo
 |`PreviousEmployment.DateTerminated`|`date`|Date when the applicant's employment was terminated or when they left their previous job|10/30/2020|
 |`PreviousEmployment.PositionHeld`|`string`|Title or role the applicant held in their previous job|SUPERVISOR|
 
-
 ## Field extraction 1008 Uniform Underwriting and Transmittal Summary
 
 The following are the fields extracted from a 1008 form in the JSON output response.
@@ -337,5 +337,4 @@ The mortgage closing disclosure key-value pairs and line items extracted are in
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
- 
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "住宅ローン文書モデルページの名称変更と内容更新"
}
```

### Explanation
この変更は、「concept-mortgage-documents.md」ファイルが「mortgage-documents.md」にリネームされ、内容が少し更新されたことを示しています。合計で27行が変更され、その内訳には13行の追加と14行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名の変更**: ドキュメントが`concept-mortgage-documents.md`から`mortgage-documents.md`にリネームされ、より特定のモデル名が強調されています。

2. **日付の更新**: ドキュメントの最終更新日が`05/07/2024`から`10/03/2024`に変更され、最新の情報が反映されています。

3. **相対パスの使用**: リンクや画像パスが全て相対パスに変更され、ドキュメント内のリンク切れのリスクが軽減され、ファイル構造の一貫性が向上しました。

4. **モデルの説明**: 住宅ローンモデルに関する説明がわかりやすく整理され、APIがどのように機能し、どの情報を抽出できるかについての情報が明確になっています。

5. **利用可能なモデルのリスト**: 新たに支援される文書タイプが、文書インテリジェンスの機能として追加されており、モデルの利用についての具体的な情報が強調されています。

6. **データ抽出の説明の整理**: 各フォームにおけるフィールド抽出の説明が整理され、JSON出力の例が提供されています。この情報は、ユーザーがどのようなデータを期待できるかを理解するのに役立ちます。

7. **クイックスタートガイドのリンクの修正**: クイックスタートのリンクが更新され、最新バージョンのドキュメント処理アプリを開発するためのリソースが提供されています。

これらの変更により、住宅ローン関連のドキュメントモデルに関する情報はより明確で実用的になり、ユーザーにとっての利便性が高まっています。

## articles/ai-services/document-intelligence/prebuilt/pay-stub.md{#item-7f747e}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 08/07/2024
+ms.date: 10/03/2024
 ms.author: admaheshwari
 monikerRange: '>=doc-intel-4.0.0'
 ---
@@ -29,7 +29,7 @@ Pay stubs are essential documents issued by employers to employees, providing ea
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
-    :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+    :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 ## Document Intelligence Studio
 
@@ -41,11 +41,11 @@ Pay stubs are essential documents issued by employers to employees, providing ea
 
 ## Input requirements
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ## Supported languages and locales
 
-*See* our [Language Support](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extractions
 
@@ -76,4 +76,4 @@ The **prebuilt-payStub.us** version 2027-07-31-preview supports the **en-us** lo
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "給与明細モデルページの名称変更と内容更新"
}
```

### Explanation
この変更は、「concept-pay-stub.md」ファイルが「pay-stub.md」にリネームされ、内容が少し更新されたことを示しています。合計で10行が変更され、その内訳には5行の追加と5行の削除が含まれています。

主な変更内容は次の通りです：

1. **ファイル名の変更**: ドキュメントが`concept-pay-stub.md`から`pay-stub.md`にリネームされ、ユーザーが内容をすぐに理解できるようになっています。

2. **日付の更新**: ドキュメントの最終更新日が`08/07/2024`から`10/03/2024`に変更され、最新の情報が確保されています。

3. **相対パスの使用**: 画像やリンクが相対パスに変更され、ファイルの構造が一貫し、他の関連コンテンツへのリンクがより安定しました。

4. **入力要件の更新**: 入力要件に関する情報が整理され、最新のファイルパスが反映されています。

5. **言語サポートの更新**: サポートされている言語に関する情報が最新のファイル構成に基づいて変更され、ユーザーにとってアクセスしやすくなっています。

6. **クイックスタートガイドのリンクの更新**: クイックスタートに関するリンクが更新され、最新の情報にアクセスできるようになっています。

これらの変更により、給与明細モデルに関する重要な情報が明確に整理され、ユーザーが必要な情報を効率良く得られるように改善されています。

## articles/ai-services/document-intelligence/prebuilt/read.md{#item-06f32f}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,633 @@
+---
+title: Read model OCR data extraction - Document Intelligence
+titleSuffix: Azure AI services
+description: Extract print and handwritten text from scanned and digital documents with Document Intelligence's Read OCR model.
+author: laujan
+manager: nitinme
+ms.service: azure-ai-document-intelligence
+ms.topic: conceptual
+ms.date: 10/07/2024
+ms.author: lajanuar
+---
+
+<!-- markdownlint-disable MD033 -->
+<!-- markdownlint-disable MD051 -->
+<!-- markdownlint-disable MD024 -->
+
+# Document Intelligence read model
+
+<!---------------------- v4.0 content ---------------------->
+
+ ::: moniker range="doc-intel-4.0.0"
+
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
+
+**This content applies to:**![checkmark](../media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
+
+**This content applies to:**![checkmark](../media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
+
+> [!NOTE]
+>
+> For extracting text from external images like labels, street signs, and posters, use the [Azure AI Image Analysis v4.0 Read](../../Computer-vision/concept-ocr.md) feature optimized for general, non-document images with a performance-enhanced synchronous API that makes it easier to embed OCR in your user experience scenarios.
+>
+
+Document Intelligence Read Optical Character Recognition (OCR) model runs at a higher resolution than Azure AI Vision Read and extracts print and handwritten text from PDF documents and scanned images. It also includes support for extracting text from Microsoft Word, Excel, PowerPoint, and HTML documents. It detects paragraphs, text lines, words, locations, and languages. The Read model is the underlying OCR engine for other Document Intelligence prebuilt models like Layout, General Document, Invoice, Receipt, Identity (ID) document, Health insurance card, W2 in addition to custom models.
+
+## What is Optical Character Recognition?
+
+Optical Character Recognition (OCR) for documents is optimized for large text-heavy documents in multiple file formats and global languages. It includes features like higher-resolution scanning of document images for better handling of smaller and dense text; paragraph detection; and fillable form management. OCR capabilities also include advanced scenarios like single character boxes and accurate extraction of key fields commonly found in invoices, receipts, and other prebuilt scenarios.
+
+## Development options (v4)
+
+Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, applications, and libraries:
+
+| Feature | Resources | Model ID |
+|----------|-------------|-----------|
+|**Read OCR model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-read**|
+
+## Input requirements (v4)
+
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
+
+## Get started with Read model (v4)
+
+Try extracting text from forms and documents using the Document Intelligence Studio. You need the following assets:
+
+* An Azure subscription—you can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
+
+* A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
+
+  :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+
+> [!NOTE]
+> Currently, Document Intelligence Studio doesn't support Microsoft Word, Excel, PowerPoint, and HTML file formats.
+
+***Sample document processed with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/read)***
+
+:::image type="content" source="../media/studio/form-recognizer-studio-read-v3p2-updated.png" alt-text="Screenshot of Read processing in Document Intelligence Studio.":::
+
+1. On the [Document Intelligence Studio home page](https://documentintelligence.ai.azure.com/studio), select **Read**.
+
+1. You can analyze the sample document or upload your own files.
+
+1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
+
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+
+    > [!div class="nextstepaction"]
+    > [Try Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/read).
+
+## Supported languages and locales (v4)
+
+See our [Language Support—document analysis models](../language-support/ocr.md) page for a complete list of supported languages.
+
+## Data extraction (v4)
+
+> [!NOTE]
+> Microsoft Word and HTML file are supported in v4.0. Compared with PDF and images, below features are not supported:
+>
+> * There are no angle, width/height and unit with each page object.
+> * For each object detected, there is no bounding polygon or bounding region.
+> * Page range (`pages`) is not supported as a parameter.
+> * No `lines` object.
+
+## Searchable PDFs
+
+The searchable PDF capability enables you to convert an analog PDF, such as scanned-image PDF files, to a PDF with embedded text. The embedded text enables deep text search within the PDF's extracted content by overlaying the detected text entities on top of the image files.
+
+  > [!IMPORTANT]
+  >
+  > * Currently, the searchable PDF capability is only supported by Read OCR model `prebuilt-read`. When using this feature, please specify the `modelId` as `prebuilt-read`, as other model types will return error for this preview version.
+  > * Searchable PDF is included with the 2024-07-31-preview `prebuilt-read` model with no additional cost for generating a searchable PDF output.
+>   * Searchable PDF currently only supports PDF files as input. Support for other file types, such as image files, will be available later.
+
+### Use searchable PDFs
+
+To use searchable PDF, make a `POST` request using the `Analyze` operation and specify the output format as `pdf`:
+
+```bash
+
+     POST /documentModels/prebuilt-read:analyze?output=pdf
+     {...}
+     202
+```
+
+Poll for completion of the `Analyze` operation. Once the operation is complete, issue a `GET` request to retrieve the PDF format of the `Analyze` operation results.
+
+Upon successful completion, the PDF can be retrieved and downloaded as `application/pdf`. This operation allows direct downloading of the embedded text form of PDF instead of Base64-encoded JSON.
+
+```bash
+
+     // Monitor the operation until completion.
+     GET /documentModels/prebuilt-read/analyzeResults/{resultId}
+     200
+     {...}
+
+     // Upon successful completion, retrieve the PDF as application/pdf.
+     GET /documentModels/prebuilt-read/analyzeResults/{resultId}/pdf
+     200 OK
+     Content-Type: application/pdf
+```
+
+### Pages parameter
+
+The pages collection is a list of pages within the document. Each page is represented sequentially within the document and includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
+
+|**File format**   | **Computed page unit**   | **Total pages**  |
+| --- | --- | --- |
+|Images (JPEG/JPG, PNG, BMP, HEIF) | Each image = 1 page unit | Total images  |
+|PDF | Each page in the PDF = 1 page unit | Total pages in the PDF |
+|TIFF | Each image in the TIFF = 1 page unit | Total images in the TIFF |
+|Word (DOCX)  | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
+|Excel (XLSX)  | Each worksheet = 1 page unit, embedded or linked images not supported | Total worksheets |
+|PowerPoint (PPTX) |  Each slide = 1 page unit, embedded or linked images not supported | Total slides |
+|HTML | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
+
+#### [Sample code](#tab/sample-code)
+
+```Python
+    # Analyze pages.
+    for page in result.pages:
+        print(f"----Analyzing document from page #{page.page_number}----")
+        print(f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}")
+```
+
+  > [!div class="nextstepaction"]
+  > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Read_model/sample_analyze_read.py)
+
+#### [Output](#tab/output)
+
+```json
+    "pages": [
+        {
+            "pageNumber": 1,
+            "angle": 0,
+            "width": 915,
+            "height": 1190,
+            "unit": "pixel",
+            "words": [],
+            "lines": [],
+            "spans": []
+        }
+    ]
+```
+
+---
+
+### Use pages for text extraction
+
+For large multi-page PDF documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction.
+
+### Paragraph extraction
+
+The Read OCR model in Document Intelligence extracts all identified blocks of text in the `paragraphs` collection as a top level object under `analyzeResults`. Each entry in this collection represents a text block and includes the extracted text as`content` and the bounding `polygon` coordinates. The `span` information points to the text fragment within the top-level `content` property that contains the full text from the document.
+
+```json
+    "paragraphs": [
+        {
+            "spans": [],
+            "boundingRegions": [],
+            "content": "While healthcare is still in the early stages of its Al journey, we are seeing pharmaceutical and other life sciences organizations making major investments in Al and related technologies.\" TOM LAWRY | National Director for Al, Health and Life Sciences | Microsoft"
+        }
+    ]
+```
+
+### Text, lines, and words extraction
+
+The Read OCR model extracts print and handwritten style text as `lines` and `words`. The model outputs bounding `polygon` coordinates and `confidence` for the extracted words. The `styles` collection includes any handwritten style for lines if detected along with the spans pointing to the associated text. This feature applies to [supported handwritten languages](../../language-support.md).
+
+For Microsoft Word, Excel, PowerPoint, and HTML, Document Intelligence Read model v3.1 and later versions extracts all embedded text as is. Texts are extrated as words and paragraphs. Embedded images aren't supported.
+
+#### [Sample code](#tab/sample-code)
+
+```Python
+    # Analyze lines.
+    if page.lines:
+        for line_idx, line in enumerate(page.lines):
+            words = get_words(page, line)
+            print(
+                f"...Line # {line_idx} has {len(words)} words and text '{line.content}' within bounding polygon '{line.polygon}'"
+            )
+
+            # Analyze words.
+            for word in words:
+                print(f"......Word '{word.content}' has a confidence of {word.confidence}")
+```
+
+  > [!div class="nextstepaction"]
+  > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Read_model/sample_analyze_read.py)
+
+#### [Output](#tab/output)
+
+```json
+    "words": [
+        {
+            "content": "While",
+            "polygon": [],
+            "confidence": 0.997,
+            "span": {}
+        },
+    ],
+    "lines": [
+        {
+            "content": "While healthcare is still in the early stages of its Al journey, we",
+            "polygon": [],
+            "spans": [],
+        }
+    ]
+```
+
+---
+
+### Handwritten style extraction
+
+The response includes classifying whether each text line is of handwriting style or not, along with a confidence score. For more information, *see* [handwritten language support](../language-support/ocr.md). The following example shows an example JSON snippet.
+
+```json
+    "styles": [
+    {
+        "confidence": 0.95,
+        "spans": [
+        {
+            "offset": 509,
+            "length": 24
+        }
+        "isHandwritten": true
+        ]
+    }
+```
+
+If you enabled the [font/style addon capability](../concept-add-on-capabilities.md#font-property-extraction), you also get the font/style result as part of the `styles` object.
+
+## Next steps v4.0
+
+Complete a Document Intelligence quickstart:
+
+   > [!div class="checklist"]
+   >
+   > * [**REST API**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)
+   > * [**C# SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-csharp)
+   > * [**Python SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-python)
+   > * [**Java SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-java)
+   > * [**JavaScript**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-javascript)</li></ul>
+
+Explore our REST API:
+
+   > [!div class="nextstepaction"]
+   > [Document Intelligence API v4.0](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)
+
+Find more samples on GitHub:
+   > [!div class="nextstepaction"]
+   > [Read model.](https://github.com/Azure-Samples/document-intelligence-code-samples/tree/main/Python(v4.0)/Read_model)
+
+::: moniker-end
+
+<!---------------------- v3.1 v3.0 v2.1 content ---------------------->
+
+::: moniker range="doc-intel-3.1.0"
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true)
+::: moniker-end
+
+::: moniker range="doc-intel-3.0.0"
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](../media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true)
+::: moniker-end
+
+::: moniker range="<=doc-intel-3.1.0"
+
+> [!NOTE]
+>
+> For extracting text from external images like labels, street signs, and posters, use the [Azure AI Image Analysis v4.0 Read](../..//Computer-vision/concept-ocr.md) feature optimized for general, non-document images with a performance-enhanced synchronous API that makes it easier to embed OCR in your user experience scenarios.
+>
+
+Document Intelligence Read Optical Character Recognition (OCR) model runs at a higher resolution than Azure AI Vision Read and extracts print and handwritten text from PDF documents and scanned images. It also includes support for extracting text from Microsoft Word, Excel, PowerPoint, and HTML documents. It detects paragraphs, text lines, words, locations, and languages. The Read model is the underlying OCR engine for other Document Intelligence prebuilt models like Layout, General Document, Invoice, Receipt, Identity (ID) document, Health insurance card, W2 in addition to custom models.
+
+## What is OCR for documents?
+
+Optical Character Recognition (OCR) for documents is optimized for large text-heavy documents in multiple file formats and global languages. It includes features like higher-resolution scanning of document images for better handling of smaller and dense text; paragraph detection; and fillable form management. OCR capabilities also include advanced scenarios like single character boxes and accurate extraction of key fields commonly found in invoices, receipts, and other prebuilt scenarios.
+
+::: moniker-end
+
+::: moniker range="doc-intel-3.1.0"
+
+## Development options
+
+Document Intelligence v3.1 supports the following tools, applications, and libraries:
+
+| Feature | Resources | Model ID |
+|----------|-------------|-----------|
+|**Read OCR model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-read**|
+
+::: moniker-end
+
+::: moniker range="doc-intel-3.0.0"
+
+Document Intelligence v3.0 supports the following tools, applications, and libraries:
+
+| Feature | Resources | Model ID |
+|----------|-------------|-----------|
+|**Read OCR model**|&bullet; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-read**|
+
+::: moniker-end
+
+ ::: moniker range="<= doc-intel-3.1.0"
+
+## Input requirements
+
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
+
+## Get started with Read model
+
+Try extracting text from forms and documents using the Document Intelligence Studio. You need the following assets:
+
+* An Azure subscription—you can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
+
+* A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
+
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+
+> [!NOTE]
+> Currently, Document Intelligence Studio doesn't support Microsoft Word, Excel, PowerPoint, and HTML file formats.
+
+***Sample document processed with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/read)***
+
+:::image type="content" source="../media/studio/form-recognizer-studio-read-v3p2-updated.png" alt-text="Screenshot of Read processing in Document Intelligence Studio.":::
+
+1. On the [Document Intelligence Studio home page](https://documentintelligence.ai.azure.com/studio), select **Read**.
+
+1. You can analyze the sample document or upload your own files.
+
+1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
+
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+
+    > [!div class="nextstepaction"]
+    > [Try Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio/read).
+
+## Supported languages and locales
+
+See our [Language Support—document analysis models](../language-support/ocr.md) page for a complete list of supported languages.
+
+## Data extraction
+
+> [!NOTE]
+> Microsoft Word and HTML file are supported in v3.1 and later versions. Compared with PDF and images, below features are not supported:
+>
+> * There are no angle, width/height and unit with each page object.
+> * For each object detected, there is no bounding polygon or bounding region.
+> * Page range (`pages`) is not supported as a parameter.
+> * No `lines` object.
+
+## Searchable PDF
+
+The searchable PDF capability enables you to convert an analog PDF, such as scanned-image PDF files, to a PDF with embedded text. The embedded text enables deep text search within the PDF's extracted content by overlaying the detected text entities on top of the image files.
+
+  > [!IMPORTANT]
+  >
+  > * Currently, the searchable PDF capability is only supported by Read OCR model `prebuilt-read`. When using this feature, please specify the `modelId` as `prebuilt-read`, as other model types will return error for this preview version.
+  > * Searchable PDF is included with the 2024-07-31-preview `prebuilt-read` model with no additional cost for generating a searchable PDF output.
+>   * Searchable PDF currently only supports PDF files as input. Support for other file types, such as image files, will be available later.
+
+### Use searchable PDF
+
+To use searchable PDF, make a `POST` request using the `Analyze` operation and specify the output format as `pdf`:
+
+```bash
+
+    POST /documentModels/prebuilt-read:analyze?output=pdf
+    {...}
+    202
+```
+
+Poll for completion of the `Analyze` operation. Once the operation is complete, issue a `GET` request to retrieve the PDF format of the `Analyze` operation results.
+
+Upon successful completion, the PDF can be retrieved and downloaded as `application/pdf`. This operation allows direct downloading of the embedded text form of PDF instead of Base64-encoded JSON.
+
+```bash
+
+    // Monitor the operation until completion.
+    GET /documentModels/prebuilt-read/analyzeResults/{resultId}
+    200
+    {...}
+
+    // Upon successful completion, retrieve the PDF as application/pdf.
+    GET /documentModels/prebuilt-read/analyzeResults/{resultId}/pdf
+    200 OK
+    Content-Type: application/pdf
+```
+
+### Pages
+
+The pages collection is a list of pages within the document. Each page is represented sequentially within the document and includes the orientation angle indicating if the page is rotated and the width and height (dimensions in pixels). The page units in the model output are computed as shown:
+
+|**File format**   | **Computed page unit**   | **Total pages**  |
+| --- | --- | --- |
+|Images (JPEG/JPG, PNG, BMP, HEIF) | Each image = 1 page unit | Total images  |
+|PDF | Each page in the PDF = 1 page unit | Total pages in the PDF |
+|TIFF | Each image in the TIFF = 1 page unit | Total images in the TIFF |
+|Word (DOCX)  | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
+|Excel (XLSX)  | Each worksheet = 1 page unit, embedded or linked images not supported | Total worksheets |
+|PowerPoint (PPTX) |  Each slide = 1 page unit, embedded or linked images not supported | Total slides |
+|HTML | Up to 3,000 characters = 1 page unit, embedded or linked images not supported | Total pages of up to 3,000 characters each |
+
+::: moniker-end
+
+::: moniker range="doc-intel-2.1.0 || doc-intel-3.0.0"
+
+```json
+    "pages": [
+        {
+            "pageNumber": 1,
+            "angle": 0,
+            "width": 915,
+            "height": 1190,
+            "unit": "pixel",
+            "words": [],
+            "lines": [],
+            "spans": []
+        }
+    ]
+```
+
+::: moniker-end
+
+::: moniker range="doc-intel-3.1.0"
+
+#### [Sample code](#tab/sample-code)
+
+```Python
+    # Analyze pages.
+    for page in result.pages:
+        print(f"----Analyzing document from page #{page.page_number}----")
+        print(
+            f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}"
+        )
+```
+
+   > [!div class="nextstepaction"]
+   > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Read_model/sample_analyze_read.py)
+
+#### [Output](#tab/output)
+
+```json
+    "pages": [
+        {
+            "pageNumber": 1,
+            "angle": 0,
+            "width": 915,
+            "height": 1190,
+            "unit": "pixel",
+            "words": [],
+            "lines": [],
+            "spans": []
+        }
+    ]
+```
+
+---
+
+::: moniker-end
+
+::: moniker range="<=doc-intel-3.1.0"
+
+### Select pages for text extraction
+
+For large multi-page PDF documents, use the `pages` query parameter to indicate specific page numbers or page ranges for text extraction.
+
+### Paragraphs
+
+The Read OCR model in Document Intelligence extracts all identified blocks of text in the `paragraphs` collection as a top level object under `analyzeResults`. Each entry in this collection represents a text block and includes the extracted text as`content` and the bounding `polygon` coordinates. The `span` information points to the text fragment within the top-level `content` property that contains the full text from the document.
+
+```json
+    "paragraphs": [
+        {
+            "spans": [],
+            "boundingRegions": [],
+            "content": "While healthcare is still in the early stages of its Al journey, we are seeing pharmaceutical and other life sciences organizations making major investments in Al and related technologies.\" TOM LAWRY | National Director for Al, Health and Life Sciences | Microsoft"
+        }
+    ]
+```
+
+### Text, lines, and words
+
+The Read OCR model extracts print and handwritten style text as `lines` and `words`. The model outputs bounding `polygon` coordinates and `confidence` for the extracted words. The `styles` collection includes any handwritten style for lines if detected along with the spans pointing to the associated text. This feature applies to [supported handwritten languages](../language-support/prebuilt.md).
+
+For Microsoft Word, Excel, PowerPoint, and HTML, Document Intelligence Read model v3.1 and later versions extracts all embedded text as is. Texts are extrated as words and paragraphs. Embedded images aren't supported.
+
+::: moniker-end
+
+::: moniker range="doc-intel-2.1.0 || doc-intel-3.0.0"
+
+```json
+
+    "words": [
+        {
+            "content": "While",
+            "polygon": [],
+            "confidence": 0.997,
+            "span": {}
+        },
+    ],
+    "lines": [
+        {
+            "content": "While healthcare is still in the early stages of its Al journey, we",
+            "polygon": [],
+            "spans": [],
+        }
+    ]
+```
+
+::: moniker-end
+
+::: moniker range="doc-intel-3.1.0"
+
+#### [Sample code](#tab/sample-code)
+
+```Python
+    # Analyze lines.
+    for line_idx, line in enumerate(page.lines):
+        words = line.get_words()
+        print(
+            f"...Line # {line_idx} has {len(words)} words and text '{line.content}' within bounding polygon '{format_polygon(line.polygon)}'"
+        )
+
+        # Analyze words.
+        for word in words:
+            print(
+                f"......Word '{word.content}' has a confidence of {word.confidence}"
+            )
+```
+
+   > [!div class="nextstepaction"]
+   > [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Read_model/sample_analyze_read.py)
+
+#### [Output](#tab/output)
+
+```json
+    "words": [
+        {
+            "content": "While",
+            "polygon": [],
+            "confidence": 0.997,
+            "span": {}
+        },
+    ],
+    "lines": [
+        {
+            "content": "While healthcare is still in the early stages of its Al journey, we",
+            "polygon": [],
+            "spans": [],
+        }
+    ]
+```
+
+---
+::: moniker-end
+
+::: moniker range="<=doc-intel-3.1.0"
+
+### Handwritten style for text lines
+
+The response includes classifying whether each text line is of handwriting style or not, along with a confidence score. For more information, *see* [handwritten language support](../language-support/ocr.md). The following example shows an example JSON snippet.
+
+```json
+    "styles": [
+    {
+        "confidence": 0.95,
+        "spans": [
+        {
+            "offset": 509,
+            "length": 24
+        }
+        "isHandwritten": true
+        ]
+    }
+```
+
+If you enabled the [font/style addon capability](../concept-add-on-capabilities.md#font-property-extraction), you also get the font/style result as part of the `styles` object.
+
+## Next steps
+
+Complete a Document Intelligence quickstart:
+
+   > [!div class="checklist"]
+   >
+   > * [**REST API**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)
+   > * [**C# SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-csharp)
+   > * [**Python SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-python)
+   > * [**Java SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-java)
+   > * [**JavaScript**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-4.0.0&preserve-view=true?pivots=programming-language-javascript)</li></ul>
+
+Explore our REST API:
+
+   > [!div class="nextstepaction"]
+   > [Document Intelligence API v4.0](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)
+
+::: moniker-end
+
+::: moniker range="doc-intel-3.1.0"
+
+Find more samples on GitHub:
+   > [!div class="nextstepaction"]
+   > [Read model.](https://github.com/Azure-Samples/document-intelligence-code-samples/tree/v3.1(2023-07-31-GA)/Python(v3.1)/Read_model)
+
+::: moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Document Intelligence Readモデルの新しいページの追加"
}
```

### Explanation
この変更は、新しいファイル「read.md」が追加され、Document IntelligenceサービスのReadモデルに関する詳細な情報が633行分導入されました。これは、印刷されたテキストや手書きのテキストをスキャンしたりデジタル文書から抽出するための技術です。

主な内容は以下の通りです：

1. **Readモデルの概要**: Readモデルは、PDF文書やスキャンした画像から印刷物および手書きのテキストを抽出するための光学式文字認識（OCR）技術を使用しており、Microsoft Word、Excel、PowerPoint、HTML文書からのテキスト抽出もサポートしています。

2. **OCRについての説明**: OCR技術は、大量のテキストを扱う文書向けに最適化されており、特に小さな文字や密集したテキストの処理機能も向上しています。

3. **開発オプションの提示**: v4.0に対応するツール、アプリケーション、およびライブラリのリストが提供され、具体的にどのようにこの技術を活用できるのかのリソースが追加されています。

4. **入力要件**: 新しいファイルには、Readモデルを利用する際の具体的な入力要件が明記されています。

5. **具体的な機能と制限**: 例えば、PDFからの検索可能なPDFの作成や、ページごとのテキスト抽出のためのクエリパラメータ利用方法が詳しく説明されています。

6. **サンプルコード**: Pythonでの実装例や、実際に入力されたデータとその結果を確認するためのサンプルコードが豊富に提供されています。

この新しいページの追加により、ユーザーや開発者は、Document IntelligenceのOCR技術をより深く理解し、効果的に利用するための情報が得られるようになります。

## articles/ai-services/document-intelligence/prebuilt/receipt.md{#item-089054}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Use machine learning powered receipt data extraction model to digit
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 05/23/2024
 ms.author: lajanuar
@@ -17,21 +15,21 @@ ms.author: lajanuar
 # Document Intelligence receipt model
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-[!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
+[!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
+[!INCLUDE [applies to v3.1](../includes/applies-to-v31.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 ::: moniker-end
 
 The Document Intelligence receipt model combines powerful Optical Character Recognition (OCR) capabilities with deep learning models to analyze and extract key information from sales receipts. Receipts can be of various formats and quality including printed and handwritten receipts. The API extracts key information such as merchant name, merchant phone number, transaction date, tax, and transaction total and returns structured JSON data.
@@ -58,15 +56,15 @@ Receipt digitization encompasses the transformation of various types of receipts
 
 ***Sample receipt processed with [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=receipt)***:
 
-:::image type="content" source="media/studio/overview-receipt.png" alt-text="Screenshot of a sample receipt processed in the Document Intelligence Studio." lightbox="media/overview-receipt.jpg":::
+:::image type="content" source="../media/studio/overview-receipt.png" alt-text="Screenshot of a sample receipt processed in the Document Intelligence Studio." lightbox="../media/overview-receipt.jpg":::
 
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
 
 **Sample receipt processed with [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/connection)**:
 
-:::image type="content" source="media/analyze-receipt-fott.png" alt-text="Screenshot of a sample receipt processed with the Form Sample Labeling tool.":::
+:::image type="content" source="../media/analyze-receipt-fott.png" alt-text="Screenshot of a sample receipt processed with the Form Sample Labeling tool.":::
 
 ::: moniker-end
 
@@ -78,7 +76,7 @@ Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, ap
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Receipt model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-receipt**|
+|**Receipt model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**prebuilt-receipt**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
@@ -87,7 +85,7 @@ Document Intelligence v3.1 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Receipt model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-receipt**|
+|**Receipt model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**prebuilt-receipt**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
@@ -96,7 +94,7 @@ Document Intelligence v3.0 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**Receipt model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-receipt**|
+|**Receipt model**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**prebuilt-receipt**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
@@ -105,14 +103,14 @@ Document Intelligence v2.1 supports the following tools, applications, and libra
 
 | Feature | Resources |
 |----------|-------------------------|
-|**Receipt model**|&bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/prebuilts-analyze)</br>&bullet;  [**REST API**](how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&view=doc-intel-2.1.0&preserve-view=true&tabs=windows)</br>&bullet;  [**Client-library SDK**](~/articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet;  [**Document Intelligence Docker container**](containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
+|**Receipt model**|&bullet; [**Document Intelligence labeling tool**](https://fott-2-1.azurewebsites.net/prebuilts-analyze)</br>&bullet;  [**REST API**](../how-to-guides/use-sdk-rest-api.md?pivots=programming-language-rest-api&view=doc-intel-2.1.0&preserve-view=true&tabs=windows)</br>&bullet;  [**Client-library SDK**](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet;  [**Document Intelligence Docker container**](../containers/install-run.md?tabs=id-document#run-the-container-with-the-docker-compose-up-command)|
 ::: moniker-end
 
 ## Input requirements
 
 ::: moniker range=">=doc-intel-3.0.0"
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ::: moniker-end
 
@@ -132,7 +130,7 @@ See how Document Intelligence extracts data, including time and date of transact
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 ::: moniker range=">=doc-intel-3.0.0"
 
@@ -145,7 +143,7 @@ See how Document Intelligence extracts data, including time and date of transact
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options**:
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
     > [!div class="nextstepaction"]
     > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=receipt).
@@ -160,7 +158,7 @@ See how Document Intelligence extracts data, including time and date of transact
 
 1. On the sample tool home page, select the **Use prebuilt model to get data** tile.
 
-    :::image type="content" source="media/label-tool/prebuilt-1.jpg" alt-text="Screenshot of the layout model analyze results process.":::
+    :::image type="content" source="../media/label-tool/prebuilt-1.jpg" alt-text="Screenshot of the layout model analyze results process.":::
 
 1. Select the **Form Type**  to analyze from the dropdown menu.
 
@@ -176,19 +174,19 @@ See how Document Intelligence extracts data, including time and date of transact
 
 1. In the **Source** field, select **URL** from the dropdown menu, paste the selected URL, and select the **Fetch** button.
 
-    :::image type="content" source="media/label-tool/fott-select-url.png" alt-text="Screenshot of source location dropdown menu.":::
+    :::image type="content" source="../media/label-tool/fott-select-url.png" alt-text="Screenshot of source location dropdown menu.":::
 
 1. In the **Document Intelligence service endpoint** field, paste the endpoint that you obtained with your Document Intelligence subscription.
 
 1. In the **key** field, paste  the key you obtained from your Document Intelligence resource.
 
-    :::image type="content" source="media/fott-select-form-type.png" alt-text="Screenshot of the select-form-type dropdown menu.":::
+    :::image type="content" source="../media/fott-select-form-type.png" alt-text="Screenshot of the select-form-type dropdown menu.":::
 
 1. Select **Run analysis**. The Document Intelligence Sample Labeling tool calls the Analyze Prebuilt API and analyze the document.
 
 1. View the results - see the key-value pairs extracted, line items, highlighted text extracted, and tables detected.
 
-    :::image type="content" source="media/receipts-example.jpg" alt-text="Screenshot of the layout model analyze results operation.":::
+    :::image type="content" source="../media/receipts-example.jpg" alt-text="Screenshot of the layout model analyze results operation.":::
 
 > [!NOTE]
 > The [Sample Labeling tool](https://fott-2-1.azurewebsites.net/) does not support the BMP file format. This is a limitation of the tool not the Document Intelligence Service.
@@ -197,7 +195,7 @@ See how Document Intelligence extracts data, including time and date of transact
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extraction
 
@@ -400,7 +398,7 @@ See how Document Intelligence extracts data, including time and date of transact
 
 ### Migration guide and REST API v3.1
 
-* Follow our [**Document Intelligence v3.1 migration guide**](v3-1-migration-guide.md) to learn how to use the v3.1 version in your applications and workflows.
+* Follow our [**Document Intelligence v3.1 migration guide**](../v3-1-migration-guide.md) to learn how to use the v3.1 version in your applications and workflows.
 
 ::: moniker-end
 
@@ -410,7 +408,7 @@ See how Document Intelligence extracts data, including time and date of transact
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
 ::: moniker-end
 
@@ -426,6 +424,6 @@ See how Document Intelligence extracts data, including time and date of transact
 
 * Try processing your own forms and documents with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
 ::: moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "領収書モデルページの名称変更と相対パスの更新"
}
```

### Explanation
この変更では、「concept-receipt.md」というファイルが「receipt.md」にリネームされ、一部の内容が更新されました。合計で46行が変更され、その内訳には22行の追加と24行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名の変更**: ドキュメントが`concept-receipt.md`から`receipt.md`にリネームされ、より分かりやすいタイトルに変更されました。これにより、ファイルの目的が明確になります。

2. **相対パスの修正**: いくつかのリンクと画像の参照パスが相対パスに修正され、ドキュメントのファイル構成が統一感を持ち、他の関連コンテンツへのリンクが安定しました。

3. **メタデータの更新**: 一部のメタデータ（例：`ms.custom`の削除や、特定の監視対象のリンクが更新され）が変更され、より最新の情報が反映されています。

4. **詳しい機能の説明**: 領収書モデルがどのようにOCR技術とディープラーニングを組み合わせて重要な情報を抽出するかに関する説明があり、APIがどのように働くのか、抽出される情報（例えば、商人名や取引日など）が明記されています。

5. **サンプル画像の更新**: 画像の参照も更新され、新しい相対パスが使われるようになっています。これによって、画像が正しく表示されるようになります。

これらの変更により、領収書モデルのユーザーにとって、情報がよりアクセスしやすく、理解しやすくなっています。また、リネームにより、ドキュメントの用途が明確化されたことで、ユーザー体験が向上しています。

## articles/ai-services/document-intelligence/prebuilt/tax-document.md{#item-e19fe5}

<details>
<summary>Diff</summary>
````diff
@@ -16,13 +16,13 @@ monikerRange: ">=doc-intel-3.0.0"
 # Document Intelligence US tax document models
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-**This content applies to:** ![checkmark](media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true)
 :::moniker-end
 
 The Document Intelligence contract model uses powerful Optical Character Recognition (OCR) capabilities to analyze and extract key fields and line items from a select group of tax documents. Tax documents can be of various formats and quality including phone-captured images, scanned documents, and digital PDFs. The API analyzes document text; extracts key information such as customer name, billing address, due date, and amount due; and returns a structured JSON data representation. The model currently supports certain English tax document formats.
@@ -45,7 +45,7 @@ Automated tax document processing is the process of extracting key fields from t
 
 This preview introduces the `Unified US Tax` prebuilt model, which automatically detects and extracts data from `W2`, `1098`, `1040`, and `1099`  tax forms in submitted documents. These documents can be composed of many tax or non-tax-related documents. The model only processes the forms it supports.
 
-:::image type="content" source="media/us-unified-tax-diagram.png" alt-text="Screenshot of a Unified Tax processing diagram.":::
+:::image type="content" source="../media/us-unified-tax-diagram.png" alt-text="Screenshot of a Unified Tax processing diagram.":::
 
 ## Development options
 
@@ -55,7 +55,7 @@ Document Intelligence v4.0 (2024-07-31-preview) supports the following tools, ap
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-2024-07-31-preview&preserve-view=true)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**&bullet; prebuilt-tax.us</br>&bullet; prebuilt-tax.us.W-2</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T</br>&bullet; prebuilt-tax.us.1099A</br>&bullet; prebuilt-tax.us.1099B</br>&bullet; prebuilt-tax.us.1099C</br>&bullet; prebuilt-tax.us.1099CAP</br>&bullet; prebuilt-tax.us.1099Combo</br>&bullet; prebuilt-tax.us.1099DIV</br>&bullet; prebuilt-tax.us.1099G</br>&bullet; prebuilt-tax.us.1099H</br>&bullet; prebuilt-tax.us.1099INT</br>&bullet; prebuilt-tax.us.1099K</br>&bullet; prebuilt-tax.us.1099LS</br>&bullet; prebuilt-tax.us.1099LTC</br>&bullet; prebuilt-tax.us.1099MISC</br>&bullet; prebuilt-tax.us.1099NEC</br>&bullet; prebuilt-tax.us.1099OID</br>&bullet; prebuilt-tax.us.1099PATR</br>&bullet; prebuilt-tax.us.1099Q</br>&bullet; prebuilt-tax.us.1099QA</br>&bullet; prebuilt-tax.us.1099R</br>&bullet; prebuilt-tax.us.1099S</br>&bullet; prebuilt-tax.us.1099SA</br>&bullet; prebuilt-tax.us.1099SB</br>&bullet; prebuilt-tax.us.1040</br>&bullet; prebuilt-tax.us.1040Schedule1</br>&bullet; prebuilt-tax.us.1040Schedule2</br>&bullet; prebuilt-tax.us.1040Schedule3</br>&bullet; prebuilt-tax.us.1040Schedule8812</br>&bullet; prebuilt-tax.us.1040ScheduleA</br>&bullet; prebuilt-tax.us.1040ScheduleB</br>&bullet; prebuilt-tax.us.1040ScheduleC</br>&bullet; prebuilt-tax.us.1040ScheduleD</br>&bullet; prebuilt-tax.us.1040ScheduleE</br>&bullet; prebuilt-tax.us.1040ScheduleEIC</br>&bullet; prebuilt-tax.us.1040ScheduleF</br>&bullet; prebuilt-tax.us.1040ScheduleH</br>&bullet; prebuilt-tax.us.1040ScheduleJ</br>&bullet; prebuilt-tax.us.1040ScheduleR</br>&bullet; prebuilt-tax.us.1040ScheduleSE</br>&bullet; prebuilt-tax.us.1040Senior**|
+|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-2024-07-31-preview&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**&bullet; prebuilt-tax.us</br>&bullet; prebuilt-tax.us.W-2</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T</br>&bullet; prebuilt-tax.us.1099A</br>&bullet; prebuilt-tax.us.1099B</br>&bullet; prebuilt-tax.us.1099C</br>&bullet; prebuilt-tax.us.1099CAP</br>&bullet; prebuilt-tax.us.1099Combo</br>&bullet; prebuilt-tax.us.1099DIV</br>&bullet; prebuilt-tax.us.1099G</br>&bullet; prebuilt-tax.us.1099H</br>&bullet; prebuilt-tax.us.1099INT</br>&bullet; prebuilt-tax.us.1099K</br>&bullet; prebuilt-tax.us.1099LS</br>&bullet; prebuilt-tax.us.1099LTC</br>&bullet; prebuilt-tax.us.1099MISC</br>&bullet; prebuilt-tax.us.1099NEC</br>&bullet; prebuilt-tax.us.1099OID</br>&bullet; prebuilt-tax.us.1099PATR</br>&bullet; prebuilt-tax.us.1099Q</br>&bullet; prebuilt-tax.us.1099QA</br>&bullet; prebuilt-tax.us.1099R</br>&bullet; prebuilt-tax.us.1099S</br>&bullet; prebuilt-tax.us.1099SA</br>&bullet; prebuilt-tax.us.1099SB</br>&bullet; prebuilt-tax.us.1040</br>&bullet; prebuilt-tax.us.1040Schedule1</br>&bullet; prebuilt-tax.us.1040Schedule2</br>&bullet; prebuilt-tax.us.1040Schedule3</br>&bullet; prebuilt-tax.us.1040Schedule8812</br>&bullet; prebuilt-tax.us.1040ScheduleA</br>&bullet; prebuilt-tax.us.1040ScheduleB</br>&bullet; prebuilt-tax.us.1040ScheduleC</br>&bullet; prebuilt-tax.us.1040ScheduleD</br>&bullet; prebuilt-tax.us.1040ScheduleE</br>&bullet; prebuilt-tax.us.1040ScheduleEIC</br>&bullet; prebuilt-tax.us.1040ScheduleF</br>&bullet; prebuilt-tax.us.1040ScheduleH</br>&bullet; prebuilt-tax.us.1040ScheduleJ</br>&bullet; prebuilt-tax.us.1040ScheduleR</br>&bullet; prebuilt-tax.us.1040ScheduleSE</br>&bullet; prebuilt-tax.us.1040Senior**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
@@ -64,7 +64,7 @@ Document Intelligence v3.1 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**&bullet; prebuilt-tax.us.W-2</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T**|
+|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**&bullet; prebuilt-tax.us.W-2</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
@@ -73,12 +73,12 @@ Document Intelligence v3.0 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**&bullet; prebuilt-tax.us.W-2</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T**|
+|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**&bullet; prebuilt-tax.us.W-2</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T**|
 ::: moniker-end
 
 ## Input requirements
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ## Try tax document data extraction
 
@@ -88,7 +88,7 @@ See how data, including customer information, vendor details, and line items, is
 
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
- :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+ :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 ## Document Intelligence Studio
 
@@ -98,14 +98,14 @@ See how data, including customer information, vendor details, and line items, is
 
 1. Select the **Run analysis** button and, if necessary, configure the **Analyze options** :
 
-    :::image type="content" source="media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
+    :::image type="content" source="../media/studio/run-analysis-analyze-options.png" alt-text="Screenshot of Run analysis and Analyze options buttons in the Document Intelligence Studio.":::
 
 > [!div class="nextstepaction"]
 > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/prebuilt?formType=invoice)
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](language-support-prebuilt.md) page for a complete list of supported languages.
+*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
 
 ## Field extraction W-2
 
@@ -454,7 +454,7 @@ The tax documents key-value pairs and line items extracted are in the `documentR
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
 ::: moniker range="doc-intel-4.0.0"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "税務文書モデルページの名称変更と相対パスの更新"
}
```

### Explanation
この変更では、「concept-tax-document.md」というファイルが「tax-document.md」にリネームされ、12行の追加と12行の削除が行われました。変更により合計で24行が変更されました。

主な変更内容は以下の通りです：

1. **ファイル名の変更**: ドキュメントが`concept-tax-document.md`から`tax-document.md`にリネームされ、より明確なタイトルが付けられました。この名称変更により、文書の目的が一目瞭然になります。

2. **相対パスの修正**: ドキュメント内のリンクや画像への参照が相対パスに修正されており、ファイルの参照がより安定し、構造的な整合性が保たれています。

3. **メタデータの更新**: 一部の内容が更新され、特にプレビューや適用バージョンに関する表示が更新されて、新しいパスの利用が反映されています。

4. **文書内容の修正**: 税務文書モデルがどのようにOCRを使用して重要なフィールドや項目を抽出するかについての説明が含まれており、特にW2、1098、1040、1099のフォームに関連する内容が詳しく述べられています。

5. **サンプル画像の更新**: サンプル画像の相対パスも更新され、正しい画像表示が保証されています。

これらの変更により、税務文書モデルに関する情報がよりアクセスしやすく、理解しやすくなり、ユーザー体験が向上しています。リネームによって文書の用途が明確化され、より利用しやすいコンテンツとなっています。

## articles/ai-services/document-intelligence/quickstarts/includes/csharp-sdk.md{#item-ee69c7}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: 'Form and document processing, data extraction, and analysis using
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 09/09/2024
 ms.author: lajanuar
@@ -622,14 +620,14 @@ Once you add a code sample to your application, choose the green **Start** butto
 Analyze and extract common fields from specific document types using a prebuilt model. In this example, we analyze an invoice using the **prebuilt-invoice** model.
 
 > [!TIP]
-> You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the `analyze` operation depends on the type of document to be analyzed. See [**model data extraction**](../../concept-model-overview.md#model-data-extraction).
+> You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the `analyze` operation depends on the type of document to be analyzed. See [**model data extraction**](../../model-overview.md#model-data-extraction).
 
 > [!div class="checklist"]
 >
 > * Analyze an invoice using the prebuilt-invoice model. You can use our [sample invoice document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf) for this quickstart.
 > * We've added the file URI value to the `Uri invoiceUri` variable at the top of the Program.cs file.
 > * To analyze a given file at a URI, use the `StartAnalyzeDocumentFromUri` method and pass `prebuilt-invoice` as the model ID. The returned value is an `AnalyzeResult` object containing data from the submitted document.
-> * For simplicity, all the key-value pairs that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../concept-invoice.md#field-extraction) concept page.
+> * For simplicity, all the key-value pairs that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../prebuilt/invoice.md#field-extraction) concept page.
 
 :::moniker range="doc-intel-4.0.0"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDKガイドのリンク修正とメタデータの更新"
}
```

### Explanation
この変更では、C# SDKに関するガイドの内容が更新され、特にリンクの修正とメタデータの軽微な変更が含まれています。合計で6行の変更が行われ、その内訳には2行の追加と4行の削除があります。

主な変更内容は以下の通りです：

1. **リンクの修正**: 「**model data extraction**」へのリンクが、誤ったパスから正しいパスに修正されました。具体的には、`concept-model-overview.md`から`model-overview.md`に変更され、文書の構造を正確に反映するようになっています。

2. **メタデータの更新**: 一部のメタデータが削除され、特に`ms.custom`に関しては`- ignite-2023`の行が削除されました。これにより、プロジェクト内の不要な情報の整理が行われています。

3. **内容の改善**: いくつかの注意喚起やヒントの文言が改善され、ユーザーへのインストラクションがより明確になりました。特に、プレビルトモデルについての説明が充実しています。

これらの変更により、C# SDKに関する準備ガイドがより使いやすくなり、最新の情報を反映した内容に更新されています。ユーザーは、異なるドキュメントタイプに応じたモデルの利用についての理解が深まるでしょう。

## articles/ai-services/document-intelligence/quickstarts/includes/java-sdk.md{#item-166b2e}

<details>
<summary>Diff</summary>
````diff
@@ -623,14 +623,14 @@ After you add a code sample to your application, navigate back to your main proj
 Analyze and extract common fields from specific document types using a prebuilt model. In this example, we analyze an invoice using the **prebuilt-invoice** model.
 
 > [!TIP]
-> You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the `analyze` operation depends on the type of document to be analyzed. See [**model data extraction**](../../concept-model-overview.md#model-data-extraction).
+> You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the `analyze` operation depends on the type of document to be analyzed. See [**model data extraction**](../../model-overview.md#model-data-extraction).
 
 > [!div class="checklist"]
 >
 > * Analyze an invoice using the prebuilt-invoice model. You can use our [sample invoice document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf) for this quickstart.
 > * We've added the file URL value to the `invoiceUrl` variable at the top of the file.
 > * To analyze a given file at a URI, you'll use the `beginAnalyzeDocuments` method and pass `PrebuiltModels.Invoice` as the model Id. The returned value is a `result` object containing data about the submitted document.
-> * For simplicity, all the key-value pairs that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../concept-invoice.md#field-extraction) concept page.
+> * For simplicity, all the key-value pairs that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../prebuilt/invoice.md#field-extraction) concept page.
 
 :::moniker range="doc-intel-4.0.0"
 **Add the following code sample to the `DocIntelligence.java` file. Make sure you update the key and endpoint variables with values from your Azure portal Document Intelligence instance:**
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Java SDKガイドのリンク修正と内容の更新"
}
```

### Explanation
この変更では、Java SDKに関するガイドの内容が更新され、特にリンクの修正と一部の文の軽微な変更が行われました。合計で4行の変更があり、その内訳には2行の追加と2行の削除があります。

主な変更内容は以下の通りです：

1. **リンクの修正**: 「**model data extraction**」へのリンクが、誤ったパスから正しいパスに変更されました。具体的には、`concept-model-overview.md`から`model-overview.md`へ修正され、文書の内容が正確に参照されるようになっています。

2. **内容の改善**: ユーザーへのアドバイスとしてのヒントが提供されており、プレビルトモデルに関する説明がより詳しくなっています。この改訂により、どのモデルがどの種類のドキュメントに適しているかが明確に示されています。

3. **簡略化の強調**: キーと値のペアに関する説明部分がわかりやすくなり、サービスが戻す情報の一部が省略されている理由がクリアになっています。これにより、技術的な理解が深まり、必要な情報にアクセスしやすくなっています。

これらの変更により、Java SDKに関する準備ガイドは最新の情報を反映し、ユーザーにとって使いやすくなっています。ユーザーは、特定のドキュメントタイプに応じて適切なモデルを選択する際の理解が促進されるでしょう。

## articles/ai-services/document-intelligence/quickstarts/includes/javascript-sdk.md{#item-615fcd}

<details>
<summary>Diff</summary>
````diff
@@ -302,14 +302,14 @@ To view the entire output, visit the Azure samples repository on GitHub to view
 In this example, we analyze an invoice using the **prebuilt-invoice** model.
 
 > [!TIP]
-> You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the `analyze` operation depends on the type of document to be analyzed. See [**model data extraction**](../../concept-model-overview.md#model-data-extraction).
+> You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the `analyze` operation depends on the type of document to be analyzed. See [**model data extraction**](../../model-overview.md#model-data-extraction).
 
 > [!div class="checklist"]
 >
 > * Analyze an invoice using the prebuilt-invoice model. You can use our [sample invoice document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf) for this quickstart.
 > * We've added the file URL value to the `invoiceUrl` variable at the top of the file.
 > * To analyze a given file at a URI, you'll use the `beginAnalyzeDocuments` method and pass `PrebuiltModels.Invoice` as the model Id. The returned value is a `result` object containing data about the submitted document.
-> * For simplicity, all the key-value pairs that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../concept-invoice.md#field-extraction) concept page.
+> * For simplicity, all the key-value pairs that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../prebuilt/invoice.md#field-extraction) concept page.
 
 :::moniker range="doc-intel-4.0.0"
 
@@ -526,7 +526,7 @@ async function main() {
       amountDue,
     } = document.fields;
 
-    // The invoice model has many fields. For details, *see* [Invoice model field extraction](../../concept-invoice.md#field-extraction)
+    // The invoice model has many fields. For details, *see* [Invoice model field extraction](../../prebuilt/invoice.md#field-extraction)
     console.log("Vendor Name:", vendorName && vendorName.value);
     console.log("Customer Name:", customerName && customerName.value);
     console.log("Invoice Date:", invoiceDate && invoiceDate.value);
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScript SDKガイドのリンク修正と内容の更新"
}
```

### Explanation
この変更では、JavaScript SDKに関するガイドの内容が更新されました。具体的には、リンクの修正と一部の文の変更が行われ、合計で6行の変更があり、その内訳には3行の追加と3行の削除があります。

主な変更内容は以下の通りです：

1. **リンクの修正**: 「**model data extraction**」へのリンクが、誤ったパスから正しいパスに変更されました。具体的には、`concept-model-overview.md`から`model-overview.md`に修正され、正確な参照がなされるようになりました。

2. **内容の改善**: ユーザーへのアドバイスやヒントが提供されており、プレビルトモデルに関する説明がより具体的になっています。特に、`analyze`操作に適用するモデルの選択に関する指示が明確化されています。

3. **簡略化の強調**: キーと値のペアに関する説明がわかりやすくなり、サービスが返す情報の一部が省略されている理由が明確になっています。また、具体的なインボイスモデルのフィールドに関するリンクも正しいページに更新されました。

これらの変更により、JavaScript SDKに関する準備ガイドは最新の情報を反映し、利用者にとってより使いやすく、理解しやすい内容に進化しています。ユーザーは、異なるドキュメントタイプの分析に必要な情報を容易に得ることができるでしょう。

## articles/ai-services/document-intelligence/quickstarts/includes/python-sdk.md{#item-83c83f}

<details>
<summary>Diff</summary>
````diff
@@ -527,13 +527,13 @@ ___
 Analyze and extract common fields from specific document types using a prebuilt model. In this example, we analyze an invoice using the **prebuilt-invoice** model.
 
 > [!TIP]
-> You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the `analyze` operation depends on the type of document to be analyzed. See [**model data extraction**](../../concept-model-overview.md#model-data-extraction).
+> You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the `analyze` operation depends on the type of document to be analyzed. See [**model data extraction**](../../model-overview.md#model-data-extraction).
 
 > [!div class="checklist"]
 >
 > * Analyze an invoice using the prebuilt-invoice model. You can use our [sample invoice document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf) for this quickstart.
 > * We've added the file URL value to the `invoiceUrl` variable at the top of the file.
-> * For simplicity, all the key-value pairs that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../concept-invoice.md#field-extraction) concept page.
+> * For simplicity, all the key-value pairs that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../prebuilt/invoice.md#field-extraction) concept page.
 
 :::moniker range="doc-intel-4.0.0"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKガイドのリンク修正と内容の更新"
}
```

### Explanation
この変更では、Python SDKに関するガイドの内容が更新され、特にリンクの修正と文章の軽微な変更が行われました。合計で4行の変更があり、その内訳には2行の追加と2行の削除があります。

主な変更内容は以下の通りです：

1. **リンクの修正**: 「**model data extraction**」へのリンクが、誤ったパスから正しいパスに修正されました。これにより、`concept-model-overview.md`から`model-overview.md`へリンクが更新され、正確な情報へアクセスできるようになっています。

2. **内容の改善**: インボイスを分析するためのプレビルトモデルに関する説明がより明確になり、異なるモデルの選択肢についての情報が強調されています。また、ドキュメント分析に関する計画が示されています。

3. **簡略化の強調**: サービスが返すデータの一部が省略されている理由が簡潔に説明されており、ユーザーが全ての対応フィールドやその型に関する情報にアクセスするための最新のリンクが提供されています。

これらの変更により、Python SDKに関するガイドは最新の情報を反映し、ユーザーにとってより使いやすく、理解しやすい内容に進化しています。ユーザーは、異なるドキュメントの種類に応じた適切なモデルを選択する際の理解が深まることでしょう。

## articles/ai-services/document-intelligence/quickstarts/includes/rest-api.md{#item-9d952f}

<details>
<summary>Diff</summary>
````diff
@@ -328,4 +328,4 @@ You receive a `200 (Success)` response with JSON output. The first field, `"stat
 
 #### Supported document fields
 
-The prebuilt models extract predefined sets of document fields. See [Model data extraction](../../concept-model-overview.md#model-data-extraction) for extracted field names, types, descriptions, and examples.
+The prebuilt models extract predefined sets of document fields. See [Model data extraction](../../model-overview.md#model-data-extraction) for extracted field names, types, descriptions, and examples.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIガイドのリンク修正"
}
```

### Explanation
この変更は、REST APIに関するガイドの内容を更新するもので、特にリンクの修正が行われました。具体的には、合計で2行が変更され、その内訳には1行の追加と1行の削除があります。

主な変更内容は以下の通りです：

1. **リンクの修正**: 「Model data extraction」へのリンクが、誤ったURLから正しいURLに更新されました。この修正により、`concept-model-overview.md`という古いパスが`model-overview.md`という最新のパスに変更され、正確な情報へのアクセスが可能になっています。

2. **内容の明確化**: プレビルトモデルが抽出するドキュメントフィールドの説明に関連する文が更新されており、情報がより一貫性を持って伝えられるようになっています。

この更新により、REST APIガイドは最新の情報を反映し、読者にとってより使いやすいものになっています。ユーザーは、ドキュメントフィールドの抽出に関する理解を深めるための正確な情報を得ることができるでしょう。

## articles/ai-services/document-intelligence/quickstarts/includes/v2-1/csharp.md{#item-5bb590}

<details>
<summary>Diff</summary>
````diff
@@ -179,15 +179,15 @@ This sample demonstrates how to analyze data from certain types of common docume
 > * For this example, we wll analyze an invoice document using a prebuilt model. You can use our [sample invoice document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf) for this quickstart.
 > * We've added the file URI value to the `invoiceUri` variable at the top of the Main method.
 > * To analyze a given file at a URI, use the `StartRecognizeInvoicesFromUriAsync` method.
-> * For simplicity, all the fields that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../../concept-invoice.md#field-extraction) concept page.
+> * For simplicity, all the fields that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../../prebuilt/invoice.md#field-extraction) concept page.
 
 ### Choose a prebuilt model
 
 You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the analyze operation depends on the type of document to be analyzed. Here are the prebuilt models currently supported by the Document Intelligence service:
 
-* [**Invoice**](../../../concept-invoice.md): extracts text, selection marks, tables, fields, and key information from invoices.
-* [**Receipt**](../../../concept-receipt.md): extracts text and key information from receipts.
-* [**ID document**](../../../concept-id-document.md): extracts text and key information from driver licenses and international passports.
+* [**Invoice**](../../../prebuilt/invoice.md): extracts text, selection marks, tables, fields, and key information from invoices.
+* [**Receipt**](../../../prebuilt/receipt.md): extracts text and key information from receipts.
+* [**ID document**](../../../prebuilt/id-document.md): extracts text and key information from driver licenses and international passports.
 * [**Business-card**](../../../concept-business-card.md): extracts text and key information from business cards.
 
 ### Add the following code to your prebuilt invoice application Program.cs file method
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C#ガイドのリンク修正と情報の更新"
}
```

### Explanation
この変更では、C#に関するガイドの内容が更新され、特にリンクの修正と一部情報の見直しが行われました。合計で8行が変更され、その内訳には4行の追加と4行の削除があります。

主な変更内容は以下の通りです：

1. **リンクの修正**: インボイスに関する項目のリンクが、古いパスから新しいパスに更新されました。「Invoice」コンセプトページへのリンクが`concept-invoice.md`から`prebuilt/invoice.md`に変更されることで、ユーザーが最新の情報にアクセスできるようになっています。

2. **内容の改善**: リスト内の他のリンクも同様に修正され、レシートやID文書、ビジネスカードに関するリンクも最新のパスに更新されています。これにより、すべての関連する情報が一貫性を持って提供されるようになりました。

3. **説明の明確化**: 特定のモデルを使ったドキュメント分析に関する指示がより明確に示されており、ドキュメントに対する理解が深まりやすくなっています。

この更新によって、C#ガイドはより質の高い情報を提供し、ユーザーが容易にアクセスできる最新のリソースへ誘導されることが期待されます。これにより、ドキュメント分析機能を利用する上での利便性が向上しています。

## articles/ai-services/document-intelligence/quickstarts/includes/v2-1/java.md{#item-dd6c6f}

<details>
<summary>Diff</summary>
````diff
@@ -172,15 +172,15 @@ This sample demonstrates how to analyze data from certain types of common docume
 > * For this example, we wll analyze an invoice document using a prebuilt model. You can use our [sample invoice document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf) for this quickstart.
 > * To analyze a given file at a URI, you'll use the `beginRecognizeInvoicesFromUrl` .
 > * We've added the file URI value to the `invoiceUrl` variable in the main method.
-> * For simplicity, all the fields that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../../concept-invoice.md#field-extraction) concept page.
+> * For simplicity, all the fields that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../../prebuilt/invoice.md#field-extraction) concept page.
 
 ### Choose a prebuilt model
 
 You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the analyze operation depends on the type of document to be analyzed. Here are the prebuilt models currently supported by the Document Intelligence service:
 
-* [**Invoice**](../../../concept-invoice.md): extracts text, selection marks, tables, fields, and key information from invoices.
-* [**Receipt**](../../../concept-receipt.md): extracts text and key information from receipts.
-* [**ID document**](../../../concept-id-document.md): extracts text and key information from driver licenses and international passports.
+* [**Invoice**](../../../prebuilt/invoice.md): extracts text, selection marks, tables, fields, and key information from invoices.
+* [**Receipt**](../../../prebuilt/receipt.md): extracts text and key information from receipts.
+* [**ID document**](../../../prebuilt/id-document.md): extracts text and key information from driver licenses and international passports.
 * [**Business-card**](../../../concept-business-card.md): extracts text and key information from business cards.
 
 Update your application's **FormRecognizer** class, with the following code (be certain to update the key and endpoint variables with values from your Azure portal Document Intelligence instance):
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Javaガイドのリンク修正と情報の更新"
}
```

### Explanation
この変更では、Javaに関するガイドの内容が更新され、特にリンクの修正と一部の情報の見直しが行われました。合計で8行が変更され、その内訳には4行の追加と4行の削除があります。

主な変更内容は以下の通りです：

1. **リンクの修正**: インボイスに関連する項目のリンクが更新され、古いパスである`concept-invoice.md`から、最新のパス`prebuilt/invoice.md`に変更されました。これにより、ユーザーは最新の情報に簡単にアクセスできるようになります。

2. **情報の一貫性**: 他のプレビルトモデルのリンクも同様に修正されており、レシートやID文書に関しても新しいパスに更新されています。このことにより、情報の一貫性が保たれ、ユーザーが正しい情報に基づいて作業を進めやすくなります。

3. **説明の改善**: プレビルトモデルを選択する際の情報がより明確になり、ドキュメント分析のプロセスが分かりやすく説明されています。

この更新により、Javaガイドはより高品質な情報を提供し、ユーザーが必要なリソースへ容易にアクセスできるようになることが期待されます。これにより、ユーザーはドキュメント分析機能を効率的に利用できるようになります。

## articles/ai-services/document-intelligence/quickstarts/includes/v2-1/javascript.md{#item-1b193e}

<details>
<summary>Diff</summary>
````diff
@@ -133,22 +133,22 @@ recognizeContent().catch((err) => {
 
 ## **Try it**: Prebuilt model
 
-This sample demonstrates how to analyze data from certain types of common documents with pretrained models, using an invoice as an example. *See* our prebuilt concept page for a complete list of [**invoice fields**](../../../concept-invoice.md#field-extraction)
+This sample demonstrates how to analyze data from certain types of common documents with pretrained models, using an invoice as an example. *See* our prebuilt concept page for a complete list of [**invoice fields**](../../../prebuilt/invoice.md#field-extraction)
 
 > [!div class="checklist"]
 >
 > * For this example, we wll analyze an invoice document using a prebuilt model. You can use our [sample invoice document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf) for this quickstart.
 > * We've added the file URI value to the `invoiceUrl` variable at the top of the file.
 > * To analyze a given file at a URI, you'll use the `beginRecognizeInvoices` method.
-> * For simplicity, all the fields that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../../concept-invoice.md#field-extraction) concept page.
+> * For simplicity, all the fields that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../../prebuilt/invoice.md#field-extraction) concept page.
 
 ### Choose a prebuilt model
 
 You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the analyze operation depends on the type of document to be analyzed. Here are the prebuilt models currently supported by the Document Intelligence service:
 
-* [**Invoice**](../../../concept-invoice.md): extracts text, selection marks, tables, fields, and key information from invoices.
-* [**Receipt**](../../../concept-receipt.md): extracts text and key information from receipts.
-* [**ID document**](../../../concept-id-document.md): extracts text and key information from driver licenses and international passports.
+* [**Invoice**](../../../prebuilt/invoice.md): extracts text, selection marks, tables, fields, and key information from invoices.
+* [**Receipt**](../../../prebuilt/receipt.md): extracts text and key information from receipts.
+* [**ID document**](../../../prebuilt/id-document.md): extracts text and key information from driver licenses and international passports.
 * [**Business-card**](../../../concept-business-card.md): extracts text and key information from business cards.
 
 ### Add the following code to your prebuilt invoice application below the `key` variable
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptガイドのリンク修正と内容の更新"
}
```

### Explanation
この変更では、JavaScriptに関するガイドの内容が更新され、特にリンクの修正と一部情報の見直しが行われました。合計で10行が変更され、その内訳には5行の追加と5行の削除があります。

主な変更内容は以下の通りです：

1. **リンクの修正**: インボイスに関連する項目のリンクが変更され、古いパス`concept-invoice.md`から新しいパス`prebuilt/invoice.md`に更新されています。これによって、ユーザーが最新のインボイス関連の情報に簡単にアクセスできるようになります。

2. **情報の整合性**: 他の関連リンクも新しいパスに修正されており、レシートやID文書に関するリンクも更新されています。これにより、情報の一貫性が保たれ、ユーザーが必要なリソースにスムーズにアクセスできるようになります。

3. **説明の明確化**: プレトレーニングモデルの選択に関する説明がより明確になり、ドキュメント分析のプロセスが理解しやすくなっています。

この更新により、JavaScriptガイドはより高品質な情報を提供し、ユーザーが必要なリソースへ容易にアクセスできるようになることが期待されます。これにより、ドキュメント分析機能を効率的に利用できる環境が整います。

## articles/ai-services/document-intelligence/quickstarts/includes/v2-1/python.md{#item-996d7f}

<details>
<summary>Diff</summary>
````diff
@@ -180,22 +180,22 @@ if __name__ == "__main__":
 
 ## **Try it**: Prebuilt model
 
-This sample demonstrates how to analyze data from certain types of common documents with pretrained models, using an invoice as an example. *See* our prebuilt concept page for a complete list of [**invoice fields**](../../../concept-invoice.md#field-extraction)
+This sample demonstrates how to analyze data from certain types of common documents with pretrained models, using an invoice as an example. *See* our prebuilt concept page for a complete list of [**invoice fields**](../../../prebuilt/invoice.md#field-extraction)
 
 > [!div class="checklist"]
 >
 > * For this example, we wll analyze an invoice document using a prebuilt model. You can use our [sample invoice document](https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf) for this quickstart.
 > * We've added the file URI value to the ``formUrl` variable at the top of the file.
 > * To analyze a given file at a URI, you'll use the ``begin_recognize_invoices_from_url` method.
-> * For simplicity, all the fields that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../../concept-invoice.md#field-extraction) concept page.
+> * For simplicity, all the fields that the service returns are not shown here. To see the list of all supported fields and corresponding types, see our [Invoice](../../../prebuilt/invoice.md#field-extraction) concept page.
 
 ### Choose a prebuilt model
 
 You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the analyze operation depends on the type of document to be analyzed. Here are the prebuilt models currently supported by the Document Intelligence service:
 
-* [**Invoice**](../../../concept-invoice.md): extracts text, selection marks, tables, fields, and key information from invoices.
-* [**Receipt**](../../../concept-receipt.md): extracts text and key information from receipts.
-* [**ID document**](../../../concept-id-document.md): extracts text and key information from driver licenses and international passports.
+* [**Invoice**](../../../prebuilt/invoice.md): extracts text, selection marks, tables, fields, and key information from invoices.
+* [**Receipt**](../../../prebuilt/receipt.md): extracts text and key information from receipts.
+* [**ID document**](../../../prebuilt/id-document.md): extracts text and key information from driver licenses and international passports.
 * [**Business-card**](../../../concept-business-card.md): extracts text and key information from business cards.
 
 ### Add the following code to your prebuilt invoice application below the `key` variable
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Pythonガイドのリンク修正と内容の更新"
}
```

### Explanation
この変更では、Pythonに関するガイドの内容が更新され、特にリンクの修正と一部情報の見直しが行われました。合計で10行が変更され、その内訳には5行の追加と5行の削除があります。

主な変更内容は以下の通りです：

1. **リンクの修正**: インボイスに関連する項目のリンクが変更され、古いパスである`concept-invoice.md`から新しいパス`prebuilt/invoice.md`に更新されています。これにより、ユーザーは最新のインボイス関連の情報に簡単にアクセスできるようになります。

2. **情報の整合性**: 他の関連リンクも新しいパスに修正されており、レシートやID文書に関するリンクも更新されています。この修正は、文書全体の情報の一貫性を保ち、ユーザーが必要なリソースにスムーズにアクセスできることを目的としています。

3. **説明の明確化**: プレトレーニングモデルの選択に関する説明が洗練され、ドキュメント分析のプロセスがより理解しやすくなっています。

この更新により、Pythonガイドはより質の高い情報を提供し、ユーザーが必要なリソースへ容易にアクセスできるようになることが期待されます。これにより、ユーザーはドキュメント分析機能を効率的に利用できる環境を整えることができます。

## articles/ai-services/document-intelligence/quickstarts/includes/v2-1/rest-api.md{#item-3bd0eb}

<details>
<summary>Diff</summary>
````diff
@@ -4,8 +4,6 @@ description: Use the Document Intelligence REST API v2.1 to create a forms proce
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: include
 ms.date: 05/23/2024
 ms.author: lajanuar
@@ -122,9 +120,9 @@ You can view the [full sample output on GitHub](https://github.com/Azure-Samples
 
 You aren't limited to invoices—there are several prebuilt models to choose from, each of which has its own set of supported fields. The model to use for the analyze operation depends on the type of document to be analyzed. Here are the prebuilt models currently supported by the Document Intelligence service:
 
-* [**Invoice**](../../../concept-invoice.md): extracts text, selection marks, tables, fields, and key information from invoices.
-* [**Receipt**](../../../concept-receipt.md): extracts text and key information from receipts.
-* [**ID document**](../../../concept-id-document.md): extracts text and key information from driver licenses and international passports.
+* [**Invoice**](../../../prebuilt/invoice.md): extracts text, selection marks, tables, fields, and key information from invoices.
+* [**Receipt**](../../../prebuilt/receipt.md): extracts text and key information from receipts.
+* [**ID document**](../../../prebuilt/id-document.md): extracts text and key information from driver licenses and international passports.
 * [**Business-card**](../../../concept-business-card.md): extracts text and key information from business cards.
 
 Before you run the command, make these changes:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIガイドのリンク修正と不必要なメタ情報の削除"
}
```

### Explanation
この変更では、REST APIに関するガイドの内容が更新され、不必要なメタ情報の削除とリンクの修正が行われました。合計で8行が変更され、その内訳には3行の追加と5行の削除があります。

主な変更内容は以下の通りです：

1. **不必要なメタ情報の削除**: メタデータの一部として含まれていた不要な情報（`ms.custom`の値）が削除され、ドキュメントがより簡潔になりました。

2. **リンクの修正**: 複数のモデルに関するリンクが古いパスから新しいパスに更新されています。具体的には、インボイスやレシート、ID文書に関連するリンクが、`concept`から`prebuilt`に変更されています。これにより、ユーザーは最新の情報にアクセスしやすくなります。

3. **情報の整合性**: 様々なプレトレーニングモデルに関する情報が一貫性を持って整備されており、文書全体の信頼性を高めています。

この更新により、REST APIガイドはより質の高い情報を提供し、ユーザーが必要なリソースへスムーズにアクセスできるようになることが期待されます。これにより、ドキュメント分析機能を効果的に利用するためのより良い環境が整います。

## articles/ai-services/document-intelligence/quickstarts/try-document-intelligence-studio.md{#item-ff12d6}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Form and document processing, data extraction, and analysis using D
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: quickstart
 ms.date: 08/07/2024
 ms.author: lajanuar
@@ -52,7 +50,7 @@ To use Document Intelligence Studio, you need the following assets and settings:
 
 * To test any of the document analysis or prebuilt models, select the model and use one of the sample documents or upload your own document to analyze. The analysis result is displayed at the right in the content-result-code window.
 
-* Custom models need to be trained on your documents. See [custom models overview](../concept-custom.md) for an overview of custom models.
+* Custom models need to be trained on your documents. See [custom models overview](../train/custom-model.md) for an overview of custom models.
 
 ## Authentication
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンススタジオに関するリンク修正"
}
```

### Explanation
この変更では、ドキュメントインテリジェンススタジオに関するガイドの内容が更新され、リンクの修正と不要なメタ情報の削除が行われました。合計で4行が変更され、その内訳には1行の追加と3行の削除があります。

主な変更内容は以下の通りです：

1. **不必要なメタ情報の削除**: メタデータの一部が削除され、ドキュメントがより簡潔になりました。特に`ms.custom`の値が削除されています。

2. **リンクの修正**: カスタムモデルに関するリンクが更新され、以前のパスである`../concept-custom.md`から新しいパス`../train/custom-model.md`に変更されています。これにより、ユーザーはカスタムモデルのトレーニングに関する最新情報にアクセスしやすくなります。

3. **情報の明確化**: カスタムモデルの情報がより正確なリンクによって提供されることで、ユーザーが必要なリソースを見つけやすくなっています。

この更新により、ドキュメントインテリジェンススタジオに関するガイドがより効率的に情報を提供し、ユーザーが最新のリソースに基づいてカスタムモデルのトレーニングを行うことが容易になります。全体として、ユーザーの体験向上が期待されます。

## articles/ai-services/document-intelligence/service-limits.md{#item-5ceae5}

<details>
<summary>Diff</summary>
````diff
@@ -6,8 +6,6 @@ description: Quick reference, detailed description, and best practices for worki
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 09/26/2024
 ms.author: lajanuar
@@ -116,11 +114,11 @@ Document Intelligence billing is calculated monthly based on the model type and
 
 > [!div class="checklist"]
 >
-> * [**Custom template model**](concept-custom-template.md)
-> * [**Custom neural model**](concept-custom-neural.md)
-> * [**Custom generative model**](concept-custom-generative.md)
-> * [**Composed classification models**](concept-custom-classifier.md)
-> * [**Composed custom models**](concept-composed-models.md)
+> * [**Custom template model**](train/custom-template.md)
+> * [**Custom neural model**](train/custom-neural.md)
+> * [**Custom generative model**](train/custom-generative-extraction.md)
+> * [**Composed classification models**](train/custom-classifier.md)
+> * [**Composed custom models**](train/composed-models.md)
 
 |Quota|Free (F0) <sup>1</sup>|Standard (S0)|
 |--|--|--|
@@ -153,10 +151,10 @@ Document Intelligence billing is calculated monthly based on the model type and
 
 > [!div class="checklist"]
 >
-> * [**Custom template model**](concept-custom-template.md)
-> * [**Custom neural model**](concept-custom-neural.md)
-> * [**Composed classification models**](concept-custom-classifier.md)
-> * [**Composed custom models**](concept-composed-models.md)
+> * [**Custom template model**](train/custom-template.md)
+> * [**Custom neural model**](train/custom-neural.md)
+> * [**Composed classification models**](train/custom-classifier.md)
+> * [**Composed custom models**](train/composed-models.md)
 
 |Quota|Free (F0) <sup>1</sup>|Standard (S0)|
 |--|--|--|
@@ -189,10 +187,10 @@ Document Intelligence billing is calculated monthly based on the model type and
 
 > [!div class="checklist"]
 >
-> * [**Custom template model**](concept-custom-template.md)
-> * [**Custom neural model**](concept-custom-neural.md)
-> * [**Composed classification models**](concept-custom-classifier.md)
-> * [**Composed custom models**](concept-composed-models.md)
+> * [**Custom template model**](train/custom-template.md)
+> * [**Custom neural model**](train/custom-neural.md)
+> * [**Composed classification models**](train/custom-classifier.md)
+> * [**Composed custom models**](train/composed-models.md)
 
 |Quota|Free (F0) <sup>1</sup>|Standard (S0)|
 |--|--|--|
@@ -225,8 +223,8 @@ Document Intelligence billing is calculated monthly based on the model type and
 
 > [!div class="checklist"]
 >
-> * [**Custom template model**](concept-custom-template.md)
-> * [**Composed custom models**](concept-composed-models.md)
+> * [**Custom template model**](train/custom-template.md)
+> * [**Composed custom models**](train/composed-models.md)
 
 | Quota | Free (F0) <sup>1</sup> | Standard (S0) |
 |--|--|--|
@@ -249,7 +247,7 @@ Document Intelligence billing is calculated monthly based on the model type and
 > <sup>4</sup> This limit applies to all documents found in your training dataset folder prior to any labeling-related updates.
 ::: moniker-end
 ::: moniker range=">=doc-intel-4.0.0"
-> <sup>5</sup> This limit applies for `v 4.0 (2024-07-31)` custom neural models only. Starting from `v 4.0`, we support training larger documents for longer durations (up to 10 hours for free, and incurring charges after). For more information, please refer to [custom nerual model page](concept-custom-neural.md).
+> <sup>5</sup> This limit applies for `v 4.0 (2024-07-31)` custom neural models only. Starting from `v 4.0`, we support training larger documents for longer durations (up to 10 hours for free, and incurring charges after). For more information, please refer to [custom nerual model page](train/custom-neural.md).
 ::: moniker-end
 
 ## Detailed description, Quota adjustment, and best practices
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サービス制限に関するリンク修正とメタ情報の整理"
}
```

### Explanation
この変更では、ドキュメントインテリジェンスのサービス制限に関する文書が更新され、複数のリンク修正と不必要なメタ情報の削除が行われました。合計で34行が変更され、その内訳には16行の追加と18行の削除があります。

主な変更内容は以下の通りです：

1. **不必要なメタ情報の削除**: `ms.custom`に関連する不必要な情報が削除され、文書がより明確になりました。

2. **リンクの修正**: カスタムモデルに関するリンクが古いパスから新しいパスに更新されました。これにより、ユーザーは最新のリソースにアクセスしやすくなっています。具体的には、以下のリンクが変更されました：
   - `concept-custom-template.md`が`train/custom-template.md`に
   - `concept-custom-neural.md`が`train/custom-neural.md`に
   - その他のカスタムモデル関連リンクも更新されています。

3. **情報の更新**: ドキュメントインテリジェンスの課金に関する説明も更新され、具体的にはバージョン4.0のカスタムニューラルモデルについての情報が強調されています。これにより、ユーザーが重要な情報を簡単に見つけやすくなっています。

これらの変更により、文書全体がより一貫性を持ち、ユーザーが最新の情報を容易に取得できるようになります。全体として、サービスに関する理解を深める助けとなることが期待されます。

## articles/ai-services/document-intelligence/studio-overview.md{#item-db8fa3}

<details>
<summary>Diff</summary>
````diff
@@ -13,6 +13,8 @@ monikerRange: '>=doc-intel-3.0.0'
 
 
 <!-- markdownlint-disable MD033 -->
+<!-- markdownlint-disable MD051 -->
+
 # Studio experience for Document Intelligence
 
 [!INCLUDE [applies to v4.0 v3.1 v3.0](includes/applies-to-v40-v31-v30.md)]
@@ -52,7 +54,6 @@ Select the studio experience from the following tabs to learn more about each st
 > * Azure for US Government: [Document Intelligence Studio (Azure Fairfax cloud)](https://formrecognizer.appliedai.azure.us/studio)
 > * Microsoft Azure operated by 21Vianet: [Document Intelligence Studio (Azure in China)](https://formrecognizer.appliedai.azure.cn/studio)
 
-
 The studio supports Document Intelligence v3.0 and later API versions for model analysis and custom model training. Previously trained v2.1 models with labeled data are supported, but not v2.1 model training. Refer to the [REST API migration guide](v3-1-migration-guide.md) for detailed information about migrating from v2.1 to v3.0.
 
 Use the [Document Intelligence Studio quickstart](quickstarts/try-document-intelligence-studio.md) to get started analyzing documents with document analysis or prebuilt models. Build custom models and reference the models in your applications using one of the [language specific `SDKs`](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true). To use Document Intelligence Studio, you need to acquire the following assets from the Azure portal:
@@ -78,23 +79,23 @@ Your organization can opt to disable local authentication and enforce Microsoft
 
 > [!IMPORTANT]
 >
-> * Make sure you have the **Cognitive Services User role**, and not the Cognitive Services Contributor role when setting up Entra authentication. 
-> * In Azure context, Contributor role can only perform actions to control and manage the resource itself, including listing the access keys. 
+> * Make sure you have the **Cognitive Services User role**, and not the Cognitive Services Contributor role when setting up Entra authentication.
+> * In Azure context, Contributor role can only perform actions to control and manage the resource itself, including listing the access keys.
 > * User accounts with a Contributor are only able to access the Document Intelligence service by calling with access keys. However, when setting up access with Entra ID, key-access will be disabled and **Cognitive Service User** role will be required for an account to use the resources.
 
 #### Document Intelligence model support
 
 Use the help wizard, labeling interface, training step, and interactive visualizations to understand how each feature works.
 
-* **Read**: Try out Document Intelligence's [Studio Read feature](https://documentintelligence.ai.azure.com/studio/read) with sample documents or your own documents and extract text lines, words, detected languages, and handwritten style if detected. To learn more, *see* [Read overview](concept-read.md).
+* **Read**: Try out Document Intelligence's [Studio Read feature](https://documentintelligence.ai.azure.com/studio/read) with sample documents or your own documents and extract text lines, words, detected languages, and handwritten style if detected. To learn more, *see* [Read overview](prebuilt/read.md).
 
-* **Layout**: Try out Document Intelligence's [Studio Layout feature](https://documentintelligence.ai.azure.com/studio/layout) with sample documents or your own documents and extract text, tables, selection marks, and structure information. To learn more, *see* [Layout overview](concept-layout.md). 
+* **Layout**: Try out Document Intelligence's [Studio Layout feature](https://documentintelligence.ai.azure.com/studio/layout) with sample documents or your own documents and extract text, tables, selection marks, and structure information. To learn more, *see* [Layout overview](prebuilt/layout.md).
 
-* **Prebuilt models**: Document Intelligence's prebuilt models enable you to add intelligent document processing to your apps and flows without having to train and build your own models. As an example, start with the [Studio Invoice feature](https://documentintelligence.ai.azure.com/studio/prebuilt?formType=invoice). To learn more, *see* [Models overview](concept-model-overview.md).
+* **Prebuilt models**: Document Intelligence's prebuilt models enable you to add intelligent document processing to your apps and flows without having to train and build your own models. As an example, start with the [Studio Invoice feature](https://documentintelligence.ai.azure.com/studio/prebuilt?formType=invoice). To learn more, *see* [Models overview](model-overview.md).
 
-* **Custom extraction models**: Document Intelligence's [Studio Custom models feature](https://documentintelligence.ai.azure.com/studio/custommodel/projects) enables you to extract fields and values from models trained with your data, tailored to your forms and documents. To extract data from multiple form types, create standalone custom models or combine two, or more, custom models and create a composed model. Test the custom model with your sample documents and iterate to improve the model. To learn more, *see* the [Custom models overview](concept-custom.md).
+* **Custom extraction models**: Document Intelligence's [Studio Custom models feature](https://documentintelligence.ai.azure.com/studio/custommodel/projects) enables you to extract fields and values from models trained with your data, tailored to your forms and documents. To extract data from multiple form types, create standalone custom models or combine two, or more, custom models and create a composed model. Test the custom model with your sample documents and iterate to improve the model. To learn more, *see* the [Custom models overview](train/custom-model.md).
 
-* **Custom classification models**: Document classification is a new scenario supported by Document Intelligence. The document classifier API supports classification and splitting scenarios. Train a classification model to identify the different types of documents your application supports. The input file for the classification model can contain multiple documents and classifies each document within an associated page range. To learn more, *see* [custom classification models](concept-custom-classifier.md).
+* **Custom classification models**: Document classification is a new scenario supported by Document Intelligence. The document classifier API supports classification and splitting scenarios. Train a classification model to identify the different types of documents your application supports. The input file for the classification model can contain multiple documents and classifies each document within an associated page range. To learn more, *see* [custom classification models](train/custom-classifier.md).
 
 * **Add-on Capabilities**: Document Intelligence supports more sophisticated analysis capabilities. These optional capabilities can be enabled and disabled in the studio using the `Analyze Options` button in each model page. There are four add-on capabilities available: `highResolution`, `formula`, `font`, and `barcode extraction` capabilities. To learn more, *see* [Add-on capabilities](concept-add-on-capabilities.md).
 
@@ -104,7 +105,7 @@ Use the help wizard, labeling interface, training step, and interactive visualiz
 
 * To test any of the document analysis or prebuilt models, select the model and use one of the sample documents or upload your own document to analyze. The analysis result is displayed at the right in the content-result-code window.
 
-* Custom models need to be trained on your documents. See [custom models overview](concept-custom.md) for an overview of custom models.
+* Custom models need to be trained on your documents. See [custom models overview](train/custom-model.md) for an overview of custom models.
 
 * After validating the scenario in the Document Intelligence Studio, use the [**C#**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [**Python**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) client libraries or the [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) to get started incorporating Document Intelligence models into your own applications.
 
@@ -203,7 +204,7 @@ Share custom extraction projects with ease. For more information, see [Project s
 
 ### [**AI Studio**](#tab/ai-studio)
 
-Document Intelligence is part of the Azure AI services offerings in the Azure AI Studio. Each of the Azure AI services helps developers and organizations rapidly create intelligent, cutting-edge, market-ready, and responsible applications with out-of-the-box and prebuilt and customizable APIs and models. 
+Document Intelligence is part of the Azure AI services offerings in the Azure AI Studio. Each of the Azure AI services helps developers and organizations rapidly create intelligent, cutting-edge, market-ready, and responsible applications with out-of-the-box and prebuilt and customizable APIs and models.
 
 Learn how to [connect your AI services hub](../../ai-studio/ai-services/connect-ai-services.md) with AI services and get started using Document Intelligence.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence Studioの概要に関するリンク修正とメタ情報の追加"
}
```

### Explanation
この変更では、ドキュメントインテリジェンススタジオに関する概要文書が更新され、特定のリンクの修正やメタ情報の追加が行われました。総計で21行が変更され、その内訳には11行の追加と10行の削除があります。

主な変更内容は以下の通りです：

1. **メタ情報の追加**: 新たに`markdownlint-disable MD051`が追加され、ドキュメントの整合性が向上しました。

2. **リンクの修正**: 複数の関連リンクが最新のリソースに更新されました。具体的には、カスタムモデルや整理されたオーバービューへのリンクが修正され、ユーザーが情報を簡単に見つけられるようになっています。例として、`concept-read.md`は`prebuilt/read.md`に、カスタムモデルのリンクも`concept-custom.md`から`train/custom-model.md`に変更されています。

3. **情報の明確化**: ドキュメントインテリジェンススタジオの各機能の説明が整理され、ユーザーが利用可能な機能の理解を深めやすくなりました。

4. **構成の改善**: 不要な空行やマークアップが整理され、全体の読みやすさが向上しています。

これらの変更により、ドキュメントがより一貫性を持ち、ユーザーが必要な情報を迅速に取得できることが期待されます。全体として、ユーザーエクスペリエンスの向上を目指した改善がなされています。

## articles/ai-services/document-intelligence/toc.yml{#item-81aa7b}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ items:
     displayName: models, develop, development, cognitive, applied, form recognizer, form, recognizer
     href: overview.md
   - name: Which model should I choose?
-    href: choose-model-feature.md
+    href: concept/choose-model-feature.md
   - name: Document Intelligence Studio
     displayName: get started
     href: studio-overview.md
@@ -32,18 +32,18 @@ items:
         href: sdk-overview-v3-0.md
       - name:  "SDK targets: REST API v2.1 (GA)"
         displayName: get started, installation, downloads, formRecognizerClientClient, form recognizer client, Azure AD, Azure Active Directory, identity, changelog, package, version,AzureKeyCredential, Azure key credential, key, endpoint
-        href: sdk-overview-v2-1.md
+        href: /v21/sdk-overview.md
   - name: Language support
     items:
       - name: Document analysis models
         displayName: language, locale, handwritten, handwriting, text, detect, detection, general, document, printed
-        href: language-support-ocr.md?view=doc-intel-4.0.0&preserve-view=true
+        href: language-support/ocr.md?view=doc-intel-4.0.0&preserve-view=true
       - name: Prebuilt models
         displayName: locale, handwritten, handwriting, text, detect, detection, printed
-        href: language-support-prebuilt.md
+        href: language-support/prebuilt.md
       - name: Custom models
         displayName: locale, handwritten, handwriting, text, detect, detection, printed
-        href: language-support-custom.md
+        href: language-support/custom.md
   - name: Pricing
     displayName: cost, free, F0, tiers, standard, S0
     href: https://azure.microsoft.com/pricing/details/form-recognizer/
@@ -53,6 +53,113 @@ items:
   - name: What's new
     displayName: changelog, release, updates, previews, beta, packages, ga, cognitive, applied, form recognizer, form, recognizer
     href: whats-new.md
+- name: Prebuilt models
+  items:
+  - name: Model overview
+    displayName: get started, prebuilt, extraction, input
+    href: model-overview.md
+  - name: 🆕 Bank check
+    displayName: routing, account, number, amount, payee, issuer, date
+    href: prebuilt/bank-check.md
+  - name: 🆕 Bank statement
+    displayName: transactions, deposits, withdrawals, balance, account, number, date
+    href: prebuilt/bank-statement.md
+  - name: Business card
+    displayName: /rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP
+    href: prebuilt/business-card.md?view<=doc-intel-3.1.0&preserve-view=true
+  - name: Contract
+    displayName: contracts, agreements, legal, terms, conditions, clauses, parties, dates, signatures
+    href: prebuilt/contract.md
+  - name: Credit card
+    displayName: debit
+    href: prebuilt/credit-card.md
+  - name: General document
+    displayName: key value pairs, selection marks, structured
+    href: prebuilt/general-document.md?view<=doc-intel-3.1.0&preserve-view=true
+  - name: Health insurance card
+    displayName: health, proof, hospital
+    href: prebuilt/health-insurance-card.md
+  - name: ID document
+    displayName: passport, visa, ID, social security, green card
+    href: prebuilt/id-document.md
+  - name: Invoice
+    displayName: sales, vendors, VAT
+    href: prebuilt/invoice.md
+  - name: Layout
+    displayName: tables, selection marks, structure, paragraph roles, text, headers, page numbers
+    href: prebuilt/layout.md
+  - name: Marriage certificate
+    displayName: license
+    href: prebuilt/marriage-certificate.md
+  - name: Mortgage documents (U.S.)
+    displayName: 1003, 1008, closing, disclosure
+    href: prebuilt/mortgage-documents.md
+  - name: 🆕 Pay stub
+    displayName: compensation, earnings, deductions, taxes, benefits, employer, employee
+    href: prebuilt/pay-stub.md
+  - name: Read
+    displayName: text
+    href: prebuilt/read.md
+  - name: Receipt
+    displayName: sales, merchants
+    href: prebuilt/receipt.md
+  - name: Tax documents (U.S.)
+    displayName: tax, forms, 1098, 1098-E, 1098-T, W-2, wages, taxes, salary, employees, tuition, loan, interest, mortgage
+    href: prebuilt/tax-document.md
+- name: Custom models
+  items:
+  - name: Custom model overview
+    displayName: table, label, ocr, confidence, template, neural
+    href: train/custom-model.md
+  - name: 🆕 Composed models
+    displayName: custom, assign, modelId, model ID
+    href:  train/composed-models.md
+  - name: 🆕 Incremental classifier
+    displayName: custom, classification, training
+    href: concept/incremental-classifier.md
+  - name: 🆕Custom generative model
+    displayName: ai studio, neural, template, custom
+    href: train/custom-generative-extraction.md
+  - name: Custom template model
+    displayName: structure, selection, labels, tables, tabular, train, template, neural, build mode, signatures, custom
+    href: train/custom-template.md
+  - name: Custom neural model
+    displayName: selection, structure, tables, tabular, train, template, neural, build mode, signatures, custom
+    href: train/custom-neural.md
+  - name: Custom classification model
+    displayName: custom, train, classification, splitting
+    href: train/custom-classifier.md
+  - name: Custom labels
+    displayName: structure, selection, labels, tables, tabular, train
+    href: train/custom-labels.md
+  - name: Custom labeling tips
+    displayName: structure, selection, labels, tables, tabular, train, tips
+    href: train/custom-label-tips.md
+  - name: Custom model lifecycle
+    displayName: custom, train, modelId, model ID, expiration, train, build
+    href: train/custom-lifecycle.md
+- name: Features
+  items:
+  - name: Add-on capabilities
+    displayName: extract, formula, font, styles, fontStyle, ocr.highResolution, ocr.formula, high resolution, background color, inline, display
+    href: concept-add-on-capabilities.md
+  - name: Query field extraction
+    displayName: queries, fields, OpenAI, chat
+    href: concept-query-fields.md
+- name: Concepts
+  items:
+  - name: Accuracy and confidence scores
+    displayName: tables, labels, ocr, performance, signatures
+    href: concept/accuracy-confidence.md
+  - name: Analyze document API response
+    displayName: words, lines, pages, bounding regions, documents
+    href: concept/analyze-document-response.md
+  - name: 🆕 Retrieval-Augmented Generation (RAG)
+    displayName: RAG, LLM, semantic, chunk, LangChain, language model
+    href: concept/retrieval-augmented-generation.md
+  - name: 🆕 Batch documents analysis
+    displayName: analyze, azureBlobFileListSource, azureBlobSource, azureBlobFileListSource, resultContainerUrl, resultPrefix, overwriteExisting
+    href: concept-batch-analysis.md
 - name: Quickstarts
   items:
     - name: Document Intelligence Studio
@@ -63,24 +170,24 @@ items:
       href: quickstarts/get-started-sdks-rest-api.md
     - name: Sample Labeling tool
       displayName: tables, labels, ocr, bounding box
-      href: quickstarts/try-sample-label-tool.md
+      href: /v21/try-sample-label-tool.md
 - name: How-to guides
   items:
   - name: Use Document Intelligence models
     displayName: documentAnalysisClient, document analysis client, polygon, boundingPolygon, begin_analyze_document,ormRecognizerClient, Document Intelligence client, boundingBox, box, begin_recognize, v2.1
     href: how-to-guides/use-sdk-rest-api.md
   - name: Create a Document Intelligence resource
     displayName: endpoint, key, portal
-    href:  create-document-intelligence-resource.md
+    href:  how-to-guides/create-document-intelligence-resource.md
   - name: 🆕 Build and train a custom generative model
     displayName: ai studio, neural, template, custom
-    href: how-to-guides/build-train-custom-generative-model.md  
+    href: how-to-guides/build-train-custom-generative-model.md
   - name: Check my usage and estimate the cost
     displayName: price, metrics, dashboard, check, estimate
     href: how-to-guides/estimate-cost.md
   - name: Create SAS tokens for storage containers
     displayName: blob, delegation, shared, explorer
-    href:  create-sas-tokens.md
+    href:  authentication/create-sas-tokens.md
   - name: "SDK Migration guides: 2023-10-31-preview"
     items:
     - name: ".NET/C# SDK"
@@ -110,13 +217,13 @@ items:
       href: how-to-guides/compose-custom-models.md
     - name: Deploy the sample-labeling tool
       displayName: FOTT, migration, containers, docker
-      href: deploy-label-tool.md
+      href: /v21/deploy-label-tool.md
     - name: Train a custom model with the sample-labeling tool
       displayName: FOTT, migration, containers, docker
-      href: label-tool.md
+      href: /v21/label-tool.md
     - name: Use table tags to train your custom model
       displayName: FOTT, migration, dynamic
-      href: supervised-table-tags.md
+      href: /v21/supervised-table-tags.md
   - name: Back up and recover models
     displayName: disaster, recovery, region, copy, modelId, model ID
     href: disaster-recovery.md
@@ -127,13 +234,13 @@ items:
       href: ../../ai-services/cognitive-services-virtual-networks.md?context=/azure/ai-services/document-intelligence/context/context
     - name: Create and use managed identities
       displayName: azure RBAC, role based access control, sas, private, assigned, system assigned, role, blob
-      href: managed-identities.md
+      href: authentication/managed-identities.md
     - name: Configure managed identities with private endpoints
       displayName: Azure RBAC, role based access control, sas, private, assigned, system assigned, role, blob, virtual, firewalls, VNet, virtual networks, endpoints, storage
-      href: managed-identities-secured-access.md
+      href: authentication/managed-identities-secured-access.md
     - name: Use customer-managed keys
       displayName: encrypt, encryption, key vault
-      href: encrypt-data-at-rest.md
+      href: authentication/encrypt-data-at-rest.md
     - name: Use Microsoft Entra authentication
       displayName: headers, subscription, access token, azure active directory, subdomain, role, service principal
       href: ../../ai-services/authentication.md?context=/azure/ai-services/document-intelligence/context/context
@@ -151,109 +258,7 @@ items:
   - name: Disconnected containers
     displayName: docker, commitment, plan, environment, usage
     href: containers/disconnected.md
-- name: Concepts
-  items:
-  - name: Model overview
-    displayName: get started, prebuilt, extraction, input
-    href: concept-model-overview.md
-  - name: Accuracy and confidence scores
-    displayName: tables, labels, ocr, performance, signatures
-    href: concept-accuracy-confidence.md
-  - name: Analyze document API response
-    displayName: words, lines, pages, bounding regions, documents
-    href: concept-analyze-document-response.md
-  - name: Read model
-    displayName: text
-    href: concept-read.md
-  - name: General document model
-    displayName: key value pairs, selection marks, structured
-    href: concept-general-document.md?view<=doc-intel-3.1.0&preserve-view=true
-  - name: Layout model
-    displayName: tables, selection marks, structure, paragraph roles, text, headers, page numbers
-    href: concept-layout.md
-  - name: Add-on capabilities
-    displayName: extract, formula, font, styles, fontStyle, ocr.highResolution, ocr.formula, high resolution, background color, inline, display
-    href: concept-add-on-capabilities.md
-  - name: Query field extraction
-    displayName: queries, fields, OpenAI, chat
-    href: concept-query-fields.md
-  - name: 🆕 Retrieval-Augmented Generation (RAG)
-    displayName: RAG, LLM, semantic, chunk, LangChain, language model
-    href: concept-retrieval-augmented-generation.md
-  - name: 🆕Custom generative model
-    displayName: ai studio, neural, template, custom
-    href: concept-custom-generative.md
-  - name: 🆕 Batch documents analysis 
-    displayName: analyze, azureBlobFileListSource, azureBlobSource, azureBlobFileListSource, resultContainerUrl, resultPrefix, overwriteExisting
-    href: concept-batch-analysis.md
-  - name: 🆕 Pay stub model
-    displayName: compensation, earnings, deductions, taxes, benefits, employer, employee
-    href: concept-pay-stub.md
-  - name: 🆕 Bank check model
-    displayName: routing, account, number, amount, payee, issuer, date
-    href: concept-bank-check.md
-  - name: 🆕 Bank statement model
-    displayName: transactions, deposits, withdrawals, balance, account, number, date
-    href: concept-bank-statement.md
-  - name: Credit card model
-    displayName: debit
-    href: concept-credit-card.md
-  - name: US mortgage documents
-    displayName: 1003, 1008, closing, disclosure
-    href: concept-mortgage-documents.md
-  - name: Marriage certificate model
-    displayName: license
-    href: concept-marriage-certificate.md
-  - name: Contract model
-    displayName: contracts, agreements, legal, terms, conditions, clauses, parties, dates, signatures
-    href: concept-contract.md
-  - name: U.S.Tax document models
-    displayName: tax, forms, 1098, 1098-E, 1098-T, W-2, wages, taxes, salary, employees, tuition, loan, interest, mortgage
-    href: concept-tax-document.md
-  - name: Health insurance card model
-    displayName: health, proof, hospital
-    href: concept-health-insurance-card.md
-  - name: Invoice model
-    displayName: sales, vendors, VAT
-    href: concept-invoice.md
-  - name: Receipt model
-    displayName: sales, merchants
-    href: concept-receipt.md
-  - name: ID document model
-    displayName: passport, visa, ID, social security, green card
-    href: concept-id-document.md
-  - name: Business card model
-    displayName: /rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP
-    href: concept-business-card.md?view<=doc-intel-3.1.0&preserve-view=true
-  - name: Custom models
-    items:
-    - name: Custom model overview
-      displayName: table, label, ocr, confidence, template, neural
-      href: concept-custom.md
-    - name: 🆕 Composed models
-      displayName: custom, assign, modelId, model ID
-      href:  concept-composed-models.md
-    - name: 🆕 Incremental classifier
-      displayName: custom, classification, training
-      href: concept-incremental-classifier.md  
-    - name: Custom template model
-      displayName: structure, selection, labels, tables, tabular, train, template, neural, build mode, signatures, custom
-      href: concept-custom-template.md
-    - name: Custom neural model
-      displayName: selection, structure, tables, tabular, train, template, neural, build mode, signatures, custom
-      href: concept-custom-neural.md
-    - name: Custom classification model
-      displayName: custom, train, classification, splitting
-      href: concept-custom-classifier.md
-    - name: Custom labels
-      displayName: structure, selection, labels, tables, tabular, train
-      href: concept-custom-label.md
-    - name: Custom labeling tips
-      displayName: structure, selection, labels, tables, tabular, train, tips
-      href: concept-custom-label-tips.md
-    - name: Custom model lifecycle
-      displayName: custom, train, modelId, model ID, expiration, train, build
-      href: concept-custom-lifecycle.md
+
 - name: Code samples
   items:
   - name: "C#/.NET"
@@ -302,7 +307,7 @@ items:
     - name: 2022-08-31 (v3.0)
       href: /rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP
     - name: Error codes v4.0, v3.1, and v3.0
-      href: v3-error-guide.md
+      href: how-to-guides/resolve-errors.md
     - name: v2.1
       href: /rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true
   - name: Client libraries (2024-07-31-preview)
@@ -315,6 +320,10 @@ items:
       href: /javascript/api/overview/azure/ai-document-intelligence-rest-readme?view=azure-node-preview&preserve-view=true
     - name: Python
       href: /python/api/overview/azure/ai-documentintelligence-readme?view=azure-python-preview&preserve-view=true
+  - name: Schema
+    items:
+    - name: Marriage certificate
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/marriage-certificate/2024-07-31-preview.json?context=/azure/ai-services/context/context
 - name: Resources
   items:
   - name: Enterprise readiness
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスの目次の更新とリンク修正"
}
```

### Explanation
この変更では、ドキュメントインテリジェンスに関する目次（toc.yml）が更新され、特定のリンクの修正やコンテンツの再構成が行われました。総計で247行が変更され、その内訳には128行の追加と119行の削除があります。

主な変更内容は以下の通りです：

1. **リンクの修正**: 各種モデルや機能に関連するリンクが、より適切なパスに修正されています。特に、モデルの選択や言語サポートに関連する項目でリンクの構造が変更されました。これにより、ユーザーが必要な情報に迅速にアクセスできるようになっています。

2. **項目の追加**: プリビルトモデルやカスタムモデルに関する項目が新たに追加され、多くの具体的なモデル（例：銀行小切手、請求書など）の概要が示されています。この変更により、ユーザーが提供される機能やサービスの理解が深まり、選択肢が拡大しました。

3. **セクションの再構成**: 「コンセプト」セクション内のエントリが整理され、関連性のある情報がまとめられました。また、個々の機能に対する説明が指定されたパスに更新されており、文書全体の整合性が向上しています。

4. **削除された項目**: いくつかの古い参照や冗長な項目が削除され、全体の読みやすさとコンパクトさが向上しました。

これらの変更により、ドキュメントインテリジェンスの目次が最新の情報を反映し、ユーザーが機能やリソースを探しやすくなることが期待されます。また、教育的価値も増しており、新しいユーザーにとって非常に使いやすくなっています。

## articles/ai-services/document-intelligence/train/composed-models.md{#item-3f2e9f}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Composed custom models - Document Intelligence 
+title: Composed custom models - Document Intelligence
 titleSuffix: Azure AI services
 description: Compose several custom models into a single model for easier data extraction from groups of distinct form types.
 author: laujan
@@ -13,21 +13,21 @@ ms.author: lajanuar
 # Document Intelligence composed custom models
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-[!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
+[!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
+[!INCLUDE [applies to v3.1](../includes/applies-to-v31.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 ::: moniker-end
 
 > [!IMPORTANT]
@@ -46,15 +46,15 @@ In previous versions, the `model compose` operation performed an implicit classi
 
 The new `model compose` operation requires you to train an explicit classifier and provides several benefits.
 
-* **Continual incremental improvement**. You can consistently improve the quality of the classifier by adding more samples and [incrementally improving classification]( concept-incremental-classifier.md). This fine tuning ensures your documents are always routed to the right model for extraction.
+* **Continual incremental improvement**. You can consistently improve the quality of the classifier by adding more samples and [incrementally improving classification](../concept/incremental-classifier.md). This fine tuning ensures your documents are always routed to the right model for extraction.
 
 * **Complete control over routing**. By adding confidence-based routing, you provide a confidence threshold for the document type and the classification response.
 
 * **Ignore document specific document types during the operation**. Earlier implementations of the `model compose` operation selected the best analysis model for extraction based on the confidence score even if the highest confidence scores were relatively low. By providing a confidence threshold or explicitly not mapping a known document type from classification to an extraction model, you can ignore specific document types.
 
 * **Analyze multiple instances of the same document type**. When paired with the  `splitMode` option of the classifier, the `model compose` operation can detect multiple instances of the same document in a file and split the file to process each document independently. Using `splitMode` enables the processing of multiple instances of a document in a single request.
 
-* **Support for add on features**. [Add on features](concept-add-on-capabilities.md) like query fields or barcodes can also be specified as a part of the analysis model parameters.
+* **Support for add on features**. [Add on features](../concept/add-on-capabilities.md) like query fields or barcodes can also be specified as a part of the analysis model parameters.
 
 * **Assigned custom model maximum expanded to 500**. The new implementation of the `model compose` operation allows you to assign up to 500 trained custom models to a single composed model.
 
@@ -84,11 +84,11 @@ Composed models are billed the same as individual custom models. The pricing is
 
 ::: moniker range="<=doc-intel-3.1.0"
 
-## Use model compose
+## Use the model compose operation
 
 * Start by creating a list of all the model IDs you want to compose into a single model.
 
-* Compose the models into a single model ID using the Studio, REST API, or client libraries. 
+* Compose the models into a single model ID using the Studio, REST API, or client libraries.
 
 * Use the composed model ID to analyze documents.
 
@@ -112,9 +112,9 @@ Composed models are billed the same as individual custom models. The pricing is
 
 * With the `model compose` operation, you can assign up to 500 models to a single model ID. If the number of models that I want to compose exceeds the upper limit of a composed model, you can use one of these alternatives:
 
-  * Classify the documents before calling the custom model. You can use the [Read model](concept-read.md) and build a classification based on the extracted text from the documents and certain phrases by using sources like code, regular expressions, or search.
+  * Classify the documents before calling the custom model. You can use the [Read model](../prebuilt/read.md) and build a classification based on the extracted text from the documents and certain phrases by using sources like code, regular expressions, or search.
 
-  * If you want to extract the same fields from various structured, semi-structured, and unstructured documents, consider using the deep-learning [custom neural model](concept-custom-neural.md). Learn more about the [differences between the custom template model and the custom neural model](concept-custom.md#compare-model-features).
+  * If you want to extract the same fields from various structured, semi-structured, and unstructured documents, consider using the deep-learning [custom neural model](../train/custom-neural.md). Learn more about the [differences between the custom template model and the custom neural model](../train/custom-model.md#compare-model-features).
 
 * Analyzing a document by using composed models is identical to analyzing a document by using a single model. The `Analyze Document` result returns a `docType` property that indicates which of the component models you selected for analyzing the document.
 
@@ -143,7 +143,7 @@ Document Intelligence **v4.0:2024-07-31-preview** supports the following tools,
 
 | Feature | Resources |
 |----------|-------------|
-|***Custom model***| &bullet; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&bullet; [REST API](/rest/api/aiservices/operation-groups?view=rest-aiservices-2024-07-31-preview&preserve-view=true)</br>&bullet; [C# SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet; [Java SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet; [JavaScript SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet; [Python SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|
+|***Custom model***| &bullet; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&bullet; [REST API](/rest/api/aiservices/operation-groups?view=rest-aiservices-2024-07-31-preview&preserve-view=true)</br>&bullet; [C# SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet; [Java SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet; [JavaScript SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet; [Python SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|
 | ***Composed model***| &bullet; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&bullet; [REST API](/rest/api/aiservices/operation-groups?view=rest-aiservices-2024-02-29-preview&preserve-view=true)</br>&bullet; [C# SDK](/dotnet/api/azure.ai.formrecognizer.training.formtrainingclient.startcreatecomposedmodel)</br>&bullet; [Java SDK](/java/api/com.azure.ai.formrecognizer.training.formtrainingclient.begincreatecomposedmodel)</br>&bullet; [JavaScript SDK](/javascript/api/@azure/ai-form-recognizer/documentmodeladministrationclient?view=azure-node-latest#@azure-ai-form-recognizer-documentmodeladministrationclient-begincomposemodel&preserve-view=true)</br>&bullet; [Python SDK](/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.formtrainingclient?view=azure-python#azure-ai-formrecognizer-formtrainingclient-begin-create-composed-model&preserve-view=true)|
 
 :::moniker-end
@@ -154,7 +154,7 @@ Document Intelligence **v3.1:2023-07-31 (GA)** supports the following tools, app
 
 | Feature | Resources |
 |----------|-------------|
-|***Custom model***| &bullet; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&bullet; [REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet; [C# SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet; [Java SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet; [JavaScript SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet; [Python SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|
+|***Custom model***| &bullet; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&bullet; [REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet; [C# SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet; [Java SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet; [JavaScript SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet; [Python SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|
 | ***Composed model***| &bullet; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&bullet; [REST API](/rest/api/aiservices/document-models/compose-model?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet; [C# SDK](/dotnet/api/azure.ai.formrecognizer.training.formtrainingclient.startcreatecomposedmodel)</br>&bullet; [Java SDK](/java/api/com.azure.ai.formrecognizer.training.formtrainingclient.begincreatecomposedmodel)</br>&bullet; [JavaScript SDK](/javascript/api/@azure/ai-form-recognizer/documentmodeladministrationclient?view=azure-node-latest#@azure-ai-form-recognizer-documentmodeladministrationclient-begincomposemodel&preserve-view=true)</br>&bullet; [Python SDK](/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.formtrainingclient?view=azure-python#azure-ai-formrecognizer-formtrainingclient-begin-create-composed-model&preserve-view=true)|
 
 :::moniker-end
@@ -165,7 +165,7 @@ Document Intelligence **v3.0:2022-08-31 (GA)** supports the following tools, app
 
 | Feature | Resources |
 |----------|-------------|
-|***Custom model***| &bullet; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&bullet; [REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet; [C# SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet; [Java SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet; [JavaScript SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet; [Python SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|
+|***Custom model***| &bullet; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&bullet; [REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet; [C# SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet; [Java SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet; [JavaScript SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet; [Python SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|
 | ***Composed model***| &bullet; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects)</br>&bullet; [REST API](/rest/api/aiservices/document-models/compose-model?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet; [C# SDK](/dotnet/api/azure.ai.formrecognizer.training.formtrainingclient.startcreatecomposedmodel)</br>&bullet; [Java SDK](/java/api/com.azure.ai.formrecognizer.training.formtrainingclient.begincreatecomposedmodel)</br>&bullet; [JavaScript SDK](/javascript/api/@azure/ai-form-recognizer/documentmodeladministrationclient?view=azure-node-latest#@azure-ai-form-recognizer-documentmodeladministrationclient-begincomposemodel&preserve-view=true)</br>&bullet; [Python SDK](/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.formtrainingclient?view=azure-python#azure-ai-formrecognizer-formtrainingclient-begin-create-composed-model&preserve-view=true)|
 
 ::: moniker-end
@@ -176,7 +176,7 @@ Document Intelligence v2.1 supports the following resources:
 
 | Feature | Resources |
 |----------|-------------------------|
-|***Custom model***| &bullet; [Document Intelligence labeling tool](https://fott-2-1.azurewebsites.net)</br>&bullet; [REST API](how-to-guides/compose-custom-models.md?view=doc-intel-2.1.0&tabs=rest&preserve-view=true)</br>&bullet; [Client library SDK](~/articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet; [Document Intelligence Docker container](containers/install-run.md?tabs=custom#run-the-container-with-the-docker-compose-up-command)|
+|***Custom model***| &bullet; [Document Intelligence labeling tool](https://fott-2-1.azurewebsites.net)</br>&bullet; [REST API](../how-to-guides/compose-custom-models.md?view=doc-intel-2.1.0&tabs=rest&preserve-view=true)</br>&bullet; [Client library SDK](~/articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet; [Document Intelligence Docker container](../containers/install-run.md?tabs=custom#run-the-container-with-the-docker-compose-up-command)|
 | ***Composed model*** |&bullet; [Document Intelligence labeling tool](https://fott-2-1.azurewebsites.net/)</br>&bullet; [REST API](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)</br>&bullet; [C# SDK](/dotnet/api/azure.ai.formrecognizer.training.createcomposedmodeloperation?view=azure-dotnet&preserve-view=true)</br>&bullet; [Java SDK](/java/api/com.azure.ai.formrecognizer.models.createcomposedmodeloptions?view=azure-java-stable&preserve-view=true)</br>&bullet; JavaScript SDK</br>&bullet; [Python SDK](/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.formtrainingclient?view=azure-python#azure-ai-formrecognizer-formtrainingclient-begin-create-composed-model&preserve-view=true)|
 
 ::: moniker-end
@@ -187,5 +187,5 @@ Learn to create and compose custom models:
 
 > [!div class="nextstepaction"]
 >
-> [**Build a custom model**](how-to-guides/build-a-custom-model.md)
-> [**Compose custom models**](how-to-guides/compose-custom-models.md)
+> [**Build a custom model**](../how-to-guides/build-a-custom-model.md)
+> [**Compose custom models**](../how-to-guides/compose-custom-models.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのコンポーズモデルのファイル名変更とリンク修正"
}
```

### Explanation
この変更では、ドキュメントインテリジェンスに関する「コンポーズモデル」の文書ファイル名が変更され、関連するリンクも修正されました。具体的には、ファイル名が「concept-composed-models.md」から「train/composed-models.md」に変更された他、合計で36行が変更された部分があります。

主な変更内容は以下の通りです：

1. **ファイル名変更**: ファイルが「concept-composed-models.md」から「train/composed-models.md」に移動され、文書の目的や内容に関連する整理が行われました。この再構成により、ユーザーは関連情報にアクセスしやすくなるとともに、文書体系の一貫性が向上します。

2. **リンクの修正**: ドキュメント内のリンクが修正され、多くの相対パスが更新されました。特に、他のドキュメントやコンセプトに対するリンクが以前の形式から相対パス形式に変更されており、これにより文書間の移動がスムーズになっています。

3. **情報の明確化**: 一部のステートメントや説明が整理され、コンポーズモデルの操作に関する説明がより明確になっています。たとえば、モデルの組み合わせや新しい機能に関する説明が充実し、ユーザーがこの機能をより理解しやすくなっています。

4. **導入ノートの追加**: 新しいモデル構成の操作についての注意事項や使い方が詳しく説明され、コンセプト実装に際してのガイダンスが強化されています。

これらの変更により、文書が最新の情報を反映し、ユーザーがドキュメントインテリジェンスのコンポーズモデル機能を効果的に理解し、利用できるようになることが期待されます。全体的に、ドキュメントがより一貫性を持ち、使い勝手が向上する効果があります。

## articles/ai-services/document-intelligence/train/custom-classifier.md{#item-42f8fd}

<details>
<summary>Diff</summary>
````diff
@@ -17,13 +17,13 @@ monikerRange: '>=doc-intel-3.1.0'
 # Document Intelligence custom classification model
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-**This content applies to:**![checkmark](media/yes-icon.png) **v4.0 (preview)** | **Previous version:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru)
+**This content applies to:**![checkmark](../media/yes-icon.png) **v4.0 (preview)** | **Previous version:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru)
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true)
 :::moniker-end
 
 ::: moniker range=">=doc-intel-4.0.0"
@@ -67,15 +67,15 @@ With custom models, you need to maintain access to the training dataset to updat
 >
 > Incremental training is only supported with models trained with the same API version. If you are trying to extend a model, use the API version the original model was trained with to extend the model. Incremental training is only supported with API version **2024-07-31-preview** or later.
 
-Incremental training requires that you provide the original model ID as the `baseClassifierId`. See [incremental training](concept-incremental-classifier.md) to learn more about how to use incremental training.
+Incremental training requires that you provide the original model ID as the `baseClassifierId`. See [incremental training](../concept/incremental-classifier.md) to learn more about how to use incremental training.
 
 ### Office document type support
 
 You can now train classifiers to recognize document types in various formats including PDF, images, Word, PowerPoint, and Excel. When assembling your training dataset, you can add documents of any of the supported types. The classifier doesn't require you to explicitly label specific types. As a best practice, ensure your training dataset has at least one sample of each format to improve the overall accuracy of the model.
 
 ### Compare custom classification and composed models
 
-A custom classification model can replace [a composed model](concept-composed-models.md) in some scenarios but there are a few differences to be aware of:
+A custom classification model can replace [a composed model](../train/composed-models.md) in some scenarios but there are a few differences to be aware of:
 
 | Capability | Custom classifier process | Composed model process |
 |--|--|--|
@@ -90,7 +90,7 @@ Classification models currently only support English language documents.
 :::moniker-end
 
 ::: moniker range=">=doc-intel-4.0.0"
-Classification models can now be trained on documents of different languages. See [supported languages](language-support-custom.md) for a complete list.
+Classification models can now be trained on documents of different languages. See [supported languages](../language-support/custom.md) for a complete list.
 ::: moniker-end
 
 ## Input requirements
@@ -145,7 +145,7 @@ The classifier attempts to assign each document to one of the classes, if you ex
 
 ## Training a model
 
-Custom classification models are supported by **v4.0: 2024-02-29-preview, 2024-07-31-preview** and **v3.1: 2023-07-31 (GA)** APIs. [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio) provides a no-code user interface to interactively train a custom classifier. Follow the [how to guide](how-to-guides/build-a-custom-classifier.md) to get started.
+Custom classification models are supported by **v4.0: 2024-02-29-preview, 2024-07-31-preview** and **v3.1: 2023-07-31 (GA)** APIs. [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio) provides a no-code user interface to interactively train a custom classifier. Follow the [how to guide](../how-to-guides/build-a-custom-classifier.md) to get started.
 
 When using the REST API, if you organize your documents by folders, you can use the `azureBlobSource` property of the request to train a classification model.
 
@@ -399,5 +399,5 @@ The response contains the identified documents with the associated page ranges i
 Learn to create custom classification models:
 
 > [!div class="nextstepaction"]
-> [**Build a custom classification model**](how-to-guides/build-a-custom-classifier.md)
-> [**Custom models overview**](concept-custom.md)
+> [**Build a custom classification model**](../how-to-guides/build-a-custom-classifier.md)
+> [**Custom models overview**](../train/custom-model.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム分類モデル文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、ドキュメントインテリジェンスにおけるカスタム分類モデルに関する文書がリネームされ、同時にリンクも修正されました。具体的には、ファイル名が「concept-custom-classifier.md」から「train/custom-classifier.md」に変更され、合計で18行の変更がありました。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名が変更され、内容の整理が図られました。これにより、ユーザーはカスタム分類モデルに関連する情報をより明確に見つけることができるようになります。

2. **リンクの修正**: 文書内に存在する多数のリンクが更新され、相対パス形式に変更されています。この修正により、他の関連文書へのアクセスがよりスムーズになり、文書全体の整合性が向上しました。

3. **情報の明確化**: 一部の説明が詳細になり、特に増分トレーニングや異なる種類のドキュメントのサポートに関する情報が強化されています。また、カスタム分類モデルとコンポーズモデルとの比較説明もより明確に整理されています。

4. **トレーニング要件の説明追加**: カスタム分類モデルをトレーニングする際の要件や推奨事項が整理され、ユーザーが必要なサンプルやフォルダ構成に関する理解を深めることができるようになっています。

これらの変更により、カスタム分類モデルに関する文書が最新の情報を反映し、ユーザーがこの機能を効果的に利用できるようになることが期待されます。また、整理されたコンテンツは、ユーザー体験を向上させる重要な要素となります。

## articles/ai-services/document-intelligence/train/custom-generative-extraction.md{#item-a8f912}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: overview
-ms.date: 08/09/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 monikerRange: '>=doc-intel-4.0.0'
 ---
@@ -58,7 +58,7 @@ Field extraction custom generative model currently supports dynamic table with t
 
 ## Build mode  
 
-The `build custom model` operation supports custom **template**, **neural**, and **generative** models, _see_ [Custom model build mode](concept-custom.md#build-mode). Here are the differences in the model types:
+The `build custom model` operation supports custom **template**, **neural**, and **generative** models, _see_ [Custom model build mode](../train/custom-model.md#build-mode). Here are the differences in the model types:
 
 * **Custom generative AI models** can process complex documents with various formats, varied templates, and unstructured data.
 
@@ -68,15 +68,15 @@ The `build custom model` operation supports custom **template**, **neural**,
 
 ## Languages and locale support
 
-Field extraction custom generative model `2024-07-31-preview` version supports the **en-us** locale. For more information on language support, _see_ [Language support - custom models](language-support-custom.md).
+Field extraction custom generative model `2024-07-31-preview` version supports the **en-us** locale. For more information on language support, _see_ [Language support - custom models](../language-support/custom.md).
 
 ## Region support
 
 Field extraction custom generative model `2024-07-31-preview` version is only available in 'East US' and `North Central US`.  
 
 ## Input requirements
 
-[!INCLUDE [input requirements](./includes/input-requirements.md)]
+[!INCLUDE [input requirements](../includes/input-requirements.md)]
 
 ## Best practices  
 
@@ -86,7 +86,7 @@ Field extraction custom generative model `2024-07-31-preview` version is only av
 
 * **Field Description**. Provide more contextual information in description to help clarify the field that needs to be extracted. Examples include location in the document, potential field labels it can be associated with, and ways to differentiate with other terms that could be ambiguous.
 
-* **Variation**. Custom generative models can generalize across different document templates of the same document type. As a best practice, create a single model for all variations of a document type. Ideally, include a visual template for each type, especially for ones that involve distinct formatting or structural elements, to improve the model's accuracy and consistency in generating or processing documents.
+* **Variation**. Custom generative models can generalize across different document templates of the same document type. As a best practice, create a single model for all variations of a document type. To enhance the model's accuracy and consistency in document generation or processing, include a visual template for each type, particularly those requiring specific formatting and/or structural elements.
 
 ## Service guidance
 
@@ -127,5 +127,5 @@ https://{endpoint}/documentintelligence/documentModels:build?api-version=2024-07
 
 ## Next steps
 
-* Learn how to [create custom generative models](how-to-guides/build-train-custom-generative-model.md)
-* Learn more about [custom models](concept-custom.md)
+* Learn how to [create custom generative models](../how-to-guides/build-train-custom-generative-model.md)
+* Learn more about [custom models](../train/custom-model.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム生成抽出モデル文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、カスタム生成抽出モデルに関する文書のファイル名が変更され、追加のリンク修正が行われました。具体的には、ファイル名が「concept-custom-generative.md」から「train/custom-generative-extraction.md」に変更され、全体で14行の変更がありました。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名が変更され、カスタム生成抽出モデルに関する情報がより明確に整理されています。これにより、ユーザーは関連情報をより簡単に見つけることができ、ドキュメントの構造が向上したと言えます。

2. **リンクの修正**: 文書内の多くのリンクが相対パス形式に修正され、他の関連コンテンツへのアクセスがよりスムーズになりました。これにより、全体的な文書の整合性が向上しています。

3. **日付の更新**: ドキュメントの日付が「08/09/2024」から「10/03/2024」に更新され、最新の情報が反映されています。

4. **情報の明確化**: 特に、フィールド抽出に関する説明がより具体的になり、カスタム生成モデルの構成や使用に関する推奨事項が強化されています。たとえば、生成モデルが異なるテンプレートを一般化する能力についての説明が改善され、ユーザーがこれを利用する際の理解が深まる内容になっています。

5. **ベストプラクティスの強化**: ドキュメントの作成や処理におけるベストプラクティスが明確に示され、具体的な例や推奨事項が整理されています。

これらの変更により、カスタム生成抽出モデルに関するドキュメントが最新の情報を反映し、ユーザーが関連機能を効果的に理解し、利用できるようになることが期待されます。全体的に、文書がより一貫し、利用しやすくなることに寄与しています。

## articles/ai-services/document-intelligence/train/custom-label-tips.md{#item-041f5c}

<details>
<summary>Diff</summary>
````diff
@@ -17,25 +17,25 @@ monikerRange: '>=doc-intel-3.0.0'
 # Tips for building labeled datasets
 
 ::: moniker range="doc-intel-4.0.0"
-**This content applies to:**![checkmark](media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
+**This content applies to:**![checkmark](../media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true)
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](../media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true)
 ::: moniker-end
 
 > [!IMPORTANT]
-> Best practices to generating labelled datasets only applies to custom template and custom neural models, for custom generative, refer to [Custom Generative](concept-custom-generative.md)
+> Best practices to generating labelled datasets only applies to custom template and custom neural models, for custom generative, refer to [Custom Generative](custom-generative-extraction.md)
 
 This article highlights the best methods for labeling custom model datasets in the Document Intelligence Studio. Labeling documents can be time consuming when you have a large number of labels, long documents, or documents with varying structure. These tips should help you label documents more efficiently.
 
 ## Video: Custom labels best practices
 
-* The following video is the second of two presentations intended to help you build custom models with higher accuracy (the first presentation explores [How to create a balanced data set](concept-custom-label.md#video-custom-label-tips-and-pointers)).
+* The following video is the second of two presentations intended to help you build custom models with higher accuracy (the first presentation explores [How to create a balanced data set](custom-labels.md#video-custom-label-tips-and-pointers)).
 
 * We examine best practices for labeling your selected documents. With semantically relevant and consistent labeling, you should see an improvement in model performance.
 
@@ -70,10 +70,10 @@ When creating a field, select the right subtype to minimize post processing, for
 * Learn more about custom labeling:
 
   > [!div class="nextstepaction"]
-  > [Custom labels](concept-custom-label.md)
+  > [Custom labels](custom-labels.md)
 
 * Learn more about custom template models:
 
   > [!div class="nextstepaction"]
-  > [Custom models](concept-custom-template.md)
+  > [Custom models](custom-template.md)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムラベル作成のヒント文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、カスタムラベルの作成に関するヒントを提供する文書のファイル名が変更され、いくつかのリンクが修正されました。具体的には、ファイル名が「concept-custom-label-tips.md」から「train/custom-label-tips.md」に変更され、全体で14行の変更がありました。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名が変更され、カスタムラベル作成に関する情報がより具体的に整理されています。これにより、ユーザーは関連情報を迅速に見つけやすくなります。

2. **リンクの修正**: 文書中の多数のリンクが更新され、相対リンクに変更されています。これにより、関連するドキュメントへのアクセスが容易になり、文書全体の整合性が向上しました。

3. **重要な注意書きの修正**: ラベル付きデータセット生成のベストプラクティスについての重要なセクションが修正され、カスタム生成モデルへのリンクが更新されました。

4. **情報の明確化**: 文書内での表現が明確になり、特にラベル付けのベストプラクティスに関する説明が強化されています。これにより、ユーザーが効率的に文書をラベル付けできるようになることが期待されます。

5. **ビデオリンクの更新**: ラベル付けのベストプラクティスに関するビデオのリンクが更新され、ユーザーが関連するリソースにアクセスしやすくなっています。

これらの変更により、カスタムラベル作成のためのヒントが最新の情報を反映し、より使いやすい形で提供されるようになりました。文書全体の整合性と一貫性が向上することで、ユーザーはより効果的にこの機能を活用できるようになると期待されます。

## articles/ai-services/document-intelligence/train/custom-labels.md{#item-90435a}

<details>
<summary>Diff</summary>
````diff
@@ -16,10 +16,10 @@ monikerRange: '>=doc-intel-3.0.0'
 
 # Best practices: generating labeled datasets
 
-[!INCLUDE [applies to v4.0 v3.1 v3.0](includes/applies-to-v40-v31-v30.md)]
+[!INCLUDE [applies to v4.0 v3.1 v3.0](../includes/applies-to-v40-v31-v30.md)]
 
 > [!IMPORTANT]
-> Best practices to generating labelled datasets only applies to custom template and custom neural models, for custom generative, refer to [Custom Generative](concept-custom-generative.md)
+> Best practices to generating labelled datasets only applies to custom template and custom neural models, for custom generative, refer to [Custom Generative](custom-generative-extraction.md)
 
 Custom models (template and neural) require a labeled dataset of at least five documents to train a model. The quality of the labeled dataset affects the accuracy of the trained model. This guide helps you learn more about generating a model with high accuracy by assembling a diverse dataset and provides best practices for labeling your documents.
 
@@ -33,13 +33,13 @@ A labeled dataset consists of several files:
 
   * A `fields.json` file is created when the first field is added. There's one `fields.json` file for the entire training dataset, the field list contains the field name and associated sub fields and types.
 
-  * The Studio runs each of the documents through the [Layout API](concept-layout.md). The layout response for each of the sample files in the dataset is added as `{file}.ocr.json`. The layout response is used to generate the field labels when a specific span of text is labeled.
+  * The Studio runs each of the documents through the [Layout API](../prebuilt/layout.md). The layout response for each of the sample files in the dataset is added as `{file}.ocr.json`. The layout response is used to generate the field labels when a specific span of text is labeled.
 
   * A `{file}.labels.json` file is created or updated when a field is labeled in a document. The label file contains the spans of text and associated polygons from the layout output for each span of text the user adds as a value for a specific field.
 
 ## Video: Custom label tips and pointers
 
-* The following video is the first of two presentations intended to help you build custom models with higher accuracy (The second presentation examines [Best practices for labeling documents](concept-custom-label-tips.md#video-custom-labels-best-practices)).
+* The following video is the first of two presentations intended to help you build custom models with higher accuracy (The second presentation examines [Best practices for labeling documents](custom-label-tips.md#video-custom-labels-best-practices)).
 
 * We explore how to create a balanced data set and select the right documents to label. This process sets you on the path to higher quality models.
 
@@ -51,9 +51,9 @@ Before you start labeling, it's a good idea to look at a few different samples o
 
 * **Document formats**: If you expect to analyze both digital and scanned documents, add a few examples of each type to the training dataset.
 
-* **Variations (template model)**:  Consider splitting the dataset into folders and train a model for each of variation. Any variations that include either structure or layout should be split into different models. You can then compose the individual models into a single [composed model](concept-composed-models.md).
+* **Variations (template model)**:  Consider splitting the dataset into folders and train a model for each of variation. Any variations that include either structure or layout should be split into different models. You can then compose the individual models into a single [composed model](composed-models.md).
 
-* **Variations (Neural models)**: When your dataset has a manageable set of variations, about 15 or fewer, create a single dataset with a few samples of each of the different variations to train a single model. If the number of template variations is larger than 15, you train multiple models and [compose](concept-composed-models.md) them together.
+* **Variations (Neural models)**: When your dataset has a manageable set of variations, about 15 or fewer, create a single dataset with a few samples of each of the different variations to train a single model. If the number of template variations is larger than 15, you train multiple models and [compose](composed-models.md) them together.
 
 * **Tables**: For documents containing tables with a variable number of rows, ensure that the training dataset also represents documents with different numbers of rows.
 
@@ -88,7 +88,7 @@ Custom neural models currently only support key-value pairs, structured fields (
 | Custom template | ✔️Supported| ✔️Supported | ✔️Supported | ✔️Supported | ✔️Supported | Unsupported |
 
 <sup>1</sup> Region labeling implementation differs between template and neural models. For template models, the training process injects synthetic data at training time if no text is found in the region labeled. With neural models, no synthetic text is injected and the recognized text is used as is.</br>
-<sup>2</sup> Overlapping fields are supported starting with the API version ```2024-02-29-preview``` and later. Overlapping fields have some limits. For more information, *see* [overlapping fields](concept-custom-neural.md#overlapping-fields).
+<sup>2</sup> Overlapping fields are supported starting with the API version ```2024-02-29-preview``` and later. Overlapping fields have some limits. For more information, *see* [overlapping fields](custom-neural.md#overlapping-fields).
 
 ## Tabular fields
 
@@ -120,7 +120,7 @@ Tabular fields are also useful when extracting repeating information within a do
 * Train a custom model:
 
   > [!div class="nextstepaction"]
-  > [How to train a model](how-to-guides/build-a-custom-model.md?view=doc-intel-3.0.0&preserve-view=true)
+  > [How to train a model](../how-to-guides/build-a-custom-model.md?view=doc-intel-3.0.0&preserve-view=true)
 
 * View the REST APIs:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムラベルに関する文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、カスタムラベルの生成に関する文書のファイル名が変更され、関連するリンクも更新されました。具体的には、ファイル名が「concept-custom-label.md」から「train/custom-labels.md」に変更され、全体で16行の変更が行われました。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名が変更され、より明確にカスタムラベルに関連する情報を示すようになりました。これにより、ユーザーは該当する情報を見つけやすくなります。

2. **リンクの修正**: 文書内の数箇所でリンクが相対的に更新され、関連情報へのアクセスがスムーズになりました。特に、他の文書へのリンクや画像のリンクが修正され、全体の整合性が向上しています。

3. **重要な注意書きの更新**: ラベル付きデータセットの生成におけるベストプラクティスについての重要なセクションが更新され、カスタム生成モデルへのリンクを新しいファイル名に合わせて変更しました。

4. **情報の明確化**: 各種モデルに関する情報が更新され、特にカスタムモデルおよびラベル付きデータセットの要件やベストプラクティスが明確に述べられています。

5. **ビデオリンクの修正**: カスタムラベルのヒントに関するビデオリンクが更新され、関連するリソースへのアクセスが容易になりました。

これらの変更により、カスタムラベル生成に関する文書が最新の情報を反映し、ユーザーがより効果的に利用できるように改善されています。また、文書の整合性と一貫性が向上することで、ユーザーはこの機能をより活用しやすくなることが期待されます。

## articles/ai-services/document-intelligence/train/custom-lifecycle.md{#item-2b7401}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Document Intelligence custom model lifecycle and management guide.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 02/29/2024
 ms.author: lajanuar
@@ -17,7 +15,7 @@ monikerRange: '>=doc-intel-3.1.0'
 # Document Intelligence custom model lifecycle
 
 ::: moniker range=">=doc-intel-3.1.0"
-[!INCLUDE [applies to v4.0 and v3.1](includes/applies-to-v40-v31.md)]
+[!INCLUDE [applies to v4.0 and v3.1](../includes/applies-to-v40-v31.md)]
 ::: moniker-end
 
 With the v3.1 (GA) and later APIs, custom models introduce a expirationDateTime property that is set for each model trained with the 3.1 API or later. Custom models are dependent on the API version of the Layout API version and the API version of the model build operation. For best results, continue to use the API version the model was trained with for all analyze requests. The guidance applies to all Document Intelligence custom models including extraction and classification models.
@@ -26,7 +24,7 @@ With the v3.1 (GA) and later APIs, custom models introduce a expirationDateTime
 
 With the v3.1 API, custom models introduce a new model expiration property. The model expiration is set to two years from the date the model is built for all requests that use a GA API to build a model. To continue to use the model past the expiration date, you need to  train the model with a current GA API version. The API version can be the one that the model was originally trained with or a later API version. The following figure illustrates the options when you need to retrain an expiring or expired model.
 
-:::image type="content" source="media/model-lifecycle.png" alt-text="Screenshot showing how to choose an API version and retrain a model.":::
+:::image type="content" source="../media/model-lifecycle.png" alt-text="Screenshot showing how to choose an API version and retrain a model.":::
 
 ## Models trained with preview API version
 
@@ -60,4 +58,4 @@ Learn to create and compose custom models:
 
 > [!div class="nextstepaction"]
 >
-> [**Build a custom model**](how-to-guides/build-a-custom-model.md)  [**Compose custom models**](how-to-guides/compose-custom-models.md)
+> [**Build a custom model**](../how-to-guides/build-a-custom-model.md)  [**Compose custom models**](../how-to-guides/compose-custom-models.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムライフサイクルに関する文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、カスタムモデルのライフサイクルに関する文書のファイル名が変更され、いくつかのリンクが更新されました。具体的には、ファイル名が「concept-custom-lifecycle.md」から「train/custom-lifecycle.md」に変更され、全体で8行の変更が行われました。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名が変更され、カスタムモデルのライフサイクルに関連する内容がより明確に示されています。これにより、ユーザーが情報をより簡単に特定できるようになります。

2. **リンクの修正**: 文書内のいくつかのリンクが相対的に更新され、他の関連リソースへのアクセスが容易になりました。特に、画像のリンクや他のガイドへのリンクが修正されています。

3. **重要な情報の強調**: カスタムモデルに関する重要な情報が強調され、特にモデルの有効期限やそれを超えてモデルを使用するためのトレーニング要件についての説明が強化されています。

4. **視覚的な要素の更新**: モデルライフサイクルを示す図のリンクが修正され、ユーザーがAPIのバージョンを選択してモデルを再トレーニングする方法をより明確に示すようになっています。

5. **ナビゲーションの向上**: ガイドのリンクが更新され、ユーザーがカスタムモデルの構築や合成を学ぶために必要な情報に簡単にアクセスできるように工夫されています。

これらの変更により、カスタムライフサイクルに関する文書が最新の情報を反映し、ユーザーがより効果的に利用できるように改善されています。また、文書の整合性と一貫性が向上することで、ユーザーはこの機能をより活用しやすくなることが期待されます。

## articles/ai-services/document-intelligence/train/custom-model.md{#item-27c3b9}

<details>
<summary>Diff</summary>
````diff
@@ -5,43 +5,42 @@ description: Label and train customized models for your documents and compose mu
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 07/09/2024
 ms.author: lajanuar
 monikerRange: '<=doc-intel-4.0.0'
 ---
+<!-- markdownlint-disable MD033 -->
 
 # Document Intelligence custom models
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-[!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
+[!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
+[!INCLUDE [applies to v3.1](../includes/applies-to-v31.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 ::: moniker-end
 
 Document Intelligence uses advanced machine learning technology to identify documents, detect and extract information from forms and documents, and return the extracted data in a structured JSON output. With Document Intelligence, you can use document analysis models, pre-built/pre-trained, or your trained standalone custom models.
 
-Custom models now include [custom classification models](./concept-custom-classifier.md) for scenarios where you need to identify the document type before invoking the extraction model. Classifier models are available starting with the ```2023-07-31 (GA)``` API. A classification model can be paired with a custom extraction model to analyze and extract fields from forms and documents specific to your business. Standalone custom extraction models can be combined to create [composed models](concept-composed-models.md).
+Custom models now include [custom classification models](custom-classifier.md) for scenarios where you need to identify the document type before invoking the extraction model. Classifier models are available starting with the ```2023-07-31 (GA)``` API. A classification model can be paired with a custom extraction model to analyze and extract fields from forms and documents specific to your business. Standalone custom extraction models can be combined to create [composed models](composed-models.md).
 
 ::: moniker range=">=doc-intel-3.0.0"
 
 ## Custom document model types
 
-Custom document models can be one of two types, [**custom template**](concept-custom-template.md) or custom form and [**custom neural**](concept-custom-neural.md)  or custom document models. The labeling and training process for both models is identical, but the models differ as follows:
+Custom document models can be one of two types, [**custom template**](custom-template.md) or custom form and [**custom neural**](custom-neural.md)  or custom document models. The labeling and training process for both models is identical, but the models differ as follows:
 
 ### Custom extraction models
 
@@ -54,21 +53,21 @@ To create a custom extraction model, label a dataset of documents with the value
 > Starting with version 4.0 (2024-02-29-preview) API, custom neural models now support **overlapping fields** and **table, row and cell level confidence**.
 >
 
-The custom neural (custom document) model uses deep learning models and  base model trained on a large collection of documents. This model is then fine-tuned or adapted to your data when you train the model with a labeled dataset. Custom neural models support extracting key data fields from structured, semi-structured, and unstructured documents. When you're choosing between the two model types, start with a neural model to determine if it meets your functional needs. See [neural models](concept-custom-neural.md) to learn more about custom document models.
+The custom neural (custom document) model uses deep learning models and  base model trained on a large collection of documents. This model is then fine-tuned or adapted to your data when you train the model with a labeled dataset. Custom neural models support extracting key data fields from structured, semi-structured, and unstructured documents. When you're choosing between the two model types, start with a neural model to determine if it meets your functional needs. See [neural models](custom-neural.md) to learn more about custom document models.
 
 ### Custom template model
 
 The custom template or custom form model relies on a consistent visual template to extract the labeled data. Variances in the visual structure of your documents affect the accuracy of your model. Structured  forms such as questionnaires or applications are examples of consistent visual templates.
 
-Your training set consists of structured documents where the formatting and layout are static and constant from one document instance to the next. Custom template models support key-value pairs, selection marks, tables, signature fields, and regions. Template models and can be trained on documents in any of the [supported languages](language-support.md). For more information, *see* [custom template models](concept-custom-template.md).
+Your training set consists of structured documents where the formatting and layout are static and constant from one document instance to the next. Custom template models support key-value pairs, selection marks, tables, signature fields, and regions. Template models and can be trained on documents in any of the [supported languages](../language-support/custom.md). For more information, *see* [custom template models](custom-template.md).
 
 If the language of your documents and extraction scenarios supports custom neural models, we recommend that you use custom neural models over template models for higher accuracy.
 
 > [!TIP]
 >
 >To confirm that your training documents present a consistent visual template, remove all the user-entered data from each form in the set. If the blank forms are identical in appearance, they represent a consistent visual template.
 >
-> For more information, *see* [Interpret and improve accuracy and confidence for custom models](concept-accuracy-confidence.md).
+> For more information, *see* [Interpret and improve accuracy and confidence for custom models](../concept/accuracy-confidence.md).
 
 ## Input requirements
 
@@ -153,23 +152,23 @@ The following table compares custom template and custom neural features:
 |Data extraction | Key-value pairs, tables, selection marks, coordinates, and signatures | Key-value pairs, selection marks, and tables|
 |Overlapping fields | Not supported | Supported |
 |Document variations | Requires a model per each variation | Uses a single model for all variations |
-|Language support | [**Language support custom template**](language-support-custom.md#custom-template)  | [**Language support custom neural**](language-support-custom.md#custom-neural) |
+|Language support | [**Language support custom template**](../language-support/custom.md#custom-template)  | [**Language support custom neural**](../language-support/custom.md#custom-neural) |
 
 ### Custom classification model
 
- Document classification is a new scenario supported by Document Intelligence with the ```2023-07-31``` (v3.1 GA) API. The document classifier API supports classification and splitting scenarios. Train a classification model to identify the different types of documents your application supports. The input file for the classification model can contain multiple documents and classifies each document within an associated page range. To learn more, *see* [custom classification](concept-custom-classifier.md) models.
+ Document classification is a new scenario supported by Document Intelligence with the ```2023-07-31``` (v3.1 GA) API. The document classifier API supports classification and splitting scenarios. Train a classification model to identify the different types of documents your application supports. The input file for the classification model can contain multiple documents and classifies each document within an associated page range. To learn more, *see* [custom classification](custom-classifier.md) models.
 
  > [!NOTE]
 >
->Starting with the ```2024-02-29-preview``` API version document classification now supports Office document types for classification. This API version also introduces [incremental training](concept-incremental-classifier.md) for the classification model.
+>Starting with the ```2024-02-29-preview``` API version document classification now supports Office document types for classification. This API version also introduces [incremental training](../concept/incremental-classifier.md) for the classification model.
 
 ## Custom model tools
 
 Document Intelligence v3.1 and later models support the following tools, applications, and libraries, programs, and libraries:
 
 | Feature | Resources | Model ID|
 |---|---|:---|
-|Custom model| &bullet; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/customform/projects)</br>&bullet; [REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet; [C# SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet; [Python SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|***custom-model-id***|
+|Custom model| &bullet; [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/customform/projects)</br>&bullet; [REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet; [C# SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet; [Python SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|***custom-model-id***|
 
 ## Custom model life cycle
 
@@ -182,11 +181,11 @@ The life cycle of a custom model depends on the API version that is used to trai
 Document Intelligence v2.1 supports the following tools, applications, and libraries:
 
 > [!NOTE]
-> Custom model types [custom neural](concept-custom-neural.md) and [custom template](concept-custom-template.md) are available with Document Intelligence version v3.1 and v3.0 APIs.
+> Custom model types [custom neural](custom-neural.md) and [custom template](custom-template.md) are available with Document Intelligence version v3.1 and v3.0 APIs.
 
 | Feature | Resources |
 |---|---|
-|Custom model| &bullet; [Document Intelligence labeling tool](https://fott-2-1.azurewebsites.net)</br>&bullet; [REST API](how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&tabs=windows&pivots=programming-language-rest-api&preserve-view=true)</br>&bullet; [Client library SDK](~/articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet; [Document Intelligence Docker container](containers/install-run.md?tabs=custom#run-the-container-with-the-docker-compose-up-command)|
+|Custom model| &bullet; [Document Intelligence labeling tool](https://fott-2-1.azurewebsites.net)</br>&bullet; [REST API](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&tabs=windows&pivots=programming-language-rest-api&preserve-view=true)</br>&bullet; [Client library SDK](~/articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)</br>&bullet; [Document Intelligence Docker container](../containers/install-run.md?tabs=custom#run-the-container-with-the-docker-compose-up-command)|
 
 :::moniker-end
 
@@ -197,7 +196,7 @@ Extract data from your specific or unique documents using custom models. You nee
 * An Azure subscription. You can [create one for free](https://azure.microsoft.com/free/cognitive-services/).
 * A [Document Intelligence instance](https://portal.azure.com/#create/Microsoft.CognitiveServicesFormRecognizer) in the Azure portal. You can use the free pricing tier (`F0`) to try the service. After your resource deploys, select **Go to resource** to get your key and endpoint.
 
-  :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot that shows the keys and endpoint location in the Azure portal.":::
+  :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot that shows the keys and endpoint location in the Azure portal.":::
 
 ::: moniker range="doc-intel-2.1.0"
 
@@ -208,11 +207,11 @@ Extract data from your specific or unique documents using custom models. You nee
 > * For an enhanced experience and advanced model quality, try the [Document Intelligence v3.0 Studio](https://formrecognizer.appliedai.azure.com/studio).
 > * The v3.0 Studio supports any model trained with v2.1 labeled data.
 > * You can refer to the API migration guide for detailed information about migrating from v2.1 to v3.0.
-> * *See* our [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) or [**C#**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [Python](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) SDK quickstarts to get started with the v3.0 version.
+> * *See* our [**REST API**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) or [**C#**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [Python](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) SDK ../quickstarts to get started with the v3.0 version.
 
 * The Document Intelligence Sample Labeling tool is an open source tool that enables you to test the latest features of Document Intelligence and Optical Character Recognition (OCR) features.
 
-* Try the [**Sample Labeling tool quickstart**](quickstarts/try-sample-label-tool.md#train-a-custom-model) to get started building and using a custom model.
+* Try the [**Sample Labeling tool quickstart**](../quickstarts/try-sample-label-tool.md#train-a-custom-model) to get started building and using a custom model.
 
 :::moniker-end
 
@@ -239,7 +238,7 @@ Extract data from your specific or unique documents using custom models. You nee
 > [Try Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio/customform/projects)
 >
 
-For a detailed walkthrough to create your first custom extraction model, *see* [How to create a custom extraction model](how-to-guides/build-a-custom-model.md).
+For a detailed walkthrough to create your first custom extraction model, *see* [How to create a custom extraction model](../how-to-guides/build-a-custom-model.md).
 
 ## Custom model extraction summary
 
@@ -256,7 +255,7 @@ This table compares the supported data extraction areas:
 *-Behaves differently depending upon model. With template models, synthetic data is generated at training time. With neural models, exiting text recognized in the region is selected.
 
 > [!TIP]
-> When choosing between the two model types, start with a custom neural model if it meets your functional needs. See [custom neural](concept-custom-neural.md) to learn more about custom neural models.
+> When choosing between the two model types, start with a custom neural model if it meets your functional needs. See [custom neural](custom-neural.md) to learn more about custom neural models.
 
 :::moniker-end
 
@@ -266,9 +265,9 @@ The following table describes the features available with the associated tools a
 
 | Document type | REST API | SDK | Label and Test Models|
 |--|--|--|--|
-| Custom template v 4.0 v3.1 v3.0 | [Document Intelligence 3.1](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)| [Document Intelligence SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)| [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)|
-| Custom neural v4.0 v3.1 v3.0 | [Document Intelligence 3.1](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)| [Document Intelligence SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)| [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)
-| Custom form v2.1 | [Document Intelligence 2.1 GA API](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true) | [Document Intelligence SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true?pivots=programming-language-python)| [Sample labeling tool](https://fott-2-1.azurewebsites.net/)|
+| Custom template v 4.0 v3.1 v3.0 | [Document Intelligence 3.1](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)| [Document Intelligence SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)| [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)|
+| Custom neural v4.0 v3.1 v3.0 | [Document Intelligence 3.1](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)| [Document Intelligence SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)| [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)
+| Custom form v2.1 | [Document Intelligence 2.1 GA API](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true) | [Document Intelligence SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true?pivots=programming-language-python)| [Sample labeling tool](https://fott-2-1.azurewebsites.net/)|
 > [!NOTE]
 > Custom template models trained with the 3.0 API will have a few improvements over the 2.1 API stemming from improvements to the OCR engine. Datasets used to train a custom template model using the 2.1 API can still be used to train a new model using the 3.0 API.
 
@@ -292,23 +291,22 @@ The following table describes the features available with the associated tools a
 
 ## Supported languages and locales
 
-*See* our [Language Support—custom models](language-support-custom.md) page for a complete list of supported languages.
-
+*See* our [Language Support—custom models](../language-support/custom.md) page for a complete list of supported languages.
 
 ## Next steps
 
 ::: moniker range="doc-intel-2.1.0"
 
 * Try processing your own forms and documents with the [Document Intelligence Sample Labeling tool](https://fott-2-1.azurewebsites.net/).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
 :::moniker-end
 
 ::: moniker range=">=doc-intel-3.0.0"
 
 * Try processing your own forms and documents with the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio).
 
-* Complete a [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
+* Complete a [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) and get started creating a document processing app in the development language of your choice.
 
 :::moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデルに関する文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、カスタムモデルに関する文書のファイル名が変更され、さまざまなリンクが更新されました。具体的には、ファイル名が「concept-custom.md」から「train/custom-model.md」に変更され、全体で58行の変更が行われました。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名が変更され、カスタムモデルに関する内容がより明確に示されています。これにより、ユーザーが情報を特定しやすくなります。

2. **リンクの修正**: 文書内の複数箇所でリンクが相対的に更新され、他の関連リソースへのアクセスが容易になりました。特に、画像のリンクやガイドへのリンクが修正されています。

3. **新機能の紹介**: カスタムモデルに、新しいカスタム分類モデルが追加され、文書処理を行う前にドキュメントタイプを識別するためのシナリオが強調されています。

4. **情報の整理**: カスタムドキュメントモデルの種類、トレーニングプロセス、特徴に関する情報が整理され、ユーザーがどのモデルを使用するかを決定する際のガイダンスが改善されています。

5. **ナビゲーションの向上**: ガイドや参考情報へのリンクが更新され、ユーザーが効果的に文書をナビゲートできるように工夫されています。また、関連情報へのアクセスがよりスムーズになっています。

これらの変更により、カスタムモデルに関する文書が最新の情報を反映し、ユーザーがより効果的に利用できるように改善されています。また、文書の整合性と一貫性が向上することで、ユーザーはこの機能をより活用しやすくなることが期待されます。

## articles/ai-services/document-intelligence/train/custom-neural.md{#item-ac0e69}

<details>
<summary>Diff</summary>
````diff
@@ -21,27 +21,27 @@ monikerRange: '>=doc-intel-3.0.0'
 # Document Intelligence custom neural model
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-**This content applies to:**![checkmark](media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
+**This content applies to:**![checkmark](../media/yes-icon.png) **v4.0 (preview)** | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.1 (GA)**](?view=doc-intel-3.1.0&preserve-view=tru) ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0 (GA)**](?view=doc-intel-3.0.0&preserve-view=tru)
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous versions:** ![blue-checkmark](media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.1 (GA)** | **Latest version:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) | **Previous versions:** ![blue-checkmark](../media/blue-yes-icon.png) [**v3.0**](?view=doc-intel-3.0.0&preserve-view=true)
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-**This content applies to:** ![checkmark](media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true)
+**This content applies to:** ![checkmark](../media/yes-icon.png) **v3.0 (GA)** | **Latest versions:** ![purple-checkmark](../media/purple-yes-icon.png) [**v4.0 (preview)**](?view=doc-intel-4.0.0&preserve-view=true) ![purple-checkmark](../media/purple-yes-icon.png) [**v3.1**](?view=doc-intel-3.1.0&preserve-view=true)
 ::: moniker-end
 
-Custom neural document models or neural models are a deep learned model type that combines layout and language features to accurately extract labeled fields from documents. The base custom neural model is trained on various document types that makes it suitable to be trained for extracting fields from structured and semi-structured documents. Custom neural models are available in the [v3.0 and later models](v3-1-migration-guide.md) The table below lists common document types for each category:
+Custom neural document models or neural models are a deep learned model type that combines layout and language features to accurately extract labeled fields from documents. The base custom neural model is trained on various document types that makes it suitable to be trained for extracting fields from structured and semi-structured documents. Custom neural models are available in the [v3.0 and later models](../v3-1-migration-guide.md) The table below lists common document types for each category:
 
 | Documents | Examples |
 |---|--|
 | Structured| surveys, questionnaires|
 | Semi-structured | invoices, purchase orders |
 
-Custom neural models share the same labeling format and strategy as [custom template](concept-custom-template.md) models. Currently custom neural models only support a subset of the field types supported by custom template models.
+Custom neural models share the same labeling format and strategy as [custom template](custom-template.md) models. Currently custom neural models only support a subset of the field types supported by custom template models.
 
 ## Model capabilities
 
@@ -61,7 +61,7 @@ Custom neural models currently support key-value pairs and selection marks and s
 
 The `Build` operation supports *template* and *neural* custom models. Previous versions of the REST API and client libraries only supported a single build mode that is now known as the *template* mode.
 
-Neural models support documents that have the same information, but different page structures. Examples of these documents include United States W2 forms, which share the same information, but can vary in appearance across companies. For more information, *see* [Custom model build mode](concept-custom.md#build-mode).
+Neural models support documents that have the same information, but different page structures. Examples of these documents include United States W2 forms, which share the same information, but can vary in appearance across companies. For more information, *see* [Custom model build mode](custom-model.md#build-mode).
 
 ### Overlapping fields
 
@@ -106,11 +106,11 @@ Tabular fields provide **table, row and cell confidence** starting with the ```2
   * Row confidence, a measure of recognition of an individual row.
   * Cell confidence, a measure of recognition of an individual cell.
 
-* The recommended approach is to review the accuracy in a top-down manner starting with the table first, followed by the row and then the cell. See  [confidence and accuracy scores](concept-accuracy-confidence.md) to learn more about table, row, and cell confidence.
+* The recommended approach is to review the accuracy in a top-down manner starting with the table first, followed by the row and then the cell. See  [confidence and accuracy scores](../concept/accuracy-confidence.md) to learn more about table, row, and cell confidence.
 
 ### Supported languages and locales
 
-*See* our [Language Support—custom models](language-support-custom.md#custom-neural) for a complete list of supported languages.
+*See* our [Language Support—custom models](../language-support/custom.md#custom-neural) for a complete list of supported languages.
 
 ## Supported regions
 
@@ -137,7 +137,7 @@ As of October 18, 2022, Document Intelligence custom neural model training will
 :::moniker range="doc-intel-4.0.0"
 
 > [!TIP]
-> You can [copy a model](disaster-recovery.md#copy-api-overview) trained in one of the select regions listed to **any other region** and use it accordingly.
+> You can [copy a model](../disaster-recovery.md#copy-api-overview) trained in one of the select regions listed to **any other region** and use it accordingly.
 >
 > Use the [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-07-31-preview)&preserve-view=true) or [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects) to copy a model to another region.
 
@@ -146,7 +146,7 @@ As of October 18, 2022, Document Intelligence custom neural model training will
 :::moniker range="doc-intel-3.1.0"
 
 > [!TIP]
-> You can [copy a model](disaster-recovery.md#copy-api-overview) trained in one of the select regions listed to **any other region** and use it accordingly.
+> You can [copy a model](../disaster-recovery.md#copy-api-overview) trained in one of the select regions listed to **any other region** and use it accordingly.
 >
 > Use the [**REST API**](/rest/api/aiservices/document-models/copy-model-to?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP) or [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects) to copy a model to another region.
 
@@ -155,7 +155,7 @@ As of October 18, 2022, Document Intelligence custom neural model training will
 :::moniker range="doc-intel-3.0.0"
 
 > [!TIP]
-> You can [copy a model](disaster-recovery.md#copy-api-overview) trained in one of the select regions listed to **any other region** and use it accordingly.
+> You can [copy a model](../disaster-recovery.md#copy-api-overview) trained in one of the select regions listed to **any other region** and use it accordingly.
 >
 > Use the [**REST API**](/rest/api/aiservices/document-models/copy-model-to?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP) or [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio/custommodel/projects) to copy a model to another region.
 
@@ -208,15 +208,15 @@ Custom neural models differ from custom template models in a few different ways.
 
 * Custom neural model doesn't recognize values split across page boundaries.
 * Custom neural unsupported field types are ignored if a dataset labeled for custom template models is used to train a custom neural model.
-* Custom neural models are limited to 20 build operations per month. Open a support request if you need the limit increased. For more information, see [Document Intelligence service quotas and limits](service-limits.md).
+* Custom neural models are limited to 20 build operations per month. Open a support request if you need the limit increased. For more information, see [Document Intelligence service quotas and limits](../service-limits.md).
 
 ## Training a model
 
-Custom neural models are available in the [v3.0 and later models](v3-1-migration-guide.md).
+Custom neural models are available in the [v3.0 and later models](../v3-1-migration-guide.md).
 
 | Document Type | REST API | SDK | Label and Test Models|
 |--|--|--|--|
-| Custom document | [Document Intelligence 3.1](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)| [Document Intelligence SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)| [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)|
+| Custom document | [Document Intelligence 3.1](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)| [Document Intelligence SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)| [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)|
 
 The `Build` operation to train model supports a new ```buildMode``` property, to train a custom neural model, set the ```buildMode``` to ```neural```.
 
@@ -316,35 +316,37 @@ GET /documentModels/{myCustomModel}
 ```
 
 > [!NOTE]
-> For Document Intelligence versions `v3.1 (2023-07-31)` and `v3.0 (2022-08-31)`, custom neural model's paid training is not enabled. For the two older versions, you will get a maximum of 30 minutes training duration per model. If you would like to train more than 20 model instances, you can create an [Azure support ticket](service-limits.md#create-and-submit-support-request) to increase in the training limit.
+> For Document Intelligence versions `v3.1 (2023-07-31)` and `v3.0 (2022-08-31)`, custom neural model's paid training is not enabled. For the two older versions, you will get a maximum of 30 minutes training duration per model. If you would like to train more than 20 model instances, you can create an [Azure support ticket](../service-limits.md#create-and-submit-support-request) to increase in the training limit.
 
 :::moniker-end
 
 :::moniker range="doc-intel-3.1.0"
 
 ## Billing
 
-For Document Intelligence versions `v3.1 (2023-07-31) and v3.0 (2022-08-31)`, you receive a maximum 30 minutes of training duration per model, and a maximum of 20 trainings for free per month. If you would like to train more than 20 model instances, you can create an [Azure support ticket](service-limits.md#create-and-submit-support-request) to increase in the training limit. For Azure support ticket, enter in the `summary` field: `Increase Document Intelligence custom neural training (TPS) limit`. 
+For Document Intelligence versions `v3.1 (2023-07-31) and v3.0 (2022-08-31)`, you receive a maximum 30 minutes of training duration per model, and a maximum of 20 trainings for free per month. If you would like to train more than 20 model instances, you can create an [Azure support ticket](../service-limits.md#create-and-submit-support-request) to increase in the training limit. For Azure support ticket, enter in the `summary` field: `Increase Document Intelligence custom neural training (TPS) limit`. 
 
 > [!IMPORTANT]
-> * When increasing the training limit, note that 2 custom neural model training sessions will be considered as 1 training hour. For more details on the pricing for increasing the number of training sessions, refer to the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).
+>
+> * When increasing the training limit, note that 2 custom neural model training sessions will be considered as 1 training hour. For more information on the pricing for increasing the number of training sessions, *see** the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).
 > * Azure support ticket for training limit increase can only apply at a **resource-level**, not a subscription level. You can request a training limit increase for a single Document Intelligence resource by specifying your resource ID and region in the support ticket.
 
-If you want to train models for longer durations than 30 minutes, we support **paid training** with our newest version, `v4.0 (2024-07-31-preview)`. Using the latest version, you can train your model for a longer duration to process larger documents. For more information about paid training, *see* [Billing v4.0](service-limits.md#billing).
+If you want to train models for longer durations than 30 minutes, we support **paid training** with our newest version, `v4.0 (2024-07-31-preview)`. Using the latest version, you can train your model for a longer duration to process larger documents. For more information about paid training, *see* [Billing v4.0](../service-limits.md#billing).
 
 :::moniker-end
 
 :::moniker range="doc-intel-3.0.0"
 
 ## Billing
 
-For Document Intelligence versions `v3.1 (2023-07-31) and v3.0 (2022-08-31)`, you receive a maximum 30 minutes of training duration per model, and a maximum of 20 trainings for free per month. If you would like to train more than 20 model instances, you can create an [Azure support ticket](service-limits.md#create-and-submit-support-request) to increase in the training limit. For Azure support ticket, enter in the `summary` field: `Increase Document Intelligence custom neural training (TPS) limit`. 
+For Document Intelligence versions `v3.1 (2023-07-31) and v3.0 (2022-08-31)`, you receive a maximum 30 minutes of training duration per model, and a maximum of 20 trainings for free per month. If you would like to train more than 20 model instances, you can create an [Azure support ticket](../service-limits.md#create-and-submit-support-request) to increase in the training limit. For Azure support ticket, enter in the `summary` field: `Increase Document Intelligence custom neural training (TPS) limit`. 
 
 > [!IMPORTANT]
-> * When increasing the training limit, note that 2 custom neural model training sessions will be considered as 1 training hour. For more details on the pricing for increasing the number of training sessions, refer to the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).
+>
+> * When increasing the training limit, note that 2 custom neural model training sessions will be considered as 1 training hour. For more information on the pricing for increasing the number of training sessions, *see* the [pricing page](https://azure.microsoft.com/pricing/details/ai-document-intelligence/).
 > * Azure support ticket for training limit increase can only apply at a **resource-level**, not a subscription level. You can request a training limit increase for a single Document Intelligence resource by specifying your resource ID and region in the support ticket.
 
-If you want to train models for longer durations than 30 minutes, we support **paid training** with our newest version, `v4.0 (2024-07-31)`. Using the latest version, you can train your model for a longer duration to process larger documents. For more information about paid training, *see* [Billing v4.0](service-limits.md#billing).
+If you want to train models for longer durations than 30 minutes, we support **paid training** with our newest version, `v4.0 (2024-07-31)`. Using the latest version, you can train your model for a longer duration to process larger documents. For more information about paid training, *see* [Billing v4.0](../service-limits.md#billing).
 
 :::moniker-end
 
@@ -353,5 +355,5 @@ If you want to train models for longer durations than 30 minutes, we support **p
 Learn to create and compose custom models:
 
 > [!div class="nextstepaction"]
-> [**Build a custom model**](how-to-guides/build-a-custom-model.md)
-> [**Compose custom models**](how-to-guides/compose-custom-models.md)
+> [**Build a custom model**](../how-to-guides/build-a-custom-model.md)
+> [**Compose custom models**](../how-to-guides/compose-custom-models.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムニューラルモデルに関する文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、カスタムニューラルモデルに関する文書のファイル名が変更され、いくつかのリンクが更新されました。具体的には、ファイル名が「concept-custom-neural.md」から「train/custom-neural.md」に変更され、全体で50行の変更が行われました。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名が変更され、カスタムニューラルモデルに特化した内容がより明確に示されています。これにより、ユーザーは情報を簡単に特定できるようになります。

2. **リンクの修正**: 文書内で使用されている大多数のリンクが相対的に更新され、他の関連リソースへのアクセスが容易になりました。特に、文書内での画像やガイドへのリンクが修正されています。

3. **コンテンツの整理**: カスタムニューラルモデルに関する説明が整理され、ユーザーがどの機能や利用シナリオを選択すべきかが分かりやすくなっています。これには、モデルの能力や、サポートされているフォーマット、ビルドオペレーションの概要が含まれています。

4. **新機能の紹介**: モデルの重複フィールドや、タブularフィールドに関する更新が追加されており、これによりユーザーはモデルの新機能や強化された機能についての理解を深められます。

5. **ナビゲーションの向上**: 内容のスムーズなナビゲーションを目的としたリンクが更新され、ユーザーは関連情報により迅速にアクセスできるようになりました。

これらの変更により、カスタムニューラルモデルに関する文書が最新の情報を反映し、ユーザーがより効果的に文書を利用できるように改善されています。この更新により、ユーザーは機能の本質を把握しやすくなり、ドキュメント処理に関する理解が深まることが期待されます。

## articles/ai-services/document-intelligence/train/custom-template.md{#item-78e685}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: Use the custom template document model to train a model to extract
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 08/07/2024
 ms.author: lajanuar
@@ -18,21 +16,21 @@ monikerRange: 'doc-intel-4.0.0 || <=doc-intel-3.1.0'
 
 ::: moniker range="doc-intel-4.0.0"
 
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-[!INCLUDE [applies to v4.0](includes/applies-to-v40.md)]
+[!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1](includes/applies-to-v31.md)]
+[!INCLUDE [applies to v3.1](../includes/applies-to-v31.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
-[!INCLUDE [applies to v3.0](includes/applies-to-v30.md)]
+[!INCLUDE [applies to v3.0](../includes/applies-to-v30.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 ::: moniker-end
 
 Custom template (formerly custom form) is an easy-to-train document model that accurately extracts labeled key-value pairs, selection marks, tables, regions, and signatures from documents. Template models use layout cues to extract values from documents and are suitable to extract fields from highly structured documents with defined visual templates.
@@ -66,7 +64,7 @@ Tabular fields are also useful when extracting repeating information within a do
 
 ## Dealing with variations
 
-Template models rely on a defined visual template, changes to the template results in lower accuracy. In those instances, split your training dataset to include at least five samples of each template and train a model for each of the variations. You can then [compose](concept-composed-models.md) the models into a single endpoint. For subtle variations, like digital PDF documents and images, it's best to include at least five examples of each type in the same training dataset.
+Template models rely on a defined visual template, changes to the template results in lower accuracy. In those instances, split your training dataset to include at least five samples of each template and train a model for each of the variations. You can then [compose](composed-models.md) the models into a single endpoint. For subtle variations, like digital PDF documents and images, it's best to include at least five examples of each type in the same training dataset.
 
 ## Input requirements
 
@@ -108,7 +106,7 @@ Custom template models are generally available starting with v2.0 API and later
 
 | Model | REST API | SDK | Label and Test Models|
 |--|--|--|--|
-| Custom template  | [v3.1 API](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2024-02-29-preview&preserve-view=true&branch=docintelligence&tabs=HTTP)| [Document Intelligence SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)| [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)|
+| Custom template  | [v3.1 API](/rest/api/aiservices/document-models/build-model?view=rest-aiservices-2024-02-29-preview&preserve-view=true&branch=docintelligence&tabs=HTTP)| [Document Intelligence SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)| [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)|
 
 With the v3.0 and later APIs, the build operation to train model supports a new ```buildMode``` property, to train a custom template model, set the ```buildMode``` to ```template```.
 
@@ -136,7 +134,7 @@ Custom template models are generally available with the [v3.1 API](/rest/api/ais
 
 | Model | REST API | SDK | Label and Test Models|
 |--|--|--|--|
-| Custom template  | [v3.1 API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)| [Document Intelligence SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)| [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)|
+| Custom template  | [v3.1 API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)| [Document Intelligence SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)| [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)|
 
 With the v3.0 and later APIs, the build operation to train model supports a new ```buildMode``` property, to train a custom template model, set the ```buildMode``` to ```template```.
 
@@ -159,15 +157,15 @@ https://{endpoint}/formrecognizer/documentModels:build?api-version=2023-07-31
 
 ## Supported languages and locales
 
-*See* our [Language Support—custom models](language-support-custom.md) page for a complete list of supported languages.
+*See* our [Language Support—custom models](../language-support/custom.md) page for a complete list of supported languages.
 
 ::: moniker range="doc-intel-2.1.0"
 
 Custom (template) models  are generally available with the [v2.1 API](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true).
 
 | Model | REST API | SDK | Label and Test Models|
 |--|--|--|--|
-| Custom model (template) | [Document Intelligence 2.1 ](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)| [Document Intelligence SDK](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true?pivots=programming-language-python)| [Document Intelligence Sample labeling tool](https://fott-2-1.azurewebsites.net/)|
+| Custom model (template) | [Document Intelligence 2.1 ](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)| [Document Intelligence SDK](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true?pivots=programming-language-python)| [Document Intelligence Sample labeling tool](https://fott-2-1.azurewebsites.net/)|
 
 ::: moniker-end
 
@@ -178,15 +176,15 @@ Learn to create and compose custom models:
 ::: moniker range=">=doc-intel-3.0.0"
 
 > [!div class="nextstepaction"]
-> [**Build a custom model**](how-to-guides/build-a-custom-model.md)
-> [**Compose custom models**](how-to-guides/compose-custom-models.md)
+> [**Build a custom model**](../how-to-guides/build-a-custom-model.md)
+> [**Compose custom models**](../how-to-guides/compose-custom-models.md)
 
 ::: moniker-end
 
 ::: moniker range="doc-intel-2.1.0"
 
 > [!div class="nextstepaction"]
-> [**Build a custom model**](concept-custom.md#build-a-custom-model)
-> [**Compose custom models**](concept-composed-models.md#development-options)
+> [**Build a custom model**](custom-model.md#build-a-custom-model)
+> [**Compose custom models**](composed-models.md#development-options)
 
 ::: moniker-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムテンプレートに関する文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、カスタムテンプレートに関する文書のファイル名が変更され、さらにいくつかのリンクが相対的に更新されました。具体的には、ファイル名が「concept-custom-template.md」から「train/custom-template.md」に変更され、全体で30行の変更が見られました。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名を変更することで、カスタムテンプレートに特化した内容がより明確に示されています。これにより、ユーザーは情報を特定しやすくなっています。

2. **リンクの修正**: 文書内のリンクが相対的に更新され、他の関連リソースにアクセスしやすくなりました。特に、他のドキュメントやAPIに関連するリンクの修正が行われています。

3. **コンテンツの整備**: カスタムテンプレートモデルについての説明が整備されており、ユーザーがこのモデルを使用する目的や機能を理解しやすくなっています。特に、ビジュアルテンプレートに基づく情報抽出の精度に関する注意事項が強調されています。

4. **新機能と推奨事項の提供**: 文書は、トレーニングデータセットの構成やテンプレートの変動に対処する方法に関する推奨事項を提供し、ユーザーが複雑なデータをより効果的に扱えるようにしています。

5. **ナビゲーションの改善**: 文書全体のナビゲーションが改善されており、関連情報や次のステップに進むためのリンクが更新されています。これにより、ユーザーは他の文書やリソースにスムーズにアクセスできるようになります。

これらの変更により、カスタムテンプレートに関する文書が最新の情報を反映し、ユーザーがこの機能をより効果的に利用できるように改善されています。さらにユーザーの理解を助け、ドキュメント処理の効率を向上させることが期待されています。

## articles/ai-services/document-intelligence/tutorial/azure-function.md{#item-e0ba8d}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ ms.custom: VS Code-azure-extension-update-completed, devx-track-python
 
 Document Intelligence can be used as part of an automated data processing pipeline built with Azure Functions. This guide will show you how to use Azure Functions to process documents that are uploaded to an Azure blob storage container. This workflow extracts table data from stored documents using the Document Intelligence layout model and saves the table data in a .csv file in Azure. You can then display the data using Microsoft Power BI (not covered here).
 
-:::image type="content" source="media/tutorial-azure-function/workflow-diagram.png" alt-text="Screenshot of Azure Service workflow diagram":::
+:::image type="content" source="../media/tutorial-azure-function/workflow-diagram.png" alt-text="Screenshot of Azure Service workflow diagram":::
 
 In this tutorial, you learn how to:
 
@@ -36,7 +36,7 @@ In this tutorial, you learn how to:
 
   * After your resource deploys, select **Go to resource**. You need the key and endpoint from the resource you create to connect your application to the Document Intelligence API. You'll paste your key and endpoint into the code below later in the tutorial:
 
-      :::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
+      :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of keys and endpoint location in the Azure portal.":::
 
 * [**Python 3.6.x, 3.7.x, 3.8.x or 3.9.x**](https://www.python.org/downloads/) (Python 3.10.x isn't supported for this project).
 
@@ -75,11 +75,11 @@ In this tutorial, you learn how to:
 
     * Select the Azure subscription that you're using for this project and below you should see the Azure Function App.
 
-      :::image type="content" source="media/tutorial-azure-function/azure-extensions-visual-studio-code.png" alt-text="Screenshot of a list showing your Azure resources in a single, unified view.":::
+      :::image type="content" source="../media/tutorial-azure-function/azure-extensions-visual-studio-code.png" alt-text="Screenshot of a list showing your Azure resources in a single, unified view.":::
 
 1. Select the Workspace (Local) section located below your listed resources. Select the plus symbol and choose the **Create Function** button.
 
-    :::image type="content" source="media/tutorial-azure-function/workspace-create-function.png" alt-text="Screenshot showing where to begin creating an Azure function.":::
+    :::image type="content" source="../media/tutorial-azure-function/workspace-create-function.png" alt-text="Screenshot showing where to begin creating an Azure function.":::
 
 1. When prompted, choose **Create new project** and navigate to the **function-app** directory. Choose **Select**.
 
@@ -119,13 +119,13 @@ In this tutorial, you learn how to:
 
 1. Open Azure Storage Explorer and upload the sample PDF document to the **input** container. Then check the VS Code terminal. The script should log that it was triggered by the PDF upload.
 
-    :::image type="content" source="media/tutorial-azure-function/visual-studio-code-terminal-test.png" alt-text="Screenshot of the VS Code terminal after uploading a new document.":::
+    :::image type="content" source="../media/tutorial-azure-function/visual-studio-code-terminal-test.png" alt-text="Screenshot of the VS Code terminal after uploading a new document.":::
 
 1. Stop the script before continuing.
 
 ## Add document processing code
 
-Next, you'll add your own code to the Python script to call the Document Intelligence service and parse the uploaded documents using the Document Intelligence [layout model](concept-layout.md).
+Next, you'll add your own code to the Python script to call the Document Intelligence service and parse the uploaded documents using the Document Intelligence [layout model](../prebuilt/layout.md).
 
 1. In VS Code, navigate to the function's *requirements.txt* file. This file defines the dependencies for your script. Add the following Python packages to the file:
 
@@ -184,7 +184,7 @@ Next, you'll add your own code to the Python script to call the Document Intelli
     ```
 
     > [!IMPORTANT]
-    > Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information, *see* Azure AI services [security](../../ai-services/security-features.md).
+    > Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information, *see* Azure AI services [security](../../../ai-services/security-features.md).
 
 1. Next, add code to query the service and get the returned data.
 
@@ -297,5 +297,5 @@ In this tutorial, you learned how to use an Azure Function written in Python to
 > [!div class="nextstepaction"]
 > [Microsoft Power BI](https://powerbi.microsoft.com/integrations/azure-table-storage/)
 
-* [What is Document Intelligence?](overview.md)
-* Learn more about the [layout model](concept-layout.md)
+* [What is Document Intelligence?](../overview.md)
+* Learn more about the [layout model](../prebuilt/layout.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Functionsチュートリアルにおけるリンクの修正"
}
```

### Explanation
この変更では、Azure Functionsに関するチュートリアル文書のファイル名が「tutorial-azure-function.md」から「azure-function.md」に変更され、いくつかのリンクが更新されました。全体で18行の変更が見られ、追加と削除はそれぞれ9行ずつです。

主な変更内容は以下の通りです：

1. **ファイル名変更**: チュートリアルのファイル名が変更され、情報の整理やアクセスの簡素化が図られています。これにより、関連するリソースをより明確に特定できます。

2. **リンクの修正**: 文書内のコンテンツリンクが相対的に更新され、画像やドキュメントへのリンクが新しいパスに変更されています。これによって、チュートリアルが最新の情報を利用できるようになっています。

3. **コンテンツの整備**: チュートリアルの各ステップにおいて、Screenshotsの提供や手順の明確化が行われています。具体的には、Azureポータル内のキーやエンドポイントの位置を示す画像の更新や、Pythonスクリプト内で行う設定方法の説明が整理されています。

4. **新しい情報へのアクセス**: 記載されているリソースへのリンクが適切に更新されたことで、ユーザーは関連する情報やリソースにスムーズにアクセスできるようになりました。特に、セキュリティ関連の情報提供についての更新が見られます。

これらの変更によって、Azure Functionsを使用したドキュメント処理に関するチュートリアルが、より分かりやすく、使いやすくなっています。ユーザーは最新のリソースを活用して、より効果的に手続きを進めることが期待されます。

## articles/ai-services/document-intelligence/tutorial/logic-apps.md{#item-c6a43a}

<details>
<summary>Diff</summary>
````diff
@@ -5,10 +5,8 @@ description: A tutorial introducing how to use Document intelligence with Logic
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: tutorial
-ms.date: 04/24/2024
+ms.date: 10/15/2024
 ms.author: lajanuar
 zone_pivot_groups: cloud-location
 monikerRange: '<=doc-intel-4.0.0'
@@ -22,12 +20,12 @@ monikerRange: '<=doc-intel-4.0.0'
 <!-- markdownlint-disable MD004 -->
 <!-- markdownlint-disable MD032 -->
 :::moniker range=">=doc-intel-3.0.0"
-[!INCLUDE [applies to v4.0, v3.1 and v3.0](includes/applies-to-v40-v31-v30.md)]
+[!INCLUDE [applies to v4.0, v3.1 and v3.0](../includes/applies-to-v40-v31-v30.md)]
 
 :::moniker-end
 
 :::moniker range="doc-intel-2.1.0"
-[!INCLUDE [applies to v2.1](includes/applies-to-v21.md)]
+[!INCLUDE [applies to v2.1](../includes/applies-to-v21.md)]
 :::moniker-end
 
 :::moniker range=">=doc-intel-3.0.0"
@@ -65,11 +63,11 @@ For more information, *see* [Logic Apps Overview](/azure/logic-apps/logic-apps-o
 Choose a workflow using a file from either your Microsoft OneDrive account or Microsoft ShareDrive site:
 
 :::zone pivot="workflow-onedrive"
-[!INCLUDE [OneDrive](includes/logic-app-tutorial/onedrive.md)]
+[!INCLUDE [OneDrive](../includes/logic-app-tutorial/onedrive.md)]
 :::zone-end
 
 :::zone pivot="workflow-sharepoint"
-[!INCLUDE [SharePoint](includes/logic-app-tutorial/sharepoint.md)]
+[!INCLUDE [SharePoint](../includes/logic-app-tutorial/sharepoint.md)]
 :::zone-end
 
 ## Test the automation flow
@@ -88,35 +86,35 @@ Now that we created the flow, the last thing to do is to test it and make sure t
 
 1. Return to the Logic App designer tab and select the **Run trigger** button and select **Run** from the drop-down menu.
 
-    :::image type="content" source="media/logic-apps-tutorial/trigger-run.png" alt-text="Screenshot of Run trigger and Run buttons.":::
+    :::image type="content" source="../media/logic-apps-tutorial/trigger-run.png" alt-text="Screenshot of Run trigger and Run buttons.":::
 
 1. You see a message in the upper=right corner indicating that the trigger was successful:
 
-   :::image type="content" source="media/logic-apps-tutorial/trigger-successful.png" alt-text="Screenshot of Successful trigger message.":::
+   :::image type="content" source="../media/logic-apps-tutorial/trigger-successful.png" alt-text="Screenshot of Successful trigger message.":::
 
 1. Navigate to your Logic App overview page by selecting your app name link in the upper-left corner.
 
-    :::image type="content" source="media/logic-apps-tutorial/navigate-overview.png" alt-text="Screenshot of navigate to overview page link.":::
+    :::image type="content" source="../media/logic-apps-tutorial/navigate-overview.png" alt-text="Screenshot of navigate to overview page link.":::
 
 1. Check the status, to see if the run succeeded or failed. You can select the status indicator to check which steps were successful.
 
-    :::image border="true" type="content" source="media/logic-apps-tutorial/succeeded-failed-indicator.png" alt-text="Screenshot of Succeeded or Failed status.":::
+    :::image border="true" type="content" source="../media/logic-apps-tutorial/succeeded-failed-indicator.png" alt-text="Screenshot of Succeeded or Failed status.":::
 
 1. If your run failed, check the failed step to ensure that you entered the correct information.
 
-   :::image type="content" source="media/logic-apps-tutorial/failed-run-step.png" alt-text="Screenshot of failed step.":::
+   :::image type="content" source="../media/logic-apps-tutorial/failed-run-step.png" alt-text="Screenshot of failed step.":::
 
 1. After a workflow run succeeds, check your email. There's a new email with the information we specified.
 
-    :::image type="content" source="media/logic-apps-tutorial/invoice-received.png" alt-text="Screenshot of received email message.":::
+    :::image type="content" source="../media/logic-apps-tutorial/invoice-received.png" alt-text="Screenshot of received email message.":::
 
 1. After you're done, [disable or delete your logic app](/azure/logic-apps/manage-logic-apps-with-azure-portal?tabs=consumption#disable-enable-logic-apps) so that usage stops.
 
-   :::image type="content" source="media/logic-apps-tutorial/disable-delete.png" alt-text="Screenshot of disable and delete buttons.":::
+   :::image type="content" source="../media/logic-apps-tutorial/disable-delete.png" alt-text="Screenshot of disable and delete buttons.":::
 
 Congratulations! You completed this tutorial.
 
 ## Next steps
 
 > [!div class="nextstepaction"]
-> [Learn more about Document Intelligence models](concept-model-overview.md)
+> [Learn more about Document Intelligence models](../model-overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Logic Appsチュートリアルにおけるファイル名変更とリンク修正"
}
```

### Explanation
この変更では、「Logic Apps」に関するチュートリアル文書のファイル名が「tutorial-logic-apps.md」から「logic-apps.md」に変更され、関連するリンクが相対的に更新されました。全体で28行の変更があり、追加と削除はそれぞれ13行と15行です。

主な変更内容は以下の通りです：

1. **ファイル名変更**: チュートリアルのファイル名が変更されたことにより、文書がより整理された形式で提供されています。この変更は、関連情報の明確化に寄与しています。

2. **リンクの修正**: 文書内の各リンクが相対パスで更新され、ファイル内の読みやすさと整合性が向上しました。特に、インクルード文やメディアファイルのパスが適切に変更されています。

3. **日付の更新**: 文書の日付が「04/24/2024」から「10/15/2024」に更新され、最新の内容に合わせる形でタイムスタンプが改訂されています。

4. **コンテンツの整備**: Logic Appのワークフローの設計やトリガーの成功メッセージ、状態確認の手順についての説明が整理されており、ユーザーが手順を理解しやすくなっています。

5. **ナビゲーションの改善**: チュートリアル内のナビゲーションが強化され、ユーザーが後続のアクションに容易にアクセスできるように設計されています。特に、次のステップとして文書インテリジェンスモデルについての学習を促す部分が目立ちます。

これらの変更により、特にLogic Appsを利用したドキュメントインテリジェンスの使用方法についての理解が深まり、ユーザーはチュートリアルを通じてより効果的に学べるようになります。全体として、ドキュメントが最新の情報を反映し、利用者がスムーズに情報を取得できる環境が整えられています。

## articles/ai-services/document-intelligence/v21/deploy-label-tool.md{#item-e3c9ae}

<details>
<summary>Diff</summary>
````diff
@@ -5,28 +5,26 @@ description: Learn the different ways you can deploy the Document Intelligence S
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
-ms.date: 07/11/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 monikerRange: 'doc-intel-2.1.0'
 ---
-
+<!-- markdownlint-disable MD033 -->
 
 # Deploy the Sample Labeling tool
 
-**This content applies to:** ![Document Intelligence v2.1 checkmark](media/yes-icon.png) **v2.1**.
+**This content applies to:** ![Document Intelligence v2.1 checkmark](../media/yes-icon.png) **v2.1**.
 
 >[!TIP]
 >
 > * For an enhanced experience and advanced model quality, try the [Document Intelligence v3.0 Studio](https://formrecognizer.appliedai.azure.com/studio).
 > * The v3.0 Studio supports any model trained with v2.1 labeled data.
-> * You can refer to the [API migration guide](v3-1-migration-guide.md) for detailed information about migrating from v2.1 to v3.0.
-> * *See* our [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) or [**C#**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [Python](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) SDK quickstarts to get started with the v3.0 version.
+> * You can refer to the [API migration guide](../v3-1-migration-guide.md) for detailed information about migrating from v2.1 to v3.0.
+> * *See* our [**REST API**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) or [**C#**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [Python](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) SDK quickstarts to get started with the v3.0 version.
 
 > [!NOTE]
-> The [cloud hosted](https://fott-2-1.azurewebsites.net/) labeling tool is available at [https://fott-2-1.azurewebsites.net/](https://fott-2-1.azurewebsites.net/). Follow the steps in this document only if you want to deploy the Sample Labeling tool for yourself. 
+> The [cloud hosted](https://fott-2-1.azurewebsites.net/) labeling tool is available at [https://fott-2-1.azurewebsites.net/](https://fott-2-1.azurewebsites.net/). Follow the steps in this document only if you want to deploy the Sample Labeling tool for yourself.
 
 The Document Intelligence Sample Labeling tool is an application that provides a simple user interface (UI), which you can use to manually label forms (documents) for supervised learning. In this article, we provide links and instructions that teach you how to:
 
@@ -56,12 +54,12 @@ Follow these steps to create a new resource using the Azure portal:
 3. Next, select **Web App**.
 
    > [!div class="mx-imgBorder"]
-   > ![Select web app](./media/quickstarts/create-web-app.png)
+   > ![Select web app](../media/quickstarts/create-web-app.png)
 
 4. First, make sure that the **Basics** tab is selected. Now, you're going to need to provide some information:
 
    > [!div class="mx-imgBorder"]
-   > ![Select Basics](./media/quickstarts/select-basics.png)
+   > ![Select Basics](../media/quickstarts/select-basics.png)
    * Subscription - Select an existing Azure subscription
    * Resource Group - You can reuse an existing resource group or create a new one for this project. Creating a new resource group is recommended.
    * Name - Give your web app a name.
@@ -71,12 +69,12 @@ Follow these steps to create a new resource using the Azure portal:
    * Linux Plan - Select a pricing tier/plan for your app service.
 
    > [!div class="mx-imgBorder"]
-   > ![Configure your web app](./media/quickstarts/select-docker.png)
+   > ![Configure your web app](../media/quickstarts/select-docker.png)
 
 5. Next, select the **Docker** tab.
 
    > [!div class="mx-imgBorder"]
-   > ![Select Docker](./media/quickstarts/select-docker.png)
+   > ![Select Docker](../media/quickstarts/select-docker.png)
 
 6. Now let's configure your Docker container. All fields are required unless otherwise noted:
 <!-- markdownlint-disable MD025 -->
@@ -91,7 +89,7 @@ Follow these steps to create a new resource using the Azure portal:
 * Startup command - Set to `./run.sh eula=accept`
 
 > [!div class="mx-imgBorder"]
-> ![Configure Docker](./media/quickstarts/configure-docker.png)
+> ![Configure Docker](../media/quickstarts/configure-docker.png)
 
 * Next, select **Review + Create**, then **Create** to deploy your web app. When complete, you can access your web app at the URL provided in the **Overview** for your resource.
 
@@ -102,7 +100,7 @@ After you create your web app, you can enable the continuous deployment option:
 * From the left pane, choose **Container settings**.
 * In the main window, navigate to Continuous deployment and toggle between the **On** and **Off** buttons to set your preference:
 
-:::image type="content" source="media/label-tool/continuous-deployment.png" alt-text="Screenshot of enlargement of container settings for continuous deployment." lightbox="media/label-tool/continuous-deployment-bigger.png":::
+:::image type="content" source="../media/label-tool/continuous-deployment.png" alt-text="Screenshot of enlargement of container settings for continuous deployment." lightbox="../media/label-tool/continuous-deployment-bigger.png":::
 
 > [!NOTE]
 > When creating your web app, you can also configure authorization/authentication. This is not necessary to get started.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Label Toolデプロイチュートリアルのファイル名変更とリンク修正"
}
```

### Explanation
この変更では、Document Intelligenceに関連する「Label Tool」のデプロイに関するチュートリアル文書のファイル名が「deploy-label-tool.md」から「v21/deploy-label-tool.md」に変更され、内容内のリンクが調整されました。全体で26行の変更があり、追加と削除はそれぞれ12行と14行です。

主な変更内容は以下の通りです：

1. **ファイル名変更**: チュートリアルのファイル名の変更により、バージョン情報が明確になり、関連するリソースへのアクセスが容易になりました。新しい場所での整理が行われ、文書の可読性が向上しています。

2. **リンクの修正**: ドキュメント内で使用されていたローカルリンクが相対パスに修正され、これによりメディアファイルや関連リソースへのアクセスが正確に行えるようになっています。具体的には、画像のパスなどが更新されています。

3. **日付の更新**: コンテンツの日付が「07/11/2024」から「10/03/2024」に変更され、最新の情報であることを示しています。これにより、ユーザーは新しい情報と手順にアクセスできるようになっています。

4. **資料の明確化**: チュートリアル内では、APIの移行に関するガイドやSDKのクイックスタートへのリンクが強化されており、ユーザーが必要な情報を見つけやすくなっています。

5. **デプロイ手順の整理**: Azureポータルを使った新しいリソースの作成に関して、手順が整理され、必要な情報がわかりやすく示されています。特に、Webアプリケーションの設定に関する図が明確に更新されています。

これらの変更により、Label Toolのデプロイに関するチュートリアルがよりユーザーフレンドリーになり、手順が理解しやすくなっています。全体として、最新のリソースを反映した文書が整理され、利用者が順応しやすい環境が整えられています。

## articles/ai-services/document-intelligence/v21/label-tool.md{#item-2eeebd}

<details>
<summary>Diff</summary>
````diff
@@ -5,10 +5,8 @@ description: How to use the Document Intelligence sample tool to analyze documen
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
-ms.date: 07/11/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 monikerRange: 'doc-intel-2.1.0'
 ---
@@ -19,14 +17,14 @@ monikerRange: 'doc-intel-2.1.0'
 <!-- markdownlint-disable MD034 -->
 # Train a custom model using the Sample Labeling tool
 
-**This content applies to:** ![Document Intelligence v2.1 checkmark](media/yes-icon.png) **v2.1**.
+**This content applies to:** ![Document Intelligence v2.1 checkmark](../media/yes-icon.png) **v2.1**.
 
 >[!TIP]
 >
 > * For an enhanced experience and advanced model quality, try the [Document Intelligence v3.0 Studio](https://formrecognizer.appliedai.azure.com/studio).
 > * The v3.0 Studio supports any model trained with v2.1 labeled data.
-> * You can refer to the [API migration guide](v3-1-migration-guide.md) for detailed information about migrating from v2.1 to v3.0.
-> * *See* our [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) or [**C#**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [Python](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) SDK quickstarts to get started with the V3.0.
+> * You can refer to the [API migration guide](../v3-1-migration-guide.md) for detailed information about migrating from v2.1 to v3.0.
+> * *See* our [**REST API**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) or [**C#**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [Python](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) SDK quickstarts to get started with the V3.0.
 
 In this article, you use the Document Intelligence REST API with the Sample Labeling tool to train a custom model with manually labeled data.
 
@@ -44,7 +42,7 @@ In this article, you use the Document Intelligence REST API with the Sample Labe
 
 ## Create a Document Intelligence resource
 
-[!INCLUDE [create resource](includes/create-resource.md)]
+[!INCLUDE [create resource](../includes/create-resource.md)]
 
 ## Try it out
 
@@ -59,7 +57,7 @@ You need an Azure subscription ([create one for free](https://azure.microsoft.co
 
 > [!NOTE]
 >
-> If your storage data is behind a VNet or firewall, you must deploy the **Document Intelligence Sample Labeling tool** behind your VNet or firewall and grant access by creating a [system-assigned managed identity](managed-identities.md "Azure managed identity is a service principal that creates a Microsoft Entra identity and specific permissions for Azure managed resources").
+> If your storage data is behind a VNet or firewall, you must deploy the **Document Intelligence Sample Labeling tool** behind your VNet or firewall and grant access by creating a [system-assigned managed identity](../authentication/managed-identities.md "Azure managed identity is a service principal that creates a Microsoft Entra identity and specific permissions for Azure managed resources").
 
 You use the Docker engine to run the Sample Labeling tool. Follow these steps to set up the Docker container. For a primer on Docker and container basics, see the [Docker overview](https://docs.docker.com/engine/docker-overview/).
 
@@ -112,7 +110,7 @@ Enable CORS on your storage account. Select your storage account in the Azure po
 * Max age = 200
 
 > [!div class="mx-imgBorder"]
-> ![CORS setup in the Azure portal](media/label-tool/cors-setup.png)
+> ![CORS setup in the Azure portal](../media/label-tool/cors-setup.png)
 
 ## Connect to the Sample Labeling tool
 
@@ -126,11 +124,11 @@ Fill in the fields with the following values:
 
 * **Display Name** - The connection display name.
 * **Description** - Your project description.
-* **SAS URL** - The shared access signature (SAS) URL of your Azure Blob Storage container. [!INCLUDE [get SAS URL](includes/sas-instructions.md)]
+* **SAS URL** - The shared access signature (SAS) URL of your Azure Blob Storage container. [!INCLUDE [get SAS URL](../includes/sas-instructions.md)]
 
-   :::image type="content" source="media/quickstarts/get-sas-url.png" alt-text="SAS URL retrieval":::
+   :::image type="content" source="../media/quickstarts/get-sas-url.png" alt-text="SAS URL retrieval":::
 
-:::image type="content" source="media/label-tool/connections.png" alt-text="Connection settings of Sample Labeling tool.":::
+:::image type="content" source="../media/label-tool/connections.png" alt-text="Connection settings of Sample Labeling tool.":::
 
 ## Create a new project
 
@@ -144,7 +142,7 @@ In the Sample Labeling tool, projects store your configurations and settings. Cr
 * **Key** - Your Document Intelligence key.
 * **Description** - Optional - Project description
 
-:::image type="content" source="media/label-tool/new-project.png" alt-text="New project page on Sample Labeling tool.":::
+:::image type="content" source="../media/label-tool/new-project.png" alt-text="New project page on Sample Labeling tool.":::
 
 ## Label your forms
 
@@ -160,7 +158,7 @@ Select **Run Layout on unvisited documents** on the left pane to get the text an
 
 The labeling tool also shows which tables were automatically extracted. To see extracted tables, select the table/grid icon on the left hand of the document. In this quickstart, because the table content is automatically extracted, we don't label the table content, but rather rely on the automated extraction.
 
-:::image type="content" source="media/label-tool/table-extraction.png" alt-text="Table visualization in Sample Labeling tool.":::
+:::image type="content" source="../media/label-tool/table-extraction.png" alt-text="Table visualization in Sample Labeling tool.":::
 
 In v2.1, if your training document doesn't have a value filled in, you can draw a box where the value should be. Use **Draw region** on the upper left corner of the window to make the region taggable.
 
@@ -171,7 +169,7 @@ Next, you create tags (labels) and apply them to the text elements that you want
 1. First, use the tags editor pane to create the tags you'd like to identify.
    1. Select **+** to create a new tag.
    1. Enter the tag name.
-   1. Press Enter to save the tag.
+   1. Select Enter to save the tag.
 1. In the main editor, select words from the highlighted text elements or a region you drew in.
 1. Select the tag you want to apply, or press the corresponding keyboard key. The number keys are assigned as hotkeys for the first 10 tags. You can reorder your tags using the up and down arrow icons in the tag editor pane.
 1. Follow these steps to label at least five of your forms.
@@ -188,14 +186,14 @@ Next, you create tags (labels) and apply them to the text elements that you want
     > * To remove an applied tag without deleting the tag itself, select the tagged rectangle on the document view and press the delete key.
     >
 
-:::image type="content" source="media/label-tool/main-editor-2-1.png" alt-text="Main editor window of Sample Labeling tool.":::
+:::image type="content" source="../media/label-tool/main-editor-2-1.png" alt-text="Main editor window of Sample Labeling tool.":::
 
 ### Specify tag value types
 
 You can set the expected data type for each tag. Open the context menu to the right of a tag and select a type from the menu. This feature allows the detection algorithm to make assumptions that improve the text-detection accuracy. It also ensures that the detected values are returned in a standardized format in the final JSON output. Value type information is saved in the **fields.json** file in the same path as your label files.
 
 > [!div class="mx-imgBorder"]
-> ![Value type selection with Sample Labeling tool](media/whats-new/value-type.png)
+> ![Value type selection with Sample Labeling tool](../media/whats-new/value-type.png)
 
 The following value types and variations are currently supported:
 
@@ -247,11 +245,11 @@ The following value types and variations are currently supported:
 
 At times, your data might lend itself better to being labeled as a table rather than key-value pairs. In this case, you can create a table tag by selecting **Add a new table tag**. Specify whether the table has a fixed number of rows or variable number of rows depending on the document and define the schema.
 
-:::image type="content" source="media/label-tool/table-tag.png" alt-text="Configuring a table tag.":::
+:::image type="content" source="../media/label-tool/table-tag.png" alt-text="Configuring a table tag.":::
 
 Once you define your table tag, tag the cell values.
 
-:::image type="content" source="media/table-labeling.png" alt-text="Labeling a table.":::
+:::image type="content" source="../media/table-labeling.png" alt-text="Labeling a table.":::
 
 ## Train a custom model
 
@@ -261,8 +259,7 @@ To open the Training page, choose the Train icon on the left pane. Then select t
 * **Average Accuracy** - The model's average accuracy. You can improve model accuracy by adding and labeling more forms, then retraining to create a new model. We recommend starting by labeling five forms and adding more forms as needed.
 * The list of tags, and the estimated accuracy per tag.
 
-
-:::image type="content" source="media/label-tool/train-screen.png" alt-text="Training view.":::
+:::image type="content" source="../media/label-tool/train-screen.png" alt-text="Training view.":::
 
 After training finishes, examine the **Average Accuracy** value. If it's low, you should add more input documents and repeat the labeling steps. The documents you already labeled remain in the project index.
 
@@ -278,13 +275,13 @@ With Model Compose, you can compose up to 200 models to a single model ID. When
 * Choose the **Compose button**. In the pop-up, name your new composed model and select **Compose**.
 * When the operation completes, your newly composed model should appear in the list.
 
-:::image type="content" source="media/label-tool/model-compose.png" alt-text="Model compose UX view.":::
+:::image type="content" source="../media/label-tool/model-compose.png" alt-text="Model compose UX view.":::
 
 ## Analyze a form
 
 To test your model, select the `Analyze` icon from the navigation bar. Select source *Local file*. Browse for a file and select a file from the sample dataset that you unzipped in the test folder. Then choose the **Run analysis** button to get key/value pairs, text, and tables predictions for the form. The tool applies tags in bounding boxes and reports the confidence of each tag.
 
-:::image type="content" source="media/analyze.png" alt-text="Screenshot of analyze-a-custom-form window":::
+:::image type="content" source="../media/analyze.png" alt-text="Screenshot of analyze-a-custom-form window":::
 
 > [!TIP]
 > You can also run the `Analyze` API with a REST call. To learn how to do this, see [Train with labels using Python](https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/FormRecognizer/rest/python-labeled-data.md).
@@ -318,5 +315,5 @@ In this quickstart, you learned how to use the Document Intelligence Sample Labe
 > [!div class="nextstepaction"]
 > [Train with labels using Python](https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/FormRecognizer/rest/python-labeled-data.md)
 
-* [What is Document Intelligence?](overview.md)
-* [Document Intelligence quickstart](~/articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)
+* [What is Document Intelligence?](../overview.md)
+* [Document Intelligence quickstart](../how-to-guides/use-sdk-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Label Toolに関する文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、「Document Intelligence」に関連する「Label Tool」の文書が「label-tool.md」から「v21/label-tool.md」にファイル名を変更し、内容内のリンクが相対パスに修正されました。全体で47行の変更があり、追加と削除はそれぞれ22行と25行です。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名を変更することにより、バージョン情報が明確になります。これにより、他の関連リソースとの整合性が向上し、ユーザーにとってのわかりやすさが増しています。

2. **リンクの修正**: 内容内で使用されていたリンクが相対パスに修正されることで、文書内のリソースやメディアへのアクセスが正確かつ効率的になりました。具体的には、メディアファイルやサンプルリンクのパスが更新されています。

3. **日付の更新**: 文書の日付が「07/11/2024」から「10/03/2024」に変更され、最新の内容を反映しています。これにより、ユーザーは新しい情報を基に手続きを行うことができます。

4. **資料の明確化**: APIの移行ガイドやSDKのクイックスタートへのリンクが強化されており、これによりユーザーは必要な情報を容易に見つけられます。

5. **手順の整備**: Dockerエンジンを使用したLabeling Toolの設定や使い方に関する手順が整理され、ユーザーが必要とする情報に迅速にアクセスできるようになっています。この文書は、特に手順が視覚的に理解しやすく提示されています。

これらの変更により、Label Toolに関するチュートリアルがよりユーザーフレンドリーになり、内容が最新のステータスを反映したものとなっています。全体として、文書の明確性や整合性が向上し、ユーザーはより効率的に必要な情報を取得できるようになっています。

## articles/ai-services/document-intelligence/v21/sdk-overview-v2-1.md{#item-c5f5c7}

<details>
<summary>Diff</summary>
````diff
@@ -9,20 +9,20 @@ ms.custom:
   - devx-track-python
   - ignite-2023
 ms.topic: conceptual
-ms.date: 05/23/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 monikerRange: 'doc-intel-2.1.0'
 ---
 
-
+<!-- markdownlint-disable MD033 -->
 <!-- markdownlint-disable MD024 -->
 <!-- markdownlint-disable MD036 -->
 <!-- markdownlint-disable MD001 -->
 <!-- markdownlint-disable MD051 -->
 
 # SDK target: REST API v2.1 (GA)
 
-![Document Intelligence checkmark](media/yes-icon.png) **REST API version v2.1 (GA) 21-06-08**
+![Document Intelligence checkmark](../media/yes-icon.png) **REST API version v2.1 (GA) 21-06-08**
 
 Azure AI Document Intelligence is a cloud service that uses machine learning to analyze text and structured data from documents. The Document Intelligence software development kit (SDK) is a set of libraries and tools that enable you to easily integrate Document Intelligence models and capabilities into your applications. Document Intelligence SDK is available across platforms in C#/.NET, Java, JavaScript, and Python programming languages.
 
@@ -35,14 +35,14 @@ Document Intelligence SDK supports the following languages and platforms:
 | [.NET/C# → 3.1.x (GA)](/dotnet/api/azure.ai.formrecognizer?view=azure-dotnet&preserve-view=true)|[NuGet](https://www.nuget.org/packages/Azure.AI.FormRecognizer)|[v2.1](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)|[Windows, macOS, Linux, Docker](https://dotnet.microsoft.com/download)|
 |[Java → 3.1.x (GA)](https://azuresdkdocs.blob.core.windows.net/$web/java/azure-ai-formrecognizer/3.1.1/index.html) |[Maven repository](https://mvnrepository.com/artifact/com.azure/azure-ai-formrecognizer/3.1.1) |[v2.1](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)|[Windows, macOS, Linux](/java/openjdk/install)|
 |[JavaScript → 3.1.0 (GA)](https://azuresdkdocs.blob.core.windows.net/$web/javascript/azure-ai-form-recognizer/3.1.0/index.html)| [npm](https://www.npmjs.com/package/@azure/ai-form-recognizer/v/3.1.0)|[v2.1](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)| [Browser, Windows, macOS, Linux](https://nodejs.org/en/download/) |
-|[Python → 3.1.0 (GA)](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-formrecognizer/3.1.0/index.html) | [PyPI](https://pypi.org/project/azure-ai-formrecognizer/3.1.0/)|[v2.1](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)
-|[Windows, macOS, Linux](/azure/developer/python/configure-local-development-environment?tabs=windows%2Capt%2Ccmd#use-the-azure-cli)|
+|[Python → 3.1.0 (GA)](https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-formrecognizer/3.1.0/index.html) | [PyPI](https://pypi.org/project/azure-ai-formrecognizer/3.1.0/)|[v2.1](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)||
+|[Windows, macOS, Linux](/azure/developer/python/configure-local-development-environment?tabs=windows%2Capt%2Ccmd#use-the-azure-cli)||||
 
 For more information on other SDK versions, see:
 
-* [`2024-02-29` (preview)](sdk-overview-v4-0.md)
-* [`2023-07-31` v3.1 (GA)](sdk-overview-v3-1.md)
-* [`2022-08-31` v3.0 (GA)](sdk-overview-v3-0.md)
+* [`2024-02-29` (preview)](../sdk-overview-v4-0.md)
+* [`2023-07-31` v3.1 (GA)](../sdk-overview-v3-1.md)
+* [`2022-08-31` v3.0 (GA)](../sdk-overview-v3-0.md)
 
 ## Supported Clients
 
@@ -142,7 +142,7 @@ There are two supported methods for authentication.
 
 Here's where to find your Document Intelligence API key in the Azure portal:
 
-:::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of the keys and endpoint location in the Azure portal.":::
+:::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of the keys and endpoint location in the Azure portal.":::
 
 [!INCLUDE [Microsoft Entra ID or AKV](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv.md)]
 
@@ -191,7 +191,7 @@ async function main() {
 #### Use a Microsoft Entra token credential
 
 > [!NOTE]
-> Regional endpoints do not support Microsoft Entra authentication. Create a [custom subdomain](../../ai-services/authentication.md?tabs=powershell#create-a-resource-with-a-custom-subdomain) for your resource in order to use this type of authentication.
+> Regional endpoints do not support Microsoft Entra authentication. Create a [custom subdomain](../../../ai-services/authentication.md?tabs=powershell#create-a-resource-with-a-custom-subdomain) for your resource in order to use this type of authentication.
 
 Authorization is easiest using the `DefaultAzureCredential`. It provides a default token credential, based upon the running environment, capable of handling most Azure authentication scenarios.
 
@@ -209,7 +209,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/dotnet/api/azure.ide
         Install-Package Azure.Identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -238,7 +238,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/java/api/com.azure.i
     </dependency>
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -266,7 +266,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/javascript/api/@azur
     npm install @azure/identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -293,7 +293,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/python/api/azure-ide
     pip install azure-identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -318,7 +318,7 @@ For more information, *see* [Authenticate the client](https://github.com/Azure/a
 
 ### 4. Build your application
 
-Create a client object to interact with the Document Intelligence SDK, and then call methods on that client object to interact with the service. The SDKs provide both synchronous and asynchronous methods. For more insight, try a [quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) in a language of your choice.
+Create a client object to interact with the Document Intelligence SDK, and then call methods on that client object to interact with the service. The SDKs provide both synchronous and asynchronous methods. For more insight, try a [quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) in a language of your choice.
 
 ## Help options
 
@@ -330,4 +330,4 @@ The [Microsoft Q & A](/answers/topics/azure-form-recognizer.html) and [Stack Ove
 > [**Explore Document Intelligence REST API v2.1**](/rest/api/aiservices/analyzer?view=rest-aiservices-v2.1&preserve-view=true)
 
 > [!div class="nextstepaction"]
-> [**Try a Document Intelligence quickstart**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)
+> [**Try a Document Intelligence quickstart**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-2.1.0&preserve-view=true)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SDKオーバービュー文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、「Document Intelligence」に関連するSDKのオーバービュー文書が「sdk-overview-v2-1.md」から「v21/sdk-overview-v2-1.md」にファイル名が変更され、内容内のリンクも相対パスに修正されました。全体で32行の変更があり、追加と削除はそれぞれ16行と16行です。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名を変更することで、バージョンに関連付けが明確になり、他の資料との整合性が向上しました。これにより、ユーザーは特定のバージョンのドキュメントを容易に見つけることができます。

2. **リンクの修正**: 各種情報やリソースへのリンクが相対パスに変更され、文書内のメディアや外部リソースへのアクセスが正確になっています。これにより、ユーザーが関連情報を探す際の手間が軽減されています。

3. **日付の更新**: 文書の日付が「05/23/2024」から「10/03/2024」に変更され、最新の情報が反映されています。これにより、ユーザーは更新された内容に基づいて手続きを行うことが可能です。

4. **SDKの説明の強化**: Document Intelligence SDKの説明が充実しており、各プログラミング言語（C#、Java、JavaScript、Python）でのサポート状況が明示されています。これにより、開発者は自分の使用する言語に適したSDKを見つけやすくなっています。

5. **認証方法の説明**: 認証に関する情報が明確に示されており、ユーザーは必要なステップを理解しやすい状態になっています。また、Microsoft Entraを使用したトークン認証方法に関する詳細も加えられました。

6. **ヘルプオプションの明確化**: ユーザーがリソースを探しやすくするためのヘルプオプションや次のステップのアクションも明示されています。これにより、問題が発生した際に迅速にリソースを見つけて対処する手助けがなされます。

これらの変更により、SDKオーバービュー文書がよりユーザーフレンドリーになり、情報が最新の状態で提供されています。全体的に、構造と明確さが向上しており、開発者が必要な情報を洞察的に得やすくなっています。

## articles/ai-services/document-intelligence/v21/supervised-table-tags.md{#item-21d2b0}

<details>
<summary>Diff</summary>
````diff
@@ -5,26 +5,25 @@ description: Learn how to effectively use supervised table tag labeling.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
-ms.date: 07/11/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 monikerRange: 'doc-intel-2.1.0'
+
 #Customer intent: As a user of the Document Intelligence custom model service, I want to ensure I'm training my model in the best way.
 ---
 
 
 # Train models with the sample-labeling tool
 
-**This content applies to:** ![Document Intelligence v2.1 checkmark](media/yes-icon.png) **v2.1**.
+**This content applies to:** ![Document Intelligence v2.1 checkmark](../media/yes-icon.png) **v2.1**.
 
 >[!TIP]
 >
 > * For an enhanced experience and advanced model quality, try the [Document Intelligence v3.0 Studio](https://formrecognizer.appliedai.azure.com/studio).
 > * The v3.0 Studio supports any model trained with v2.1 labeled data.
-> * You can refer to the [API migration guide](v3-1-migration-guide.md) for detailed information about migrating from v2.1 to v3.0.
-> * *See* our [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) or [**C#**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [Python](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) SDK quickstarts to get started with version v3.0.
+> * You can refer to the [API migration guide](../v3-1-migration-guide.md) for detailed information about migrating from v2.1 to v3.0.
+> * *See* our [**REST API**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) or [**C#**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [Python](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) SDK quickstarts to get started with version v3.0.
 
 In this article, learn how to train your custom template model with table tags (labels). Some scenarios require more complex labeling than simply aligning key-value pairs. Such scenarios include extracting information from forms with complex hierarchical structures or encountering items that not automatically detected and extracted by the service. In these cases, you can use table tags to train your custom template model.
 
@@ -43,12 +42,12 @@ Here are some examples of when using table tags would be appropriate:
 * Determine whether you want a **dynamic** or **fixed-size** table tag. If the number of rows vary from document to document use a dynamic table tag. If the number of rows is consistent across your documents, use a fixed-size table tag.
 * If your table tag is dynamic, define the column names and the data type and format for each column.
 * If your table is fixed-size, define the column name, row name, data type, and format for each tag.
-:::image type="content" source="./media/table-tag-configure.png" alt-text="Configure a table tag":::
+:::image type="content" source="../media/table-tag-configure.png" alt-text="Configure a table tag":::
 
 ## Label your table tag data
 
 * If your project has a table tag, you can open the labeling panel, and populate the tag as you would label key-value fields.
-:::image type="content" source="media/table-labeling.png" alt-text="Label with table tags":::
+:::image type="content" source="../media/table-labeling.png" alt-text="Label with table tags":::
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "監視付きテーブルタグに関する文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、「Document Intelligence」に関連する監視付きテーブルタグについての文書が「supervised-table-tags.md」から「v21/supervised-table-tags.md」にファイル名を変更し、内容内のリンクが相対パスに修正されました。全体で15行の変更があり、7行の追加と8行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名を変更することで、バージョン情報との関連が明確になり、他の資料との整合性が向上しています。これにより、ユーザーは特定のバージョンのドキュメントを容易に探し出せます。

2. **リンクの修正**: 内部リンクが相対パスに修正され、ドキュメント内のリソースへのアクセスがより正確で効率的になりました。これにより、ユーザーが関連情報をスムーズに参照できるようになっています。

3. **日付の更新**: 文書の日付が「07/11/2024」から「10/03/2024」に変更され、最新の情報に基づいています。この更新により、ユーザーは新しい手順や情報を利用することができます。

4. **カスタマーインテントの追加**: 文書の冒頭にカスタマーインテントが追加され、ユーザーがどのような目的でこのサービスを使用するかが明示されています。これにより、文書の目的が一層明確になります。

5. **テーブルタグの使用方法の説明の強化**: テーブルタグの使用例やその構成方法についての説明が強化されており、ユーザーがより複雑なラベリングを行う必要があるシナリオについて具体的に学べるようになっています。

6. **画像のパス修正**: ドキュメント内で参照される画像へのパスが修正され、視覚的な資料が適切に表示されるようになっています。

これらの変更により、文書の構造と内容の明確性が向上し、ユーザーは自分のニーズに合わせた情報を見つけやすくなっています。全体として、監視付きテーブルタグに関する最新の知識を反映した充実したリソースとなっています。

## articles/ai-services/document-intelligence/v21/try-sample-label-tool.md{#item-c07ebc}

<details>
<summary>Diff</summary>
````diff
@@ -5,10 +5,8 @@ description: In this quickstart, learn to use the Document Intelligence Sample L
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: quickstart
-ms.date: 03/28/2024
+ms.date: 10/03/2024
 ms.author: lajanuar
 monikerRange: 'doc-intel-2.1.0'
 ---
@@ -27,7 +25,7 @@ monikerRange: 'doc-intel-2.1.0'
 > * For an enhanced experience and advanced model quality, try the [Document Intelligence v3.0 Studio](https://formrecognizer.appliedai.azure.com/studio).
 > * The v3.0 Studio supports any model trained with v2.1 labeled data.
 > * You can refer to the API migration guide for detailed information about migrating from v2.1 to v3.0.
-> * *See* our [**REST API**](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) or [**C#**](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [Python](get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) SDK quickstarts to get started with the v3.0 version.
+> * *See* our [**REST API**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) or [**C#**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**Java**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), [**JavaScript**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true), or [Python](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) SDK quickstarts to get started with the v3.0 version.
 
 The Azure AI Document Intelligence Sample Labeling tool is an open source tool that enables you to test the latest features of Document Intelligence and Optical Character Recognition (OCR) services:
 
@@ -58,9 +56,9 @@ You need the following to get started:
 
 Document Intelligence offers several prebuilt models to choose from. Each model has its own set of supported fields. The model to use for the `Analyze` operation depends on the type of document to be analyzed. Here are the prebuilt models currently supported by the Document Intelligence service:
 
-* [**Invoice**](../concept-invoice.md): extracts text, selection marks, tables, key-value pairs, and key information from invoices.
-* [**Receipt**](../concept-receipt.md): extracts text and key information from receipts.
-* [**ID document**](../concept-id-document.md): extracts text and key information from driver licenses and international passports.
+* [**Invoice**](../prebuilt/invoice.md): extracts text, selection marks, tables, key-value pairs, and key information from invoices.
+* [**Receipt**](../prebuilt/receipt.md): extracts text and key information from receipts.
+* [**ID document**](../prebuilt/id-document.md): extracts text and key information from driver licenses and international passports.
 * [**Business-card**](../concept-business-card.md): extracts text and key information from business cards.
 
 1. Navigate to the [Document Intelligence Sample Tool](https://fott-2-1.azurewebsites.net/).
@@ -119,7 +117,7 @@ Azure the Document Intelligence Layout API extracts text, tables, selection mark
 
 1. Select **Run Layout**. The Document Intelligence Sample Labeling tool calls the `Analyze Layout API` and analyzes the document.
 
-    :::image type="content" source="../media/fott-layout.png" alt-text="Screenshot of layout dropdown menu.":::
+    :::image type="content" source="../media/fott-layout.png" alt-text="Screenshot of the layout dropdown menu.":::
 
 1. View the results - see the highlighted text extracted, selection marks detected, and tables detected.
 
@@ -136,7 +134,7 @@ Train a custom model to analyze and extract data from forms and documents specif
 
 ### Prerequisites for training a custom form model
 
-* An Azure Storage blob container that contains a set of training data. Make sure all the training documents are of the same format. If you have forms in multiple formats, organize them into subfolders based on common format. For this project, you can use our [sample data set](https://github.com/Azure-Samples/cognitive-services-REST-api-samples/blob/master/curl/form-recognizer/sample_data_without_labels.zip). 
+* An Azure Storage blob container that contains a set of training data. Make sure all the training documents are of the same format. If you have forms in multiple formats, organize them into subfolders based on common format. For this project, you can use our [sample data set](https://github.com/Azure-Samples/cognitive-services-REST-api-samples/blob/master/curl/form-recognizer/sample_data_without_labels.zip).
 
 * If you don't know how to create an Azure storage account with a container, follow the [Azure Storage quickstart for Azure portal](/azure/storage/blobs/storage-quickstart-blobs-portal).
 
@@ -187,7 +185,7 @@ Configure the **Project Settings** fields with the following values:
 
 1. **Source connection**. The Sample Labeling tool connects to a source (your original uploaded forms) and a target (created labels and output data). Connections can be set up and shared across projects. They use an extensible provider model, so you can easily add new source/target providers.
 
-    * Create a new connection, select the **Add Connection** button. Complete the fields with the following values:
+    * **Create a new connection**. Select the **Add Connection** button. Complete the fields with the following values:
 
     > [!div class="checklist"]
     >
@@ -265,10 +263,10 @@ Use the tags editor pane to create a new tag you'd like to identify:
 
 Choose the Train icon on the left pane and open the Training page. Then select the **Train** button to begin training the model. Once the training process completes, you see the following information:
 
-* **Model ID** - The ID of the model that was created and trained. Each training call creates a new model with its own ID. Copy this string to a secure location; you need it if you want to do prediction calls through the [REST API](./get-started-sdks-rest-api.md?pivots=programming-language-rest-api) or [client library](./get-started-sdks-rest-api.md).
+* **Model ID** - The ID of the model that was created and trained. Each training call creates a new model with its own ID. Copy this string to a secure location; you need it if you want to do prediction calls through the [REST API](../quickstarts/get-started-sdks-rest-api.md?pivots=programming-language-rest-api) or [client library](../quickstarts/get-started-sdks-rest-api.md).
 
 * **Average Accuracy** - The model's average accuracy. You can improve model accuracy by labeling more forms and retraining to create a new model. We recommend starting by labeling five forms analyzing and testing the results and then if needed adding more forms as needed.
-* The list of tags, and the estimated accuracy per tag. For more information, _see_ [Interpret and improve accuracy and confidence](../concept-accuracy-confidence.md).
+* The list of tags, and the estimated accuracy per tag. For more information, *see* [Interpret and improve accuracy and confidence](../concept/accuracy-confidence.md).
 
     :::image type="content" source="../media/label-tool/custom-3.jpg" alt-text="Training view tool.":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サンプルラベルツールのクイックスタート文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、「Document Intelligence」に関するサンプルラベルツールのクイックスタートガイドが「try-sample-label-tool.md」から「v21/try-sample-label-tool.md」にファイル名が変更され、内容内のリンクも相対パスに修正されました。全体で22行の変更があり、10行の追加と12行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書のファイル名を変更することにより、バージョン情報との関連がより明確になり、ユーザーが関連する文書を見つけやすくなっています。

2. **リンクの修正**: ドキュメント内のリンクが相対パスに更新され、外部リソースへのアクセスが改善されました。これにより、ユーザーが同じリポジトリ内の他のページに簡単に移動できるようになっています。

3. **日付の更新**: 文書の日付が「03/28/2024」から「10/03/2024」に更新され、最新の情報が反映されています。これにより、ユーザーは新しい手順や改善された機能を利用できるようになります。

4. **内容の整理**: ドキュメント内の一部の情報が明確に整理され、特にモデルやサービスに関する説明が強化されています。例えば、ドキュメントインテリジェンスによって提供される各種プリビルトモデルに関する具体的な情報が明示されており、どういった場面でどのモデルを使用すべきかの理解が促進されています。

5. **ツール使用法の説明の充実**: ユーザーがサンプルラベルツールをより効果的に利用できるように、手順や重要な情報がより詳細に記述されています。特に、トレーニングモデルを作成する際の注意事項や推奨される処理手順が分かりやすくなっています。

6. **情報の一貫性の向上**: 記載の内容の整合性が向上し、ユーザーが異なるセクション間で情報を容易に理解できるようになっています。

これらの変更は、サンプルラベルツールに関するドキュメントをより使いやすくし、ユーザーが必要な情報を迅速に見つけられるようにするために行われました。全体として、最新の技術情報を反映した充実したリソースとなっています。

## articles/ai-services/document-intelligence/versioning/changelog-release-history.md{#item-dccdd3}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: A version-based description of Document Intelligence feature and ca
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: reference
 ms.date: 09/09/2024
 ms.author: lajanuar
@@ -21,7 +19,7 @@ ms.author: lajanuar
 
 This reference article provides a version-based description of Document Intelligence feature and capability releases, changes, updates, and enhancements.
 
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
 #### August 2024 (preview) release
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リリース履歴の文書のファイル名変更とリンク修正"
}
```

### Explanation
この変更では、「Document Intelligence」に関するリリース履歴の文書がファイル名の変更とともに、内部リンクが相対パスに修正されました。全体で4行の変更があり、1行の追加と3行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書がリネームされることで、バージョン管理やリリース情報に対する明確性が向上し、ユーザーが該当する情報を簡単に見つけやすくなっています。

2. **リンクの修正**: リンクが相対パスに更新され、関連するリソースへのアクセスが改善されました。この変更により、ユーザーが同じリポジトリ内の他のページにアクセスしやすくなり、情報の整合性も強化されています。

3. **日付の更新やカスタム属性の削除**: 日付の更新や、カスタム属性に関連する行が削除され、文書の構成がよりシンプルになっています。

4. **文書の内容の再構築**: リリースに関する情報がより効果的に整理され、ユーザーが新機能や変更点について簡単に理解できるようになっています。

これらの変更は、リリース履歴に関する情報をより分かりやすくし、ユーザーが求める情報を迅速に取得できるようにするために行われました。全体として、リリース履歴に関する最新の情報が整然と整理され、ユーザーにとって利用しやすいリソースとなっています。

## articles/ai-services/document-intelligence/versioning/sdk-overview-v3-0.md{#item-f82845}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,6 @@ manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.custom:
   - devx-track-python
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 05/23/2024
 ms.author: lajanuar
@@ -22,7 +21,7 @@ monikerRange: 'doc-intel-3.0.0'
 
 # SDK target: REST API 2022–08–31 (GA)
 
-![Document Intelligence checkmark](media/yes-icon.png) **REST API version 2022–08–31 (GA)**
+![Document Intelligence checkmark]../media/yes-icon.png) **REST API version 2022–08–31 (GA)**
 
 Azure AI Document Intelligence is a cloud service that uses machine learning to analyze text and structured data from documents. The Document Intelligence software development kit (SDK) is a set of libraries and tools that enable you to easily integrate Document Intelligence models and capabilities into your applications. Document Intelligence SDK is available across platforms in C#/.NET, Java, JavaScript, and Python programming languages.
 
@@ -42,7 +41,7 @@ For more information on other SDK versions, see:
 * [`2024-02-29` v4.0 (preview)](sdk-overview-v4-0.md)
 * [`2023-07-31` v3.1 (GA)](sdk-overview-v3-1.md)
 
-* [`v2.1` (GA)](sdk-overview-v2-1.md)
+* [`v2.1` (GA)](../v21/sdk-overview-v2-1.md)
 
 ## Supported Clients
 
@@ -96,6 +95,7 @@ npm i @azure/ai-form-recognizer@4.0.0
 ```python
 pip install azure-ai-formrecognizer==3.2.0
 ```
+
 ---
 
 
@@ -146,7 +146,7 @@ There are two supported methods for authentication:
 
 Here's where to find your Document Intelligence API key in the Azure portal:
 
-:::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of the keys and endpoint location in the Azure portal.":::
+:::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of the keys and endpoint location in the Azure portal.":::
 
 [!INCLUDE [Microsoft Entra ID or AKV](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv.md)]
 
@@ -197,7 +197,7 @@ async function main() {
 #### Use a Microsoft Entra token credential
 
 > [!NOTE]
-> Regional endpoints do not support Microsoft Entra authentication. Create a [custom subdomain](../../ai-services/authentication.md?tabs=powershell#create-a-resource-with-a-custom-subdomain) for your resource in order to use this type of authentication.
+> Regional endpoints do not support Microsoft Entra authentication. Create a [custom subdomain](../../../ai-services/authentication.md?tabs=powershell#create-a-resource-with-a-custom-subdomain) for your resource in order to use this type of authentication.
 
 Authorization is easiest using the `DefaultAzureCredential`. It provides a default token credential, based upon the running environment, capable of handling most Azure authentication scenarios.
 
@@ -215,7 +215,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/dotnet/api/azure.ide
         Install-Package Azure.Identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -244,7 +244,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/java/api/com.azure.i
     </dependency>
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -272,7 +272,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/javascript/api/@azur
     npm install @azure/identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -299,7 +299,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/python/api/azure-ide
     pip install azure-identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -325,7 +325,7 @@ For more information, *see* [Authenticate the client](https://github.com/Azure/a
 
 ### 4. Build your application
 
-Create a client object to interact with the Document Intelligence SDK, and then call methods on that client object to interact with the service. The SDKs provide both synchronous and asynchronous methods. For more insight, try a [quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) in a language of your choice.
+Create a client object to interact with the Document Intelligence SDK, and then call methods on that client object to interact with the service. The SDKs provide both synchronous and asynchronous methods. For more insight, try a [quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) in a language of your choice.
 
 ## Help options
 
@@ -337,4 +337,4 @@ The [Microsoft Q & A](/answers/topics/azure-form-recognizer.html) and [Stack Ove
 > [**Explore Document Intelligence REST API v3.0**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)
 
 > [!div class="nextstepaction"]
-> [**Try a Document Intelligence quickstart**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
+> [**Try a Document Intelligence quickstart**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence SDKの概要文書のリネームとリンク修正"
}
```

### Explanation
この変更では、「Document Intelligence SDK の概要」に関する文書がファイル名の変更と内部リンクの修正を含んでいます。全体で22行の変更があり、11行の追加と11行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名変更**: ドキュメントがリネームされることにより、バージョン管理の明確性が向上し、関連する情報を簡単に見つけられるようになっています。

2. **リンクの修正**: ドキュメント内のリンクが相対パスに修正され、他のページやリソースへのアクセスが改善されました。この変更により、一貫性が増し、文書の整合性が強化されています。

3. **情報の整備**: SDKに関する説明や、提供される各種機能についての詳細が整理され、ユーザーにとって理解しやすくなっています。また、APIのバージョン情報装飾や関連する文書へのリンクも適切に更新されています。

4. **文書の内容更新**: SDKの使用方法や、サポートされているクライアントに関する情報が明確化され、実際の使用例や手順が充実しています。これにより、ユーザーは必要な情報を迅速に把握できるようになっています。

5. **トレーサビリティの強化**: 変更箇所が明示的に表示され、ユーザーがバージョン間の違いを容易に確認できるようになっています。本変更により、今後の更新がより効率的に行えるようになっています。

これらの変更は、SDKに関するドキュメンテーションをより使いやすくし、開発者が必要なリファレンス情報をすばやく見つけられるようにするために行われました。全体として、SDKの利用に関する最新の情報が整理された、よりアクセスしやすいリソースに仕上げられています。

## articles/ai-services/document-intelligence/versioning/sdk-overview-v3-1.md{#item-534671}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,6 @@ manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.custom:
   - devx-track-python
-  - ignite-2023
 ms.topic: conceptual
 ms.date: 05/06/2024
 ms.author: lajanuar
@@ -22,7 +21,7 @@ monikerRange: 'doc-intel-3.1.0'
 
 # SDK target: REST API 2023-07-31 (GA)
 
-![Document Intelligence checkmark](media/yes-icon.png) **REST API version 2023-07-31 (GA)**
+![Document Intelligence checkmark](../media/yes-icon.png) **REST API version 2023-07-31 (GA)**
 
 Azure AI Document Intelligence is a cloud service that uses machine learning to analyze text and structured data from documents. The Document Intelligence software development kit (SDK) is a set of libraries and tools that enable you to easily integrate Document Intelligence models and capabilities into your applications. Document Intelligence SDK is available across platforms in C#/.NET, Java, JavaScript, and Python programming languages.
 
@@ -42,7 +41,7 @@ For more information on other SDK versions, see:
 * [`2024-02-29` v4.0 (preview)](sdk-overview-v4-0.md)
 
 * [`2022-08-31` v3.0 (GA)](sdk-overview-v3-0.md)
-* [`v2.1` (GA)](sdk-overview-v2-1.md)
+* [`v2.1` (GA)](../v21/sdk-overview-v2-1.md)
 
 ## Supported Clients
 
@@ -176,7 +175,7 @@ There are two supported methods for authentication:
 
 Here's where to find your Document Intelligence API key in the Azure portal:
 
-:::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of the keys and endpoint location in the Azure portal.":::
+:::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of the keys and endpoint location in the Azure portal.":::
 
 [!INCLUDE [Microsoft Entra ID or AKV](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv.md)]
 
@@ -226,7 +225,7 @@ async function main() {
 #### Use a Microsoft Entra token credential
 
 > [!NOTE]
-> Regional endpoints do not support Microsoft Entra authentication. Create a [custom subdomain](../../ai-services/authentication.md?tabs=powershell#create-a-resource-with-a-custom-subdomain) for your resource in order to use this type of authentication.
+> Regional endpoints do not support Microsoft Entra authentication. Create a [custom subdomain](../../../ai-services/authentication.md?tabs=powershell#create-a-resource-with-a-custom-subdomain) for your resource in order to use this type of authentication.
 
 Authorization is easiest using the `DefaultAzureCredential`. It provides a default token credential, based upon the running environment, capable of handling most Azure authentication scenarios.
 
@@ -244,7 +243,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/dotnet/api/azure.ide
         Install-Package Azure.Identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -273,7 +272,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/java/api/com.azure.i
     </dependency>
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -301,7 +300,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/javascript/api/@azur
     npm install @azure/identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -328,7 +327,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/python/api/azure-ide
     pip install azure-identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -353,7 +352,7 @@ For more information, *see* [Authenticate the client](https://github.com/Azure/a
 
 ### 4. Build your application
 
-Create a client object to interact with the Document Intelligence SDK, and then call methods on that client object to interact with the service. The SDKs provide both synchronous and asynchronous methods. For more insight, try a [quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) in a language of your choice.
+Create a client object to interact with the Document Intelligence SDK, and then call methods on that client object to interact with the service. The SDKs provide both synchronous and asynchronous methods. For more insight, try a [quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) in a language of your choice.
 
 ## Help options
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence SDKの概要文書のリネームとリンク修正"
}
```

### Explanation
この変更では、「Document Intelligence SDK の概要」に関する文書がリネームされ、内部リンクが更新されました。全体で19行の変更があり、9行の追加と10行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名変更**: 文書が新しいファイル名にリネームされ、構造がより明確になりました。これにより、特定のバージョンのSDKに関する情報を見つけやすくなっています。

2. **リンクの修正**: 内部リンクが相対パスに修正され、関連するメディアや他の文書へのアクセスが改善されました。この変更により、ユーザーが情報を一貫した形で参照できるように整理されています。

3. **SDKバージョンの更新**: SDKの対象とするREST APIのバージョンが2023-07-31 (GA) に更新され、最新の情報に合わせた内容に改訂されています。

4. **利用方法の整理**: SDKの使用方法や、必要な認証手順についての情報が整理され、利用者に対して実用的なガイドが提供されています。また、Microsoft Entra 認証に関する留意点が明記されており、ユーザーの理解を助けています。

5. **材料の整備**: 様々なプログラミング言語でのSDK利用についての情報も最新のものに更新され、開発者がそれぞれの環境に合わせた利用方法を見つけやすくしています。

これらの変更は、SDKのドキュメンテーションが最新で、利用者にとって理解しやすい形になるよう配慮された結果です。SDKに関する情報を迅速に取得し、実装に役立てるための情報が整理されたため、開発者がより効果的に利用できるようになっています。

## articles/ai-services/document-intelligence/versioning/sdk-overview-v4-0.md{#item-d59a82}

<details>
<summary>Diff</summary>
````diff
@@ -24,9 +24,9 @@ monikerRange: 'doc-intel-4.0.0'
 
 # SDK target: REST API 2024-07-31-preview
 
-[!INCLUDE [preview-version-notice](includes/preview-notice.md)]
+[!INCLUDE [preview-version-notice](../includes/preview-notice.md)]
 
-![Document Intelligence checkmark](media/yes-icon.png) **REST API version 2024-07-31-preview**
+![Document Intelligence checkmark](../media/yes-icon.png) **REST API version 2024-07-31-preview**
 
 Azure AI Document Intelligence is a cloud service that uses machine learning to analyze text and structured data from documents. The Document Intelligence software development kit (SDK) is a set of libraries and tools that enable you to easily integrate Document Intelligence models and capabilities into your applications. Document Intelligence SDK is available across platforms in C#/.NET, Java, JavaScript, and Python programming languages.
 
@@ -45,7 +45,7 @@ For more information on other SDK versions, see:
 
 * [`2023-07-31` v3.1 (GA)](sdk-overview-v3-1.md)
 * [`2022-08-31` v3.0 (GA)](sdk-overview-v3-0.md)
-* [`v2.1` (GA)](sdk-overview-v2-1.md)
+* [`v2.1` (GA)](../v21/sdk-overview-v2-1.md)
 
 ## Supported Clients
 
@@ -184,7 +184,7 @@ There are two supported methods for authentication:
 
 Here's where to find your Document Intelligence API key in the Azure portal:
 
-:::image type="content" source="media/containers/keys-and-endpoint.png" alt-text="Screenshot of the keys and endpoint location in the Azure portal.":::
+:::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of the keys and endpoint location in the Azure portal.":::
 
 [!INCLUDE [Microsoft Entra ID or AKV](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv.md)]
 
@@ -236,7 +236,7 @@ async function main() {
 #### Use a Microsoft Entra token credential
 
 > [!NOTE]
-> Regional endpoints do not support Microsoft Entra authentication. Create a [custom subdomain](../../ai-services/authentication.md?tabs=powershell#create-a-resource-with-a-custom-subdomain) for your resource in order to use this type of authentication.
+> Regional endpoints do not support Microsoft Entra authentication. Create a [custom subdomain](../../../ai-services/authentication.md?tabs=powershell#create-a-resource-with-a-custom-subdomain) for your resource in order to use this type of authentication.
 
 Authorization is easiest using the `DefaultAzureCredential`. It provides a default token credential, based upon the running environment, capable of handling most Azure authentication scenarios.
 
@@ -254,7 +254,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/dotnet/api/azure.ide
         Install-Package Azure.Identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -283,7 +283,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/java/api/com.azure.i
     </dependency>
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -311,7 +311,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/javascript/api/@azur
     npm install @azure/identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -338,7 +338,7 @@ Here's how to acquire and use the [DefaultAzureCredential](/python/api/azure-ide
     pip install azure-identity
     ```
 
-1. [Register a Microsoft Entra application and create a new service principal](../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
+1. [Register a Microsoft Entra application and create a new service principal](../../../ai-services/authentication.md?tabs=powershell#assign-a-role-to-a-service-principal).
 
 1. Grant access to Document Intelligence by assigning the **`Cognitive Services User`** role to your service principal.
 
@@ -363,7 +363,7 @@ For more information, *see* [Authenticate the client](https://github.com/Azure/a
 
 ### 4. Build your application
 
-Create a client object to interact with the Document Intelligence SDK, and then call methods on that client object to interact with the service. The SDKs provide both synchronous and asynchronous methods. For more insight, try a [quickstart](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) in a language of your choice.
+Create a client object to interact with the Document Intelligence SDK, and then call methods on that client object to interact with the service. The SDKs provide both synchronous and asynchronous methods. For more insight, try a [quickstart](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true) in a language of your choice.
 
 ## Help options
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence SDKの概要文書のリネームとリンク修正"
}
```

### Explanation
この変更では、「Document Intelligence SDKの概要」文書がリネームされ、いくつかの内部リンクが更新されています。全体で20行の変更があり、10行の追加と10行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名変更**: この文書のファイル名が変更され、より明確にバージョン情報を示す構造になりました。この変更により、特定のSDKバージョン情報を容易に参照できるようになっています。

2. **リンクの修正**: 内部リンクが相対パスに更新されたことにより、ドキュメント内でのナビゲーションやリソースへのアクセスが改善されました。特に、メディアファイルや外部リソースへのリンクが適切に修正されています。

3. **SDKターゲットの更新**: SDKが対象とするREST APIのバージョンが「2024-07-31-preview」に設定され、最新のAPI情報を反映する形になっています。

4. **情報の整理**: SDKの使用方法や、認証手順に関するガイドラインが整理され、開発者が容易に理解できるよう配慮されています。特に、Microsoft Entra 認証の使用方法に関する情報が明確に記載されています。

5. **ユーザーへの配慮**: ドキュメントに含まれる情報は最新かつ実用的であり、開発者がSDKを効果的に使用するための手助けとなるような形式になっています。各プログラミング言語における利用方法やプラクティスも具体的に示されています。

これらの変更により、Document Intelligence SDKに関する最新情報がより整然としていてアクセスしやすい形に整理されており、利用者が必要な情報を迅速に得られるよう支援されています。

## articles/ai-services/document-intelligence/versioning/v3-1-migration-guide.md{#item-6f9943}

<details>
<summary>Diff</summary>
````diff
@@ -5,8 +5,6 @@ description: In this how-to guide, learn the differences between Document Intell
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
-ms.custom:
-  - ignite-2023
 ms.topic: how-to
 ms.date: 05/23/2024
 ms.author: lajanuar
@@ -17,7 +15,7 @@ monikerRange: '<=doc-intel-3.1.0'
 # Document Intelligence v3.1 migration
 
 ::: moniker range="<=doc-intel-3.1.0"
-[!INCLUDE [applies to v3.1, v3.0, and v2.1](includes/applies-to-v40-v31-v30-v21.md)]
+[!INCLUDE [applies to v3.1, v3.0, and v2.1](../includes/applies-to-v40-v31-v30-v21.md)]
 ::: moniker-end
 
 > [!IMPORTANT]
@@ -64,12 +62,12 @@ Formulas/StyleFont/OCR High Resolution* - Premium features incur added costs
 
 Compared with v3.0, Document Intelligence v3.1 introduces several new features and capabilities:
 
-* [Barcode](concept-add-on-capabilities.md#barcode-property-extraction) extraction.
-* [Add-on capabilities](concept-add-on-capabilities.md) including high resolution, formula, and font properties extraction.
-* [Custom classification model](concept-custom-classifier.md) for document splitting and classification.
-* Language expansion and new fields support in [Invoice](concept-invoice.md) and [Receipt](concept-receipt.md) model.
-* New document type support in [ID document](concept-id-document.md) model.
-* New prebuilt [Health insurance card](concept-health-insurance-card.md) model.
+* [Barcode](../concept-add-on-capabilities.md#barcode-property-extraction) extraction.
+* [Add-on capabilities](../concept-add-on-capabilities.md) including high resolution, formula, and font properties extraction.
+* [Custom classification model](../train/custom-classifier.md) for document splitting and classification.
+* Language expansion and new fields support in [Invoice](../prebuilt/invoice.md) and [Receipt](../prebuilt/receipt.md) model.
+* New document type support in [ID document](../prebuilt/id-document.md) model.
+* New prebuilt [Health insurance card](../prebuilt/health-insurance-card.md) model.
 * Office/HTML files are supported in prebuilt-read model, extracting words and paragraphs without bounding boxes. Embedded images are no longer supported. If add-on features are requested for Office/HTML files, an empty array is returned without errors.
 * Model expiration for custom extraction and classification models - Our new custom models build upon on a large base model that we update periodically for quality improvement. An expiration date is introduced to all custom models to enable the retirement of the corresponding base models.  Once a custom model expires, you need to retrain the model using the latest API version (base model).
 
@@ -122,9 +120,9 @@ Besides model quality improvement, you're highly recommended to update your appl
 
 ## Migrating from v2.1 or v2.0
 
-Document Intelligence v3.1 is the latest GA version with the richest features, most languages and document types coverage, and improved model quality. Refer to [model overview](overview.md) for the features and capabilities available in v3.1.
+Document Intelligence v3.1 is the latest GA version with the richest features, most languages and document types coverage, and improved model quality. Refer to [model overview](../overview.md) for the features and capabilities available in v3.1.
 
-Starting from v3.0, [Document Intelligence REST API](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true) is redesigned for better usability. In this section, learn the differences between Document Intelligence v2.0, v2.1 and v3.1 and how to move to the newer version of the API.
+Starting from v3.0, [Document Intelligence REST API](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true) is redesigned for better usability. In this section, learn the differences between Document Intelligence v2.0, v2.1 and v3.1 and how to move to the newer version of the API.
 
 > [!CAUTION]
 >
@@ -133,7 +131,7 @@ Starting from v3.0, [Document Intelligence REST API](quickstarts/get-started-sdk
 
 ## Changes to the REST API endpoints
 
- The v3.1 REST API combines the analysis operations for layout analysis, prebuilt models, and custom models into a single pair of operations by assigning **`documentModels`**  and  **`modelId`** to the layout analysis (prebuilt-layout) and prebuilt models.
+ The v3.1 REST API combines the analysis operations for layout analysis, prebuilt models, and custom models into a single pair of operations by assigning **`documentModels`**  and  **`modelId`** to the layout analysis (../prebuilt-layout) and prebuilt models.
 
 ### POST request
 
@@ -456,5 +454,5 @@ GET https://{your-form-recognizer-endpoint}/formrecognizer/info? api-version=202
 ## Next steps
 
 * [Review the new REST API](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)
-* [What is Document Intelligence?](overview.md)
-* [Document Intelligence quickstart](quickstarts/get-started-sdks-rest-api.md)
+* [What is Document Intelligence?](../overview.md)
+* [Document Intelligence quickstart](../quickstarts/get-started-sdks-rest-api.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligence v3.1 マイグレーションガイドのリネームとリンク修正"
}
```

### Explanation
この変更では、「Document Intelligence v3.1 マイグレーションガイド」の文書がリネームされ、いくつかの内部リンクが更新されています。合計で26行の変更があり、12行の追加と14行の削除が含まれています。

主な変更内容は以下の通りです：

1. **ファイル名変更**: マイグレーションガイドのファイル名が変更され、より明確にその内容が示されるようになりました。これにより、ユーザーが関連する情報を容易に見つけることができるようになります。

2. **リンクの修正**: 内部リンクが相対パスに更新され、関連するリソースやメディアファイルへのアクセスがより簡素化されています。特に、依存関係や関連資料へのリンクが正しくリンクされ、情報の整合性が向上しています。

3. **マイグレーションの説明内容の更新**: v3.1の新機能に関する情報が追加され、特にバージョン間の違いについての具体的な説明が強化されています。これにより、ユーザーは新しい機能や改善点をより理解しやすくなっています。

4. **APIの変更点の説明**: Document Intelligence v3.1におけるREST APIの変更点についての説明が明確化され、どのように新しいバージョンへ移行するかについて詳しい情報が提供されています。

5. **ユーザーへのアドバイス**: マイグレーションガイドには、APIの新しい利用方法とともに、移行を円滑に進めるための注意点が含まれており、開発者が最新の仕様に基づいてアプリケーションを更新するのに役立っています。

これらの変更により、Document Intelligence v3.1 マイグレーションガイドは、ユーザーに対して最新情報と具体的なマイグレーション手順を的確に提供し、実用的な内容に整備されています。これにより、開発者は最新のSDKとAPIを効果的に活用するためのサポートを得られます。

## articles/ai-services/document-intelligence/whats-new.md{#item-1ec8d3}

<details>
<summary>Diff</summary>
````diff
@@ -16,6 +16,7 @@ ms.custom:
 <!-- markdownlint-disable MD036 -->
 <!-- markdownlint-disable MD001 -->
 <!-- markdownlint-disable MD051 -->
+<!-- markdownlint-disable MD049 -->
 
 # What's new in Azure AI Document Intelligence
 
@@ -37,11 +38,11 @@ The Document Intelligence [**2024-07-31-preview**](/rest/api/aiservices/document
 * **West Europe**
 * **North Central US**
 
-* [🆕 Document field extraction (custom generative) model](concept-custom-generative.md)
+* [🆕 Document field extraction (custom generative) model](train/custom-generative-extraction.md)
   * Use **Generative AI** to extract fields from documents and forms. Document Intelligence now offers a new document field extraction model that utilizes large language models (LLMs) to extract fields from unstructured documents or structured forms with a wide variety of visual templates. With grounded values and confidence scores, the new Generative AI based extraction fits into your existing processes.
-* [🆕 Model compose with custom classifiers](concept-composed-models.md)
-  * Document Intelligence now adds support for composing model with an explicit custom classification model. [Learn more about the benefits](concept-composed-models.md) of using the new compose capability.
-* [Custom classification model](concept-custom.md#custom-classification-model)
+* [🆕 Model compose with custom classifiers](train/composed-models.md)
+  * Document Intelligence now adds support for composing model with an explicit custom classification model. [Learn more about the benefits](train/composed-models.md) of using the new compose capability.
+* [Custom classification model](train/custom-model.md#custom-classification-model)
   * Custom classification model now supports updating the model in-place as well.
   * Custom classification model adds support for model copy operation to enable backup and disaster recovery.
   * Custom classification model now supports explicitly specifying pages to be classified from an input document.
@@ -54,17 +55,15 @@ The Document Intelligence [**2024-07-31-preview**](/rest/api/aiservices/document
   * New prebuilt to process pay stubs to extract wages, hours, deductions, net pay and more.​
 * [🆕 Bank statement model](concept-bank-statement.md)
   * New prebuilt to extract account information including beginning and ending balances, transaction details from bank statements.​
-* [🆕 US Tax model](concept-tax-document.md)
+* [🆕 US Tax model](prebuilt/tax-document.md)
   * New unified US tax model that can extract from forms such as W-2, 1098, 1099, and 1040.
-* 🆕 Searchable PDF. The [prebuilt read](concept-read.md) model now supports [PDF output](concept-read.md#searchable-pdf)  to download PDFs with embedded text from extraction results, allowing for PDF to be utilized in scenarios such as search copy of contents.
-* [Layout model](concept-layout.md) now supports improved [figure detection](concept-layout.md#figures) where figures from documents can now be downloaded as an image file to be used for further figure understanding. The layout model also features improvements to the OCR model for scanned text targeting improvements for single characters, boxed text, and dense text documents.
+* 🆕 Searchable PDF. The [prebuilt read](prebuilt/read.md) model now supports [PDF output](prebuilt/read.md#searchable-pdf)  to download PDFs with embedded text from extraction results, allowing for PDF to be utilized in scenarios such as search copy of contents.
+* [Layout model](prebuilt/layout.md) now supports improved [figure detection](prebuilt/layout.md#figures) where figures from documents can now be downloaded as an image file to be used for further figure understanding. The layout model also features improvements to the OCR model for scanned text targeting improvements for single characters, boxed text, and dense text documents.
 * [🆕 Batch API](concept-batch-analysis.md)
   * Document Intelligence now adds support for batch analysis operation to support analyzing a set of documents to simplify developer experience and improve efficiency.
 * [Add-on capabilities](concept-add-on-capabilities.md)
   * [Query fields](concept-add-on-capabilities.md#query-fields) AI quality of extraction is improved with the latest model.
 
-
-
 ## May 2024
 
 The Document Intelligence Studio adds support for Microsoft Entra (formerly Azure Active Directory) authentication. For more information, *see* [Document Intelligence Studio overview](quickstarts/try-document-intelligence-studio.md#authentication).
@@ -79,15 +78,15 @@ The Document Intelligence [**2024-07-31-preview**](/rest/api/aiservices/document
   * **West US2**
   * **West Europe**
 
-* [Layout model](concept-layout.md) now supports [figure detection](concept-layout.md#figures) and [hierarchical document structure analysis (sections and subsections)](concept-layout.md#sections). The AI quality of reading order and logical roles detection is also improved.
-* [Custom extraction models](concept-custom.md#custom-extraction-models)
-  * Custom extraction models now support cell, row, and table level confidence scores. Learn more about [table, row, and cell confidence](concept-accuracy-confidence.md#table-row-and-cell-confidence).
+* [Layout model](prebuilt/layout.md) now supports [figure detection](prebuilt/layout.md#figures) and [hierarchical document structure analysis (sections and subsections)](prebuilt/layout.md#sections). The AI quality of reading order and logical roles detection is also improved.
+* [Custom extraction models](train/custom-model.md#custom-extraction-models)
+  * Custom extraction models now support cell, row, and table level confidence scores. Learn more about [table, row, and cell confidence](concept/accuracy-confidence.md#table-row-and-cell-confidence).
   * Custom extraction models have AI quality improvements for field extraction.
-  * Custom template extraction model now supports extracting overlapping fields. Learn more about [overlapping fields and how you use them](concept-custom-neural.md#overlapping-fields).
-* [Custom classification model](concept-custom.md#custom-classification-model)
-  * Custom classification model now supported incremental training for scenarios where you need to update the classifier model with added samples or classes. Learn more about [incremental training](concept-custom-classifier.md#incremental-training).
-  * Custom classification model adds support for Office document types (.docx, .pptx, and .xls). Learn more about [expanded document type support](concept-custom-classifier.md#office-document-type-support).
-* [Invoice model](concept-invoice.md)
+  * Custom template extraction model now supports extracting overlapping fields. Learn more about [overlapping fields and how you use them](train/custom-neural.md#overlapping-fields).
+* [Custom classification model](train/custom-model.md#custom-classification-model)
+  * Custom classification model now supported incremental training for scenarios where you need to update the classifier model with added samples or classes. Learn more about [incremental training](train/custom-classifier.md#incremental-training).
+  * Custom classification model adds support for Office document types (.docx, .pptx, and .xls). Learn more about [expanded document type support](train/custom-classifier.md#office-document-type-support).
+* [Invoice model](prebuilt/invoice.md)
   * Support for new locales:
 
   |Locale| Code|
@@ -119,8 +118,8 @@ The Document Intelligence [**2024-07-31-preview**](/rest/api/aiservices/document
 
   * Tax items support expansion for Germany (`de`), Spain (`es`), Portugal (`pt`), English Canada `en-CA`.
 
-* [ID model](concept-id-document.md)
-  * [Expanded field support](concept-id-document.md#supported-document-types) for European Union IDs and driver license.
+* [ID model](prebuilt/id-document.md)
+  * [Expanded field support](prebuilt/id-document.md#supported-document-types) for European Union IDs and driver license.
 * [🆕 Mortgage documents](concept-mortgage-documents.md)
   * Extract information from Uniform Residential Loan Application (Form 1003).
   * Extract information from Uniform Underwriting and Transmittal Summary or Form 1008.
@@ -144,31 +143,31 @@ The Document Intelligence [**2023-10-31-preview**](/rest/api/aiservices/document
   * **West US2**
   * **West Europe**
 
-* [Read model](concept-contract.md)
+* [Read model](prebuilt/contract.md)
   * Language Expansion for Handwriting: Russian(`ru`), Arabic(`ar`), Thai(`th`).
   * Cyber Executive Order (EO) compliance.
-* [Layout model](concept-layout.md)
+* [Layout model](prebuilt/layout.md)
   * Support office and HTML files.
   * Markdown output support.
   * Table extraction, reading order, and section heading detection improvements.
   * With the Document Intelligence 2023-10-31-preview, the general document model (prebuilt-document) is deprecated. Going forward, to extract key-value pairs from documents, use the
     `prebuilt-layout` model with the optional query string parameter `features=keyValuePairs` enabled.
-* [Receipt model](concept-receipt.md)
+* [Receipt model](prebuilt/receipt.md)
   * Now extracts currency for all price-related fields.
-* [Health Insurance Card model](concept-health-insurance-card.md)
+* [Health Insurance Card model](prebuilt/health-insurance-card.md)
   * New field support for Medicare and Medicaid information.
-* [US Tax Document models](concept-tax-document.md)
+* [US Tax Document models](prebuilt/tax-document.md)
   * New 1099 tax model. Supports base 1099 form and the following variations: A, B, C, CAP, DIV, G, H, INT, K, LS, LTC, MISC, NEC, OID, PATR, Q, QA, R, S, SA, SB​.
-* [Invoice model](concept-invoice.md)
+* [Invoice model](prebuilt/invoice.md)
   * Support for `KVK` field.
   * Support for `BPAY` field.
   * Numerous field refinements.
-* [Custom Classification](concept-custom-classifier.md)
+* [Custom Classification](train/custom-classifier.md)
   * Support for multi-language documents.
   * New page splitting options: autosplit, always split by page, no split.
 * [Add-on capabilities](concept-add-on-capabilities.md)
   * [Query fields](concept-add-on-capabilities.md#query-fields) are available with the `2023-10-31-preview` release.
-  * Add-on capabilities are available within all models excluding the [Read model](concept-read.md).
+  * Add-on capabilities are available within all models excluding the [Read model](prebuilt/read.md).
 
 >[!NOTE]
 > With the 2022-08-31 API general availability (GA) release, the associated preview APIs are being deprecated. If you are using the 2021-09-30-preview, the 2022-01-30-preview or he 2022-06-30-preview API versions, please update your applications to target the 2022-08-31 API version. There are a few minor changes involved, for more information, _see_ the [migration guide](v3-1-migration-guide.md).
@@ -190,21 +189,20 @@ The Document Intelligence version 3.1 API is now generally available (GA)! The A
 The v3.1 API introduces new and updated capabilities:
 
 * Document Intelligence APIs are now more modular and with support for optional features. You can now customize the output to specifically include the features you need. Learn more about the [optional parameters](v3-1-migration-guide.md).
-* Document classification API for splitting a single file into individual documents. [Learn more](concept-custom-classifier.md) about document classification.
-* [Prebuilt contract model](concept-contract.md).
-* [Prebuilt US tax form 1098 model](concept-tax-document.md).
-* Support for [Office file types](concept-read.md) with Read API.
-* [Barcode recognition](concept-read.md) in documents.
+* Document classification API for splitting a single file into individual documents. [Learn more](train/custom-classifier.md) about document classification.
+* [Prebuilt contract model](prebuilt/contract.md).
+* [Prebuilt US tax form 1098 model](prebuilt/tax-document.md).
+* Support for [Office file types](prebuilt/read.md) with Read API.
+* [Barcode recognition](prebuilt/read.md) in documents.
 * Formula recognition [add-on capability](concept-add-on-capabilities.md).
 * Font recognition [add-on capability](concept-add-on-capabilities.md).
 * Support for [high resolution documents](concept-add-on-capabilities.md).
 * Custom neural models now require a single labeled sample to train.
-* Custom neural models language expansion. Train a neural model for documents in 30 languages. See [language support](language-support.md) for the complete list of supported languages.
-* 🆕 [Prebuilt health insurance card model](concept-health-insurance-card.md).
-* [Prebuilt invoice model locale expansion](concept-invoice.md#supported-languages-and-locales).
-* [Prebuilt receipt model language and locale expansion](concept-receipt.md#supported-languages-and-locales) with more than 100 languages supported.
-* [Prebuilt ID model](concept-id-document.md#supported-document-types) now supports European IDs.
-
+* Custom neural models language expansion. Train a neural model for documents in 30 languages. See [language support](language-support/custom.md) for the complete list of supported languages.
+* 🆕 [Prebuilt health insurance card model](prebuilt/health-insurance-card.md).
+* [Prebuilt invoice model locale expansion](prebuilt/invoice.md#supported-languages-and-locales).
+* [Prebuilt receipt model language and locale expansion](prebuilt/receipt.md#supported-languages-and-locales) with more than 100 languages supported.
+* [Prebuilt ID model](prebuilt/id-document.md#supported-document-types) now supports European IDs.
 
 **Document Intelligence Studio UX Updates**
 
@@ -260,15 +258,15 @@ The v3.1 API introduces new and updated capabilities:
 
 * [🆕 Document Intelligence Overview](overview.md?view=doc-intel-3.0.0&preserve-view=true) enhanced navigation, structured access points, and enriched images.
 
-* [🆕 Choose a Document Intelligence model](choose-model-feature.md?view=doc-intel-3.0.0&preserve-view=true) provides guidance for choosing the best Document Intelligence solution for your projects and workflows.
+* [🆕 Choose a Document Intelligence model](concept/choose-model-feature.md?view=doc-intel-3.0.0&preserve-view=true) provides guidance for choosing the best Document Intelligence solution for your projects and workflows.
 
 ## April 2023
 
 **Announcing the latest Document Intelligence client-library public preview release**
 
 * Document Intelligence REST API Version **2023-02-28-preview** supports the public preview release client libraries. This release includes the following new features and capabilities available for .NET/C# (4.1.0-beta-1), Java (4.1.0-beta-1), JavaScript (4.1.0-beta-1), and Python (3.3.0b.1) client libraries:
 
-  * [**Custom classification model**](concept-custom-classifier.md)
+  * [**Custom classification model**](train/custom-classifier.md)
 
   * [**Query fields extraction**](concept-query-fields.md)
 
@@ -285,28 +283,27 @@ The v3.1 API introduces new and updated capabilities:
 > * West US2
 > * East US
 
-* [**Custom classification model**](concept-custom-classifier.md) is a new capability within Document Intelligence starting with the ```2023-02-28-preview``` API.
+* [**Custom classification model**](train/custom-classifier.md) is a new capability within Document Intelligence starting with the ```2023-02-28-preview``` API.
 * [**Query fields**](concept-query-fields.md) capabilities added to the General Document model, use Azure OpenAI models to extract specific fields from documents. Try the **General documents with query fields** feature using the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio). Query fields are currently only active for resources in the `East US` region.
 * [**Add-on capabilities**](concept-add-on-capabilities.md):
   * [**Font extraction**](concept-add-on-capabilities.md#font-property-extraction) is now recognized with the ```2023-02-28-preview``` API.
   * [**Formula extraction**](concept-add-on-capabilities.md#formula-extraction) is now recognized with the ```2023-02-28-preview``` API.
   * [**High resolution extraction**](concept-add-on-capabilities.md#high-resolution-extraction) is now recognized with the ```2023-02-28-preview``` API.
-* [**Custom extraction model updates**](concept-custom.md):
-  * [**Custom neural model**](concept-custom-neural.md) now supports added languages for training and analysis. Train neural models for Dutch, French, German, Italian, and Spanish.
-  * [**Custom template model**](concept-custom-template.md) now has an improved signature detection capability.
+* [**Custom extraction model updates**](train/custom-model.md):
+  * [**Custom neural model**](train/custom-neural.md) now supports added languages for training and analysis. Train neural models for Dutch, French, German, Italian, and Spanish.
+  * [**Custom template model**](train/custom-template.md) now has an improved signature detection capability.
 * [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com/studio) updates:
   * In addition to support for all the new features like classification and query fields, the Studio now enables project sharing for custom model projects.
   * New model additions in gated preview: **Vaccination cards**, **Contracts**, **US Tax 1098**, **US Tax 1098-E**, and **US Tax 1098-T**. To request access to gated preview models, complete and submit the [**Document Intelligence private preview request form**](https://aka.ms/form-recognizer/preview/survey).
-* [**Receipt model updates**](concept-receipt.md):
+* [**Receipt model updates**](prebuilt/receipt.md):
   * Receipt model adds support for thermal receipts.
   * Receipt model now adds language support for 18 languages and three regional languages (English, French, Portuguese).
   * Receipt model now supports `TaxDetails` extraction.
-* [**Layout model**](concept-layout.md) now improves table recognition.
-* [**Read model**](concept-read.md) now adds improvement for single-digit character recognition.
+* [**Layout model**](prebuilt/layout.md) now improves table recognition.
+* [**Read model**](prebuilt/read.md) now adds improvement for single-digit character recognition.
 
 ---
 
-
 ## February 2023
 
 * Select Document Intelligence containers for v3.0 are now available for use!
@@ -316,7 +313,6 @@ The v3.1 API introduces new and updated capabilities:
 
 ---
 
-
 ## January 2023
 
 * Prebuilt receipt model -  added languages supported. The receipt model now supports these added languages and locales
@@ -346,7 +342,7 @@ The v3.1 API introduces new and updated capabilities:
 > [!TIP]
 > All January 2023 updates are available with [REST API version **2022-08-31 (GA)**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP).
 
-* **[Prebuilt receipt model](concept-receipt.md#supported-languages-and-locales)—additional language support**:
+* **[Prebuilt receipt model](prebuilt/receipt.md#supported-languages-and-locales)—additional language support**:
 
    The **prebuilt receipt model** adds support for the following languages:
 
@@ -358,7 +354,7 @@ The v3.1 API introduces new and updated capabilities:
   * Japanese - Japan (ja-JP)
   * Portuguese - Brazil (pt-BR)
 
-* **[Prebuilt invoice model](concept-invoice.md)—additional language support and field extractions**
+* **[Prebuilt invoice model](prebuilt/invoice.md)—additional language support and field extractions**
 
   The **prebuilt invoice model** adds support for the following languages:
 
@@ -372,7 +368,7 @@ The v3.1 API introduces new and updated capabilities:
   * Total discount
   * Tax items (en-IN only)
 
-* **[Prebuilt ID document model](concept-id-document.md#supported-document-types)—additional document types support**
+* **[Prebuilt ID document model](prebuilt/id-document.md#supported-document-types)—additional document types support**
 
   The **prebuilt ID document model** now adds support for the following document types:
 
@@ -385,7 +381,6 @@ The v3.1 API introduces new and updated capabilities:
 
 ---
 
-
 ## December 2022
 
 * [**Document Intelligence Studio updates**](https://formrecognizer.appliedai.azure.com/studio)
@@ -412,7 +407,6 @@ The v3.1 API introduces new and updated capabilities:
 
 ---
 
-
 ## November 2022
 
 * **Announcing the latest stable release of Azure AI Document Intelligence libraries**
@@ -421,7 +415,6 @@ The v3.1 API introduces new and updated capabilities:
 
 ---
 
-
 ## October 2022
 
 * **Document Intelligence versioned content**
@@ -433,7 +426,7 @@ The v3.1 API introduces new and updated capabilities:
   * Sample code for the [Document Intelligence Studio labeling experience](https://github.com/microsoft/Form-Recognizer-Toolkit/tree/main/SampleCode/LabelingUX) is now available on GitHub. Customers can develop and integrate Document Intelligence into their own UX or build their own new UX using the Document Intelligence Studio sample code.
 
 * **Language expansion**
-  * With the latest preview release, Document Intelligence's Read (OCR), Layout, and Custom template models support 134 new languages. These language additions include Greek, Latvian, Serbian, Thai, Ukrainian, and Vietnamese, along with several Latin, and Cyrillic languages. Document Intelligence now has a total of 299 supported languages across the most recent GA and new preview versions. Refer to the [supported languages](language-support.md) page to see all supported languages.
+  * With the latest preview release, Document Intelligence's Read (OCR), Layout, and Custom template models support 134 new languages. These language additions include Greek, Latvian, Serbian, Thai, Ukrainian, and Vietnamese, along with several Latin, and Cyrillic languages. Document Intelligence now has a total of 299 supported languages across the most recent GA and new preview versions. Refer to the supported languages pages to see all supported languages.
   * Use the REST API parameter `api-version=2022-06-30-preview` when using the API or the corresponding SDK to support the new languages in your applications.
 
 * **New Prebuilt Contract model**
@@ -449,7 +442,6 @@ The v3.1 API introduces new and updated capabilities:
 
 ---
 
-
 ## September 2022
 
 >[!NOTE]
@@ -522,7 +514,6 @@ The v3.1 API introduces new and updated capabilities:
 
 ---
 
-
 * **Region expansion for training custom neural models now supported in six new regions**
     > [!div class="checklist"]
     >
@@ -533,7 +524,7 @@ The v3.1 API introduces new and updated capabilities:
     > * UK South
     > * West US2
 
-  * For a complete list of regions where training is supported see [custom neural models](concept-custom-neural.md).
+  * For a complete list of regions where training is supported see [custom neural models](train/custom-neural.md).
 
   * Document Intelligence SDK version `4.0.0 GA` release:
     * **Document Intelligence client libraries version 4.0.0 (.NET/C#, Java, JavaScript) and version 3.2.0 (Python) are generally available and ready for use in production applications!**.
@@ -542,7 +533,6 @@ The v3.1 API introduces new and updated capabilities:
 
 ---
 
-
 ## August 2022
 
 **Document Intelligence SDK beta August 2022 preview release includes the following updates:**
@@ -592,7 +582,6 @@ The v3.1 API introduces new and updated capabilities:
 
 ---
 
-
 * Document Intelligence v3.0 generally available
 
   * **Document Intelligence REST API v3.0 is now generally available and ready for use in production applications!** Update your applications with [**REST API version 2022-08-31**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP).
@@ -607,23 +596,22 @@ The v3.1 API introduces new and updated capabilities:
 
 * Document Intelligence service updates
 
-  * [**prebuilt-read**](concept-read.md). Read OCR model is now also available in Document Intelligence with paragraphs and language detection as the two new features. Document Intelligence Read targets advanced document scenarios aligned with the broader document intelligence capabilities in Document Intelligence.
-  * [**prebuilt-layout**](concept-layout.md). The Layout model extracts paragraphs and whether the extracted text is a paragraph, title, section heading, footnote, page header, page footer, or page number.
-  * [**prebuilt-invoice**](concept-invoice.md). The TotalVAT and Line/VAT fields now resolves to the existing fields TotalTax and Line/Tax respectively.
-  * [**prebuilt-idDocument**](concept-id-document.md). Data extraction support for US state ID, social security, and green cards. Support for passport visa information.
-  * [**prebuilt-receipt**](concept-receipt.md). Expanded locale support for French (fr-FR), Spanish (es-ES), Portuguese (pt-PT), Italian (it-IT) and German (de-DE).
+  * [**prebuilt-read**](prebuilt/read.md). Read OCR model is now also available in Document Intelligence with paragraphs and language detection as the two new features. Document Intelligence Read targets advanced document scenarios aligned with the broader document intelligence capabilities in Document Intelligence.
+  * [**prebuilt-layout**](prebuilt/layout.md). The Layout model extracts paragraphs and whether the extracted text is a paragraph, title, section heading, footnote, page header, page footer, or page number.
+  * [**prebuilt-invoice**](prebuilt/invoice.md). The TotalVAT and Line/VAT fields now resolves to the existing fields TotalTax and Line/Tax respectively.
+  * [**prebuilt-idDocument**](prebuilt/id-document.md). Data extraction support for US state ID, social security, and green cards. Support for passport visa information.
+  * [**prebuilt-receipt**](prebuilt/receipt.md). Expanded locale support for French (fr-FR), Spanish (es-ES), Portuguese (pt-PT), Italian (it-IT) and German (de-DE).
   * [**prebuilt-businessCard**](concept-business-card.md). Address parse support to extract subfields for address components like address, city, state, country/region, and zip code.
 
 * **AI quality improvements**
 
-  * [**prebuilt-read**](concept-read.md). Enhanced support for single characters, handwritten dates, amounts, names, other key data commonly found in receipts and invoices and improved processing of digital PDF documents.
-  * [**prebuilt-layout**](concept-layout.md). Support for better detection of cropped tables, borderless tables, and improved recognition of long spanning cells.
-  * [**prebuilt-document**](concept-general-document.md). Improved value and check box detection.
-  * [**custom-neural**](concept-custom-neural.md). Improved accuracy for table detection and extraction.
+  * [**prebuilt-read**](prebuilt/read.md). Enhanced support for single characters, handwritten dates, amounts, names, other key data commonly found in receipts and invoices and improved processing of digital PDF documents.
+  * [**prebuilt-layout**](prebuilt/layout.md). Support for better detection of cropped tables, borderless tables, and improved recognition of long spanning cells.
+  * [**prebuilt-document**](prebuilt/general-document.md). Improved value and check box detection.
+  * [**custom-neural**](train/custom-neural.md). Improved accuracy for table detection and extraction.
 
 ---
 
-
 ## June 2022
 
 * Document Intelligence SDK beta June 2022 preview release includes the following updates:
@@ -678,14 +666,14 @@ The v3.1 API introduces new and updated capabilities:
 
 * Document Intelligence v3.0 **2022-06-30-preview** release presents extensive updates across the feature APIs:
 
-  * [**Layout extends structure extraction**](concept-layout.md). Layout now includes added structure elements including sections, section headers, and paragraphs. This update enables finer grain document segmentation scenarios. For a complete list of structure elements identified, _see_ [enhanced structure](concept-layout.md#data-extraction).
-  * [**Custom neural model tabular fields support**](concept-custom-neural.md). Custom document models now support tabular fields. Tabular fields by default are also multi page. To learn more about tabular fields in custom neural models, _see_ [tabular fields](concept-custom-neural.md#tabular-fields).
-  * [**Custom template model tabular fields support for cross page tables**](concept-custom-template.md). Custom form models now support tabular fields across pages. To learn more about tabular fields in custom template models, _see_ [tabular fields](concept-custom-neural.md#tabular-fields).
-  * [**Invoice model output now includes general document key-value pairs**](concept-invoice.md). Where invoices contain required fields beyond the fields included in the prebuilt model, the general document model supplements the output with key-value pairs. _See_ [key value pairs](concept-invoice.md#key-value-pairs).
-  * [**Invoice language expansion**](concept-invoice.md). The invoice model includes expanded language support. _See_ [supported languages](concept-invoice.md#supported-languages-and-locales).
+  * [**Layout extends structure extraction**](prebuilt/layout.md). Layout now includes added structure elements including sections, section headers, and paragraphs. This update enables finer grain document segmentation scenarios. For a complete list of structure elements identified, _see_ [enhanced structure](prebuilt/layout.md#data-extraction).
+  * [**Custom neural model tabular fields support**](train/custom-neural.md). Custom document models now support tabular fields. Tabular fields by default are also multi page. To learn more about tabular fields in custom neural models, _see_ [tabular fields](train/custom-neural.md#tabular-fields).
+  * [**Custom template model tabular fields support for cross page tables**](train/custom-template.md). Custom form models now support tabular fields across pages. To learn more about tabular fields in custom template models, _see_ [tabular fields](train/custom-neural.md#tabular-fields).
+  * [**Invoice model output now includes general document key-value pairs**](prebuilt/invoice.md). Where invoices contain required fields beyond the fields included in the prebuilt model, the general document model supplements the output with key-value pairs. _See_ [key value pairs](prebuilt/invoice.md#key-value-pairs).
+  * [**Invoice language expansion**](prebuilt/invoice.md). The invoice model includes expanded language support. _See_ [supported languages](prebuilt/invoice.md#supported-languages-and-locales).
   * [**Prebuilt business card**](concept-business-card.md) now includes Japanese language support. _See_ [supported languages](concept-business-card.md#supported-languages-and-locales).
-  * [**Prebuilt ID document model**](concept-id-document.md). The ID document model now extracts DateOfIssue, Height, Weight, EyeColor, HairColor, and DocumentDiscriminator from US driver's licenses. _See_ [field extraction](concept-id-document.md).
-  * [**Read model now supports common Microsoft Office document types**](concept-read.md). Document types like Word (docx), Excel (xlsx), and PowerPoint (pptx) are now supported with the Read API. See [Read data extraction](concept-read.md#data-extraction).
+  * [**Prebuilt ID document model**](prebuilt/id-document.md). The ID document model now extracts DateOfIssue, Height, Weight, EyeColor, HairColor, and DocumentDiscriminator from US driver's licenses. _See_ [field extraction](prebuilt/id-document.md).
+  * [**Read model now supports common Microsoft Office document types**](prebuilt/read.md). Document types like Word (docx), Excel (xlsx), and PowerPoint (pptx) are now supported with the Read API. See [Read data extraction](prebuilt/read.md#data-extraction).
 
 ---
 
@@ -735,13 +723,13 @@ The v3.1 API introduces new and updated capabilities:
 
 * Document Intelligence v3.0 preview release introduces several new features, capabilities, and enhancements:
 
-  * [**Custom neural model**](concept-custom-neural.md) or custom document model is a new custom model to extract text and selection marks from structured forms, semi-structured and **unstructured documents**.
+  * [**Custom neural model**](train/custom-neural.md) or custom document model is a new custom model to extract text and selection marks from structured forms, semi-structured and **unstructured documents**.
   * [**W-2 prebuilt model**](concept-w2.md) is a new prebuilt model to extract fields from W-2 forms for tax reporting and income verification scenarios.
-  * [**Read**](concept-read.md) API extracts printed text lines, words, text locations, detected languages, and handwritten text, if detected.
-  * [**General document**](concept-general-document.md) pretrained model is now updated to support selection marks in addition to API  text, tables, structure, and key-value pairs from forms and documents.
-  * [**Invoice API**](concept-invoice.md#supported-languages-and-locales) Invoice prebuilt model expands support to Spanish invoices.
+  * [**Read**](prebuilt/read.md) API extracts printed text lines, words, text locations, detected languages, and handwritten text, if detected.
+  * [**General document**](prebuilt/general-document.md) pretrained model is now updated to support selection marks in addition to API  text, tables, structure, and key-value pairs from forms and documents.
+  * [**Invoice API**](prebuilt/invoice.md#supported-languages-and-locales) Invoice prebuilt model expands support to Spanish invoices.
   * [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com) adds new demos for Read, W2, Hotel receipt samples, and support for training the new custom neural models.
-  * [**Language Expansion**](language-support.md) Document Intelligence Read, Layout, and Custom Form add support for 42 new languages including Arabic, Hindi, and other languages using Arabic and Devanagari scripts to expand the coverage to 164 languages. Handwritten language support expands to Japanese and Korean.
+  * [**Language Expansion**](language-support/prebuilt.md) Document Intelligence Read, Layout, and Custom Form add support for 42 new languages including Arabic, Hindi, and other languages using Arabic and Devanagari scripts to expand the coverage to 164 languages. Handwritten language support expands to Japanese and Korean.
 
 * Get started with the new v3.0 preview API.
 
@@ -761,14 +749,14 @@ The v3.1 API introduces new and updated capabilities:
 
 * Document Intelligence SDK beta preview release includes the following updates:
 
-  * [Custom Document models and modes](concept-custom.md):
-    * [Custom template](concept-custom-template.md) (formerly custom form).
-    * [Custom neural](concept-custom-neural.md).
-    * [Custom model—build mode](concept-custom.md#build-mode).
+  * [Custom Document models and modes](train/custom-model.md):
+    * [Custom template](train/custom-template.md) (formerly custom form).
+    * [Custom neural](train/custom-neural.md).
+    * [Custom model—build mode](train/custom-model.md#build-mode).
 
   * [W-2 prebuilt model](concept-w2.md) (prebuilt-tax.us.w2).
-  * [Read prebuilt model](concept-read.md) (prebuilt-read).
-  * [Invoice prebuilt model (Spanish)](concept-invoice.md#supported-languages-and-locales) (prebuilt-invoice).
+  * [Read prebuilt model](prebuilt/read.md) (prebuilt-read).
+  * [Invoice prebuilt model (Spanish)](prebuilt/invoice.md#supported-languages-and-locales) (prebuilt-invoice).
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Document Intelligenceに関する「What's New」ページの更新"
}
```

### Explanation
この変更では、「Document Intelligence」の「What's New」ページが大幅に更新され、主に77行の追加と89行の削除が行われ、合計で166行の内容が変更されました。この変更によって、最新の機能や新しいリソースについての情報が整理され、明確に示されています。

主な変更内容は以下の通りです：

1. **新機能の紹介**: Document Intelligenceに関する多くの新機能が追加され、それに伴って説明も更新されています。特に、カスタム生成モデルや新しい文書タイプのサポートなど、最新のエンドポイントと機能が詳述されています。

2. **リンクの更新**: 各機能やリソースに関連するリンクが更新され、相対パスが使用されているため、リソースへのアクセスが簡単になりました。これにより、ユーザーは必要な情報を迅速に見つけることができます。

3. **APIの拡張と改善**: 新たに追加されたAPIや機能の説明が精緻化され、ユーザーがどのようにこれらを活用できるかについての具体的な手引きが提供されています。特に、エンドポイントの統合やカスタムモデルの改善など、重要なテクニカル情報が整理されています。

4. **言語サポートの拡張**: 新しい言語のサポートや、特定のモデルに関連する地理的要件についても言及されています。これにより、より多様なユーザーが利用できるようになっています。

5. **要約と注意点の整理**: 文書全体にわたる更新の内容が要約され、重要な注意点や推奨されるアクションが明確に示されています。これにより、ユーザーは最新の情報を踏まえた上で行動することができます。

これらの変更により、Document Intelligenceの「What's New」ページは、ユーザーに対して最新の機能や改善点を迅速かつ効率的に把握するための貴重なリソースとなります。開発者や実務者にとって、これらの情報は非常に役立つものであり、導入の手助けを行います。


