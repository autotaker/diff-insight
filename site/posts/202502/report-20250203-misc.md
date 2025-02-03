---
date: '2025-02-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5c1bed9...MicrosoftDocs:83a6833
summary: このコードの差分では、カスタムテキスト分析サービスに関連するドキュメントが広範囲に削除されたことが目立ちます。また、Serp APIに関連する接続キー画像の追加が新機能として挙げられています。これにより特定のドキュメントが更新され、情報の再編成とユーザーエクスペリエンスの向上が図られています。削除されたドキュメントはAzure
  AIプラットフォームの利便性を支えていたと考えられ、これによりユーザーは新しいリソースやサポートを探し求める必要が生じる可能性があります。全体的な更新は技術の進歩に伴うものであり、持続可能なユーザーサポートを確保するための努力が見受けられます。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:5c1bed9...MicrosoftDocs:83a6833){target="_blank"}

<format>
# Highlights
このコードの差分には、カスタムテキスト分析サービスに関連する広範囲なドキュメント削除が目立ちます。また、新しく追加された機能に関しては、Serp APIに関連する接続キー画像が含まれており、特定のドキュメントの更新により、情報の再編成とユーザーエクスペリエンスの向上が図られています。

## New features
- Serp API接続キーに関連する新しい画像が追加されました。

## Breaking changes
- カスタムテキスト分析及びカスタム感情分析に関連する多くのドキュメントが削除され、これにはデータフォーマット、API呼び出し、プロジェクト作成、モデルデプロイに関する詳細な手順が含まれます。
- Serp APIカスタム接続キーの画像が削除され、ユーザー向けの視覚的情報が失われました。

## Other updates
- 一部のドキュメントの更新日が最新のものに変更されました。
- トピック的な情報整理が行われ、より簡潔な内容提供が試みられています。

# Insights
今回の変更では、削除されたカスタムテキスト分析およびカスタム感情分析に関するドキュメントの多くが、Azure AIプラットフォームの利便性を大きく支えていたと考えられます。これらの削除は、Azureの機能が進化し、それに伴う技術的要件やサービス提供方法の変更を示唆しているかもしれません。

とはいえ、ユーザーはこれにより、新しいワークフローやガイドを自ら探し出さなければならず、知識のギャップが広がる可能性があります。このギャップを埋めるために、開発者やユーザーは別途リソースやサポートを探し求めなければならないかもしれません。

新しい画像の追加や、プロンプトフロー等の更新は、利用者の操作体験を支え、日付変更などの小さなアップデートは、文書が最新であることを保証します。文書の信頼性や有効性を高めるための努力が見受けられ、新規ユーザーや既存のユーザーが最新のハードウェア/ソフトウェアを効率的に活用できるように提供されています。

結果として、全体的な更新は、技術の進歩とサービスの更新に伴った必然的な情報再編を反映しており、持続可能なユーザーサポートを確保するためのものであると考えられます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-lifecycle.md](#item-417f3f) | minor update | モデルライフサイクルの更新日付の変更 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-abe5b8) | minor update | クイックスタートの更新日付の変更 | modified | 1 | 1 | 2 | 
| [data-formats.md](#item-11da30) | breaking change | データフォーマットに関するドキュメントの削除 | removed | 0 | 168 | 168 | 
| [entity-components.md](#item-7620d9) | breaking change | エンティティコンポーネントに関するドキュメントの削除 | removed | 0 | 106 | 106 | 
| [evaluation-metrics.md](#item-1de45a) | breaking change | 評価指標に関するドキュメントの削除 | removed | 0 | 152 | 152 | 
| [call-api.md](#item-5489c5) | breaking change | カスタムテキスト分析API呼び出しに関するドキュメントの削除 | removed | 0 | 57 | 57 | 
| [create-project.md](#item-4c7376) | breaking change | カスタムテキスト分析プロジェクト作成に関するドキュメントの削除 | removed | 0 | 117 | 117 | 
| [deploy-model.md](#item-7bddde) | breaking change | カスタムテキスト分析モデルのデプロイに関するドキュメントの削除 | removed | 0 | 105 | 105 | 
| [design-schema.md](#item-6c40e2) | breaking change | カスタムテキスト分析プロジェクトのためのデータ準備とスキーマ設計に関するドキュメントの削除 | removed | 0 | 109 | 109 | 
| [fail-over.md](#item-473399) | breaking change | カスタムテキスト分析モデルのバックアップとリカバリに関するドキュメントの削除 | removed | 0 | 140 | 140 | 
| [label-data.md](#item-75aad1) | breaking change | カスタムテキスト分析モデル用のデータラベリングに関するドキュメントの削除 | removed | 0 | 109 | 109 | 
| [train-model.md](#item-328f92) | breaking change | カスタムテキスト分析モデルのトレーニングに関するドキュメントの削除 | removed | 0 | 82 | 82 | 
| [view-model-evaluation.md](#item-463e8a) | breaking change | カスタムテキスト分析モデルの評価に関するドキュメントの削除 | removed | 0 | 75 | 75 | 
| [get-keys-endpoint-azure.md](#item-6156ce) | breaking change | Azureのキーとエンドポイント取得に関する情報の削除 | removed | 0 | 15 | 15 | 
| [cancel-training.md](#item-d752dc) | breaking change | Language Studioでのトレーニングキャンセル方法に関する情報の削除 | removed | 0 | 11 | 11 | 
| [create-project.md](#item-ba82ba) | breaking change | Language Studioでのプロジェクト作成に関する情報の削除 | removed | 0 | 39 | 39 | 
| [delete-deployment.md](#item-0f0d7c) | breaking change | Language Studioでのデプロイメント削除方法に関する情報の削除 | removed | 0 | 12 | 12 | 
| [delete-project.md](#item-f5cf6c) | breaking change | Language Studioでのプロジェクト削除に関する情報の削除 | removed | 0 | 15 | 15 | 
| [deploy-model.md](#item-6515b1) | breaking change | Language Studioでのモデルデプロイに関する情報の削除 | removed | 0 | 28 | 28 | 
| [import-project.md](#item-cd3b25) | breaking change | Language Studioでのプロジェクトインポートに関する情報の削除 | removed | 0 | 44 | 44 | 
| [swap-deployment.md](#item-4ed03f) | breaking change | Language Studioでのデプロイメントのスワップに関する情報の削除 | removed | 0 | 16 | 16 | 
| [test-model.md](#item-f5996f) | breaking change | Language Studioでのモデルテストに関する情報の削除 | removed | 0 | 26 | 26 | 
| [train-model.md](#item-d22149) | breaking change | Language Studioでのモデルトレーニングに関する情報の削除 | removed | 0 | 30 | 30 | 
| [blob-storage-upload.md](#item-52b1f8) | breaking change | Blobストレージへのアップロードに関するクイックスタート情報の削除 | removed | 0 | 29 | 29 | 
| [language-studio.md](#item-75ac6e) | breaking change | Language Studioに関するクイックスタート情報の削除 | removed | 0 | 81 | 81 | 
| [rest-api.md](#item-218739) | breaking change | REST APIに関するクイックスタート情報の削除 | removed | 0 | 128 | 128 | 
| [resource-creation-azure-portal.md](#item-49304b) | breaking change | Azureポータルからのリソース作成に関する情報の削除 | removed | 0 | 39 | 39 | 
| [cancel-training.md](#item-79e31a) | breaking change | トレーニング取消に関するREST API情報の削除 | removed | 0 | 35 | 35 | 
| [create-project.md](#item-c32223) | breaking change | カスタムプロジェクト作成に関するREST API情報の削除 | removed | 0 | 72 | 72 | 
| [delete-deployment.md](#item-3551ec) | breaking change | デプロイメント削除に関するREST API情報の削除 | removed | 0 | 36 | 36 | 
| [delete-project.md](#item-139027) | breaking change | プロジェクト削除に関するREST API情報の削除 | removed | 0 | 31 | 31 | 
| [deploy-model.md](#item-92e68f) | breaking change | モデルデプロイメントのAPI情報の削除 | removed | 0 | 52 | 52 | 
| [export-project.md](#item-7970cf) | breaking change | プロジェクト輸出に関するAPI情報の削除 | removed | 0 | 51 | 51 | 
| [get-deployment-status.md](#item-7b9bdc) | breaking change | デプロイメントステータス取得に関するAPI情報の削除 | removed | 0 | 46 | 46 | 
| [get-export-status.md](#item-467cd8) | breaking change | プロジェクトエクスポートステータス取得に関するAPI情報の削除 | removed | 0 | 64 | 64 | 
| [get-import-status.md](#item-2dec2c) | breaking change | プロジェクトインポートステータス取得に関するAPI情報の削除 | removed | 0 | 31 | 31 | 
| [get-project-details.md](#item-9ec8e1) | breaking change | プロジェクト詳細取得に関するAPI情報の削除 | removed | 0 | 45 | 45 | 
| [get-results.md](#item-7a7625) | breaking change | カスタムエンティティ認識タスクの結果取得に関するAPI情報の削除 | removed | 0 | 289 | 289 | 
| [get-training-status.md](#item-787844) | breaking change | モデルのトレーニング進行状況取得に関するAPI情報の削除 | removed | 0 | 60 | 60 | 
| [import-project.md](#item-6fa50e) | breaking change | ラベルファイルのインポートに関するAPI情報の削除 | removed | 0 | 185 | 185 | 
| [model-evaluation.md](#item-65d73e) | breaking change | トレーニング済みモデルの評価に関するAPI情報の削除 | removed | 0 | 133 | 133 | 
| [project-details.md](#item-443b56) | breaking change | プロジェクト詳細に関するAPI情報の削除 | removed | 0 | 57 | 57 | 
| [submit-task.md](#item-393d79) | breaking change | カスタムテキスト分析タスクの送信に関するAPI情報の削除 | removed | 0 | 86 | 86 | 
| [swap-deployment.md](#item-b2677f) | breaking change | デプロイメントのスワップに関するAPI情報の削除 | removed | 0 | 54 | 54 | 
| [train-model.md](#item-ce039c) | breaking change | モデルのトレーニングに関するAPI情報の削除 | removed | 0 | 66 | 66 | 
| [use-pre-existing-resource.md](#item-c35be9) | breaking change | 既存のリソースを使用する方法に関する情報の削除 | removed | 0 | 65 | 65 | 
| [language-support.md](#item-416183) | breaking change | カスタムテキスト分析の言語サポートに関する情報の削除 | removed | 0 | 45 | 45 | 
| [add-deployment.png](#item-b13093) | breaking change | デプロイメント画像の削除 | removed | 0 | 0 | 0 | 
| [connect-storage.png](#item-6ae9de) | breaking change | ストレージ接続画像の削除 | removed | 0 | 0 | 0 | 
| [create-project.png](#item-a58210) | breaking change | プロジェクト作成画像の削除 | removed | 0 | 0 | 0 | 
| [deploy-model.png](#item-cd9164) | breaking change | モデル展開画像の削除 | removed | 0 | 0 | 0 | 
| [development-lifecycle.png](#item-4dca20) | breaking change | 開発ライフサイクル画像の削除 | removed | 0 | 0 | 0 | 
| [file-upload-screen.png](#item-314ce4) | breaking change | ファイルアップロード画面画像の削除 | removed | 0 | 0 | 0 | 
| [learned-component.png](#item-74afb1) | breaking change | 学習コンポーネント画像の削除 | removed | 0 | 0 | 0 | 
| [list-component.png](#item-e9952e) | breaking change | リストコンポーネント画像の削除 | removed | 0 | 0 | 0 | 
| [prebuilt-component.png](#item-ea83f3) | breaking change | プリビルトコンポーネント画像の削除 | removed | 0 | 0 | 0 | 
| [resource-sharing.png](#item-732a75) | breaking change | リソース共有画像の削除 | removed | 0 | 0 | 0 | 
| [select-custom-feature-azure-portal.png](#item-7dfe20) | breaking change | Azureポータルでのカスタム機能選択画像の削除 | removed | 0 | 0 | 0 | 
| [separated-overlap-example-1-part-2.svg](#item-7488c7) | breaking change | 分離オーバーラップ例1パート2のSVGファイルの削除 | removed | 0 | 22 | 22 | 
| [separated-overlap-example-1.svg](#item-68315c) | breaking change | 分離オーバーラップ例1のSVGファイルの削除 | removed | 0 | 14 | 14 | 
| [storage-screen.png](#item-4dd51e) | breaking change | ストレージスクリーンのPNGファイルの削除 | removed | 0 | 0 | 0 | 
| [tag-options.png](#item-0597c4) | breaking change | タグオプションのPNGファイルの削除 | removed | 0 | 0 | 0 | 
| [test-model-results.png](#item-15ad58) | breaking change | テストモデル結果のPNGファイルの削除 | removed | 0 | 0 | 0 | 
| [train-model.png](#item-fb48a4) | breaking change | モデル訓練のPNGファイルの削除 | removed | 0 | 0 | 0 | 
| [union-overlap-example-1-part-2.svg](#item-f266f5) | breaking change | 重複領域の例のSVGファイルの削除 | removed | 0 | 10 | 10 | 
| [union-overlap-example-1.svg](#item-52bda8) | breaking change | 重複領域の例のSVGファイルの削除 | removed | 0 | 13 | 13 | 
| [union-overlap-example-2-part-2.svg](#item-6faae8) | breaking change | 重複領域の例のSVGファイルの削除 | removed | 0 | 10 | 10 | 
| [union-overlap-example-2.svg](#item-331137) | breaking change | 重複領域の例のSVGファイルの削除 | removed | 0 | 14 | 14 | 
| [overview.md](#item-6f599b) | breaking change | カスタムテキスト分析の概要文書の削除 | removed | 0 | 79 | 79 | 
| [quickstart.md](#item-5bcba3) | breaking change | カスタムテキスト分析のクイックスタート文書の削除 | removed | 0 | 50 | 50 | 
| [glossary.md](#item-f2ab66) | breaking change | カスタムテキスト分析の用語集文書の削除 | removed | 0 | 69 | 69 | 
| [service-limits.md](#item-b62cd6) | breaking change | カスタムテキスト分析のサービス制限に関する文書の削除 | removed | 0 | 93 | 93 | 
| [index.yml](#item-c9444f) | minor update | カスタムテキスト分析の概要に関する項目の削除 | modified | 0 | 3 | 3 | 
| [overview.md](#item-f138b4) | minor update | 健康に関するカスタムテキスト分析の情報の削除 | modified | 0 | 12 | 12 | 
| [data-formats.md](#item-b252b4) | breaking change | カスタム感情分析データフォーマットに関する文書の削除 | removed | 0 | 103 | 103 | 
| [call-api.md](#item-54966c) | breaking change | カスタム感情分析API呼び出しに関する文書の削除 | removed | 0 | 56 | 56 | 
| [create-project.md](#item-7699a8) | breaking change | カスタム感情分析プロジェクト作成に関する文書の削除 | removed | 0 | 117 | 117 | 
| [deploy-model.md](#item-435eeb) | breaking change | カスタム感情分析モデルのデプロイに関する文書の削除 | removed | 0 | 104 | 104 | 
| [design-schema.md](#item-f66944) | breaking change | カスタム感情分析スキーマの定義に関する文書の削除 | removed | 0 | 51 | 51 | 
| [label-data.md](#item-a91115) | breaking change | カスタム感情分析のためのデータラベリングに関する文書の削除 | removed | 0 | 75 | 75 | 
| [train-model.md](#item-2b8047) | breaking change | カスタム感情分析モデルの訓練に関する文書の削除 | removed | 0 | 86 | 86 | 
| [quickstart.md](#item-32972e) | breaking change | カスタム感情分析のクイックスタート文書の削除 | removed | 0 | 45 | 45 | 
| [overview.md](#item-831fe6) | minor update | 感情分析と意見マイニングの概要文書の更新 | modified | 6 | 44 | 50 | 
| [toc.yml](#item-12f1f0) | minor update | 感情分析および意見マイニングのTOCの更新 | modified | 58 | 158 | 216 | 
| [prompt-flow.md](#item-22c24b) | minor update | プロンプトフローに関するチュートリアルの日付の更新 | modified | 1 | 1 | 2 | 
| [serp-api-tool.md](#item-144ed7) | minor update | Serp APIツールに関するドキュメントの更新 | modified | 7 | 10 | 17 | 
| [serp-api-tool.png](#item-2a4be2) | minor update | Serp APIツールの画像に関する変更 | modified | 0 | 0 | 0 | 
| [serp-connection-keys.png](#item-50b509) | new feature | Serp API接続キーの画像が追加されました | added | 0 | 0 | 0 | 
| [serp-custom-connection-keys.png](#item-e22fae) | breaking change | Serp APIカスタム接続キーの画像が削除されました | removed | 0 | 0 | 0 | 


# Modified Contents
## articles/ai-services/language-service/concepts/model-lifecycle.md{#item-417f3f}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 01/16/2024
+ms.date: 01/31/2025
 ms.author: jboback
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルの更新日付の変更"
}
```

### Explanation
この変更は、`model-lifecycle.md`ドキュメントの更新日付を変更しました。具体的には、元々の更新日付が「2024年1月16日」から「2025年1月31日」に変更されています。この修正は、ドキュメント管理の目的で、より正確な情報を提供するために行われました。変更は1行追加され、1行削除され、全体で2行が更新されています。更新内容の詳細は、GitHubのリポジトリ内の該当ページで確認できます。

## articles/ai-services/language-service/custom-named-entity-recognition/quickstart.md{#item-abe5b8}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 12/19/2023
+ms.date: 01/31/2025
 ms.author: jboback
 ms.custom: language-service-custom-ner, mode-other
 zone_pivot_groups: usage-custom-language-features
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートの更新日付の変更"
}
```

### Explanation
この変更は、`quickstart.md`ドキュメント内の更新日付を変更しています。具体的には、更新日が「2023年12月19日」から「2025年1月31日」に変更されました。この修正は、最新の情報を反映させるために必要なもので、ドキュメントの正確さを向上させることを目的としています。変更点は1行の追加と1行の削除を伴い、合計で2行が更新されているという内容です。詳細は、GitHubのリポジトリの該当リンクで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/concepts/data-formats.md{#item-11da30}

<details>
<summary>Diff</summary>
````diff
@@ -1,168 +0,0 @@
----
-title: Custom Text Analytics for health data formats
-titleSuffix: Azure AI services
-description: Learn about the data formats accepted by custom text analytics for health.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: conceptual
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h
----
-
-# Accepted data formats in custom text analytics for health
-
-Use this article to learn about formatting your data to be imported into custom text analytics for health.
-
-If you are trying to [import your data](../how-to/create-project.md#import-project) into custom Text Analytics for health, it has to follow a specific format. If you don't have data to import, you can [create your project](../how-to/create-project.md) and use the Language Studio to [label your documents](../how-to/label-data.md).
-
-Your Labels file should be in the `json` format below to be used when importing your labels into a project.
-
-```json
-{
-	"projectFileVersion": "{API-VERSION}",
-	"stringIndexType": "Utf16CodeUnit",
-	"metadata": {
-		"projectName": "{PROJECT-NAME}",
-		"projectKind": "CustomHealthcare",
-		"description": "Trying out custom Text Analytics for health",
-		"language": "{LANGUAGE-CODE}",
-		"multilingual": true,
-		"storageInputContainerName": "{CONTAINER-NAME}",
-		"settings": {}
-	},
-	"assets": {
-		"projectKind": "CustomHealthcare",
-		"entities": [
-			{
-				"category": "Entity1",
-				"compositionSetting": "{COMPOSITION-SETTING}",
-				"list": {
-					"sublists": [
-						{
-							"listKey": "One",
-							"synonyms": [
-								{
-									"language": "en",
-									"values": [
-										"EntityNumberOne",
-										"FirstEntity"
-									]
-								}
-							]
-						}
-					]
-				}
-			},
-			{
-				"category": "Entity2"
-			},
-			{
-				"category": "MedicationName",
-				"list": {
-					"sublists": [
-						{
-							"listKey": "research drugs",
-							"synonyms": [
-								{
-									"language": "en",
-									"values": [
-										"rdrug a",
-										"rdrug b"
-									]
-								}
-							]
-
-						}
-					]
-				}
-				"prebuilts": "MedicationName"
-			}
-		],
-		"documents": [
-			{
-				"location": "{DOCUMENT-NAME}",
-				"language": "{LANGUAGE-CODE}",
-				"dataset": "{DATASET}",
-				"entities": [
-					{
-						"regionOffset": 0,
-						"regionLength": 500,
-						"labels": [
-							{
-								"category": "Entity1",
-								"offset": 25,
-								"length": 10
-							},
-							{
-								"category": "Entity2",
-								"offset": 120,
-								"length": 8
-							}
-						]
-					}
-				]
-			},
-			{
-				"location": "{DOCUMENT-NAME}",
-				"language": "{LANGUAGE-CODE}",
-				"dataset": "{DATASET}",
-				"entities": [
-					{
-						"regionOffset": 0,
-						"regionLength": 100,
-						"labels": [
-							{
-								"category": "Entity2",
-								"offset": 20,
-								"length": 5
-							}
-						]
-					}
-				]
-			}
-		]
-	}
-}
-
-```
-
-|Key  |Placeholder  |Value  | Example |
-|---------|---------|----------|--|
-| `multilingual` | `true`| A boolean value that enables you to have documents in multiple languages in your dataset and when your model is deployed you can query the model in any supported language (not necessarily included in your training documents). See [language support](../language-support.md#) to learn more about multilingual support. | `true`|
-|`projectName`|`{PROJECT-NAME}`|Project name|`myproject`|
-| `storageInputContainerName` |`{CONTAINER-NAME}`|Container name|`mycontainer`|
-| `entities` | | Array containing all the entity types you have in the project. These are the entity types that will be extracted from your documents into.|  |
-| `category` | | The name of the entity type, which can be user defined for new entity definitions, or predefined for prebuilt entities. For more information, see the entity naming rules below.|  |
-|`compositionSetting`|`{COMPOSITION-SETTING}`|Rule that defines how to manage multiple components in your entity. Options are `combineComponents` or `separateComponents`. |`combineComponents`|
-| `list` | | Array containing all the sublists you have in the project for a specific entity. Lists can be added to prebuilt entities or new entities with learned components.|  |
-|`sublists`|`[]`|Array containing sublists. Each sublist is a key and its associated values.|`[]`|
-| `listKey`| `One` | A normalized value for the list of synonyms to map back to in prediction. | `One` |
-|`synonyms`|`[]`|Array containing all the synonyms|synonym|
-| `language` | `{LANGUAGE-CODE}` |  A string specifying the language code for the synonym in your sublist. If your project is a multilingual project and you want to support your list of synonyms for all the languages in your project, you have to explicitly add your synonyms to each language. See [Language support](../language-support.md) for more information about supported language codes. |`en`|
-| `values`| `"EntityNumberone"`, `"FirstEntity"`  | A list of comma separated strings that will be matched exactly for extraction and map to the list key. | `"EntityNumberone"`, `"FirstEntity"` |
-| `prebuilts` | `MedicationName` | The name of the prebuilt component populating the prebuilt entity. [Prebuilt entities](../../text-analytics-for-health/concepts/health-entity-categories.md) are automatically loaded into your project by default but you can extend them with list components in your labels file.  | `MedicationName` |
-| `documents` | | Array containing all the documents in your project and list of the entities labeled within each document. | [] |
-| `location` | `{DOCUMENT-NAME}` |  The location of the documents in the storage container. Since all the documents are in the root of the container this should be the document name.|`doc1.txt`|
-| `dataset` | `{DATASET}` |  The test set to which this file goes to when split before training. Learn more about data splitting [here](../how-to/train-model.md#data-splitting). Possible values for this field are `Train` and `Test`.      |`Train`|
-| `regionOffset` |  |  The inclusive character position of the start of the text.      |`0`|
-| `regionLength` |  |  The length of the bounding box in terms of UTF16 characters. Training only considers the data in this region.      |`500`|
-| `category` |  |  The type of entity associated with the span of text specified. | `Entity1`|
-| `offset` |  |  The start position for the entity text. | `25`|
-| `length` |  |  The length of the entity in terms of UTF16 characters. | `20`|
-| `language` | `{LANGUAGE-CODE}` |  A string specifying the language code for the document used in your project. If your project is a multilingual project, choose the language code of the majority of the documents. See [Language support](../language-support.md) for more information about supported language codes. |`en`|
-
-## Entity naming rules
-
-1. [Prebuilt entity names](../../text-analytics-for-health/concepts/health-entity-categories.md) are predefined. They must be populated with a prebuilt component and it must match the entity name.
-2. New user defined entities (entities with learned components or labeled text) can't use prebuilt entity names.
-3. New user defined entities can't be populated with prebuilt components as prebuilt components must match their associated entities names and have no labeled data assigned to them in the documents array.
-
-
-
-## Next steps
-* You can import your labeled data into your project directly. Learn how to [import project](../how-to/create-project.md#import-project)
-* See the [how-to article](../how-to/label-data.md)  more information about labeling your data. 
-* When you're done labeling your data, you can [train your model](../how-to/train-model.md).  
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "データフォーマットに関するドキュメントの削除"
}
```

### Explanation
この変更では、`data-formats.md`ドキュメントが完全に削除されました。この文書は、カスタムテキスト分析のための健康データフォーマットに関する情報を提供していました。削除された内容には、データのフォーマット、受け入れられるデータ形式に関する具体的な例、プロジェクトの作成やデータのインポート方法が詳細に説明されていました。また、JSON形式でのラベルファイルの要件やエンティティ命名のルールについても言及されていました。この大規模な変更により、該当する情報が利用できなくなるため、ユーザーにとって重要な情報源が失われることになります。変更の詳細は、GitHubのリポジトリで確認することができます。

## articles/ai-services/language-service/custom-text-analytics-for-health/concepts/entity-components.md{#item-7620d9}

<details>
<summary>Diff</summary>
````diff
@@ -1,106 +0,0 @@
----
-title: Entity components in custom Text Analytics for health
-titleSuffix: Azure AI services
-description: Learn how custom Text Analytics for health extracts entities from text
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: conceptual
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h
----
-
-# Entity components in custom text analytics for health
-
-In custom Text Analytics for health, entities are relevant pieces of information that are extracted from your unstructured input text. An entity can be extracted by different methods. They can be learned through context, matched from a list, or detected by a prebuilt recognized entity. Every entity in your project is composed of one or more of these methods, which are defined as your entity's components. When an entity is defined by more than one component, their predictions can overlap. You can determine the behavior of an entity prediction when its components overlap by using a fixed set of options in the **Entity options**.
-
-## Component types
-
-An entity component determines a way you can extract the entity. An entity can contain one component, which would determine the only method that would be used to extract the entity, or multiple components to expand the ways in which the entity is defined and extracted. 
-
-The [Text Analytics for health entities](../../text-analytics-for-health/concepts/health-entity-categories.md) are automatically loaded into your project as entities with prebuilt components. You can define list components for entities with prebuilt components but you can't add learned components. Similarly, you can create new entities with learned and list components, but you can't populate them with additional prebuilt components.
-
-### Learned component
-
-The learned component uses the entity tags you label your text with to train a machine learned model. The model learns to predict where the entity is, based on the context within the text. Your labels provide examples of where the entity is expected to be present in text, based on the meaning of the words around it and as the words that were labeled. This component is only defined if you add labels to your data for the entity. If you do not label any data, it will not have a learned component.
-
-The Text Analytics for health entities, which by default have prebuilt components can't be extended with learned components, meaning they do not require or accept further labeling to function.
-
-:::image type="content" source="../media/learned-component.png" alt-text="A screenshot showing an example of learned components for entities." lightbox="../media/learned-component.png":::
-
-### List component
-
-The list component represents a fixed, closed set of related words along with their synonyms. The component performs an exact text match against the list of values you provide as synonyms. Each synonym belongs to a "list key", which can be used as the normalized, standard value for the synonym that will return in the output if the list component is matched. List keys are **not** used for matching.
-
-In multilingual projects, you can specify a different set of synonyms for each language. While using the prediction API, you can specify the language in the input request, which will only match the synonyms associated to that language.
-
-
-:::image type="content" source="../media/list-component.png" alt-text="A screenshot showing an example of list components for entities." lightbox="../media/list-component.png":::
-
-### Prebuilt component
-
-The [Text Analytics for health entities](../../text-analytics-for-health/concepts/health-entity-categories.md) are automatically loaded into your project as entities with prebuilt components. You can define list components for entities with prebuilt components but you cannot add learned components. Similarly, you can create new entities with learned and list components, but you cannot populate them with additional prebuilt components. Entities with prebuilt components are pretrained and can extract information relating to their categories without any labels.
-
-:::image type="content" source="../media/prebuilt-component.png" alt-text="A screenshot showing an example of prebuilt components for entities." lightbox="../media/prebuilt-component.png":::
-
-
-## Entity options
-
-When multiple components are defined for an entity, their predictions may overlap. When an overlap occurs, each entity's final prediction is determined by one of the following options.
-
-### Combine components
-
-Combine components as one entity when they overlap by taking the union of all the components.
-
-Use this to combine all components when they overlap. When components are combined, you get all the extra information that’s tied to a list or prebuilt component when they are present.
-
-#### Example
-
-Suppose you have an entity called Software that has a list component, which contains “Proseware OS” as an entry. In your input data, you have “I want to buy Proseware OS 9” with “Proseware OS 9” tagged as Software:
-
-:::image type="content" source="../media/union-overlap-example-1.svg" alt-text="A screenshot showing a learned and list entity overlapped." lightbox="../media/union-overlap-example-1.svg":::
-
-By using combine components, the entity will return with the full context as “Proseware OS 9” along with the key from the list component:
-
-:::image type="content" source="../media/union-overlap-example-1-part-2.svg" alt-text="A screenshot showing the result of a combined component." lightbox="../media/union-overlap-example-1-part-2.svg":::
-
-Suppose you had the same utterance but only “OS 9” was predicted by the learned component:
-
-:::image type="content" source="../media/union-overlap-example-2.svg" alt-text="A screenshot showing an utterance with O S 9 predicted by the learned component." lightbox="../media/union-overlap-example-2.svg":::
-
-With combine components, the entity will still return as “Proseware OS 9” with the key from the list component:
-
-:::image type="content" source="../media/union-overlap-example-2-part-2.svg" alt-text="A screenshot showing the returned software entity." lightbox="../media/union-overlap-example-2-part-2.svg":::
-
-
-### Don't combine components
-
-Each overlapping component will return as a separate instance of the entity. Apply your own logic after prediction with this option.
-
-#### Example
-
-Suppose you have an entity called Software that has a list component, which contains “Proseware Desktop” as an entry. In your labeled data, you have “I want to buy Proseware Desktop Pro” with “Proseware Desktop Pro” labeled as Software:
-
-:::image type="content" source="../media/separated-overlap-example-1.svg" alt-text="A screenshot showing an example of a learned and list entity overlapped." lightbox="../media/separated-overlap-example-1.svg":::
-
-When you do not combine components, the entity will return twice:
-
-:::image type="content" source="../media/separated-overlap-example-1-part-2.svg" alt-text="A screenshot showing the entity returned twice." lightbox="../media/separated-overlap-example-1-part-2.svg":::
-
-
-## How to use components and options
-
-Components give you the flexibility to define your entity in more than one way. When you combine components, you make sure that each component is represented and you reduce the number of entities returned in your predictions. 
-
-A common practice is to extend a prebuilt component with a list of values that the prebuilt might not support. For example, if you have a **Medication Name** entity, which has a `Medication.Name` prebuilt component added to it, the entity may not predict all the medication names specific to your domain. You can use a list component to extend the values of the Medication Name entity and thereby extending the prebuilt with your own values of Medication Names.
-
-Other times you may be interested in extracting an entity through context such as a **medical device**. You would label for the learned component of the medical device to learn _where_ a medical device is based on its position within the sentence. You may also have a list of medical devices that you already know before hand that you'd like to always extract. Combining both components in one entity allows you to get both options for the entity.
-
-When you do not combine components, you allow every component to act as an independent entity extractor. One way of using this option is to separate the entities extracted from a list to the ones extracted through the learned or prebuilt components to handle and treat them differently.
-
-
-## Next steps
-
-* [Entities with prebuilt components](../../text-analytics-for-health/concepts/health-entity-categories.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "エンティティコンポーネントに関するドキュメントの削除"
}
```

### Explanation
この変更では、`entity-components.md`ドキュメントが完全に削除されました。この文書は、カスタムテキスト分析におけるエンティティの取得方法や、その構成要素についての詳細を提供していました。削除された内容には、エンティティの種類、学習コンポーネント、リストコンポーネント、プリビルトコンポーネントの説明、また異なるコンポーネントが重なった場合の処理方法などが含まれていました。この変更により、カスタムテキスト分析におけるエンティティ関連の理解に重要な情報が失われることになります。具体的な内容や過去の情報は、GitHubのリポジトリにて確認可能です。

## articles/ai-services/language-service/custom-text-analytics-for-health/concepts/evaluation-metrics.md{#item-1de45a}

<details>
<summary>Diff</summary>
````diff
@@ -1,152 +0,0 @@
----
-title: Custom text analytics for health evaluation metrics
-titleSuffix: Azure AI services
-description: Learn about evaluation metrics in custom Text Analytics for health
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: conceptual 
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h
----
-
-# Evaluation metrics for custom Text Analytics for health models
-
-Your [dataset is split](../how-to/train-model.md#data-splitting) into two parts: a set for training, and a set for testing. The training set is used to train the model, while the testing set is used as a test for model after training to calculate the model performance and evaluation. The testing set is not introduced to the model through the training process, to make sure that the model is tested on new data.
-
-Model evaluation is triggered automatically after training is completed successfully. The evaluation process starts by using the trained model to predict user defined entities for documents in the test set, and compares them with the provided data labels (which establishes a baseline of truth). The results are returned so you can review the model’s performance. User defined entities are **included** in the evaluation factoring in Learned and List components; Text Analytics for health prebuilt entities are **not** factored in the model evaluation. For evaluation, custom Text Analytics for health uses the following metrics:
-
-* **Precision**: Measures how precise/accurate your model is. It is the ratio between the correctly identified positives (true positives) and all identified positives. The precision metric reveals how many of the predicted entities are correctly labeled. 
-
-    `Precision = #True_Positive / (#True_Positive + #False_Positive)`
-
-* **Recall**: Measures the model's ability to predict actual positive classes. It is the ratio between the predicted true positives and what was actually tagged. The recall metric reveals how many of the predicted entities are correct.
-
-    `Recall = #True_Positive / (#True_Positive + #False_Negatives)`
-
-* **F1 score**: The F1 score is a function of Precision and Recall. It's needed when you seek a balance between Precision and Recall.
-
-    `F1 Score = 2 * Precision * Recall / (Precision + Recall)` <br> 
-
->[!NOTE]
-> Precision, recall and F1 score are calculated for each entity separately (*entity-level* evaluation) and for the model collectively (*model-level* evaluation).
-
-## Model-level and entity-level evaluation metrics
-
-Precision, recall, and F1 score are calculated for each entity separately (entity-level evaluation) and for the model collectively (model-level evaluation).
-
-The definitions of precision, recall, and evaluation are the same for both entity-level and model-level evaluations. However, the counts for *True Positives*, *False Positives*, and *False Negatives* differ can differ. For example, consider the following text.
-
-### Example
-
-*The first party of this contract is John Smith, resident of 5678 Main Rd., City of Frederick, state of Nebraska. And the second party is Forrest Ray, resident of 123-345 Integer Rd., City of Corona, state of New Mexico. There is also Fannie Thomas resident of 7890 River Road, city of Colorado Springs, State of Colorado.*
-
-The model extracting entities from this text could have the following predictions:
-
-| Entity | Predicted as | Actual type |
-|--|--|--|
-| John Smith | Person | Person |
-| Frederick | Person | City |
-| Forrest | City | Person |
-| Fannie Thomas | Person | Person |
-| Colorado Springs | City | City |
-
-### Entity-level evaluation for the *person* entity 
-
-The model would have the following entity-level evaluation, for the *person* entity:
-
-| Key | Count | Explanation |
-|--|--|--|
-| True Positive | 2 | *John Smith* and *Fannie Thomas* were correctly predicted as *person*. |
-| False Positive | 1 | *Frederick* was incorrectly predicted as *person* while it should have been *city*. |
-| False Negative | 1 | *Forrest* was incorrectly predicted as *city* while it should have been *person*. |
-
-* **Precision**: `#True_Positive / (#True_Positive + #False_Positive)` = `2 / (2 + 1) = 0.67`
-* **Recall**: `#True_Positive / (#True_Positive + #False_Negatives)` = `2 / (2 + 1) = 0.67`
-* **F1 Score**: `2 * Precision * Recall / (Precision + Recall)` = `(2 * 0.67 * 0.67) / (0.67 + 0.67) = 0.67`
-
-### Entity-level evaluation for the *city* entity
-
-The model would have the following entity-level evaluation, for the *city* entity:
-
-| Key | Count | Explanation |
-|--|--|--|
-| True Positive | 1 | *Colorado Springs* was correctly predicted as *city*. |
-| False Positive | 1 | *Forrest* was incorrectly predicted as *city* while it should have been *person*. |
-| False Negative | 1 | *Frederick* was incorrectly predicted as *person* while it should have been *city*. |
-
-* **Precision** = `#True_Positive / (#True_Positive + #False_Positive)` = `1 / (1 + 1) = 0.5`
-* **Recall** = `#True_Positive / (#True_Positive + #False_Negatives)` = `1 / (1 + 1) = 0.5`
-* **F1 Score** = `2 * Precision * Recall / (Precision + Recall)` =  `(2 * 0.5 * 0.5) / (0.5 + 0.5) = 0.5`
-
-### Model-level evaluation for the collective model
-
-The model would have the following evaluation for the model in its entirety:
-
-| Key | Count | Explanation |
-|--|--|--|
-| True Positive | 3 | *John Smith* and *Fannie Thomas* were correctly predicted as *person*. *Colorado Springs* was correctly predicted as *city*. This is the sum of true positives for all entities. |
-| False Positive | 2 | *Forrest* was incorrectly predicted as *city* while it should have been *person*. *Frederick* was incorrectly predicted as *person* while it should have been *city*. This is the sum of false positives for all entities. |
-| False Negative | 2 | *Forrest* was incorrectly predicted as *city* while it should have been *person*. *Frederick* was incorrectly predicted as *person* while it should have been *city*. This is the sum of false negatives for all entities. |
-
-* **Precision** = `#True_Positive / (#True_Positive + #False_Positive)` = `3 / (3 + 2) = 0.6`
-* **Recall** = `#True_Positive / (#True_Positive + #False_Negatives)` = `3 / (3 + 2) = 0.6`
-* **F1 Score** = `2 * Precision * Recall / (Precision + Recall)` =  `(2 * 0.6 * 0.6) / (0.6 + 0.6) = 0.6`
-
-## Interpreting entity-level evaluation metrics
-
-So what does it actually mean to have high precision or high recall for a certain entity?
-
-| Recall | Precision | Interpretation |
-|--|--|--|
-| High | High | This entity is handled well by the model. |
-| Low | High | The model cannot always extract this entity, but when it does it is with high confidence. |
-| High | Low | The model extracts this entity well, however it is with low confidence as it is sometimes extracted as another type. |
-| Low | Low | This entity type is poorly handled by the model, because it is not usually extracted. When it is, it is not with high confidence. |
-
-## Guidance
-
-After you trained your model, you will see some guidance and recommendation on how to improve the model. It's recommended to have a model covering all points in the guidance section.
-
-* Training set has enough data: When an entity type has fewer than 15 labeled instances in the training data, it can lead to lower accuracy due to the model not being adequately trained on these cases. In this case, consider adding more labeled data in the training set. You can check the *data distribution* tab for more guidance.
-
-* All entity types are present in test set: When the testing data lacks labeled instances for an entity type, the model’s test performance may become less comprehensive due to untested scenarios. You can check the *test set data distribution* tab for more guidance.
-
-* Entity types are balanced within training and test sets: When sampling bias causes an inaccurate representation of an entity type’s frequency, it can lead to lower accuracy due to the model expecting that entity type to occur too often or too little. You can check the *data distribution* tab for more guidance.
-
-* Entity types are evenly distributed between training and test sets: When the mix of entity types doesn’t match between training and test sets, it can lead to lower testing accuracy due to the model being trained differently from how it’s being tested. You can check the *data distribution* tab for more guidance.
-
-* Unclear distinction between entity types in training set: When the training data is similar for multiple entity types, it can lead to lower accuracy because the entity types may be frequently misclassified as each other. Review the following entity types and consider merging them if they’re similar. Otherwise, add more examples to better distinguish them from each other. You can check the *confusion matrix* tab for more guidance.
-
-
-## Confusion matrix
-
-A Confusion matrix is an N x N matrix used for model performance evaluation, where N is the number of entities.
-The matrix compares the expected labels with the ones predicted by the model.
-This gives a holistic view of how well the model is performing and what kinds of errors it is making.
-
-You can use the Confusion matrix to identify entities that are too close to each other and often get mistaken (ambiguity). In this case consider merging these entity types together. If that isn't possible, consider adding more tagged examples of both entities to help the model differentiate between them.
-
-The highlighted diagonal in the image below is the correctly predicted entities, where the predicted tag is the same as the actual tag.
-
-:::image type="content" source="../../media/custom/confusion.png" alt-text="A screenshot that shows an example confusion matrix." lightbox="../../media/custom/confusion.png":::
-
-You can calculate the entity-level and model-level evaluation metrics from the confusion matrix:
-
-* The values in the diagonal are the *True Positive* values of each entity.
-* The sum of the values in the entity rows (excluding the diagonal) is the *false positive* of the model.
-* The sum of the values in the entity columns (excluding the diagonal) is the *false Negative* of the model.
-
-Similarly,
-
-* The *true positive* of the model is the sum of *true Positives* for all entities.
-* The *false positive* of the model is the sum of *false positives* for all entities.
-* The *false Negative* of the model is the sum of *false negatives* for all entities. 
-
-## Next steps
-
-* [Custom text analytics for health overview](../overview.md)
-* [View a model's performance in Language Studio](../how-to/view-model-evaluation.md)
-* [Train a model](../how-to/train-model.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "評価指標に関するドキュメントの削除"
}
```

### Explanation
この変更では、`evaluation-metrics.md`ドキュメントが完全に削除されました。この文書は、カスタムテキスト分析におけるモデル評価指標に関する情報を提供しており、モデルのトレーニングとテストの過程、評価指標（精度、再現率、F1スコア）についての説明が含まれていました。また、エンティティのレベル評価とモデル全体の評価、混同行列の利用方法、モデルの改善に関するガイダンスも示されていました。この重要な情報の削除により、ユーザーはカスタムテキスト分析のモデル評価において必要な知識を欠くことになるため、実用的な影響が及ぶ可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/how-to/call-api.md{#item-5489c5}

<details>
<summary>Diff</summary>
````diff
@@ -1,57 +0,0 @@
----
-title: Send a custom Text Analytics for health request to your custom model
-description: Learn how to send a request for custom text analytics for health.
-titleSuffix: Azure AI services
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.devlang: http
-ms.custom: language-service-custom-ta4h
----
-
-# Send queries to your custom Text Analytics for health model
-
-After the deployment is added successfully, you can query the deployment to extract entities from your text based on the model you assigned to the deployment.
-You can query the deployment programmatically using the [Prediction API](/rest/api/language/text-analysis-runtime/analyze-text). 
-
-## Test deployed model
-
-You can use Language Studio to submit the custom Text Analytics for health task and visualize the results. 
-
-[!INCLUDE [Test model](../../includes/custom/language-studio/test-model.md)]
-
-:::image type="content" source="../media/test-model-results.png" alt-text="A screenshot showing the deployment testing screen in Language Studio for Custom text analytics of health." lightbox="../media/test-model-results.png":::
-
-
-## Send a custom text analytics for health request to your model
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Get prediction URL](../../includes/custom/language-studio/get-prediction-url.md)]
-
-
-# [REST API](#tab/rest-api)
-
-First you will need to get your resource key and endpoint:
-
-[!INCLUDE [Get keys and endpoint Azure Portal](../../includes/key-endpoint-page-azure-portal.md)]
-
-
-### Submit a custom Text Analytics for health task
-
-[!INCLUDE [submit a custom Text Analytics for health task using the REST API](../includes/rest-api/submit-task.md)]
-
-### Get task results
-
-[!INCLUDE [get custom Text Analytics for health task results](../includes/rest-api/get-results.md)]
-
-
----
-
-## Next steps
-
-* [Custom text analytics for health](../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析API呼び出しに関するドキュメントの削除"
}
```

### Explanation
この変更では、`call-api.md`ドキュメントが完全に削除されました。この文書は、カスタムテキスト分析モデルに対してリクエストを送信する方法を説明しており、モデルのデプロイ後にエンティティを抽出するための手順やAPIの使用法について述べていました。具体的には、Language Studioを使用したモデルのテスト方法、REST APIを介してリクエストを送信する方法、リソースキーとエンドポイントの取得手順などが説明されていました。この重要な情報の削除により、ユーザーはカスタムテキスト分析APIを適切に呼び出す方法を学ぶ機会を失うことになります。変更内容の詳細はGitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/how-to/create-project.md{#item-4c7376}

<details>
<summary>Diff</summary>
````diff
@@ -1,117 +0,0 @@
----
-title: Using Azure resources in custom Text Analytics for health
-titleSuffix: Azure AI services
-description: Learn about the steps for using Azure resources with custom text analytics for health.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h, references_regions
----
-
-# How to create custom Text Analytics for health project
-
-Use this article to learn how to set up the requirements for starting with custom text analytics for health and create a project.
-
-## Prerequisites
-
-Before you start using custom text analytics for health, you need:
-
-* An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services).
-
-## Create a Language resource 
-
-Before you start using custom text analytics for health, you'll need an Azure AI Language resource. It's recommended to create your Language resource and connect a storage account to it in the Azure portal. Creating a resource in the Azure portal lets you create an Azure storage account at the same time, with all of the required permissions preconfigured. You can also read further in the article to learn how to use a pre-existing resource, and configure it to work with custom text analytics for health.
-
-You also will need an Azure storage account where you will upload your `.txt` documents that will be used to train a model to extract entities.
-
-> [!NOTE]
->  * You need to have an **owner** role assigned on the resource group to create a Language resource.
->  * If you will connect a pre-existing storage account, you should have an owner role assigned to it.
-
-## Create Language resource and connect storage account
-
-You can create a resource in the following ways:
-
-* The Azure portal
-* Language Studio
-* PowerShell
-
-> [!Note]
-> You shouldn't move the storage account to a different resource group or subscription once it's linked with the Language resource.
-
-[!INCLUDE [create a new resource from the Azure portal](../../includes/custom/resource-creation-azure-portal.md)]
-
-[!INCLUDE [create a new resource from Language Studio](../../includes/custom/resource-creation-language-studio.md)]
-
-[!INCLUDE [create a new resource with Azure PowerShell](../../includes/custom/resource-creation-powershell.md)]
-
-
-> [!NOTE]
-> * The process of connecting a storage account to your Language resource is irreversible, it cannot be disconnected later.
-> * You can only connect your language resource to one storage account.
-
-## Using a pre-existing Language resource
-
-[!INCLUDE [use an existing resource](../includes/use-pre-existing-resource.md)]
-
-## Create a custom Text Analytics for health project
-
-Once your resource and storage container are configured, create a new custom text analytics for health project. A project is a work area for building your custom AI models based on your data. Your project can only be accessed by you and others who have access to the Azure resource being used. If you have labeled data, you can use it to get started by [importing a project](#import-project).
-
-### [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Language Studio project creation](../includes/language-studio/create-project.md)]
-
-### [REST APIs](#tab/rest-api)
-
-[!INCLUDE [REST APIs project creation](../includes/rest-api/create-project.md)]
-
----
-
-## Import project
-
-If you have already labeled data, you can use it to get started with the service. Make sure that your labeled data follows the [accepted data formats](../concepts/data-formats.md).
-
-### [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Import project](../includes/language-studio/import-project.md)]
-
-### [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Import project](../includes/rest-api/import-project.md)]
-
----
-
-## Get project details
-
-### [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Language Studio project details](../../includes/custom/project-details.md)]
-
-### [REST APIs](#tab/rest-api)
-
-[!INCLUDE [REST APIs project details](../includes/rest-api/project-details.md)]
-
----
-
-## Delete project
-
-### [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Delete project using Language studio](../includes/language-studio/delete-project.md)]
-
-### [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Delete project using the REST API](../includes/rest-api/delete-project.md)]
-
----
-
-## Next steps
-
-* You should have an idea of the [project schema](design-schema.md) you will use to label your data.
-
-* After you define your schema, you can start [labeling your data](label-data.md), which will be used for model training, evaluation, and finally making predictions.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析プロジェクト作成に関するドキュメントの削除"
}
```

### Explanation
この変更では、`create-project.md`ドキュメントが完全に削除されました。この文書は、カスタムテキスト分析プロジェクトを作成するための手順や要件について説明していました。具体的には、Azureのリソースの作成、ストレージアカウントの接続方法、プロジェクトのインポートや削除の方法、さらにはREST APIやLanguage Studioを使用したプロジェクトの管理に関する情報が含まれていました。これらの詳細な手順の削除により、ユーザーはカスタムテキスト分析のプロジェクトを設定する際に必要な情報を失い、作業が複雑になる可能性があります。変更の詳細はGitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/how-to/deploy-model.md{#item-7bddde}

<details>
<summary>Diff</summary>
````diff
@@ -1,105 +0,0 @@
----
-title: Deploy a custom Text Analytics for health model
-titleSuffix: Azure AI services
-description: Learn about deploying a model for custom Text Analytics for health.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h
----
-
-# Deploy a custom text analytics for health model
-
-Once you're satisfied with how your model performs, it's ready to be deployed and used to recognize entities in text. Deploying a model makes it available for use through the [prediction API](https://aka.ms/ct-runtime-swagger).
-
-## Prerequisites
-
-* A successfully [created project](create-project.md) with a configured Azure storage account.
-* Text data that has [been uploaded](design-schema.md#data-preparation) to your storage account.
-* [Labeled data](label-data.md) and a successfully [trained model](train-model.md).
-* Reviewed the [model evaluation details](view-model-evaluation.md) to determine how your model is performing.
-
-For more information, see [project development lifecycle](../overview.md#project-development-lifecycle).
-
-## Deploy model
-
-After you've reviewed your model's performance and decided it can be used in your environment, you need to assign it to a deployment. Assigning the model to a deployment makes it available for use through the [prediction API](https://aka.ms/ct-runtime-swagger). It is recommended to create a deployment named *production* to which you assign the best model you have built so far and use it in your system. You can create another deployment called *staging* to which you can assign the model you're currently working on to be able to test it. You can have a maximum of 10 deployments in your project. 
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Deploy a model using Language Studio](../includes/language-studio/deploy-model.md)]
-   
-# [REST APIs](#tab/rest-api)
-
-### Submit deployment job
-
-[!INCLUDE [deploy model](../includes/rest-api/deploy-model.md)]
-
-### Get deployment job status
-
-[!INCLUDE [get deployment status](../includes/rest-api/get-deployment-status.md)]
-
----
-
-## Swap deployments
-
-After you are done testing a model assigned to one deployment and you want to assign this model to another deployment you can swap these two deployments. Swapping deployments involves taking the model assigned to the first deployment, and assigning it to the second deployment. Then taking the model assigned to second deployment, and assigning it to the first deployment. You can use this process to swap your *production* and *staging* deployments when you want to take the model assigned to *staging* and assign it to *production*. 
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Swap deployments](../includes/language-studio/swap-deployment.md)]
-
-# [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Swap deployments](../includes/rest-api/swap-deployment.md)]
-
----
-
-
-## Delete deployment
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Delete deployment](../includes/language-studio/delete-deployment.md)]
-
-# [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Delete deployment](../includes/rest-api/delete-deployment.md)]
-
----
-
-## Assign deployment resources
-
-You can [deploy your project to multiple regions](../../concepts/custom-features/multi-region-deployment.md) by assigning different Language resources that exist in different regions.
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Assign resource](../../conversational-language-understanding/includes/language-studio/assign-resources.md)]
-
-# [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Assign resource](../../custom-text-classification/includes/rest-api/assign-resources.md)]
-
----
-
-## Unassign deployment resources
-
-When unassigning or removing a deployment resource from a project, you will also delete all the deployments that have been deployed to that resource's region.
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Unassign resource](../../conversational-language-understanding/includes/language-studio/unassign-resources.md)]
-
-# [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Unassign resource](../../custom-text-classification/includes/rest-api/unassign-resources.md)]
-
----
-
-## Next steps
-
-After you have a deployment, you can use it to [extract entities](call-api.md) from text.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析モデルのデプロイに関するドキュメントの削除"
}
```

### Explanation
この変更では、`deploy-model.md`ドキュメントが完全に削除されました。この文書は、カスタムテキスト分析モデルをデプロイする手順や要件について詳細に説明していました。具体的には、モデルが使用可能になるための前提条件、デプロイメントの作成方法、モデルのテスト後のデプロイメントの入れ替え、リソースの割り当てと解除、及びAPIを介して実行する方法などが記載されていました。この情報の削除により、ユーザーはカスタムモデルをデプロイするための手続きを理解する機会を失い、作業がより困難になる可能性があります。変更の詳細はGitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/how-to/design-schema.md{#item-6c40e2}

<details>
<summary>Diff</summary>
````diff
@@ -1,109 +0,0 @@
----
-title: Preparing data and designing a schema for custom Text Analytics for health
-titleSuffix: Azure AI services
-description: Learn about how to select and prepare data, to be successful in creating custom TA4H projects.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h
----
-
-# How to prepare data and define a schema for custom Text Analytics for health
-
-In order to create a custom TA4H model, you will need quality data to train it. This article covers how you should select and prepare your data, along with defining a schema. Defining the schema is the first step in [project development lifecycle](../overview.md#project-development-lifecycle), and it entailing defining the entity types or categories that you need your model to extract from the text at runtime.
-
-## Schema design
-
-Custom Text Analytics for health allows you to extend and customize the Text Analytics for health entity map. The first step of the process is building your schema, which allows you to define the new entity types or categories that you need your model to extract from text in addition to the Text Analytics for health existing entities at runtime.  
-
-* Review documents in your dataset to be familiar with their format and structure.
-
-* Identify the entities you want to extract from the data.
-
-    For example, if you are extracting entities from support emails, you might need to extract "Customer name", "Product name", "Request date", and "Contact information".
-
-* Avoid entity types ambiguity.
-
-    **Ambiguity** happens when entity types you select are similar to each other. The more ambiguous your schema the more labeled data you will need to differentiate between different entity types.
-
-    For example, if you are extracting data from a legal contract, to extract "Name of first party" and "Name of second party" you will need to add more examples to overcome ambiguity since the names of both parties look similar. Avoid ambiguity as it saves time, effort, and yields better results.
-
-* Avoid complex entities. Complex entities can be difficult to pick out precisely from text, consider breaking it down into multiple entities.
-
-    For example, extracting "Address" would be challenging if it's not broken down to smaller entities. There are so many variations of how addresses appear, it would take large number of labeled entities to teach the model to extract an address, as a whole, without breaking it down. However, if you replace "Address" with "Street Name", "PO Box", "City", "State" and "Zip", the model will require fewer labels per entity.
-
-
-## Add entities
-
-To add entities to your project:
-
-1. Move to **Entities** pivot from the top of the page.
-
-2. [Text Analytics for health entities](../../text-analytics-for-health/concepts/health-entity-categories.md) are automatically loaded into your project. To add additional entity categories, select **Add** from the top menu. You will be prompted to type in a name before completing creating the entity.
-
-3. After creating an entity, you'll be routed to the entity details page where you can define the composition settings for this entity.
-
-4. Entities are defined by [entity components](../concepts/entity-components.md): learned, list or prebuilt. Text Analytics for health entities are by default populated with the prebuilt component and cannot have learned components. Your newly defined entities can be populated with the learned component once you add labels for them in your data but cannot be populated with the prebuilt component. 
-
-5. You can add a [list](../concepts/entity-components.md#list-component)  component to any of your entities. 
-
-   
-### Add list component
-
-To add a **list** component, select **Add new list**. You can add multiple lists to each entity.
-
-1. To create a new list, in the *Enter value* text box enter this is the normalized value that will be returned when any of the synonyms values is extracted.
-
-2. For multilingual projects, from the *language* drop-down menu, select the language of the synonyms list and start typing in your synonyms and hit enter after each one. It is recommended to have synonyms lists in multiple languages.
-
-   <!--:::image type="content" source="../media/add-list-component.png" alt-text="A screenshot showing a list component in Language Studio." lightbox="../media/add-list-component.png":::-->
-   
-### Define entity options
-
-Change to the **Entity options** pivot in the entity details page. When multiple components are defined for an entity, their predictions may overlap. When an overlap occurs, each entity's final prediction is determined based on the [entity option](../concepts/entity-components.md#entity-options) you select in this step. Select the one that you want to apply to this entity and select the **Save** button at the top.
-
-   <!--:::image type="content" source="../media/entity-options.png" alt-text="A screenshot showing an entity option in Language Studio." lightbox="../media/entity-options.png":::-->
-
-
-After you create your entities, you can come back and edit them. You can **Edit entity components** or **delete** them by selecting this option from the top menu.
-
-
-## Data selection
-
-The quality of data you train your model with affects model performance greatly.
-
-* Use real-life data that reflects your domain's problem space to effectively train your model. You can use synthetic data to accelerate the initial model training process, but it will likely differ from your real-life data and make your model less effective when used.
-
-* Balance your data distribution as much as possible without deviating far from the distribution in real-life. For example, if you are training your model to extract entities from legal documents that may come in many different formats and languages, you should provide examples that exemplify the diversity as you would expect to see in real life.
-
-* Use diverse data whenever possible to avoid overfitting your model. Less diversity in training data may lead to your model learning spurious correlations that may not exist in real-life data. 
- 
-* Avoid duplicate documents in your data. Duplicate data has a negative effect on the training process, model metrics, and model performance. 
-
-* Consider where your data comes from. If you are collecting data from one person, department, or part of your scenario, you are likely missing diversity that may be important for your model to learn about. 
-
-> [!NOTE]
-> If your documents are in multiple languages, select the **enable multi-lingual** option during [project creation](../quickstart.md) and set the **language** option to the language of the majority of your documents.
-
-## Data preparation
-
-As a prerequisite for creating a project, your training data needs to be uploaded to a blob container in your storage account. You can create and upload training documents from Azure directly, or through using the Azure Storage Explorer tool. Using the Azure Storage Explorer tool allows you to upload more data quickly.  
-
-* [Create and upload documents from Azure](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container)
-* [Create and upload documents using Azure Storage Explorer](/azure/vs-azure-tools-storage-explorer-blobs)
-
-You can only use `.txt` documents. If your data is in other format, you can use [CLUtils parse command](https://github.com/microsoft/CognitiveServicesLanguageUtilities/blob/main/CustomTextAnalytics.CLUtils/Solution/CogSLanguageUtilities.ViewLayer.CliCommands/Commands/ParseCommand/README.md) to change your document format.
-
-You can upload an annotated dataset, or you can upload an unannotated one and [label your data](../how-to/label-data.md) in Language studio. 
- 
-## Test set
-
-When defining the testing set, make sure to include example documents that are not present in the training set. Defining the testing set is an important step to calculate the [model performance](view-model-evaluation.md#model-details). Also, make sure that the testing set includes documents that represent all entities used in your project.
-
-## Next steps
-
-If you haven't already, create a custom Text Analytics for health project. If it's your first time using custom Text Analytics for health, consider following the [quickstart](../quickstart.md) to create an example project. You can also see the [how-to article](../how-to/create-project.md) for more details on what you need to create a project.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析プロジェクトのためのデータ準備とスキーマ設計に関するドキュメントの削除"
}
```

### Explanation
この変更では、`design-schema.md`ドキュメントが完全に削除されました。この文書は、カスタムテキスト分析プロジェクトを作成するために必要なデータの選択と準備、ならびにスキーマの設計方法について詳しく説明していました。具体的には、エンティティタイプの定義やデータ品質の重要性、エンティティの追加方法、データ選択時の注意点とデータ準備の手法について記載されていました。これにより、ユーザーはカスタムプロジェクトの構築に必要な基本的な知識を失い、作業が複雑になることが考えられます。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/how-to/fail-over.md{#item-473399}

<details>
<summary>Diff</summary>
````diff
@@ -1,140 +0,0 @@
----
-title: Back up and recover your custom Text Analytics for health models
-titleSuffix: Azure AI services
-description: Learn how to save and recover your custom Text Analytics for health models.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: conceptual
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h
----
-
-# Back up and recover your custom Text Analytics for health models
-
-When you create a Language resource, you specify a region for it to be created in. From then on, your resource and all of the operations related to it take place in the specified Azure server region. It's rare, but not impossible, to encounter a network issue that affects an entire region. If your solution needs to always be available, then you should design it to fail over into another region. This requires two Azure AI Language resources in different regions and synchronizing custom models across them. 
-
-If your app or business depends on the use of a custom Text Analytics for health model, we recommend that you create a replica of your project in an additional supported region. If a regional outage occurs, you can then access your model in the other fail-over region where you replicated your project.
-
-Replicating a project means that you export your project metadata and assets, and import them into a new project. This only makes a copy of your project settings and tagged data. You still need to [train](./train-model.md) and [deploy](./deploy-model.md) the models to be available for use with [prediction APIs](https://aka.ms/ct-runtime-swagger).
-
-In this article, you will learn to how to use the export and import APIs to replicate your project from one resource to another existing in different supported geographical regions, guidance on keeping your projects in sync and changes needed to your runtime consumption.
-
-##  Prerequisites
-
-* Two Azure AI Language resources in different Azure regions. [Create your resources](./create-project.md#create-a-language-resource) and connect them to an Azure storage account. It's recommended that you connect each of your Language resources to different storage accounts. Each storage account should be located in the same respective regions that your separate Language resources are in. You can follow the [quickstart](../quickstart.md?pivots=rest-api#create-a-new-azure-ai-language-resource-and-azure-storage-account) to create an additional Language resource and storage account.
-
-
-## Get your resource keys endpoint
-
-Use the following steps to get the keys and endpoint of your primary and secondary resources. These will be used in the following steps.
-
-[!INCLUDE [Get keys and endpoint Azure Portal](../includes/get-keys-endpoint-azure.md)]
-
-> [!TIP]
-> Keep a note of keys and endpoints for both primary and secondary resources as well as the primary and secondary container names. Use these values to replace the following placeholders:
-`{PRIMARY-ENDPOINT}`, `{PRIMARY-RESOURCE-KEY}`, `{PRIMARY-CONTAINER-NAME}`, `{SECONDARY-ENDPOINT}`, `{SECONDARY-RESOURCE-KEY}`, and `{SECONDARY-CONTAINER-NAME}`.
-> Also take note of your project name, your model name and your deployment name. Use these values to replace the following placeholders:  `{PROJECT-NAME}`, `{MODEL-NAME}` and `{DEPLOYMENT-NAME}`.
-
-## Export your primary project assets
-
-Start by exporting the project assets from the project in your primary resource.
-
-### Submit export job
-
-Replace the placeholders in the following request with your `{PRIMARY-ENDPOINT}` and `{PRIMARY-RESOURCE-KEY}` that you obtained in the first step.
-
-[!INCLUDE [Export project assets using the REST API](../includes/rest-api/export-project.md)]
-
-### Get export job status
-
-Replace the placeholders in the following request with your `{PRIMARY-ENDPOINT}` and `{PRIMARY-RESOURCE-KEY}` that you obtained in the first step.
-
-[!INCLUDE [Export project assets using the REST API](../includes/rest-api/get-export-status.md)]
-
-
-Copy the response body as you will use it as the body for the next import job.
-
-## Import to a new project 
-
-Now go ahead and import the exported project assets in your new project in the secondary region so you can replicate it.
-
-### Submit import job
-
-Replace the placeholders in the following request with your `{SECONDARY-ENDPOINT}`, `{SECONDARY-RESOURCE-KEY}`, and `{SECONDARY-CONTAINER-NAME}` that you obtained in the first step.
-
-[!INCLUDE [Import project using the REST API](../includes/rest-api/import-project.md)]
-
-### Get import job status
-
-Replace the placeholders in the following request with your `{SECONDARY-ENDPOINT}` and `{SECONDARY-RESOURCE-KEY}` that you obtained in the first step.
-
-[!INCLUDE [Import project using the REST API](../includes/rest-api/get-import-status.md)]
-
-
-## Train your model
-
-After importing your project, you only have copied the project's assets and metadata and assets. You still need to train your model, which will incur usage on your account. 
-
-### Submit training job
-
-Replace the placeholders in the following request with your `{SECONDARY-ENDPOINT}` and `{SECONDARY-RESOURCE-KEY}` that you obtained in the first step.
-
-[!INCLUDE [train model](../includes/rest-api/train-model.md)]
-
-
-### Get training status
-
-Replace the placeholders in the following request with your `{SECONDARY-ENDPOINT}` and `{SECONDARY-RESOURCE-KEY}` that you obtained in the first step.
-
-[!INCLUDE [get training model status](../includes/rest-api/get-training-status.md)]
-
-## Deploy your model
-
-This is the step where you make your trained model available form consumption via the [runtime prediction API](https://aka.ms/ct-runtime-swagger). 
-
-> [!TIP]
-> Use the same deployment name as your primary project for easier maintenance and minimal changes to your system to handle redirecting your traffic.
-
-### Submit deployment job 
-
-Replace the placeholders in the following request with your `{SECONDARY-ENDPOINT}` and `{SECONDARY-RESOURCE-KEY}` that you obtained in the first step.
-
-[!INCLUDE [deploy model](../includes/rest-api/deploy-model.md)]
-
-### Get the deployment status
-
-Replace the placeholders in the following request with your `{SECONDARY-ENDPOINT}` and `{SECONDARY-RESOURCE-KEY}` that you obtained in the first step.
-
-[!INCLUDE [get deploy status](../includes/rest-api/get-deployment-status.md)]
-
-## Changes in calling the runtime
-
-Within your system, at the step where you call [runtime prediction API](https://aka.ms/ct-runtime-swagger) check for the response code returned from the submit task API. If you observe a **consistent** failure in submitting the request, this could indicate an outage in your primary region. Failure once doesn't mean an outage, it may be transient issue. Retry submitting the job through the secondary resource you have created. For the second request use your `{SECONDARY-ENDPOINT}` and `{SECONDARY-RESOURCE-KEY}`, if you have followed the steps above, `{PROJECT-NAME}` and `{DEPLOYMENT-NAME}` would be the same so no changes are required to the request body. 
-
-In case you revert to using your secondary resource you will observe slight increase in latency because of the difference in regions where your model is deployed. 
-
-## Check if your projects are out of sync
-
-Maintaining the freshness of both projects is an important part of the process. You need to frequently check if any updates were made to your primary project so that you move them over to your secondary project. This way if your primary region fails and you move into the secondary region you should expect similar model performance since it already contains the latest updates. Setting the frequency of checking if your projects are in sync is an important choice. We recommend that you do this check daily in order to guarantee the freshness of data in your secondary model.
-
-### Get project details
-
-Use the following url to get your project details, one of the keys returned in the body indicates the last modified date of the project. 
-Repeat the following step twice, one for your primary project and another for your secondary project and compare the timestamp returned for both of them to check if they are out of sync.
-
-  [!INCLUDE [get project details](../includes/rest-api/get-project-details.md)]
-
-
-Repeat the same steps for your replicated project using `{SECONDARY-ENDPOINT}` and `{SECONDARY-RESOURCE-KEY}`. Compare the returned `lastModifiedDateTime` from both projects. If your primary project was modified sooner than your secondary one, you need to repeat the steps of [exporting](#export-your-primary-project-assets), [importing](#import-to-a-new-project), [training](#train-your-model) and [deploying](#deploy-your-model).
-
-
-## Next steps
-
-In this article, you have learned how to use the export and import APIs to replicate your project to a secondary Language resource in other region. Next, explore the API reference docs to see what else you can do with authoring APIs.
-
-* [Authoring REST API reference](https://aka.ms/ct-authoring-swagger)
-
-* [Runtime prediction REST API reference](https://aka.ms/ct-runtime-swagger)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析モデルのバックアップとリカバリに関するドキュメントの削除"
}
```

### Explanation
この変更では、`fail-over.md`ドキュメントが完全に削除されました。この文書は、カスタムテキスト分析モデルのバックアップおよび復元方法を詳しく説明しており、リージョン間でのフェイルオーバー設計の重要性や、複製プロジェクトの作成手順、プロジェクトを同期させるための手法について解説していました。ユーザーは、異なるリージョンにおけるAIリソースの操作やモデルのトレーニング・デプロイに関する具体的な手順を失うことになります。この変更により、システムの可用性を確保するための手段が失われ、ユーザーは新しい構成を理解するために追加の努力が必要となるかもしれません。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/how-to/label-data.md{#item-75aad1}

<details>
<summary>Diff</summary>
````diff
@@ -1,109 +0,0 @@
----
-title: How to label your data for custom Text Analytics for health
-titleSuffix: Azure AI services
-description: Learn how to label your data for use with custom Text Analytics for health.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ner
----
-
-# Label your data using the Language Studio
-
-Data labeling is a crucial step in development lifecycle. In this step, you  label your documents with the new entities you defined in your schema to populate their learned components. This data will be used in the next step when training your model so that your model can learn from the labeled data to know which entities to extract. If you already have labeled data, you can directly [import](create-project.md#import-project) it into your project, but you need to make sure that your data follows the [accepted data format](../concepts/data-formats.md). See [create project](create-project.md#import-project) to learn more about importing labeled data into your project. If your data isn't labeled already, you can label it in the [Language Studio](https://aka.ms/languageStudio).
-
-## Prerequisites
-
-Before you can label your data, you need:
-
-* A successfully [created project](create-project.md) with a configured Azure blob storage account
-* Text data that [has been uploaded](design-schema.md#data-preparation) to your storage account.
-
-See the [project development lifecycle](../overview.md#project-development-lifecycle) for more information.
-
-## Data labeling guidelines
-
-After preparing your data, designing your schema and creating your project, you will need to label your data. Labeling your data is important so your model knows which words will be associated with the entity types you need to extract. When you label your data in [Language Studio](https://aka.ms/languageStudio) (or import labeled data), these labels are stored in the JSON document in your storage container that you have connected to this project. 
-
-As you label your data, keep in mind:
-
-* You can't add labels for Text Analytics for health entities as they're pretrained prebuilt entities. You can only add labels to new entity categories that you defined during schema definition. 
-
-If you want to improve the recall for a prebuilt entity, you can extend it by adding a list component while you are [defining your schema](design-schema.md).
-
-* In general, more labeled data leads to better results, provided the data is labeled accurately.
-
-* The precision, consistency and completeness of your labeled data are key factors to determining model performance. 
-
-    * **Label precisely**: Label each entity to its right type always. Only include what you want extracted, avoid unnecessary data in your labels.
-    * **Label consistently**:  The same entity should have the same label across all the documents.
-    * **Label completely**: Label all the instances of the entity in all your documents. 
-
-   > [!NOTE]
-   > There is no fixed number of labels that can guarantee your model will perform the best. Model performance is dependent on possible ambiguity in your schema, and the quality of your labeled data. Nevertheless, we recommend having around 50 labeled instances per entity type.
-
-## Label your data
-
-Use the following steps to label your data:
-
-1. Go to your project page in [Language Studio](https://aka.ms/languageStudio).
-
-2. From the left side menu, select **Data labeling**. You can find a list of all documents in your storage container.
-
-    <!--:::image type="content" source="../media/tagging-files-view.png" alt-text="A screenshot showing the Language Studio screen for labeling data." lightbox="../media/tagging-files-view.png":::-->
-
-    >[!TIP]
-    > You can use the filters in top menu to view the unlabeled documents so that you can start labeling them.
-    > You can also use the filters to view the documents that are labeled with a specific entity type.
-
-3. Change to a single document view from the left side in the top menu or select a specific document to start labeling. You can find a list of all `.txt` documents available in your project to the left. You can use the **Back** and **Next** button from the bottom of the page to navigate through your documents.
-
-    > [!NOTE]
-    > If you enabled multiple languages for your project, you will find a **Language** dropdown in the top menu, which lets you select the language of each document. Hebrew is not supported with multi-lingual projects.
-
-4. In the right side pane, you can use the **Add entity type** button to add additional entities to your project that you missed during schema definition.
-
-    <!--:::image type="content" source="../media/tag-1.png" alt-text="A screenshot showing complete data labeling." lightbox="../media/tag-1.png":::-->
-
-5. You have two options to label your document:
-    
-    |Option |Description  |
-    |---------|---------|
-    |Label using a brush     | Select the brush icon next to an entity type in the right pane, then highlight the text in the document you want to annotate with this entity type.           |
-    |Label using a menu    | Highlight the word you want to label as an entity, and a menu will appear. Select the entity type you want to assign for this entity.        |
-    
-    The below screenshot shows labeling using a brush.
-    
-    :::image type="content" source="../media/tag-options.png" alt-text="A screenshot showing the labeling options offered in Custom NER." lightbox="../media/tag-options.png":::
-    
-6. In the right side pane under the **Labels** pivot you can find all the entity types in your project and the count of labeled instances per each. The prebuilt entities will be shown for reference but you will not be able to label for these prebuilt entities as they are pretrained.
-
-7. In the bottom section of the right side pane you can add the current document you are viewing to the training set or the testing set. By default all the documents are added to your training set. See [training and testing sets](train-model.md#data-splitting) for information on how they are used for model training and evaluation.
-
-    > [!TIP]
-    > If you are planning on using **Automatic** data splitting, use the default option of assigning all the documents into your training set.
-
-7. Under the **Distribution** pivot you can view the distribution across training and testing sets. You have two options for viewing:
-   * *Total instances* where you can view count of all labeled instances of a specific entity type.
-   * *Documents with at least one label* where each document is counted if it contains at least one labeled instance of this entity.
-  
-7. When you're labeling, your changes are synced periodically, if they have not been saved yet you will find a warning at the top of your page. If you want to save manually, select **Save labels** button at the bottom of the page.
-
-## Remove labels
-
-To remove a label
-
-1. Select the entity you want to remove a label from.
-2. Scroll through the menu that appears, and select **Remove label**.
-
-## Delete entities
-
-You cannot delete any of the Text Analytics for health pretrained entities because they have a prebuilt component. You are only permitted to delete newly defined entity categories. To delete an entity, select the delete icon next to the entity you want to remove. Deleting an entity removes all its labeled instances from your dataset. 
-
-## Next steps
-
-After you've labeled your data, you can begin [training a model](train-model.md) that will learn based on your data.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析モデル用のデータラベリングに関するドキュメントの削除"
}
```

### Explanation
この変更では、`label-data.md`ドキュメントが完全に削除されました。この文書は、カスタムテキスト分析モデルのためのデータラベリング方法について詳細に説明しており、ラベリングの重要性や、ラベリングのための手順、ガイドラインについて述べていました。具体的には、データのアップロード、ラベリングのためのツールの使用、ラベルの削除、エンティティの管理に関する情報が含まれていました。この変更により、ユーザーはデータラベリングのプロセスを理解するための重要なリソースを失うこととなり、モデルの適切なトレーニングに向けた準備が難しくなる可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/how-to/train-model.md{#item-328f92}

<details>
<summary>Diff</summary>
````diff
@@ -1,82 +0,0 @@
----
-title: How to train your custom Text Analytics for health model
-titleSuffix: Azure AI services
-description: Learn about how to train your model for custom Text Analytics for health.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h
----
-
-# Train your custom Text Analytics for health model
-
-Training is the process where the model learns from your [labeled data](label-data.md). After training is completed, you'll be able to view the [model's performance](view-model-evaluation.md) to determine if you need to improve your model.
-
-To train a model, you start a training job and only successfully completed jobs create a model. Training jobs expire after seven days, which means you won't be able to retrieve the job details after this time. If your training job completed successfully and a model was created, the model won't be affected. You can only have one training job running at a time, and you can't start other jobs in the same project. 
-
-The training times can be anywhere from a few minutes when dealing with few documents, up to several hours depending on the dataset size and the complexity of your schema.
-
-
-## Prerequisites
-
-* A successfully [created project](create-project.md) with a configured Azure blob storage account
-* Text data that [has been uploaded](design-schema.md#data-preparation) to your storage account.
-* [Labeled data](label-data.md)
-
-See the [project development lifecycle](../overview.md#project-development-lifecycle) for more information.
-
-## Data splitting
-
-Before you start the training process, labeled documents in your project are divided into a training set and a testing set. Each one of them serves a different function.
-The **training set** is used in training the model, this is the set from which the model learns the labeled entities and what spans of text are to be extracted as entities. 
-The **testing set** is a blind set that is not introduced to the model during training but only during evaluation. 
-After model training is completed successfully, the model is used to make predictions from the documents in the testing and based on these predictions [evaluation metrics](../concepts/evaluation-metrics.md) are calculated. Model training and evaluation are only for newly defined entities with learned components; therefore, Text Analytics for health entities are excluded from model training and evaluation due to them being entities with prebuilt components. It's recommended to make sure that all your labeled entities are adequately represented in both the training and testing set.
-
-Custom Text Analytics for health supports two methods for data splitting:
-
-* **Automatically splitting the testing set from training data**:The system splits your labeled data between the training and testing sets, according to the percentages you choose. The recommended percentage split is 80% for training and 20% for testing. 
-
- > [!NOTE]
- > If you choose the **Automatically splitting the testing set from training data** option, only the data assigned to training set will be split according to the percentages provided.
-
-* **Use a manual split of training and testing data**: This method enables users to define which labeled documents should belong to which set. This step is only enabled if you have added documents to your testing set during [data labeling](label-data.md).
-
-## Train model
-
-# [Language studio](#tab/Language-studio)
-
-[!INCLUDE [Train model](../includes/language-studio/train-model.md)]
-
-# [REST APIs](#tab/REST-APIs)
-
-### Start training job
-
-[!INCLUDE [train model](../includes/rest-api/train-model.md)]
-
-### Get training job status
-
-Training could take sometime depending on the size of your training data and complexity of your schema. You can use the following request to keep polling the status of the training job until it's successfully completed.
-
- [!INCLUDE [get training model status](../includes/rest-api/get-training-status.md)]
-
----
-
-### Cancel training job
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Cancel training](../includes/language-studio/cancel-training.md)]
-
-# [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Cancel training](../includes/rest-api/cancel-training.md)]
-
----
-
-## Next steps
-
-After training is completed, you'll be able to view the [model's performance](view-model-evaluation.md) to optionally improve your model if needed. Once you're satisfied with your model, you can deploy it, making it available to use for [extracting entities](call-api.md) from text.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析モデルのトレーニングに関するドキュメントの削除"
}
```

### Explanation
この変更では、`train-model.md`ドキュメントが完全に削除されました。この文書は、カスタムテキスト分析モデルのトレーニング方法に関する重要な情報を提供しており、トレーニングプロセスやデータの分割方法、トレーニングジョブの開始とキャンセルの手順について述べていました。特に、トレーニングセットとテストセットの役割や、データの手動分割および自動分割の選択肢についての説明が含まれていました。このドキュメントの削除により、ユーザーはモデルのトレーニングについての重要なリソースを失い、適切なトレーニング手順を理解するために追加の情報を探す必要があるかもしれません。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/how-to/view-model-evaluation.md{#item-463e8a}

<details>
<summary>Diff</summary>
````diff
@@ -1,75 +0,0 @@
----
-title: Evaluate a Custom Text Analytics for health model
-titleSuffix: Azure AI services
-description: Learn how to evaluate and score your Custom Text Analytics for health model
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h
----
-
-
-# View a custom text analytics for health model's evaluation and details
-
-After your model has finished training, you can view the model performance and see the extracted entities for the documents in the test set. 
-
-> [!NOTE]
-> Using the **Automatically split the testing set from training data** option may result in different model evaluation result every time you train a new model, as the test set is selected randomly from the data. To make sure that the evaluation is calculated on the same test set every time you train a model, make sure to use the **Use a manual split of training and testing data** option when starting a training job and define your **Test** documents when [labeling data](label-data.md).
-
-## Prerequisites
-
-Before viewing model evaluation, you need:
-
-* A successfully [created project](create-project.md) with a configured Azure blob storage account.
-* Text data that [has been uploaded](design-schema.md#data-preparation) to your storage account.
-* [Labeled data](label-data.md)
-* A [successfully trained model](train-model.md)
-
-
-## Model details
-
-There are several metrics you can use to evaluate your mode. See the [performance metrics](../concepts/evaluation-metrics.md) article for more information on the model details described in this article.
-
-### [Language studio](#tab/language-studio)
-
-[!INCLUDE [View model evaluation using Language Studio](../../includes/custom/model-evaluation-language-studio.md)]
-
-### [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Model evaluation](../includes/rest-api/model-evaluation.md)]
-
----
-
-## Load or export model data
-
-### [Language studio](#tab/Language-studio)
-
-[!INCLUDE [Load export model](../../includes/custom/load-export-model-language-studio.md)]
-
-
-### [REST APIs](#tab/REST-APIs)
-
-[!INCLUDE [Load export model](../../includes/custom/load-export-model-rest-api.md)]
-
----
-
-## Delete model
-
-### [Language studio](#tab/language-studio)
-
-[!INCLUDE [Delete model](../../includes/custom/delete-model-language-studio.md)]
-
-### [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Delete model](../../includes/custom/delete-model-rest-api.md)]
-
----
-
-## Next steps
-
-* [Deploy your model](deploy-model.md)
-* Learn about the [metrics used in evaluation](../concepts/evaluation-metrics.md). 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析モデルの評価に関するドキュメントの削除"
}
```

### Explanation
この変更では、`view-model-evaluation.md`ドキュメントが完全に削除されました。このドキュメントは、カスタムテキスト分析モデルの評価方法に関する重要な情報を提供しており、モデルのパフォーマンスの確認方法や、テストセットから抽出されたエンティティの表示方法について説明していました。また、トレーニング時に使用するテストセットの管理についての注意点や、モデルの詳細評価に必要な前提条件も含まれていました。このドキュメントの削除により、ユーザーはモデル評価の手順やパフォーマンス指標に関する情報を失い、今後のモデル改善のための重要なリソースが得られなくなります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/get-keys-endpoint-azure.md{#item-6156ce}

<details>
<summary>Diff</summary>
````diff
@@ -1,15 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-1. Go to your resource overview page in the [Azure portal](https://portal.azure.com/#home)
-
-2. From the menu on the left side, select **Keys and Endpoint**. You'll use the endpoint and key for the API requests 
-
-    :::image type="content" source="../../custom-text-classification/media/get-endpoint-azure.png" alt-text="A screenshot showing the key and endpoint page in the Azure portal" lightbox="../../custom-text-classification/media/get-endpoint-azure.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azureのキーとエンドポイント取得に関する情報の削除"
}
```

### Explanation
この変更では、`get-keys-endpoint-azure.md`ドキュメントが完全に削除されました。この文書は、Azureポータルでリソースのキーとエンドポイントを取得する方法についての手順を説明していました。具体的には、Azureポータルでのリソースの概要ページにアクセスし、メニューから「キーとエンドポイント」を選択する方法が示されていました。また、APIリクエストに必要なキーとエンドポイントの利用についても言及されていました。このドキュメントの削除により、ユーザーはAzureの設定に関する重要な手順を失い、カスタムテキスト分析モデルを使用する際の前提条件を満たすための情報にアクセスできなくなります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/language-studio/cancel-training.md{#item-d752dc}

<details>
<summary>Diff</summary>
````diff
@@ -1,11 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-To cancel a training job from within [Language Studio](https://aka.ms/languageStudio), go to the **Training jobs** page. Select the training job you want to cancel and select **Cancel** from the top menu. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioでのトレーニングキャンセル方法に関する情報の削除"
}
```

### Explanation
この変更では、`cancel-training.md`ドキュメントが完全に削除されました。この文書は、Language Studio内でトレーニングジョブをキャンセルする方法に関する手順を説明しており、トレーニングジョブページにアクセスし、キャンセルしたいトレーニングジョブを選択してから「キャンセル」オプションを選ぶ方法が記載されていました。このドキュメントの削除により、ユーザーはトレーニングプロセスの管理に必要な重要な情報を失うことになり、特にトレーニングの状態を変更する際の手引きがなくなります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/language-studio/create-project.md{#item-ba82ba}

<details>
<summary>Diff</summary>
````diff
@@ -1,39 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-1. Sign into the [Language Studio](https://aka.ms/languageStudio). A window will appear to let you select your subscription and Language resource. Select the Language resource you created in the above step. 
-
-2. Under the **Extract information** section of Language Studio, select **Custom Text Analytics for health**.
-
-    <!--:::image type="content" source="../../media/select-custom-TA4H.png" alt-text="A screenshot showing the location of custom TA4H in the Language Studio landing page." lightbox="../../media/select-custom-TA4H.png":::-->
-
-3. Select **Create new project** from the top menu in your projects page. Creating a project lets you label data, train, evaluate, improve, and deploy your models. 
-
-    :::image type="content" source="../../media/create-project.png" alt-text="A screenshot of the project creation page." lightbox="../../media/create-project.png":::
-
-4. Enter the project information, including a name, description, and the language of the files in your project. If you're using the [example dataset](https://aka.ms/custom-ta4h-quickstart-samples), select **English**. You can't change the name of your project later. Select **Next**
-
-    > [!TIP]
-    > Your dataset doesn't have to be entirely in the same language. You can have multiple documents, each with different supported languages. If your dataset contains documents of different languages or if you expect text from different languages during runtime, select **enable multi-lingual dataset** option when you enter the basic information for your project. This option can be enabled later from the **Project settings** page.
-
-5.  After you select **Create new project**, a window will appear to let you connect your storage account. If you've already connected a storage account, you will see the storage accounted connected. If not, choose your storage account from the dropdown that appears and select **Connect storage account**; this will set the required roles for your storage account. This step will possibly return an error if you are not assigned as **owner** on the storage account.
-
-    >[!NOTE]
-    > * You only need to do this step once for each new resource you use. 
-    > * This process is irreversible, if you connect a storage account to your Language resource you cannot disconnect it later.
-    > * You can only connect your Language resource to one storage account.
-    
-    :::image type="content" source="../../media/connect-storage.png" alt-text="A screenshot showing the storage connection screen." lightbox="../../media/connect-storage.png":::
-
-6. Select the container where you have uploaded your dataset.
-
-7. If you have already labeled data make sure it follows the supported format and select **Yes, my files are already labeled and I have formatted JSON labels file** and select the labels file from the drop-down menu. Select **Next**. If you are using the dataset from the QuickStart, there is no need to review the formatting of the JSON labels file. 
-
-8. Review the data you entered and select **Create Project**.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioでのプロジェクト作成に関する情報の削除"
}
```

### Explanation
この変更では、`create-project.md`ドキュメントが完全に削除されました。この文書は、Language Studio内で新しいプロジェクトを作成するための詳細な手順を提供しており、プロジェクトの名前、説明、言語設定や、必要に応じてストレージアカウントの接続方法など、多くの重要なステップを説明していました。具体的には、データのラベル付けやモデルのトレーニング、評価、改善、デプロイに関する内容が含まれていました。このドキュメントの削除により、ユーザーはプロジェクト作成プロセスに関する重要な情報を失い、新しいテキスト分析プロジェクトの開始が困難になる可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/language-studio/delete-deployment.md{#item-0f0d7c}

<details>
<summary>Diff</summary>
````diff
@@ -1,12 +0,0 @@
----
-titleSuffix: Azure AI services
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-To delete a deployment from within [Language Studio](https://aka.ms/laguageStudio), go to the **Deploying a model** page. Select the deployment you want to delete and select **Delete deployment** from the top menu. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioでのデプロイメント削除方法に関する情報の削除"
}
```

### Explanation
この変更では、`delete-deployment.md`ドキュメントが完全に削除されました。この文書は、Language Studio内でデプロイメントを削除する方法について、関連する手順を詳しく説明していました。具体的には、モデルのデプロイメントページにアクセスし、削除したいデプロイメントを選択して「デプロイメントの削除」オプションを選ぶという内容が含まれていました。このドキュメントの削除により、ユーザーはデプロイメントの管理に必要な重要な情報を失うことになり、特に不要なデプロイメントを効率的に削除できなくなるリスクがあります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/language-studio/delete-project.md{#item-f5cf6c}

<details>
<summary>Diff</summary>
````diff
@@ -1,15 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
-ms.custom: language-service-custom-classification
----
-
-When you don't need your project anymore, you can delete your project using [Language Studio](https://aka.ms/custom-extraction). 
-1. Select the Language service feature you're using at the top of the page, s
-1. Select the project you want to delete
-1. Select **Delete** from the top menu.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioでのプロジェクト削除に関する情報の削除"
}
```

### Explanation
この変更では、`delete-project.md`ドキュメントが完全に削除されました。この文書は、Language Studio内でプロジェクトを削除する手順を詳細に説明しており、不要になったプロジェクトを効率的に管理するための重要な情報を提供していました。具体的には、使用中の言語サービス機能を選択し、削除したいプロジェクトを選択した後、メニューから「削除」オプションを選ぶという流れが記載されていました。このドキュメントの削除により、ユーザーはプロジェクト管理のプロセスを理解しづらくなり、不要なプロジェクトを適切に処理することが難しくなる可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/language-studio/deploy-model.md{#item-6515b1}

<details>
<summary>Diff</summary>
````diff
@@ -1,28 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-To deploy your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Deploying a model** from the left side menu.
-
-2. Select **Add deployment** to start a new deployment job.
-
-    :::image type="content" source="../../media/deploy-model.png" alt-text="A screenshot showing the deployment button in Language Studio." lightbox="../../media/deploy-model.png":::
-
-3. Select **Create new deployment** to create a new deployment and assign a trained model from the dropdown below. You can also **Overwrite an existing deployment** by selecting this option and select the trained model you want to assign to it from the dropdown below.
-
-    > [!NOTE]
-    > Overwriting an existing deployment doesn't require changes to your [prediction API](https://aka.ms/ct-runtime-swagger) call but the results you get will be based on the newly assigned model.
-    
-   :::image type="content" source="../../media/add-deployment.png" alt-text="A screenshot showing the model deployment options in Language Studio." lightbox="../../media/add-deployment.png":::
-     
-4. Select **Deploy** to start the deployment job.
-
-5. After deployment is successful, an expiration date will appear next to it. [Deployment expiration](../../../concepts/model-lifecycle.md#expiration-timeline) is when your deployed model will be unavailable to be used for prediction, which typically happens **twelve** months after a training configuration expires.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioでのモデルデプロイに関する情報の削除"
}
```

### Explanation
この変更では、`deploy-model.md`ドキュメントが完全に削除されました。この文書は、Language Studioを使用してモデルをデプロイする方法を詳細に説明しており、ユーザーがデプロイメントプロセスを理解し、実行するための具体的な手順が含まれていました。手順には、デプロイメントジョブを開始するための「デプロイメントの追加」、新しいデプロイメントの作成、既存のデプロイメントの上書き、そしてデプロイメント開始後の有効期限の確認が含まれていました。このドキュメントの削除により、ユーザーはモデルデプロイメントの手順を失い、デプロイメントに関する重要な情報にアクセスできなくなります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/language-studio/import-project.md{#item-cd3b25}

<details>
<summary>Diff</summary>
````diff
@@ -1,44 +0,0 @@
----
-titleSuffix: Azure AI services
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-1. Sign into the [Language Studio](https://aka.ms/languageStudio). A window will appear to let you select your subscription and Language resource. Select your Language resource. 
-
-2. Under the **Extract information** section of Language Studio, select **Custom text analytics for health**.
-
-    <!--:::image type="content" source="../../media/select-custom-ner.png" alt-text="A screenshot showing the location of the custom NER feature in the Language Studio landing page." lightbox="../../media/select-custom-ner.png":::-->
-        
-
-3. Select **Create new project** from the top menu in your projects page. Creating a project will let you tag data, train, evaluate, improve, and deploy your models. 
-
-    <!--:::image type="content" source="../../media/create-project.png" alt-text="A screenshot of the project creation page." lightbox="../../media/create-project.png":::-->
-
-
-4.  After you select **Create new project**, a screen will appear to let you connect your storage account. If you can’t find your storage account, make sure you created a resource using the recommended steps. If you've already connected a storage account to your Language resource, you will see your storage account connected.
-
-    >[!NOTE]
-    > * You only need to do this step once for each new language resource you use. 
-    > * This process is irreversible, if you connect a storage account to your Language resource you cannot disconnect it later.
-    > * You can only connect your Language resource to one storage account.
-
-    :::image type="content" source="../../media/connect-storage.png" alt-text="A screenshot of the storage connection screen for new projects." lightbox="../../media/connect-storage.png":::
-
-4. Enter the project information, including a name, description, and the language of the files in your project. You won’t be able to change the name of your project later. Select **Next**.
-       
-    >[!TIP]
-    > Your dataset doesn't have to be entirely in the same language. You can have multiple documents, each with different supported languages. If your dataset contains documents of different languages or if you expect text from different languages during runtime, select **enable multi-lingual dataset** option when you enter the basic information for your project. This option can be enabled later from the **Project settings** page.
-
-5. Select the container where you have uploaded your dataset. 
-
-7. Select **Yes, my files are already labeled and I have formatted JSON labels file** and select the labels file from the drop-down menu below to import your JSON labels file. Make sure it follows the [supported format](../../concepts/data-formats.md).
-
-8.   Select **Next**.
-
-9. Review the data you entered and select **Create Project**.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioでのプロジェクトインポートに関する情報の削除"
}
```

### Explanation
この変更では、`import-project.md`ドキュメントが完全に削除されました。この文書は、Language Studioを使用してプロジェクトをインポートするための詳細な手順を提供していました。具体的には、ユーザーがサインインし、言語リソースを選択し、新しいプロジェクトを作成してデータをタグ付けする方法、ストレージアカウントを接続する手順、およびプロジェクトに関する情報（名前や説明、言語）の入力について説明していました。また、複数の言語を含むデータセットのサポートや、フォーマットされたJSONラベルファイルの取り込み方法も含まれていました。この情報の削除により、ユーザーはプロジェクトインポートの重要な手順を失い、Language Studioでの操作が困難になる可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/language-studio/swap-deployment.md{#item-4ed03f}

<details>
<summary>Diff</summary>
````diff
@@ -1,16 +0,0 @@
----
-titleSuffix: Azure AI services
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-To swap deployments from within [Language Studio](https://aka.ms/laguageStudio):
-
-1. In the **Deploying a model** page, select the two deployments you want to swap and select **Swap deployments** from the top menu. 
-
-2. From the window that appears, select the names of the deployments you want to swap. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioでのデプロイメントのスワップに関する情報の削除"
}
```

### Explanation
この変更では、`swap-deployment.md`ドキュメントが完全に削除されました。この文書は、Language Studioを使用してデプロイメントをスワップする手順を説明しており、ユーザーがモデルを効率的に管理できるようにするための重要な情報を提供していました。具体的には、デプロイメントページからスワップしたい2つのデプロイメントを選択し、「デプロイメントをスワップ」するための選択肢を使用して、デプロイメント名を選ぶ手順が含まれていました。この情報が削除されることで、ユーザーはデプロイメントの管理方法に関する知識を失い、操作が困難になる可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/language-studio/test-model.md{#item-f5996f}

<details>
<summary>Diff</summary>
````diff
@@ -1,26 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
-ms.custom: language-service-custom-text-analytics-for-health-model-testing
----
-
-To test your deployed models from within the [Language Studio](https://aka.ms/LanguageStudio):
-1. Select **Testing deployments** from the left side menu.
-
-2. Select the deployment you want to test. You can only test models that are assigned to deployments. 
-
-3. Select the deployment you want to query/test from the dropdown.
-
-4. You can enter the text you want to submit to the request or upload a `.txt` file to use.
-
-5. Select **Run the test** from the top menu.
-
-6. In the **Result** tab, you can see the extracted entities from your text and their types. You can also view the [JSON response](../../how-to/call-api.md#get-task-results) under the **JSON** tab.
-
-    :::image type="content" source="../../media/test-model-results.png" alt-text="A screenshot showing the deployment testing screen in Language Studio." lightbox="../../media/test-model-results.png":::
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioでのモデルテストに関する情報の削除"
}
```

### Explanation
この変更では、`test-model.md`ドキュメントが完全に削除されました。この文書は、Language Studioを使用してデプロイされたモデルをテストするための手順を詳細に説明していました。具体的には、ユーザーがテストしたいデプロイメントを選択し、テキストを入力したり`.txt`ファイルをアップロードしたりする方法、テストを実行するための手順、そして結果として抽出されたエンティティやそのタイプを確認する方法が含まれていました。また、JSONレスポンスを確認するための方法も記載されていました。この情報が削除されることで、ユーザーはモデルテストを行うための重要な手順を失い、Language Studioでの操作が困難になる可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/language-studio/train-model.md{#item-d22149}

<details>
<summary>Diff</summary>
````diff
@@ -1,30 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-To start training your model from within the [Language Studio](https://aka.ms/LanguageStudio):
-
-1. Select **Training jobs** from the left side menu.
-
-2. Select **Start a training job** from the top menu.
-
-3. Select **Train a new model** and type in the model name in the text box. You can also **overwrite an existing model** by selecting this option and choosing the model you want to overwrite from the dropdown menu. Overwriting a trained model is irreversible, but it won't affect your deployed models until you deploy the new model.
-
-    :::image type="content" source="../../media/train-model.png" alt-text="A screenshot showing the training job creation screen in Language Studio." lightbox="../../media/train-model.png":::
-    
-4. Select data splitting method. You can choose **Automatically splitting the testing set from training data** where the system will split your labeled data between the training and testing sets, according to the specified percentages. Or you can **Use a manual split of training and testing data**, this option is only enabled if you have added documents to your testing set. See [data labeling](../../how-to/label-data.md) and [how to train a model](../../how-to/train-model.md#data-splitting) for information about data splitting.
-
-5. Select the **Train** button.
-
-6. If you select the Training Job ID from the list, a side pane will appear where you can check the **Training progress**, **Job status**, and other details for this job.
-
-    > [!NOTE]
-    > * Only successfully completed training jobs will generate models.
-    > * Training can take some time between a couple of minutes and several hours based on the size of your labeled data.
-    > * You can only have one training job running at a time. You can't start other training job within the same project until the running job is completed. 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioでのモデルトレーニングに関する情報の削除"
}
```

### Explanation
この変更では、`train-model.md`ドキュメントが完全に削除されました。この文書は、Language Studioを使用してモデルをトレーニングするための手順を詳細に説明していました。具体的には、トレーニングジョブを開始するための選択メニューや、新しいモデルの名前を入力する方法、既存のモデルを上書きするオプション、データの分割方法の選択肢、トレーニングの進捗状況やジョブのステータスを確認する方法が含まれていました。この情報が削除されることで、ユーザーはモデルのトレーニングに関する重要な手順を失い、Language Studioでの作業が困難になる可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/quickstarts/blob-storage-upload.md{#item-52b1f8}

<details>
<summary>Diff</summary>
````diff
@@ -1,29 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-After you have created an Azure storage account and connected it to your Language resource, you will need to upload the documents from the sample dataset to the root directory of your container. These documents will later be used to train your model.
-
-
-1. [Download the sample dataset](https://aka.ms/custom-ta4h-quickstart-samples) from GitHub. 
-
-2. Open the .zip file, and extract the folder containing the documents. 
-
-2. In the [Azure portal](https://portal.azure.com), navigate to the storage account you created, and select it.
-
-3. In your storage account, select **Containers** from the left menu, located below **Data storage**. On the screen that appears, select **+ Container**. Give the container the name **example-data** and leave the default **Public access level**.
-
-    :::image type="content" source="../../media/storage-screen.png" alt-text="A screenshot showing the main page for a storage account." lightbox="../../media/storage-screen.png":::
-
-4. After your container has been created, select it. Then select **Upload** button to select the `.txt` and `.json` files you downloaded earlier. 
-
-    :::image type="content" source="../../media/file-upload-screen.png" alt-text="A screenshot showing the button for uploading files to the storage account." lightbox="../../media/file-upload-screen.png":::
-
-
-The provided sample dataset contains 12 clinical notes. Each clinical note includes several medical entities and the treatment location. We will use the prebuilt entities to extract the medical entities and train the custom model to extract the treatment location using the entity's learned and list components.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Blobストレージへのアップロードに関するクイックスタート情報の削除"
}
```

### Explanation
この変更では、`blob-storage-upload.md`ドキュメントが完全に削除されました。この文書は、Azureストレージアカウントを作成し、Languageリソースに接続した後に、サンプルデータセットの文書をコンテナのルートディレクトリにアップロードする手順を説明していました。具体的には、サンプルデータセットのダウンロード、Azureポータルでのストレージアカウントの選択、コンテナの作成、ファイルのアップロード手順が記載されていました。この情報が削除されることで、ユーザーは文書のアップロードおよびモデルのトレーニングに必要な手順を失い、システムの利用が難しくなる可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/quickstarts/language-studio.md{#item-75ac6e}

<details>
<summary>Diff</summary>
````diff
@@ -1,81 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-## Prerequisites
-
-* Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services)
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=Language-studio&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Prerequisites" target="_target">I ran into an issue</a>
-
-## Create a new Azure AI Language resource and Azure storage account
-
-Before you can use custom Text Analytics for health, you need to create an Azure AI Language resource, which will give you the credentials that you need to create a project and start training a model. You'll also need an Azure storage account, where you can upload your dataset that is used to build your model.
-
-> [!IMPORTANT]
-> To quickly get started, we recommend creating a new Azure AI Language resource using the steps provided in this article. Using the steps in this article will let you create the Language resource and storage account at the same time, which is easier than doing it later.
->
-> If you have a pre-existing resource that you'd like to use, you will need to connect it to storage account. For more information, see [guidance to using a pre-existing resource](../../how-to/create-project.md#using-a-pre-existing-language-resource).
-
-[!INCLUDE [create a new resource from the Azure portal](../resource-creation-azure-portal.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=Language-studio&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Create-a-new-azure-language-resource-and-storage-account" target="_target">I ran into an issue</a>
-
-## Upload sample data to blob container
-
-[!INCLUDE [Uploading sample data for custom TA4H](blob-storage-upload.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=Language-studio&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Upload-sample-data-to-blob-container" target="_target">I ran into an issue</a>
-
-## Create a custom Text Analytics for health project
-
-Once your resource and storage account are configured, create a new custom Text Analytics for health project. A project is a work area for building your custom ML models based on your data. Your project can only be accessed by you and others who have access to the Language resource being used.
-
-[!INCLUDE [Create a custom Text Analytics for health project](../language-studio/create-project.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=Language-studio&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Create-custom-named-entity-recognition-project" target="_target">I ran into an issue</a>
-
-## Train your model
-
-Typically after you create a project, you go ahead and start labeling the documents you have in the container connected to your project. For this quickstart, you have imported a sample tagged dataset and initialized your project with the sample JSON labels file so there is no need to add additional labels.
-
-[!INCLUDE [Train a model using Language Studio](../language-studio/train-model.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=Language-studio&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Train-model" target="_target">I ran into an issue</a>
-
-## Deploy your model
-
-Generally after training a model you would review its evaluation details and make improvements if necessary. In this quickstart, you will just deploy your model, and make it available for you to try in Language studio, or you can call the [prediction API](https://aka.ms/ct-runtime-swagger).
-
-[!INCLUDE [Deploy a model using Language Studio](../language-studio/deploy-model.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=Language-studio&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Deploy-model" target="_target">I ran into an issue</a>
-
-
-## Test your model
-
-After your model is deployed, you can start using it to extract entities from your text via [Prediction API](https://aka.ms/ct-runtime-swagger). For this quickstart, you will use the [Language Studio](https://aka.ms/LanguageStudio) to submit the custom Text Analytics for health prediction task and visualize the results. In the sample dataset you downloaded earlier, you can find some test documents that you can use in this step.
-
-[!INCLUDE [Test a model using Language Studio](../language-studio/test-model.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=Language-studio&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Test-model" target="_target">I ran into an issue</a>
-
-## Clean up resources
-
-[!INCLUDE [Delete project using Language Studio](../language-studio/delete-project.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=Language-studio&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Clean-up-projects" target="_target">I ran into an issue</a>
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Language Studioに関するクイックスタート情報の削除"
}
```

### Explanation
この変更では、`language-studio.md`ドキュメントが完全に削除されました。この文書は、Language Studioを使用してカスタムテキスト分析プロジェクトを作成し、モデルをトレーニングするための手順を包括的に説明していました。具体的には、Azure AI Languageリソースとストレージアカウントの作成、サンプルデータのアップロード、プロジェクトの作成、モデルのトレーニング、デプロイ、テスト、リソースのクリーンアップに関する詳細なガイドが含まれていました。この情報が削除されることで、ユーザーはカスタムテキスト分析プロジェクトを効果的に開始するための重要な手順を失い、その結果、Language Studioの利用が困難になる恐れがあります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/quickstarts/rest-api.md{#item-218739}

<details>
<summary>Diff</summary>
````diff
@@ -1,128 +0,0 @@
----
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-## Prerequisites
-
-* Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services)
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Trigger-import-project-job" target="_target">I ran into an issue</a>
-
-## Create a new Azure AI Language resource and Azure storage account
-
-Before you can use custom Text Analytics for health, you'll need to create an Azure AI Language resource, which will give you the credentials that you need to create a project and start training a model. You'll also need an Azure storage account, where you can upload your dataset that will be used in building your model.
-
-> [!IMPORTANT]
-> To get started quickly, we recommend creating a new Azure AI Language resource using the steps provided in this article, which will let you create the Language resource, and create and/or connect a storage account at the same time, which is easier than doing it later.
->
-> If you have a pre-existing resource that you'd like to use, you will need to connect it to storage account. See [create project](../../how-to/create-project.md#using-a-pre-existing-language-resource) for more information.
-
-[!INCLUDE [create a new resource from the Azure portal](../resource-creation-azure-portal.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Create-new-resource" target="_target">I ran into an issue</a>
-
-## Upload sample data to blob container
-
-[!INCLUDE [Uploading sample data for custom Text Analytics for health](blob-storage-upload.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Upload-sample-data-to-blob-container" target="_target">I ran into an issue</a>
-
-### Get your resource keys and endpoint
-
-[!INCLUDE [Get keys and endpoint Azure Portal](../get-keys-endpoint-azure.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Get-resource-keys-and-endpoint" target="_target">I ran into an issue</a>
-
-## Create a custom Text Analytics for health project
-
-Once your resource and storage account are configured, create a new custom Text Analytics for health project. A project is a work area for building your custom ML models based on your data. Your project can only be accessed by you and others who have access to the Language resource being used.
-
-Use the labels file you downloaded from the sample data in the previous step and add it to the body of the following request. 
-
-### Trigger import project job 
-
-[!INCLUDE [Import a project using the REST API](../rest-api/import-project.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Trigger-import-project-job" target="_target">I ran into an issue</a>
-
-### Get import job status
-
- [!INCLUDE [get import project status](../rest-api/get-import-status.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Get-import-job-status" target="_target">I ran into an issue</a>
-
-## Train your model
-
-Typically after you create a project, you go ahead and start labeling the documents you have in the container connected to your project. For this quickstart, you have imported a sample tagged dataset and initialized your project with the sample JSON tags file.
-
-### Start training job
-
-After your project has been imported, you can start training your model. 
-
-[!INCLUDE [train model](../rest-api/train-model.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Start-training-your-job" target="_target">I ran into an issue</a>
-
-### Get training job status
-
-Training could take sometime between 10 and 30 minutes for this sample dataset. You can use the following request to keep polling the status of the training job until it is successfully completed.
-
-[!INCLUDE [get training model status](../rest-api/get-training-status.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Get-training-job-status" target="_target">I ran into an issue</a>
-
-## Deploy your model
-
-Generally after training a model you would review its evaluation details and make improvements if necessary. In this quickstart, you will just deploy your model, and make it available for you to try in Language Studio, or you can call the [prediction API](https://aka.ms/ct-runtime-swagger).
-
-### Start deployment job
-
-[!INCLUDE [deploy model](../rest-api/deploy-model.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Submit-deployment-job" target="_target">I ran into an issue</a>
-
-### Get deployment job status
-
-[!INCLUDE [get deployment status](../rest-api/get-deployment-status.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Get-deployment-job-status" target="_target">I ran into an issue</a>
-
-## Make predictions with your trained model
-
-After your model is deployed, you can start using it to extract entities from your text using the [prediction API](https://aka.ms/ct-runtime-swagger). In the sample dataset you downloaded earlier you can find some test documents that you can use in this step.
-
-### Submit a custom Text Analytics for health task
-
-[!INCLUDE [submit a custom Text Analytics for health task using the REST API](../rest-api/submit-task.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Submit-custom-text-analytics-for-health-task" target="_target">I ran into an issue</a>
-
-### Get task results
-
-[!INCLUDE [get custom Text Analytics for health task results](../rest-api/get-results.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Get-task-results" target="_target">I ran into an issue</a>
-
-## Clean up resources
-
-[!INCLUDE [Delete project using the REST API](../rest-api/delete-project.md)]
-
-> [!div class="nextstepaction"]
-> <a href="https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=REST API&Pillar=Language&Product=Custom-text-analytics-for-health&Page=quickstart&Section=Clean-up-resources" target="_target">I ran into an issue</a>
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "REST APIに関するクイックスタート情報の削除"
}
```

### Explanation
この変更では、`rest-api.md`ドキュメントが完全に削除されました。この文書は、カスタムテキスト分析プロジェクトをREST APIを利用して作成、トレーニング、デプロイ、そして予測を行う手順を詳しく説明していました。内容には、Azure AI Languageリソースおよびストレージアカウントの作成、サンプルデータのアップロード、プロジェクトの作成、モデルのトレーニング、デプロイ、テスト、リソースのクリーンアップに関する具体的な手順が含まれていました。この情報が削除されることで、ユーザーはREST APIを通じてカスタムテキスト分析プロジェクトを進めるための重要なガイドラインを失い、プロジェクトの実施が難しくなる恐れがあります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/resource-creation-azure-portal.md{#item-49304b}

<details>
<summary>Diff</summary>
````diff
@@ -1,39 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-### Create a new resource from the Azure portal
-
-1. Sign in to the [Azure portal](https://portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics) to create a new Azure AI Language resource.
-
-1. In the window that appears, select **Custom text classification & custom named entity recognition** from the custom features. Select **Continue to create your resource** at the bottom of the screen. 
-
-    :::image type="content" source="../media/select-custom-feature-azure-portal.png" alt-text="A screenshot showing custom text classification & custom named entity recognition in the Azure portal." lightbox="../media/select-custom-feature-azure-portal.png":::
-
-1. Create a Language resource with following details.
-
-    |Name  | Description  |
-    |---------|---------|
-    | Subscription | Your Azure subscription. |
-    | Resource group | A resource group that will contain your resource. You can use an existing one, or create a new one. |
-    |Region | The region for your Language resource. For example, "West US 2". |
-    | Name | A name for your resource. |
-    |Pricing tier     | The pricing tier for your Language resource. You can use the Free (F0) tier to try the service.       |
-
-    > [!NOTE]
-    > If you get a message saying "*your login account is not an owner of the selected storage account's resource group*", your account needs to have an owner role assigned on the resource group before you can create a Language resource. Contact your Azure subscription owner for assistance.
-
-1. In the **Custom text classification & custom named entity recognition** section, select an existing storage account or select **New storage account**. These values are to help you get started, and not necessarily the [storage account values](/azure/storage/common/storage-account-overview) you’ll want to use in production environments. To avoid latency during building your project connect to storage accounts in the same region as your Language resource.
-
-    |Storage account value  |Recommended value  |
-    |---------|---------|
-    | Storage account name | Any name |
-    | Storage account type | Standard LRS |
-
-1. Make sure the **Responsible AI Notice** is checked. Select **Review + create** at the bottom of the page, then select **Create**.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azureポータルからのリソース作成に関する情報の削除"
}
```

### Explanation
この変更では、`resource-creation-azure-portal.md`ドキュメントが完全に削除されました。この文書には、Azureポータルを使用して新しいAzure AI Languageリソースを作成する手順が詳述されていました。具体的には、カスタムテキスト分類やカスタム命名エンティティ認識の選択、リソースの詳細（サブスクリプション、リソースグループ、リージョン、名称、価格プラン）を含む手順が含まれていました。また、ストレージアカウントの選択に関する推奨事項や、リソースを作成する前に確認すべき重要な情報も記載されていました。この情報が削除されることで、ユーザーはAzureポータルからリソースを作成する方法に関する重要なガイダンスを失い、新しいリソースの作成が困難になる恐れがあります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/cancel-training.md{#item-79e31a}

<details>
<summary>Diff</summary>
````diff
@@ -1,35 +0,0 @@
----
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Create a **POST** request by using the following URL, headers, and JSON body to cancel a training job. 
-
-### Request URL
-
-Use the following URL when creating your API request. Replace the placeholder values below with your own values. 
-
-```rest
-{Endpoint}/language/authoring/analyze-text/projects/{PROJECT-NAME}/train/jobs/{JOB-ID}/:cancel?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `EmailApp` |
-|`{JOB-ID}`       | This value is the training job ID.|  `XXXXX-XXXXX-XXXX-XX`|
-|`{API-VERSION}`     | The version of the API you're calling. The value referenced is for the latest released [model version](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data).  | `2022-05-01` |
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
- 
-After you send your API request, you'll receive a 202 response with an `Operation-Location` header used to check the status of the job.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "トレーニング取消に関するREST API情報の削除"
}
```

### Explanation
この変更では、`cancel-training.md`ドキュメントが完全に削除されました。この文書は、トレーニングジョブをキャンセルするためのREST APIのリクエストを作成する方法について説明していました。具体的には、キャンセルリクエストを送信するためのPOSTリクエストのURL、必須のヘッダー情報、各プレースホルダーの詳細な説明（エンドポイント、プロジェクト名、ジョブID、APIバージョン）が含まれていました。ユーザーはAPIリクエストを送信した後に受け取るレスポンスについても言及されており、ジョブのステータスを確認する方法が示されていました。この情報の削除により、ユーザーはトレーニングジョブを適切にキャンセルできなくなる可能性があり、APIを使用する上での重要なガイダンスを失います。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/create-project.md{#item-c32223}

<details>
<summary>Diff</summary>
````diff
@@ -1,72 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-To start creating a custom Text Analytics for health model, you need to create a project. Creating a project will let you label data, train, evaluate, improve, and deploy your models.
-
-> [!NOTE]
-> The project name is case-sensitive for all operations.
-
-Create a **PATCH** request using the following URL, headers, and JSON body to create your project.
-
-### Request URL
-
-Use the following URL to create a project. Replace the placeholder values below with your own values. 
-
-```rest
-{Endpoint}/language/authoring/analyze-text/projects/{projectName}?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `myProject` |
-|`{API-VERSION}`     | The version of the API you are calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-### Body
-
-Use the following JSON in your request. Replace the placeholder values below with your own values.
-
-```json
-{
-  "projectName": "{PROJECT-NAME}",
-  "language": "{LANGUAGE-CODE}",
-  "projectKind": "CustomHealthcare",
-  "description": "Project description",
-  "multilingual": "True",
-  "storageInputContainerName": "{CONTAINER-NAME}"
-}
-
-```
-
-|Key  |Placeholder|Value  | Example |
-|---------|---------|---------|--|
-| projectName | `{PROJECT-NAME}` | The name of your project. This value is case-sensitive. | `myProject` |
-| language | `{LANGUAGE-CODE}` |  A string specifying the language code for the documents used in your project. If your project is a multilingual project, choose the language code of the majority of the documents. See [language support](../../language-support.md) to learn more about supported language codes. |`en-us`|
-| projectKind | `CustomHealthcare` | Your project kind. | `CustomHealthcare` |
-| multilingual | `true`| A boolean value that enables you to have documents in multiple languages in your dataset and when your model is deployed you can query the model in any supported language (not necessarily ones included in your training documents). See [language support](../../language-support.md) to learn more about multilingual support.  | `true`|
-| storageInputContainerName | `{CONTAINER-NAME` | The name of your Azure storage container where you have uploaded your documents.   | `myContainer` |
-
-
-
-
-This request will return a 201 response, which means that the project is created.
-
-
-This request will return an error if:
-* The selected resource doesn't have proper permission for the storage account. 
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムプロジェクト作成に関するREST API情報の削除"
}
```

### Explanation
この変更により、`create-project.md`ドキュメントが完全に削除されました。この文書は、カスタムText Analytics for Healthモデルを作成するためのプロジェクトを作成する手順について詳しく説明していました。具体的には、プロジェクトを作成するためのPATCHリクエストのURL、必要なヘッダー、JSONボディの内容が含まれており、プレースホルダーの説明や具体的な入力例も提供されていました。また、成功時のレスポンスや、エラーが発生する可能性のある条件についても説明されていました。この情報の削除により、ユーザーはAPIを使用してプロジェクトを適切に作成する方法が分からなくなり、カスタムモデルの開発や管理が困難になる可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/delete-deployment.md{#item-3551ec}

<details>
<summary>Diff</summary>
````diff
@@ -1,36 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Create a **DELETE** request using the following URL, headers, and JSON body to delete a deployment.
-
-
-### Request URL
-
-```rest
-{Endpoint}/language/authoring/analyze-text/projects/{PROJECT-NAME}/deployments/{deploymentName}?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `myProject` |
-|`{DEPLOYMENT-NAME}`     | The name for your deployment name. This value is case-sensitive.   | `prod` |
-|`{API-VERSION}`     | The version of the API you are calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-
-Once you send your API request, you will receive a `202` response indicating success, which means your deployment has been deleted. A successful call results with an `Operation-Location` header used to check the status of the job.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デプロイメント削除に関するREST API情報の削除"
}
```

### Explanation
この変更により、`delete-deployment.md`ドキュメントが完全に削除されました。この文書は、デプロイメントを削除するためのDELETEリクエストを作成する手順を詳細に説明していました。具体的には、リクエストURL、必要なヘッダー情報、プレースホルダーの説明、および成功時のレスポンスに関する情報が含まれていました。リクエストURLには、プロジェクト名やデプロイメント名、APIバージョンを指定する必要があり、それぞれの値はケースセンシティブであることが強調されていました。削除成功時には202のレスポンスが返されることが示されており、デプロイメントの削除状況を確認するための`Operation-Location`ヘッダーの使用についても説明されていました。この情報の削除により、ユーザーはデプロイメントを適切に削除する方法が不明になり、API使用時の手順が困難になります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/delete-project.md{#item-139027}

<details>
<summary>Diff</summary>
````diff
@@ -1,31 +0,0 @@
----
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-When you no longer need your project, you can delete it with the following **DELETE** request. Replace the placeholder values with your own values.   
-
-```rest
-{Endpoint}/language/authoring/analyze-text/projects/{projectName}?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.  | `myProject` |
-|`{API-VERSION}`     | The version of the API you are calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|Ocp-Apim-Subscription-Key| The key to your resource. Used for authenticating your API requests.|
-
-
-Once you send your API request, you will receive a `202` response indicating success, which means your project has been deleted. A successful call results with an Operation-Location header used to check the status of the job.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト削除に関するREST API情報の削除"
}
```

### Explanation
この変更により、`delete-project.md`ドキュメントが完全に削除されました。この文書は、不要なプロジェクトを削除するためのDELETEリクエストを作成する手順を詳述していました。具体的には、リクエストURLの構成、プレースホルダーの説明、必要なヘッダー、そして成功時のレスポンスに関する情報が含まれていました。リクエストURLには、プロジェクト名やAPIバージョンを指定する必要があり、これらの値はすべてケースセンシティブであることが重要でした。また、APIリクエストを送信すると202のレスポンスが受け取れることが示されており、このレスポンスはプロジェクトが削除されたことを示しています。さらに、成功したリクエストには`Operation-Location`ヘッダーが含まれ、削除の進捗を確認するために使用されることが説明されていました。この情報の削除に伴い、ユーザーはプロジェクトを適切に削除する方法が不明になり、API使用時に混乱を招く可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/deploy-model.md{#item-92e68f}

<details>
<summary>Diff</summary>
````diff
@@ -1,52 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Submit a **PUT** request using the following URL, headers, and JSON body to submit a deployment job. Replace the placeholder values below with your own values. 
-
-```rest
-{Endpoint}/language/authoring/analyze-text/projects/{projectName}/deployments/{deploymentName}?api-version={API-VERSION}
-```
-
-| Placeholder |Value | Example |
-|---------|---------|---------|
-| `{ENDPOINT}` | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-| `{PROJECT-NAME}` | The name of your project. This value is case-sensitive.   | `myProject` |
-| `{DEPLOYMENT-NAME}`     | The name of your deployment. This value is case-sensitive.  | `staging` |
-|`{API-VERSION}`     | The version of the API you're calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-#### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-#### Request body
-
-Use the following JSON in the body of your request. Use the name of the model you to assign to the deployment.  
-
-```json
-{
-  "trainedModelLabel": "{MODEL-NAME}"
-}
-```
-
-|Key  |Placeholder  |Value  | Example |
-|---------|---------|-----|----|
-| trainedModelLabel | `{MODEL-NAME}` | The model name that will be assigned to your deployment. You can only assign successfully trained models. This value is case-sensitive.   | `myModel` |
-
-Once you send your API request, you’ll receive a `202` response indicating that the job was submitted correctly. In the response headers, extract the `operation-location` value. It will be formatted like this: 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/deployments/{DEPLOYMENT-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
-``` 
-
-`{JOB-ID}` is used to identify your request, since this operation is asynchronous. You can use this URL to get the deployment status.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルデプロイメントのAPI情報の削除"
}
```

### Explanation
この変更により、`deploy-model.md`ドキュメントが完全に削除されました。この文書は、モデルデプロイメントジョブを提出するためのPUTリクエストの手順を詳述していました。具体的には、リクエストURL、必要なヘッダー情報、リクエストボディに含めるJSON形式のデータ、および成功時のレスポンスに関する詳細が記載されていました。リクエストURLはプロジェクト名やデプロイメント名、APIバージョンを指定する必要があり、これらの値はすべてケースセンシティブであることが強調されていました。さらに、リクエストボディには、デプロイメントに割り当てるモデル名を指定する必要があり、成功したリクエストには202のレスポンスが返されることが示されており、その際に返される`operation-location`の値を基に非同期操作の結果を確認できることが説明されていました。この情報が削除されたことにより、ユーザーはモデルデプロイメントを適切に行う方法が不明になり、APIの利用において混乱を招く可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/export-project.md{#item-7970cf}

<details>
<summary>Diff</summary>
````diff
@@ -1,51 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Create a **POST** request using the following URL, headers, and JSON body to export your project.
-
-### Request URL
-
-Use the following URL when creating your API request. Replace the placeholder values with your own values. 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/:export?stringIndexType=Utf16CodeUnit&api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `MyProject` |
-|`{API-VERSION}`     | The version of the API you are calling. The value referenced here is the latest [model version](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) released.  | `2022-05-01` |
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-#### Body
-
-Use the following JSON in your request body specifying that you want to export all the assets.
-
-```json
-{
-  "assetsToExport": ["*"]
-}
-```
-
-Once you send your API request, you’ll receive a `202` response indicating that the job was submitted correctly. In the response headers, extract the `operation-location` value. It's formatted like this: 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/export/jobs/{JOB-ID}?api-version={API-VERSION}
-``` 
-
-`{JOB-ID}` is used to identify your request, since this operation is asynchronous. You’ll use this URL to get the export job status.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト輸出に関するAPI情報の削除"
}
```

### Explanation
この変更により、`export-project.md`ドキュメントが完全に削除されました。この文書は、プロジェクトをエクスポートするためのPOSTリクエストを作成する手順を詳細に説明していました。具体的には、リクエストURLの構成、必要なヘッダー情報、リクエストボディに含めるJSONデータの例、および成功時のレスポンスに関する情報が含まれていました。リクエストURLにはプロジェクト名やAPIバージョンを指定する必要があり、これらの値はすべてケースセンシティブであり、特定のエンドポイントに対してリクエストを行うことが強調されていました。

リクエストボディでは、エクスポートする資産を指定するためにJSON形式で"assetsToExport"フィールドの設定が求められました。また、APIリクエストを送信すると202のレスポンスが返され、これはジョブが正しく提出されたことを示します。レスポンスヘッダーには`operation-location`の値が含まれ、それを使用して非同期のエクスポートジョブの状態を確認するためのURLが提供されていました。この情報の削除に伴い、ユーザーはプロジェクトを適切にエクスポートする方法が不明になり、API利用時に混乱を招く可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/get-deployment-status.md{#item-7b9bdc}

<details>
<summary>Diff</summary>
````diff
@@ -1,46 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Use the following **GET** request to query the status of the deployment job. You can use the URL you received from the previous step, or replace the placeholder values below with your own values. 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/deployments/{DEPLOYMENT-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
-```
-
-| Placeholder |Value | Example |
-|---------|---------|---------|
-| `{ENDPOINT}` | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-| `{PROJECT-NAME}` | The name of your project. This value is case-sensitive.   | `myProject` |
-| `{DEPLOYMENT-NAME}`     | The name of your deployment. This value is case-sensitive.  | `staging` |
-|`{JOB-ID}`     | The ID for locating your model's training status. This is in the `location` header value you received in the previous step.  | `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx` |
-|`{API-VERSION}`     | The version of the API you're calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-#### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-
-### Response Body
-
-You'll receive the following request when you send the request. Keep polling this endpoint until the **status** parameter changes to "succeeded". You should get a `200` code to indicate the success of the request. 
-
-```json
-{
-    "jobId":"{JOB-ID}",
-    "createdDateTime":"{CREATED-TIME}",
-    "lastUpdatedDateTime":"{UPDATED-TIME}",
-    "expirationDateTime":"{EXPIRATION-TIME}",
-    "status":"running"
-}
-```
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デプロイメントステータス取得に関するAPI情報の削除"
}
```

### Explanation
この変更により、`get-deployment-status.md`ドキュメントが完全に削除されました。この文書は、デプロイメントジョブのステータスを確認するためのGETリクエストを送信する方法を詳しく説明していました。具体的には、リクエストURLの構造、必要なプレースホルダの情報、認証に必要なヘッダー、および成功時のレスポンスボディの内容が詳述されていました。

リクエストURLには、プロジェクト名、デプロイメント名、ジョブID、APIバージョンが含まれる必要があり、これらのプレースホルダは特定の値に置き換えられる必要がありました。また、APIへのリクエスト認証に必要なヘッダー情報として`Ocp-Apim-Subscription-Key`が記載されていました。

さらに、リクエストを送信すると、ジョブの詳細を含むJSON形式のレスポンスが返されることが説明されており、`status`パラメータが"成功"に変わるまでこのエンドポイントをポーリングし続ける必要があることも指摘されていました。この情報の削除により、ユーザーはデプロイメントのステータスを確認する手続きを理解できなくなり、API利用時に困惑する可能性があります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/get-export-status.md{#item-467cd8}

<details>
<summary>Diff</summary>
````diff
@@ -1,64 +0,0 @@
----
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Use the following **GET** request to get the status of exporting your project assets. Replace the placeholder values below with your own values. 
-
-### Request URL
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/export/jobs/{JOB-ID}?api-version={API-VERSION}
-``` 
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name of your project. This value is case-sensitive.   | `myProject` |
-|`{JOB-ID}`     | The ID for locating your model's training status. This is in the `location` header value you received in the previous step.  | `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx` |
-|`{API-VERSION}`     | The version of the API you are calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-### Response body
-
-```json
-{
-  "resultUrl": "{RESULT-URL}",
-  "jobId": "string",
-  "createdDateTime": "2021-10-19T23:24:41.572Z",
-  "lastUpdatedDateTime": "2021-10-19T23:24:41.572Z",
-  "expirationDateTime": "2021-10-19T23:24:41.572Z",
-  "status": "unknown",
-  "errors": [
-    {
-      "code": "unknown",
-      "message": "string"
-    }
-  ]
-}
-```
-
-Use the URL from the `resultUrl` key in the body to view the exported assets from this job.
-
-### Get export results
-
-Submit a **GET** request using the `{RESULT-URL}` you received from the previous step to view the results of the export job.
-
-#### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクトエクスポートステータス取得に関するAPI情報の削除"
}
```

### Explanation
この変更により、`get-export-status.md`ドキュメントが削除されました。この文書は、プロジェクト資産のエクスポート状況を取得するためのGETリクエストを送信する手順を詳細に説明していました。具体的には、リクエストURLの構成、必要なプレースホルダ情報、認証に必要なヘッダー、エクスポート状況を示すレスポンスボディなどが含まれていました。

リクエストURLには、プロジェクト名、ジョブID、APIバージョンが含まれる必要があり、これらはユーザーが持つ特定の値に置き換える必要があります。認証には`Ocp-Apim-Subscription-Key`ヘッダーが必要であることも明記されていました。

レスポンスボディは、エクスポートの結果に関する情報を含むJSON形式であり、`resultUrl`キ―を使用してエクスポートされた資産を表示するためのURLが提供されていました。また、エクスポートジョブの結果を参照するためのGETリクエストの方法も説明されていました。この情報の削除により、ユーザーはプロジェクト資産のエクスポート状況を確認する手段を失い、APIの利用において混乱を招く恐れがあります。変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/get-import-status.md{#item-2dec2c}

<details>
<summary>Diff</summary>
````diff
@@ -1,31 +0,0 @@
----
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Use the following **GET** request to get the status of your importing your project. Replace the placeholder values below with your own values. 
-
-### Request URL
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/import/jobs/{JOB-ID}?api-version={API-VERSION}
-``` 
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name of your project. This value is case-sensitive.   | `myProject` |
-|`{JOB-ID}`     | The ID for locating your model's training status. This value is in the `location` header value you received in the previous step.  | `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx` |
-|`{API-VERSION}`     | The version of the API you are calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-#### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクトインポートステータス取得に関するAPI情報の削除"
}
```

### Explanation
この変更により、`get-import-status.md`ドキュメントが削除されました。この文書は、プロジェクトのインポート状況を取得するためのGETリクエストを送信する手続きを詳しく説明していました。具体的には、リクエストURLの構造や必要なプレースホルダ、認証に必要なヘッダーについての情報が含まれていました。

リクエストURLには、プロジェクト名、ジョブID、APIバージョンが含まれる必要があり、これらはユーザーが入力すべき特定の値に置き換えられなければなりませんでした。また、APIリクエストの認証には`Ocp-Apim-Subscription-Key`というヘッダーが必要であることも強調されていました。

このドキュメントが削除されたことにより、ユーザーはプロジェクトのインポート状況を確認するための手段を持たなくなり、APIの利用において混乱を招く可能性があります。この変更の詳細は、GitHubのリポジトリで確認することができます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/get-project-details.md{#item-9ec8e1}

<details>
<summary>Diff</summary>
````diff
@@ -1,45 +0,0 @@
----
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Use the following **GET** request to get your project details. Replace the placeholder values with your own values. 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.  | `myProject` |
-|`{API-VERSION}`     | The version of the API you're calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-#### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-#### Response body
-
-```json
-    {
-        "createdDateTime": "2021-10-19T23:24:41.572Z",
-        "lastModifiedDateTime": "2021-10-19T23:24:41.572Z",
-        "lastTrainedDateTime": "2021-10-19T23:24:41.572Z",
-        "lastDeployedDateTime": "2021-10-19T23:24:41.572Z",
-        "projectKind": "CustomEntityRecognition",
-        "storageInputContainerName": "{CONTAINER-NAME}",
-        "projectName": "{PROJECT-NAME}",
-        "multilingual": false,
-        "description": "Project description",
-        "language": "{LANGUAGE-CODE}"
-    }
-```
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト詳細取得に関するAPI情報の削除"
}
```

### Explanation
この変更により、`get-project-details.md`ドキュメントが削除されました。この文書は、プロジェクトの詳細を取得するためのGETリクエストの手順を説明していました。具体的には、リクエストURLの構成や必要なプレースホルダ、認証に必要なヘッダー、レスポンスボディの構造についての詳細が含まれていました。

リクエストURLには、プロジェクト名とAPIバージョンが含まれ、これらはユーザーが自身の値に置き換える必要がありました。APIアクセスには`Ocp-Apim-Subscription-Key`というヘッダーが必要で、リクエストを認証するために必要でした。

レスポンスボディは、プロジェクトの作成日時、最終更新日時、トレーニング日時、デプロイ日時などの情報を含むJSON形式であり、プロジェクトの状態を把握するために重要なデータを提供していました。このドキュメントが削除されたことにより、ユーザーはプロジェクトの詳細を確認するための情報を失い、API使用に関して混乱を生じる可能性があります。この変更の詳細は、GitHubのリポジトリで確認可能です。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/get-results.md{#item-7a7625}

<details>
<summary>Diff</summary>
````diff
@@ -1,289 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-
-Use the following **GET** request to query the status/results of the custom entity recognition task. 
-
-```rest
-{ENDPOINT}/language/analyze-text/jobs/{JOB-ID}?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{API-VERSION}`     | The version of the API you're calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-#### Headers
-
-|Key|Value|
-|--|--|
-|Ocp-Apim-Subscription-Key| Your key that provides access to this API.|
-
-### Response Body
-
-The response is a JSON document with the following parameters
-
-```json
-{
-	"createdDateTime": "2021-05-19T14:32:25.578Z",
-	"displayName": "MyJobName",
-	"expirationDateTime": "2021-05-19T14:32:25.578Z",
-	"jobId": "xxxx-xxxx-xxxxx-xxxxx",
-	"lastUpdateDateTime": "2021-05-19T14:32:25.578Z",
-	"status": "succeeded",
-	"tasks": {
-		"completed": 1,
-		"failed": 0,
-		"inProgress": 0,
-		"total": 1,
-		"items": [
-			{
-				"kind": "CustomHealthcareLROResults",
-				"taskName": "Custom Text Analytics for Health Test",
-				"lastUpdateDateTime": "2020-10-01T15:01:03Z",
-				"status": "succeeded",
-				"results": {
-					"documents": [
-						{
-							"entities": [
-								{
-									"entityComponentInformation": [
-										{
-											"entityComponentKind": "learnedComponent"
-										}
-									],
-									"offset": 0,
-									"length": 11,
-									"text": "first entity",
-									"category": "Entity1",
-									"confidenceScore": 0.98
-								},
-								{
-									"entityComponentInformation": [
-										{
-											"entityComponentKind": "listComponent"
-										}
-									],
-									"offset": 0,
-									"length": 11,
-									"text": "first entity",
-									"category": "Entity1.Dictionary",
-									"confidenceScore": 1.0
-								},
-								{
-									"entityComponentInformation": [
-										{
-											"entityComponentKind": "learnedComponent"
-										}
-									],
-									"offset": 16,
-									"length": 9,
-									"text": "entity two",
-									"category": "Entity2",
-									"confidenceScore": 1.0
-								},
-								{
-									"entityComponentInformation": [
-										{
-											"entityComponentKind": "prebuiltComponent"
-										}
-									],
-									"offset": 37,
-									"length": 9,
-									"text": "ibuprofen",
-									"category": "MedicationName",
-									"confidenceScore": 1,
-									"assertion": {
-										"certainty": "negative"
-									},
-									"name": "ibuprofen",
-									"links": [
-										{
-											"dataSource": "UMLS",
-											"id": "C0020740"
-										},
-										{
-											"dataSource": "AOD",
-											"id": "0000019879"
-										},
-										{
-											"dataSource": "ATC",
-											"id": "M01AE01"
-										},
-										{
-											"dataSource": "CCPSS",
-											"id": "0046165"
-										},
-										{
-											"dataSource": "CHV",
-											"id": "0000006519"
-										},
-										{
-											"dataSource": "CSP",
-											"id": "2270-2077"
-										},
-										{
-											"dataSource": "DRUGBANK",
-											"id": "DB01050"
-										},
-										{
-											"dataSource": "GS",
-											"id": "1611"
-										},
-										{
-											"dataSource": "LCH_NW",
-											"id": "sh97005926"
-										},
-										{
-											"dataSource": "LNC",
-											"id": "LP16165-0"
-										},
-										{
-											"dataSource": "MEDCIN",
-											"id": "40458"
-										},
-										{
-											"dataSource": "MMSL",
-											"id": "d00015"
-										},
-										{
-											"dataSource": "MSH",
-											"id": "D007052"
-										},
-										{
-											"dataSource": "MTHSPL",
-											"id": "WK2XYI10QM"
-										},
-										{
-											"dataSource": "NCI",
-											"id": "C561"
-										},
-										{
-											"dataSource": "NCI_CTRP",
-											"id": "C561"
-										},
-										{
-											"dataSource": "NCI_DCP",
-											"id": "00803"
-										},
-										{
-											"dataSource": "NCI_DTP",
-											"id": "NSC0256857"
-										},
-										{
-											"dataSource": "NCI_FDA",
-											"id": "WK2XYI10QM"
-										},
-										{
-											"dataSource": "NCI_NCI-GLOSS",
-											"id": "CDR0000613511"
-										},
-										{
-											"dataSource": "NDDF",
-											"id": "002377"
-										},
-										{
-											"dataSource": "PDQ",
-											"id": "CDR0000040475"
-										},
-										{
-											"dataSource": "RCD",
-											"id": "x02MO"
-										},
-										{
-											"dataSource": "RXNORM",
-											"id": "5640"
-										},
-										{
-											"dataSource": "SNM",
-											"id": "E-7772"
-										},
-										{
-											"dataSource": "SNMI",
-											"id": "C-603C0"
-										},
-										{
-											"dataSource": "SNOMEDCT_US",
-											"id": "387207008"
-										},
-										{
-											"dataSource": "USP",
-											"id": "m39860"
-										},
-										{
-											"dataSource": "USPMG",
-											"id": "MTHU000060"
-										},
-										{
-											"dataSource": "VANDF",
-											"id": "4017840"
-										}
-									]
-								},
-								{
-									"entityComponentInformation": [
-										{
-											"entityComponentKind": "prebuiltComponent"
-										}
-									],
-									"offset": 30,
-									"length": 6,
-									"text": "100 mg",
-									"category": "Dosage",
-									"confidenceScore": 0.98
-								}
-							],
-							"relations": [
-								{
-									"confidenceScore": 1,
-									"relationType": "DosageOfMedication",
-									"entities": [
-										{
-											"ref": "#/documents/0/entities/1",
-											"role": "Dosage"
-										},
-										{
-											"ref": "#/documents/0/entities/0",
-											"role": "Medication"
-										}
-									]
-								}
-							],
-							"id": "1",
-							"warnings": []
-						}
-					],
-					"errors": [],
-					"modelVersion": "2020-04-01"
-				}
-			}
-		]
-	}
-}
-
-```
-
-|Key|Sample Value|Description|
-|--|--|--|
-|entities|[]|An array containing all the extracted entities.|
-|entityComponentKind|`prebuiltComponent`| A variable that indicates which component returned the specific entity. Possible values: `prebuiltComponent`, `learnedComponent`, `listComponent` |
-|offset|`0`| A number denoting the starting point of the extracted entity by indexing over the characters|
-|length| `10`| A number denoting the length of the extracted entity in number of characters.|
-|text|`first entity`| The text that was extracted for a specific entity.|
-|category|`MedicationName`| The name of the entity type or category corresponding to the extracted text.|
-|confidenceScore|`0.9`| A number denoting the model's certainty level of the extracted entity ranging from 0 to 1 with higher number denoting higher certainty.|
-|assertion|`certainty`| [Assertions](../../../text-analytics-for-health/concepts/assertion-detection.md) associated with the extracted entity. Assertions are only supported for prebuilt [Text Analytics for health entities](../../../text-analytics-for-health/overview.md?tabs=entity-linking#text-analytics-for-health-features).|
-|name|`Ibuprofen`| The normalized name for the [entity linking](../../../text-analytics-for-health/overview.md?tabs=entity-linking#text-analytics-for-health-features) associated with the extracted entity. Entity linking is only supported for prebuilt [Text Analytics for health entities](../../../text-analytics-for-health/concepts/health-entity-categories.md).|
-|links| [] | An array containing all the results from the [entity linking](../../../text-analytics-for-health/overview.md?tabs=entity-linking#text-analytics-for-health-features) associated with the extracted entity. Entity linking is only supported for prebuilt [Text Analytics for health entities](../../../text-analytics-for-health/concepts/health-entity-categories.md).|
-|dataSource| `UMLS` | The reference standard resulting from the [entity linking](../../../text-analytics-for-health/overview.md?tabs=entity-linking#text-analytics-for-health-features) associated with the extracted entity. Entity linking is only supported for prebuilt [Text Analytics for health entities](../../../text-analytics-for-health/concepts/health-entity-categories.md).|
-|ID| `C0020740` | The reference code resulting from the [entity linking](../../../text-analytics-for-health/overview.md?tabs=entity-linking#text-analytics-for-health-features) associated with the extracted entity belonging to the extracted data source. Entity linking is only supported for prebuilt [Text Analytics for health entities](../../../text-analytics-for-health/concepts/health-entity-categories.md).|
-|relations| [] | Array containing all the extracted relationships. [Relationship extraction](../../../text-analytics-for-health/concepts/relation-extraction.md) is only supported for prebuilt [Text Analytics for health entities](../../../text-analytics-for-health/concepts/health-entity-categories.md).|
-|relationType| `DosageOfMedication` | The category of the extracted [relationship](../../../text-analytics-for-health/concepts/relation-extraction.md). Relationship extraction is only supported for prebuilt [Text Analytics for health entities](../../../text-analytics-for-health/concepts/health-entity-categories.md).|
-|entities| `"Dosage", "Medication"` | The entities associated with the extracted relationship. Relationship extraction is only supported for prebuilt [Text Analytics for health entities](../../../text-analytics-for-health/concepts/health-entity-categories.md).|
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムエンティティ認識タスクの結果取得に関するAPI情報の削除"
}
```

### Explanation
この変更により、`get-results.md`ドキュメントが削除されました。この文書は、カスタムエンティティ認識タスクの結果を取得するためのGETリクエストの方法を説明していました。具体的には、APIのエンドポイント、プレースホルダ、認証に必要なヘッダー、そしてレスポンスボディの構造についての情報が含まれていました。

リクエストには、ジョブIDとAPIバージョンを指定する必要があり、ユーザーはそれぞれの値を自分の環境に合わせて置き換えなければなりませんでした。レスポンスボディは、ジョブの作成日時、状態、タスクの詳細、抽出されたエンティティに関する情報を含むJSON形式のデータでした。この情報は、処理状況を把握し、解析結果を確認するために重要でした。

このドキュメントが削除されたことにより、ユーザーはカスタムエンティティ認識タスクの結果を確認する手段を失い、APIの利用において混乱を招く可能性があります。この変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/get-training-status.md{#item-787844}

<details>
<summary>Diff</summary>
````diff
@@ -1,60 +0,0 @@
----
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Use the following **GET** request to get the status of your model's training progress. Replace the placeholder values below with your own values. 
-
-### Request URL
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/train/jobs/{JOB-ID}?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name of your project. This value is case-sensitive.   | `myProject` |
-|`{JOB-ID}`     | The ID for locating your model's training status. This value is in the `location` header value you received in the previous step.  | `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx` |
-|`{API-VERSION}`     | The version of the API you're calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-#### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-#### Response Body
-
-After sending the request, you will get the following response. 
-
-```json
-{
-  "result": {
-    "modelLabel": "{MODEL-NAME}",
-    "trainingConfigVersion": "{CONFIG-VERSION}",
-    "estimatedEndDateTime": "2022-04-18T15:47:58.8190649Z",
-    "trainingStatus": {
-      "percentComplete": 3,
-      "startDateTime": "2022-04-18T15:45:06.8190649Z",
-      "status": "running"
-    },
-    "evaluationStatus": {
-      "percentComplete": 0,
-      "status": "notStarted"
-    }
-  },
-  "jobId": "{JOB-ID}",
-  "createdDateTime": "2022-04-18T15:44:44Z",
-  "lastUpdatedDateTime": "2022-04-18T15:45:48Z",
-  "expirationDateTime": "2022-04-25T15:44:44Z",
-  "status": "running"
-}
-
-```
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルのトレーニング進行状況取得に関するAPI情報の削除"
}
```

### Explanation
この変更により、`get-training-status.md`ドキュメントが削除されました。この文書は、モデルのトレーニング進行状況を取得するためのGETリクエストについて説明しており、具体的にはリクエストURL、必要なプレースホルダ、認証に必要なヘッダー、およびレスポンスボディの構造についての情報が含まれていました。

リクエストURLには、エンドポイント、プロジェクト名、ジョブID、およびAPIバージョンが必要であり、これらの情報をユーザーが自分の環境に合わせて置き換えなければなりませんでした。レスポンスボディでは、トレーニングの進行状況を示すために、パーセンテージやトレーニングの開始日時、進行中のステータスが提供されていました。この情報は、ユーザーがトレーニングの進行を把握し、今後のアクションを計画する際に重要でした。

このドキュメントが削除されたことで、ユーザーはモデルのトレーニング状況を確認する手段を失い、APIの利用において混乱を招く可能性があります。この変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/import-project.md{#item-6fa50e}

<details>
<summary>Diff</summary>
````diff
@@ -1,185 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Submit a **POST** request using the following URL, headers, and JSON body to import your labels file. Make sure that your labels file follow the [accepted format](../../concepts/data-formats.md).
-
-If a project with the same name already exists, the data of that project is replaced.
-
-```rest
-{Endpoint}/language/authoring/analyze-text/projects/{projectName}/:import?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `myProject` |
-|`{API-VERSION}`     | The version of the API you are calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-
-### Body
-
-Use the following JSON in your request. Replace the placeholder values below with your own values. 
-
-```json
-{
-	"projectFileVersion": "{API-VERSION}",
-	"stringIndexType": "Utf16CodeUnit",
-	"metadata": {
-		"projectName": "{PROJECT-NAME}",
-		"projectKind": "CustomHealthcare",
-		"description": "Trying out custom Text Analytics for health",
-		"language": "{LANGUAGE-CODE}",
-		"multilingual": true,
-		"storageInputContainerName": "{CONTAINER-NAME}",
-		"settings": {}
-	},
-	"assets": {
-		"projectKind": "CustomHealthcare",
-		"entities": [
-			{
-				"category": "Entity1",
-				"compositionSetting": "{COMPOSITION-SETTING}",
-				"list": {
-					"sublists": [
-						{
-							"listKey": "One",
-							"synonyms": [
-								{
-									"language": "en",
-									"values": [
-										"EntityNumberOne",
-										"FirstEntity"
-									]
-								}
-							]
-						}
-					]
-				}
-			},
-			{
-				"category": "Entity2"
-			},
-			{
-				"category": "MedicationName",
-				"list": {
-					"sublists": [
-						{
-							"listKey": "research drugs",
-							"synonyms": [
-								{
-									"language": "en",
-									"values": [
-										"rdrug a",
-										"rdrug b"
-									]
-								}
-							]
-
-						}
-					]
-				}
-				"prebuilts": "MedicationName"
-			}
-		],
-		"documents": [
-			{
-				"location": "{DOCUMENT-NAME}",
-				"language": "{LANGUAGE-CODE}",
-				"dataset": "{DATASET}",
-				"entities": [
-					{
-						"regionOffset": 0,
-						"regionLength": 500,
-						"labels": [
-							{
-								"category": "Entity1",
-								"offset": 25,
-								"length": 10
-							},
-							{
-								"category": "Entity2",
-								"offset": 120,
-								"length": 8
-							}
-						]
-					}
-				]
-			},
-			{
-				"location": "{DOCUMENT-NAME}",
-				"language": "{LANGUAGE-CODE}",
-				"dataset": "{DATASET}",
-				"entities": [
-					{
-						"regionOffset": 0,
-						"regionLength": 100,
-						"labels": [
-							{
-								"category": "Entity2",
-								"offset": 20,
-								"length": 5
-							}
-						]
-					}
-				]
-			}
-		]
-	}
-}
-
-```
-
-|Key  |Placeholder  |Value  | Example |
-|---------|---------|----------|--|
-| `multilingual` | `true`| A boolean value that enables you to have documents in multiple languages in your dataset and when your model is deployed you can query the model in any supported language (not necessarily included in your training documents). See [language support](../../language-support.md) to learn more about multilingual support. | `true`|
-|`projectName`|`{PROJECT-NAME}`|Project name|`myproject`|
-| `storageInputContainerName` |`{CONTAINER-NAME}`|Container name|`mycontainer`|
-| `entities` | | Array containing all the entity types you have in the project. These are the entity types that will be extracted from your documents into.|  |
-| `category` | | The name of the entity type, which can be user defined for new entity definitions, or predefined for prebuilt entities. |  |
-|`compositionSetting`|`{COMPOSITION-SETTING}`|Rule that defines how to manage multiple components in your entity. Options are `combineComponents` or `separateComponents`. |`combineComponents`|
-| `list` | | Array containing all the sublists you have in the project for a specific entity. Lists can be added to prebuilt entities or new entities with learned components.|  |
-|`sublists`|`[]`|Array containing sublists. Each sublist is a key and its associated values.|`[]`|
-| `listKey`| `One` | A normalized value for the list of synonyms to map back to in prediction. | `One` |
-|`synonyms`|`[]`|Array containing all the synonyms|synonym|
-| `language` | `{LANGUAGE-CODE}` |  A string specifying the language code for the synonym in your sublist. If your project is a multilingual project and you want to support your list of synonyms for all the languages in your project, you have to explicitly add your synonyms to each language. See [Language support](../../language-support.md) for more information about supported language codes. |`en`|
-| `values`| `"EntityNumberone"`, `"FirstEntity"`  | A list of comma separated strings that will be matched exactly for extraction and map to the list key. | `"EntityNumberone"`, `"FirstEntity"` |
-| `prebuilts` | `MedicationName` | The name of the prebuilt component populating the prebuilt entity. [Prebuilt entities](../../../text-analytics-for-health/concepts/health-entity-categories.md) are automatically loaded into your project by default but you can extend them with list components in your labels file.  | `MedicationName` |
-| `documents` | | Array containing all the documents in your project and list of the entities labeled within each document. | [] |
-| `location` | `{DOCUMENT-NAME}` |  The location of the documents in the storage container. Since all the documents are in the root of the container this should be the document name.|`doc1.txt`|
-| `dataset` | `{DATASET}` |  The [test set](../../how-to/train-model.md#data-splitting) to which this file will go to when split before training. Possible values for this field are `Train` and `Test`.      |`Train`|
-| `regionOffset` |  |  The inclusive character position of the start of the text.      |`0`|
-| `regionLength` |  |  The length of the bounding box in terms of UTF16 characters. Training only considers the data in this region.      |`500`|
-| `category` |  |  The type of entity associated with the span of text specified. | `Entity1`|
-| `offset` |  |  The start position for the entity text. | `25`|
-| `length` |  |  The length of the entity in terms of UTF16 characters. | `20`|
-| `language` | `{LANGUAGE-CODE}` |  A string specifying the language code for the document used in your project. If your project is a multilingual project, choose the language code of the majority of the documents. See [Language support](../../language-support.md) for more information about supported language codes. |`en`|
-
-Once you send your API request, you’ll receive a `202` response indicating that the job was submitted correctly. In the response headers, extract the `operation-location` value. It will be formatted like this: 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/import/jobs/{JOB-ID}?api-version={API-VERSION}
-``` 
-
-`{JOB-ID}` is used to identify your request, since this operation is asynchronous. You’ll use this URL to get the import job status.  
-
-Possible error scenarios for this request:
-
-* The selected resource doesn't have [proper permissions](../../how-to/create-project.md#using-a-pre-existing-language-resource) for the storage account.
-* The `storageInputContainerName` specified doesn't exist.
-* Invalid language code is used, or if the language code type isn't string.
-* `multilingual` value is a string and not a boolean.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ラベルファイルのインポートに関するAPI情報の削除"
}
```

### Explanation
この変更により、`import-project.md`ドキュメントが削除されました。この文書は、ラベルファイルをインポートするためのPOSTリクエストについて説明しており、具体的には要求URL、必要なヘッダー、リクエストボディのJSON構造、およびレスポンスの処理方法が含まれていました。

リクエストURLにはエンドポイント、プロジェクト名、APIバージョンが必要で、ユーザーはそれに応じて値を置き換えることが求められました。ヘッダーには認証に必要な情報が含まれており、リクエストボディではインポートするデータの形式や内容（プロジェクト設定やエンティティに関する詳細）が明示されていました。

ドキュメントが削除された結果、ユーザーはラベルファイルをインポートする手段を失い、APIの利用において重大な影響を受ける可能性があります。具体的には、プロジェクトにラベルを追加したり、既存のデータを更新したりすることができなくなります。この変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/model-evaluation.md{#item-65d73e}

<details>
<summary>Diff</summary>
````diff
@@ -1,133 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-
-
-Submit a **GET** request using the following URL, headers, and JSON body to get trained model evaluation summary.
-
-
-### Request URL
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/models/{trainedModelLabel}/evaluation/summary-result?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `myProject` |
-|`{trainedModelLabel}`     | The name for your trained model. This value is case-sensitive.   | `Model1` |
-|`{API-VERSION}`     | The version of the API you're calling. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-### Response Body
-
-Once you send the request, you'll get the following response.
-
-```json
-{
-  "projectKind": "CustomHealthcare",
-  "customEntityRecognitionEvaluation": {
-    "confusionMatrix": {
-      "additionalProp1": {
-        "additionalProp1": {
-          "normalizedValue": 0,
-          "rawValue": 0
-        },
-        "additionalProp2": {
-          "normalizedValue": 0,
-          "rawValue": 0
-        },
-        "additionalProp3": {
-          "normalizedValue": 0,
-          "rawValue": 0
-        }
-      },
-      "additionalProp2": {
-        "additionalProp1": {
-          "normalizedValue": 0,
-          "rawValue": 0
-        },
-        "additionalProp2": {
-          "normalizedValue": 0,
-          "rawValue": 0
-        },
-        "additionalProp3": {
-          "normalizedValue": 0,
-          "rawValue": 0
-        }
-      },
-      "additionalProp3": {
-        "additionalProp1": {
-          "normalizedValue": 0,
-          "rawValue": 0
-        },
-        "additionalProp2": {
-          "normalizedValue": 0,
-          "rawValue": 0
-        },
-        "additionalProp3": {
-          "normalizedValue": 0,
-          "rawValue": 0
-        }
-      }
-    },
-    "entities": {
-      "additionalProp1": {
-        "f1": 0,
-        "precision": 0,
-        "recall": 0,
-        "truePositivesCount": 0,
-        "trueNegativesCount": 0,
-        "falsePositivesCount": 0,
-        "falseNegativesCount": 0
-      },
-      "additionalProp2": {
-        "f1": 0,
-        "precision": 0,
-        "recall": 0,
-        "truePositivesCount": 0,
-        "trueNegativesCount": 0,
-        "falsePositivesCount": 0,
-        "falseNegativesCount": 0
-      },
-      "additionalProp3": {
-        "f1": 0,
-        "precision": 0,
-        "recall": 0,
-        "truePositivesCount": 0,
-        "trueNegativesCount": 0,
-        "falsePositivesCount": 0,
-        "falseNegativesCount": 0
-      }
-    },
-    "microF1": 0,
-    "microPrecision": 0,
-    "microRecall": 0,
-    "macroF1": 0,
-    "macroPrecision": 0,
-    "macroRecall": 0
-  },
-  "evaluationOptions": {
-    "kind": "percentage",
-    "trainingSplitPercentage": 0,
-    "testingSplitPercentage": 0
-  }
-}
-
-```
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "トレーニング済みモデルの評価に関するAPI情報の削除"
}
```

### Explanation
この変更により、`model-evaluation.md`ドキュメントが削除されました。この文書は、トレーニング済みモデルの評価要約を取得するためのGETリクエストについての詳細を提供していました。具体的には、リクエストURL、必要なヘッダー、レスポンスボディの構造など、評価結果を取得するために必要な情報が含まれていました。

リクエストURLでは、エンドポイント、プロジェクト名、トレーニングモデルのラベル、APIバージョンを指定する必要があり、レスポンスボディには混同行列やエンティティの評価指標（f1スコア、精度、再現率など）が含まれていました。これにより、ユーザーはモデルの性能を把握し、必要に応じて調整を行うことができました。

このドキュメントの削除は、ユーザーにとって非常に影響が大きく、トレーニング済みモデルの評価情報を取得する手段が失われることになります。これにより、ユーザーは自己のモデルのパフォーマンスを確認することができなくなり、業務に支障をきたす可能性があります。この変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/project-details.md{#item-443b56}

<details>
<summary>Diff</summary>
````diff
@@ -1,57 +0,0 @@
----
-titleSuffix: Azure AI services
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Use the following **GET** request to get your project details. Replace the placeholder values below with your own values. 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.  | `myProject` |
-|`{API-VERSION}`     | The version of the API you are calling. See [Model lifecycle](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) to learn more about other available API versions.  | `2022-05-01` |
-
-#### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-#### Response body
-
-```json
-    {
-        "createdDateTime": "2021-10-19T23:24:41.572Z",
-        "lastModifiedDateTime": "2021-10-19T23:24:41.572Z",
-        "lastTrainedDateTime": "2021-10-19T23:24:41.572Z",
-        "lastDeployedDateTime": "2021-10-19T23:24:41.572Z",
-        "projectKind": "CustomHealthcare",
-        "storageInputContainerName": "{CONTAINER-NAME}",
-        "projectName": "{PROJECT-NAME}",
-        "multilingual": false,
-        "description": "Project description",
-        "language": "{LANGUAGE-CODE}"
-    }
-```
-
-|Value | Placeholder  | Description | Example |
-|---------|---------|---------|---------|
-| `projectKind` | `CustomHealthcare` | Your project kind. | `CustomHealthcare` |
-| `storageInputContainerName` | `{CONTAINER-NAME}` | The name of your Azure storage container where you have uploaded your documents.   | `myContainer` |
-| `projectName` | `{PROJECT-NAME}` | The name of your project. This value is case-sensitive. | `myProject` |
-| `multilingual` | `true`| A boolean value that enables you to have documents in multiple languages in your dataset and when your model is deployed you can query the model in any supported language (not necessarily ones included in your training documents). For more information about multilingual support, see [Language support](../../language-support.md). | `true`|
-| `language` | `{LANGUAGE-CODE}` |  A string specifying the language code for the documents used in your project. If your project is a multilingual project, choose the language code of the majority of the documents. |`en`|
-
-Once you send your API request, you will receive a `200` response indicating success and JSON response body with your project details.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト詳細に関するAPI情報の削除"
}
```

### Explanation
この変更により、`project-details.md`ドキュメントが削除されました。この文書は、プロジェクトの詳細を取得するためのGETリクエストについての情報を提供していました。具体的には、リクエストURL、必要なヘッダー、およびレスポンスボディの構造が記載されており、ユーザーがプロジェクトのメタデータを取得するための具体的な指示が含まれていました。

リクエストURLにはエンドポイント、プロジェクト名、APIバージョンを指定する必要があり、レスポンスボディには作成日時、最終修正日時、プロジェクト名、ストレージコンテナ名、マルチリンガル設定など重要な情報が含まれていました。これにより、ユーザーは自分のプロジェクトの current 状態を把握できるようになっていました。

このドキュメントの削除は、ユーザーにとって重要な情報源を失うことを意味し、プロジェクトの詳細を取得する手段がなくなるため、業務に支障をきたす可能性があります。この変更の詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/submit-task.md{#item-393d79}

<details>
<summary>Diff</summary>
````diff
@@ -1,86 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Use this **POST** request to start a Custom Text Analytics for health extraction task.
-
-```rest
-{ENDPOINT}/language/analyze-text/jobs?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{API-VERSION}`     | The version of the API you are calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md) to learn more about other available API versions.  | `2022-05-01` |
-
-#### Headers
-
-|Key|Value|
-|--|--|
-|Ocp-Apim-Subscription-Key| Your key that provides access to this API.|
-
-#### Body
-
-```json
-{
-  "displayName": "Extracting entities",
-  "analysisInput": {
-    "documents": [
-      {
-        "id": "1",
-        "language": "{LANGUAGE-CODE}",
-        "text": "Text1"
-      },
-      {
-        "id": "2",
-        "language": "{LANGUAGE-CODE}",
-        "text": "Text2"
-      }
-    ]
-  },
-  "tasks": [
-     {
-      "kind": "CustomHealthcare",
-      "taskName": "Custom TextAnalytics for Health Test",
-      "parameters": {
-        "projectName": "{PROJECT-NAME}",
-        "deploymentName": "{DEPLOYMENT-NAME}"
-      }
-    }
-  ]
-}
-```
-
-
-
-|Key  |Placeholder  |Value  | Example |
-|---------|---------|----------|--|
-| `displayName` | `{JOB-NAME}` | Your job name. | `MyJobName` |
-| `documents` | [{},{}] | List of documents to run tasks on. | `[{},{}]` |
-| `id` | `{DOC-ID}` | Document name or ID. | `doc1`|
-| `language` | `{LANGUAGE-CODE}` |  A string specifying the language code for the document. If this key isn't specified, the service will assume the default language of the project that was selected during project creation. See [language support](../../language-support.md) for a list of supported language codes. |`en-us`|
-| `text` | `{DOC-TEXT}` | Document task to run the tasks on. | `Lorem ipsum dolor sit amet` |
-|`tasks`| | List of tasks we want to perform.|`[]`|
-| `taskName`|`Custom Text Analytics for Health Test`|The task name|`Custom Text Analytics for Health Test`|
-| `kind`|`CustomHealthcare`|The project or task kind we are trying to perform|`CustomHealthcare`|
-|`parameters`| |List of parameters to pass to the task.| |
-| `project-name` |`{PROJECT-NAME}` | The name for your project. This value is case-sensitive.  | `myProject` |
-| `deployment-name` |`{DEPLOYMENT-NAME}` | The name of your deployment. This value is case-sensitive.  | `prod` |
-
-
-#### Response
-
-You will receive a 202 response indicating that your task has been submitted successfully. In the response **headers**, extract `operation-location`.
-`operation-location` is formatted like this:
-
-```rest
-{ENDPOINT}/language/analyze-text/jobs/{JOB-ID}?api-version={API-VERSION}
-```
-
-You can use this URL to query the task completion status and get the results when task is completed.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析タスクの送信に関するAPI情報の削除"
}
```

### Explanation
この変更により、`submit-task.md`ドキュメントが削除されました。この文書は、健康向けのカスタムテキスト分析タスクを開始するためのPOSTリクエストに関する詳細情報を提供していました。具体的には、エンドポイント、必要なヘッダー、リクエストボディの構造、ならびに成功した場合のレスポンス情報が含まれていました。

リクエストボディでは、ジョブに関する表示名、分析する文書のリスト、タスク名、プロジェクト名、デプロイメント名などを指定する必要がありました。また、必要に応じて言語コードを指定し、プロジェクトのデフォルト言語を使用することができました。

このドキュメントが削除されることにより、ユーザーはカスタムテキスト分析タスクを正式に送信する手段を失うことになります。これにより、ユーザーのワークフローに支障をきたす可能性があり、タスク実行に必要な情報を入手できなくなるため、業務に大きな影響を及ぼすことが予想されます。この変更の詳細は、GitHubのリポジトリで確認可能です。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/swap-deployment.md{#item-b2677f}

<details>
<summary>Diff</summary>
````diff
@@ -1,54 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-
-
-Create a **POST** request using the following URL, headers, and JSON body to start a swap deployments job.
-
-
-### Request URL
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/deployments/:swap?api-version={API-VERSION}
-```
-
-|Placeholder  |Value  | Example |
-|---------|---------|---------|
-|`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-|`{PROJECT-NAME}`     | The name for your project. This value is case-sensitive.   | `myProject` |
-|`{API-VERSION}`     | The version of the API you're calling. The value referenced here is for the latest [model version](../../../concepts/model-lifecycle.md#choose-the-model-version-used-on-your-data) released. | `2022-05-01` |
-
-
-### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-
-### Request Body
-
-```json
-{
-  "firstDeploymentName": "{FIRST-DEPLOYMENT-NAME}",
-  "secondDeploymentName": "{SECOND-DEPLOYMENT-NAME}"
-}
-```
-
-
-|Key|Placeholder| Value| Example|
-|--|--|--|--|
-|firstDeploymentName |`{FIRST-DEPLOYMENT-NAME}`| The name for your first deployment. This value is case-sensitive.   | `production` |
-|secondDeploymentName | `{SECOND-DEPLOYMENT-NAME}`|The name for your second deployment. This value is case-sensitive.   | `staging` |
-
-
-Once you send your API request, you will receive a `202` response indicating success.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デプロイメントのスワップに関するAPI情報の削除"
}
```

### Explanation
この変更により、`swap-deployment.md`ドキュメントが削除されました。この文書は、デプロイメントのスワップを開始するためのPOSTリクエストに関する詳細情報を提供していました。具体的には、リクエストURL、必要なヘッダー、リクエストボディの構造が記載されており、ユーザーがデプロイメントをスワップする手順を理解できるようになっていました。

リクエストのボディには、スワップする二つのデプロイメント名を指定する必要があり、ユーザーは具体的なデプロイメントの状態を管理できました。また、この操作の成功を示すために、`202`レスポンスが返されることも記載されていました。

このドキュメントの削除により、ユーザーはデプロイメントのスワップを実行する方法に関する情報源を失うことになります。これにより、デプロイメント管理の効率が低下し、業務に影響を及ぼす可能性があります。この変更の詳細情報については、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/rest-api/train-model.md{#item-ce039c}

<details>
<summary>Diff</summary>
````diff
@@ -1,66 +0,0 @@
----
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-Submit a **POST** request using the following URL, headers, and JSON body to submit a training job. Replace the placeholder values with your own values. 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/:train?api-version={API-VERSION}
-```
-
-| Placeholder |Value | Example |
-|---------|---------|---------|
-| `{ENDPOINT}` | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
-| `{PROJECT-NAME}` | The name of your project. This value is case-sensitive.   | `myProject` |
-|`{API-VERSION}`     | The version of the API you're calling. The value referenced here is for the latest version released. See [Model lifecycle](../../../concepts/model-lifecycle.md) to learn more about other available API versions.  | `2022-05-01` |
-
-#### Headers
-
-Use the following header to authenticate your request. 
-
-|Key|Value|
-|--|--|
-|`Ocp-Apim-Subscription-Key`| The key to your resource. Used for authenticating your API requests.|
-
-#### Request body
-
-Use the following JSON in your request body. The model is given the `{MODEL-NAME}` once training is complete. Only successful training jobs produce models. 
-
-
-```json
-{
-	"modelLabel": "{MODEL-NAME}",
-	"trainingConfigVersion": "{CONFIG-VERSION}",
-	"evaluationOptions": {
-		"kind": "percentage",
-		"trainingSplitPercentage": 80,
-		"testingSplitPercentage": 20
-	}
-}
-```
-
-|Key  |Placeholder  |Value  | Example |
-|---------|---------|-----|----|
-| modelLabel | `{MODEL-NAME}` | The model name that is assigned to your model once trained successfully.  | `myModel` |
-| trainingConfigVersion | `{CONFIG-VERSION}` | This is the [model version](../../../concepts/model-lifecycle.md) that is used to train the model. | `2022-05-01`| 
-| evaluationOptions |  | Option to split your data across training and testing sets. | `{}` |
-| kind | `percentage` |  Split methods. Possible values are `percentage` or `manual`. See [How to train a model](../../how-to/train-model.md#data-splitting) for more information. |`percentage`|
-| trainingSplitPercentage | `80`| Percentage of your tagged data to be included in the training set. Recommended value is `80`. | `80`|
-| testingSplitPercentage | `20` | Percentage of your tagged data to be included in the testing set. Recommended value is `20`.   | `20` |
-
-  > [!NOTE]
-  > The `trainingSplitPercentage` and `testingSplitPercentage` are only required if `Kind` is set to `percentage` and the sum of both percentages should be equal to 100.
-
-Once you send your API request, you’ll receive a `202` response indicating that the job was submitted correctly. In the response headers, extract the `location` value. It is formatted like this: 
-
-```rest
-{ENDPOINT}/language/authoring/analyze-text/projects/{PROJECT-NAME}/train/jobs/{JOB-ID}?api-version={API-VERSION}
-``` 
-
-`{JOB-ID}` is used to identify your request, since this operation is asynchronous. You can use this URL to get the training status.  
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデルのトレーニングに関するAPI情報の削除"
}
```

### Explanation
この変更により、`train-model.md`ドキュメントが削除されました。この文書は、トレーニングジョブを送信するためのPOSTリクエストに必要な情報を提供していました。具体的には、リクエストURL、認証に必要なヘッダー、及びリクエストボディの詳細が含まれており、ユーザーがモデルをトレーニングするために必要な手順を理解できる内容となっていました。

リクエストボディでは、トレーニングが完了した際にモデルに与えられるラベルや、トレーニングおよびテストの分割方法に関するオプションが含まれていました。トレーニングジョブの成功を示すために、`202`レスポンスが返されることも明示されており、ジョブの識別に使用される`JOB-ID`を取得する手順も説明されていました。

このドキュメントが削除されたことで、ユーザーはモデルをトレーニングする方法に関する公式な情報を失うことになります。このため、モデル管理やトレーニングプロセスに関して混乱が生じる可能性があり、業務に悪影響を及ぼすことが懸念されます。詳細情報はGitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/includes/use-pre-existing-resource.md{#item-c35be9}

<details>
<summary>Diff</summary>
````diff
@@ -1,65 +0,0 @@
----
-titleSuffix: Azure AI services
-description: Learn about the steps for using Azure resources with custom NER.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: include
-ms.date: 12/19/2023
-ms.author: jboback
----
-
-You can use an existing Language resource to get started with custom NER as long as this resource meets the below requirements:
-
-|Requirement  |Description  |
-|---------|---------|
-|Regions     | Make sure your existing resource is provisioned in one of the supported regions. If not, you will need to create a new resource in one of these regions.        |
-|Pricing tier     | The [pricing tier](../reference/service-limits.md#language-resource-limits) for your resource.       |
-|Managed identity     | Make sure that the resource's managed identity setting is enabled. Otherwise, read the next section. |
-
-To use custom text analytics for health, you'll need to [create an Azure storage account](/azure/storage/common/storage-account-create) if you don't have one already. 
-
-## Enable identity management for your resource
-
-# [Azure portal](#tab/portal)
-
-Your Language resource must have identity management. To enable it using the [Azure portal](https://portal.azure.com):
-
-1. Go to your Language resource
-2. From left hand menu, under **Resource Management** section, select **Identity**
-3. From **System assigned** tab, make sure to set **Status** to **On**
-
-# [Language Studio](#tab/studio)
-
-Your Language resource must have identity management, to enable it using [Language Studio](https://aka.ms/languageStudio):
-
-1. Select the settings icon in the top right corner of the screen
-2. Select **Resources**
-3. Select the check box **Managed Identity** for your Azure AI Language resource.
-
----
-
-### Enable custom text analytics for health
-
-Make sure to enable **Custom text classification / Custom Named Entity Recognition / Custom text analytics for health** feature from Azure portal.
-
-1. Go to your Language resource in the [Azure portal](https://portal.azure.com).
-2. From the left side menu, under **Resource Management** section, select **Features**
-3. Enable the **Custom text classification / Custom Named Entity Recognition / Custom text analytics** feature
-4. Connect your storage account
-5. Select **Apply**
-
->[!Important]
-> * Make sure that your **Language resource** has **storage blob data contributor** role assigned on the storage account you are connecting.
-
-### Add required roles
-
-[!INCLUDE [required roles](../../includes/custom/roles-for-resource-and-storage.md)]
-
-### Enable CORS for your storage account
-
-Make sure to allow (**GET, PUT, DELETE**) methods when enabling Cross-Origin Resource Sharing (CORS). 
-Set allowed origins field to `https://language.cognitive.azure.com`. Allow all header by adding `*` to the allowed header values, and set the maximum age to `500`.
-
-:::image type="content" source="../media/resource-sharing.png" alt-text="A screenshot showing how to use CORS for storage accounts." lightbox="../media/resource-sharing.png":::
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "既存のリソースを使用する方法に関する情報の削除"
}
```

### Explanation
この変更により、`use-pre-existing-resource.md`ドキュメントが削除されました。この文書は、カスタムNER（Named Entity Recognition）を使用するために、既存のLanguageリソースを利用する手順について説明していました。具体的には、リソースが満たすべき要件（地域、価格帯、マネージドアイデンティティの設定）や、AzureポータルおよびLanguage Studioを使用してアイデンティティ管理を有効にする方法が含まれていました。

また、カスタムテキスト分析を有効にするための手順や、ストレージアカウントの作成についても詳細に説明されていました。CORS（Cross-Origin Resource Sharing）の設定方法、およびストレージアカウントに必要な役割を追加するための情報も含まれていました。

このドキュメントの削除は、ユーザーが既存のリソースを利用してカスタムテキスト分析を行う際のガイダンスを失うことを意味します。その結果、ユーザーはリソース管理や設定に関して混乱し、業務プロセスに支障をきたす懸念があります。削除された内容の詳細については、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/language-support.md{#item-416183}

<details>
<summary>Diff</summary>
````diff
@@ -1,45 +0,0 @@
----
-title: Language and region support for custom Text Analytics for health
-titleSuffix: Azure AI services
-description: Learn about the languages and regions supported by custom Text Analytics for health
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: conceptual
-ms.date: 11/21/2024
-ms.custom: language-service-custom-ta4h
-ms.author: jboback
----
-
-# Language support for custom text analytics for health
-
-Use this article to learn about the languages currently supported by custom Text Analytics for health.
-
-## Multilingual option
-
-With custom Text Analytics for health, you can train a model in one language and use it to extract entities from documents other languages. This feature saves you the trouble of building separate projects for each language and instead combining your datasets in a single project, making it easy to scale your projects to multiple languages. You can train your project entirely with English documents, and query it in: French, German, Italian, and others. You can enable the multilingual option as part of the project creation process or later through the project settings.
-
-You aren't expected to add the same number of documents for every language. You should build the majority of your project in one language, and only add a few documents in languages you observe aren't performing well. If you create a project that is primarily in English, and start testing it in French, German, and Spanish, you might observe that German doesn't perform as well as the other two languages. In that case, consider adding 5% of your original English documents in German, train a new model and test in German again. In the [data labeling](how-to/label-data.md) page in Language Studio, you can select the language of the document you're adding. You should see better results for German queries. The more labeled documents you add, the more likely the results are going to get better. When you add data in another language, you shouldn't expect it to negatively affect other languages. 
-
-Hebrew is not supported in multilingual projects. If the primary language of the project is Hebrew, you will not be able to add training data in other languages, or query the model with other languages. Similarly, if the primary language of the project is not Hebrew, you will not be able to add training data in Hebrew, or query the model in Hebrew.
-
-## Language support
-
-Custom Text Analytics for health supports `.txt` files in the following languages:
-
-| Language | Language code |
-| --- | --- |
-| English | `en` |
-| French | `fr` |
-| German | `de` |
-| Spanish | `es` |
-| Italian | `it` |
-| Portuguese (Portugal) | `pt-pt` |
-| Hebrew | `he` |
-
-
-## Next steps
-
-* [Custom Text Analytics for health overview](overview.md)
-* [Service limits](reference/service-limits.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析の言語サポートに関する情報の削除"
}
```

### Explanation
この変更により、`language-support.md`ドキュメントが削除されました。この文書は、カスタムテキスト分析の健康に関するサポートされている言語および地域についての情報を提供していました。特に、マルチリンガルオプションの利用方法や、特定の言語でのトレーニングデータの追加に関するガイドラインが含まれていました。

削除された内容には、モデルを一つの言語でトレーニングし、他の言語からエンティティを抽出する方法が説明されており、言語ごとにプロジェクトを分離することなく複数の言語にスケールさせるためのヒントも示されていました。また、言語サポートの具体的なリスト（英語、フランス語、ドイツ語など）や、ヘブライ語に関する制限についても詳細がありました。

このドキュメントの削除は、ユーザーがカスタムテキスト分析を使用する際に必要な言語サポートに関する指針を失うことを意味し、その結果、ユーザーのプロジェクトにおいて言語関連の設定が困難になる可能性があります。この変更による影響を最小限に抑えるためには、利用可能な情報を提供する必要があります。詳細情報はGitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/add-deployment.png{#item-b13093}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "デプロイメント画像の削除"
}
```

### Explanation
この変更では、`add-deployment.png`という画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスのデプロイメント手順を視覚的に示すために使用されていたものです。具体的には、ユーザーがデプロイメントプロセスを理解しやすくするための補助として提供されていた可能性があります。

画像の削除により、ドキュメントにおける視覚的な指示が失われ、ユーザーが手順を理解する際に不便を感じることが予想されます。また、新たにデプロイメントに関する情報や手順を学ぶ際のサポートが無くなるため、ユーザーフレンドリーさが低下する可能性があります。この変更に伴い、デプロイメントに関する他の資料やガイダンスが存在するか、適切な代替手段を提供する必要があります。画像の詳細については、GitHubのリポジトリでの閲覧が可能です。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/connect-storage.png{#item-6ae9de}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ストレージ接続画像の削除"
}
```

### Explanation
この変更では、`connect-storage.png`という画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスにおけるストレージの接続手順を視覚的に示すために使用されていたと考えられます。

画像の削除により、ユーザーはストレージ接続の手順を理解するための視覚的な助けを失うことになります。これにより、特に新しいユーザーや初心者にとって、設定や接続が難しく感じられる可能性があります。また、画像に依存していた内容を理解するために追加の文書や指示が必要になる場合も考えられます。

視覚的なガイダンスの欠如は、ユーザーエクスペリエンスに影響を与える可能性があるため、代替情報や資料を提供することが望まれます。この画像に関する詳細は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/create-project.png{#item-a58210}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プロジェクト作成画像の削除"
}
```

### Explanation
この変更では、`create-project.png`という画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスにおけるプロジェクト作成手順を視覚的にサポートするために使用されていました。

画像の削除に伴い、ユーザーはプロジェクトを作成するための視覚的なガイドを失うことになります。このため、特に初めて使用するユーザーには、手続きの理解や実施が困難になる可能性があります。これにより、手順を文書だけで理解しようとする必要があり、不明点が生じるかもしれません。

この画像なき後、プロジェクト作成に関する情報や支援を提供するために、代わりのドキュメントやリソースが必要となるでしょう。詳細な情報は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/deploy-model.png{#item-cd9164}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル展開画像の削除"
}
```

### Explanation
この変更では、`deploy-model.png`という画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスにおけるモデルの展開手順を視覚的に示していたと考えられます。

画像が削除されたことにより、ユーザーはモデルを展開するための視覚的なサポートを失うことになります。その結果、特に新しいユーザーや初心者にとって、手順を理解することが困難になる可能性があります。手続きが複雑に感じられることで、業務の流れに影響を与えることも考えられます。

この画像に代わる情報や手順を提供することが重要であり、ユーザーが依然としてモデルの展開を円滑に行えるように、補足資料が必要になるでしょう。詳細については、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/development-lifecycle.png{#item-4dca20}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "開発ライフサイクル画像の削除"
}
```

### Explanation
この変更では、`development-lifecycle.png`という画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスにおける開発ライフサイクルの概観を視覚的に示していたものと考えられます。

画像が削除されたことによって、ユーザーは開発プロセスの重要な部分を視覚的に理解する手助けを失うことになります。特に、プロジェクトの計画や構造を把握するためにこのような視覚資料が不可欠なユーザーには、一層の混乱をもたらす可能性があります。結果として、開発工程に関する情報を理解するために、より多くのテキスト情報や補足資料が必要となるかもしれません。

さらに、開発ライフサイクルの視覚化は、チーム間のコミュニケーションや協力を促進するための重要な要素であり、削除によってその効果が損なわれる恐れがあります。詳細は、GitHubのリポジトリにて確認可能です。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/file-upload-screen.png{#item-314ce4}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ファイルアップロード画面画像の削除"
}
```

### Explanation
この変更では、`file-upload-screen.png`という画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスにおけるファイルアップロードのインターフェースを示していた可能性があります。

画像の削除により、ユーザーはファイルのアップロード手順を視覚的に理解するための情報を失うことになります。このような視覚資料が欠けることで、特に新規ユーザーや技術に不慣れなユーザーは、操作手順を理解する上で困難を感じるかもしれません。結果として、手順の理解や採用を促進する上での障壁が生じる可能性があります。

したがって、この画像に代わる情報や手順の文書化が急務となります。これにより、ユーザーがファイルを円滑にアップロードできるようにするための支援が必要です。詳細については、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/learned-component.png{#item-74afb1}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "学習コンポーネント画像の削除"
}
```

### Explanation
この変更では、`learned-component.png`という画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスにおける学習コンポーネントのビジュアル概要を提供していたと考えられます。

画像の削除により、ユーザーは学習コンポーネントの構成や動作を視覚的に理解するための手掛かりを失うことになります。特に複雑なシステムに関与する開発者やデータサイエンティストにとって、このような視覚的資料は動作理解のために重要です。削除の結果、理解を補完するためのテキスト情報の充実が求められるでしょう。

この変更により、学習プロセスやコンポーネントの利用に関する情報提供が不足する可能性があり、特に新しいユーザーやプロジェクトの立ち上げ時には、より多くの説明や例が必要となります。詳細は、GitHubのリポジトリにて確認可能です。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/list-component.png{#item-e9952e}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "リストコンポーネント画像の削除"
}
```

### Explanation
この変更では、`list-component.png`という画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスにおけるリストコンポーネントの視覚的な説明を提供していたと思われます。

リストコンポーネントの画像が削除されることにより、ユーザーはリストの構造や動作を理解するための視覚的な情報を失います。特に、リストコンポーネントがどのように機能し、どのようにデータとインタラクションするのかを学ぶ新しいユーザーには、視覚的サポートが重要です。この削除により、ユーザーが直面する情報の欠落が生じ、操作性や理解度に影響を与える可能性があります。

この変更を補完するためには、代替となる説明文や図解を提供することが推奨されます。これにより、ユーザーがリストコンポーネントを正しく活用できるようにする必要があります。詳細については、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/prebuilt-component.png{#item-ea83f3}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "プリビルトコンポーネント画像の削除"
}
```

### Explanation
この変更では、`prebuilt-component.png`という画像ファイルが削除されました。この画像は、カスタムテキスト分析サービス内のプリビルトコンポーネントの視覚的な例を示していたと考えられます。

プリビルトコンポーネントの画像が削除されることで、ユーザーはその機能や配置方法を理解するための重要な視覚情報を失うことになります。これにより、新しいユーザーや開発者がプリビルトコンポーネントを使用する際に、操作や実装に関する理解が難しくなる可能性があります。

この削除によって、ユーザーはテキスト分析サービスを効果的に活用するために、他のソースやドキュメントに頼らざるを得なくなるかもしれません。代わりに、詳細なテキスト説明やガイドラインを提供することが求められます。関連情報は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/resource-sharing.png{#item-732a75}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "リソース共有画像の削除"
}
```

### Explanation
この変更では、`resource-sharing.png`という画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスにおいてリソース共有のプロセスや方法を視覚的に示すために使用されていたと推測されます。

リソース共有の画像が削除されることで、ユーザーはこの機能の具体的な利用方法や推奨される手順を理解するための重要な視覚的情報を失います。特に、新しいユーザーや開発者にとっては、リソース共有の設定や管理方法を理解する際に、視覚的な例が役立つため、影響が大きいです。

この削除により、情報の欠落が発生し、ユーザーは他の資料やドキュメントを参照する必要が生じるかもしれません。したがって、代替として詳しいテキスト説明や手順を提供することが望まれます。詳細については、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/select-custom-feature-azure-portal.png{#item-7dfe20}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Azureポータルでのカスタム機能選択画像の削除"
}
```

### Explanation
この変更では、`select-custom-feature-azure-portal.png`という画像ファイルが削除されました。この画像は、Azureポータルでカスタム機能を選択する手順を視覚的に示すために使用されていたと考えられます。

この画像が削除されることで、ユーザーはAzureポータルにおけるカスタム機能の選択方法を理解するための重要な視覚的ヒントを失います。特に、初心者や新しい開発者にとっては、視覚的なガイドが操作を簡便にし、理解を助ける役割を果たしていたため、大きな影響があります。

この削除により、ユーザーはカスタム機能の選択に関して、追加の文書や指示を探す必要が生じるかもしれません。そのため、削除された画像の代わりに、より詳細なテキスト説明や説明書を提供することが求められるでしょう。関連情報は、GitHubのリポジトリで確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/separated-overlap-example-1-part-2.svg{#item-7488c7}

<details>
<summary>Diff</summary>
````diff
@@ -1,22 +0,0 @@
-<svg width="289" height="167" viewBox="0 0 289 167" fill="none" xmlns="http://www.w3.org/2000/svg">
-<g clip-path="url(#clip0_858_39236)">
-<path d="M296 0H0V167H296V0Z" fill="#F3F2F1"/>
-<path d="M102.953 66.2949V70H101.805V60.1973H104.498C105.546 60.1973 106.357 60.4525 106.932 60.9629C107.51 61.4733 107.8 62.1934 107.8 63.123C107.8 64.0527 107.479 64.8138 106.836 65.4062C106.198 65.9987 105.334 66.2949 104.245 66.2949H102.953ZM102.953 61.2363V65.2559H104.156C104.949 65.2559 105.553 65.0758 105.968 64.7158C106.387 64.3512 106.597 63.8385 106.597 63.1777C106.597 61.8835 105.831 61.2363 104.3 61.2363H102.953ZM113.152 64.1348C112.956 63.9844 112.674 63.9092 112.305 63.9092C111.826 63.9092 111.425 64.1348 111.102 64.5859C110.783 65.0371 110.623 65.6523 110.623 66.4316V70H109.502V63H110.623V64.4424H110.65C110.81 63.9502 111.054 63.5674 111.382 63.2939C111.71 63.016 112.077 62.877 112.482 62.877C112.774 62.877 112.997 62.9089 113.152 62.9727V64.1348ZM117.295 70.1641C116.26 70.1641 115.433 69.8382 114.813 69.1865C114.198 68.5303 113.891 67.6621 113.891 66.582C113.891 65.4062 114.212 64.488 114.854 63.8271C115.497 63.1663 116.365 62.8359 117.459 62.8359C118.503 62.8359 119.316 63.1572 119.899 63.7998C120.487 64.4424 120.781 65.3333 120.781 66.4727C120.781 67.5892 120.465 68.4847 119.831 69.1592C119.202 69.8291 118.357 70.1641 117.295 70.1641ZM117.377 63.7793C116.657 63.7793 116.087 64.0254 115.668 64.5176C115.249 65.0052 115.039 65.6797 115.039 66.541C115.039 67.3704 115.251 68.0244 115.675 68.5029C116.099 68.9814 116.666 69.2207 117.377 69.2207C118.102 69.2207 118.658 68.986 119.045 68.5166C119.437 68.0472 119.633 67.3796 119.633 66.5137C119.633 65.6387 119.437 64.9642 119.045 64.4902C118.658 64.0163 118.102 63.7793 117.377 63.7793ZM122.148 69.7471V68.5439C122.759 68.9951 123.431 69.2207 124.165 69.2207C125.149 69.2207 125.642 68.8926 125.642 68.2363C125.642 68.0495 125.598 67.8923 125.512 67.7646C125.43 67.6325 125.316 67.5163 125.17 67.416C125.029 67.3158 124.86 67.2269 124.664 67.1494C124.473 67.0674 124.265 66.9831 124.042 66.8965C123.732 66.7734 123.459 66.6504 123.222 66.5273C122.989 66.3997 122.793 66.2585 122.634 66.1035C122.479 65.944 122.36 65.764 122.278 65.5635C122.201 65.363 122.162 65.1283 122.162 64.8594C122.162 64.5312 122.237 64.2419 122.388 63.9912C122.538 63.736 122.739 63.5241 122.989 63.3555C123.24 63.1823 123.525 63.0524 123.844 62.9658C124.167 62.8792 124.5 62.8359 124.842 62.8359C125.448 62.8359 125.99 62.9408 126.469 63.1504V64.2852C125.954 63.9479 125.361 63.7793 124.691 63.7793C124.482 63.7793 124.293 63.8044 124.124 63.8545C123.955 63.9001 123.81 63.9661 123.687 64.0527C123.568 64.1393 123.475 64.2441 123.406 64.3672C123.342 64.4857 123.311 64.6178 123.311 64.7637C123.311 64.946 123.342 65.0986 123.406 65.2217C123.475 65.3447 123.573 65.4541 123.7 65.5498C123.828 65.6455 123.983 65.7321 124.165 65.8096C124.347 65.887 124.555 65.9714 124.787 66.0625C125.097 66.181 125.375 66.304 125.621 66.4316C125.867 66.5547 126.077 66.696 126.25 66.8555C126.423 67.0104 126.555 67.1904 126.646 67.3955C126.742 67.6006 126.79 67.8444 126.79 68.127C126.79 68.4733 126.713 68.7741 126.558 69.0293C126.407 69.2845 126.204 69.4964 125.949 69.665C125.694 69.8337 125.4 69.959 125.067 70.041C124.735 70.123 124.386 70.1641 124.021 70.1641C123.301 70.1641 122.677 70.0251 122.148 69.7471ZM134.146 66.7803H129.203C129.221 67.5596 129.431 68.1611 129.832 68.585C130.233 69.0088 130.785 69.2207 131.486 69.2207C132.275 69.2207 132.999 68.9609 133.66 68.4414V69.4941C133.045 69.9408 132.231 70.1641 131.22 70.1641C130.231 70.1641 129.454 69.8473 128.889 69.2139C128.324 68.5758 128.041 67.6803 128.041 66.5273C128.041 65.4382 128.349 64.5518 128.964 63.8682C129.584 63.18 130.352 62.8359 131.268 62.8359C132.184 62.8359 132.892 63.1322 133.394 63.7246C133.895 64.3171 134.146 65.1396 134.146 66.1924V66.7803ZM132.997 65.8301C132.993 65.1829 132.835 64.6794 132.525 64.3193C132.22 63.9593 131.794 63.7793 131.247 63.7793C130.718 63.7793 130.27 63.9684 129.9 64.3467C129.531 64.7249 129.303 65.2194 129.217 65.8301H132.997ZM144.666 63L142.567 70H141.405L139.963 64.9893C139.908 64.7979 139.872 64.5814 139.854 64.3398H139.826C139.812 64.5039 139.765 64.7158 139.683 64.9756L138.117 70H136.996L134.877 63H136.053L137.502 68.2637C137.548 68.4232 137.579 68.6328 137.598 68.8926H137.652C137.666 68.6921 137.707 68.4779 137.775 68.25L139.389 63H140.414L141.863 68.2773C141.909 68.446 141.943 68.6556 141.966 68.9062H142.021C142.03 68.7285 142.068 68.5189 142.137 68.2773L143.559 63H144.666ZM150.976 70H149.854V68.9062H149.827C149.34 69.7448 148.622 70.1641 147.674 70.1641C146.977 70.1641 146.43 69.9795 146.033 69.6104C145.641 69.2412 145.445 68.7513 145.445 68.1406C145.445 66.8327 146.215 66.0716 147.756 65.8574L149.854 65.5635C149.854 64.374 149.374 63.7793 148.412 63.7793C147.569 63.7793 146.808 64.0664 146.129 64.6406V63.4922C146.817 63.0547 147.61 62.8359 148.508 62.8359C150.153 62.8359 150.976 63.7064 150.976 65.4473V70ZM149.854 66.459L148.166 66.6914C147.646 66.7643 147.255 66.8942 146.99 67.0811C146.726 67.2633 146.594 67.5892 146.594 68.0586C146.594 68.4004 146.715 68.6807 146.956 68.8994C147.202 69.1136 147.528 69.2207 147.934 69.2207C148.49 69.2207 148.948 69.027 149.308 68.6396C149.672 68.2477 149.854 67.7533 149.854 67.1562V66.459ZM156.738 64.1348C156.542 63.9844 156.26 63.9092 155.891 63.9092C155.412 63.9092 155.011 64.1348 154.688 64.5859C154.368 65.0371 154.209 65.6523 154.209 66.4316V70H153.088V63H154.209V64.4424H154.236C154.396 63.9502 154.64 63.5674 154.968 63.2939C155.296 63.016 155.663 62.877 156.068 62.877C156.36 62.877 156.583 62.9089 156.738 62.9727V64.1348ZM163.581 66.7803H158.639C158.657 67.5596 158.867 68.1611 159.268 68.585C159.669 69.0088 160.22 69.2207 160.922 69.2207C161.71 69.2207 162.435 68.9609 163.096 68.4414V69.4941C162.48 69.9408 161.667 70.1641 160.655 70.1641C159.666 70.1641 158.889 69.8473 158.324 69.2139C157.759 68.5758 157.477 67.6803 157.477 66.5273C157.477 65.4382 157.784 64.5518 158.399 63.8682C159.019 63.18 159.787 62.8359 160.703 62.8359C161.619 62.8359 162.328 63.1322 162.829 63.7246C163.33 64.3171 163.581 65.1396 163.581 66.1924V66.7803ZM162.433 65.8301C162.428 65.1829 162.271 64.6794 161.961 64.3193C161.656 63.9593 161.229 63.7793 160.683 63.7793C160.154 63.7793 159.705 63.9684 159.336 64.3467C158.967 64.7249 158.739 65.2194 158.652 65.8301H162.433ZM169.275 70V60.1973H171.982C175.437 60.1973 177.164 61.79 177.164 64.9756C177.164 66.4886 176.683 67.7054 175.722 68.626C174.765 69.542 173.482 70 171.873 70H169.275ZM170.424 61.2363V68.9609H171.887C173.172 68.9609 174.172 68.6169 174.888 67.9287C175.603 67.2406 175.961 66.2653 175.961 65.0029C175.961 62.4919 174.626 61.2363 171.955 61.2363H170.424ZM184.567 66.7803H179.625C179.643 67.5596 179.853 68.1611 180.254 68.585C180.655 69.0088 181.206 69.2207 181.908 69.2207C182.697 69.2207 183.421 68.9609 184.082 68.4414V69.4941C183.467 69.9408 182.653 70.1641 181.642 70.1641C180.653 70.1641 179.876 69.8473 179.311 69.2139C178.745 68.5758 178.463 67.6803 178.463 66.5273C178.463 65.4382 178.771 64.5518 179.386 63.8682C180.006 63.18 180.773 62.8359 181.689 62.8359C182.605 62.8359 183.314 63.1322 183.815 63.7246C184.317 64.3171 184.567 65.1396 184.567 66.1924V66.7803ZM183.419 65.8301C183.414 65.1829 183.257 64.6794 182.947 64.3193C182.642 63.9593 182.216 63.7793 181.669 63.7793C181.14 63.7793 180.691 63.9684 180.322 64.3467C179.953 64.7249 179.725 65.2194 179.639 65.8301H183.419ZM185.846 69.7471V68.5439C186.456 68.9951 187.129 69.2207 187.862 69.2207C188.847 69.2207 189.339 68.8926 189.339 68.2363C189.339 68.0495 189.296 67.8923 189.209 67.7646C189.127 67.6325 189.013 67.5163 188.867 67.416C188.726 67.3158 188.557 67.2269 188.361 67.1494C188.17 67.0674 187.963 66.9831 187.739 66.8965C187.429 66.7734 187.156 66.6504 186.919 66.5273C186.687 66.3997 186.491 66.2585 186.331 66.1035C186.176 65.944 186.058 65.764 185.976 65.5635C185.898 65.363 185.859 65.1283 185.859 64.8594C185.859 64.5312 185.935 64.2419 186.085 63.9912C186.235 63.736 186.436 63.5241 186.687 63.3555C186.937 63.1823 187.222 63.0524 187.541 62.9658C187.865 62.8792 188.197 62.8359 188.539 62.8359C189.145 62.8359 189.688 62.9408 190.166 63.1504V64.2852C189.651 63.9479 189.059 63.7793 188.389 63.7793C188.179 63.7793 187.99 63.8044 187.821 63.8545C187.653 63.9001 187.507 63.9661 187.384 64.0527C187.265 64.1393 187.172 64.2441 187.104 64.3672C187.04 64.4857 187.008 64.6178 187.008 64.7637C187.008 64.946 187.04 65.0986 187.104 65.2217C187.172 65.3447 187.27 65.4541 187.397 65.5498C187.525 65.6455 187.68 65.7321 187.862 65.8096C188.045 65.887 188.252 65.9714 188.484 66.0625C188.794 66.181 189.072 66.304 189.318 66.4316C189.564 66.5547 189.774 66.696 189.947 66.8555C190.12 67.0104 190.253 67.1904 190.344 67.3955C190.439 67.6006 190.487 67.8444 190.487 68.127C190.487 68.4733 190.41 68.7741 190.255 69.0293C190.104 69.2845 189.902 69.4964 189.646 69.665C189.391 69.8337 189.097 69.959 188.765 70.041C188.432 70.123 188.083 70.1641 187.719 70.1641C186.999 70.1641 186.374 70.0251 185.846 69.7471ZM198.027 70H196.455L193.365 66.6367H193.338V70H192.217V59.6367H193.338V66.2061H193.365L196.305 63H197.774L194.527 66.377L198.027 70ZM202.423 69.9316C202.159 70.0775 201.81 70.1504 201.377 70.1504C200.151 70.1504 199.538 69.4668 199.538 68.0996V63.957H198.335V63H199.538V61.291L200.659 60.9287V63H202.423V63.957H200.659V67.9014C200.659 68.3708 200.739 68.7057 200.898 68.9062C201.058 69.1068 201.322 69.207 201.691 69.207C201.974 69.207 202.218 69.1296 202.423 68.9746V69.9316ZM206.846 70.1641C205.811 70.1641 204.984 69.8382 204.364 69.1865C203.749 68.5303 203.441 67.6621 203.441 66.582C203.441 65.4062 203.763 64.488 204.405 63.8271C205.048 63.1663 205.916 62.8359 207.01 62.8359C208.053 62.8359 208.867 63.1572 209.45 63.7998C210.038 64.4424 210.332 65.3333 210.332 66.4727C210.332 67.5892 210.015 68.4847 209.382 69.1592C208.753 69.8291 207.908 70.1641 206.846 70.1641ZM206.928 63.7793C206.208 63.7793 205.638 64.0254 205.219 64.5176C204.799 65.0052 204.59 65.6797 204.59 66.541C204.59 67.3704 204.802 68.0244 205.226 68.5029C205.649 68.9814 206.217 69.2207 206.928 69.2207C207.652 69.2207 208.208 68.986 208.596 68.5166C208.988 68.0472 209.184 67.3796 209.184 66.5137C209.184 65.6387 208.988 64.9642 208.596 64.4902C208.208 64.0163 207.652 63.7793 206.928 63.7793ZM213.271 68.9883H213.244V73.2197H212.123V63H213.244V64.2305H213.271C213.823 63.3008 214.63 62.8359 215.691 62.8359C216.594 62.8359 217.298 63.1504 217.804 63.7793C218.31 64.4036 218.562 65.2422 218.562 66.2949C218.562 67.4661 218.278 68.4049 217.708 69.1113C217.138 69.8132 216.359 70.1641 215.37 70.1641C214.463 70.1641 213.764 69.7721 213.271 68.9883ZM213.244 66.165V67.1426C213.244 67.7214 213.431 68.2135 213.805 68.6191C214.183 69.0202 214.661 69.2207 215.24 69.2207C215.919 69.2207 216.45 68.9609 216.833 68.4414C217.22 67.9219 217.414 67.1995 217.414 66.2744C217.414 65.4951 217.234 64.8844 216.874 64.4424C216.514 64.0003 216.026 63.7793 215.411 63.7793C214.759 63.7793 214.235 64.0072 213.839 64.4629C213.442 64.9141 213.244 65.4814 213.244 66.165ZM225.494 66.2949V70H224.346V60.1973H227.039C228.087 60.1973 228.898 60.4525 229.473 60.9629C230.051 61.4733 230.341 62.1934 230.341 63.123C230.341 64.0527 230.02 64.8138 229.377 65.4062C228.739 65.9987 227.875 66.2949 226.786 66.2949H225.494ZM225.494 61.2363V65.2559H226.697C227.49 65.2559 228.094 65.0758 228.509 64.7158C228.928 64.3512 229.138 63.8385 229.138 63.1777C229.138 61.8835 228.372 61.2363 226.841 61.2363H225.494ZM235.693 64.1348C235.497 63.9844 235.215 63.9092 234.846 63.9092C234.367 63.9092 233.966 64.1348 233.643 64.5859C233.324 65.0371 233.164 65.6523 233.164 66.4316V70H232.043V63H233.164V64.4424H233.191C233.351 63.9502 233.595 63.5674 233.923 63.2939C234.251 63.016 234.618 62.877 235.023 62.877C235.315 62.877 235.538 62.9089 235.693 62.9727V64.1348ZM239.836 70.1641C238.801 70.1641 237.974 69.8382 237.354 69.1865C236.739 68.5303 236.432 67.6621 236.432 66.582C236.432 65.4062 236.753 64.488 237.396 63.8271C238.038 63.1663 238.906 62.8359 240 62.8359C241.044 62.8359 241.857 63.1572 242.44 63.7998C243.028 64.4424 243.322 65.3333 243.322 66.4727C243.322 67.5892 243.006 68.4847 242.372 69.1592C241.743 69.8291 240.898 70.1641 239.836 70.1641ZM239.918 63.7793C239.198 63.7793 238.628 64.0254 238.209 64.5176C237.79 65.0052 237.58 65.6797 237.58 66.541C237.58 67.3704 237.792 68.0244 238.216 68.5029C238.64 68.9814 239.207 69.2207 239.918 69.2207C240.643 69.2207 241.199 68.986 241.586 68.5166C241.978 68.0472 242.174 67.3796 242.174 66.5137C242.174 65.6387 241.978 64.9642 241.586 64.4902C241.199 64.0163 240.643 63.7793 239.918 63.7793Z" fill="black"/>
-<path d="M102.953 113.295V117H101.805V107.197H104.498C105.546 107.197 106.357 107.452 106.932 107.963C107.51 108.473 107.8 109.193 107.8 110.123C107.8 111.053 107.479 111.814 106.836 112.406C106.198 112.999 105.334 113.295 104.245 113.295H102.953ZM102.953 108.236V112.256H104.156C104.949 112.256 105.553 112.076 105.968 111.716C106.387 111.351 106.597 110.839 106.597 110.178C106.597 108.883 105.831 108.236 104.3 108.236H102.953ZM113.152 111.135C112.956 110.984 112.674 110.909 112.305 110.909C111.826 110.909 111.425 111.135 111.102 111.586C110.783 112.037 110.623 112.652 110.623 113.432V117H109.502V110H110.623V111.442H110.65C110.81 110.95 111.054 110.567 111.382 110.294C111.71 110.016 112.077 109.877 112.482 109.877C112.774 109.877 112.997 109.909 113.152 109.973V111.135ZM117.295 117.164C116.26 117.164 115.433 116.838 114.813 116.187C114.198 115.53 113.891 114.662 113.891 113.582C113.891 112.406 114.212 111.488 114.854 110.827C115.497 110.166 116.365 109.836 117.459 109.836C118.503 109.836 119.316 110.157 119.899 110.8C120.487 111.442 120.781 112.333 120.781 113.473C120.781 114.589 120.465 115.485 119.831 116.159C119.202 116.829 118.357 117.164 117.295 117.164ZM117.377 110.779C116.657 110.779 116.087 111.025 115.668 111.518C115.249 112.005 115.039 112.68 115.039 113.541C115.039 114.37 115.251 115.024 115.675 115.503C116.099 115.981 116.666 116.221 117.377 116.221C118.102 116.221 118.658 115.986 119.045 115.517C119.437 115.047 119.633 114.38 119.633 113.514C119.633 112.639 119.437 111.964 119.045 111.49C118.658 111.016 118.102 110.779 117.377 110.779ZM122.148 116.747V115.544C122.759 115.995 123.431 116.221 124.165 116.221C125.149 116.221 125.642 115.893 125.642 115.236C125.642 115.049 125.598 114.892 125.512 114.765C125.43 114.632 125.316 114.516 125.17 114.416C125.029 114.316 124.86 114.227 124.664 114.149C124.473 114.067 124.265 113.983 124.042 113.896C123.732 113.773 123.459 113.65 123.222 113.527C122.989 113.4 122.793 113.258 122.634 113.104C122.479 112.944 122.36 112.764 122.278 112.563C122.201 112.363 122.162 112.128 122.162 111.859C122.162 111.531 122.237 111.242 122.388 110.991C122.538 110.736 122.739 110.524 122.989 110.355C123.24 110.182 123.525 110.052 123.844 109.966C124.167 109.879 124.5 109.836 124.842 109.836C125.448 109.836 125.99 109.941 126.469 110.15V111.285C125.954 110.948 125.361 110.779 124.691 110.779C124.482 110.779 124.293 110.804 124.124 110.854C123.955 110.9 123.81 110.966 123.687 111.053C123.568 111.139 123.475 111.244 123.406 111.367C123.342 111.486 123.311 111.618 123.311 111.764C123.311 111.946 123.342 112.099 123.406 112.222C123.475 112.345 123.573 112.454 123.7 112.55C123.828 112.646 123.983 112.732 124.165 112.81C124.347 112.887 124.555 112.971 124.787 113.062C125.097 113.181 125.375 113.304 125.621 113.432C125.867 113.555 126.077 113.696 126.25 113.855C126.423 114.01 126.555 114.19 126.646 114.396C126.742 114.601 126.79 114.844 126.79 115.127C126.79 115.473 126.713 115.774 126.558 116.029C126.407 116.285 126.204 116.496 125.949 116.665C125.694 116.834 125.4 116.959 125.067 117.041C124.735 117.123 124.386 117.164 124.021 117.164C123.301 117.164 122.677 117.025 122.148 116.747ZM134.146 113.78H129.203C129.221 114.56 129.431 115.161 129.832 115.585C130.233 116.009 130.785 116.221 131.486 116.221C132.275 116.221 132.999 115.961 133.66 115.441V116.494C133.045 116.941 132.231 117.164 131.22 117.164C130.231 117.164 129.454 116.847 128.889 116.214C128.324 115.576 128.041 114.68 128.041 113.527C128.041 112.438 128.349 111.552 128.964 110.868C129.584 110.18 130.352 109.836 131.268 109.836C132.184 109.836 132.892 110.132 133.394 110.725C133.895 111.317 134.146 112.14 134.146 113.192V113.78ZM132.997 112.83C132.993 112.183 132.835 111.679 132.525 111.319C132.22 110.959 131.794 110.779 131.247 110.779C130.718 110.779 130.27 110.968 129.9 111.347C129.531 111.725 129.303 112.219 129.217 112.83H132.997ZM144.666 110L142.567 117H141.405L139.963 111.989C139.908 111.798 139.872 111.581 139.854 111.34H139.826C139.812 111.504 139.765 111.716 139.683 111.976L138.117 117H136.996L134.877 110H136.053L137.502 115.264C137.548 115.423 137.579 115.633 137.598 115.893H137.652C137.666 115.692 137.707 115.478 137.775 115.25L139.389 110H140.414L141.863 115.277C141.909 115.446 141.943 115.656 141.966 115.906H142.021C142.03 115.729 142.068 115.519 142.137 115.277L143.559 110H144.666ZM150.976 117H149.854V115.906H149.827C149.34 116.745 148.622 117.164 147.674 117.164C146.977 117.164 146.43 116.979 146.033 116.61C145.641 116.241 145.445 115.751 145.445 115.141C145.445 113.833 146.215 113.072 147.756 112.857L149.854 112.563C149.854 111.374 149.374 110.779 148.412 110.779C147.569 110.779 146.808 111.066 146.129 111.641V110.492C146.817 110.055 147.61 109.836 148.508 109.836C150.153 109.836 150.976 110.706 150.976 112.447V117ZM149.854 113.459L148.166 113.691C147.646 113.764 147.255 113.894 146.99 114.081C146.726 114.263 146.594 114.589 146.594 115.059C146.594 115.4 146.715 115.681 146.956 115.899C147.202 116.114 147.528 116.221 147.934 116.221C148.49 116.221 148.948 116.027 149.308 115.64C149.672 115.248 149.854 114.753 149.854 114.156V113.459ZM156.738 111.135C156.542 110.984 156.26 110.909 155.891 110.909C155.412 110.909 155.011 111.135 154.688 111.586C154.368 112.037 154.209 112.652 154.209 113.432V117H153.088V110H154.209V111.442H154.236C154.396 110.95 154.64 110.567 154.968 110.294C155.296 110.016 155.663 109.877 156.068 109.877C156.36 109.877 156.583 109.909 156.738 109.973V111.135ZM163.581 113.78H158.639C158.657 114.56 158.867 115.161 159.268 115.585C159.669 116.009 160.22 116.221 160.922 116.221C161.71 116.221 162.435 115.961 163.096 115.441V116.494C162.48 116.941 161.667 117.164 160.655 117.164C159.666 117.164 158.889 116.847 158.324 116.214C157.759 115.576 157.477 114.68 157.477 113.527C157.477 112.438 157.784 111.552 158.399 110.868C159.019 110.18 159.787 109.836 160.703 109.836C161.619 109.836 162.328 110.132 162.829 110.725C163.33 111.317 163.581 112.14 163.581 113.192V113.78ZM162.433 112.83C162.428 112.183 162.271 111.679 161.961 111.319C161.656 110.959 161.229 110.779 160.683 110.779C160.154 110.779 159.705 110.968 159.336 111.347C158.967 111.725 158.739 112.219 158.652 112.83H162.433ZM169.275 117V107.197H171.982C175.437 107.197 177.164 108.79 177.164 111.976C177.164 113.489 176.683 114.705 175.722 115.626C174.765 116.542 173.482 117 171.873 117H169.275ZM170.424 108.236V115.961H171.887C173.172 115.961 174.172 115.617 174.888 114.929C175.603 114.241 175.961 113.265 175.961 112.003C175.961 109.492 174.626 108.236 171.955 108.236H170.424ZM184.567 113.78H179.625C179.643 114.56 179.853 115.161 180.254 115.585C180.655 116.009 181.206 116.221 181.908 116.221C182.697 116.221 183.421 115.961 184.082 115.441V116.494C183.467 116.941 182.653 117.164 181.642 117.164C180.653 117.164 179.876 116.847 179.311 116.214C178.745 115.576 178.463 114.68 178.463 113.527C178.463 112.438 178.771 111.552 179.386 110.868C180.006 110.18 180.773 109.836 181.689 109.836C182.605 109.836 183.314 110.132 183.815 110.725C184.317 111.317 184.567 112.14 184.567 113.192V113.78ZM183.419 112.83C183.414 112.183 183.257 111.679 182.947 111.319C182.642 110.959 182.216 110.779 181.669 110.779C181.14 110.779 180.691 110.968 180.322 111.347C179.953 111.725 179.725 112.219 179.639 112.83H183.419ZM185.846 116.747V115.544C186.456 115.995 187.129 116.221 187.862 116.221C188.847 116.221 189.339 115.893 189.339 115.236C189.339 115.049 189.296 114.892 189.209 114.765C189.127 114.632 189.013 114.516 188.867 114.416C188.726 114.316 188.557 114.227 188.361 114.149C188.17 114.067 187.963 113.983 187.739 113.896C187.429 113.773 187.156 113.65 186.919 113.527C186.687 113.4 186.491 113.258 186.331 113.104C186.176 112.944 186.058 112.764 185.976 112.563C185.898 112.363 185.859 112.128 185.859 111.859C185.859 111.531 185.935 111.242 186.085 110.991C186.235 110.736 186.436 110.524 186.687 110.355C186.937 110.182 187.222 110.052 187.541 109.966C187.865 109.879 188.197 109.836 188.539 109.836C189.145 109.836 189.688 109.941 190.166 110.15V111.285C189.651 110.948 189.059 110.779 188.389 110.779C188.179 110.779 187.99 110.804 187.821 110.854C187.653 110.9 187.507 110.966 187.384 111.053C187.265 111.139 187.172 111.244 187.104 111.367C187.04 111.486 187.008 111.618 187.008 111.764C187.008 111.946 187.04 112.099 187.104 112.222C187.172 112.345 187.27 112.454 187.397 112.55C187.525 112.646 187.68 112.732 187.862 112.81C188.045 112.887 188.252 112.971 188.484 113.062C188.794 113.181 189.072 113.304 189.318 113.432C189.564 113.555 189.774 113.696 189.947 113.855C190.12 114.01 190.253 114.19 190.344 114.396C190.439 114.601 190.487 114.844 190.487 115.127C190.487 115.473 190.41 115.774 190.255 116.029C190.104 116.285 189.902 116.496 189.646 116.665C189.391 116.834 189.097 116.959 188.765 117.041C188.432 117.123 188.083 117.164 187.719 117.164C186.999 117.164 186.374 117.025 185.846 116.747ZM198.027 117H196.455L193.365 113.637H193.338V117H192.217V106.637H193.338V113.206H193.365L196.305 110H197.774L194.527 113.377L198.027 117ZM202.423 116.932C202.159 117.077 201.81 117.15 201.377 117.15C200.151 117.15 199.538 116.467 199.538 115.1V110.957H198.335V110H199.538V108.291L200.659 107.929V110H202.423V110.957H200.659V114.901C200.659 115.371 200.739 115.706 200.898 115.906C201.058 116.107 201.322 116.207 201.691 116.207C201.974 116.207 202.218 116.13 202.423 115.975V116.932ZM206.846 117.164C205.811 117.164 204.984 116.838 204.364 116.187C203.749 115.53 203.441 114.662 203.441 113.582C203.441 112.406 203.763 111.488 204.405 110.827C205.048 110.166 205.916 109.836 207.01 109.836C208.053 109.836 208.867 110.157 209.45 110.8C210.038 111.442 210.332 112.333 210.332 113.473C210.332 114.589 210.015 115.485 209.382 116.159C208.753 116.829 207.908 117.164 206.846 117.164ZM206.928 110.779C206.208 110.779 205.638 111.025 205.219 111.518C204.799 112.005 204.59 112.68 204.59 113.541C204.59 114.37 204.802 115.024 205.226 115.503C205.649 115.981 206.217 116.221 206.928 116.221C207.652 116.221 208.208 115.986 208.596 115.517C208.988 115.047 209.184 114.38 209.184 113.514C209.184 112.639 208.988 111.964 208.596 111.49C208.208 111.016 207.652 110.779 206.928 110.779ZM213.271 115.988H213.244V120.22H212.123V110H213.244V111.23H213.271C213.823 110.301 214.63 109.836 215.691 109.836C216.594 109.836 217.298 110.15 217.804 110.779C218.31 111.404 218.562 112.242 218.562 113.295C218.562 114.466 218.278 115.405 217.708 116.111C217.138 116.813 216.359 117.164 215.37 117.164C214.463 117.164 213.764 116.772 213.271 115.988ZM213.244 113.165V114.143C213.244 114.721 213.431 115.214 213.805 115.619C214.183 116.02 214.661 116.221 215.24 116.221C215.919 116.221 216.45 115.961 216.833 115.441C217.22 114.922 217.414 114.2 217.414 113.274C217.414 112.495 217.234 111.884 216.874 111.442C216.514 111 216.026 110.779 215.411 110.779C214.759 110.779 214.235 111.007 213.839 111.463C213.442 111.914 213.244 112.481 213.244 113.165Z" fill="black"/>
-<rect x="102" y="78" width="3" height="3" fill="#4B003F"/>
-<path d="M241 78H244V81H241V78Z" fill="#4B003F"/>
-<rect x="103" y="79" width="140" height="1" fill="#4B003F"/>
-<path d="M102.65 92.6885V91.625C102.772 91.7324 102.917 91.8291 103.085 91.915C103.257 92.001 103.436 92.0744 103.622 92.1353C103.812 92.1925 104.002 92.2373 104.191 92.2695C104.381 92.3018 104.557 92.3179 104.718 92.3179C105.273 92.3179 105.686 92.2158 105.958 92.0117C106.234 91.804 106.372 91.5068 106.372 91.1201C106.372 90.9124 106.326 90.7316 106.232 90.5776C106.143 90.4237 106.018 90.284 105.856 90.1587C105.695 90.0298 105.504 89.908 105.282 89.7935C105.063 89.6753 104.827 89.5518 104.573 89.4229C104.304 89.2868 104.054 89.1489 103.821 89.0093C103.588 88.8696 103.386 88.7157 103.214 88.5474C103.042 88.3791 102.906 88.1893 102.806 87.978C102.709 87.7632 102.661 87.5125 102.661 87.2261C102.661 86.8752 102.738 86.5708 102.892 86.313C103.046 86.0516 103.248 85.8368 103.499 85.6685C103.749 85.5002 104.034 85.3748 104.353 85.2925C104.675 85.2101 105.002 85.1689 105.335 85.1689C106.095 85.1689 106.648 85.2603 106.995 85.4429V86.458C106.54 86.1429 105.957 85.9854 105.244 85.9854C105.047 85.9854 104.85 86.0068 104.653 86.0498C104.456 86.0892 104.281 86.1554 104.127 86.2485C103.973 86.3416 103.848 86.4616 103.751 86.6084C103.654 86.7552 103.606 86.9342 103.606 87.1455C103.606 87.3424 103.642 87.5125 103.713 87.6558C103.789 87.799 103.898 87.9297 104.041 88.0479C104.184 88.166 104.358 88.2806 104.562 88.3916C104.77 88.5026 105.008 88.6243 105.276 88.7568C105.552 88.8929 105.813 89.0361 106.061 89.1865C106.308 89.3369 106.524 89.5034 106.71 89.686C106.897 89.8687 107.043 90.071 107.151 90.293C107.262 90.515 107.317 90.7692 107.317 91.0557C107.317 91.4352 107.242 91.7575 107.092 92.0225C106.945 92.2839 106.744 92.4969 106.49 92.6616C106.24 92.8263 105.95 92.9445 105.62 93.0161C105.291 93.0913 104.943 93.1289 104.578 93.1289C104.456 93.1289 104.306 93.1182 104.127 93.0967C103.948 93.0788 103.765 93.0501 103.579 93.0107C103.393 92.9749 103.216 92.9302 103.047 92.8765C102.883 92.8192 102.75 92.7565 102.65 92.6885ZM111.034 93.1289C110.221 93.1289 109.571 92.8729 109.084 92.3608C108.601 91.8452 108.359 91.1631 108.359 90.3145C108.359 89.3906 108.612 88.6691 109.117 88.1499C109.622 87.6307 110.304 87.3711 111.163 87.3711C111.983 87.3711 112.622 87.6235 113.081 88.1284C113.542 88.6333 113.773 89.3333 113.773 90.2285C113.773 91.1058 113.525 91.8094 113.027 92.3394C112.533 92.8657 111.868 93.1289 111.034 93.1289ZM111.099 88.1123C110.533 88.1123 110.085 88.3057 109.756 88.6924C109.426 89.0755 109.262 89.6055 109.262 90.2822C109.262 90.9339 109.428 91.4478 109.761 91.8237C110.094 92.1997 110.54 92.3877 111.099 92.3877C111.668 92.3877 112.105 92.2033 112.409 91.8345C112.717 91.4657 112.871 90.9411 112.871 90.2607C112.871 89.5732 112.717 89.0433 112.409 88.6709C112.105 88.2985 111.668 88.1123 111.099 88.1123ZM117.898 85.6309C117.727 85.5342 117.531 85.4858 117.313 85.4858C116.697 85.4858 116.389 85.8743 116.389 86.6514V87.5H117.678V88.252H116.389V93H115.514V88.252H114.574V87.5H115.514V86.6084C115.514 86.0319 115.68 85.5771 116.013 85.2441C116.346 84.9076 116.762 84.7393 117.259 84.7393C117.528 84.7393 117.741 84.7715 117.898 84.8359V85.6309ZM121.18 92.9463C120.972 93.0609 120.699 93.1182 120.358 93.1182C119.395 93.1182 118.914 92.5811 118.914 91.5068V88.252H117.968V87.5H118.914V86.1572L119.794 85.8726V87.5H121.18V88.252H119.794V91.3511C119.794 91.7199 119.857 91.9831 119.982 92.1406C120.108 92.2982 120.315 92.377 120.605 92.377C120.827 92.377 121.019 92.3161 121.18 92.1943V92.9463ZM129.285 87.5L127.636 93H126.723L125.59 89.063C125.547 88.9126 125.518 88.7425 125.504 88.5527H125.482C125.472 88.6816 125.434 88.8481 125.37 89.0522L124.14 93H123.259L121.594 87.5H122.518L123.656 91.6357C123.692 91.7611 123.717 91.9258 123.731 92.1299H123.774C123.785 91.9723 123.817 91.804 123.871 91.625L125.139 87.5H125.944L127.083 91.6465C127.119 91.779 127.146 91.9437 127.164 92.1406H127.207C127.214 92.001 127.244 91.8363 127.298 91.6465L128.415 87.5H129.285ZM134.243 93H133.362V92.1406H133.34C132.957 92.7995 132.393 93.1289 131.648 93.1289C131.101 93.1289 130.671 92.9839 130.359 92.6938C130.051 92.4038 129.897 92.0189 129.897 91.5391C129.897 90.5114 130.503 89.9134 131.713 89.7451L133.362 89.5142C133.362 88.5796 132.984 88.1123 132.229 88.1123C131.566 88.1123 130.968 88.3379 130.435 88.7891V87.8867C130.975 87.543 131.598 87.3711 132.304 87.3711C133.596 87.3711 134.243 88.055 134.243 89.4229V93ZM133.362 90.2178L132.035 90.4004C131.627 90.4577 131.319 90.5597 131.111 90.7065C130.904 90.8498 130.8 91.1058 130.8 91.4746C130.8 91.7432 130.895 91.9634 131.084 92.1353C131.278 92.3035 131.534 92.3877 131.853 92.3877C132.289 92.3877 132.649 92.2355 132.932 91.9312C133.219 91.6232 133.362 91.2347 133.362 90.7656V90.2178ZM138.771 88.3916C138.617 88.2734 138.395 88.2144 138.104 88.2144C137.729 88.2144 137.413 88.3916 137.159 88.7461C136.909 89.1006 136.783 89.584 136.783 90.1963V93H135.902V87.5H136.783V88.6333H136.805C136.93 88.2466 137.122 87.9458 137.379 87.731C137.637 87.5125 137.925 87.4033 138.244 87.4033C138.473 87.4033 138.649 87.4284 138.771 87.4785V88.3916ZM144.147 90.4702H140.264C140.278 91.0825 140.443 91.5552 140.758 91.8882C141.073 92.2212 141.506 92.3877 142.058 92.3877C142.677 92.3877 143.246 92.1836 143.766 91.7754V92.6025C143.282 92.9535 142.643 93.1289 141.848 93.1289C141.071 93.1289 140.461 92.88 140.017 92.3823C139.573 91.881 139.351 91.1774 139.351 90.2715C139.351 89.4157 139.592 88.7192 140.076 88.1821C140.563 87.6414 141.166 87.3711 141.886 87.3711C142.605 87.3711 143.162 87.6038 143.556 88.0693C143.95 88.5348 144.147 89.1812 144.147 90.0083V90.4702ZM143.245 89.7236C143.241 89.2152 143.118 88.8195 142.874 88.5366C142.634 88.2537 142.299 88.1123 141.87 88.1123C141.454 88.1123 141.102 88.2609 140.812 88.5581C140.521 88.8553 140.342 89.2438 140.274 89.7236H143.245Z" fill="#4B003F"/>
-<path d="M277 126H-19V274H277V126Z" fill="#F3F2F1"/>
-<path d="M217 126H220V129H217V126Z" fill="#4B003F"/>
-<rect x="102" y="126" width="3" height="3" fill="#4B003F"/>
-<rect x="103" y="127" width="116" height="1" fill="#4B003F"/>
-<path d="M102.65 140.688V139.625C102.772 139.732 102.917 139.829 103.085 139.915C103.257 140.001 103.436 140.074 103.622 140.135C103.812 140.193 104.002 140.237 104.191 140.27C104.381 140.302 104.557 140.318 104.718 140.318C105.273 140.318 105.686 140.216 105.958 140.012C106.234 139.804 106.372 139.507 106.372 139.12C106.372 138.912 106.326 138.732 106.232 138.578C106.143 138.424 106.018 138.284 105.856 138.159C105.695 138.03 105.504 137.908 105.282 137.793C105.063 137.675 104.827 137.552 104.573 137.423C104.304 137.287 104.054 137.149 103.821 137.009C103.588 136.87 103.386 136.716 103.214 136.547C103.042 136.379 102.906 136.189 102.806 135.978C102.709 135.763 102.661 135.513 102.661 135.226C102.661 134.875 102.738 134.571 102.892 134.313C103.046 134.052 103.248 133.837 103.499 133.668C103.749 133.5 104.034 133.375 104.353 133.292C104.675 133.21 105.002 133.169 105.335 133.169C106.095 133.169 106.648 133.26 106.995 133.443V134.458C106.54 134.143 105.957 133.985 105.244 133.985C105.047 133.985 104.85 134.007 104.653 134.05C104.456 134.089 104.281 134.155 104.127 134.249C103.973 134.342 103.848 134.462 103.751 134.608C103.654 134.755 103.606 134.934 103.606 135.146C103.606 135.342 103.642 135.513 103.713 135.656C103.789 135.799 103.898 135.93 104.041 136.048C104.184 136.166 104.358 136.281 104.562 136.392C104.77 136.503 105.008 136.624 105.276 136.757C105.552 136.893 105.813 137.036 106.061 137.187C106.308 137.337 106.524 137.503 106.71 137.686C106.897 137.869 107.043 138.071 107.151 138.293C107.262 138.515 107.317 138.769 107.317 139.056C107.317 139.435 107.242 139.757 107.092 140.022C106.945 140.284 106.744 140.497 106.49 140.662C106.24 140.826 105.95 140.944 105.62 141.016C105.291 141.091 104.943 141.129 104.578 141.129C104.456 141.129 104.306 141.118 104.127 141.097C103.948 141.079 103.765 141.05 103.579 141.011C103.393 140.975 103.216 140.93 103.047 140.876C102.883 140.819 102.75 140.757 102.65 140.688ZM111.034 141.129C110.221 141.129 109.571 140.873 109.084 140.361C108.601 139.845 108.359 139.163 108.359 138.314C108.359 137.391 108.612 136.669 109.117 136.15C109.622 135.631 110.304 135.371 111.163 135.371C111.983 135.371 112.622 135.624 113.081 136.128C113.542 136.633 113.773 137.333 113.773 138.229C113.773 139.106 113.525 139.809 113.027 140.339C112.533 140.866 111.868 141.129 111.034 141.129ZM111.099 136.112C110.533 136.112 110.085 136.306 109.756 136.692C109.426 137.076 109.262 137.605 109.262 138.282C109.262 138.934 109.428 139.448 109.761 139.824C110.094 140.2 110.54 140.388 111.099 140.388C111.668 140.388 112.105 140.203 112.409 139.834C112.717 139.466 112.871 138.941 112.871 138.261C112.871 137.573 112.717 137.043 112.409 136.671C112.105 136.299 111.668 136.112 111.099 136.112ZM117.898 133.631C117.727 133.534 117.531 133.486 117.313 133.486C116.697 133.486 116.389 133.874 116.389 134.651V135.5H117.678V136.252H116.389V141H115.514V136.252H114.574V135.5H115.514V134.608C115.514 134.032 115.68 133.577 116.013 133.244C116.346 132.908 116.762 132.739 117.259 132.739C117.528 132.739 117.741 132.771 117.898 132.836V133.631ZM121.18 140.946C120.972 141.061 120.699 141.118 120.358 141.118C119.395 141.118 118.914 140.581 118.914 139.507V136.252H117.968V135.5H118.914V134.157L119.794 133.873V135.5H121.18V136.252H119.794V139.351C119.794 139.72 119.857 139.983 119.982 140.141C120.108 140.298 120.315 140.377 120.605 140.377C120.827 140.377 121.019 140.316 121.18 140.194V140.946ZM129.285 135.5L127.636 141H126.723L125.59 137.063C125.547 136.913 125.518 136.743 125.504 136.553H125.482C125.472 136.682 125.434 136.848 125.37 137.052L124.14 141H123.259L121.594 135.5H122.518L123.656 139.636C123.692 139.761 123.717 139.926 123.731 140.13H123.774C123.785 139.972 123.817 139.804 123.871 139.625L125.139 135.5H125.944L127.083 139.646C127.119 139.779 127.146 139.944 127.164 140.141H127.207C127.214 140.001 127.244 139.836 127.298 139.646L128.415 135.5H129.285ZM134.243 141H133.362V140.141H133.34C132.957 140.799 132.393 141.129 131.648 141.129C131.101 141.129 130.671 140.984 130.359 140.694C130.051 140.404 129.897 140.019 129.897 139.539C129.897 138.511 130.503 137.913 131.713 137.745L133.362 137.514C133.362 136.58 132.984 136.112 132.229 136.112C131.566 136.112 130.968 136.338 130.435 136.789V135.887C130.975 135.543 131.598 135.371 132.304 135.371C133.596 135.371 134.243 136.055 134.243 137.423V141ZM133.362 138.218L132.035 138.4C131.627 138.458 131.319 138.56 131.111 138.707C130.904 138.85 130.8 139.106 130.8 139.475C130.8 139.743 130.895 139.963 131.084 140.135C131.278 140.304 131.534 140.388 131.853 140.388C132.289 140.388 132.649 140.236 132.932 139.931C133.219 139.623 133.362 139.235 133.362 138.766V138.218ZM138.771 136.392C138.617 136.273 138.395 136.214 138.104 136.214C137.729 136.214 137.413 136.392 137.159 136.746C136.909 137.101 136.783 137.584 136.783 138.196V141H135.902V135.5H136.783V136.633H136.805C136.93 136.247 137.122 135.946 137.379 135.731C137.637 135.513 137.925 135.403 138.244 135.403C138.473 135.403 138.649 135.428 138.771 135.479V136.392ZM144.147 138.47H140.264C140.278 139.083 140.443 139.555 140.758 139.888C141.073 140.221 141.506 140.388 142.058 140.388C142.677 140.388 143.246 140.184 143.766 139.775V140.603C143.282 140.953 142.643 141.129 141.848 141.129C141.071 141.129 140.461 140.88 140.017 140.382C139.573 139.881 139.351 139.177 139.351 138.271C139.351 137.416 139.592 136.719 140.076 136.182C140.563 135.641 141.166 135.371 141.886 135.371C142.605 135.371 143.162 135.604 143.556 136.069C143.95 136.535 144.147 137.181 144.147 138.008V138.47ZM143.245 137.724C143.241 137.215 143.118 136.819 142.874 136.537C142.634 136.254 142.299 136.112 141.87 136.112C141.454 136.112 141.102 136.261 140.812 136.558C140.521 136.855 140.342 137.244 140.274 137.724H143.245Z" fill="#4B003F"/>
-<path d="M21.9375 36H20.9609L19.7891 34.0371C19.6816 33.8548 19.5775 33.7002 19.4766 33.5732C19.3757 33.443 19.2715 33.3372 19.1641 33.2559C19.0599 33.1745 18.946 33.1159 18.8223 33.0801C18.7018 33.041 18.5651 33.0215 18.4121 33.0215H17.7383V36H16.918V28.998H19.0078C19.3138 28.998 19.5954 29.0371 19.8525 29.1152C20.113 29.1901 20.3376 29.3057 20.5264 29.4619C20.7184 29.6182 20.8682 29.8135 20.9756 30.0479C21.083 30.279 21.1367 30.5508 21.1367 30.8633C21.1367 31.1074 21.0993 31.332 21.0244 31.5371C20.9528 31.7389 20.8486 31.9196 20.7119 32.0791C20.5785 32.2386 20.4157 32.3753 20.2236 32.4893C20.0348 32.5999 19.8216 32.6862 19.584 32.748V32.7676C19.7012 32.8197 19.8021 32.8799 19.8867 32.9482C19.9746 33.0133 20.0576 33.0915 20.1357 33.1826C20.2139 33.2738 20.2904 33.3779 20.3652 33.4951C20.4434 33.609 20.5296 33.7425 20.624 33.8955L21.9375 36ZM17.7383 29.7402V32.2793H18.8516C19.0566 32.2793 19.2454 32.2484 19.418 32.1865C19.5938 32.1247 19.7451 32.0368 19.8721 31.9229C19.999 31.8057 20.0983 31.6641 20.1699 31.498C20.2415 31.3288 20.2773 31.14 20.2773 30.9316C20.2773 30.5573 20.1553 30.266 19.9111 30.0576C19.6702 29.846 19.3203 29.7402 18.8613 29.7402H17.7383ZM26.6152 36H22.9043V28.998H26.459V29.7402H23.7246V32.0693H26.2539V32.8066H23.7246V35.2578H26.6152V36ZM32.1035 29.7402H30.082V36H29.2617V29.7402H27.2451V28.998H32.1035V29.7402ZM38.3291 33.168C38.3291 35.1341 37.4421 36.1172 35.668 36.1172C33.9688 36.1172 33.1191 35.1715 33.1191 33.2803V28.998H33.9395V33.2266C33.9395 34.6621 34.5449 35.3799 35.7559 35.3799C36.9245 35.3799 37.5088 34.6865 37.5088 33.2998V28.998H38.3291V33.168ZM45.1016 36H44.125L42.9531 34.0371C42.8457 33.8548 42.7415 33.7002 42.6406 33.5732C42.5397 33.443 42.4355 33.3372 42.3281 33.2559C42.224 33.1745 42.11 33.1159 41.9863 33.0801C41.8659 33.041 41.7292 33.0215 41.5762 33.0215H40.9023V36H40.082V28.998H42.1719C42.4779 28.998 42.7594 29.0371 43.0166 29.1152C43.277 29.1901 43.5016 29.3057 43.6904 29.4619C43.8825 29.6182 44.0322 29.8135 44.1396 30.0479C44.2471 30.279 44.3008 30.5508 44.3008 30.8633C44.3008 31.1074 44.2633 31.332 44.1885 31.5371C44.1169 31.7389 44.0127 31.9196 43.876 32.0791C43.7425 32.2386 43.5798 32.3753 43.3877 32.4893C43.1989 32.5999 42.9857 32.6862 42.748 32.748V32.7676C42.8652 32.8197 42.9661 32.8799 43.0508 32.9482C43.1387 33.0133 43.2217 33.0915 43.2998 33.1826C43.3779 33.2738 43.4544 33.3779 43.5293 33.4951C43.6074 33.609 43.6937 33.7425 43.7881 33.8955L45.1016 36ZM40.9023 29.7402V32.2793H42.0156C42.2207 32.2793 42.4095 32.2484 42.582 32.1865C42.7578 32.1247 42.9092 32.0368 43.0361 31.9229C43.1631 31.8057 43.2624 31.6641 43.334 31.498C43.4056 31.3288 43.4414 31.14 43.4414 30.9316C43.4414 30.5573 43.3193 30.266 43.0752 30.0576C42.8343 29.846 42.4844 29.7402 42.0254 29.7402H40.9023ZM51.7129 36H50.707L47.1035 30.4189C47.0124 30.279 46.9375 30.1325 46.8789 29.9795H46.8496C46.8757 30.1292 46.8887 30.4499 46.8887 30.9414V36H46.0684V28.998H47.1328L50.6387 34.4912C50.7852 34.7191 50.8796 34.8753 50.9219 34.96H50.9414C50.9089 34.7581 50.8926 34.4147 50.8926 33.9297V28.998H51.7129V36ZM57.2598 36H53.5488V28.998H57.1035V29.7402H54.3691V32.0693H56.8984V32.8066H54.3691V35.2578H57.2598V36ZM58.6074 36V28.998H60.541C63.0085 28.998 64.2422 30.1357 64.2422 32.4111C64.2422 33.4919 63.8988 34.361 63.2119 35.0186C62.5283 35.6729 61.612 36 60.4629 36H58.6074ZM59.4277 29.7402V35.2578H60.4727C61.3906 35.2578 62.1051 35.012 62.6162 34.5205C63.1273 34.029 63.3828 33.3324 63.3828 32.4307C63.3828 30.637 62.429 29.7402 60.5215 29.7402H59.4277ZM72.0742 36H68.3633V28.998H71.918V29.7402H69.1836V32.0693H71.7129V32.8066H69.1836V35.2578H72.0742V36ZM79.0664 36H78.0605L74.457 30.4189C74.3659 30.279 74.291 30.1325 74.2324 29.9795H74.2031C74.2292 30.1292 74.2422 30.4499 74.2422 30.9414V36H73.4219V28.998H74.4863L77.9922 34.4912C78.1387 34.7191 78.2331 34.8753 78.2754 34.96H78.2949C78.2624 34.7581 78.2461 34.4147 78.2461 33.9297V28.998H79.0664V36ZM85.043 29.7402H83.0215V36H82.2012V29.7402H80.1846V28.998H85.043V29.7402ZM86.9668 36H86.1465V28.998H86.9668V36ZM92.9531 29.7402H90.9316V36H90.1113V29.7402H88.0947V28.998H92.9531V29.7402ZM94.877 36H94.0566V28.998H94.877V36ZM100.434 36H96.7227V28.998H100.277V29.7402H97.543V32.0693H100.072V32.8066H97.543V35.2578H100.434V36ZM101.454 35.7168V34.75C101.565 34.8477 101.697 34.9355 101.85 35.0137C102.006 35.0918 102.169 35.1585 102.338 35.2139C102.51 35.266 102.683 35.3066 102.855 35.3359C103.028 35.3652 103.188 35.3799 103.334 35.3799C103.839 35.3799 104.215 35.2871 104.462 35.1016C104.713 34.9128 104.838 34.6426 104.838 34.291C104.838 34.1022 104.796 33.9378 104.711 33.7979C104.63 33.6579 104.516 33.5309 104.369 33.417C104.223 33.2998 104.049 33.1891 103.847 33.085C103.648 32.9775 103.433 32.8652 103.202 32.748C102.958 32.6243 102.73 32.499 102.519 32.3721C102.307 32.2451 102.123 32.1051 101.967 31.9521C101.811 31.7992 101.687 31.6266 101.596 31.4346C101.508 31.2393 101.464 31.0114 101.464 30.751C101.464 30.432 101.534 30.1553 101.674 29.9209C101.814 29.6833 101.998 29.488 102.226 29.335C102.453 29.182 102.712 29.068 103.002 28.9932C103.295 28.9183 103.593 28.8809 103.896 28.8809C104.586 28.8809 105.089 28.9639 105.404 29.1299V30.0527C104.991 29.7663 104.46 29.623 103.812 29.623C103.633 29.623 103.454 29.6426 103.275 29.6816C103.096 29.7174 102.937 29.7777 102.797 29.8623C102.657 29.9469 102.543 30.056 102.455 30.1895C102.367 30.3229 102.323 30.4857 102.323 30.6777C102.323 30.8568 102.356 31.0114 102.421 31.1416C102.489 31.2718 102.589 31.3906 102.719 31.498C102.849 31.6055 103.007 31.7096 103.192 31.8105C103.381 31.9115 103.598 32.0221 103.842 32.1426C104.092 32.2663 104.33 32.3965 104.555 32.5332C104.779 32.6699 104.976 32.8213 105.146 32.9873C105.315 33.1533 105.448 33.3372 105.546 33.5391C105.647 33.7409 105.697 33.972 105.697 34.2324C105.697 34.5775 105.629 34.8704 105.492 35.1113C105.359 35.349 105.176 35.5426 104.945 35.6924C104.717 35.8421 104.454 35.9495 104.154 36.0146C103.855 36.083 103.539 36.1172 103.207 36.1172C103.096 36.1172 102.96 36.1074 102.797 36.0879C102.634 36.0716 102.468 36.0456 102.299 36.0098C102.13 35.9772 101.968 35.9365 101.815 35.8877C101.666 35.8356 101.545 35.7786 101.454 35.7168Z" fill="#323130"/>
-</g>
-<defs>
-<clipPath id="clip0_858_39236">
-<rect width="289" height="167" fill="white"/>
-</clipPath>
-</defs>
-</svg>
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "分離オーバーラップ例1パート2のSVGファイルの削除"
}
```

### Explanation
この変更では、`separated-overlap-example-1-part-2.svg`というSVG形式の画像ファイルが削除されました。このファイルは、カスタムテキスト分析サービスにおける特定の例や概念を視覚的に示すために使用されていたと想像されます。

削除されたSVGファイルは、技術的な説明や手順を補足するための重要なビジュアルリソースであり、その内容を理解しやすくする役割を果たしていました。この画像が失われることで、ユーザーは分離オーバーラップの概念や、サービスにおけるその適用方法を視覚的に参照することができなくなります。

特に、この種の技術的な情報を扱うユーザーにとって、イメージや図解は非常に重要ですので、情報伝達にキーポイントの欠落が生じる可能性があります。そのため、この削除に際しては、関連するテキスト説明や代替資料を用意することが望ましいです。GitHubのリポジトリでは、詳細な変更点や影響について確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/separated-overlap-example-1.svg{#item-68315c}

<details>
<summary>Diff</summary>
````diff
@@ -1,14 +0,0 @@
-<svg width="289" height="148" viewBox="0 0 289 148" fill="none"
-    xmlns="http://www.w3.org/2000/svg">
-    <path d="M296 0H0V148H296V0Z" fill="#F3F2F1"/>
-    <path d="M18.4336 70H17.2852V60.1973H18.4336V70ZM33.5273 63L31.4287 70H30.2666L28.8242 64.9893C28.7695 64.7979 28.7331 64.5814 28.7148 64.3398H28.6875C28.6738 64.5039 28.626 64.7158 28.5439 64.9756L26.9785 70H25.8574L23.7383 63H24.9141L26.3633 68.2637C26.4089 68.4232 26.4408 68.6328 26.459 68.8926H26.5137C26.5273 68.6921 26.5684 68.4779 26.6367 68.25L28.25 63H29.2754L30.7246 68.2773C30.7702 68.446 30.8044 68.6556 30.8271 68.9062H30.8818C30.891 68.7285 30.9297 68.5189 30.998 68.2773L32.4199 63H33.5273ZM39.8369 70H38.7158V68.9062H38.6885C38.2008 69.7448 37.4831 70.1641 36.5352 70.1641C35.8379 70.1641 35.291 69.9795 34.8945 69.6104C34.5026 69.2412 34.3066 68.7513 34.3066 68.1406C34.3066 66.8327 35.0768 66.0716 36.6172 65.8574L38.7158 65.5635C38.7158 64.374 38.235 63.7793 37.2734 63.7793C36.4303 63.7793 35.6693 64.0664 34.9902 64.6406V63.4922C35.6784 63.0547 36.4714 62.8359 37.3691 62.8359C39.0143 62.8359 39.8369 63.7064 39.8369 65.4473V70ZM38.7158 66.459L37.0273 66.6914C36.5078 66.7643 36.1159 66.8942 35.8516 67.0811C35.5872 67.2633 35.4551 67.5892 35.4551 68.0586C35.4551 68.4004 35.5758 68.6807 35.8174 68.8994C36.0635 69.1136 36.3893 69.2207 36.7949 69.2207C37.3509 69.2207 37.8089 69.027 38.1689 68.6396C38.5335 68.2477 38.7158 67.7533 38.7158 67.1562V66.459ZM47.7598 70H46.6387V66.0078C46.6387 64.5221 46.0964 63.7793 45.0117 63.7793C44.4512 63.7793 43.9863 63.9912 43.6172 64.415C43.2526 64.8343 43.0703 65.3652 43.0703 66.0078V70H41.9492V63H43.0703V64.1621H43.0977C43.6263 63.278 44.3919 62.8359 45.3945 62.8359C46.1602 62.8359 46.7458 63.0843 47.1514 63.5811C47.557 64.0732 47.7598 64.7865 47.7598 65.7207V70ZM53.126 69.9316C52.8617 70.0775 52.513 70.1504 52.0801 70.1504C50.8542 70.1504 50.2412 69.4668 50.2412 68.0996V63.957H49.0381V63H50.2412V61.291L51.3623 60.9287V63H53.126V63.957H51.3623V67.9014C51.3623 68.3708 51.4421 68.7057 51.6016 68.9062C51.7611 69.1068 52.0254 69.207 52.3945 69.207C52.6771 69.207 52.9209 69.1296 53.126 68.9746V69.9316ZM61.7119 69.9316C61.4476 70.0775 61.099 70.1504 60.666 70.1504C59.4401 70.1504 58.8271 69.4668 58.8271 68.0996V63.957H57.624V63H58.8271V61.291L59.9482 60.9287V63H61.7119V63.957H59.9482V67.9014C59.9482 68.3708 60.028 68.7057 60.1875 68.9062C60.347 69.1068 60.6113 69.207 60.9805 69.207C61.263 69.207 61.5068 69.1296 61.7119 68.9746V69.9316ZM66.1348 70.1641C65.1003 70.1641 64.2731 69.8382 63.6533 69.1865C63.0381 68.5303 62.7305 67.6621 62.7305 66.582C62.7305 65.4062 63.0518 64.488 63.6943 63.8271C64.3369 63.1663 65.2051 62.8359 66.2988 62.8359C67.3424 62.8359 68.1559 63.1572 68.7393 63.7998C69.3271 64.4424 69.6211 65.3333 69.6211 66.4727C69.6211 67.5892 69.3044 68.4847 68.6709 69.1592C68.042 69.8291 67.1966 70.1641 66.1348 70.1641ZM66.2168 63.7793C65.4967 63.7793 64.9271 64.0254 64.5078 64.5176C64.0885 65.0052 63.8789 65.6797 63.8789 66.541C63.8789 67.3704 64.0908 68.0244 64.5146 68.5029C64.9385 68.9814 65.5059 69.2207 66.2168 69.2207C66.9414 69.2207 67.4974 68.986 67.8848 68.5166C68.2767 68.0472 68.4727 67.3796 68.4727 66.5137C68.4727 65.6387 68.2767 64.9642 67.8848 64.4902C67.4974 64.0163 66.9414 63.7793 66.2168 63.7793ZM76.4023 68.9883H76.375V70H75.2539V59.6367H76.375V64.2305H76.4023C76.9538 63.3008 77.7604 62.8359 78.8223 62.8359C79.7201 62.8359 80.4219 63.1504 80.9277 63.7793C81.4382 64.4036 81.6934 65.2422 81.6934 66.2949C81.6934 67.4661 81.4085 68.4049 80.8389 69.1113C80.2692 69.8132 79.4899 70.1641 78.501 70.1641C77.5758 70.1641 76.8763 69.7721 76.4023 68.9883ZM76.375 66.165V67.1426C76.375 67.7214 76.5618 68.2135 76.9355 68.6191C77.3138 69.0202 77.7923 69.2207 78.3711 69.2207C79.0501 69.2207 79.5811 68.9609 79.9639 68.4414C80.3512 67.9219 80.5449 67.1995 80.5449 66.2744C80.5449 65.4951 80.3649 64.8844 80.0049 64.4424C79.6449 64.0003 79.1572 63.7793 78.542 63.7793C77.8903 63.7793 77.3662 64.0072 76.9697 64.4629C76.5732 64.9141 76.375 65.4814 76.375 66.165ZM89.1445 70H88.0234V68.8926H87.9961C87.5312 69.7402 86.8112 70.1641 85.8359 70.1641C84.168 70.1641 83.334 69.1706 83.334 67.1836V63H84.4482V67.0059C84.4482 68.4824 85.0133 69.2207 86.1436 69.2207C86.6904 69.2207 87.1393 69.0202 87.4902 68.6191C87.8457 68.2135 88.0234 67.6849 88.0234 67.0332V63H89.1445V70ZM96.9854 63L93.7656 71.1211C93.1914 72.5703 92.3848 73.2949 91.3457 73.2949C91.054 73.2949 90.8102 73.2653 90.6143 73.2061V72.2012C90.8558 72.2832 91.0768 72.3242 91.2773 72.3242C91.8424 72.3242 92.2663 71.987 92.5488 71.3125L93.1094 69.9863L90.375 63H91.6191L93.5127 68.3867C93.5355 68.4551 93.5833 68.6328 93.6562 68.9199H93.6973C93.7201 68.8105 93.7656 68.6374 93.834 68.4004L95.8232 63H96.9854ZM103.336 66.2949V70H102.188V60.1973H104.881C105.929 60.1973 106.74 60.4525 107.314 60.9629C107.893 61.4733 108.183 62.1934 108.183 63.123C108.183 64.0527 107.861 64.8138 107.219 65.4062C106.581 65.9987 105.717 66.2949 104.628 66.2949H103.336ZM103.336 61.2363V65.2559H104.539C105.332 65.2559 105.936 65.0758 106.351 64.7158C106.77 64.3512 106.979 63.8385 106.979 63.1777C106.979 61.8835 106.214 61.2363 104.683 61.2363H103.336ZM113.535 64.1348C113.339 63.9844 113.057 63.9092 112.688 63.9092C112.209 63.9092 111.808 64.1348 111.484 64.5859C111.165 65.0371 111.006 65.6523 111.006 66.4316V70H109.885V63H111.006V64.4424H111.033C111.193 63.9502 111.437 63.5674 111.765 63.2939C112.093 63.016 112.46 62.877 112.865 62.877C113.157 62.877 113.38 62.9089 113.535 62.9727V64.1348ZM117.678 70.1641C116.643 70.1641 115.816 69.8382 115.196 69.1865C114.581 68.5303 114.273 67.6621 114.273 66.582C114.273 65.4062 114.595 64.488 115.237 63.8271C115.88 63.1663 116.748 62.8359 117.842 62.8359C118.885 62.8359 119.699 63.1572 120.282 63.7998C120.87 64.4424 121.164 65.3333 121.164 66.4727C121.164 67.5892 120.847 68.4847 120.214 69.1592C119.585 69.8291 118.74 70.1641 117.678 70.1641ZM117.76 63.7793C117.04 63.7793 116.47 64.0254 116.051 64.5176C115.632 65.0052 115.422 65.6797 115.422 66.541C115.422 67.3704 115.634 68.0244 116.058 68.5029C116.481 68.9814 117.049 69.2207 117.76 69.2207C118.484 69.2207 119.04 68.986 119.428 68.5166C119.82 68.0472 120.016 67.3796 120.016 66.5137C120.016 65.6387 119.82 64.9642 119.428 64.4902C119.04 64.0163 118.484 63.7793 117.76 63.7793ZM122.531 69.7471V68.5439C123.142 68.9951 123.814 69.2207 124.548 69.2207C125.532 69.2207 126.024 68.8926 126.024 68.2363C126.024 68.0495 125.981 67.8923 125.895 67.7646C125.812 67.6325 125.699 67.5163 125.553 67.416C125.411 67.3158 125.243 67.2269 125.047 67.1494C124.855 67.0674 124.648 66.9831 124.425 66.8965C124.115 66.7734 123.841 66.6504 123.604 66.5273C123.372 66.3997 123.176 66.2585 123.017 66.1035C122.862 65.944 122.743 65.764 122.661 65.5635C122.584 65.363 122.545 65.1283 122.545 64.8594C122.545 64.5312 122.62 64.2419 122.771 63.9912C122.921 63.736 123.121 63.5241 123.372 63.3555C123.623 63.1823 123.908 63.0524 124.227 62.9658C124.55 62.8792 124.883 62.8359 125.225 62.8359C125.831 62.8359 126.373 62.9408 126.852 63.1504V64.2852C126.337 63.9479 125.744 63.7793 125.074 63.7793C124.865 63.7793 124.675 63.8044 124.507 63.8545C124.338 63.9001 124.192 63.9661 124.069 64.0527C123.951 64.1393 123.857 64.2441 123.789 64.3672C123.725 64.4857 123.693 64.6178 123.693 64.7637C123.693 64.946 123.725 65.0986 123.789 65.2217C123.857 65.3447 123.955 65.4541 124.083 65.5498C124.211 65.6455 124.366 65.7321 124.548 65.8096C124.73 65.887 124.938 65.9714 125.17 66.0625C125.48 66.181 125.758 66.304 126.004 66.4316C126.25 66.5547 126.46 66.696 126.633 66.8555C126.806 67.0104 126.938 67.1904 127.029 67.3955C127.125 67.6006 127.173 67.8444 127.173 68.127C127.173 68.4733 127.095 68.7741 126.94 69.0293C126.79 69.2845 126.587 69.4964 126.332 69.665C126.077 69.8337 125.783 69.959 125.45 70.041C125.118 70.123 124.769 70.1641 124.404 70.1641C123.684 70.1641 123.06 70.0251 122.531 69.7471ZM134.528 66.7803H129.586C129.604 67.5596 129.814 68.1611 130.215 68.585C130.616 69.0088 131.167 69.2207 131.869 69.2207C132.658 69.2207 133.382 68.9609 134.043 68.4414V69.4941C133.428 69.9408 132.614 70.1641 131.603 70.1641C130.614 70.1641 129.837 69.8473 129.271 69.2139C128.706 68.5758 128.424 67.6803 128.424 66.5273C128.424 65.4382 128.731 64.5518 129.347 63.8682C129.966 63.18 130.734 62.8359 131.65 62.8359C132.566 62.8359 133.275 63.1322 133.776 63.7246C134.278 64.3171 134.528 65.1396 134.528 66.1924V66.7803ZM133.38 65.8301C133.375 65.1829 133.218 64.6794 132.908 64.3193C132.603 63.9593 132.177 63.7793 131.63 63.7793C131.101 63.7793 130.652 63.9684 130.283 64.3467C129.914 64.7249 129.686 65.2194 129.6 65.8301H133.38ZM145.049 63L142.95 70H141.788L140.346 64.9893C140.291 64.7979 140.255 64.5814 140.236 64.3398H140.209C140.195 64.5039 140.147 64.7158 140.065 64.9756L138.5 70H137.379L135.26 63H136.436L137.885 68.2637C137.93 68.4232 137.962 68.6328 137.98 68.8926H138.035C138.049 68.6921 138.09 68.4779 138.158 68.25L139.771 63H140.797L142.246 68.2773C142.292 68.446 142.326 68.6556 142.349 68.9062H142.403C142.412 68.7285 142.451 68.5189 142.52 68.2773L143.941 63H145.049ZM151.358 70H150.237V68.9062H150.21C149.722 69.7448 149.005 70.1641 148.057 70.1641C147.359 70.1641 146.812 69.9795 146.416 69.6104C146.024 69.2412 145.828 68.7513 145.828 68.1406C145.828 66.8327 146.598 66.0716 148.139 65.8574L150.237 65.5635C150.237 64.374 149.757 63.7793 148.795 63.7793C147.952 63.7793 147.191 64.0664 146.512 64.6406V63.4922C147.2 63.0547 147.993 62.8359 148.891 62.8359C150.536 62.8359 151.358 63.7064 151.358 65.4473V70ZM150.237 66.459L148.549 66.6914C148.029 66.7643 147.637 66.8942 147.373 67.0811C147.109 67.2633 146.977 67.5892 146.977 68.0586C146.977 68.4004 147.097 68.6807 147.339 68.8994C147.585 69.1136 147.911 69.2207 148.316 69.2207C148.872 69.2207 149.33 69.027 149.69 68.6396C150.055 68.2477 150.237 67.7533 150.237 67.1562V66.459ZM157.121 64.1348C156.925 63.9844 156.643 63.9092 156.273 63.9092C155.795 63.9092 155.394 64.1348 155.07 64.5859C154.751 65.0371 154.592 65.6523 154.592 66.4316V70H153.471V63H154.592V64.4424H154.619C154.779 63.9502 155.022 63.5674 155.351 63.2939C155.679 63.016 156.046 62.877 156.451 62.877C156.743 62.877 156.966 62.9089 157.121 62.9727V64.1348ZM163.964 66.7803H159.021C159.04 67.5596 159.249 68.1611 159.65 68.585C160.051 69.0088 160.603 69.2207 161.305 69.2207C162.093 69.2207 162.818 68.9609 163.479 68.4414V69.4941C162.863 69.9408 162.05 70.1641 161.038 70.1641C160.049 70.1641 159.272 69.8473 158.707 69.2139C158.142 68.5758 157.859 67.6803 157.859 66.5273C157.859 65.4382 158.167 64.5518 158.782 63.8682C159.402 63.18 160.17 62.8359 161.086 62.8359C162.002 62.8359 162.711 63.1322 163.212 63.7246C163.713 64.3171 163.964 65.1396 163.964 66.1924V66.7803ZM162.815 65.8301C162.811 65.1829 162.654 64.6794 162.344 64.3193C162.038 63.9593 161.612 63.7793 161.065 63.7793C160.537 63.7793 160.088 63.9684 159.719 64.3467C159.35 64.7249 159.122 65.2194 159.035 65.8301H162.815ZM169.658 70V60.1973H172.365C175.82 60.1973 177.547 61.79 177.547 64.9756C177.547 66.4886 177.066 67.7054 176.104 68.626C175.147 69.542 173.865 70 172.256 70H169.658ZM170.807 61.2363V68.9609H172.27C173.555 68.9609 174.555 68.6169 175.271 67.9287C175.986 67.2406 176.344 66.2653 176.344 65.0029C176.344 62.4919 175.008 61.2363 172.338 61.2363H170.807ZM184.95 66.7803H180.008C180.026 67.5596 180.236 68.1611 180.637 68.585C181.038 69.0088 181.589 69.2207 182.291 69.2207C183.079 69.2207 183.804 68.9609 184.465 68.4414V69.4941C183.85 69.9408 183.036 70.1641 182.024 70.1641C181.035 70.1641 180.258 69.8473 179.693 69.2139C179.128 68.5758 178.846 67.6803 178.846 66.5273C178.846 65.4382 179.153 64.5518 179.769 63.8682C180.388 63.18 181.156 62.8359 182.072 62.8359C182.988 62.8359 183.697 63.1322 184.198 63.7246C184.7 64.3171 184.95 65.1396 184.95 66.1924V66.7803ZM183.802 65.8301C183.797 65.1829 183.64 64.6794 183.33 64.3193C183.025 63.9593 182.599 63.7793 182.052 63.7793C181.523 63.7793 181.074 63.9684 180.705 64.3467C180.336 64.7249 180.108 65.2194 180.021 65.8301H183.802ZM186.229 69.7471V68.5439C186.839 68.9951 187.511 69.2207 188.245 69.2207C189.229 69.2207 189.722 68.8926 189.722 68.2363C189.722 68.0495 189.678 67.8923 189.592 67.7646C189.51 67.6325 189.396 67.5163 189.25 67.416C189.109 67.3158 188.94 67.2269 188.744 67.1494C188.553 67.0674 188.345 66.9831 188.122 66.8965C187.812 66.7734 187.539 66.6504 187.302 66.5273C187.069 66.3997 186.873 66.2585 186.714 66.1035C186.559 65.944 186.44 65.764 186.358 65.5635C186.281 65.363 186.242 65.1283 186.242 64.8594C186.242 64.5312 186.317 64.2419 186.468 63.9912C186.618 63.736 186.819 63.5241 187.069 63.3555C187.32 63.1823 187.605 63.0524 187.924 62.9658C188.247 62.8792 188.58 62.8359 188.922 62.8359C189.528 62.8359 190.07 62.9408 190.549 63.1504V64.2852C190.034 63.9479 189.441 63.7793 188.771 63.7793C188.562 63.7793 188.373 63.8044 188.204 63.8545C188.035 63.9001 187.89 63.9661 187.767 64.0527C187.648 64.1393 187.555 64.2441 187.486 64.3672C187.423 64.4857 187.391 64.6178 187.391 64.7637C187.391 64.946 187.423 65.0986 187.486 65.2217C187.555 65.3447 187.653 65.4541 187.78 65.5498C187.908 65.6455 188.063 65.7321 188.245 65.8096C188.427 65.887 188.635 65.9714 188.867 66.0625C189.177 66.181 189.455 66.304 189.701 66.4316C189.947 66.5547 190.157 66.696 190.33 66.8555C190.503 67.0104 190.635 67.1904 190.727 67.3955C190.822 67.6006 190.87 67.8444 190.87 68.127C190.87 68.4733 190.793 68.7741 190.638 69.0293C190.487 69.2845 190.285 69.4964 190.029 69.665C189.774 69.8337 189.48 69.959 189.147 70.041C188.815 70.123 188.466 70.1641 188.102 70.1641C187.382 70.1641 186.757 70.0251 186.229 69.7471ZM198.41 70H196.838L193.748 66.6367H193.721V70H192.6V59.6367H193.721V66.2061H193.748L196.688 63H198.157L194.91 66.377L198.41 70ZM202.806 69.9316C202.541 70.0775 202.193 70.1504 201.76 70.1504C200.534 70.1504 199.921 69.4668 199.921 68.0996V63.957H198.718V63H199.921V61.291L201.042 60.9287V63H202.806V63.957H201.042V67.9014C201.042 68.3708 201.122 68.7057 201.281 68.9062C201.441 69.1068 201.705 69.207 202.074 69.207C202.357 69.207 202.601 69.1296 202.806 68.9746V69.9316ZM207.229 70.1641C206.194 70.1641 205.367 69.8382 204.747 69.1865C204.132 68.5303 203.824 67.6621 203.824 66.582C203.824 65.4062 204.146 64.488 204.788 63.8271C205.431 63.1663 206.299 62.8359 207.393 62.8359C208.436 62.8359 209.25 63.1572 209.833 63.7998C210.421 64.4424 210.715 65.3333 210.715 66.4727C210.715 67.5892 210.398 68.4847 209.765 69.1592C209.136 69.8291 208.29 70.1641 207.229 70.1641ZM207.311 63.7793C206.59 63.7793 206.021 64.0254 205.602 64.5176C205.182 65.0052 204.973 65.6797 204.973 66.541C204.973 67.3704 205.185 68.0244 205.608 68.5029C206.032 68.9814 206.6 69.2207 207.311 69.2207C208.035 69.2207 208.591 68.986 208.979 68.5166C209.37 68.0472 209.566 67.3796 209.566 66.5137C209.566 65.6387 209.37 64.9642 208.979 64.4902C208.591 64.0163 208.035 63.7793 207.311 63.7793ZM213.654 68.9883H213.627V73.2197H212.506V63H213.627V64.2305H213.654C214.206 63.3008 215.012 62.8359 216.074 62.8359C216.977 62.8359 217.681 63.1504 218.187 63.7793C218.692 64.4036 218.945 65.2422 218.945 66.2949C218.945 67.4661 218.66 68.4049 218.091 69.1113C217.521 69.8132 216.742 70.1641 215.753 70.1641C214.846 70.1641 214.146 69.7721 213.654 68.9883ZM213.627 66.165V67.1426C213.627 67.7214 213.814 68.2135 214.188 68.6191C214.566 69.0202 215.044 69.2207 215.623 69.2207C216.302 69.2207 216.833 68.9609 217.216 68.4414C217.603 67.9219 217.797 67.1995 217.797 66.2744C217.797 65.4951 217.617 64.8844 217.257 64.4424C216.897 64.0003 216.409 63.7793 215.794 63.7793C215.142 63.7793 214.618 64.0072 214.222 64.4629C213.825 64.9141 213.627 65.4814 213.627 66.165ZM225.877 66.2949V70H224.729V60.1973H227.422C228.47 60.1973 229.281 60.4525 229.855 60.9629C230.434 61.4733 230.724 62.1934 230.724 63.123C230.724 64.0527 230.402 64.8138 229.76 65.4062C229.122 65.9987 228.258 66.2949 227.169 66.2949H225.877ZM225.877 61.2363V65.2559H227.08C227.873 65.2559 228.477 65.0758 228.892 64.7158C229.311 64.3512 229.521 63.8385 229.521 63.1777C229.521 61.8835 228.755 61.2363 227.224 61.2363H225.877ZM236.076 64.1348C235.88 63.9844 235.598 63.9092 235.229 63.9092C234.75 63.9092 234.349 64.1348 234.025 64.5859C233.706 65.0371 233.547 65.6523 233.547 66.4316V70H232.426V63H233.547V64.4424H233.574C233.734 63.9502 233.978 63.5674 234.306 63.2939C234.634 63.016 235.001 62.877 235.406 62.877C235.698 62.877 235.921 62.9089 236.076 62.9727V64.1348ZM240.219 70.1641C239.184 70.1641 238.357 69.8382 237.737 69.1865C237.122 68.5303 236.814 67.6621 236.814 66.582C236.814 65.4062 237.136 64.488 237.778 63.8271C238.421 63.1663 239.289 62.8359 240.383 62.8359C241.426 62.8359 242.24 63.1572 242.823 63.7998C243.411 64.4424 243.705 65.3333 243.705 66.4727C243.705 67.5892 243.388 68.4847 242.755 69.1592C242.126 69.8291 241.281 70.1641 240.219 70.1641ZM240.301 63.7793C239.581 63.7793 239.011 64.0254 238.592 64.5176C238.173 65.0052 237.963 65.6797 237.963 66.541C237.963 67.3704 238.175 68.0244 238.599 68.5029C239.022 68.9814 239.59 69.2207 240.301 69.2207C241.025 69.2207 241.581 68.986 241.969 68.5166C242.361 68.0472 242.557 67.3796 242.557 66.5137C242.557 65.6387 242.361 64.9642 241.969 64.4902C241.581 64.0163 241.025 63.7793 240.301 63.7793Z" fill="black"/>
-    <rect x="102" y="78" width="3" height="3" fill="#00188F"/>
-    <path d="M241 78H244V81H241V78Z" fill="#00188F"/>
-    <rect x="103" y="79" width="140" height="1" fill="#00188F"/>
-    <path d="M102.65 92.6885V91.625C102.772 91.7324 102.917 91.8291 103.085 91.915C103.257 92.001 103.436 92.0744 103.622 92.1353C103.812 92.1925 104.002 92.2373 104.191 92.2695C104.381 92.3018 104.557 92.3179 104.718 92.3179C105.273 92.3179 105.686 92.2158 105.958 92.0117C106.234 91.804 106.372 91.5068 106.372 91.1201C106.372 90.9124 106.326 90.7316 106.232 90.5776C106.143 90.4237 106.018 90.284 105.856 90.1587C105.695 90.0298 105.504 89.908 105.282 89.7935C105.063 89.6753 104.827 89.5518 104.573 89.4229C104.304 89.2868 104.054 89.1489 103.821 89.0093C103.588 88.8696 103.386 88.7157 103.214 88.5474C103.042 88.3791 102.906 88.1893 102.806 87.978C102.709 87.7632 102.661 87.5125 102.661 87.2261C102.661 86.8752 102.738 86.5708 102.892 86.313C103.046 86.0516 103.248 85.8368 103.499 85.6685C103.749 85.5002 104.034 85.3748 104.353 85.2925C104.675 85.2101 105.002 85.1689 105.335 85.1689C106.095 85.1689 106.648 85.2603 106.995 85.4429V86.458C106.54 86.1429 105.957 85.9854 105.244 85.9854C105.047 85.9854 104.85 86.0068 104.653 86.0498C104.456 86.0892 104.281 86.1554 104.127 86.2485C103.973 86.3416 103.848 86.4616 103.751 86.6084C103.654 86.7552 103.606 86.9342 103.606 87.1455C103.606 87.3424 103.642 87.5125 103.713 87.6558C103.789 87.799 103.898 87.9297 104.041 88.0479C104.184 88.166 104.358 88.2806 104.562 88.3916C104.77 88.5026 105.008 88.6243 105.276 88.7568C105.552 88.8929 105.813 89.0361 106.061 89.1865C106.308 89.3369 106.524 89.5034 106.71 89.686C106.897 89.8687 107.043 90.071 107.151 90.293C107.262 90.515 107.317 90.7692 107.317 91.0557C107.317 91.4352 107.242 91.7575 107.092 92.0225C106.945 92.2839 106.744 92.4969 106.49 92.6616C106.24 92.8263 105.95 92.9445 105.62 93.0161C105.291 93.0913 104.943 93.1289 104.578 93.1289C104.456 93.1289 104.306 93.1182 104.127 93.0967C103.948 93.0788 103.765 93.0501 103.579 93.0107C103.393 92.9749 103.216 92.9302 103.047 92.8765C102.883 92.8192 102.75 92.7565 102.65 92.6885ZM111.034 93.1289C110.221 93.1289 109.571 92.8729 109.084 92.3608C108.601 91.8452 108.359 91.1631 108.359 90.3145C108.359 89.3906 108.612 88.6691 109.117 88.1499C109.622 87.6307 110.304 87.3711 111.163 87.3711C111.983 87.3711 112.622 87.6235 113.081 88.1284C113.542 88.6333 113.773 89.3333 113.773 90.2285C113.773 91.1058 113.525 91.8094 113.027 92.3394C112.533 92.8657 111.868 93.1289 111.034 93.1289ZM111.099 88.1123C110.533 88.1123 110.085 88.3057 109.756 88.6924C109.426 89.0755 109.262 89.6055 109.262 90.2822C109.262 90.9339 109.428 91.4478 109.761 91.8237C110.094 92.1997 110.54 92.3877 111.099 92.3877C111.668 92.3877 112.105 92.2033 112.409 91.8345C112.717 91.4657 112.871 90.9411 112.871 90.2607C112.871 89.5732 112.717 89.0433 112.409 88.6709C112.105 88.2985 111.668 88.1123 111.099 88.1123ZM117.898 85.6309C117.727 85.5342 117.531 85.4858 117.313 85.4858C116.697 85.4858 116.389 85.8743 116.389 86.6514V87.5H117.678V88.252H116.389V93H115.514V88.252H114.574V87.5H115.514V86.6084C115.514 86.0319 115.68 85.5771 116.013 85.2441C116.346 84.9076 116.762 84.7393 117.259 84.7393C117.528 84.7393 117.741 84.7715 117.898 84.8359V85.6309ZM121.18 92.9463C120.972 93.0609 120.699 93.1182 120.358 93.1182C119.395 93.1182 118.914 92.5811 118.914 91.5068V88.252H117.968V87.5H118.914V86.1572L119.794 85.8726V87.5H121.18V88.252H119.794V91.3511C119.794 91.7199 119.857 91.9831 119.982 92.1406C120.108 92.2982 120.315 92.377 120.605 92.377C120.827 92.377 121.019 92.3161 121.18 92.1943V92.9463ZM129.285 87.5L127.636 93H126.723L125.59 89.063C125.547 88.9126 125.518 88.7425 125.504 88.5527H125.482C125.472 88.6816 125.434 88.8481 125.37 89.0522L124.14 93H123.259L121.594 87.5H122.518L123.656 91.6357C123.692 91.7611 123.717 91.9258 123.731 92.1299H123.774C123.785 91.9723 123.817 91.804 123.871 91.625L125.139 87.5H125.944L127.083 91.6465C127.119 91.779 127.146 91.9437 127.164 92.1406H127.207C127.214 92.001 127.244 91.8363 127.298 91.6465L128.415 87.5H129.285ZM134.243 93H133.362V92.1406H133.34C132.957 92.7995 132.393 93.1289 131.648 93.1289C131.101 93.1289 130.671 92.9839 130.359 92.6938C130.051 92.4038 129.897 92.0189 129.897 91.5391C129.897 90.5114 130.503 89.9134 131.713 89.7451L133.362 89.5142C133.362 88.5796 132.984 88.1123 132.229 88.1123C131.566 88.1123 130.968 88.3379 130.435 88.7891V87.8867C130.975 87.543 131.598 87.3711 132.304 87.3711C133.596 87.3711 134.243 88.055 134.243 89.4229V93ZM133.362 90.2178L132.035 90.4004C131.627 90.4577 131.319 90.5597 131.111 90.7065C130.904 90.8498 130.8 91.1058 130.8 91.4746C130.8 91.7432 130.895 91.9634 131.084 92.1353C131.278 92.3035 131.534 92.3877 131.853 92.3877C132.289 92.3877 132.649 92.2355 132.932 91.9312C133.219 91.6232 133.362 91.2347 133.362 90.7656V90.2178ZM138.771 88.3916C138.617 88.2734 138.395 88.2144 138.104 88.2144C137.729 88.2144 137.413 88.3916 137.159 88.7461C136.909 89.1006 136.783 89.584 136.783 90.1963V93H135.902V87.5H136.783V88.6333H136.805C136.93 88.2466 137.122 87.9458 137.379 87.731C137.637 87.5125 137.925 87.4033 138.244 87.4033C138.473 87.4033 138.649 87.4284 138.771 87.4785V88.3916ZM144.147 90.4702H140.264C140.278 91.0825 140.443 91.5552 140.758 91.8882C141.073 92.2212 141.506 92.3877 142.058 92.3877C142.677 92.3877 143.246 92.1836 143.766 91.7754V92.6025C143.282 92.9535 142.643 93.1289 141.848 93.1289C141.071 93.1289 140.461 92.88 140.017 92.3823C139.573 91.881 139.351 91.1774 139.351 90.2715C139.351 89.4157 139.592 88.7192 140.076 88.1821C140.563 87.6414 141.166 87.3711 141.886 87.3711C142.605 87.3711 143.162 87.6038 143.556 88.0693C143.95 88.5348 144.147 89.1812 144.147 90.0083V90.4702ZM143.245 89.7236C143.241 89.2152 143.118 88.8195 142.874 88.5366C142.634 88.2537 142.299 88.1123 141.87 88.1123C141.454 88.1123 141.102 88.2609 140.812 88.5581C140.521 88.8553 140.342 89.2438 140.274 89.7236H143.245ZM150.812 94.751H150.028C148.918 93.4834 148.363 91.9204 148.363 90.062C148.363 88.1965 148.918 86.6084 150.028 85.2979H150.823C149.699 86.6585 149.137 88.243 149.137 90.0513C149.137 91.8452 149.695 93.4118 150.812 94.751ZM152.703 93H151.822V84.8574H152.703V93ZM158.907 90.4702H155.023C155.038 91.0825 155.202 91.5552 155.518 91.8882C155.833 92.2212 156.266 92.3877 156.817 92.3877C157.437 92.3877 158.006 92.1836 158.525 91.7754V92.6025C158.042 92.9535 157.403 93.1289 156.608 93.1289C155.831 93.1289 155.22 92.88 154.776 92.3823C154.332 91.881 154.11 91.1774 154.11 90.2715C154.11 89.4157 154.352 88.7192 154.835 88.1821C155.322 87.6414 155.926 87.3711 156.646 87.3711C157.365 87.3711 157.922 87.6038 158.316 88.0693C158.71 88.5348 158.907 89.1812 158.907 90.0083V90.4702ZM158.004 89.7236C158.001 89.2152 157.877 88.8195 157.634 88.5366C157.394 88.2537 157.059 88.1123 156.629 88.1123C156.214 88.1123 155.861 88.2609 155.571 88.5581C155.281 88.8553 155.102 89.2438 155.034 89.7236H158.004ZM164.181 93H163.3V92.1406H163.279C162.896 92.7995 162.332 93.1289 161.587 93.1289C161.039 93.1289 160.609 92.9839 160.298 92.6938C159.99 92.4038 159.836 92.0189 159.836 91.5391C159.836 90.5114 160.441 89.9134 161.651 89.7451L163.3 89.5142C163.3 88.5796 162.923 88.1123 162.167 88.1123C161.505 88.1123 160.907 88.3379 160.373 88.7891V87.8867C160.914 87.543 161.537 87.3711 162.242 87.3711C163.535 87.3711 164.181 88.055 164.181 89.4229V93ZM163.3 90.2178L161.974 90.4004C161.565 90.4577 161.257 90.5597 161.05 90.7065C160.842 90.8498 160.738 91.1058 160.738 91.4746C160.738 91.7432 160.833 91.9634 161.023 92.1353C161.216 92.3035 161.472 92.3877 161.791 92.3877C162.228 92.3877 162.588 92.2355 162.871 91.9312C163.157 91.6232 163.3 91.2347 163.3 90.7656V90.2178ZM168.709 88.3916C168.555 88.2734 168.333 88.2144 168.043 88.2144C167.667 88.2144 167.352 88.3916 167.098 88.7461C166.847 89.1006 166.722 89.584 166.722 90.1963V93H165.841V87.5H166.722V88.6333H166.743C166.868 88.2466 167.06 87.9458 167.318 87.731C167.576 87.5125 167.864 87.4033 168.183 87.4033C168.412 87.4033 168.587 87.4284 168.709 87.4785V88.3916ZM174.23 93H173.35V89.8633C173.35 88.696 172.924 88.1123 172.071 88.1123C171.631 88.1123 171.266 88.2788 170.976 88.6118C170.689 88.9412 170.546 89.3584 170.546 89.8633V93H169.665V87.5H170.546V88.4131H170.567C170.983 87.7184 171.584 87.3711 172.372 87.3711C172.974 87.3711 173.434 87.5662 173.752 87.9565C174.071 88.3433 174.23 88.9036 174.23 89.6377V93ZM180.316 90.4702H176.433C176.447 91.0825 176.612 91.5552 176.927 91.8882C177.242 92.2212 177.675 92.3877 178.227 92.3877C178.846 92.3877 179.415 92.1836 179.935 91.7754V92.6025C179.451 92.9535 178.812 93.1289 178.017 93.1289C177.24 93.1289 176.63 92.88 176.186 92.3823C175.742 91.881 175.52 91.1774 175.52 90.2715C175.52 89.4157 175.761 88.7192 176.245 88.1821C176.732 87.6414 177.335 87.3711 178.055 87.3711C178.774 87.3711 179.331 87.6038 179.725 88.0693C180.119 88.5348 180.316 89.1812 180.316 90.0083V90.4702ZM179.414 89.7236C179.41 89.2152 179.286 88.8195 179.043 88.5366C178.803 88.2537 178.468 88.1123 178.039 88.1123C177.623 88.1123 177.271 88.2609 176.98 88.5581C176.69 88.8553 176.511 89.2438 176.443 89.7236H179.414ZM186.348 93H185.467V92.0654H185.445C185.037 92.7744 184.407 93.1289 183.555 93.1289C182.864 93.1289 182.31 92.8836 181.895 92.3931C181.483 91.8989 181.277 91.2275 181.277 90.3789C181.277 89.4694 181.507 88.7407 181.965 88.1929C182.423 87.645 183.034 87.3711 183.796 87.3711C184.552 87.3711 185.102 87.6683 185.445 88.2627H185.467V84.8574H186.348V93ZM185.467 90.5132V89.7021C185.467 89.2581 185.32 88.8822 185.026 88.5742C184.733 88.2663 184.36 88.1123 183.909 88.1123C183.372 88.1123 182.95 88.3092 182.642 88.7031C182.334 89.097 182.18 89.6413 182.18 90.3359C182.18 90.9697 182.326 91.471 182.62 91.8398C182.917 92.2051 183.315 92.3877 183.812 92.3877C184.303 92.3877 184.701 92.2104 185.005 91.856C185.313 91.5015 185.467 91.0539 185.467 90.5132ZM188.152 94.751H187.368C188.485 93.4118 189.044 91.8452 189.044 90.0513C189.044 88.243 188.482 86.6585 187.357 85.2979H188.152C189.27 86.6084 189.828 88.1965 189.828 90.062C189.828 91.9204 189.27 93.4834 188.152 94.751Z" fill="#00188F"/>
-    <rect x="102" y="98" width="3" height="3" fill="#EF6950"/>
-    <rect x="103" y="99" width="116" height="1" fill="#EF6950"/>
-    <path d="M102.65 112.688V111.625C102.772 111.732 102.917 111.829 103.085 111.915C103.257 112.001 103.436 112.074 103.622 112.135C103.812 112.193 104.002 112.237 104.191 112.27C104.381 112.302 104.557 112.318 104.718 112.318C105.273 112.318 105.686 112.216 105.958 112.012C106.234 111.804 106.372 111.507 106.372 111.12C106.372 110.912 106.326 110.732 106.232 110.578C106.143 110.424 106.018 110.284 105.856 110.159C105.695 110.03 105.504 109.908 105.282 109.793C105.063 109.675 104.827 109.552 104.573 109.423C104.304 109.287 104.054 109.149 103.821 109.009C103.588 108.87 103.386 108.716 103.214 108.547C103.042 108.379 102.906 108.189 102.806 107.978C102.709 107.763 102.661 107.513 102.661 107.226C102.661 106.875 102.738 106.571 102.892 106.313C103.046 106.052 103.248 105.837 103.499 105.668C103.749 105.5 104.034 105.375 104.353 105.292C104.675 105.21 105.002 105.169 105.335 105.169C106.095 105.169 106.648 105.26 106.995 105.443V106.458C106.54 106.143 105.957 105.985 105.244 105.985C105.047 105.985 104.85 106.007 104.653 106.05C104.456 106.089 104.281 106.155 104.127 106.249C103.973 106.342 103.848 106.462 103.751 106.608C103.654 106.755 103.606 106.934 103.606 107.146C103.606 107.342 103.642 107.513 103.713 107.656C103.789 107.799 103.898 107.93 104.041 108.048C104.184 108.166 104.358 108.281 104.562 108.392C104.77 108.503 105.008 108.624 105.276 108.757C105.552 108.893 105.813 109.036 106.061 109.187C106.308 109.337 106.524 109.503 106.71 109.686C106.897 109.869 107.043 110.071 107.151 110.293C107.262 110.515 107.317 110.769 107.317 111.056C107.317 111.435 107.242 111.757 107.092 112.022C106.945 112.284 106.744 112.497 106.49 112.662C106.24 112.826 105.95 112.944 105.62 113.016C105.291 113.091 104.943 113.129 104.578 113.129C104.456 113.129 104.306 113.118 104.127 113.097C103.948 113.079 103.765 113.05 103.579 113.011C103.393 112.975 103.216 112.93 103.047 112.876C102.883 112.819 102.75 112.757 102.65 112.688ZM111.034 113.129C110.221 113.129 109.571 112.873 109.084 112.361C108.601 111.845 108.359 111.163 108.359 110.314C108.359 109.391 108.612 108.669 109.117 108.15C109.622 107.631 110.304 107.371 111.163 107.371C111.983 107.371 112.622 107.624 113.081 108.128C113.542 108.633 113.773 109.333 113.773 110.229C113.773 111.106 113.525 111.809 113.027 112.339C112.533 112.866 111.868 113.129 111.034 113.129ZM111.099 108.112C110.533 108.112 110.085 108.306 109.756 108.692C109.426 109.076 109.262 109.605 109.262 110.282C109.262 110.934 109.428 111.448 109.761 111.824C110.094 112.2 110.54 112.388 111.099 112.388C111.668 112.388 112.105 112.203 112.409 111.834C112.717 111.466 112.871 110.941 112.871 110.261C112.871 109.573 112.717 109.043 112.409 108.671C112.105 108.299 111.668 108.112 111.099 108.112ZM117.898 105.631C117.727 105.534 117.531 105.486 117.313 105.486C116.697 105.486 116.389 105.874 116.389 106.651V107.5H117.678V108.252H116.389V113H115.514V108.252H114.574V107.5H115.514V106.608C115.514 106.032 115.68 105.577 116.013 105.244C116.346 104.908 116.762 104.739 117.259 104.739C117.528 104.739 117.741 104.771 117.898 104.836V105.631ZM121.18 112.946C120.972 113.061 120.699 113.118 120.358 113.118C119.395 113.118 118.914 112.581 118.914 111.507V108.252H117.968V107.5H118.914V106.157L119.794 105.873V107.5H121.18V108.252H119.794V111.351C119.794 111.72 119.857 111.983 119.982 112.141C120.108 112.298 120.315 112.377 120.605 112.377C120.827 112.377 121.019 112.316 121.18 112.194V112.946ZM129.285 107.5L127.636 113H126.723L125.59 109.063C125.547 108.913 125.518 108.743 125.504 108.553H125.482C125.472 108.682 125.434 108.848 125.37 109.052L124.14 113H123.259L121.594 107.5H122.518L123.656 111.636C123.692 111.761 123.717 111.926 123.731 112.13H123.774C123.785 111.972 123.817 111.804 123.871 111.625L125.139 107.5H125.944L127.083 111.646C127.119 111.779 127.146 111.944 127.164 112.141H127.207C127.214 112.001 127.244 111.836 127.298 111.646L128.415 107.5H129.285ZM134.243 113H133.362V112.141H133.34C132.957 112.799 132.393 113.129 131.648 113.129C131.101 113.129 130.671 112.984 130.359 112.694C130.051 112.404 129.897 112.019 129.897 111.539C129.897 110.511 130.503 109.913 131.713 109.745L133.362 109.514C133.362 108.58 132.984 108.112 132.229 108.112C131.566 108.112 130.968 108.338 130.435 108.789V107.887C130.975 107.543 131.598 107.371 132.304 107.371C133.596 107.371 134.243 108.055 134.243 109.423V113ZM133.362 110.218L132.035 110.4C131.627 110.458 131.319 110.56 131.111 110.707C130.904 110.85 130.8 111.106 130.8 111.475C130.8 111.743 130.895 111.963 131.084 112.135C131.278 112.304 131.534 112.388 131.853 112.388C132.289 112.388 132.649 112.236 132.932 111.931C133.219 111.623 133.362 111.235 133.362 110.766V110.218ZM138.771 108.392C138.617 108.273 138.395 108.214 138.104 108.214C137.729 108.214 137.413 108.392 137.159 108.746C136.909 109.101 136.783 109.584 136.783 110.196V113H135.902V107.5H136.783V108.633H136.805C136.93 108.247 137.122 107.946 137.379 107.731C137.637 107.513 137.925 107.403 138.244 107.403C138.473 107.403 138.649 107.428 138.771 107.479V108.392ZM144.147 110.47H140.264C140.278 111.083 140.443 111.555 140.758 111.888C141.073 112.221 141.506 112.388 142.058 112.388C142.677 112.388 143.246 112.184 143.766 111.775V112.603C143.282 112.953 142.643 113.129 141.848 113.129C141.071 113.129 140.461 112.88 140.017 112.382C139.573 111.881 139.351 111.177 139.351 110.271C139.351 109.416 139.592 108.719 140.076 108.182C140.563 107.641 141.166 107.371 141.886 107.371C142.605 107.371 143.162 107.604 143.556 108.069C143.95 108.535 144.147 109.181 144.147 110.008V110.47ZM143.245 109.724C143.241 109.215 143.118 108.819 142.874 108.537C142.634 108.254 142.299 108.112 141.87 108.112C141.454 108.112 141.102 108.261 140.812 108.558C140.521 108.855 140.342 109.244 140.274 109.724H143.245ZM150.812 114.751H150.028C148.918 113.483 148.363 111.92 148.363 110.062C148.363 108.196 148.918 106.608 150.028 105.298H150.823C149.699 106.659 149.137 108.243 149.137 110.051C149.137 111.845 149.695 113.412 150.812 114.751ZM152.703 113H151.822V104.857H152.703V113ZM154.938 106.104C154.78 106.104 154.646 106.05 154.535 105.942C154.424 105.835 154.368 105.699 154.368 105.534C154.368 105.369 154.424 105.233 154.535 105.126C154.646 105.015 154.78 104.959 154.938 104.959C155.099 104.959 155.235 105.015 155.346 105.126C155.46 105.233 155.518 105.369 155.518 105.534C155.518 105.692 155.46 105.826 155.346 105.937C155.235 106.048 155.099 106.104 154.938 106.104ZM155.367 113H154.486V107.5H155.367V113ZM156.817 112.801V111.856C157.297 112.21 157.825 112.388 158.402 112.388C159.175 112.388 159.562 112.13 159.562 111.614C159.562 111.467 159.528 111.344 159.46 111.244C159.396 111.14 159.306 111.049 159.191 110.97C159.08 110.891 158.948 110.821 158.794 110.76C158.644 110.696 158.481 110.63 158.305 110.562C158.062 110.465 157.847 110.368 157.661 110.271C157.478 110.171 157.324 110.06 157.199 109.938C157.077 109.813 156.984 109.672 156.919 109.514C156.859 109.357 156.828 109.172 156.828 108.961C156.828 108.703 156.887 108.476 157.005 108.279C157.124 108.078 157.281 107.912 157.478 107.779C157.675 107.643 157.899 107.541 158.149 107.473C158.404 107.405 158.665 107.371 158.934 107.371C159.41 107.371 159.836 107.453 160.212 107.618V108.51C159.807 108.245 159.342 108.112 158.815 108.112C158.651 108.112 158.502 108.132 158.37 108.171C158.237 108.207 158.123 108.259 158.026 108.327C157.933 108.395 157.859 108.478 157.806 108.574C157.756 108.667 157.73 108.771 157.73 108.886C157.73 109.029 157.756 109.149 157.806 109.246C157.859 109.342 157.936 109.428 158.037 109.503C158.137 109.579 158.259 109.647 158.402 109.708C158.545 109.768 158.708 109.835 158.891 109.906C159.134 109.999 159.353 110.096 159.546 110.196C159.739 110.293 159.904 110.404 160.04 110.529C160.176 110.651 160.28 110.792 160.352 110.954C160.427 111.115 160.464 111.306 160.464 111.528C160.464 111.8 160.403 112.037 160.282 112.237C160.164 112.438 160.004 112.604 159.804 112.737C159.603 112.869 159.372 112.968 159.111 113.032C158.849 113.097 158.576 113.129 158.289 113.129C157.723 113.129 157.233 113.02 156.817 112.801ZM164.375 112.946C164.167 113.061 163.893 113.118 163.553 113.118C162.59 113.118 162.108 112.581 162.108 111.507V108.252H161.163V107.5H162.108V106.157L162.989 105.873V107.5H164.375V108.252H162.989V111.351C162.989 111.72 163.051 111.983 163.177 112.141C163.302 112.298 163.51 112.377 163.8 112.377C164.022 112.377 164.213 112.316 164.375 112.194V112.946ZM165.572 114.751H164.788C165.905 113.412 166.464 111.845 166.464 110.051C166.464 108.243 165.902 106.659 164.777 105.298H165.572C166.689 106.608 167.248 108.196 167.248 110.062C167.248 111.92 166.689 113.483 165.572 114.751Z" fill="#EF6950"/>
-    <rect x="217" y="98" width="3" height="3" fill="#EF6950"/>
-    <path d="M22.04 33.168C22.04 35.1341 21.153 36.1172 19.3789 36.1172C17.6797 36.1172 16.8301 35.1715 16.8301 33.2803V28.998H17.6504V33.2266C17.6504 34.6621 18.2559 35.3799 19.4668 35.3799C20.6354 35.3799 21.2197 34.6865 21.2197 33.2998V28.998H22.04V33.168ZM27.9336 29.7402H25.9121V36H25.0918V29.7402H23.0752V28.998H27.9336V29.7402ZM33.373 29.7402H31.3516V36H30.5312V29.7402H28.5146V28.998H33.373V29.7402ZM38.1875 36H34.4766V28.998H38.0312V29.7402H35.2969V32.0693H37.8262V32.8066H35.2969V35.2578H38.1875V36ZM44.5547 36H43.5781L42.4062 34.0371C42.2988 33.8548 42.1947 33.7002 42.0938 33.5732C41.9928 33.443 41.8887 33.3372 41.7812 33.2559C41.6771 33.1745 41.5632 33.1159 41.4395 33.0801C41.319 33.041 41.1823 33.0215 41.0293 33.0215H40.3555V36H39.5352V28.998H41.625C41.931 28.998 42.2126 29.0371 42.4697 29.1152C42.7301 29.1901 42.9548 29.3057 43.1436 29.4619C43.3356 29.6182 43.4854 29.8135 43.5928 30.0479C43.7002 30.279 43.7539 30.5508 43.7539 30.8633C43.7539 31.1074 43.7165 31.332 43.6416 31.5371C43.57 31.7389 43.4658 31.9196 43.3291 32.0791C43.1956 32.2386 43.0329 32.3753 42.8408 32.4893C42.652 32.5999 42.4388 32.6862 42.2012 32.748V32.7676C42.3184 32.8197 42.4193 32.8799 42.5039 32.9482C42.5918 33.0133 42.6748 33.0915 42.7529 33.1826C42.8311 33.2738 42.9076 33.3779 42.9824 33.4951C43.0605 33.609 43.1468 33.7425 43.2412 33.8955L44.5547 36ZM40.3555 29.7402V32.2793H41.4688C41.6738 32.2793 41.8626 32.2484 42.0352 32.1865C42.2109 32.1247 42.3623 32.0368 42.4893 31.9229C42.6162 31.8057 42.7155 31.6641 42.7871 31.498C42.8587 31.3288 42.8945 31.14 42.8945 30.9316C42.8945 30.5573 42.7725 30.266 42.5283 30.0576C42.2874 29.846 41.9375 29.7402 41.4785 29.7402H40.3555ZM50.9414 36H50.0332L49.291 34.0371H46.3223L45.624 36H44.7109L47.3965 28.998H48.2461L50.9414 36ZM49.0225 33.2998L47.9238 30.3164C47.888 30.2188 47.8522 30.0625 47.8164 29.8477H47.7969C47.7643 30.0462 47.7269 30.2025 47.6846 30.3164L46.5957 33.2998H49.0225ZM57.6211 36H56.6152L53.0117 30.4189C52.9206 30.279 52.8457 30.1325 52.7871 29.9795H52.7578C52.7839 30.1292 52.7969 30.4499 52.7969 30.9414V36H51.9766V28.998H53.041L56.5469 34.4912C56.6934 34.7191 56.7878 34.8753 56.8301 34.96H56.8496C56.8171 34.7581 56.8008 34.4147 56.8008 33.9297V28.998H57.6211V36ZM64.2227 35.707C63.7051 35.9805 63.0605 36.1172 62.2891 36.1172C61.293 36.1172 60.4954 35.7965 59.8965 35.1553C59.2975 34.514 58.998 33.6725 58.998 32.6309C58.998 31.5111 59.335 30.6061 60.0088 29.916C60.6826 29.2259 61.5371 28.8809 62.5723 28.8809C63.2363 28.8809 63.7865 28.9769 64.2227 29.1689V30.043C63.7214 29.763 63.168 29.623 62.5625 29.623C61.7585 29.623 61.1058 29.8916 60.6045 30.4287C60.1064 30.9658 59.8574 31.6836 59.8574 32.582C59.8574 33.4349 60.0902 34.1152 60.5557 34.623C61.0244 35.1276 61.638 35.3799 62.3965 35.3799C63.0996 35.3799 63.7083 35.2236 64.2227 34.9111V35.707ZM69.3594 36H65.6484V28.998H69.2031V29.7402H66.4688V32.0693H68.998V32.8066H66.4688V35.2578H69.3594V36ZM78.8711 36H77.9629L77.2207 34.0371H74.252L73.5537 36H72.6406L75.3262 28.998H76.1758L78.8711 36ZM76.9521 33.2998L75.8535 30.3164C75.8177 30.2188 75.7819 30.0625 75.7461 29.8477H75.7266C75.694 30.0462 75.6566 30.2025 75.6143 30.3164L74.5254 33.2998H76.9521ZM85.5508 36H84.5449L80.9414 30.4189C80.8503 30.279 80.7754 30.1325 80.7168 29.9795H80.6875C80.7135 30.1292 80.7266 30.4499 80.7266 30.9414V36H79.9062V28.998H80.9707L84.4766 34.4912C84.623 34.7191 84.7174 34.8753 84.7598 34.96H84.7793C84.7467 34.7581 84.7305 34.4147 84.7305 33.9297V28.998H85.5508V36ZM87.3867 36V28.998H89.3203C91.7878 28.998 93.0215 30.1357 93.0215 32.4111C93.0215 33.4919 92.6781 34.361 91.9912 35.0186C91.3076 35.6729 90.3913 36 89.2422 36H87.3867ZM88.207 29.7402V35.2578H89.252C90.1699 35.2578 90.8844 35.012 91.3955 34.5205C91.9066 34.029 92.1621 33.3324 92.1621 32.4307C92.1621 30.637 91.2083 29.7402 89.3008 29.7402H88.207ZM97.1426 36V28.998H99.0762C101.544 28.998 102.777 30.1357 102.777 32.4111C102.777 33.4919 102.434 34.361 101.747 35.0186C101.063 35.6729 100.147 36 98.998 36H97.1426ZM97.9629 29.7402V35.2578H99.0078C99.9258 35.2578 100.64 35.012 101.151 34.5205C101.662 34.029 101.918 33.3324 101.918 32.4307C101.918 30.637 100.964 29.7402 99.0566 29.7402H97.9629ZM107.865 36H104.154V28.998H107.709V29.7402H104.975V32.0693H107.504V32.8066H104.975V35.2578H107.865V36ZM113.354 29.7402H111.332V36H110.512V29.7402H108.495V28.998H113.354V29.7402ZM118.168 36H114.457V28.998H118.012V29.7402H115.277V32.0693H117.807V32.8066H115.277V35.2578H118.168V36ZM124.281 35.707C123.764 35.9805 123.119 36.1172 122.348 36.1172C121.352 36.1172 120.554 35.7965 119.955 35.1553C119.356 34.514 119.057 33.6725 119.057 32.6309C119.057 31.5111 119.394 30.6061 120.067 29.916C120.741 29.2259 121.596 28.8809 122.631 28.8809C123.295 28.8809 123.845 28.9769 124.281 29.1689V30.043C123.78 29.763 123.227 29.623 122.621 29.623C121.817 29.623 121.164 29.8916 120.663 30.4287C120.165 30.9658 119.916 31.6836 119.916 32.582C119.916 33.4349 120.149 34.1152 120.614 34.623C121.083 35.1276 121.697 35.3799 122.455 35.3799C123.158 35.3799 123.767 35.2236 124.281 34.9111V35.707ZM129.848 29.7402H127.826V36H127.006V29.7402H124.989V28.998H129.848V29.7402ZM134.662 36H130.951V28.998H134.506V29.7402H131.771V32.0693H134.301V32.8066H131.771V35.2578H134.662V36ZM136.01 36V28.998H137.943C140.411 28.998 141.645 30.1357 141.645 32.4111C141.645 33.4919 141.301 34.361 140.614 35.0186C139.931 35.6729 139.014 36 137.865 36H136.01ZM136.83 29.7402V35.2578H137.875C138.793 35.2578 139.507 35.012 140.019 34.5205C140.53 34.029 140.785 33.3324 140.785 32.4307C140.785 30.637 139.831 29.7402 137.924 29.7402H136.83ZM150.531 35.707C150.014 35.9805 149.369 36.1172 148.598 36.1172C147.602 36.1172 146.804 35.7965 146.205 35.1553C145.606 34.514 145.307 33.6725 145.307 32.6309C145.307 31.5111 145.644 30.6061 146.317 29.916C146.991 29.2259 147.846 28.8809 148.881 28.8809C149.545 28.8809 150.095 28.9769 150.531 29.1689V30.043C150.03 29.763 149.477 29.623 148.871 29.623C148.067 29.623 147.414 29.8916 146.913 30.4287C146.415 30.9658 146.166 31.6836 146.166 32.582C146.166 33.4349 146.399 34.1152 146.864 34.623C147.333 35.1276 147.947 35.3799 148.705 35.3799C149.408 35.3799 150.017 35.2236 150.531 34.9111V35.707ZM154.506 36.1172C153.513 36.1172 152.717 35.79 152.118 35.1357C151.522 34.4814 151.225 33.6302 151.225 32.582C151.225 31.4557 151.529 30.5573 152.138 29.8867C152.746 29.2161 153.575 28.8809 154.623 28.8809C155.59 28.8809 156.368 29.2064 156.957 29.8574C157.549 30.5085 157.846 31.3597 157.846 32.4111C157.846 33.5537 157.543 34.457 156.938 35.1211C156.332 35.7852 155.521 36.1172 154.506 36.1172ZM154.564 29.623C153.829 29.623 153.231 29.8883 152.772 30.4189C152.313 30.9495 152.084 31.6462 152.084 32.5088C152.084 33.3714 152.307 34.0664 152.753 34.5938C153.202 35.1178 153.786 35.3799 154.506 35.3799C155.274 35.3799 155.88 35.1292 156.322 34.6279C156.765 34.1266 156.986 33.4251 156.986 32.5234C156.986 31.599 156.771 30.8844 156.342 30.3799C155.912 29.8753 155.32 29.623 154.564 29.623ZM166.361 36H165.546V31.3027C165.546 30.9316 165.569 30.4775 165.614 29.9404H165.595C165.517 30.2562 165.447 30.4824 165.385 30.6191L162.992 36H162.592L160.204 30.6582C160.136 30.502 160.066 30.2627 159.994 29.9404H159.975C160.001 30.2204 160.014 30.6777 160.014 31.3125V36H159.223V28.998H160.307L162.455 33.8809C162.621 34.2552 162.729 34.5352 162.777 34.7207H162.807C162.947 34.3366 163.059 34.0501 163.144 33.8613L165.336 28.998H166.361V36ZM169.027 33.3535V36H168.207V28.998H170.131C170.88 28.998 171.459 29.1803 171.869 29.5449C172.283 29.9095 172.489 30.4238 172.489 31.0879C172.489 31.752 172.26 32.2956 171.801 32.7188C171.345 33.1419 170.728 33.3535 169.95 33.3535H169.027ZM169.027 29.7402V32.6113H169.887C170.453 32.6113 170.884 32.4827 171.181 32.2256C171.48 31.9652 171.63 31.599 171.63 31.127C171.63 30.2025 171.083 29.7402 169.989 29.7402H169.027ZM176.635 36.1172C175.642 36.1172 174.846 35.79 174.247 35.1357C173.651 34.4814 173.354 33.6302 173.354 32.582C173.354 31.4557 173.658 30.5573 174.267 29.8867C174.875 29.2161 175.704 28.8809 176.752 28.8809C177.719 28.8809 178.497 29.2064 179.086 29.8574C179.678 30.5085 179.975 31.3597 179.975 32.4111C179.975 33.5537 179.672 34.457 179.066 35.1211C178.461 35.7852 177.65 36.1172 176.635 36.1172ZM176.693 29.623C175.958 29.623 175.36 29.8883 174.901 30.4189C174.442 30.9495 174.213 31.6462 174.213 32.5088C174.213 33.3714 174.436 34.0664 174.882 34.5938C175.331 35.1178 175.915 35.3799 176.635 35.3799C177.403 35.3799 178.008 35.1292 178.451 34.6279C178.894 34.1266 179.115 33.4251 179.115 32.5234C179.115 31.599 178.9 30.8844 178.471 30.3799C178.041 29.8753 177.449 29.623 176.693 29.623ZM186.996 36H185.99L182.387 30.4189C182.296 30.279 182.221 30.1325 182.162 29.9795H182.133C182.159 30.1292 182.172 30.4499 182.172 30.9414V36H181.352V28.998H182.416L185.922 34.4912C186.068 34.7191 186.163 34.8753 186.205 34.96H186.225C186.192 34.7581 186.176 34.4147 186.176 33.9297V28.998H186.996V36ZM192.543 36H188.832V28.998H192.387V29.7402H189.652V32.0693H192.182V32.8066H189.652V35.2578H192.543V36ZM199.535 36H198.529L194.926 30.4189C194.835 30.279 194.76 30.1325 194.701 29.9795H194.672C194.698 30.1292 194.711 30.4499 194.711 30.9414V36H193.891V28.998H194.955L198.461 34.4912C198.607 34.7191 198.702 34.8753 198.744 34.96H198.764C198.731 34.7581 198.715 34.4147 198.715 33.9297V28.998H199.535V36ZM205.512 29.7402H203.49V36H202.67V29.7402H200.653V28.998H205.512V29.7402ZM206.093 35.7168V34.75C206.203 34.8477 206.335 34.9355 206.488 35.0137C206.645 35.0918 206.807 35.1585 206.977 35.2139C207.149 35.266 207.322 35.3066 207.494 35.3359C207.667 35.3652 207.826 35.3799 207.973 35.3799C208.477 35.3799 208.853 35.2871 209.101 35.1016C209.351 34.9128 209.477 34.6426 209.477 34.291C209.477 34.1022 209.434 33.9378 209.35 33.7979C209.268 33.6579 209.154 33.5309 209.008 33.417C208.861 33.2998 208.687 33.1891 208.485 33.085C208.287 32.9775 208.072 32.8652 207.841 32.748C207.597 32.6243 207.369 32.499 207.157 32.3721C206.946 32.2451 206.762 32.1051 206.605 31.9521C206.449 31.7992 206.326 31.6266 206.234 31.4346C206.146 31.2393 206.103 31.0114 206.103 30.751C206.103 30.432 206.173 30.1553 206.312 29.9209C206.452 29.6833 206.636 29.488 206.864 29.335C207.092 29.182 207.351 29.068 207.641 28.9932C207.934 28.9183 208.231 28.8809 208.534 28.8809C209.224 28.8809 209.727 28.9639 210.043 29.1299V30.0527C209.63 29.7663 209.099 29.623 208.451 29.623C208.272 29.623 208.093 29.6426 207.914 29.6816C207.735 29.7174 207.576 29.7777 207.436 29.8623C207.296 29.9469 207.182 30.056 207.094 30.1895C207.006 30.3229 206.962 30.4857 206.962 30.6777C206.962 30.8568 206.994 31.0114 207.06 31.1416C207.128 31.2718 207.227 31.3906 207.357 31.498C207.488 31.6055 207.646 31.7096 207.831 31.8105C208.02 31.9115 208.236 32.0221 208.48 32.1426C208.731 32.2663 208.969 32.3965 209.193 32.5332C209.418 32.6699 209.615 32.8213 209.784 32.9873C209.953 33.1533 210.087 33.3372 210.185 33.5391C210.285 33.7409 210.336 33.972 210.336 34.2324C210.336 34.5775 210.268 34.8704 210.131 35.1113C209.997 35.349 209.815 35.5426 209.584 35.6924C209.356 35.8421 209.092 35.9495 208.793 36.0146C208.493 36.083 208.178 36.1172 207.846 36.1172C207.735 36.1172 207.598 36.1074 207.436 36.0879C207.273 36.0716 207.107 36.0456 206.938 36.0098C206.768 35.9772 206.607 35.9365 206.454 35.8877C206.304 35.8356 206.184 35.7786 206.093 35.7168Z" fill="#323130"/>
-</svg>
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "分離オーバーラップ例1のSVGファイルの削除"
}
```

### Explanation
この変更では、`separated-overlap-example-1.svg`というSVG形式の画像ファイルが削除されました。このファイルは、カスタムテキスト分析サービスにおける特定の例や概念を視覚的に示すための重要なリソースでした。

削除されたSVGファイルは、分離オーバーラップの概念を説明する際に使用されていたと考えられます。この画像が失われることで、ユーザーはこのテーマに関する視覚的な参考資料を持たなくなり、理解が難しくなる可能性があります。特に、視覚的なガイドが学習や実装の手助けとなることが多いので、該当情報を失うことは大きな影響を及ぼすと言えます。

この削除に関しては、補完的な情報や代替のリソースを提供することで、ユーザーが混乱しないよう配慮する必要があります。さらに、GitHubのリポジトリで詳細な変更点を参照できるため、関連情報を確認することが可能です。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/storage-screen.png{#item-4dd51e}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "ストレージスクリーンのPNGファイルの削除"
}
```

### Explanation
この変更では、`storage-screen.png`というPNG形式の画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスに関連するストレージ機能を視覚的に示すために使用されていた可能性があります。

削除された画像は、ユーザーがサービスを利用する際、特にその操作や機能の理解を深めるために重要な役割を果たしていたと考えられます。このため、画像が失われることで、関連する情報の理解度が低下し、特に視覚的な情報を頼りにしているユーザーにとっては不便をもたらす可能性があります。

この削除に伴い、代替の視覚資料や補足説明を用意することが望ましいです。GitHubリポジトリでは具体的な変更履歴や影響について確認できるため、関連資料をチェックするのが推奨されます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/tag-options.png{#item-0597c4}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "タグオプションのPNGファイルの削除"
}
```

### Explanation
この変更では、`tag-options.png`というPNG形式の画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスにおけるタグオプションの設定や選択肢を視覚的に示すために重要であったと考えられます。

そのため、削除されることによって、ユーザーはタグに関する情報や操作方法の理解が難しくなる可能性があります。このような視覚資料は、特に新しいユーザーや視覚的な情報に依存するユーザーにとって、操作や機能の効果的な理解を助ける役割を果たしていたことから、その影響は大きいといえます。

削除に伴い、必要に応じて代替の視覚資料や補足情報を提供することが望ましいです。影響を受ける可能性のあるユーザーに対して、何らかの支援が必要となるでしょう。また、具体的な変更点についてはGitHubリポジトリで確認することができます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/test-model-results.png{#item-15ad58}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "テストモデル結果のPNGファイルの削除"
}
```

### Explanation
この変更では、`test-model-results.png`というPNG形式の画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスのモデルテスト結果を視覚的に表現するために使用されていた可能性があります。

このファイルの削除により、ユーザーはモデルの性能や結果の解釈に関する重要な情報を見失う可能性があります。特に、視覚的な情報を重視するユーザーや新たにサービスを使用し始めたユーザーにとって、その理解度が低下する恐れがあります。

削除された画像に代わる情報提供策を検討することが推奨されます。さらに、影響を受けるユーザーがスムーズに理解できるように補足資料や改善コースを用意することも重要です。具体的な変更内容や影響に関する詳細はGitHubリポジトリにて確認できます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/train-model.png{#item-fb48a4}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "モデル訓練のPNGファイルの削除"
}
```

### Explanation
この変更においては、`train-model.png`というPNG形式の画像ファイルが削除されました。この画像は、カスタムテキスト分析サービスにおけるモデルの訓練プロセスを視覚的に表現するために使用されていたと考えられます。

削除されたことにより、ユーザーはモデル訓練の具体的な手順や結果を理解しづらくなる可能性があります。特に初心者や視覚的な手助けを必要とするユーザーにとっては、この情報がないことで混乱を招く恐れがあります。

この変更を受けて、代替の資料やガイドを提供し、ユーザーがモデル訓練の過程を理解しやすいようにサポートすることが重要です。また、影響を受けるユーザーが必要な情報を得られるよう、GitHubリポジトリ内での詳細な確認や補足資料のリンクを示すことも推奨されます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/union-overlap-example-1-part-2.svg{#item-f266f5}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +0,0 @@
-<svg width="289" height="114" viewBox="0 0 289 114" fill="none"
-    xmlns="http://www.w3.org/2000/svg">
-    <path d="M296 0H0V114H296V0Z" fill="#F3F2F1"/>
-    <path d="M104.275 66.2949V70H103.127V60.1973H105.82C106.868 60.1973 107.68 60.4525 108.254 60.9629C108.833 61.4733 109.122 62.1934 109.122 63.123C109.122 64.0527 108.801 64.8138 108.158 65.4062C107.52 65.9987 106.657 66.2949 105.567 66.2949H104.275ZM104.275 61.2363V65.2559H105.479C106.271 65.2559 106.875 65.0758 107.29 64.7158C107.709 64.3512 107.919 63.8385 107.919 63.1777C107.919 61.8835 107.153 61.2363 105.622 61.2363H104.275ZM114.475 64.1348C114.279 63.9844 113.996 63.9092 113.627 63.9092C113.148 63.9092 112.747 64.1348 112.424 64.5859C112.105 65.0371 111.945 65.6523 111.945 66.4316V70H110.824V63H111.945V64.4424H111.973C112.132 63.9502 112.376 63.5674 112.704 63.2939C113.032 63.016 113.399 62.877 113.805 62.877C114.096 62.877 114.32 62.9089 114.475 62.9727V64.1348ZM118.617 70.1641C117.583 70.1641 116.756 69.8382 116.136 69.1865C115.521 68.5303 115.213 67.6621 115.213 66.582C115.213 65.4062 115.534 64.488 116.177 63.8271C116.819 63.1663 117.688 62.8359 118.781 62.8359C119.825 62.8359 120.638 63.1572 121.222 63.7998C121.81 64.4424 122.104 65.3333 122.104 66.4727C122.104 67.5892 121.787 68.4847 121.153 69.1592C120.524 69.8291 119.679 70.1641 118.617 70.1641ZM118.699 63.7793C117.979 63.7793 117.41 64.0254 116.99 64.5176C116.571 65.0052 116.361 65.6797 116.361 66.541C116.361 67.3704 116.573 68.0244 116.997 68.5029C117.421 68.9814 117.988 69.2207 118.699 69.2207C119.424 69.2207 119.98 68.986 120.367 68.5166C120.759 68.0472 120.955 67.3796 120.955 66.5137C120.955 65.6387 120.759 64.9642 120.367 64.4902C119.98 64.0163 119.424 63.7793 118.699 63.7793ZM123.471 69.7471V68.5439C124.081 68.9951 124.754 69.2207 125.487 69.2207C126.472 69.2207 126.964 68.8926 126.964 68.2363C126.964 68.0495 126.921 67.8923 126.834 67.7646C126.752 67.6325 126.638 67.5163 126.492 67.416C126.351 67.3158 126.182 67.2269 125.986 67.1494C125.795 67.0674 125.588 66.9831 125.364 66.8965C125.054 66.7734 124.781 66.6504 124.544 66.5273C124.312 66.3997 124.116 66.2585 123.956 66.1035C123.801 65.944 123.683 65.764 123.601 65.5635C123.523 65.363 123.484 65.1283 123.484 64.8594C123.484 64.5312 123.56 64.2419 123.71 63.9912C123.86 63.736 124.061 63.5241 124.312 63.3555C124.562 63.1823 124.847 63.0524 125.166 62.9658C125.49 62.8792 125.822 62.8359 126.164 62.8359C126.77 62.8359 127.312 62.9408 127.791 63.1504V64.2852C127.276 63.9479 126.684 63.7793 126.014 63.7793C125.804 63.7793 125.615 63.8044 125.446 63.8545C125.278 63.9001 125.132 63.9661 125.009 64.0527C124.89 64.1393 124.797 64.2441 124.729 64.3672C124.665 64.4857 124.633 64.6178 124.633 64.7637C124.633 64.946 124.665 65.0986 124.729 65.2217C124.797 65.3447 124.895 65.4541 125.022 65.5498C125.15 65.6455 125.305 65.7321 125.487 65.8096C125.67 65.887 125.877 65.9714 126.109 66.0625C126.419 66.181 126.697 66.304 126.943 66.4316C127.189 66.5547 127.399 66.696 127.572 66.8555C127.745 67.0104 127.878 67.1904 127.969 67.3955C128.064 67.6006 128.112 67.8444 128.112 68.127C128.112 68.4733 128.035 68.7741 127.88 69.0293C127.729 69.2845 127.527 69.4964 127.271 69.665C127.016 69.8337 126.722 69.959 126.39 70.041C126.057 70.123 125.708 70.1641 125.344 70.1641C124.624 70.1641 123.999 70.0251 123.471 69.7471ZM135.468 66.7803H130.525C130.544 67.5596 130.753 68.1611 131.154 68.585C131.555 69.0088 132.107 69.2207 132.809 69.2207C133.597 69.2207 134.322 68.9609 134.982 68.4414V69.4941C134.367 69.9408 133.554 70.1641 132.542 70.1641C131.553 70.1641 130.776 69.8473 130.211 69.2139C129.646 68.5758 129.363 67.6803 129.363 66.5273C129.363 65.4382 129.671 64.5518 130.286 63.8682C130.906 63.18 131.674 62.8359 132.59 62.8359C133.506 62.8359 134.215 63.1322 134.716 63.7246C135.217 64.3171 135.468 65.1396 135.468 66.1924V66.7803ZM134.319 65.8301C134.315 65.1829 134.158 64.6794 133.848 64.3193C133.542 63.9593 133.116 63.7793 132.569 63.7793C132.041 63.7793 131.592 63.9684 131.223 64.3467C130.854 64.7249 130.626 65.2194 130.539 65.8301H134.319ZM145.988 63L143.89 70H142.728L141.285 64.9893C141.23 64.7979 141.194 64.5814 141.176 64.3398H141.148C141.135 64.5039 141.087 64.7158 141.005 64.9756L139.439 70H138.318L136.199 63H137.375L138.824 68.2637C138.87 68.4232 138.902 68.6328 138.92 68.8926H138.975C138.988 68.6921 139.029 68.4779 139.098 68.25L140.711 63H141.736L143.186 68.2773C143.231 68.446 143.265 68.6556 143.288 68.9062H143.343C143.352 68.7285 143.391 68.5189 143.459 68.2773L144.881 63H145.988ZM152.298 70H151.177V68.9062H151.149C150.662 69.7448 149.944 70.1641 148.996 70.1641C148.299 70.1641 147.752 69.9795 147.355 69.6104C146.964 69.2412 146.768 68.7513 146.768 68.1406C146.768 66.8327 147.538 66.0716 149.078 65.8574L151.177 65.5635C151.177 64.374 150.696 63.7793 149.734 63.7793C148.891 63.7793 148.13 64.0664 147.451 64.6406V63.4922C148.139 63.0547 148.932 62.8359 149.83 62.8359C151.475 62.8359 152.298 63.7064 152.298 65.4473V70ZM151.177 66.459L149.488 66.6914C148.969 66.7643 148.577 66.8942 148.312 67.0811C148.048 67.2633 147.916 67.5892 147.916 68.0586C147.916 68.4004 148.037 68.6807 148.278 68.8994C148.524 69.1136 148.85 69.2207 149.256 69.2207C149.812 69.2207 150.27 69.027 150.63 68.6396C150.994 68.2477 151.177 67.7533 151.177 67.1562V66.459ZM158.061 64.1348C157.865 63.9844 157.582 63.9092 157.213 63.9092C156.734 63.9092 156.333 64.1348 156.01 64.5859C155.691 65.0371 155.531 65.6523 155.531 66.4316V70H154.41V63H155.531V64.4424H155.559C155.718 63.9502 155.962 63.5674 156.29 63.2939C156.618 63.016 156.985 62.877 157.391 62.877C157.682 62.877 157.906 62.9089 158.061 62.9727V64.1348ZM164.903 66.7803H159.961C159.979 67.5596 160.189 68.1611 160.59 68.585C160.991 69.0088 161.542 69.2207 162.244 69.2207C163.033 69.2207 163.757 68.9609 164.418 68.4414V69.4941C163.803 69.9408 162.989 70.1641 161.978 70.1641C160.989 70.1641 160.212 69.8473 159.646 69.2139C159.081 68.5758 158.799 67.6803 158.799 66.5273C158.799 65.4382 159.106 64.5518 159.722 63.8682C160.341 63.18 161.109 62.8359 162.025 62.8359C162.941 62.8359 163.65 63.1322 164.151 63.7246C164.653 64.3171 164.903 65.1396 164.903 66.1924V66.7803ZM163.755 65.8301C163.75 65.1829 163.593 64.6794 163.283 64.3193C162.978 63.9593 162.552 63.7793 162.005 63.7793C161.476 63.7793 161.027 63.9684 160.658 64.3467C160.289 64.7249 160.061 65.2194 159.975 65.8301H163.755ZM174.549 70.1641C173.159 70.1641 172.045 69.7061 171.206 68.79C170.372 67.874 169.955 66.6823 169.955 65.2148C169.955 63.638 170.381 62.3802 171.233 61.4414C172.086 60.5026 173.245 60.0332 174.713 60.0332C176.066 60.0332 177.156 60.4889 177.98 61.4004C178.81 62.3118 179.225 63.5036 179.225 64.9756C179.225 66.5752 178.801 67.8398 177.953 68.7695C177.105 69.6992 175.971 70.1641 174.549 70.1641ZM174.631 61.0723C173.601 61.0723 172.765 61.4437 172.122 62.1865C171.479 62.9294 171.158 63.9046 171.158 65.1123C171.158 66.32 171.47 67.293 172.095 68.0312C172.724 68.765 173.542 69.1318 174.549 69.1318C175.624 69.1318 176.472 68.7809 177.092 68.0791C177.712 67.3773 178.021 66.3952 178.021 65.1328C178.021 63.8385 177.721 62.8382 177.119 62.1318C176.518 61.4255 175.688 61.0723 174.631 61.0723ZM180.694 69.6035V68.25C180.849 68.3867 181.034 68.5098 181.248 68.6191C181.467 68.7285 181.695 68.8219 181.932 68.8994C182.173 68.9723 182.415 69.0293 182.656 69.0703C182.898 69.1113 183.121 69.1318 183.326 69.1318C184.033 69.1318 184.559 69.002 184.905 68.7422C185.256 68.4779 185.432 68.0996 185.432 67.6074C185.432 67.3431 185.372 67.113 185.254 66.917C185.14 66.721 184.98 66.5433 184.775 66.3838C184.57 66.2197 184.326 66.0648 184.044 65.9189C183.766 65.7686 183.465 65.6113 183.142 65.4473C182.8 65.2741 182.481 65.0986 182.185 64.9209C181.888 64.7432 181.631 64.5472 181.412 64.333C181.193 64.1188 181.02 63.8773 180.893 63.6084C180.77 63.335 180.708 63.016 180.708 62.6514C180.708 62.2048 180.806 61.8174 181.002 61.4893C181.198 61.1566 181.455 60.8831 181.774 60.6689C182.093 60.4548 182.456 60.2952 182.861 60.1904C183.271 60.0856 183.688 60.0332 184.112 60.0332C185.078 60.0332 185.783 60.1494 186.225 60.3818V61.6738C185.646 61.2728 184.903 61.0723 183.996 61.0723C183.745 61.0723 183.495 61.0996 183.244 61.1543C182.993 61.2044 182.77 61.2887 182.574 61.4072C182.378 61.5257 182.219 61.6784 182.096 61.8652C181.973 62.0521 181.911 62.2799 181.911 62.5488C181.911 62.7995 181.957 63.016 182.048 63.1982C182.144 63.3805 182.283 63.5469 182.465 63.6973C182.647 63.8477 182.868 63.9935 183.128 64.1348C183.392 64.276 183.695 64.431 184.037 64.5996C184.388 64.7728 184.721 64.9551 185.035 65.1465C185.35 65.3379 185.625 65.5498 185.862 65.7822C186.099 66.0146 186.286 66.2721 186.423 66.5547C186.564 66.8372 186.635 67.1608 186.635 67.5254C186.635 68.0085 186.539 68.4186 186.348 68.7559C186.161 69.0885 185.906 69.3597 185.582 69.5693C185.263 69.779 184.894 69.9294 184.475 70.0205C184.055 70.1162 183.613 70.1641 183.148 70.1641C182.993 70.1641 182.802 70.1504 182.574 70.123C182.346 70.1003 182.114 70.0638 181.877 70.0137C181.64 69.9681 181.414 69.9111 181.2 69.8428C180.991 69.7699 180.822 69.6901 180.694 69.6035ZM198.01 64.5107C198.01 65.4085 197.921 66.2083 197.743 66.9102C197.565 67.6074 197.306 68.1999 196.964 68.6875C196.622 69.1706 196.205 69.5397 195.713 69.7949C195.221 70.0456 194.66 70.1709 194.031 70.1709C193.384 70.1709 192.814 70.057 192.322 69.8291V68.7559C192.865 69.0612 193.443 69.2139 194.059 69.2139C194.501 69.2139 194.895 69.1227 195.241 68.9404C195.592 68.7581 195.888 68.4938 196.13 68.1475C196.371 67.7965 196.556 67.3659 196.684 66.8555C196.811 66.3451 196.875 65.7594 196.875 65.0986H196.848C196.428 65.9417 195.699 66.3633 194.66 66.3633C194.241 66.3633 193.856 66.2904 193.505 66.1445C193.154 65.9941 192.851 65.7845 192.596 65.5156C192.34 65.2422 192.142 64.9186 192.001 64.5449C191.86 64.1712 191.789 63.7588 191.789 63.3076C191.789 62.8245 191.867 62.3825 192.021 61.9814C192.181 61.5804 192.4 61.2363 192.678 60.9492C192.96 60.6576 193.293 60.432 193.676 60.2725C194.063 60.113 194.485 60.0332 194.94 60.0332C195.433 60.0332 195.868 60.1335 196.246 60.334C196.629 60.5299 196.95 60.8193 197.21 61.2021C197.47 61.5804 197.668 62.0475 197.805 62.6035C197.941 63.1595 198.01 63.7952 198.01 64.5107ZM196.8 63.5059C196.8 63.1276 196.75 62.7835 196.649 62.4736C196.554 62.1637 196.419 61.8994 196.246 61.6807C196.073 61.4574 195.866 61.2865 195.624 61.168C195.387 61.0449 195.127 60.9834 194.845 60.9834C194.576 60.9834 194.325 61.0381 194.093 61.1475C193.86 61.2523 193.658 61.4027 193.484 61.5986C193.316 61.79 193.181 62.0202 193.081 62.2891C192.985 62.5534 192.938 62.8428 192.938 63.1572C192.938 63.5036 192.983 63.8135 193.074 64.0869C193.17 64.3604 193.304 64.5928 193.478 64.7842C193.651 64.971 193.858 65.1146 194.1 65.2148C194.346 65.3151 194.617 65.3652 194.913 65.3652C195.173 65.3652 195.417 65.3174 195.645 65.2217C195.877 65.1214 196.077 64.9893 196.246 64.8252C196.419 64.6566 196.554 64.4606 196.649 64.2373C196.75 64.0094 196.8 63.7656 196.8 63.5059Z" fill="black"/>
-    <rect x="102" y="78" width="3" height="3" fill="#4B003F"/>
-    <path d="M197 78H200V81H197V78Z" fill="#4B003F"/>
-    <rect x="103" y="79" width="96" height="1" fill="#4B003F"/>
-    <path d="M102.65 92.6885V91.625C102.772 91.7324 102.917 91.8291 103.085 91.915C103.257 92.001 103.436 92.0744 103.622 92.1353C103.812 92.1925 104.002 92.2373 104.191 92.2695C104.381 92.3018 104.557 92.3179 104.718 92.3179C105.273 92.3179 105.686 92.2158 105.958 92.0117C106.234 91.804 106.372 91.5068 106.372 91.1201C106.372 90.9124 106.326 90.7316 106.232 90.5776C106.143 90.4237 106.018 90.284 105.856 90.1587C105.695 90.0298 105.504 89.908 105.282 89.7935C105.063 89.6753 104.827 89.5518 104.573 89.4229C104.304 89.2868 104.054 89.1489 103.821 89.0093C103.588 88.8696 103.386 88.7157 103.214 88.5474C103.042 88.3791 102.906 88.1893 102.806 87.978C102.709 87.7632 102.661 87.5125 102.661 87.2261C102.661 86.8752 102.738 86.5708 102.892 86.313C103.046 86.0516 103.248 85.8368 103.499 85.6685C103.749 85.5002 104.034 85.3748 104.353 85.2925C104.675 85.2101 105.002 85.1689 105.335 85.1689C106.095 85.1689 106.648 85.2603 106.995 85.4429V86.458C106.54 86.1429 105.957 85.9854 105.244 85.9854C105.047 85.9854 104.85 86.0068 104.653 86.0498C104.456 86.0892 104.281 86.1554 104.127 86.2485C103.973 86.3416 103.848 86.4616 103.751 86.6084C103.654 86.7552 103.606 86.9342 103.606 87.1455C103.606 87.3424 103.642 87.5125 103.713 87.6558C103.789 87.799 103.898 87.9297 104.041 88.0479C104.184 88.166 104.358 88.2806 104.562 88.3916C104.77 88.5026 105.008 88.6243 105.276 88.7568C105.552 88.8929 105.813 89.0361 106.061 89.1865C106.308 89.3369 106.524 89.5034 106.71 89.686C106.897 89.8687 107.043 90.071 107.151 90.293C107.262 90.515 107.317 90.7692 107.317 91.0557C107.317 91.4352 107.242 91.7575 107.092 92.0225C106.945 92.2839 106.744 92.4969 106.49 92.6616C106.24 92.8263 105.95 92.9445 105.62 93.0161C105.291 93.0913 104.943 93.1289 104.578 93.1289C104.456 93.1289 104.306 93.1182 104.127 93.0967C103.948 93.0788 103.765 93.0501 103.579 93.0107C103.393 92.9749 103.216 92.9302 103.047 92.8765C102.883 92.8192 102.75 92.7565 102.65 92.6885ZM111.034 93.1289C110.221 93.1289 109.571 92.8729 109.084 92.3608C108.601 91.8452 108.359 91.1631 108.359 90.3145C108.359 89.3906 108.612 88.6691 109.117 88.1499C109.622 87.6307 110.304 87.3711 111.163 87.3711C111.983 87.3711 112.622 87.6235 113.081 88.1284C113.542 88.6333 113.773 89.3333 113.773 90.2285C113.773 91.1058 113.525 91.8094 113.027 92.3394C112.533 92.8657 111.868 93.1289 111.034 93.1289ZM111.099 88.1123C110.533 88.1123 110.085 88.3057 109.756 88.6924C109.426 89.0755 109.262 89.6055 109.262 90.2822C109.262 90.9339 109.428 91.4478 109.761 91.8237C110.094 92.1997 110.54 92.3877 111.099 92.3877C111.668 92.3877 112.105 92.2033 112.409 91.8345C112.717 91.4657 112.871 90.9411 112.871 90.2607C112.871 89.5732 112.717 89.0433 112.409 88.6709C112.105 88.2985 111.668 88.1123 111.099 88.1123ZM117.898 85.6309C117.727 85.5342 117.531 85.4858 117.313 85.4858C116.697 85.4858 116.389 85.8743 116.389 86.6514V87.5H117.678V88.252H116.389V93H115.514V88.252H114.574V87.5H115.514V86.6084C115.514 86.0319 115.68 85.5771 116.013 85.2441C116.346 84.9076 116.762 84.7393 117.259 84.7393C117.528 84.7393 117.741 84.7715 117.898 84.8359V85.6309ZM121.18 92.9463C120.972 93.0609 120.699 93.1182 120.358 93.1182C119.395 93.1182 118.914 92.5811 118.914 91.5068V88.252H117.968V87.5H118.914V86.1572L119.794 85.8726V87.5H121.18V88.252H119.794V91.3511C119.794 91.7199 119.857 91.9831 119.982 92.1406C120.108 92.2982 120.315 92.377 120.605 92.377C120.827 92.377 121.019 92.3161 121.18 92.1943V92.9463ZM129.285 87.5L127.636 93H126.723L125.59 89.063C125.547 88.9126 125.518 88.7425 125.504 88.5527H125.482C125.472 88.6816 125.434 88.8481 125.37 89.0522L124.14 93H123.259L121.594 87.5H122.518L123.656 91.6357C123.692 91.7611 123.717 91.9258 123.731 92.1299H123.774C123.785 91.9723 123.817 91.804 123.871 91.625L125.139 87.5H125.944L127.083 91.6465C127.119 91.779 127.146 91.9437 127.164 92.1406H127.207C127.214 92.001 127.244 91.8363 127.298 91.6465L128.415 87.5H129.285ZM134.243 93H133.362V92.1406H133.34C132.957 92.7995 132.393 93.1289 131.648 93.1289C131.101 93.1289 130.671 92.9839 130.359 92.6938C130.051 92.4038 129.897 92.0189 129.897 91.5391C129.897 90.5114 130.503 89.9134 131.713 89.7451L133.362 89.5142C133.362 88.5796 132.984 88.1123 132.229 88.1123C131.566 88.1123 130.968 88.3379 130.435 88.7891V87.8867C130.975 87.543 131.598 87.3711 132.304 87.3711C133.596 87.3711 134.243 88.055 134.243 89.4229V93ZM133.362 90.2178L132.035 90.4004C131.627 90.4577 131.319 90.5597 131.111 90.7065C130.904 90.8498 130.8 91.1058 130.8 91.4746C130.8 91.7432 130.895 91.9634 131.084 92.1353C131.278 92.3035 131.534 92.3877 131.853 92.3877C132.289 92.3877 132.649 92.2355 132.932 91.9312C133.219 91.6232 133.362 91.2347 133.362 90.7656V90.2178ZM138.771 88.3916C138.617 88.2734 138.395 88.2144 138.104 88.2144C137.729 88.2144 137.413 88.3916 137.159 88.7461C136.909 89.1006 136.783 89.584 136.783 90.1963V93H135.902V87.5H136.783V88.6333H136.805C136.93 88.2466 137.122 87.9458 137.379 87.731C137.637 87.5125 137.925 87.4033 138.244 87.4033C138.473 87.4033 138.649 87.4284 138.771 87.4785V88.3916ZM144.147 90.4702H140.264C140.278 91.0825 140.443 91.5552 140.758 91.8882C141.073 92.2212 141.506 92.3877 142.058 92.3877C142.677 92.3877 143.246 92.1836 143.766 91.7754V92.6025C143.282 92.9535 142.643 93.1289 141.848 93.1289C141.071 93.1289 140.461 92.88 140.017 92.3823C139.573 91.881 139.351 91.1774 139.351 90.2715C139.351 89.4157 139.592 88.7192 140.076 88.1821C140.563 87.6414 141.166 87.3711 141.886 87.3711C142.605 87.3711 143.162 87.6038 143.556 88.0693C143.95 88.5348 144.147 89.1812 144.147 90.0083V90.4702ZM143.245 89.7236C143.241 89.2152 143.118 88.8195 142.874 88.5366C142.634 88.2537 142.299 88.1123 141.87 88.1123C141.454 88.1123 141.102 88.2609 140.812 88.5581C140.521 88.8553 140.342 89.2438 140.274 89.7236H143.245Z" fill="#4B003F"/>
-    <path d="M21.9375 30H20.9609L19.7891 28.0371C19.6816 27.8548 19.5775 27.7002 19.4766 27.5732C19.3757 27.443 19.2715 27.3372 19.1641 27.2559C19.0599 27.1745 18.946 27.1159 18.8223 27.0801C18.7018 27.041 18.5651 27.0215 18.4121 27.0215H17.7383V30H16.918V22.998H19.0078C19.3138 22.998 19.5954 23.0371 19.8525 23.1152C20.113 23.1901 20.3376 23.3057 20.5264 23.4619C20.7184 23.6182 20.8682 23.8135 20.9756 24.0479C21.083 24.279 21.1367 24.5508 21.1367 24.8633C21.1367 25.1074 21.0993 25.332 21.0244 25.5371C20.9528 25.7389 20.8486 25.9196 20.7119 26.0791C20.5785 26.2386 20.4157 26.3753 20.2236 26.4893C20.0348 26.5999 19.8216 26.6862 19.584 26.748V26.7676C19.7012 26.8197 19.8021 26.8799 19.8867 26.9482C19.9746 27.0133 20.0576 27.0915 20.1357 27.1826C20.2139 27.2738 20.2904 27.3779 20.3652 27.4951C20.4434 27.609 20.5296 27.7425 20.624 27.8955L21.9375 30ZM17.7383 23.7402V26.2793H18.8516C19.0566 26.2793 19.2454 26.2484 19.418 26.1865C19.5938 26.1247 19.7451 26.0368 19.8721 25.9229C19.999 25.8057 20.0983 25.6641 20.1699 25.498C20.2415 25.3288 20.2773 25.14 20.2773 24.9316C20.2773 24.5573 20.1553 24.266 19.9111 24.0576C19.6702 23.846 19.3203 23.7402 18.8613 23.7402H17.7383ZM26.6152 30H22.9043V22.998H26.459V23.7402H23.7246V26.0693H26.2539V26.8066H23.7246V29.2578H26.6152V30ZM32.1035 23.7402H30.082V30H29.2617V23.7402H27.2451V22.998H32.1035V23.7402ZM38.3291 27.168C38.3291 29.1341 37.4421 30.1172 35.668 30.1172C33.9688 30.1172 33.1191 29.1715 33.1191 27.2803V22.998H33.9395V27.2266C33.9395 28.6621 34.5449 29.3799 35.7559 29.3799C36.9245 29.3799 37.5088 28.6865 37.5088 27.2998V22.998H38.3291V27.168ZM45.1016 30H44.125L42.9531 28.0371C42.8457 27.8548 42.7415 27.7002 42.6406 27.5732C42.5397 27.443 42.4355 27.3372 42.3281 27.2559C42.224 27.1745 42.11 27.1159 41.9863 27.0801C41.8659 27.041 41.7292 27.0215 41.5762 27.0215H40.9023V30H40.082V22.998H42.1719C42.4779 22.998 42.7594 23.0371 43.0166 23.1152C43.277 23.1901 43.5016 23.3057 43.6904 23.4619C43.8825 23.6182 44.0322 23.8135 44.1396 24.0479C44.2471 24.279 44.3008 24.5508 44.3008 24.8633C44.3008 25.1074 44.2633 25.332 44.1885 25.5371C44.1169 25.7389 44.0127 25.9196 43.876 26.0791C43.7425 26.2386 43.5798 26.3753 43.3877 26.4893C43.1989 26.5999 42.9857 26.6862 42.748 26.748V26.7676C42.8652 26.8197 42.9661 26.8799 43.0508 26.9482C43.1387 27.0133 43.2217 27.0915 43.2998 27.1826C43.3779 27.2738 43.4544 27.3779 43.5293 27.4951C43.6074 27.609 43.6937 27.7425 43.7881 27.8955L45.1016 30ZM40.9023 23.7402V26.2793H42.0156C42.2207 26.2793 42.4095 26.2484 42.582 26.1865C42.7578 26.1247 42.9092 26.0368 43.0361 25.9229C43.1631 25.8057 43.2624 25.6641 43.334 25.498C43.4056 25.3288 43.4414 25.14 43.4414 24.9316C43.4414 24.5573 43.3193 24.266 43.0752 24.0576C42.8343 23.846 42.4844 23.7402 42.0254 23.7402H40.9023ZM51.7129 30H50.707L47.1035 24.4189C47.0124 24.279 46.9375 24.1325 46.8789 23.9795H46.8496C46.8757 24.1292 46.8887 24.4499 46.8887 24.9414V30H46.0684V22.998H47.1328L50.6387 28.4912C50.7852 28.7191 50.8796 28.8753 50.9219 28.96H50.9414C50.9089 28.7581 50.8926 28.4147 50.8926 27.9297V22.998H51.7129V30ZM57.2598 30H53.5488V22.998H57.1035V23.7402H54.3691V26.0693H56.8984V26.8066H54.3691V29.2578H57.2598V30ZM58.6074 30V22.998H60.541C63.0085 22.998 64.2422 24.1357 64.2422 26.4111C64.2422 27.4919 63.8988 28.361 63.2119 29.0186C62.5283 29.6729 61.612 30 60.4629 30H58.6074ZM59.4277 23.7402V29.2578H60.4727C61.3906 29.2578 62.1051 29.012 62.6162 28.5205C63.1273 28.029 63.3828 27.3324 63.3828 26.4307C63.3828 24.637 62.429 23.7402 60.5215 23.7402H59.4277ZM72.0742 30H68.3633V22.998H71.918V23.7402H69.1836V26.0693H71.7129V26.8066H69.1836V29.2578H72.0742V30ZM79.0664 30H78.0605L74.457 24.4189C74.3659 24.279 74.291 24.1325 74.2324 23.9795H74.2031C74.2292 24.1292 74.2422 24.4499 74.2422 24.9414V30H73.4219V22.998H74.4863L77.9922 28.4912C78.1387 28.7191 78.2331 28.8753 78.2754 28.96H78.2949C78.2624 28.7581 78.2461 28.4147 78.2461 27.9297V22.998H79.0664V30ZM85.043 23.7402H83.0215V30H82.2012V23.7402H80.1846V22.998H85.043V23.7402ZM86.9668 30H86.1465V22.998H86.9668V30ZM92.9531 23.7402H90.9316V30H90.1113V23.7402H88.0947V22.998H92.9531V23.7402ZM98.8027 22.998L96.4932 27.4121V30H95.6729V27.4316L93.4219 22.998H94.3545L95.9219 26.1621C95.9414 26.2012 95.9984 26.3444 96.0928 26.5918H96.1074C96.14 26.4811 96.2018 26.3379 96.293 26.1621L97.9336 22.998H98.8027Z" fill="#323130"/>
-</svg>
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "重複領域の例のSVGファイルの削除"
}
```

### Explanation
この変更によって、`union-overlap-example-1-part-2.svg`というSVG画像ファイルが削除されました。このファイルは、カスタムテキスト分析サービスにおける重複領域の視覚的な説明や例を提供していたと思われます。

削除によって、特に画像を活用して概念を理解しやすくしていたユーザーにとっては、情報の欠落が生じる可能性があります。具体的には、モデルの重複領域の把握や、それに基づく分析・判断を行う際に困難が生じるかもしれません。

この変更を受けて、代替の視覚的資料や説明を提供することが強く推奨されます。ユーザーが重複領域の重要性や、その親しみやすさを失わないよう、他の形式の資料（文書や図表など）を検討することが重要です。また、影響を受けるユーザーが必要な情報を得られるよう、GitHubリポジトリ内での詳細な確認を促すことも推奨されます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/union-overlap-example-1.svg{#item-52bda8}

<details>
<summary>Diff</summary>
````diff
@@ -1,13 +0,0 @@
-<svg width="289" height="148" viewBox="0 0 289 148" fill="none"
-    xmlns="http://www.w3.org/2000/svg">
-    <path d="M296 0H0V148H296V0Z" fill="#F3F2F1"/>
-    <path d="M18.4336 70H17.2852V60.1973H18.4336V70ZM33.5273 63L31.4287 70H30.2666L28.8242 64.9893C28.7695 64.7979 28.7331 64.5814 28.7148 64.3398H28.6875C28.6738 64.5039 28.626 64.7158 28.5439 64.9756L26.9785 70H25.8574L23.7383 63H24.9141L26.3633 68.2637C26.4089 68.4232 26.4408 68.6328 26.459 68.8926H26.5137C26.5273 68.6921 26.5684 68.4779 26.6367 68.25L28.25 63H29.2754L30.7246 68.2773C30.7702 68.446 30.8044 68.6556 30.8271 68.9062H30.8818C30.891 68.7285 30.9297 68.5189 30.998 68.2773L32.4199 63H33.5273ZM39.8369 70H38.7158V68.9062H38.6885C38.2008 69.7448 37.4831 70.1641 36.5352 70.1641C35.8379 70.1641 35.291 69.9795 34.8945 69.6104C34.5026 69.2412 34.3066 68.7513 34.3066 68.1406C34.3066 66.8327 35.0768 66.0716 36.6172 65.8574L38.7158 65.5635C38.7158 64.374 38.235 63.7793 37.2734 63.7793C36.4303 63.7793 35.6693 64.0664 34.9902 64.6406V63.4922C35.6784 63.0547 36.4714 62.8359 37.3691 62.8359C39.0143 62.8359 39.8369 63.7064 39.8369 65.4473V70ZM38.7158 66.459L37.0273 66.6914C36.5078 66.7643 36.1159 66.8942 35.8516 67.0811C35.5872 67.2633 35.4551 67.5892 35.4551 68.0586C35.4551 68.4004 35.5758 68.6807 35.8174 68.8994C36.0635 69.1136 36.3893 69.2207 36.7949 69.2207C37.3509 69.2207 37.8089 69.027 38.1689 68.6396C38.5335 68.2477 38.7158 67.7533 38.7158 67.1562V66.459ZM47.7598 70H46.6387V66.0078C46.6387 64.5221 46.0964 63.7793 45.0117 63.7793C44.4512 63.7793 43.9863 63.9912 43.6172 64.415C43.2526 64.8343 43.0703 65.3652 43.0703 66.0078V70H41.9492V63H43.0703V64.1621H43.0977C43.6263 63.278 44.3919 62.8359 45.3945 62.8359C46.1602 62.8359 46.7458 63.0843 47.1514 63.5811C47.557 64.0732 47.7598 64.7865 47.7598 65.7207V70ZM53.126 69.9316C52.8617 70.0775 52.513 70.1504 52.0801 70.1504C50.8542 70.1504 50.2412 69.4668 50.2412 68.0996V63.957H49.0381V63H50.2412V61.291L51.3623 60.9287V63H53.126V63.957H51.3623V67.9014C51.3623 68.3708 51.4421 68.7057 51.6016 68.9062C51.7611 69.1068 52.0254 69.207 52.3945 69.207C52.6771 69.207 52.9209 69.1296 53.126 68.9746V69.9316ZM61.7119 69.9316C61.4476 70.0775 61.099 70.1504 60.666 70.1504C59.4401 70.1504 58.8271 69.4668 58.8271 68.0996V63.957H57.624V63H58.8271V61.291L59.9482 60.9287V63H61.7119V63.957H59.9482V67.9014C59.9482 68.3708 60.028 68.7057 60.1875 68.9062C60.347 69.1068 60.6113 69.207 60.9805 69.207C61.263 69.207 61.5068 69.1296 61.7119 68.9746V69.9316ZM66.1348 70.1641C65.1003 70.1641 64.2731 69.8382 63.6533 69.1865C63.0381 68.5303 62.7305 67.6621 62.7305 66.582C62.7305 65.4062 63.0518 64.488 63.6943 63.8271C64.3369 63.1663 65.2051 62.8359 66.2988 62.8359C67.3424 62.8359 68.1559 63.1572 68.7393 63.7998C69.3271 64.4424 69.6211 65.3333 69.6211 66.4727C69.6211 67.5892 69.3044 68.4847 68.6709 69.1592C68.042 69.8291 67.1966 70.1641 66.1348 70.1641ZM66.2168 63.7793C65.4967 63.7793 64.9271 64.0254 64.5078 64.5176C64.0885 65.0052 63.8789 65.6797 63.8789 66.541C63.8789 67.3704 64.0908 68.0244 64.5146 68.5029C64.9385 68.9814 65.5059 69.2207 66.2168 69.2207C66.9414 69.2207 67.4974 68.986 67.8848 68.5166C68.2767 68.0472 68.4727 67.3796 68.4727 66.5137C68.4727 65.6387 68.2767 64.9642 67.8848 64.4902C67.4974 64.0163 66.9414 63.7793 66.2168 63.7793ZM76.4023 68.9883H76.375V70H75.2539V59.6367H76.375V64.2305H76.4023C76.9538 63.3008 77.7604 62.8359 78.8223 62.8359C79.7201 62.8359 80.4219 63.1504 80.9277 63.7793C81.4382 64.4036 81.6934 65.2422 81.6934 66.2949C81.6934 67.4661 81.4085 68.4049 80.8389 69.1113C80.2692 69.8132 79.4899 70.1641 78.501 70.1641C77.5758 70.1641 76.8763 69.7721 76.4023 68.9883ZM76.375 66.165V67.1426C76.375 67.7214 76.5618 68.2135 76.9355 68.6191C77.3138 69.0202 77.7923 69.2207 78.3711 69.2207C79.0501 69.2207 79.5811 68.9609 79.9639 68.4414C80.3512 67.9219 80.5449 67.1995 80.5449 66.2744C80.5449 65.4951 80.3649 64.8844 80.0049 64.4424C79.6449 64.0003 79.1572 63.7793 78.542 63.7793C77.8903 63.7793 77.3662 64.0072 76.9697 64.4629C76.5732 64.9141 76.375 65.4814 76.375 66.165ZM89.1445 70H88.0234V68.8926H87.9961C87.5312 69.7402 86.8112 70.1641 85.8359 70.1641C84.168 70.1641 83.334 69.1706 83.334 67.1836V63H84.4482V67.0059C84.4482 68.4824 85.0133 69.2207 86.1436 69.2207C86.6904 69.2207 87.1393 69.0202 87.4902 68.6191C87.8457 68.2135 88.0234 67.6849 88.0234 67.0332V63H89.1445V70ZM96.9854 63L93.7656 71.1211C93.1914 72.5703 92.3848 73.2949 91.3457 73.2949C91.054 73.2949 90.8102 73.2653 90.6143 73.2061V72.2012C90.8558 72.2832 91.0768 72.3242 91.2773 72.3242C91.8424 72.3242 92.2663 71.987 92.5488 71.3125L93.1094 69.9863L90.375 63H91.6191L93.5127 68.3867C93.5355 68.4551 93.5833 68.6328 93.6562 68.9199H93.6973C93.7201 68.8105 93.7656 68.6374 93.834 68.4004L95.8232 63H96.9854ZM103.336 66.2949V70H102.188V60.1973H104.881C105.929 60.1973 106.74 60.4525 107.314 60.9629C107.893 61.4733 108.183 62.1934 108.183 63.123C108.183 64.0527 107.861 64.8138 107.219 65.4062C106.581 65.9987 105.717 66.2949 104.628 66.2949H103.336ZM103.336 61.2363V65.2559H104.539C105.332 65.2559 105.936 65.0758 106.351 64.7158C106.77 64.3512 106.979 63.8385 106.979 63.1777C106.979 61.8835 106.214 61.2363 104.683 61.2363H103.336ZM113.535 64.1348C113.339 63.9844 113.057 63.9092 112.688 63.9092C112.209 63.9092 111.808 64.1348 111.484 64.5859C111.165 65.0371 111.006 65.6523 111.006 66.4316V70H109.885V63H111.006V64.4424H111.033C111.193 63.9502 111.437 63.5674 111.765 63.2939C112.093 63.016 112.46 62.877 112.865 62.877C113.157 62.877 113.38 62.9089 113.535 62.9727V64.1348ZM117.678 70.1641C116.643 70.1641 115.816 69.8382 115.196 69.1865C114.581 68.5303 114.273 67.6621 114.273 66.582C114.273 65.4062 114.595 64.488 115.237 63.8271C115.88 63.1663 116.748 62.8359 117.842 62.8359C118.885 62.8359 119.699 63.1572 120.282 63.7998C120.87 64.4424 121.164 65.3333 121.164 66.4727C121.164 67.5892 120.847 68.4847 120.214 69.1592C119.585 69.8291 118.74 70.1641 117.678 70.1641ZM117.76 63.7793C117.04 63.7793 116.47 64.0254 116.051 64.5176C115.632 65.0052 115.422 65.6797 115.422 66.541C115.422 67.3704 115.634 68.0244 116.058 68.5029C116.481 68.9814 117.049 69.2207 117.76 69.2207C118.484 69.2207 119.04 68.986 119.428 68.5166C119.82 68.0472 120.016 67.3796 120.016 66.5137C120.016 65.6387 119.82 64.9642 119.428 64.4902C119.04 64.0163 118.484 63.7793 117.76 63.7793ZM122.531 69.7471V68.5439C123.142 68.9951 123.814 69.2207 124.548 69.2207C125.532 69.2207 126.024 68.8926 126.024 68.2363C126.024 68.0495 125.981 67.8923 125.895 67.7646C125.812 67.6325 125.699 67.5163 125.553 67.416C125.411 67.3158 125.243 67.2269 125.047 67.1494C124.855 67.0674 124.648 66.9831 124.425 66.8965C124.115 66.7734 123.841 66.6504 123.604 66.5273C123.372 66.3997 123.176 66.2585 123.017 66.1035C122.862 65.944 122.743 65.764 122.661 65.5635C122.584 65.363 122.545 65.1283 122.545 64.8594C122.545 64.5312 122.62 64.2419 122.771 63.9912C122.921 63.736 123.121 63.5241 123.372 63.3555C123.623 63.1823 123.908 63.0524 124.227 62.9658C124.55 62.8792 124.883 62.8359 125.225 62.8359C125.831 62.8359 126.373 62.9408 126.852 63.1504V64.2852C126.337 63.9479 125.744 63.7793 125.074 63.7793C124.865 63.7793 124.675 63.8044 124.507 63.8545C124.338 63.9001 124.192 63.9661 124.069 64.0527C123.951 64.1393 123.857 64.2441 123.789 64.3672C123.725 64.4857 123.693 64.6178 123.693 64.7637C123.693 64.946 123.725 65.0986 123.789 65.2217C123.857 65.3447 123.955 65.4541 124.083 65.5498C124.211 65.6455 124.366 65.7321 124.548 65.8096C124.73 65.887 124.938 65.9714 125.17 66.0625C125.48 66.181 125.758 66.304 126.004 66.4316C126.25 66.5547 126.46 66.696 126.633 66.8555C126.806 67.0104 126.938 67.1904 127.029 67.3955C127.125 67.6006 127.173 67.8444 127.173 68.127C127.173 68.4733 127.095 68.7741 126.94 69.0293C126.79 69.2845 126.587 69.4964 126.332 69.665C126.077 69.8337 125.783 69.959 125.45 70.041C125.118 70.123 124.769 70.1641 124.404 70.1641C123.684 70.1641 123.06 70.0251 122.531 69.7471ZM134.528 66.7803H129.586C129.604 67.5596 129.814 68.1611 130.215 68.585C130.616 69.0088 131.167 69.2207 131.869 69.2207C132.658 69.2207 133.382 68.9609 134.043 68.4414V69.4941C133.428 69.9408 132.614 70.1641 131.603 70.1641C130.614 70.1641 129.837 69.8473 129.271 69.2139C128.706 68.5758 128.424 67.6803 128.424 66.5273C128.424 65.4382 128.731 64.5518 129.347 63.8682C129.966 63.18 130.734 62.8359 131.65 62.8359C132.566 62.8359 133.275 63.1322 133.776 63.7246C134.278 64.3171 134.528 65.1396 134.528 66.1924V66.7803ZM133.38 65.8301C133.375 65.1829 133.218 64.6794 132.908 64.3193C132.603 63.9593 132.177 63.7793 131.63 63.7793C131.101 63.7793 130.652 63.9684 130.283 64.3467C129.914 64.7249 129.686 65.2194 129.6 65.8301H133.38ZM145.049 63L142.95 70H141.788L140.346 64.9893C140.291 64.7979 140.255 64.5814 140.236 64.3398H140.209C140.195 64.5039 140.147 64.7158 140.065 64.9756L138.5 70H137.379L135.26 63H136.436L137.885 68.2637C137.93 68.4232 137.962 68.6328 137.98 68.8926H138.035C138.049 68.6921 138.09 68.4779 138.158 68.25L139.771 63H140.797L142.246 68.2773C142.292 68.446 142.326 68.6556 142.349 68.9062H142.403C142.412 68.7285 142.451 68.5189 142.52 68.2773L143.941 63H145.049ZM151.358 70H150.237V68.9062H150.21C149.722 69.7448 149.005 70.1641 148.057 70.1641C147.359 70.1641 146.812 69.9795 146.416 69.6104C146.024 69.2412 145.828 68.7513 145.828 68.1406C145.828 66.8327 146.598 66.0716 148.139 65.8574L150.237 65.5635C150.237 64.374 149.757 63.7793 148.795 63.7793C147.952 63.7793 147.191 64.0664 146.512 64.6406V63.4922C147.2 63.0547 147.993 62.8359 148.891 62.8359C150.536 62.8359 151.358 63.7064 151.358 65.4473V70ZM150.237 66.459L148.549 66.6914C148.029 66.7643 147.637 66.8942 147.373 67.0811C147.109 67.2633 146.977 67.5892 146.977 68.0586C146.977 68.4004 147.097 68.6807 147.339 68.8994C147.585 69.1136 147.911 69.2207 148.316 69.2207C148.872 69.2207 149.33 69.027 149.69 68.6396C150.055 68.2477 150.237 67.7533 150.237 67.1562V66.459ZM157.121 64.1348C156.925 63.9844 156.643 63.9092 156.273 63.9092C155.795 63.9092 155.394 64.1348 155.07 64.5859C154.751 65.0371 154.592 65.6523 154.592 66.4316V70H153.471V63H154.592V64.4424H154.619C154.779 63.9502 155.022 63.5674 155.351 63.2939C155.679 63.016 156.046 62.877 156.451 62.877C156.743 62.877 156.966 62.9089 157.121 62.9727V64.1348ZM163.964 66.7803H159.021C159.04 67.5596 159.249 68.1611 159.65 68.585C160.051 69.0088 160.603 69.2207 161.305 69.2207C162.093 69.2207 162.818 68.9609 163.479 68.4414V69.4941C162.863 69.9408 162.05 70.1641 161.038 70.1641C160.049 70.1641 159.272 69.8473 158.707 69.2139C158.142 68.5758 157.859 67.6803 157.859 66.5273C157.859 65.4382 158.167 64.5518 158.782 63.8682C159.402 63.18 160.17 62.8359 161.086 62.8359C162.002 62.8359 162.711 63.1322 163.212 63.7246C163.713 64.3171 163.964 65.1396 163.964 66.1924V66.7803ZM162.815 65.8301C162.811 65.1829 162.654 64.6794 162.344 64.3193C162.038 63.9593 161.612 63.7793 161.065 63.7793C160.537 63.7793 160.088 63.9684 159.719 64.3467C159.35 64.7249 159.122 65.2194 159.035 65.8301H162.815ZM173.609 70.1641C172.219 70.1641 171.105 69.7061 170.267 68.79C169.433 67.874 169.016 66.6823 169.016 65.2148C169.016 63.638 169.442 62.3802 170.294 61.4414C171.146 60.5026 172.306 60.0332 173.773 60.0332C175.127 60.0332 176.216 60.4889 177.041 61.4004C177.87 62.3118 178.285 63.5036 178.285 64.9756C178.285 66.5752 177.861 67.8398 177.014 68.7695C176.166 69.6992 175.031 70.1641 173.609 70.1641ZM173.691 61.0723C172.661 61.0723 171.825 61.4437 171.183 62.1865C170.54 62.9294 170.219 63.9046 170.219 65.1123C170.219 66.32 170.531 67.293 171.155 68.0312C171.784 68.765 172.602 69.1318 173.609 69.1318C174.685 69.1318 175.533 68.7809 176.152 68.0791C176.772 67.3773 177.082 66.3952 177.082 65.1328C177.082 63.8385 176.781 62.8382 176.18 62.1318C175.578 61.4255 174.749 61.0723 173.691 61.0723ZM179.755 69.6035V68.25C179.91 68.3867 180.094 68.5098 180.309 68.6191C180.527 68.7285 180.755 68.8219 180.992 68.8994C181.234 68.9723 181.475 69.0293 181.717 69.0703C181.958 69.1113 182.182 69.1318 182.387 69.1318C183.093 69.1318 183.619 69.002 183.966 68.7422C184.317 68.4779 184.492 68.0996 184.492 67.6074C184.492 67.3431 184.433 67.113 184.314 66.917C184.201 66.721 184.041 66.5433 183.836 66.3838C183.631 66.2197 183.387 66.0648 183.104 65.9189C182.826 65.7686 182.526 65.6113 182.202 65.4473C181.86 65.2741 181.541 65.0986 181.245 64.9209C180.949 64.7432 180.691 64.5472 180.473 64.333C180.254 64.1188 180.081 63.8773 179.953 63.6084C179.83 63.335 179.769 63.016 179.769 62.6514C179.769 62.2048 179.867 61.8174 180.062 61.4893C180.258 61.1566 180.516 60.8831 180.835 60.6689C181.154 60.4548 181.516 60.2952 181.922 60.1904C182.332 60.0856 182.749 60.0332 183.173 60.0332C184.139 60.0332 184.843 60.1494 185.285 60.3818V61.6738C184.706 61.2728 183.964 61.0723 183.057 61.0723C182.806 61.0723 182.555 61.0996 182.305 61.1543C182.054 61.2044 181.831 61.2887 181.635 61.4072C181.439 61.5257 181.279 61.6784 181.156 61.8652C181.033 62.0521 180.972 62.2799 180.972 62.5488C180.972 62.7995 181.017 63.016 181.108 63.1982C181.204 63.3805 181.343 63.5469 181.525 63.6973C181.708 63.8477 181.929 63.9935 182.188 64.1348C182.453 64.276 182.756 64.431 183.098 64.5996C183.449 64.7728 183.781 64.9551 184.096 65.1465C184.41 65.3379 184.686 65.5498 184.923 65.7822C185.16 66.0146 185.347 66.2721 185.483 66.5547C185.625 66.8372 185.695 67.1608 185.695 67.5254C185.695 68.0085 185.6 68.4186 185.408 68.7559C185.221 69.0885 184.966 69.3597 184.643 69.5693C184.324 69.779 183.954 69.9294 183.535 70.0205C183.116 70.1162 182.674 70.1641 182.209 70.1641C182.054 70.1641 181.863 70.1504 181.635 70.123C181.407 70.1003 181.174 70.0638 180.938 70.0137C180.701 69.9681 180.475 69.9111 180.261 69.8428C180.051 69.7699 179.882 69.6901 179.755 69.6035ZM197.07 64.5107C197.07 65.4085 196.981 66.2083 196.804 66.9102C196.626 67.6074 196.366 68.1999 196.024 68.6875C195.683 69.1706 195.266 69.5397 194.773 69.7949C194.281 70.0456 193.721 70.1709 193.092 70.1709C192.445 70.1709 191.875 70.057 191.383 69.8291V68.7559C191.925 69.0612 192.504 69.2139 193.119 69.2139C193.561 69.2139 193.955 69.1227 194.302 68.9404C194.653 68.7581 194.949 68.4938 195.19 68.1475C195.432 67.7965 195.617 67.3659 195.744 66.8555C195.872 66.3451 195.936 65.7594 195.936 65.0986H195.908C195.489 65.9417 194.76 66.3633 193.721 66.3633C193.301 66.3633 192.916 66.2904 192.565 66.1445C192.215 65.9941 191.911 65.7845 191.656 65.5156C191.401 65.2422 191.203 64.9186 191.062 64.5449C190.92 64.1712 190.85 63.7588 190.85 63.3076C190.85 62.8245 190.927 62.3825 191.082 61.9814C191.242 61.5804 191.46 61.2363 191.738 60.9492C192.021 60.6576 192.354 60.432 192.736 60.2725C193.124 60.113 193.545 60.0332 194.001 60.0332C194.493 60.0332 194.928 60.1335 195.307 60.334C195.689 60.5299 196.011 60.8193 196.271 61.2021C196.53 61.5804 196.729 62.0475 196.865 62.6035C197.002 63.1595 197.07 63.7952 197.07 64.5107ZM195.86 63.5059C195.86 63.1276 195.81 62.7835 195.71 62.4736C195.614 62.1637 195.48 61.8994 195.307 61.6807C195.133 61.4574 194.926 61.2865 194.685 61.168C194.448 61.0449 194.188 60.9834 193.905 60.9834C193.636 60.9834 193.386 61.0381 193.153 61.1475C192.921 61.2523 192.718 61.4027 192.545 61.5986C192.376 61.79 192.242 62.0202 192.142 62.2891C192.046 62.5534 191.998 62.8428 191.998 63.1572C191.998 63.5036 192.044 63.8135 192.135 64.0869C192.23 64.3604 192.365 64.5928 192.538 64.7842C192.711 64.971 192.919 65.1146 193.16 65.2148C193.406 65.3151 193.677 65.3652 193.974 65.3652C194.233 65.3652 194.477 65.3174 194.705 65.2217C194.938 65.1214 195.138 64.9893 195.307 64.8252C195.48 64.6566 195.614 64.4606 195.71 64.2373C195.81 64.0094 195.86 63.7656 195.86 63.5059Z" fill="black"/>
-    <rect x="102" y="78" width="3" height="3" fill="#00188F"/>
-    <path d="M195 78H198V81H195V78Z" fill="#00188F"/>
-    <rect x="103" y="79" width="94" height="1" fill="#00188F"/>
-    <path d="M102.65 92.6885V91.625C102.772 91.7324 102.917 91.8291 103.085 91.915C103.257 92.001 103.436 92.0744 103.622 92.1353C103.812 92.1925 104.002 92.2373 104.191 92.2695C104.381 92.3018 104.557 92.3179 104.718 92.3179C105.273 92.3179 105.686 92.2158 105.958 92.0117C106.234 91.804 106.372 91.5068 106.372 91.1201C106.372 90.9124 106.326 90.7316 106.232 90.5776C106.143 90.4237 106.018 90.284 105.856 90.1587C105.695 90.0298 105.504 89.908 105.282 89.7935C105.063 89.6753 104.827 89.5518 104.573 89.4229C104.304 89.2868 104.054 89.1489 103.821 89.0093C103.588 88.8696 103.386 88.7157 103.214 88.5474C103.042 88.3791 102.906 88.1893 102.806 87.978C102.709 87.7632 102.661 87.5125 102.661 87.2261C102.661 86.8752 102.738 86.5708 102.892 86.313C103.046 86.0516 103.248 85.8368 103.499 85.6685C103.749 85.5002 104.034 85.3748 104.353 85.2925C104.675 85.2101 105.002 85.1689 105.335 85.1689C106.095 85.1689 106.648 85.2603 106.995 85.4429V86.458C106.54 86.1429 105.957 85.9854 105.244 85.9854C105.047 85.9854 104.85 86.0068 104.653 86.0498C104.456 86.0892 104.281 86.1554 104.127 86.2485C103.973 86.3416 103.848 86.4616 103.751 86.6084C103.654 86.7552 103.606 86.9342 103.606 87.1455C103.606 87.3424 103.642 87.5125 103.713 87.6558C103.789 87.799 103.898 87.9297 104.041 88.0479C104.184 88.166 104.358 88.2806 104.562 88.3916C104.77 88.5026 105.008 88.6243 105.276 88.7568C105.552 88.8929 105.813 89.0361 106.061 89.1865C106.308 89.3369 106.524 89.5034 106.71 89.686C106.897 89.8687 107.043 90.071 107.151 90.293C107.262 90.515 107.317 90.7692 107.317 91.0557C107.317 91.4352 107.242 91.7575 107.092 92.0225C106.945 92.2839 106.744 92.4969 106.49 92.6616C106.24 92.8263 105.95 92.9445 105.62 93.0161C105.291 93.0913 104.943 93.1289 104.578 93.1289C104.456 93.1289 104.306 93.1182 104.127 93.0967C103.948 93.0788 103.765 93.0501 103.579 93.0107C103.393 92.9749 103.216 92.9302 103.047 92.8765C102.883 92.8192 102.75 92.7565 102.65 92.6885ZM111.034 93.1289C110.221 93.1289 109.571 92.8729 109.084 92.3608C108.601 91.8452 108.359 91.1631 108.359 90.3145C108.359 89.3906 108.612 88.6691 109.117 88.1499C109.622 87.6307 110.304 87.3711 111.163 87.3711C111.983 87.3711 112.622 87.6235 113.081 88.1284C113.542 88.6333 113.773 89.3333 113.773 90.2285C113.773 91.1058 113.525 91.8094 113.027 92.3394C112.533 92.8657 111.868 93.1289 111.034 93.1289ZM111.099 88.1123C110.533 88.1123 110.085 88.3057 109.756 88.6924C109.426 89.0755 109.262 89.6055 109.262 90.2822C109.262 90.9339 109.428 91.4478 109.761 91.8237C110.094 92.1997 110.54 92.3877 111.099 92.3877C111.668 92.3877 112.105 92.2033 112.409 91.8345C112.717 91.4657 112.871 90.9411 112.871 90.2607C112.871 89.5732 112.717 89.0433 112.409 88.6709C112.105 88.2985 111.668 88.1123 111.099 88.1123ZM117.898 85.6309C117.727 85.5342 117.531 85.4858 117.313 85.4858C116.697 85.4858 116.389 85.8743 116.389 86.6514V87.5H117.678V88.252H116.389V93H115.514V88.252H114.574V87.5H115.514V86.6084C115.514 86.0319 115.68 85.5771 116.013 85.2441C116.346 84.9076 116.762 84.7393 117.259 84.7393C117.528 84.7393 117.741 84.7715 117.898 84.8359V85.6309ZM121.18 92.9463C120.972 93.0609 120.699 93.1182 120.358 93.1182C119.395 93.1182 118.914 92.5811 118.914 91.5068V88.252H117.968V87.5H118.914V86.1572L119.794 85.8726V87.5H121.18V88.252H119.794V91.3511C119.794 91.7199 119.857 91.9831 119.982 92.1406C120.108 92.2982 120.315 92.377 120.605 92.377C120.827 92.377 121.019 92.3161 121.18 92.1943V92.9463ZM129.285 87.5L127.636 93H126.723L125.59 89.063C125.547 88.9126 125.518 88.7425 125.504 88.5527H125.482C125.472 88.6816 125.434 88.8481 125.37 89.0522L124.14 93H123.259L121.594 87.5H122.518L123.656 91.6357C123.692 91.7611 123.717 91.9258 123.731 92.1299H123.774C123.785 91.9723 123.817 91.804 123.871 91.625L125.139 87.5H125.944L127.083 91.6465C127.119 91.779 127.146 91.9437 127.164 92.1406H127.207C127.214 92.001 127.244 91.8363 127.298 91.6465L128.415 87.5H129.285ZM134.243 93H133.362V92.1406H133.34C132.957 92.7995 132.393 93.1289 131.648 93.1289C131.101 93.1289 130.671 92.9839 130.359 92.6938C130.051 92.4038 129.897 92.0189 129.897 91.5391C129.897 90.5114 130.503 89.9134 131.713 89.7451L133.362 89.5142C133.362 88.5796 132.984 88.1123 132.229 88.1123C131.566 88.1123 130.968 88.3379 130.435 88.7891V87.8867C130.975 87.543 131.598 87.3711 132.304 87.3711C133.596 87.3711 134.243 88.055 134.243 89.4229V93ZM133.362 90.2178L132.035 90.4004C131.627 90.4577 131.319 90.5597 131.111 90.7065C130.904 90.8498 130.8 91.1058 130.8 91.4746C130.8 91.7432 130.895 91.9634 131.084 92.1353C131.278 92.3035 131.534 92.3877 131.853 92.3877C132.289 92.3877 132.649 92.2355 132.932 91.9312C133.219 91.6232 133.362 91.2347 133.362 90.7656V90.2178ZM138.771 88.3916C138.617 88.2734 138.395 88.2144 138.104 88.2144C137.729 88.2144 137.413 88.3916 137.159 88.7461C136.909 89.1006 136.783 89.584 136.783 90.1963V93H135.902V87.5H136.783V88.6333H136.805C136.93 88.2466 137.122 87.9458 137.379 87.731C137.637 87.5125 137.925 87.4033 138.244 87.4033C138.473 87.4033 138.649 87.4284 138.771 87.4785V88.3916ZM144.147 90.4702H140.264C140.278 91.0825 140.443 91.5552 140.758 91.8882C141.073 92.2212 141.506 92.3877 142.058 92.3877C142.677 92.3877 143.246 92.1836 143.766 91.7754V92.6025C143.282 92.9535 142.643 93.1289 141.848 93.1289C141.071 93.1289 140.461 92.88 140.017 92.3823C139.573 91.881 139.351 91.1774 139.351 90.2715C139.351 89.4157 139.592 88.7192 140.076 88.1821C140.563 87.6414 141.166 87.3711 141.886 87.3711C142.605 87.3711 143.162 87.6038 143.556 88.0693C143.95 88.5348 144.147 89.1812 144.147 90.0083V90.4702ZM143.245 89.7236C143.241 89.2152 143.118 88.8195 142.874 88.5366C142.634 88.2537 142.299 88.1123 141.87 88.1123C141.454 88.1123 141.102 88.2609 140.812 88.5581C140.521 88.8553 140.342 89.2438 140.274 89.7236H143.245ZM150.812 94.751H150.028C148.918 93.4834 148.363 91.9204 148.363 90.062C148.363 88.1965 148.918 86.6084 150.028 85.2979H150.823C149.699 86.6585 149.137 88.243 149.137 90.0513C149.137 91.8452 149.695 93.4118 150.812 94.751ZM152.703 93H151.822V84.8574H152.703V93ZM158.907 90.4702H155.023C155.038 91.0825 155.202 91.5552 155.518 91.8882C155.833 92.2212 156.266 92.3877 156.817 92.3877C157.437 92.3877 158.006 92.1836 158.525 91.7754V92.6025C158.042 92.9535 157.403 93.1289 156.608 93.1289C155.831 93.1289 155.22 92.88 154.776 92.3823C154.332 91.881 154.11 91.1774 154.11 90.2715C154.11 89.4157 154.352 88.7192 154.835 88.1821C155.322 87.6414 155.926 87.3711 156.646 87.3711C157.365 87.3711 157.922 87.6038 158.316 88.0693C158.71 88.5348 158.907 89.1812 158.907 90.0083V90.4702ZM158.004 89.7236C158.001 89.2152 157.877 88.8195 157.634 88.5366C157.394 88.2537 157.059 88.1123 156.629 88.1123C156.214 88.1123 155.861 88.2609 155.571 88.5581C155.281 88.8553 155.102 89.2438 155.034 89.7236H158.004ZM164.181 93H163.3V92.1406H163.279C162.896 92.7995 162.332 93.1289 161.587 93.1289C161.039 93.1289 160.609 92.9839 160.298 92.6938C159.99 92.4038 159.836 92.0189 159.836 91.5391C159.836 90.5114 160.441 89.9134 161.651 89.7451L163.3 89.5142C163.3 88.5796 162.923 88.1123 162.167 88.1123C161.505 88.1123 160.907 88.3379 160.373 88.7891V87.8867C160.914 87.543 161.537 87.3711 162.242 87.3711C163.535 87.3711 164.181 88.055 164.181 89.4229V93ZM163.3 90.2178L161.974 90.4004C161.565 90.4577 161.257 90.5597 161.05 90.7065C160.842 90.8498 160.738 91.1058 160.738 91.4746C160.738 91.7432 160.833 91.9634 161.023 92.1353C161.216 92.3035 161.472 92.3877 161.791 92.3877C162.228 92.3877 162.588 92.2355 162.871 91.9312C163.157 91.6232 163.3 91.2347 163.3 90.7656V90.2178ZM168.709 88.3916C168.555 88.2734 168.333 88.2144 168.043 88.2144C167.667 88.2144 167.352 88.3916 167.098 88.7461C166.847 89.1006 166.722 89.584 166.722 90.1963V93H165.841V87.5H166.722V88.6333H166.743C166.868 88.2466 167.06 87.9458 167.318 87.731C167.576 87.5125 167.864 87.4033 168.183 87.4033C168.412 87.4033 168.587 87.4284 168.709 87.4785V88.3916ZM174.23 93H173.35V89.8633C173.35 88.696 172.924 88.1123 172.071 88.1123C171.631 88.1123 171.266 88.2788 170.976 88.6118C170.689 88.9412 170.546 89.3584 170.546 89.8633V93H169.665V87.5H170.546V88.4131H170.567C170.983 87.7184 171.584 87.3711 172.372 87.3711C172.974 87.3711 173.434 87.5662 173.752 87.9565C174.071 88.3433 174.23 88.9036 174.23 89.6377V93ZM180.316 90.4702H176.433C176.447 91.0825 176.612 91.5552 176.927 91.8882C177.242 92.2212 177.675 92.3877 178.227 92.3877C178.846 92.3877 179.415 92.1836 179.935 91.7754V92.6025C179.451 92.9535 178.812 93.1289 178.017 93.1289C177.24 93.1289 176.63 92.88 176.186 92.3823C175.742 91.881 175.52 91.1774 175.52 90.2715C175.52 89.4157 175.761 88.7192 176.245 88.1821C176.732 87.6414 177.335 87.3711 178.055 87.3711C178.774 87.3711 179.331 87.6038 179.725 88.0693C180.119 88.5348 180.316 89.1812 180.316 90.0083V90.4702ZM179.414 89.7236C179.41 89.2152 179.286 88.8195 179.043 88.5366C178.803 88.2537 178.468 88.1123 178.039 88.1123C177.623 88.1123 177.271 88.2609 176.98 88.5581C176.69 88.8553 176.511 89.2438 176.443 89.7236H179.414ZM186.348 93H185.467V92.0654H185.445C185.037 92.7744 184.407 93.1289 183.555 93.1289C182.864 93.1289 182.31 92.8836 181.895 92.3931C181.483 91.8989 181.277 91.2275 181.277 90.3789C181.277 89.4694 181.507 88.7407 181.965 88.1929C182.423 87.645 183.034 87.3711 183.796 87.3711C184.552 87.3711 185.102 87.6683 185.445 88.2627H185.467V84.8574H186.348V93ZM185.467 90.5132V89.7021C185.467 89.2581 185.32 88.8822 185.026 88.5742C184.733 88.2663 184.36 88.1123 183.909 88.1123C183.372 88.1123 182.95 88.3092 182.642 88.7031C182.334 89.097 182.18 89.6413 182.18 90.3359C182.18 90.9697 182.326 91.471 182.62 91.8398C182.917 92.2051 183.315 92.3877 183.812 92.3877C184.303 92.3877 184.701 92.2104 185.005 91.856C185.313 91.5015 185.467 91.0539 185.467 90.5132ZM188.152 94.751H187.368C188.485 93.4118 189.044 91.8452 189.044 90.0513C189.044 88.243 188.482 86.6585 187.357 85.2979H188.152C189.27 86.6084 189.828 88.1965 189.828 90.062C189.828 91.9204 189.27 93.4834 188.152 94.751Z" fill="#00188F"/>
-    <rect x="102" y="98" width="3" height="3" fill="#EF6950"/>
-    <rect x="103" y="99" width="83" height="1" fill="#EF6950"/>
-    <path d="M102.65 112.688V111.625C102.772 111.732 102.917 111.829 103.085 111.915C103.257 112.001 103.436 112.074 103.622 112.135C103.812 112.193 104.002 112.237 104.191 112.27C104.381 112.302 104.557 112.318 104.718 112.318C105.273 112.318 105.686 112.216 105.958 112.012C106.234 111.804 106.372 111.507 106.372 111.12C106.372 110.912 106.326 110.732 106.232 110.578C106.143 110.424 106.018 110.284 105.856 110.159C105.695 110.03 105.504 109.908 105.282 109.793C105.063 109.675 104.827 109.552 104.573 109.423C104.304 109.287 104.054 109.149 103.821 109.009C103.588 108.87 103.386 108.716 103.214 108.547C103.042 108.379 102.906 108.189 102.806 107.978C102.709 107.763 102.661 107.513 102.661 107.226C102.661 106.875 102.738 106.571 102.892 106.313C103.046 106.052 103.248 105.837 103.499 105.668C103.749 105.5 104.034 105.375 104.353 105.292C104.675 105.21 105.002 105.169 105.335 105.169C106.095 105.169 106.648 105.26 106.995 105.443V106.458C106.54 106.143 105.957 105.985 105.244 105.985C105.047 105.985 104.85 106.007 104.653 106.05C104.456 106.089 104.281 106.155 104.127 106.249C103.973 106.342 103.848 106.462 103.751 106.608C103.654 106.755 103.606 106.934 103.606 107.146C103.606 107.342 103.642 107.513 103.713 107.656C103.789 107.799 103.898 107.93 104.041 108.048C104.184 108.166 104.358 108.281 104.562 108.392C104.77 108.503 105.008 108.624 105.276 108.757C105.552 108.893 105.813 109.036 106.061 109.187C106.308 109.337 106.524 109.503 106.71 109.686C106.897 109.869 107.043 110.071 107.151 110.293C107.262 110.515 107.317 110.769 107.317 111.056C107.317 111.435 107.242 111.757 107.092 112.022C106.945 112.284 106.744 112.497 106.49 112.662C106.24 112.826 105.95 112.944 105.62 113.016C105.291 113.091 104.943 113.129 104.578 113.129C104.456 113.129 104.306 113.118 104.127 113.097C103.948 113.079 103.765 113.05 103.579 113.011C103.393 112.975 103.216 112.93 103.047 112.876C102.883 112.819 102.75 112.757 102.65 112.688ZM111.034 113.129C110.221 113.129 109.571 112.873 109.084 112.361C108.601 111.845 108.359 111.163 108.359 110.314C108.359 109.391 108.612 108.669 109.117 108.15C109.622 107.631 110.304 107.371 111.163 107.371C111.983 107.371 112.622 107.624 113.081 108.128C113.542 108.633 113.773 109.333 113.773 110.229C113.773 111.106 113.525 111.809 113.027 112.339C112.533 112.866 111.868 113.129 111.034 113.129ZM111.099 108.112C110.533 108.112 110.085 108.306 109.756 108.692C109.426 109.076 109.262 109.605 109.262 110.282C109.262 110.934 109.428 111.448 109.761 111.824C110.094 112.2 110.54 112.388 111.099 112.388C111.668 112.388 112.105 112.203 112.409 111.834C112.717 111.466 112.871 110.941 112.871 110.261C112.871 109.573 112.717 109.043 112.409 108.671C112.105 108.299 111.668 108.112 111.099 108.112ZM117.898 105.631C117.727 105.534 117.531 105.486 117.313 105.486C116.697 105.486 116.389 105.874 116.389 106.651V107.5H117.678V108.252H116.389V113H115.514V108.252H114.574V107.5H115.514V106.608C115.514 106.032 115.68 105.577 116.013 105.244C116.346 104.908 116.762 104.739 117.259 104.739C117.528 104.739 117.741 104.771 117.898 104.836V105.631ZM121.18 112.946C120.972 113.061 120.699 113.118 120.358 113.118C119.395 113.118 118.914 112.581 118.914 111.507V108.252H117.968V107.5H118.914V106.157L119.794 105.873V107.5H121.18V108.252H119.794V111.351C119.794 111.72 119.857 111.983 119.982 112.141C120.108 112.298 120.315 112.377 120.605 112.377C120.827 112.377 121.019 112.316 121.18 112.194V112.946ZM129.285 107.5L127.636 113H126.723L125.59 109.063C125.547 108.913 125.518 108.743 125.504 108.553H125.482C125.472 108.682 125.434 108.848 125.37 109.052L124.14 113H123.259L121.594 107.5H122.518L123.656 111.636C123.692 111.761 123.717 111.926 123.731 112.13H123.774C123.785 111.972 123.817 111.804 123.871 111.625L125.139 107.5H125.944L127.083 111.646C127.119 111.779 127.146 111.944 127.164 112.141H127.207C127.214 112.001 127.244 111.836 127.298 111.646L128.415 107.5H129.285ZM134.243 113H133.362V112.141H133.34C132.957 112.799 132.393 113.129 131.648 113.129C131.101 113.129 130.671 112.984 130.359 112.694C130.051 112.404 129.897 112.019 129.897 111.539C129.897 110.511 130.503 109.913 131.713 109.745L133.362 109.514C133.362 108.58 132.984 108.112 132.229 108.112C131.566 108.112 130.968 108.338 130.435 108.789V107.887C130.975 107.543 131.598 107.371 132.304 107.371C133.596 107.371 134.243 108.055 134.243 109.423V113ZM133.362 110.218L132.035 110.4C131.627 110.458 131.319 110.56 131.111 110.707C130.904 110.85 130.8 111.106 130.8 111.475C130.8 111.743 130.895 111.963 131.084 112.135C131.278 112.304 131.534 112.388 131.853 112.388C132.289 112.388 132.649 112.236 132.932 111.931C133.219 111.623 133.362 111.235 133.362 110.766V110.218ZM138.771 108.392C138.617 108.273 138.395 108.214 138.104 108.214C137.729 108.214 137.413 108.392 137.159 108.746C136.909 109.101 136.783 109.584 136.783 110.196V113H135.902V107.5H136.783V108.633H136.805C136.93 108.247 137.122 107.946 137.379 107.731C137.637 107.513 137.925 107.403 138.244 107.403C138.473 107.403 138.649 107.428 138.771 107.479V108.392ZM144.147 110.47H140.264C140.278 111.083 140.443 111.555 140.758 111.888C141.073 112.221 141.506 112.388 142.058 112.388C142.677 112.388 143.246 112.184 143.766 111.775V112.603C143.282 112.953 142.643 113.129 141.848 113.129C141.071 113.129 140.461 112.88 140.017 112.382C139.573 111.881 139.351 111.177 139.351 110.271C139.351 109.416 139.592 108.719 140.076 108.182C140.563 107.641 141.166 107.371 141.886 107.371C142.605 107.371 143.162 107.604 143.556 108.069C143.95 108.535 144.147 109.181 144.147 110.008V110.47ZM143.245 109.724C143.241 109.215 143.118 108.819 142.874 108.537C142.634 108.254 142.299 108.112 141.87 108.112C141.454 108.112 141.102 108.261 140.812 108.558C140.521 108.855 140.342 109.244 140.274 109.724H143.245ZM150.812 114.751H150.028C148.918 113.483 148.363 111.92 148.363 110.062C148.363 108.196 148.918 106.608 150.028 105.298H150.823C149.699 106.659 149.137 108.243 149.137 110.051C149.137 111.845 149.695 113.412 150.812 114.751ZM152.703 113H151.822V104.857H152.703V113ZM154.938 106.104C154.78 106.104 154.646 106.05 154.535 105.942C154.424 105.835 154.368 105.699 154.368 105.534C154.368 105.369 154.424 105.233 154.535 105.126C154.646 105.015 154.78 104.959 154.938 104.959C155.099 104.959 155.235 105.015 155.346 105.126C155.46 105.233 155.518 105.369 155.518 105.534C155.518 105.692 155.46 105.826 155.346 105.937C155.235 106.048 155.099 106.104 154.938 106.104ZM155.367 113H154.486V107.5H155.367V113ZM156.817 112.801V111.856C157.297 112.21 157.825 112.388 158.402 112.388C159.175 112.388 159.562 112.13 159.562 111.614C159.562 111.467 159.528 111.344 159.46 111.244C159.396 111.14 159.306 111.049 159.191 110.97C159.08 110.891 158.948 110.821 158.794 110.76C158.644 110.696 158.481 110.63 158.305 110.562C158.062 110.465 157.847 110.368 157.661 110.271C157.478 110.171 157.324 110.06 157.199 109.938C157.077 109.813 156.984 109.672 156.919 109.514C156.859 109.357 156.828 109.172 156.828 108.961C156.828 108.703 156.887 108.476 157.005 108.279C157.124 108.078 157.281 107.912 157.478 107.779C157.675 107.643 157.899 107.541 158.149 107.473C158.404 107.405 158.665 107.371 158.934 107.371C159.41 107.371 159.836 107.453 160.212 107.618V108.51C159.807 108.245 159.342 108.112 158.815 108.112C158.651 108.112 158.502 108.132 158.37 108.171C158.237 108.207 158.123 108.259 158.026 108.327C157.933 108.395 157.859 108.478 157.806 108.574C157.756 108.667 157.73 108.771 157.73 108.886C157.73 109.029 157.756 109.149 157.806 109.246C157.859 109.342 157.936 109.428 158.037 109.503C158.137 109.579 158.259 109.647 158.402 109.708C158.545 109.768 158.708 109.835 158.891 109.906C159.134 109.999 159.353 110.096 159.546 110.196C159.739 110.293 159.904 110.404 160.04 110.529C160.176 110.651 160.28 110.792 160.352 110.954C160.427 111.115 160.464 111.306 160.464 111.528C160.464 111.8 160.403 112.037 160.282 112.237C160.164 112.438 160.004 112.604 159.804 112.737C159.603 112.869 159.372 112.968 159.111 113.032C158.849 113.097 158.576 113.129 158.289 113.129C157.723 113.129 157.233 113.02 156.817 112.801ZM164.375 112.946C164.167 113.061 163.893 113.118 163.553 113.118C162.59 113.118 162.108 112.581 162.108 111.507V108.252H161.163V107.5H162.108V106.157L162.989 105.873V107.5H164.375V108.252H162.989V111.351C162.989 111.72 163.051 111.983 163.177 112.141C163.302 112.298 163.51 112.377 163.8 112.377C164.022 112.377 164.213 112.316 164.375 112.194V112.946ZM165.572 114.751H164.788C165.905 113.412 166.464 111.845 166.464 110.051C166.464 108.243 165.902 106.659 164.777 105.298H165.572C166.689 106.608 167.248 108.196 167.248 110.062C167.248 111.92 166.689 113.483 165.572 114.751Z" fill="#EF6950"/>
-    <path d="M22.04 33.168C22.04 35.1341 21.153 36.1172 19.3789 36.1172C17.6797 36.1172 16.8301 35.1715 16.8301 33.2803V28.998H17.6504V33.2266C17.6504 34.6621 18.2559 35.3799 19.4668 35.3799C20.6354 35.3799 21.2197 34.6865 21.2197 33.2998V28.998H22.04V33.168ZM27.9336 29.7402H25.9121V36H25.0918V29.7402H23.0752V28.998H27.9336V29.7402ZM33.373 29.7402H31.3516V36H30.5312V29.7402H28.5146V28.998H33.373V29.7402ZM38.1875 36H34.4766V28.998H38.0312V29.7402H35.2969V32.0693H37.8262V32.8066H35.2969V35.2578H38.1875V36ZM44.5547 36H43.5781L42.4062 34.0371C42.2988 33.8548 42.1947 33.7002 42.0938 33.5732C41.9928 33.443 41.8887 33.3372 41.7812 33.2559C41.6771 33.1745 41.5632 33.1159 41.4395 33.0801C41.319 33.041 41.1823 33.0215 41.0293 33.0215H40.3555V36H39.5352V28.998H41.625C41.931 28.998 42.2126 29.0371 42.4697 29.1152C42.7301 29.1901 42.9548 29.3057 43.1436 29.4619C43.3356 29.6182 43.4854 29.8135 43.5928 30.0479C43.7002 30.279 43.7539 30.5508 43.7539 30.8633C43.7539 31.1074 43.7165 31.332 43.6416 31.5371C43.57 31.7389 43.4658 31.9196 43.3291 32.0791C43.1956 32.2386 43.0329 32.3753 42.8408 32.4893C42.652 32.5999 42.4388 32.6862 42.2012 32.748V32.7676C42.3184 32.8197 42.4193 32.8799 42.5039 32.9482C42.5918 33.0133 42.6748 33.0915 42.7529 33.1826C42.8311 33.2738 42.9076 33.3779 42.9824 33.4951C43.0605 33.609 43.1468 33.7425 43.2412 33.8955L44.5547 36ZM40.3555 29.7402V32.2793H41.4688C41.6738 32.2793 41.8626 32.2484 42.0352 32.1865C42.2109 32.1247 42.3623 32.0368 42.4893 31.9229C42.6162 31.8057 42.7155 31.6641 42.7871 31.498C42.8587 31.3288 42.8945 31.14 42.8945 30.9316C42.8945 30.5573 42.7725 30.266 42.5283 30.0576C42.2874 29.846 41.9375 29.7402 41.4785 29.7402H40.3555ZM50.9414 36H50.0332L49.291 34.0371H46.3223L45.624 36H44.7109L47.3965 28.998H48.2461L50.9414 36ZM49.0225 33.2998L47.9238 30.3164C47.888 30.2188 47.8522 30.0625 47.8164 29.8477H47.7969C47.7643 30.0462 47.7269 30.2025 47.6846 30.3164L46.5957 33.2998H49.0225ZM57.6211 36H56.6152L53.0117 30.4189C52.9206 30.279 52.8457 30.1325 52.7871 29.9795H52.7578C52.7839 30.1292 52.7969 30.4499 52.7969 30.9414V36H51.9766V28.998H53.041L56.5469 34.4912C56.6934 34.7191 56.7878 34.8753 56.8301 34.96H56.8496C56.8171 34.7581 56.8008 34.4147 56.8008 33.9297V28.998H57.6211V36ZM64.2227 35.707C63.7051 35.9805 63.0605 36.1172 62.2891 36.1172C61.293 36.1172 60.4954 35.7965 59.8965 35.1553C59.2975 34.514 58.998 33.6725 58.998 32.6309C58.998 31.5111 59.335 30.6061 60.0088 29.916C60.6826 29.2259 61.5371 28.8809 62.5723 28.8809C63.2363 28.8809 63.7865 28.9769 64.2227 29.1689V30.043C63.7214 29.763 63.168 29.623 62.5625 29.623C61.7585 29.623 61.1058 29.8916 60.6045 30.4287C60.1064 30.9658 59.8574 31.6836 59.8574 32.582C59.8574 33.4349 60.0902 34.1152 60.5557 34.623C61.0244 35.1276 61.638 35.3799 62.3965 35.3799C63.0996 35.3799 63.7083 35.2236 64.2227 34.9111V35.707ZM69.3594 36H65.6484V28.998H69.2031V29.7402H66.4688V32.0693H68.998V32.8066H66.4688V35.2578H69.3594V36ZM78.8711 36H77.9629L77.2207 34.0371H74.252L73.5537 36H72.6406L75.3262 28.998H76.1758L78.8711 36ZM76.9521 33.2998L75.8535 30.3164C75.8177 30.2188 75.7819 30.0625 75.7461 29.8477H75.7266C75.694 30.0462 75.6566 30.2025 75.6143 30.3164L74.5254 33.2998H76.9521ZM85.5508 36H84.5449L80.9414 30.4189C80.8503 30.279 80.7754 30.1325 80.7168 29.9795H80.6875C80.7135 30.1292 80.7266 30.4499 80.7266 30.9414V36H79.9062V28.998H80.9707L84.4766 34.4912C84.623 34.7191 84.7174 34.8753 84.7598 34.96H84.7793C84.7467 34.7581 84.7305 34.4147 84.7305 33.9297V28.998H85.5508V36ZM87.3867 36V28.998H89.3203C91.7878 28.998 93.0215 30.1357 93.0215 32.4111C93.0215 33.4919 92.6781 34.361 91.9912 35.0186C91.3076 35.6729 90.3913 36 89.2422 36H87.3867ZM88.207 29.7402V35.2578H89.252C90.1699 35.2578 90.8844 35.012 91.3955 34.5205C91.9066 34.029 92.1621 33.3324 92.1621 32.4307C92.1621 30.637 91.2083 29.7402 89.3008 29.7402H88.207ZM97.1426 36V28.998H99.0762C101.544 28.998 102.777 30.1357 102.777 32.4111C102.777 33.4919 102.434 34.361 101.747 35.0186C101.063 35.6729 100.147 36 98.998 36H97.1426ZM97.9629 29.7402V35.2578H99.0078C99.9258 35.2578 100.64 35.012 101.151 34.5205C101.662 34.029 101.918 33.3324 101.918 32.4307C101.918 30.637 100.964 29.7402 99.0566 29.7402H97.9629ZM107.865 36H104.154V28.998H107.709V29.7402H104.975V32.0693H107.504V32.8066H104.975V35.2578H107.865V36ZM113.354 29.7402H111.332V36H110.512V29.7402H108.495V28.998H113.354V29.7402ZM118.168 36H114.457V28.998H118.012V29.7402H115.277V32.0693H117.807V32.8066H115.277V35.2578H118.168V36ZM124.281 35.707C123.764 35.9805 123.119 36.1172 122.348 36.1172C121.352 36.1172 120.554 35.7965 119.955 35.1553C119.356 34.514 119.057 33.6725 119.057 32.6309C119.057 31.5111 119.394 30.6061 120.067 29.916C120.741 29.2259 121.596 28.8809 122.631 28.8809C123.295 28.8809 123.845 28.9769 124.281 29.1689V30.043C123.78 29.763 123.227 29.623 122.621 29.623C121.817 29.623 121.164 29.8916 120.663 30.4287C120.165 30.9658 119.916 31.6836 119.916 32.582C119.916 33.4349 120.149 34.1152 120.614 34.623C121.083 35.1276 121.697 35.3799 122.455 35.3799C123.158 35.3799 123.767 35.2236 124.281 34.9111V35.707ZM129.848 29.7402H127.826V36H127.006V29.7402H124.989V28.998H129.848V29.7402ZM134.662 36H130.951V28.998H134.506V29.7402H131.771V32.0693H134.301V32.8066H131.771V35.2578H134.662V36ZM136.01 36V28.998H137.943C140.411 28.998 141.645 30.1357 141.645 32.4111C141.645 33.4919 141.301 34.361 140.614 35.0186C139.931 35.6729 139.014 36 137.865 36H136.01ZM136.83 29.7402V35.2578H137.875C138.793 35.2578 139.507 35.012 140.019 34.5205C140.53 34.029 140.785 33.3324 140.785 32.4307C140.785 30.637 139.831 29.7402 137.924 29.7402H136.83ZM150.531 35.707C150.014 35.9805 149.369 36.1172 148.598 36.1172C147.602 36.1172 146.804 35.7965 146.205 35.1553C145.606 34.514 145.307 33.6725 145.307 32.6309C145.307 31.5111 145.644 30.6061 146.317 29.916C146.991 29.2259 147.846 28.8809 148.881 28.8809C149.545 28.8809 150.095 28.9769 150.531 29.1689V30.043C150.03 29.763 149.477 29.623 148.871 29.623C148.067 29.623 147.414 29.8916 146.913 30.4287C146.415 30.9658 146.166 31.6836 146.166 32.582C146.166 33.4349 146.399 34.1152 146.864 34.623C147.333 35.1276 147.947 35.3799 148.705 35.3799C149.408 35.3799 150.017 35.2236 150.531 34.9111V35.707ZM154.506 36.1172C153.513 36.1172 152.717 35.79 152.118 35.1357C151.522 34.4814 151.225 33.6302 151.225 32.582C151.225 31.4557 151.529 30.5573 152.138 29.8867C152.746 29.2161 153.575 28.8809 154.623 28.8809C155.59 28.8809 156.368 29.2064 156.957 29.8574C157.549 30.5085 157.846 31.3597 157.846 32.4111C157.846 33.5537 157.543 34.457 156.938 35.1211C156.332 35.7852 155.521 36.1172 154.506 36.1172ZM154.564 29.623C153.829 29.623 153.231 29.8883 152.772 30.4189C152.313 30.9495 152.084 31.6462 152.084 32.5088C152.084 33.3714 152.307 34.0664 152.753 34.5938C153.202 35.1178 153.786 35.3799 154.506 35.3799C155.274 35.3799 155.88 35.1292 156.322 34.6279C156.765 34.1266 156.986 33.4251 156.986 32.5234C156.986 31.599 156.771 30.8844 156.342 30.3799C155.912 29.8753 155.32 29.623 154.564 29.623ZM166.361 36H165.546V31.3027C165.546 30.9316 165.569 30.4775 165.614 29.9404H165.595C165.517 30.2562 165.447 30.4824 165.385 30.6191L162.992 36H162.592L160.204 30.6582C160.136 30.502 160.066 30.2627 159.994 29.9404H159.975C160.001 30.2204 160.014 30.6777 160.014 31.3125V36H159.223V28.998H160.307L162.455 33.8809C162.621 34.2552 162.729 34.5352 162.777 34.7207H162.807C162.947 34.3366 163.059 34.0501 163.144 33.8613L165.336 28.998H166.361V36ZM169.027 33.3535V36H168.207V28.998H170.131C170.88 28.998 171.459 29.1803 171.869 29.5449C172.283 29.9095 172.489 30.4238 172.489 31.0879C172.489 31.752 172.26 32.2956 171.801 32.7188C171.345 33.1419 170.728 33.3535 169.95 33.3535H169.027ZM169.027 29.7402V32.6113H169.887C170.453 32.6113 170.884 32.4827 171.181 32.2256C171.48 31.9652 171.63 31.599 171.63 31.127C171.63 30.2025 171.083 29.7402 169.989 29.7402H169.027ZM176.635 36.1172C175.642 36.1172 174.846 35.79 174.247 35.1357C173.651 34.4814 173.354 33.6302 173.354 32.582C173.354 31.4557 173.658 30.5573 174.267 29.8867C174.875 29.2161 175.704 28.8809 176.752 28.8809C177.719 28.8809 178.497 29.2064 179.086 29.8574C179.678 30.5085 179.975 31.3597 179.975 32.4111C179.975 33.5537 179.672 34.457 179.066 35.1211C178.461 35.7852 177.65 36.1172 176.635 36.1172ZM176.693 29.623C175.958 29.623 175.36 29.8883 174.901 30.4189C174.442 30.9495 174.213 31.6462 174.213 32.5088C174.213 33.3714 174.436 34.0664 174.882 34.5938C175.331 35.1178 175.915 35.3799 176.635 35.3799C177.403 35.3799 178.008 35.1292 178.451 34.6279C178.894 34.1266 179.115 33.4251 179.115 32.5234C179.115 31.599 178.9 30.8844 178.471 30.3799C178.041 29.8753 177.449 29.623 176.693 29.623ZM186.996 36H185.99L182.387 30.4189C182.296 30.279 182.221 30.1325 182.162 29.9795H182.133C182.159 30.1292 182.172 30.4499 182.172 30.9414V36H181.352V28.998H182.416L185.922 34.4912C186.068 34.7191 186.163 34.8753 186.205 34.96H186.225C186.192 34.7581 186.176 34.4147 186.176 33.9297V28.998H186.996V36ZM192.543 36H188.832V28.998H192.387V29.7402H189.652V32.0693H192.182V32.8066H189.652V35.2578H192.543V36ZM199.535 36H198.529L194.926 30.4189C194.835 30.279 194.76 30.1325 194.701 29.9795H194.672C194.698 30.1292 194.711 30.4499 194.711 30.9414V36H193.891V28.998H194.955L198.461 34.4912C198.607 34.7191 198.702 34.8753 198.744 34.96H198.764C198.731 34.7581 198.715 34.4147 198.715 33.9297V28.998H199.535V36ZM205.512 29.7402H203.49V36H202.67V29.7402H200.653V28.998H205.512V29.7402ZM206.093 35.7168V34.75C206.203 34.8477 206.335 34.9355 206.488 35.0137C206.645 35.0918 206.807 35.1585 206.977 35.2139C207.149 35.266 207.322 35.3066 207.494 35.3359C207.667 35.3652 207.826 35.3799 207.973 35.3799C208.477 35.3799 208.853 35.2871 209.101 35.1016C209.351 34.9128 209.477 34.6426 209.477 34.291C209.477 34.1022 209.434 33.9378 209.35 33.7979C209.268 33.6579 209.154 33.5309 209.008 33.417C208.861 33.2998 208.687 33.1891 208.485 33.085C208.287 32.9775 208.072 32.8652 207.841 32.748C207.597 32.6243 207.369 32.499 207.157 32.3721C206.946 32.2451 206.762 32.1051 206.605 31.9521C206.449 31.7992 206.326 31.6266 206.234 31.4346C206.146 31.2393 206.103 31.0114 206.103 30.751C206.103 30.432 206.173 30.1553 206.312 29.9209C206.452 29.6833 206.636 29.488 206.864 29.335C207.092 29.182 207.351 29.068 207.641 28.9932C207.934 28.9183 208.231 28.8809 208.534 28.8809C209.224 28.8809 209.727 28.9639 210.043 29.1299V30.0527C209.63 29.7663 209.099 29.623 208.451 29.623C208.272 29.623 208.093 29.6426 207.914 29.6816C207.735 29.7174 207.576 29.7777 207.436 29.8623C207.296 29.9469 207.182 30.056 207.094 30.1895C207.006 30.3229 206.962 30.4857 206.962 30.6777C206.962 30.8568 206.994 31.0114 207.06 31.1416C207.128 31.2718 207.227 31.3906 207.357 31.498C207.488 31.6055 207.646 31.7096 207.831 31.8105C208.02 31.9115 208.236 32.0221 208.48 32.1426C208.731 32.2663 208.969 32.3965 209.193 32.5332C209.418 32.6699 209.615 32.8213 209.784 32.9873C209.953 33.1533 210.087 33.3372 210.185 33.5391C210.285 33.7409 210.336 33.972 210.336 34.2324C210.336 34.5775 210.268 34.8704 210.131 35.1113C209.997 35.349 209.815 35.5426 209.584 35.6924C209.356 35.8421 209.092 35.9495 208.793 36.0146C208.493 36.083 208.178 36.1172 207.846 36.1172C207.735 36.1172 207.598 36.1074 207.436 36.0879C207.273 36.0716 207.107 36.0456 206.938 36.0098C206.768 35.9772 206.607 35.9365 206.454 35.8877C206.304 35.8356 206.184 35.7786 206.093 35.7168Z" fill="#323130"/>
-</svg>
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "重複領域の例のSVGファイルの削除"
}
```

### Explanation
この変更により、`union-overlap-example-1.svg`というSVG画像ファイルが削除されました。このファイルは、カスタムテキスト分析における重複領域の視覚的な説明や具体例を提供していたと見られます。

このファイルが削除されることで、ユーザーは重複領域の理解に必要な視覚的な資料を失うことになります。特に、視覚的な情報に依存して概念を学ぼうとしているユーザーにとっては、情報のギャップが生じる可能性が高いです。これは、アプリケーションやサービスの利用において知識が不足し、効果的な活用が難しくなることを意味します。

この変更を受けて、代替の資料や説明、例を迅速に提供することが重要です。また、関連する他の資料へのリンクを示すことで、ユーザーが依然として必要な情報を得られるようケアすることが求められます。影響を受けるユーザーが少しでもスムーズに学習を進められるよう、サポートを行うことが推奨されます。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/union-overlap-example-2-part-2.svg{#item-6faae8}

<details>
<summary>Diff</summary>
````diff
@@ -1,10 +0,0 @@
-<svg width="289" height="114" viewBox="0 0 289 114" fill="none"
-    xmlns="http://www.w3.org/2000/svg">
-    <path d="M296 0H0V114H296V0Z" fill="#F3F2F1"/>
-    <path d="M103.434 66.2949V70H102.285V60.1973H104.979C106.027 60.1973 106.838 60.4525 107.412 60.9629C107.991 61.4733 108.28 62.1934 108.28 63.123C108.28 64.0527 107.959 64.8138 107.316 65.4062C106.678 65.9987 105.815 66.2949 104.726 66.2949H103.434ZM103.434 61.2363V65.2559H104.637C105.43 65.2559 106.034 65.0758 106.448 64.7158C106.868 64.3512 107.077 63.8385 107.077 63.1777C107.077 61.8835 106.312 61.2363 104.78 61.2363H103.434ZM113.633 64.1348C113.437 63.9844 113.154 63.9092 112.785 63.9092C112.307 63.9092 111.906 64.1348 111.582 64.5859C111.263 65.0371 111.104 65.6523 111.104 66.4316V70H109.982V63H111.104V64.4424H111.131C111.29 63.9502 111.534 63.5674 111.862 63.2939C112.19 63.016 112.557 62.877 112.963 62.877C113.255 62.877 113.478 62.9089 113.633 62.9727V64.1348ZM117.775 70.1641C116.741 70.1641 115.914 69.8382 115.294 69.1865C114.679 68.5303 114.371 67.6621 114.371 66.582C114.371 65.4062 114.692 64.488 115.335 63.8271C115.978 63.1663 116.846 62.8359 117.939 62.8359C118.983 62.8359 119.797 63.1572 120.38 63.7998C120.968 64.4424 121.262 65.3333 121.262 66.4727C121.262 67.5892 120.945 68.4847 120.312 69.1592C119.683 69.8291 118.837 70.1641 117.775 70.1641ZM117.857 63.7793C117.137 63.7793 116.568 64.0254 116.148 64.5176C115.729 65.0052 115.52 65.6797 115.52 66.541C115.52 67.3704 115.731 68.0244 116.155 68.5029C116.579 68.9814 117.146 69.2207 117.857 69.2207C118.582 69.2207 119.138 68.986 119.525 68.5166C119.917 68.0472 120.113 67.3796 120.113 66.5137C120.113 65.6387 119.917 64.9642 119.525 64.4902C119.138 64.0163 118.582 63.7793 117.857 63.7793ZM122.629 69.7471V68.5439C123.24 68.9951 123.912 69.2207 124.646 69.2207C125.63 69.2207 126.122 68.8926 126.122 68.2363C126.122 68.0495 126.079 67.8923 125.992 67.7646C125.91 67.6325 125.796 67.5163 125.65 67.416C125.509 67.3158 125.34 67.2269 125.145 67.1494C124.953 67.0674 124.746 66.9831 124.522 66.8965C124.213 66.7734 123.939 66.6504 123.702 66.5273C123.47 66.3997 123.274 66.2585 123.114 66.1035C122.959 65.944 122.841 65.764 122.759 65.5635C122.681 65.363 122.643 65.1283 122.643 64.8594C122.643 64.5312 122.718 64.2419 122.868 63.9912C123.019 63.736 123.219 63.5241 123.47 63.3555C123.72 63.1823 124.005 63.0524 124.324 62.9658C124.648 62.8792 124.98 62.8359 125.322 62.8359C125.928 62.8359 126.471 62.9408 126.949 63.1504V64.2852C126.434 63.9479 125.842 63.7793 125.172 63.7793C124.962 63.7793 124.773 63.8044 124.604 63.8545C124.436 63.9001 124.29 63.9661 124.167 64.0527C124.049 64.1393 123.955 64.2441 123.887 64.3672C123.823 64.4857 123.791 64.6178 123.791 64.7637C123.791 64.946 123.823 65.0986 123.887 65.2217C123.955 65.3447 124.053 65.4541 124.181 65.5498C124.308 65.6455 124.463 65.7321 124.646 65.8096C124.828 65.887 125.035 65.9714 125.268 66.0625C125.577 66.181 125.855 66.304 126.102 66.4316C126.348 66.5547 126.557 66.696 126.73 66.8555C126.904 67.0104 127.036 67.1904 127.127 67.3955C127.223 67.6006 127.271 67.8444 127.271 68.127C127.271 68.4733 127.193 68.7741 127.038 69.0293C126.888 69.2845 126.685 69.4964 126.43 69.665C126.174 69.8337 125.881 69.959 125.548 70.041C125.215 70.123 124.867 70.1641 124.502 70.1641C123.782 70.1641 123.158 70.0251 122.629 69.7471ZM134.626 66.7803H129.684C129.702 67.5596 129.911 68.1611 130.312 68.585C130.714 69.0088 131.265 69.2207 131.967 69.2207C132.755 69.2207 133.48 68.9609 134.141 68.4414V69.4941C133.525 69.9408 132.712 70.1641 131.7 70.1641C130.711 70.1641 129.934 69.8473 129.369 69.2139C128.804 68.5758 128.521 67.6803 128.521 66.5273C128.521 65.4382 128.829 64.5518 129.444 63.8682C130.064 63.18 130.832 62.8359 131.748 62.8359C132.664 62.8359 133.373 63.1322 133.874 63.7246C134.375 64.3171 134.626 65.1396 134.626 66.1924V66.7803ZM133.478 65.8301C133.473 65.1829 133.316 64.6794 133.006 64.3193C132.701 63.9593 132.274 63.7793 131.728 63.7793C131.199 63.7793 130.75 63.9684 130.381 64.3467C130.012 64.7249 129.784 65.2194 129.697 65.8301H133.478ZM145.146 63L143.048 70H141.886L140.443 64.9893C140.389 64.7979 140.352 64.5814 140.334 64.3398H140.307C140.293 64.5039 140.245 64.7158 140.163 64.9756L138.598 70H137.477L135.357 63H136.533L137.982 68.2637C138.028 68.4232 138.06 68.6328 138.078 68.8926H138.133C138.146 68.6921 138.188 68.4779 138.256 68.25L139.869 63H140.895L142.344 68.2773C142.389 68.446 142.424 68.6556 142.446 68.9062H142.501C142.51 68.7285 142.549 68.5189 142.617 68.2773L144.039 63H145.146ZM151.456 70H150.335V68.9062H150.308C149.82 69.7448 149.102 70.1641 148.154 70.1641C147.457 70.1641 146.91 69.9795 146.514 69.6104C146.122 69.2412 145.926 68.7513 145.926 68.1406C145.926 66.8327 146.696 66.0716 148.236 65.8574L150.335 65.5635C150.335 64.374 149.854 63.7793 148.893 63.7793C148.049 63.7793 147.288 64.0664 146.609 64.6406V63.4922C147.298 63.0547 148.09 62.8359 148.988 62.8359C150.633 62.8359 151.456 63.7064 151.456 65.4473V70ZM150.335 66.459L148.646 66.6914C148.127 66.7643 147.735 66.8942 147.471 67.0811C147.206 67.2633 147.074 67.5892 147.074 68.0586C147.074 68.4004 147.195 68.6807 147.437 68.8994C147.683 69.1136 148.008 69.2207 148.414 69.2207C148.97 69.2207 149.428 69.027 149.788 68.6396C150.153 68.2477 150.335 67.7533 150.335 67.1562V66.459ZM157.219 64.1348C157.023 63.9844 156.74 63.9092 156.371 63.9092C155.893 63.9092 155.492 64.1348 155.168 64.5859C154.849 65.0371 154.689 65.6523 154.689 66.4316V70H153.568V63H154.689V64.4424H154.717C154.876 63.9502 155.12 63.5674 155.448 63.2939C155.776 63.016 156.143 62.877 156.549 62.877C156.84 62.877 157.064 62.9089 157.219 62.9727V64.1348ZM164.062 66.7803H159.119C159.137 67.5596 159.347 68.1611 159.748 68.585C160.149 69.0088 160.701 69.2207 161.402 69.2207C162.191 69.2207 162.915 68.9609 163.576 68.4414V69.4941C162.961 69.9408 162.147 70.1641 161.136 70.1641C160.147 70.1641 159.37 69.8473 158.805 69.2139C158.24 68.5758 157.957 67.6803 157.957 66.5273C157.957 65.4382 158.265 64.5518 158.88 63.8682C159.5 63.18 160.268 62.8359 161.184 62.8359C162.1 62.8359 162.808 63.1322 163.31 63.7246C163.811 64.3171 164.062 65.1396 164.062 66.1924V66.7803ZM162.913 65.8301C162.909 65.1829 162.751 64.6794 162.441 64.3193C162.136 63.9593 161.71 63.7793 161.163 63.7793C160.634 63.7793 160.186 63.9684 159.816 64.3467C159.447 64.7249 159.219 65.2194 159.133 65.8301H162.913ZM173.707 70.1641C172.317 70.1641 171.203 69.7061 170.364 68.79C169.53 67.874 169.113 66.6823 169.113 65.2148C169.113 63.638 169.539 62.3802 170.392 61.4414C171.244 60.5026 172.404 60.0332 173.871 60.0332C175.225 60.0332 176.314 60.4889 177.139 61.4004C177.968 62.3118 178.383 63.5036 178.383 64.9756C178.383 66.5752 177.959 67.8398 177.111 68.7695C176.264 69.6992 175.129 70.1641 173.707 70.1641ZM173.789 61.0723C172.759 61.0723 171.923 61.4437 171.28 62.1865C170.638 62.9294 170.316 63.9046 170.316 65.1123C170.316 66.32 170.629 67.293 171.253 68.0312C171.882 68.765 172.7 69.1318 173.707 69.1318C174.783 69.1318 175.63 68.7809 176.25 68.0791C176.87 67.3773 177.18 66.3952 177.18 65.1328C177.18 63.8385 176.879 62.8382 176.277 62.1318C175.676 61.4255 174.846 61.0723 173.789 61.0723ZM179.853 69.6035V68.25C180.007 68.3867 180.192 68.5098 180.406 68.6191C180.625 68.7285 180.853 68.8219 181.09 68.8994C181.331 68.9723 181.573 69.0293 181.814 69.0703C182.056 69.1113 182.279 69.1318 182.484 69.1318C183.191 69.1318 183.717 69.002 184.063 68.7422C184.414 68.4779 184.59 68.0996 184.59 67.6074C184.59 67.3431 184.531 67.113 184.412 66.917C184.298 66.721 184.139 66.5433 183.934 66.3838C183.729 66.2197 183.485 66.0648 183.202 65.9189C182.924 65.7686 182.623 65.6113 182.3 65.4473C181.958 65.2741 181.639 65.0986 181.343 64.9209C181.047 64.7432 180.789 64.5472 180.57 64.333C180.352 64.1188 180.178 63.8773 180.051 63.6084C179.928 63.335 179.866 63.016 179.866 62.6514C179.866 62.2048 179.964 61.8174 180.16 61.4893C180.356 61.1566 180.614 60.8831 180.933 60.6689C181.252 60.4548 181.614 60.2952 182.02 60.1904C182.43 60.0856 182.847 60.0332 183.271 60.0332C184.237 60.0332 184.941 60.1494 185.383 60.3818V61.6738C184.804 61.2728 184.061 61.0723 183.154 61.0723C182.904 61.0723 182.653 61.0996 182.402 61.1543C182.152 61.2044 181.928 61.2887 181.732 61.4072C181.536 61.5257 181.377 61.6784 181.254 61.8652C181.131 62.0521 181.069 62.2799 181.069 62.5488C181.069 62.7995 181.115 63.016 181.206 63.1982C181.302 63.3805 181.441 63.5469 181.623 63.6973C181.805 63.8477 182.026 63.9935 182.286 64.1348C182.55 64.276 182.854 64.431 183.195 64.5996C183.546 64.7728 183.879 64.9551 184.193 65.1465C184.508 65.3379 184.784 65.5498 185.021 65.7822C185.257 66.0146 185.444 66.2721 185.581 66.5547C185.722 66.8372 185.793 67.1608 185.793 67.5254C185.793 68.0085 185.697 68.4186 185.506 68.7559C185.319 69.0885 185.064 69.3597 184.74 69.5693C184.421 69.779 184.052 69.9294 183.633 70.0205C183.214 70.1162 182.771 70.1641 182.307 70.1641C182.152 70.1641 181.96 70.1504 181.732 70.123C181.505 70.1003 181.272 70.0638 181.035 70.0137C180.798 69.9681 180.573 69.9111 180.358 69.8428C180.149 69.7699 179.98 69.6901 179.853 69.6035ZM197.168 64.5107C197.168 65.4085 197.079 66.2083 196.901 66.9102C196.724 67.6074 196.464 68.1999 196.122 68.6875C195.78 69.1706 195.363 69.5397 194.871 69.7949C194.379 70.0456 193.818 70.1709 193.189 70.1709C192.542 70.1709 191.973 70.057 191.48 69.8291V68.7559C192.023 69.0612 192.602 69.2139 193.217 69.2139C193.659 69.2139 194.053 69.1227 194.399 68.9404C194.75 68.7581 195.047 68.4938 195.288 68.1475C195.53 67.7965 195.714 67.3659 195.842 66.8555C195.969 66.3451 196.033 65.7594 196.033 65.0986H196.006C195.587 65.9417 194.857 66.3633 193.818 66.3633C193.399 66.3633 193.014 66.2904 192.663 66.1445C192.312 65.9941 192.009 65.7845 191.754 65.5156C191.499 65.2422 191.3 64.9186 191.159 64.5449C191.018 64.1712 190.947 63.7588 190.947 63.3076C190.947 62.8245 191.025 62.3825 191.18 61.9814C191.339 61.5804 191.558 61.2363 191.836 60.9492C192.118 60.6576 192.451 60.432 192.834 60.2725C193.221 60.113 193.643 60.0332 194.099 60.0332C194.591 60.0332 195.026 60.1335 195.404 60.334C195.787 60.5299 196.108 60.8193 196.368 61.2021C196.628 61.5804 196.826 62.0475 196.963 62.6035C197.1 63.1595 197.168 63.7952 197.168 64.5107ZM195.958 63.5059C195.958 63.1276 195.908 62.7835 195.808 62.4736C195.712 62.1637 195.577 61.8994 195.404 61.6807C195.231 61.4574 195.024 61.2865 194.782 61.168C194.545 61.0449 194.285 60.9834 194.003 60.9834C193.734 60.9834 193.483 61.0381 193.251 61.1475C193.019 61.2523 192.816 61.4027 192.643 61.5986C192.474 61.79 192.34 62.0202 192.239 62.2891C192.144 62.5534 192.096 62.8428 192.096 63.1572C192.096 63.5036 192.141 63.8135 192.232 64.0869C192.328 64.3604 192.463 64.5928 192.636 64.7842C192.809 64.971 193.016 65.1146 193.258 65.2148C193.504 65.3151 193.775 65.3652 194.071 65.3652C194.331 65.3652 194.575 65.3174 194.803 65.2217C195.035 65.1214 195.236 64.9893 195.404 64.8252C195.577 64.6566 195.712 64.4606 195.808 64.2373C195.908 64.0094 195.958 63.7656 195.958 63.5059Z" fill="black"/>
-    <rect x="102" y="78" width="3" height="3" fill="#4B003F"/>
-    <path d="M197 78H200V81H197V78Z" fill="#4B003F"/>
-    <rect x="103" y="79" width="96" height="1" fill="#4B003F"/>
-    <path d="M102.65 92.6885V91.625C102.772 91.7324 102.917 91.8291 103.085 91.915C103.257 92.001 103.436 92.0744 103.622 92.1353C103.812 92.1925 104.002 92.2373 104.191 92.2695C104.381 92.3018 104.557 92.3179 104.718 92.3179C105.273 92.3179 105.686 92.2158 105.958 92.0117C106.234 91.804 106.372 91.5068 106.372 91.1201C106.372 90.9124 106.326 90.7316 106.232 90.5776C106.143 90.4237 106.018 90.284 105.856 90.1587C105.695 90.0298 105.504 89.908 105.282 89.7935C105.063 89.6753 104.827 89.5518 104.573 89.4229C104.304 89.2868 104.054 89.1489 103.821 89.0093C103.588 88.8696 103.386 88.7157 103.214 88.5474C103.042 88.3791 102.906 88.1893 102.806 87.978C102.709 87.7632 102.661 87.5125 102.661 87.2261C102.661 86.8752 102.738 86.5708 102.892 86.313C103.046 86.0516 103.248 85.8368 103.499 85.6685C103.749 85.5002 104.034 85.3748 104.353 85.2925C104.675 85.2101 105.002 85.1689 105.335 85.1689C106.095 85.1689 106.648 85.2603 106.995 85.4429V86.458C106.54 86.1429 105.957 85.9854 105.244 85.9854C105.047 85.9854 104.85 86.0068 104.653 86.0498C104.456 86.0892 104.281 86.1554 104.127 86.2485C103.973 86.3416 103.848 86.4616 103.751 86.6084C103.654 86.7552 103.606 86.9342 103.606 87.1455C103.606 87.3424 103.642 87.5125 103.713 87.6558C103.789 87.799 103.898 87.9297 104.041 88.0479C104.184 88.166 104.358 88.2806 104.562 88.3916C104.77 88.5026 105.008 88.6243 105.276 88.7568C105.552 88.8929 105.813 89.0361 106.061 89.1865C106.308 89.3369 106.524 89.5034 106.71 89.686C106.897 89.8687 107.043 90.071 107.151 90.293C107.262 90.515 107.317 90.7692 107.317 91.0557C107.317 91.4352 107.242 91.7575 107.092 92.0225C106.945 92.2839 106.744 92.4969 106.49 92.6616C106.24 92.8263 105.95 92.9445 105.62 93.0161C105.291 93.0913 104.943 93.1289 104.578 93.1289C104.456 93.1289 104.306 93.1182 104.127 93.0967C103.948 93.0788 103.765 93.0501 103.579 93.0107C103.393 92.9749 103.216 92.9302 103.047 92.8765C102.883 92.8192 102.75 92.7565 102.65 92.6885ZM111.034 93.1289C110.221 93.1289 109.571 92.8729 109.084 92.3608C108.601 91.8452 108.359 91.1631 108.359 90.3145C108.359 89.3906 108.612 88.6691 109.117 88.1499C109.622 87.6307 110.304 87.3711 111.163 87.3711C111.983 87.3711 112.622 87.6235 113.081 88.1284C113.542 88.6333 113.773 89.3333 113.773 90.2285C113.773 91.1058 113.525 91.8094 113.027 92.3394C112.533 92.8657 111.868 93.1289 111.034 93.1289ZM111.099 88.1123C110.533 88.1123 110.085 88.3057 109.756 88.6924C109.426 89.0755 109.262 89.6055 109.262 90.2822C109.262 90.9339 109.428 91.4478 109.761 91.8237C110.094 92.1997 110.54 92.3877 111.099 92.3877C111.668 92.3877 112.105 92.2033 112.409 91.8345C112.717 91.4657 112.871 90.9411 112.871 90.2607C112.871 89.5732 112.717 89.0433 112.409 88.6709C112.105 88.2985 111.668 88.1123 111.099 88.1123ZM117.898 85.6309C117.727 85.5342 117.531 85.4858 117.313 85.4858C116.697 85.4858 116.389 85.8743 116.389 86.6514V87.5H117.678V88.252H116.389V93H115.514V88.252H114.574V87.5H115.514V86.6084C115.514 86.0319 115.68 85.5771 116.013 85.2441C116.346 84.9076 116.762 84.7393 117.259 84.7393C117.528 84.7393 117.741 84.7715 117.898 84.8359V85.6309ZM121.18 92.9463C120.972 93.0609 120.699 93.1182 120.358 93.1182C119.395 93.1182 118.914 92.5811 118.914 91.5068V88.252H117.968V87.5H118.914V86.1572L119.794 85.8726V87.5H121.18V88.252H119.794V91.3511C119.794 91.7199 119.857 91.9831 119.982 92.1406C120.108 92.2982 120.315 92.377 120.605 92.377C120.827 92.377 121.019 92.3161 121.18 92.1943V92.9463ZM129.285 87.5L127.636 93H126.723L125.59 89.063C125.547 88.9126 125.518 88.7425 125.504 88.5527H125.482C125.472 88.6816 125.434 88.8481 125.37 89.0522L124.14 93H123.259L121.594 87.5H122.518L123.656 91.6357C123.692 91.7611 123.717 91.9258 123.731 92.1299H123.774C123.785 91.9723 123.817 91.804 123.871 91.625L125.139 87.5H125.944L127.083 91.6465C127.119 91.779 127.146 91.9437 127.164 92.1406H127.207C127.214 92.001 127.244 91.8363 127.298 91.6465L128.415 87.5H129.285ZM134.243 93H133.362V92.1406H133.34C132.957 92.7995 132.393 93.1289 131.648 93.1289C131.101 93.1289 130.671 92.9839 130.359 92.6938C130.051 92.4038 129.897 92.0189 129.897 91.5391C129.897 90.5114 130.503 89.9134 131.713 89.7451L133.362 89.5142C133.362 88.5796 132.984 88.1123 132.229 88.1123C131.566 88.1123 130.968 88.3379 130.435 88.7891V87.8867C130.975 87.543 131.598 87.3711 132.304 87.3711C133.596 87.3711 134.243 88.055 134.243 89.4229V93ZM133.362 90.2178L132.035 90.4004C131.627 90.4577 131.319 90.5597 131.111 90.7065C130.904 90.8498 130.8 91.1058 130.8 91.4746C130.8 91.7432 130.895 91.9634 131.084 92.1353C131.278 92.3035 131.534 92.3877 131.853 92.3877C132.289 92.3877 132.649 92.2355 132.932 91.9312C133.219 91.6232 133.362 91.2347 133.362 90.7656V90.2178ZM138.771 88.3916C138.617 88.2734 138.395 88.2144 138.104 88.2144C137.729 88.2144 137.413 88.3916 137.159 88.7461C136.909 89.1006 136.783 89.584 136.783 90.1963V93H135.902V87.5H136.783V88.6333H136.805C136.93 88.2466 137.122 87.9458 137.379 87.731C137.637 87.5125 137.925 87.4033 138.244 87.4033C138.473 87.4033 138.649 87.4284 138.771 87.4785V88.3916ZM144.147 90.4702H140.264C140.278 91.0825 140.443 91.5552 140.758 91.8882C141.073 92.2212 141.506 92.3877 142.058 92.3877C142.677 92.3877 143.246 92.1836 143.766 91.7754V92.6025C143.282 92.9535 142.643 93.1289 141.848 93.1289C141.071 93.1289 140.461 92.88 140.017 92.3823C139.573 91.881 139.351 91.1774 139.351 90.2715C139.351 89.4157 139.592 88.7192 140.076 88.1821C140.563 87.6414 141.166 87.3711 141.886 87.3711C142.605 87.3711 143.162 87.6038 143.556 88.0693C143.95 88.5348 144.147 89.1812 144.147 90.0083V90.4702ZM143.245 89.7236C143.241 89.2152 143.118 88.8195 142.874 88.5366C142.634 88.2537 142.299 88.1123 141.87 88.1123C141.454 88.1123 141.102 88.2609 140.812 88.5581C140.521 88.8553 140.342 89.2438 140.274 89.7236H143.245Z" fill="#4B003F"/>
-    <path d="M21.9375 30H20.9609L19.7891 28.0371C19.6816 27.8548 19.5775 27.7002 19.4766 27.5732C19.3757 27.443 19.2715 27.3372 19.1641 27.2559C19.0599 27.1745 18.946 27.1159 18.8223 27.0801C18.7018 27.041 18.5651 27.0215 18.4121 27.0215H17.7383V30H16.918V22.998H19.0078C19.3138 22.998 19.5954 23.0371 19.8525 23.1152C20.113 23.1901 20.3376 23.3057 20.5264 23.4619C20.7184 23.6182 20.8682 23.8135 20.9756 24.0479C21.083 24.279 21.1367 24.5508 21.1367 24.8633C21.1367 25.1074 21.0993 25.332 21.0244 25.5371C20.9528 25.7389 20.8486 25.9196 20.7119 26.0791C20.5785 26.2386 20.4157 26.3753 20.2236 26.4893C20.0348 26.5999 19.8216 26.6862 19.584 26.748V26.7676C19.7012 26.8197 19.8021 26.8799 19.8867 26.9482C19.9746 27.0133 20.0576 27.0915 20.1357 27.1826C20.2139 27.2738 20.2904 27.3779 20.3652 27.4951C20.4434 27.609 20.5296 27.7425 20.624 27.8955L21.9375 30ZM17.7383 23.7402V26.2793H18.8516C19.0566 26.2793 19.2454 26.2484 19.418 26.1865C19.5938 26.1247 19.7451 26.0368 19.8721 25.9229C19.999 25.8057 20.0983 25.6641 20.1699 25.498C20.2415 25.3288 20.2773 25.14 20.2773 24.9316C20.2773 24.5573 20.1553 24.266 19.9111 24.0576C19.6702 23.846 19.3203 23.7402 18.8613 23.7402H17.7383ZM26.6152 30H22.9043V22.998H26.459V23.7402H23.7246V26.0693H26.2539V26.8066H23.7246V29.2578H26.6152V30ZM32.1035 23.7402H30.082V30H29.2617V23.7402H27.2451V22.998H32.1035V23.7402ZM38.3291 27.168C38.3291 29.1341 37.4421 30.1172 35.668 30.1172C33.9688 30.1172 33.1191 29.1715 33.1191 27.2803V22.998H33.9395V27.2266C33.9395 28.6621 34.5449 29.3799 35.7559 29.3799C36.9245 29.3799 37.5088 28.6865 37.5088 27.2998V22.998H38.3291V27.168ZM45.1016 30H44.125L42.9531 28.0371C42.8457 27.8548 42.7415 27.7002 42.6406 27.5732C42.5397 27.443 42.4355 27.3372 42.3281 27.2559C42.224 27.1745 42.11 27.1159 41.9863 27.0801C41.8659 27.041 41.7292 27.0215 41.5762 27.0215H40.9023V30H40.082V22.998H42.1719C42.4779 22.998 42.7594 23.0371 43.0166 23.1152C43.277 23.1901 43.5016 23.3057 43.6904 23.4619C43.8825 23.6182 44.0322 23.8135 44.1396 24.0479C44.2471 24.279 44.3008 24.5508 44.3008 24.8633C44.3008 25.1074 44.2633 25.332 44.1885 25.5371C44.1169 25.7389 44.0127 25.9196 43.876 26.0791C43.7425 26.2386 43.5798 26.3753 43.3877 26.4893C43.1989 26.5999 42.9857 26.6862 42.748 26.748V26.7676C42.8652 26.8197 42.9661 26.8799 43.0508 26.9482C43.1387 27.0133 43.2217 27.0915 43.2998 27.1826C43.3779 27.2738 43.4544 27.3779 43.5293 27.4951C43.6074 27.609 43.6937 27.7425 43.7881 27.8955L45.1016 30ZM40.9023 23.7402V26.2793H42.0156C42.2207 26.2793 42.4095 26.2484 42.582 26.1865C42.7578 26.1247 42.9092 26.0368 43.0361 25.9229C43.1631 25.8057 43.2624 25.6641 43.334 25.498C43.4056 25.3288 43.4414 25.14 43.4414 24.9316C43.4414 24.5573 43.3193 24.266 43.0752 24.0576C42.8343 23.846 42.4844 23.7402 42.0254 23.7402H40.9023ZM51.7129 30H50.707L47.1035 24.4189C47.0124 24.279 46.9375 24.1325 46.8789 23.9795H46.8496C46.8757 24.1292 46.8887 24.4499 46.8887 24.9414V30H46.0684V22.998H47.1328L50.6387 28.4912C50.7852 28.7191 50.8796 28.8753 50.9219 28.96H50.9414C50.9089 28.7581 50.8926 28.4147 50.8926 27.9297V22.998H51.7129V30ZM57.2598 30H53.5488V22.998H57.1035V23.7402H54.3691V26.0693H56.8984V26.8066H54.3691V29.2578H57.2598V30ZM58.6074 30V22.998H60.541C63.0085 22.998 64.2422 24.1357 64.2422 26.4111C64.2422 27.4919 63.8988 28.361 63.2119 29.0186C62.5283 29.6729 61.612 30 60.4629 30H58.6074ZM59.4277 23.7402V29.2578H60.4727C61.3906 29.2578 62.1051 29.012 62.6162 28.5205C63.1273 28.029 63.3828 27.3324 63.3828 26.4307C63.3828 24.637 62.429 23.7402 60.5215 23.7402H59.4277ZM72.0742 30H68.3633V22.998H71.918V23.7402H69.1836V26.0693H71.7129V26.8066H69.1836V29.2578H72.0742V30ZM79.0664 30H78.0605L74.457 24.4189C74.3659 24.279 74.291 24.1325 74.2324 23.9795H74.2031C74.2292 24.1292 74.2422 24.4499 74.2422 24.9414V30H73.4219V22.998H74.4863L77.9922 28.4912C78.1387 28.7191 78.2331 28.8753 78.2754 28.96H78.2949C78.2624 28.7581 78.2461 28.4147 78.2461 27.9297V22.998H79.0664V30ZM85.043 23.7402H83.0215V30H82.2012V23.7402H80.1846V22.998H85.043V23.7402ZM86.9668 30H86.1465V22.998H86.9668V30ZM92.9531 23.7402H90.9316V30H90.1113V23.7402H88.0947V22.998H92.9531V23.7402ZM98.8027 22.998L96.4932 27.4121V30H95.6729V27.4316L93.4219 22.998H94.3545L95.9219 26.1621C95.9414 26.2012 95.9984 26.3444 96.0928 26.5918H96.1074C96.14 26.4811 96.2018 26.3379 96.293 26.1621L97.9336 22.998H98.8027Z" fill="#323130"/>
-</svg>
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "重複領域の例のSVGファイルの削除"
}
```

### Explanation
今回の変更では、`union-overlap-example-2-part-2.svg`というSVG画像ファイルが削除されました。このファイルは、カスタムテキスト分析サービスにおける重複領域の具体的な例や視覚的な説明を提供するために使用されていたと考えられます。

このSVGファイルの削除により、特に視覚的なデータを重視するユーザーにとっては、重要な情報源が失われることになります。重複領域の概念や識別を理解するために依存していたユーザーは、適切な情報を得ることが難しくなる可能性があります。

この変更に伴って、影響を受けるユーザーに対しては代替資料の提供や、他の形式（例：文書や新たな図表）での視覚的な説明が求められます。さらに、削除されたファイルの役割を補完するための情報をさまざまな媒体で提供することで、ユーザーが引き続き学習を続けられるようサポートすることが重要です。また、関連するドキュメントへのリンクを更新し、ユーザーが必要な情報を取得できるように留意する必要があります。

## articles/ai-services/language-service/custom-text-analytics-for-health/media/union-overlap-example-2.svg{#item-331137}

<details>
<summary>Diff</summary>
````diff
@@ -1,14 +0,0 @@
-<svg width="289" height="148" viewBox="0 0 289 148" fill="none"
-    xmlns="http://www.w3.org/2000/svg">
-    <path d="M296 0H0V148H296V0Z" fill="#F3F2F1"/>
-    <path d="M18.4336 70H17.2852V60.1973H18.4336V70ZM33.5273 63L31.4287 70H30.2666L28.8242 64.9893C28.7695 64.7979 28.7331 64.5814 28.7148 64.3398H28.6875C28.6738 64.5039 28.626 64.7158 28.5439 64.9756L26.9785 70H25.8574L23.7383 63H24.9141L26.3633 68.2637C26.4089 68.4232 26.4408 68.6328 26.459 68.8926H26.5137C26.5273 68.6921 26.5684 68.4779 26.6367 68.25L28.25 63H29.2754L30.7246 68.2773C30.7702 68.446 30.8044 68.6556 30.8271 68.9062H30.8818C30.891 68.7285 30.9297 68.5189 30.998 68.2773L32.4199 63H33.5273ZM39.8369 70H38.7158V68.9062H38.6885C38.2008 69.7448 37.4831 70.1641 36.5352 70.1641C35.8379 70.1641 35.291 69.9795 34.8945 69.6104C34.5026 69.2412 34.3066 68.7513 34.3066 68.1406C34.3066 66.8327 35.0768 66.0716 36.6172 65.8574L38.7158 65.5635C38.7158 64.374 38.235 63.7793 37.2734 63.7793C36.4303 63.7793 35.6693 64.0664 34.9902 64.6406V63.4922C35.6784 63.0547 36.4714 62.8359 37.3691 62.8359C39.0143 62.8359 39.8369 63.7064 39.8369 65.4473V70ZM38.7158 66.459L37.0273 66.6914C36.5078 66.7643 36.1159 66.8942 35.8516 67.0811C35.5872 67.2633 35.4551 67.5892 35.4551 68.0586C35.4551 68.4004 35.5758 68.6807 35.8174 68.8994C36.0635 69.1136 36.3893 69.2207 36.7949 69.2207C37.3509 69.2207 37.8089 69.027 38.1689 68.6396C38.5335 68.2477 38.7158 67.7533 38.7158 67.1562V66.459ZM47.7598 70H46.6387V66.0078C46.6387 64.5221 46.0964 63.7793 45.0117 63.7793C44.4512 63.7793 43.9863 63.9912 43.6172 64.415C43.2526 64.8343 43.0703 65.3652 43.0703 66.0078V70H41.9492V63H43.0703V64.1621H43.0977C43.6263 63.278 44.3919 62.8359 45.3945 62.8359C46.1602 62.8359 46.7458 63.0843 47.1514 63.5811C47.557 64.0732 47.7598 64.7865 47.7598 65.7207V70ZM53.126 69.9316C52.8617 70.0775 52.513 70.1504 52.0801 70.1504C50.8542 70.1504 50.2412 69.4668 50.2412 68.0996V63.957H49.0381V63H50.2412V61.291L51.3623 60.9287V63H53.126V63.957H51.3623V67.9014C51.3623 68.3708 51.4421 68.7057 51.6016 68.9062C51.7611 69.1068 52.0254 69.207 52.3945 69.207C52.6771 69.207 52.9209 69.1296 53.126 68.9746V69.9316ZM61.7119 69.9316C61.4476 70.0775 61.099 70.1504 60.666 70.1504C59.4401 70.1504 58.8271 69.4668 58.8271 68.0996V63.957H57.624V63H58.8271V61.291L59.9482 60.9287V63H61.7119V63.957H59.9482V67.9014C59.9482 68.3708 60.028 68.7057 60.1875 68.9062C60.347 69.1068 60.6113 69.207 60.9805 69.207C61.263 69.207 61.5068 69.1296 61.7119 68.9746V69.9316ZM66.1348 70.1641C65.1003 70.1641 64.2731 69.8382 63.6533 69.1865C63.0381 68.5303 62.7305 67.6621 62.7305 66.582C62.7305 65.4062 63.0518 64.488 63.6943 63.8271C64.3369 63.1663 65.2051 62.8359 66.2988 62.8359C67.3424 62.8359 68.1559 63.1572 68.7393 63.7998C69.3271 64.4424 69.6211 65.3333 69.6211 66.4727C69.6211 67.5892 69.3044 68.4847 68.6709 69.1592C68.042 69.8291 67.1966 70.1641 66.1348 70.1641ZM66.2168 63.7793C65.4967 63.7793 64.9271 64.0254 64.5078 64.5176C64.0885 65.0052 63.8789 65.6797 63.8789 66.541C63.8789 67.3704 64.0908 68.0244 64.5146 68.5029C64.9385 68.9814 65.5059 69.2207 66.2168 69.2207C66.9414 69.2207 67.4974 68.986 67.8848 68.5166C68.2767 68.0472 68.4727 67.3796 68.4727 66.5137C68.4727 65.6387 68.2767 64.9642 67.8848 64.4902C67.4974 64.0163 66.9414 63.7793 66.2168 63.7793ZM76.4023 68.9883H76.375V70H75.2539V59.6367H76.375V64.2305H76.4023C76.9538 63.3008 77.7604 62.8359 78.8223 62.8359C79.7201 62.8359 80.4219 63.1504 80.9277 63.7793C81.4382 64.4036 81.6934 65.2422 81.6934 66.2949C81.6934 67.4661 81.4085 68.4049 80.8389 69.1113C80.2692 69.8132 79.4899 70.1641 78.501 70.1641C77.5758 70.1641 76.8763 69.7721 76.4023 68.9883ZM76.375 66.165V67.1426C76.375 67.7214 76.5618 68.2135 76.9355 68.6191C77.3138 69.0202 77.7923 69.2207 78.3711 69.2207C79.0501 69.2207 79.5811 68.9609 79.9639 68.4414C80.3512 67.9219 80.5449 67.1995 80.5449 66.2744C80.5449 65.4951 80.3649 64.8844 80.0049 64.4424C79.6449 64.0003 79.1572 63.7793 78.542 63.7793C77.8903 63.7793 77.3662 64.0072 76.9697 64.4629C76.5732 64.9141 76.375 65.4814 76.375 66.165ZM89.1445 70H88.0234V68.8926H87.9961C87.5312 69.7402 86.8112 70.1641 85.8359 70.1641C84.168 70.1641 83.334 69.1706 83.334 67.1836V63H84.4482V67.0059C84.4482 68.4824 85.0133 69.2207 86.1436 69.2207C86.6904 69.2207 87.1393 69.0202 87.4902 68.6191C87.8457 68.2135 88.0234 67.6849 88.0234 67.0332V63H89.1445V70ZM96.9854 63L93.7656 71.1211C93.1914 72.5703 92.3848 73.2949 91.3457 73.2949C91.054 73.2949 90.8102 73.2653 90.6143 73.2061V72.2012C90.8558 72.2832 91.0768 72.3242 91.2773 72.3242C91.8424 72.3242 92.2663 71.987 92.5488 71.3125L93.1094 69.9863L90.375 63H91.6191L93.5127 68.3867C93.5355 68.4551 93.5833 68.6328 93.6562 68.9199H93.6973C93.7201 68.8105 93.7656 68.6374 93.834 68.4004L95.8232 63H96.9854ZM103.336 66.2949V70H102.188V60.1973H104.881C105.929 60.1973 106.74 60.4525 107.314 60.9629C107.893 61.4733 108.183 62.1934 108.183 63.123C108.183 64.0527 107.861 64.8138 107.219 65.4062C106.581 65.9987 105.717 66.2949 104.628 66.2949H103.336ZM103.336 61.2363V65.2559H104.539C105.332 65.2559 105.936 65.0758 106.351 64.7158C106.77 64.3512 106.979 63.8385 106.979 63.1777C106.979 61.8835 106.214 61.2363 104.683 61.2363H103.336ZM113.535 64.1348C113.339 63.9844 113.057 63.9092 112.688 63.9092C112.209 63.9092 111.808 64.1348 111.484 64.5859C111.165 65.0371 111.006 65.6523 111.006 66.4316V70H109.885V63H111.006V64.4424H111.033C111.193 63.9502 111.437 63.5674 111.765 63.2939C112.093 63.016 112.46 62.877 112.865 62.877C113.157 62.877 113.38 62.9089 113.535 62.9727V64.1348ZM117.678 70.1641C116.643 70.1641 115.816 69.8382 115.196 69.1865C114.581 68.5303 114.273 67.6621 114.273 66.582C114.273 65.4062 114.595 64.488 115.237 63.8271C115.88 63.1663 116.748 62.8359 117.842 62.8359C118.885 62.8359 119.699 63.1572 120.282 63.7998C120.87 64.4424 121.164 65.3333 121.164 66.4727C121.164 67.5892 120.847 68.4847 120.214 69.1592C119.585 69.8291 118.74 70.1641 117.678 70.1641ZM117.76 63.7793C117.04 63.7793 116.47 64.0254 116.051 64.5176C115.632 65.0052 115.422 65.6797 115.422 66.541C115.422 67.3704 115.634 68.0244 116.058 68.5029C116.481 68.9814 117.049 69.2207 117.76 69.2207C118.484 69.2207 119.04 68.986 119.428 68.5166C119.82 68.0472 120.016 67.3796 120.016 66.5137C120.016 65.6387 119.82 64.9642 119.428 64.4902C119.04 64.0163 118.484 63.7793 117.76 63.7793ZM122.531 69.7471V68.5439C123.142 68.9951 123.814 69.2207 124.548 69.2207C125.532 69.2207 126.024 68.8926 126.024 68.2363C126.024 68.0495 125.981 67.8923 125.895 67.7646C125.812 67.6325 125.699 67.5163 125.553 67.416C125.411 67.3158 125.243 67.2269 125.047 67.1494C124.855 67.0674 124.648 66.9831 124.425 66.8965C124.115 66.7734 123.841 66.6504 123.604 66.5273C123.372 66.3997 123.176 66.2585 123.017 66.1035C122.862 65.944 122.743 65.764 122.661 65.5635C122.584 65.363 122.545 65.1283 122.545 64.8594C122.545 64.5312 122.62 64.2419 122.771 63.9912C122.921 63.736 123.121 63.5241 123.372 63.3555C123.623 63.1823 123.908 63.0524 124.227 62.9658C124.55 62.8792 124.883 62.8359 125.225 62.8359C125.831 62.8359 126.373 62.9408 126.852 63.1504V64.2852C126.337 63.9479 125.744 63.7793 125.074 63.7793C124.865 63.7793 124.675 63.8044 124.507 63.8545C124.338 63.9001 124.192 63.9661 124.069 64.0527C123.951 64.1393 123.857 64.2441 123.789 64.3672C123.725 64.4857 123.693 64.6178 123.693 64.7637C123.693 64.946 123.725 65.0986 123.789 65.2217C123.857 65.3447 123.955 65.4541 124.083 65.5498C124.211 65.6455 124.366 65.7321 124.548 65.8096C124.73 65.887 124.938 65.9714 125.17 66.0625C125.48 66.181 125.758 66.304 126.004 66.4316C126.25 66.5547 126.46 66.696 126.633 66.8555C126.806 67.0104 126.938 67.1904 127.029 67.3955C127.125 67.6006 127.173 67.8444 127.173 68.127C127.173 68.4733 127.095 68.7741 126.94 69.0293C126.79 69.2845 126.587 69.4964 126.332 69.665C126.077 69.8337 125.783 69.959 125.45 70.041C125.118 70.123 124.769 70.1641 124.404 70.1641C123.684 70.1641 123.06 70.0251 122.531 69.7471ZM134.528 66.7803H129.586C129.604 67.5596 129.814 68.1611 130.215 68.585C130.616 69.0088 131.167 69.2207 131.869 69.2207C132.658 69.2207 133.382 68.9609 134.043 68.4414V69.4941C133.428 69.9408 132.614 70.1641 131.603 70.1641C130.614 70.1641 129.837 69.8473 129.271 69.2139C128.706 68.5758 128.424 67.6803 128.424 66.5273C128.424 65.4382 128.731 64.5518 129.347 63.8682C129.966 63.18 130.734 62.8359 131.65 62.8359C132.566 62.8359 133.275 63.1322 133.776 63.7246C134.278 64.3171 134.528 65.1396 134.528 66.1924V66.7803ZM133.38 65.8301C133.375 65.1829 133.218 64.6794 132.908 64.3193C132.603 63.9593 132.177 63.7793 131.63 63.7793C131.101 63.7793 130.652 63.9684 130.283 64.3467C129.914 64.7249 129.686 65.2194 129.6 65.8301H133.38ZM145.049 63L142.95 70H141.788L140.346 64.9893C140.291 64.7979 140.255 64.5814 140.236 64.3398H140.209C140.195 64.5039 140.147 64.7158 140.065 64.9756L138.5 70H137.379L135.26 63H136.436L137.885 68.2637C137.93 68.4232 137.962 68.6328 137.98 68.8926H138.035C138.049 68.6921 138.09 68.4779 138.158 68.25L139.771 63H140.797L142.246 68.2773C142.292 68.446 142.326 68.6556 142.349 68.9062H142.403C142.412 68.7285 142.451 68.5189 142.52 68.2773L143.941 63H145.049ZM151.358 70H150.237V68.9062H150.21C149.722 69.7448 149.005 70.1641 148.057 70.1641C147.359 70.1641 146.812 69.9795 146.416 69.6104C146.024 69.2412 145.828 68.7513 145.828 68.1406C145.828 66.8327 146.598 66.0716 148.139 65.8574L150.237 65.5635C150.237 64.374 149.757 63.7793 148.795 63.7793C147.952 63.7793 147.191 64.0664 146.512 64.6406V63.4922C147.2 63.0547 147.993 62.8359 148.891 62.8359C150.536 62.8359 151.358 63.7064 151.358 65.4473V70ZM150.237 66.459L148.549 66.6914C148.029 66.7643 147.637 66.8942 147.373 67.0811C147.109 67.2633 146.977 67.5892 146.977 68.0586C146.977 68.4004 147.097 68.6807 147.339 68.8994C147.585 69.1136 147.911 69.2207 148.316 69.2207C148.872 69.2207 149.33 69.027 149.69 68.6396C150.055 68.2477 150.237 67.7533 150.237 67.1562V66.459ZM157.121 64.1348C156.925 63.9844 156.643 63.9092 156.273 63.9092C155.795 63.9092 155.394 64.1348 155.07 64.5859C154.751 65.0371 154.592 65.6523 154.592 66.4316V70H153.471V63H154.592V64.4424H154.619C154.779 63.9502 155.022 63.5674 155.351 63.2939C155.679 63.016 156.046 62.877 156.451 62.877C156.743 62.877 156.966 62.9089 157.121 62.9727V64.1348ZM163.964 66.7803H159.021C159.04 67.5596 159.249 68.1611 159.65 68.585C160.051 69.0088 160.603 69.2207 161.305 69.2207C162.093 69.2207 162.818 68.9609 163.479 68.4414V69.4941C162.863 69.9408 162.05 70.1641 161.038 70.1641C160.049 70.1641 159.272 69.8473 158.707 69.2139C158.142 68.5758 157.859 67.6803 157.859 66.5273C157.859 65.4382 158.167 64.5518 158.782 63.8682C159.402 63.18 160.17 62.8359 161.086 62.8359C162.002 62.8359 162.711 63.1322 163.212 63.7246C163.713 64.3171 163.964 65.1396 163.964 66.1924V66.7803ZM162.815 65.8301C162.811 65.1829 162.654 64.6794 162.344 64.3193C162.038 63.9593 161.612 63.7793 161.065 63.7793C160.537 63.7793 160.088 63.9684 159.719 64.3467C159.35 64.7249 159.122 65.2194 159.035 65.8301H162.815ZM173.609 70.1641C172.219 70.1641 171.105 69.7061 170.267 68.79C169.433 67.874 169.016 66.6823 169.016 65.2148C169.016 63.638 169.442 62.3802 170.294 61.4414C171.146 60.5026 172.306 60.0332 173.773 60.0332C175.127 60.0332 176.216 60.4889 177.041 61.4004C177.87 62.3118 178.285 63.5036 178.285 64.9756C178.285 66.5752 177.861 67.8398 177.014 68.7695C176.166 69.6992 175.031 70.1641 173.609 70.1641ZM173.691 61.0723C172.661 61.0723 171.825 61.4437 171.183 62.1865C170.54 62.9294 170.219 63.9046 170.219 65.1123C170.219 66.32 170.531 67.293 171.155 68.0312C171.784 68.765 172.602 69.1318 173.609 69.1318C174.685 69.1318 175.533 68.7809 176.152 68.0791C176.772 67.3773 177.082 66.3952 177.082 65.1328C177.082 63.8385 176.781 62.8382 176.18 62.1318C175.578 61.4255 174.749 61.0723 173.691 61.0723ZM179.755 69.6035V68.25C179.91 68.3867 180.094 68.5098 180.309 68.6191C180.527 68.7285 180.755 68.8219 180.992 68.8994C181.234 68.9723 181.475 69.0293 181.717 69.0703C181.958 69.1113 182.182 69.1318 182.387 69.1318C183.093 69.1318 183.619 69.002 183.966 68.7422C184.317 68.4779 184.492 68.0996 184.492 67.6074C184.492 67.3431 184.433 67.113 184.314 66.917C184.201 66.721 184.041 66.5433 183.836 66.3838C183.631 66.2197 183.387 66.0648 183.104 65.9189C182.826 65.7686 182.526 65.6113 182.202 65.4473C181.86 65.2741 181.541 65.0986 181.245 64.9209C180.949 64.7432 180.691 64.5472 180.473 64.333C180.254 64.1188 180.081 63.8773 179.953 63.6084C179.83 63.335 179.769 63.016 179.769 62.6514C179.769 62.2048 179.867 61.8174 180.062 61.4893C180.258 61.1566 180.516 60.8831 180.835 60.6689C181.154 60.4548 181.516 60.2952 181.922 60.1904C182.332 60.0856 182.749 60.0332 183.173 60.0332C184.139 60.0332 184.843 60.1494 185.285 60.3818V61.6738C184.706 61.2728 183.964 61.0723 183.057 61.0723C182.806 61.0723 182.555 61.0996 182.305 61.1543C182.054 61.2044 181.831 61.2887 181.635 61.4072C181.439 61.5257 181.279 61.6784 181.156 61.8652C181.033 62.0521 180.972 62.2799 180.972 62.5488C180.972 62.7995 181.017 63.016 181.108 63.1982C181.204 63.3805 181.343 63.5469 181.525 63.6973C181.708 63.8477 181.929 63.9935 182.188 64.1348C182.453 64.276 182.756 64.431 183.098 64.5996C183.449 64.7728 183.781 64.9551 184.096 65.1465C184.41 65.3379 184.686 65.5498 184.923 65.7822C185.16 66.0146 185.347 66.2721 185.483 66.5547C185.625 66.8372 185.695 67.1608 185.695 67.5254C185.695 68.0085 185.6 68.4186 185.408 68.7559C185.221 69.0885 184.966 69.3597 184.643 69.5693C184.324 69.779 183.954 69.9294 183.535 70.0205C183.116 70.1162 182.674 70.1641 182.209 70.1641C182.054 70.1641 181.863 70.1504 181.635 70.123C181.407 70.1003 181.174 70.0638 180.938 70.0137C180.701 69.9681 180.475 69.9111 180.261 69.8428C180.051 69.7699 179.882 69.6901 179.755 69.6035ZM197.07 64.5107C197.07 65.4085 196.981 66.2083 196.804 66.9102C196.626 67.6074 196.366 68.1999 196.024 68.6875C195.683 69.1706 195.266 69.5397 194.773 69.7949C194.281 70.0456 193.721 70.1709 193.092 70.1709C192.445 70.1709 191.875 70.057 191.383 69.8291V68.7559C191.925 69.0612 192.504 69.2139 193.119 69.2139C193.561 69.2139 193.955 69.1227 194.302 68.9404C194.653 68.7581 194.949 68.4938 195.19 68.1475C195.432 67.7965 195.617 67.3659 195.744 66.8555C195.872 66.3451 195.936 65.7594 195.936 65.0986H195.908C195.489 65.9417 194.76 66.3633 193.721 66.3633C193.301 66.3633 192.916 66.2904 192.565 66.1445C192.215 65.9941 191.911 65.7845 191.656 65.5156C191.401 65.2422 191.203 64.9186 191.062 64.5449C190.92 64.1712 190.85 63.7588 190.85 63.3076C190.85 62.8245 190.927 62.3825 191.082 61.9814C191.242 61.5804 191.46 61.2363 191.738 60.9492C192.021 60.6576 192.354 60.432 192.736 60.2725C193.124 60.113 193.545 60.0332 194.001 60.0332C194.493 60.0332 194.928 60.1335 195.307 60.334C195.689 60.5299 196.011 60.8193 196.271 61.2021C196.53 61.5804 196.729 62.0475 196.865 62.6035C197.002 63.1595 197.07 63.7952 197.07 64.5107ZM195.86 63.5059C195.86 63.1276 195.81 62.7835 195.71 62.4736C195.614 62.1637 195.48 61.8994 195.307 61.6807C195.133 61.4574 194.926 61.2865 194.685 61.168C194.448 61.0449 194.188 60.9834 193.905 60.9834C193.636 60.9834 193.386 61.0381 193.153 61.1475C192.921 61.2523 192.718 61.4027 192.545 61.5986C192.376 61.79 192.242 62.0202 192.142 62.2891C192.046 62.5534 191.998 62.8428 191.998 63.1572C191.998 63.5036 192.044 63.8135 192.135 64.0869C192.23 64.3604 192.365 64.5928 192.538 64.7842C192.711 64.971 192.919 65.1146 193.16 65.2148C193.406 65.3151 193.677 65.3652 193.974 65.3652C194.233 65.3652 194.477 65.3174 194.705 65.2217C194.938 65.1214 195.138 64.9893 195.307 64.8252C195.48 64.6566 195.614 64.4606 195.71 64.2373C195.81 64.0094 195.86 63.7656 195.86 63.5059Z" fill="black"/>
-    <rect x="168" y="78" width="3" height="3" fill="#00188F"/>
-    <path d="M195 78H198V81H195V78Z" fill="#00188F"/>
-    <rect x="169" y="79" width="28" height="1" fill="#00188F"/>
-    <path d="M168.65 92.6885V91.625C168.772 91.7324 168.917 91.8291 169.085 91.915C169.257 92.001 169.436 92.0744 169.622 92.1353C169.812 92.1925 170.002 92.2373 170.191 92.2695C170.381 92.3018 170.557 92.3179 170.718 92.3179C171.273 92.3179 171.686 92.2158 171.958 92.0117C172.234 91.804 172.372 91.5068 172.372 91.1201C172.372 90.9124 172.326 90.7316 172.232 90.5776C172.143 90.4237 172.018 90.284 171.856 90.1587C171.695 90.0298 171.504 89.908 171.282 89.7935C171.063 89.6753 170.827 89.5518 170.573 89.4229C170.304 89.2868 170.054 89.1489 169.821 89.0093C169.588 88.8696 169.386 88.7157 169.214 88.5474C169.042 88.3791 168.906 88.1893 168.806 87.978C168.709 87.7632 168.661 87.5125 168.661 87.2261C168.661 86.8752 168.738 86.5708 168.892 86.313C169.046 86.0516 169.248 85.8368 169.499 85.6685C169.749 85.5002 170.034 85.3748 170.353 85.2925C170.675 85.2101 171.002 85.1689 171.335 85.1689C172.095 85.1689 172.648 85.2603 172.995 85.4429V86.458C172.54 86.1429 171.957 85.9854 171.244 85.9854C171.047 85.9854 170.85 86.0068 170.653 86.0498C170.456 86.0892 170.281 86.1554 170.127 86.2485C169.973 86.3416 169.848 86.4616 169.751 86.6084C169.654 86.7552 169.606 86.9342 169.606 87.1455C169.606 87.3424 169.642 87.5125 169.713 87.6558C169.789 87.799 169.898 87.9297 170.041 88.0479C170.184 88.166 170.358 88.2806 170.562 88.3916C170.77 88.5026 171.008 88.6243 171.276 88.7568C171.552 88.8929 171.813 89.0361 172.061 89.1865C172.308 89.3369 172.524 89.5034 172.71 89.686C172.897 89.8687 173.043 90.071 173.151 90.293C173.262 90.515 173.317 90.7692 173.317 91.0557C173.317 91.4352 173.242 91.7575 173.092 92.0225C172.945 92.2839 172.744 92.4969 172.49 92.6616C172.24 92.8263 171.95 92.9445 171.62 93.0161C171.291 93.0913 170.943 93.1289 170.578 93.1289C170.456 93.1289 170.306 93.1182 170.127 93.0967C169.948 93.0788 169.765 93.0501 169.579 93.0107C169.393 92.9749 169.216 92.9302 169.047 92.8765C168.883 92.8192 168.75 92.7565 168.65 92.6885ZM177.034 93.1289C176.221 93.1289 175.571 92.8729 175.084 92.3608C174.601 91.8452 174.359 91.1631 174.359 90.3145C174.359 89.3906 174.612 88.6691 175.117 88.1499C175.622 87.6307 176.304 87.3711 177.163 87.3711C177.983 87.3711 178.622 87.6235 179.081 88.1284C179.542 88.6333 179.773 89.3333 179.773 90.2285C179.773 91.1058 179.525 91.8094 179.027 92.3394C178.533 92.8657 177.868 93.1289 177.034 93.1289ZM177.099 88.1123C176.533 88.1123 176.085 88.3057 175.756 88.6924C175.426 89.0755 175.262 89.6055 175.262 90.2822C175.262 90.9339 175.428 91.4478 175.761 91.8237C176.094 92.1997 176.54 92.3877 177.099 92.3877C177.668 92.3877 178.105 92.2033 178.409 91.8345C178.717 91.4657 178.871 90.9411 178.871 90.2607C178.871 89.5732 178.717 89.0433 178.409 88.6709C178.105 88.2985 177.668 88.1123 177.099 88.1123ZM183.898 85.6309C183.727 85.5342 183.531 85.4858 183.313 85.4858C182.697 85.4858 182.389 85.8743 182.389 86.6514V87.5H183.678V88.252H182.389V93H181.514V88.252H180.574V87.5H181.514V86.6084C181.514 86.0319 181.68 85.5771 182.013 85.2441C182.346 84.9076 182.762 84.7393 183.259 84.7393C183.528 84.7393 183.741 84.7715 183.898 84.8359V85.6309ZM187.18 92.9463C186.972 93.0609 186.699 93.1182 186.358 93.1182C185.395 93.1182 184.914 92.5811 184.914 91.5068V88.252H183.968V87.5H184.914V86.1572L185.794 85.8726V87.5H187.18V88.252H185.794V91.3511C185.794 91.7199 185.857 91.9831 185.982 92.1406C186.108 92.2982 186.315 92.377 186.605 92.377C186.827 92.377 187.019 92.3161 187.18 92.1943V92.9463ZM195.285 87.5L193.636 93H192.723L191.59 89.063C191.547 88.9126 191.518 88.7425 191.504 88.5527H191.482C191.472 88.6816 191.434 88.8481 191.37 89.0522L190.14 93H189.259L187.594 87.5H188.518L189.656 91.6357C189.692 91.7611 189.717 91.9258 189.731 92.1299H189.774C189.785 91.9723 189.817 91.804 189.871 91.625L191.139 87.5H191.944L193.083 91.6465C193.119 91.779 193.146 91.9437 193.164 92.1406H193.207C193.214 92.001 193.244 91.8363 193.298 91.6465L194.415 87.5H195.285ZM200.243 93H199.362V92.1406H199.34C198.957 92.7995 198.393 93.1289 197.648 93.1289C197.101 93.1289 196.671 92.9839 196.359 92.6938C196.051 92.4038 195.897 92.0189 195.897 91.5391C195.897 90.5114 196.503 89.9134 197.713 89.7451L199.362 89.5142C199.362 88.5796 198.984 88.1123 198.229 88.1123C197.566 88.1123 196.968 88.3379 196.435 88.7891V87.8867C196.975 87.543 197.598 87.3711 198.304 87.3711C199.596 87.3711 200.243 88.055 200.243 89.4229V93ZM199.362 90.2178L198.035 90.4004C197.627 90.4577 197.319 90.5597 197.111 90.7065C196.904 90.8498 196.8 91.1058 196.8 91.4746C196.8 91.7432 196.895 91.9634 197.084 92.1353C197.278 92.3035 197.534 92.3877 197.853 92.3877C198.289 92.3877 198.649 92.2355 198.932 91.9312C199.219 91.6232 199.362 91.2347 199.362 90.7656V90.2178ZM204.771 88.3916C204.617 88.2734 204.395 88.2144 204.104 88.2144C203.729 88.2144 203.413 88.3916 203.159 88.7461C202.909 89.1006 202.783 89.584 202.783 90.1963V93H201.902V87.5H202.783V88.6333H202.805C202.93 88.2466 203.122 87.9458 203.379 87.731C203.637 87.5125 203.925 87.4033 204.244 87.4033C204.473 87.4033 204.649 87.4284 204.771 87.4785V88.3916ZM210.147 90.4702H206.264C206.278 91.0825 206.443 91.5552 206.758 91.8882C207.073 92.2212 207.506 92.3877 208.058 92.3877C208.677 92.3877 209.246 92.1836 209.766 91.7754V92.6025C209.282 92.9535 208.643 93.1289 207.848 93.1289C207.071 93.1289 206.461 92.88 206.017 92.3823C205.573 91.881 205.351 91.1774 205.351 90.2715C205.351 89.4157 205.592 88.7192 206.076 88.1821C206.563 87.6414 207.166 87.3711 207.886 87.3711C208.605 87.3711 209.162 87.6038 209.556 88.0693C209.95 88.5348 210.147 89.1812 210.147 90.0083V90.4702ZM209.245 89.7236C209.241 89.2152 209.118 88.8195 208.874 88.5366C208.634 88.2537 208.299 88.1123 207.87 88.1123C207.454 88.1123 207.102 88.2609 206.812 88.5581C206.521 88.8553 206.342 89.2438 206.274 89.7236H209.245ZM216.812 94.751H216.028C214.918 93.4834 214.363 91.9204 214.363 90.062C214.363 88.1965 214.918 86.6084 216.028 85.2979H216.823C215.699 86.6585 215.137 88.243 215.137 90.0513C215.137 91.8452 215.695 93.4118 216.812 94.751ZM218.703 93H217.822V84.8574H218.703V93ZM224.907 90.4702H221.023C221.038 91.0825 221.202 91.5552 221.518 91.8882C221.833 92.2212 222.266 92.3877 222.817 92.3877C223.437 92.3877 224.006 92.1836 224.525 91.7754V92.6025C224.042 92.9535 223.403 93.1289 222.608 93.1289C221.831 93.1289 221.22 92.88 220.776 92.3823C220.332 91.881 220.11 91.1774 220.11 90.2715C220.11 89.4157 220.352 88.7192 220.835 88.1821C221.322 87.6414 221.926 87.3711 222.646 87.3711C223.365 87.3711 223.922 87.6038 224.316 88.0693C224.71 88.5348 224.907 89.1812 224.907 90.0083V90.4702ZM224.004 89.7236C224.001 89.2152 223.877 88.8195 223.634 88.5366C223.394 88.2537 223.059 88.1123 222.629 88.1123C222.214 88.1123 221.861 88.2609 221.571 88.5581C221.281 88.8553 221.102 89.2438 221.034 89.7236H224.004ZM230.181 93H229.3V92.1406H229.279C228.896 92.7995 228.332 93.1289 227.587 93.1289C227.039 93.1289 226.609 92.9839 226.298 92.6938C225.99 92.4038 225.836 92.0189 225.836 91.5391C225.836 90.5114 226.441 89.9134 227.651 89.7451L229.3 89.5142C229.3 88.5796 228.923 88.1123 228.167 88.1123C227.505 88.1123 226.907 88.3379 226.373 88.7891V87.8867C226.914 87.543 227.537 87.3711 228.242 87.3711C229.535 87.3711 230.181 88.055 230.181 89.4229V93ZM229.3 90.2178L227.974 90.4004C227.565 90.4577 227.257 90.5597 227.05 90.7065C226.842 90.8498 226.738 91.1058 226.738 91.4746C226.738 91.7432 226.833 91.9634 227.023 92.1353C227.216 92.3035 227.472 92.3877 227.791 92.3877C228.228 92.3877 228.588 92.2355 228.871 91.9312C229.157 91.6232 229.3 91.2347 229.3 90.7656V90.2178ZM234.709 88.3916C234.555 88.2734 234.333 88.2144 234.043 88.2144C233.667 88.2144 233.352 88.3916 233.098 88.7461C232.847 89.1006 232.722 89.584 232.722 90.1963V93H231.841V87.5H232.722V88.6333H232.743C232.868 88.2466 233.06 87.9458 233.318 87.731C233.576 87.5125 233.864 87.4033 234.183 87.4033C234.412 87.4033 234.587 87.4284 234.709 87.4785V88.3916ZM240.23 93H239.35V89.8633C239.35 88.696 238.924 88.1123 238.071 88.1123C237.631 88.1123 237.266 88.2788 236.976 88.6118C236.689 88.9412 236.546 89.3584 236.546 89.8633V93H235.665V87.5H236.546V88.4131H236.567C236.983 87.7184 237.584 87.3711 238.372 87.3711C238.974 87.3711 239.434 87.5662 239.752 87.9565C240.071 88.3433 240.23 88.9036 240.23 89.6377V93ZM246.316 90.4702H242.433C242.447 91.0825 242.612 91.5552 242.927 91.8882C243.242 92.2212 243.675 92.3877 244.227 92.3877C244.846 92.3877 245.415 92.1836 245.935 91.7754V92.6025C245.451 92.9535 244.812 93.1289 244.017 93.1289C243.24 93.1289 242.63 92.88 242.186 92.3823C241.742 91.881 241.52 91.1774 241.52 90.2715C241.52 89.4157 241.761 88.7192 242.245 88.1821C242.732 87.6414 243.335 87.3711 244.055 87.3711C244.774 87.3711 245.331 87.6038 245.725 88.0693C246.119 88.5348 246.316 89.1812 246.316 90.0083V90.4702ZM245.414 89.7236C245.41 89.2152 245.286 88.8195 245.043 88.5366C244.803 88.2537 244.468 88.1123 244.039 88.1123C243.623 88.1123 243.271 88.2609 242.98 88.5581C242.69 88.8553 242.511 89.2438 242.443 89.7236H245.414ZM252.348 93H251.467V92.0654H251.445C251.037 92.7744 250.407 93.1289 249.555 93.1289C248.864 93.1289 248.31 92.8836 247.895 92.3931C247.483 91.8989 247.277 91.2275 247.277 90.3789C247.277 89.4694 247.507 88.7407 247.965 88.1929C248.423 87.645 249.034 87.3711 249.796 87.3711C250.552 87.3711 251.102 87.6683 251.445 88.2627H251.467V84.8574H252.348V93ZM251.467 90.5132V89.7021C251.467 89.2581 251.32 88.8822 251.026 88.5742C250.733 88.2663 250.36 88.1123 249.909 88.1123C249.372 88.1123 248.95 88.3092 248.642 88.7031C248.334 89.097 248.18 89.6413 248.18 90.3359C248.18 90.9697 248.326 91.471 248.62 91.8398C248.917 92.2051 249.315 92.3877 249.812 92.3877C250.303 92.3877 250.701 92.2104 251.005 91.856C251.313 91.5015 251.467 91.0539 251.467 90.5132ZM254.152 94.751H253.368C254.485 93.4118 255.044 91.8452 255.044 90.0513C255.044 88.243 254.482 86.6585 253.357 85.2979H254.152C255.27 86.6084 255.828 88.1965 255.828 90.062C255.828 91.9204 255.27 93.4834 254.152 94.751Z" fill="#00188F"/>
-    <rect x="102" y="98" width="3" height="3" fill="#EF6950"/>
-    <rect x="103" y="99" width="83" height="1" fill="#EF6950"/>
-    <path d="M102.65 112.688V111.625C102.772 111.732 102.917 111.829 103.085 111.915C103.257 112.001 103.436 112.074 103.622 112.135C103.812 112.193 104.002 112.237 104.191 112.27C104.381 112.302 104.557 112.318 104.718 112.318C105.273 112.318 105.686 112.216 105.958 112.012C106.234 111.804 106.372 111.507 106.372 111.12C106.372 110.912 106.326 110.732 106.232 110.578C106.143 110.424 106.018 110.284 105.856 110.159C105.695 110.03 105.504 109.908 105.282 109.793C105.063 109.675 104.827 109.552 104.573 109.423C104.304 109.287 104.054 109.149 103.821 109.009C103.588 108.87 103.386 108.716 103.214 108.547C103.042 108.379 102.906 108.189 102.806 107.978C102.709 107.763 102.661 107.513 102.661 107.226C102.661 106.875 102.738 106.571 102.892 106.313C103.046 106.052 103.248 105.837 103.499 105.668C103.749 105.5 104.034 105.375 104.353 105.292C104.675 105.21 105.002 105.169 105.335 105.169C106.095 105.169 106.648 105.26 106.995 105.443V106.458C106.54 106.143 105.957 105.985 105.244 105.985C105.047 105.985 104.85 106.007 104.653 106.05C104.456 106.089 104.281 106.155 104.127 106.249C103.973 106.342 103.848 106.462 103.751 106.608C103.654 106.755 103.606 106.934 103.606 107.146C103.606 107.342 103.642 107.513 103.713 107.656C103.789 107.799 103.898 107.93 104.041 108.048C104.184 108.166 104.358 108.281 104.562 108.392C104.77 108.503 105.008 108.624 105.276 108.757C105.552 108.893 105.813 109.036 106.061 109.187C106.308 109.337 106.524 109.503 106.71 109.686C106.897 109.869 107.043 110.071 107.151 110.293C107.262 110.515 107.317 110.769 107.317 111.056C107.317 111.435 107.242 111.757 107.092 112.022C106.945 112.284 106.744 112.497 106.49 112.662C106.24 112.826 105.95 112.944 105.62 113.016C105.291 113.091 104.943 113.129 104.578 113.129C104.456 113.129 104.306 113.118 104.127 113.097C103.948 113.079 103.765 113.05 103.579 113.011C103.393 112.975 103.216 112.93 103.047 112.876C102.883 112.819 102.75 112.757 102.65 112.688ZM111.034 113.129C110.221 113.129 109.571 112.873 109.084 112.361C108.601 111.845 108.359 111.163 108.359 110.314C108.359 109.391 108.612 108.669 109.117 108.15C109.622 107.631 110.304 107.371 111.163 107.371C111.983 107.371 112.622 107.624 113.081 108.128C113.542 108.633 113.773 109.333 113.773 110.229C113.773 111.106 113.525 111.809 113.027 112.339C112.533 112.866 111.868 113.129 111.034 113.129ZM111.099 108.112C110.533 108.112 110.085 108.306 109.756 108.692C109.426 109.076 109.262 109.605 109.262 110.282C109.262 110.934 109.428 111.448 109.761 111.824C110.094 112.2 110.54 112.388 111.099 112.388C111.668 112.388 112.105 112.203 112.409 111.834C112.717 111.466 112.871 110.941 112.871 110.261C112.871 109.573 112.717 109.043 112.409 108.671C112.105 108.299 111.668 108.112 111.099 108.112ZM117.898 105.631C117.727 105.534 117.531 105.486 117.313 105.486C116.697 105.486 116.389 105.874 116.389 106.651V107.5H117.678V108.252H116.389V113H115.514V108.252H114.574V107.5H115.514V106.608C115.514 106.032 115.68 105.577 116.013 105.244C116.346 104.908 116.762 104.739 117.259 104.739C117.528 104.739 117.741 104.771 117.898 104.836V105.631ZM121.18 112.946C120.972 113.061 120.699 113.118 120.358 113.118C119.395 113.118 118.914 112.581 118.914 111.507V108.252H117.968V107.5H118.914V106.157L119.794 105.873V107.5H121.18V108.252H119.794V111.351C119.794 111.72 119.857 111.983 119.982 112.141C120.108 112.298 120.315 112.377 120.605 112.377C120.827 112.377 121.019 112.316 121.18 112.194V112.946ZM129.285 107.5L127.636 113H126.723L125.59 109.063C125.547 108.913 125.518 108.743 125.504 108.553H125.482C125.472 108.682 125.434 108.848 125.37 109.052L124.14 113H123.259L121.594 107.5H122.518L123.656 111.636C123.692 111.761 123.717 111.926 123.731 112.13H123.774C123.785 111.972 123.817 111.804 123.871 111.625L125.139 107.5H125.944L127.083 111.646C127.119 111.779 127.146 111.944 127.164 112.141H127.207C127.214 112.001 127.244 111.836 127.298 111.646L128.415 107.5H129.285ZM134.243 113H133.362V112.141H133.34C132.957 112.799 132.393 113.129 131.648 113.129C131.101 113.129 130.671 112.984 130.359 112.694C130.051 112.404 129.897 112.019 129.897 111.539C129.897 110.511 130.503 109.913 131.713 109.745L133.362 109.514C133.362 108.58 132.984 108.112 132.229 108.112C131.566 108.112 130.968 108.338 130.435 108.789V107.887C130.975 107.543 131.598 107.371 132.304 107.371C133.596 107.371 134.243 108.055 134.243 109.423V113ZM133.362 110.218L132.035 110.4C131.627 110.458 131.319 110.56 131.111 110.707C130.904 110.85 130.8 111.106 130.8 111.475C130.8 111.743 130.895 111.963 131.084 112.135C131.278 112.304 131.534 112.388 131.853 112.388C132.289 112.388 132.649 112.236 132.932 111.931C133.219 111.623 133.362 111.235 133.362 110.766V110.218ZM138.771 108.392C138.617 108.273 138.395 108.214 138.104 108.214C137.729 108.214 137.413 108.392 137.159 108.746C136.909 109.101 136.783 109.584 136.783 110.196V113H135.902V107.5H136.783V108.633H136.805C136.93 108.247 137.122 107.946 137.379 107.731C137.637 107.513 137.925 107.403 138.244 107.403C138.473 107.403 138.649 107.428 138.771 107.479V108.392ZM144.147 110.47H140.264C140.278 111.083 140.443 111.555 140.758 111.888C141.073 112.221 141.506 112.388 142.058 112.388C142.677 112.388 143.246 112.184 143.766 111.775V112.603C143.282 112.953 142.643 113.129 141.848 113.129C141.071 113.129 140.461 112.88 140.017 112.382C139.573 111.881 139.351 111.177 139.351 110.271C139.351 109.416 139.592 108.719 140.076 108.182C140.563 107.641 141.166 107.371 141.886 107.371C142.605 107.371 143.162 107.604 143.556 108.069C143.95 108.535 144.147 109.181 144.147 110.008V110.47ZM143.245 109.724C143.241 109.215 143.118 108.819 142.874 108.537C142.634 108.254 142.299 108.112 141.87 108.112C141.454 108.112 141.102 108.261 140.812 108.558C140.521 108.855 140.342 109.244 140.274 109.724H143.245ZM150.812 114.751H150.028C148.918 113.483 148.363 111.92 148.363 110.062C148.363 108.196 148.918 106.608 150.028 105.298H150.823C149.699 106.659 149.137 108.243 149.137 110.051C149.137 111.845 149.695 113.412 150.812 114.751ZM152.703 113H151.822V104.857H152.703V113ZM154.938 106.104C154.78 106.104 154.646 106.05 154.535 105.942C154.424 105.835 154.368 105.699 154.368 105.534C154.368 105.369 154.424 105.233 154.535 105.126C154.646 105.015 154.78 104.959 154.938 104.959C155.099 104.959 155.235 105.015 155.346 105.126C155.46 105.233 155.518 105.369 155.518 105.534C155.518 105.692 155.46 105.826 155.346 105.937C155.235 106.048 155.099 106.104 154.938 106.104ZM155.367 113H154.486V107.5H155.367V113ZM156.817 112.801V111.856C157.297 112.21 157.825 112.388 158.402 112.388C159.175 112.388 159.562 112.13 159.562 111.614C159.562 111.467 159.528 111.344 159.46 111.244C159.396 111.14 159.306 111.049 159.191 110.97C159.08 110.891 158.948 110.821 158.794 110.76C158.644 110.696 158.481 110.63 158.305 110.562C158.062 110.465 157.847 110.368 157.661 110.271C157.478 110.171 157.324 110.06 157.199 109.938C157.077 109.813 156.984 109.672 156.919 109.514C156.859 109.357 156.828 109.172 156.828 108.961C156.828 108.703 156.887 108.476 157.005 108.279C157.124 108.078 157.281 107.912 157.478 107.779C157.675 107.643 157.899 107.541 158.149 107.473C158.404 107.405 158.665 107.371 158.934 107.371C159.41 107.371 159.836 107.453 160.212 107.618V108.51C159.807 108.245 159.342 108.112 158.815 108.112C158.651 108.112 158.502 108.132 158.37 108.171C158.237 108.207 158.123 108.259 158.026 108.327C157.933 108.395 157.859 108.478 157.806 108.574C157.756 108.667 157.73 108.771 157.73 108.886C157.73 109.029 157.756 109.149 157.806 109.246C157.859 109.342 157.936 109.428 158.037 109.503C158.137 109.579 158.259 109.647 158.402 109.708C158.545 109.768 158.708 109.835 158.891 109.906C159.134 109.999 159.353 110.096 159.546 110.196C159.739 110.293 159.904 110.404 160.04 110.529C160.176 110.651 160.28 110.792 160.352 110.954C160.427 111.115 160.464 111.306 160.464 111.528C160.464 111.8 160.403 112.037 160.282 112.237C160.164 112.438 160.004 112.604 159.804 112.737C159.603 112.869 159.372 112.968 159.111 113.032C158.849 113.097 158.576 113.129 158.289 113.129C157.723 113.129 157.233 113.02 156.817 112.801ZM164.375 112.946C164.167 113.061 163.893 113.118 163.553 113.118C162.59 113.118 162.108 112.581 162.108 111.507V108.252H161.163V107.5H162.108V106.157L162.989 105.873V107.5H164.375V108.252H162.989V111.351C162.989 111.72 163.051 111.983 163.177 112.141C163.302 112.298 163.51 112.377 163.8 112.377C164.022 112.377 164.213 112.316 164.375 112.194V112.946ZM165.572 114.751H164.788C165.905 113.412 166.464 111.845 166.464 110.051C166.464 108.243 165.902 106.659 164.777 105.298H165.572C166.689 106.608 167.248 108.196 167.248 110.062C167.248 111.92 166.689 113.483 165.572 114.751Z" fill="#EF6950"/>
-    <rect x="184" y="98" width="3" height="3" fill="#EF6950"/>
-    <path d="M22.04 33.168C22.04 35.1341 21.153 36.1172 19.3789 36.1172C17.6797 36.1172 16.8301 35.1715 16.8301 33.2803V28.998H17.6504V33.2266C17.6504 34.6621 18.2559 35.3799 19.4668 35.3799C20.6354 35.3799 21.2197 34.6865 21.2197 33.2998V28.998H22.04V33.168ZM27.9336 29.7402H25.9121V36H25.0918V29.7402H23.0752V28.998H27.9336V29.7402ZM33.373 29.7402H31.3516V36H30.5312V29.7402H28.5146V28.998H33.373V29.7402ZM38.1875 36H34.4766V28.998H38.0312V29.7402H35.2969V32.0693H37.8262V32.8066H35.2969V35.2578H38.1875V36ZM44.5547 36H43.5781L42.4062 34.0371C42.2988 33.8548 42.1947 33.7002 42.0938 33.5732C41.9928 33.443 41.8887 33.3372 41.7812 33.2559C41.6771 33.1745 41.5632 33.1159 41.4395 33.0801C41.319 33.041 41.1823 33.0215 41.0293 33.0215H40.3555V36H39.5352V28.998H41.625C41.931 28.998 42.2126 29.0371 42.4697 29.1152C42.7301 29.1901 42.9548 29.3057 43.1436 29.4619C43.3356 29.6182 43.4854 29.8135 43.5928 30.0479C43.7002 30.279 43.7539 30.5508 43.7539 30.8633C43.7539 31.1074 43.7165 31.332 43.6416 31.5371C43.57 31.7389 43.4658 31.9196 43.3291 32.0791C43.1956 32.2386 43.0329 32.3753 42.8408 32.4893C42.652 32.5999 42.4388 32.6862 42.2012 32.748V32.7676C42.3184 32.8197 42.4193 32.8799 42.5039 32.9482C42.5918 33.0133 42.6748 33.0915 42.7529 33.1826C42.8311 33.2738 42.9076 33.3779 42.9824 33.4951C43.0605 33.609 43.1468 33.7425 43.2412 33.8955L44.5547 36ZM40.3555 29.7402V32.2793H41.4688C41.6738 32.2793 41.8626 32.2484 42.0352 32.1865C42.2109 32.1247 42.3623 32.0368 42.4893 31.9229C42.6162 31.8057 42.7155 31.6641 42.7871 31.498C42.8587 31.3288 42.8945 31.14 42.8945 30.9316C42.8945 30.5573 42.7725 30.266 42.5283 30.0576C42.2874 29.846 41.9375 29.7402 41.4785 29.7402H40.3555ZM50.9414 36H50.0332L49.291 34.0371H46.3223L45.624 36H44.7109L47.3965 28.998H48.2461L50.9414 36ZM49.0225 33.2998L47.9238 30.3164C47.888 30.2188 47.8522 30.0625 47.8164 29.8477H47.7969C47.7643 30.0462 47.7269 30.2025 47.6846 30.3164L46.5957 33.2998H49.0225ZM57.6211 36H56.6152L53.0117 30.4189C52.9206 30.279 52.8457 30.1325 52.7871 29.9795H52.7578C52.7839 30.1292 52.7969 30.4499 52.7969 30.9414V36H51.9766V28.998H53.041L56.5469 34.4912C56.6934 34.7191 56.7878 34.8753 56.8301 34.96H56.8496C56.8171 34.7581 56.8008 34.4147 56.8008 33.9297V28.998H57.6211V36ZM64.2227 35.707C63.7051 35.9805 63.0605 36.1172 62.2891 36.1172C61.293 36.1172 60.4954 35.7965 59.8965 35.1553C59.2975 34.514 58.998 33.6725 58.998 32.6309C58.998 31.5111 59.335 30.6061 60.0088 29.916C60.6826 29.2259 61.5371 28.8809 62.5723 28.8809C63.2363 28.8809 63.7865 28.9769 64.2227 29.1689V30.043C63.7214 29.763 63.168 29.623 62.5625 29.623C61.7585 29.623 61.1058 29.8916 60.6045 30.4287C60.1064 30.9658 59.8574 31.6836 59.8574 32.582C59.8574 33.4349 60.0902 34.1152 60.5557 34.623C61.0244 35.1276 61.638 35.3799 62.3965 35.3799C63.0996 35.3799 63.7083 35.2236 64.2227 34.9111V35.707ZM69.3594 36H65.6484V28.998H69.2031V29.7402H66.4688V32.0693H68.998V32.8066H66.4688V35.2578H69.3594V36ZM78.8711 36H77.9629L77.2207 34.0371H74.252L73.5537 36H72.6406L75.3262 28.998H76.1758L78.8711 36ZM76.9521 33.2998L75.8535 30.3164C75.8177 30.2188 75.7819 30.0625 75.7461 29.8477H75.7266C75.694 30.0462 75.6566 30.2025 75.6143 30.3164L74.5254 33.2998H76.9521ZM85.5508 36H84.5449L80.9414 30.4189C80.8503 30.279 80.7754 30.1325 80.7168 29.9795H80.6875C80.7135 30.1292 80.7266 30.4499 80.7266 30.9414V36H79.9062V28.998H80.9707L84.4766 34.4912C84.623 34.7191 84.7174 34.8753 84.7598 34.96H84.7793C84.7467 34.7581 84.7305 34.4147 84.7305 33.9297V28.998H85.5508V36ZM87.3867 36V28.998H89.3203C91.7878 28.998 93.0215 30.1357 93.0215 32.4111C93.0215 33.4919 92.6781 34.361 91.9912 35.0186C91.3076 35.6729 90.3913 36 89.2422 36H87.3867ZM88.207 29.7402V35.2578H89.252C90.1699 35.2578 90.8844 35.012 91.3955 34.5205C91.9066 34.029 92.1621 33.3324 92.1621 32.4307C92.1621 30.637 91.2083 29.7402 89.3008 29.7402H88.207ZM97.1426 36V28.998H99.0762C101.544 28.998 102.777 30.1357 102.777 32.4111C102.777 33.4919 102.434 34.361 101.747 35.0186C101.063 35.6729 100.147 36 98.998 36H97.1426ZM97.9629 29.7402V35.2578H99.0078C99.9258 35.2578 100.64 35.012 101.151 34.5205C101.662 34.029 101.918 33.3324 101.918 32.4307C101.918 30.637 100.964 29.7402 99.0566 29.7402H97.9629ZM107.865 36H104.154V28.998H107.709V29.7402H104.975V32.0693H107.504V32.8066H104.975V35.2578H107.865V36ZM113.354 29.7402H111.332V36H110.512V29.7402H108.495V28.998H113.354V29.7402ZM118.168 36H114.457V28.998H118.012V29.7402H115.277V32.0693H117.807V32.8066H115.277V35.2578H118.168V36ZM124.281 35.707C123.764 35.9805 123.119 36.1172 122.348 36.1172C121.352 36.1172 120.554 35.7965 119.955 35.1553C119.356 34.514 119.057 33.6725 119.057 32.6309C119.057 31.5111 119.394 30.6061 120.067 29.916C120.741 29.2259 121.596 28.8809 122.631 28.8809C123.295 28.8809 123.845 28.9769 124.281 29.1689V30.043C123.78 29.763 123.227 29.623 122.621 29.623C121.817 29.623 121.164 29.8916 120.663 30.4287C120.165 30.9658 119.916 31.6836 119.916 32.582C119.916 33.4349 120.149 34.1152 120.614 34.623C121.083 35.1276 121.697 35.3799 122.455 35.3799C123.158 35.3799 123.767 35.2236 124.281 34.9111V35.707ZM129.848 29.7402H127.826V36H127.006V29.7402H124.989V28.998H129.848V29.7402ZM134.662 36H130.951V28.998H134.506V29.7402H131.771V32.0693H134.301V32.8066H131.771V35.2578H134.662V36ZM136.01 36V28.998H137.943C140.411 28.998 141.645 30.1357 141.645 32.4111C141.645 33.4919 141.301 34.361 140.614 35.0186C139.931 35.6729 139.014 36 137.865 36H136.01ZM136.83 29.7402V35.2578H137.875C138.793 35.2578 139.507 35.012 140.019 34.5205C140.53 34.029 140.785 33.3324 140.785 32.4307C140.785 30.637 139.831 29.7402 137.924 29.7402H136.83ZM150.531 35.707C150.014 35.9805 149.369 36.1172 148.598 36.1172C147.602 36.1172 146.804 35.7965 146.205 35.1553C145.606 34.514 145.307 33.6725 145.307 32.6309C145.307 31.5111 145.644 30.6061 146.317 29.916C146.991 29.2259 147.846 28.8809 148.881 28.8809C149.545 28.8809 150.095 28.9769 150.531 29.1689V30.043C150.03 29.763 149.477 29.623 148.871 29.623C148.067 29.623 147.414 29.8916 146.913 30.4287C146.415 30.9658 146.166 31.6836 146.166 32.582C146.166 33.4349 146.399 34.1152 146.864 34.623C147.333 35.1276 147.947 35.3799 148.705 35.3799C149.408 35.3799 150.017 35.2236 150.531 34.9111V35.707ZM154.506 36.1172C153.513 36.1172 152.717 35.79 152.118 35.1357C151.522 34.4814 151.225 33.6302 151.225 32.582C151.225 31.4557 151.529 30.5573 152.138 29.8867C152.746 29.2161 153.575 28.8809 154.623 28.8809C155.59 28.8809 156.368 29.2064 156.957 29.8574C157.549 30.5085 157.846 31.3597 157.846 32.4111C157.846 33.5537 157.543 34.457 156.938 35.1211C156.332 35.7852 155.521 36.1172 154.506 36.1172ZM154.564 29.623C153.829 29.623 153.231 29.8883 152.772 30.4189C152.313 30.9495 152.084 31.6462 152.084 32.5088C152.084 33.3714 152.307 34.0664 152.753 34.5938C153.202 35.1178 153.786 35.3799 154.506 35.3799C155.274 35.3799 155.88 35.1292 156.322 34.6279C156.765 34.1266 156.986 33.4251 156.986 32.5234C156.986 31.599 156.771 30.8844 156.342 30.3799C155.912 29.8753 155.32 29.623 154.564 29.623ZM166.361 36H165.546V31.3027C165.546 30.9316 165.569 30.4775 165.614 29.9404H165.595C165.517 30.2562 165.447 30.4824 165.385 30.6191L162.992 36H162.592L160.204 30.6582C160.136 30.502 160.066 30.2627 159.994 29.9404H159.975C160.001 30.2204 160.014 30.6777 160.014 31.3125V36H159.223V28.998H160.307L162.455 33.8809C162.621 34.2552 162.729 34.5352 162.777 34.7207H162.807C162.947 34.3366 163.059 34.0501 163.144 33.8613L165.336 28.998H166.361V36ZM169.027 33.3535V36H168.207V28.998H170.131C170.88 28.998 171.459 29.1803 171.869 29.5449C172.283 29.9095 172.489 30.4238 172.489 31.0879C172.489 31.752 172.26 32.2956 171.801 32.7188C171.345 33.1419 170.728 33.3535 169.95 33.3535H169.027ZM169.027 29.7402V32.6113H169.887C170.453 32.6113 170.884 32.4827 171.181 32.2256C171.48 31.9652 171.63 31.599 171.63 31.127C171.63 30.2025 171.083 29.7402 169.989 29.7402H169.027ZM176.635 36.1172C175.642 36.1172 174.846 35.79 174.247 35.1357C173.651 34.4814 173.354 33.6302 173.354 32.582C173.354 31.4557 173.658 30.5573 174.267 29.8867C174.875 29.2161 175.704 28.8809 176.752 28.8809C177.719 28.8809 178.497 29.2064 179.086 29.8574C179.678 30.5085 179.975 31.3597 179.975 32.4111C179.975 33.5537 179.672 34.457 179.066 35.1211C178.461 35.7852 177.65 36.1172 176.635 36.1172ZM176.693 29.623C175.958 29.623 175.36 29.8883 174.901 30.4189C174.442 30.9495 174.213 31.6462 174.213 32.5088C174.213 33.3714 174.436 34.0664 174.882 34.5938C175.331 35.1178 175.915 35.3799 176.635 35.3799C177.403 35.3799 178.008 35.1292 178.451 34.6279C178.894 34.1266 179.115 33.4251 179.115 32.5234C179.115 31.599 178.9 30.8844 178.471 30.3799C178.041 29.8753 177.449 29.623 176.693 29.623ZM186.996 36H185.99L182.387 30.4189C182.296 30.279 182.221 30.1325 182.162 29.9795H182.133C182.159 30.1292 182.172 30.4499 182.172 30.9414V36H181.352V28.998H182.416L185.922 34.4912C186.068 34.7191 186.163 34.8753 186.205 34.96H186.225C186.192 34.7581 186.176 34.4147 186.176 33.9297V28.998H186.996V36ZM192.543 36H188.832V28.998H192.387V29.7402H189.652V32.0693H192.182V32.8066H189.652V35.2578H192.543V36ZM199.535 36H198.529L194.926 30.4189C194.835 30.279 194.76 30.1325 194.701 29.9795H194.672C194.698 30.1292 194.711 30.4499 194.711 30.9414V36H193.891V28.998H194.955L198.461 34.4912C198.607 34.7191 198.702 34.8753 198.744 34.96H198.764C198.731 34.7581 198.715 34.4147 198.715 33.9297V28.998H199.535V36ZM205.512 29.7402H203.49V36H202.67V29.7402H200.653V28.998H205.512V29.7402ZM206.093 35.7168V34.75C206.203 34.8477 206.335 34.9355 206.488 35.0137C206.645 35.0918 206.807 35.1585 206.977 35.2139C207.149 35.266 207.322 35.3066 207.494 35.3359C207.667 35.3652 207.826 35.3799 207.973 35.3799C208.477 35.3799 208.853 35.2871 209.101 35.1016C209.351 34.9128 209.477 34.6426 209.477 34.291C209.477 34.1022 209.434 33.9378 209.35 33.7979C209.268 33.6579 209.154 33.5309 209.008 33.417C208.861 33.2998 208.687 33.1891 208.485 33.085C208.287 32.9775 208.072 32.8652 207.841 32.748C207.597 32.6243 207.369 32.499 207.157 32.3721C206.946 32.2451 206.762 32.1051 206.605 31.9521C206.449 31.7992 206.326 31.6266 206.234 31.4346C206.146 31.2393 206.103 31.0114 206.103 30.751C206.103 30.432 206.173 30.1553 206.312 29.9209C206.452 29.6833 206.636 29.488 206.864 29.335C207.092 29.182 207.351 29.068 207.641 28.9932C207.934 28.9183 208.231 28.8809 208.534 28.8809C209.224 28.8809 209.727 28.9639 210.043 29.1299V30.0527C209.63 29.7663 209.099 29.623 208.451 29.623C208.272 29.623 208.093 29.6426 207.914 29.6816C207.735 29.7174 207.576 29.7777 207.436 29.8623C207.296 29.9469 207.182 30.056 207.094 30.1895C207.006 30.3229 206.962 30.4857 206.962 30.6777C206.962 30.8568 206.994 31.0114 207.06 31.1416C207.128 31.2718 207.227 31.3906 207.357 31.498C207.488 31.6055 207.646 31.7096 207.831 31.8105C208.02 31.9115 208.236 32.0221 208.48 32.1426C208.731 32.2663 208.969 32.3965 209.193 32.5332C209.418 32.6699 209.615 32.8213 209.784 32.9873C209.953 33.1533 210.087 33.3372 210.185 33.5391C210.285 33.7409 210.336 33.972 210.336 34.2324C210.336 34.5775 210.268 34.8704 210.131 35.1113C209.997 35.349 209.815 35.5426 209.584 35.6924C209.356 35.8421 209.092 35.9495 208.793 36.0146C208.493 36.083 208.178 36.1172 207.846 36.1172C207.735 36.1172 207.598 36.1074 207.436 36.0879C207.273 36.0716 207.107 36.0456 206.938 36.0098C206.768 35.9772 206.607 35.9365 206.454 35.8877C206.304 35.8356 206.184 35.7786 206.093 35.7168Z" fill="#323130"/>
-</svg>
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "重複領域の例のSVGファイルの削除"
}
```

### Explanation
この変更では、`union-overlap-example-2.svg`というSVGファイルが削除されました。このファイルは、カスタムテキスト分析機能における重複領域の例を示す視覚的な資料を提供していたと見られます。

このSVGファイルの削除により、ユーザーは該当する重複領域の理解を助けるためのビジュアルリソースを失うことになります。特に、このようなビジュアル資料に依存している学習者や開発者にとっては、情報の不足が生じ、機能の意図や使用法の理解が困難になる可能性があります。

この変更による影響を最小限に抑えるために、削除されたファイルの内容に代わる説明文や図表を提供することが重要です。また、類似の情報が含まれている他のリソースを参照できるよう、情報の不足を補完する方法を検討する必要があります。これにより、ユーザーが引き続き必要な情報を得られ、機能を適切に活用できるよう支援することが期待されます。

## articles/ai-services/language-service/custom-text-analytics-for-health/overview.md{#item-6f599b}

<details>
<summary>Diff</summary>
````diff
@@ -1,79 +0,0 @@
----
-title: Custom Text Analytics for health - Azure AI services
-titleSuffix: Azure AI services
-description: Customize an AI model to label and extract healthcare information from documents using Azure AI services.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: overview
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h
----
-
-# What is custom Text Analytics for health?
-
-> [!NOTE]
-> Custom text analytics for health (preview) will be retired on 10 January 2025, please transition to other custom model training services, such as custom named entity recognition in Azure AI Language, by that date. From now to 10 January 2025, you can continue to use custom text analytics for health (preview) in your existing projects without disruption. You can’t create new projects. On 10 January 2025 – workloads running on custom text analytics for health (preview) will be deleted and associated project data will be lost.
-
-Custom Text Analytics for health is one of the custom features offered by [Azure AI Language](../overview.md). It is a cloud-based API service that applies machine-learning intelligence to enable you to build custom models on top of [Text Analytics for health](../text-analytics-for-health/overview.md) for custom healthcare entity recognition tasks.
-
-Custom Text Analytics for health enables users to build custom AI models to extract healthcare specific entities from unstructured text, such as clinical notes and reports. By creating a custom Text Analytics for health project, developers can iteratively define new vocabulary, label data, train, evaluate, and improve model performance before making it available for consumption. The quality of the labeled data greatly impacts model performance. To simplify building and customizing your model, the service offers a web portal that can be accessed through the [Language studio](https://aka.ms/languageStudio). You can easily get started with the service by following the steps in this [quickstart](quickstart.md). 
- 
-This documentation contains the following article types:
-
-* [Quickstarts](quickstart.md) are getting-started instructions to guide you through creating making requests to the service.
-* [Concepts](concepts/evaluation-metrics.md) provide explanations of the service functionality and features.
-* [How-to guides](how-to/label-data.md) contain instructions for using the service in more specific or customized ways.
-
-## Example usage scenarios
-
-Similarly to Text Analytics for health, custom Text Analytics for health can be used in multiple [scenarios](../text-analytics-for-health/overview.md#example-use-cases) across a variety of healthcare industries. However, the main usage of this feature is to provide a layer of customization on top of Text Analytics for health to extend its existing entity map.
-
-
-## Project development lifecycle
-
-Using custom Text Analytics for health typically involves several different steps. 
-
-:::image type="content" source="media/development-lifecycle.png" alt-text="A diagram showing the project development lifecycle when working with custom models." lightbox="media/development-lifecycle.png":::
-
-* **Define your schema**: Know your data and define the new entities you want extracted on top of the existing Text Analytics for health entity map. Avoid ambiguity.
-
-* **Label your data**: Labeling data is a key factor in determining model performance. Label precisely, consistently and completely.
-    * **Label precisely**: Label each entity to its right type always. Only include what you want extracted, avoid unnecessary data in your labels.
-    * **Label consistently**:  The same entity should have the same label across all the files.
-    * **Label completely**: Label all the instances of the entity in all your files.
-
-* **Train the model**: Your model starts learning from your labeled data.
-
-* **View the model's performance**: After training is completed, view the model's evaluation details, its performance and guidance on how to improve it. 
-
-* **Deploy the model**: Deploying a model makes it available for use via an API.
-
-* **Extract entities**: Use your custom models for entity extraction tasks.
-
-## Reference documentation and code samples
-
-As you use custom Text Analytics for health, see the following reference documentation for Azure AI Language:
-
-|APIs| Reference documentation|
-|---------|---------|---------|
-|REST APIs (Authoring)   | [REST API documentation](/rest/api/language/2023-04-01/text-analysis-authoring)        |
-|REST APIs (Runtime)    | [REST API documentation](/rest/api/language/text-analysis-runtime/analyze-text)        |
-
-
-## Responsible AI 
-
-An AI system includes not only the technology, but also the people who will use it, the people who will be affected by it, and the environment in which it is deployed. Read the [transparency note for Text Analytics for health](/legal/cognitive-services/language-service/transparency-note-health?context=/azure/ai-services/language-service/context/context) to learn about responsible AI use and deployment in your systems. You can also see the following articles for more information:
-
-[!INCLUDE [Responsible AI links](../includes/overview-responsible-ai-links.md)]
-
-
-## Next steps
-
-* Use the [quickstart article](quickstart.md) to start using custom Text Analytics for health.  
-
-* As you go through the project development lifecycle, review the glossary to learn more about the terms used throughout the documentation for this feature. 
-
-* Remember to view the [service limits](reference/service-limits.md) for information such as [regional availability](reference/service-limits.md#regional-availability).
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析の概要文書の削除"
}
```

### Explanation
この変更は、`custom-text-analytics-for-health/overview.md`というファイルの削除に関するものであり、内容が79行削除されました。この文書は、Azure AIのカスタムテキスト分析サービスに関する概要を提供しており、ユーザーがこのサービスの機能や利点を理解するための重要なリソースでした。

削除された文書には、カスタムテキスト分析サービスの定義、機能、使用例、プロジェクトの開発ライフサイクル、リファレンスドキュメント、責任あるAIの使用に関する情報が含まれていました。この変更は、特にこの機能を利用しているユーザーにとって、重要な情報を欠くことになり、サービスの利用方法の理解に影響を与える可能性があります。

今後、ユーザーは代わりに他のリソースを参照するか、新しいドキュメントが提供されるまで情報を探し続ける必要があります。また、プロジェクト開発の一環としてカスタムモデルの使用を促進し、利用者がサポートを受けられる環境を整備することが求められます。このような変更によって生じる影響を軽減するため、代替の情報源やサポートリソースの提供が重要です。

## articles/ai-services/language-service/custom-text-analytics-for-health/quickstart.md{#item-5bcba3}

<details>
<summary>Diff</summary>
````diff
@@ -1,50 +0,0 @@
----
-title: Quickstart - Custom Text Analytics for health (Custom TA4H)
-titleSuffix: Azure AI services
-description: Quickly start building an AI model to categorize and extract information from healthcare unstructured text.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: quickstart
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-TA4H, mode-other
-zone_pivot_groups: usage-custom-language-features
----
-
-# Quickstart: custom Text Analytics for health
-
-> [!NOTE]
-> Custom text analytics for health (preview) will be retired on 10 January 2025, please transition to other custom model training services, such as custom named entity recognition in Azure AI Language, by that date. From now to 10 January 2025, you can continue to use custom text analytics for health (preview) in your existing projects without disruption. You can’t create new projects. On 10 January 2025 – workloads running on custom text analytics for health (preview) will be deleted and associated project data will be lost.
-
-Use this article to get started with creating a custom Text Analytics for health project where you can train custom models on top of Text Analytics for health for custom entity recognition. A model is artificial intelligence software that's trained to do a certain task. For this system, the models extract healthcare related named entities and are trained by learning from labeled data.
-
-In this article, we use Language Studio to demonstrate key concepts of custom Text Analytics for health. As an example we’ll build a custom Text Analytics for health model to extract the Facility or treatment location from short discharge notes.
-
-::: zone pivot="language-studio"
-
-[!INCLUDE [Language Studio quickstart](includes/quickstarts/language-studio.md)]
-
-::: zone-end
-
-::: zone pivot="rest-api"
-
-[!INCLUDE [REST API quickstart](includes/quickstarts/rest-api.md)]
-
-::: zone-end
-
-## Next steps
-
-* [Text analytics for health overview](./overview.md)
-
-After you've created entity extraction model, you can:
-
-* [Use the runtime API to extract entities](how-to/call-api.md)
-
-When you start to create your own custom Text Analytics for health projects, use the how-to articles to learn more about data labeling, training and consuming your model in greater detail:
-
-* [Data selection and schema design](how-to/design-schema.md)
-* [Tag data](how-to/label-data.md)
-* [Train a model](how-to/train-model.md)
-* [Model evaluation](how-to/view-model-evaluation.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析のクイックスタート文書の削除"
}
```

### Explanation
この変更では、`quickstart.md`というファイルが削除されました。この文書は、カスタムテキスト分析サービスにおけるプロジェクトの作成方法を迅速に始めるための手引きを提供しており、全体で50行の内容が削除されています。

削除された文書には、カスタムモデルの作成方法や、データから医療関連のエンティティを抽出する方法、Language StudioやREST APIを使った具体的な手順が含まれていました。また、クイックスタートの後に続くステップとして、エンティティ抽出モデルの使用方法やデータのラベル付け、モデルのトレーニング、評価についてのさらなるリソースが参照されていました。

この変更の影響により、特に新しいプロジェクトを開始したり、このサービスに初めて触れるユーザーにとっては、重要なガイダンスが欠落することになります。ユーザーは新たに文書の作成や参照方法を模索しなければならず、これが学習や実践における障害となる可能性があります。今後は代替の情報源や、他の関連文書へと誘導することで、利用者の教育とサポートが必要です。

## articles/ai-services/language-service/custom-text-analytics-for-health/reference/glossary.md{#item-f2ab66}

<details>
<summary>Diff</summary>
````diff
@@ -1,69 +0,0 @@
----
-title: Definitions used in custom Text Analytics for health
-titleSuffix: Azure AI services
-description: Learn about definitions used in custom Text Analytics for health
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: overview
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-TA4H
----
-
-# Terms and definitions used in custom Text Analytics for health
-
-Use this article to learn about some of the definitions and terms you may encounter when using Custom Text Analytics for health
-
-## Entity
-Entities are words in input data that describe information relating to a specific category or concept. If your entity is complex and you would like your model to identify specific parts, you can break your entity into subentities. For example, you might want your model to predict an address, but also the subentities of street, city, state, and zipcode. 
-
-## F1 score
-The F1 score is a function of Precision and Recall. It's needed when you seek a balance between [precision](#precision) and [recall](#recall).
-
-## Prebuilt entity component
-
-Prebuilt entity components represent pretrained entity components that belong to the [Text Analytics for health entity map](../../text-analytics-for-health/concepts/health-entity-categories.md). These entities are automatically loaded into your project as entities with prebuilt components. You can define list components for entities with prebuilt components but you cannot add learned components. Similarly, you can create new entities with learned and list components, but you cannot populate them with additional prebuilt components.
-
-
-## Learned entity component
-
-The learned entity component uses the entity tags you label your text with to train a machine learned model. The model learns to predict where the entity is, based on the context within the text. Your labels provide examples of where the entity is expected to be present in text, based on the meaning of the words around it and as the words that were labeled. This component is only defined if you add labels by labeling your data for the entity. If you do not label any data with the entity, it will not have a learned component. Learned components cannot be added to entities with prebuilt components.
-
-## List entity component
-A list entity component represents a fixed, closed set of related words along with their synonyms. List entities are exact matches, unlike machined learned entities.
-
-The entity will be predicted if a word in the list entity is included in the list. For example, if you have a list entity called "clinics" and you have the words "clinic a, clinic b, clinic c" in the list, then the size entity will be predicted for all instances of the input data where "clinic a, clinic b, clinic c" are used regardless of the context. List components can be added to all entities regardless of whether they are prebuilt or newly defined.
-
-## Model
-A model is an object that's trained to do a certain task, in this case custom Text Analytics for health models perform all the features of Text Analytics for health in addition to custom entity extraction for the user's defined entities. Models are trained by providing labeled data to learn from so they can later be used to understand context from the input text.
-
-* **Model evaluation** is the process that happens right after training to know how well does your model perform.
-* **Deployment** is the process of assigning your model to a deployment to make it available for use via the [prediction API](https://aka.ms/ct-runtime-swagger).
-
-## Overfitting
-
-Overfitting happens when the model is fixated on the specific examples and is not able to generalize well.
-
-## Precision
-Measures how precise/accurate your model is. It's the ratio between the correctly identified positives (true positives) and all identified positives. The precision metric reveals how many of the predicted entities are correctly labeled.
-
-## Project
-A project is a work area for building your custom ML models based on your data. Your project can only be accessed by you and others who have access to the Azure resource being used.
-
-## Recall
-Measures the model's ability to predict actual positive entities. It's the ratio between the predicted true positives and what was actually labeled. The recall metric reveals how many of the predicted entities are correct.
-
-
-## Schema
-Schema is defined as the combination of entities within your project. Schema design is a crucial part of your project's success. When creating a schema, you want think about what are the new entities should you add to your project to extend the existing [Text Analytics for health entity map](../../text-analytics-for-health/concepts/health-entity-categories.md) and which new vocabulary should you add to the prebuilt entities using list components to enhance their recall. For example, adding a new entity for patient name or extending the prebuilt entity "Medication Name" with a new research drug (Ex: research drug A).
-
-## Training data
-Training data is the set of information that is needed to train a model.
-
-
-## Next steps
-
-* [Data and service limits](service-limits.md).
-
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析の用語集文書の削除"
}
```

### Explanation
この変更では、カスタムテキスト分析の用語集(`glossary.md`)が削除されました。この文書には、カスタムテキスト分析サービスを使用する際に遭遇する可能性のある用語と定義が含まれており、全体で69行の内容が削除されています。

削除された用語集には、エンティティ、F1スコア、モデル、過学習、精度、リコール、トレーニングデータなど、サービスを効果的に利用するために重要な用語の説明が含まれていました。これにより、利用者はカスタムテキスト分析を理解し、効果的に使用するための基盤を持っている必要があります。

この文書の削除は、特に新しいユーザーやサービスを学ぶ過程にある開発者にとって、概念の理解や適切な用語の使用に困難をもたらす可能性があります。今後、代わりに他の資料が提供されることが望まれます。また、ユーザーが必要な用語の定義を容易に探せるように、関連するドキュメントの整備を進めるべきです。

## articles/ai-services/language-service/custom-text-analytics-for-health/reference/service-limits.md{#item-b62cd6}

<details>
<summary>Diff</summary>
````diff
@@ -1,93 +0,0 @@
----
-title: Custom Text Analytics for health service limits
-titleSuffix: Azure AI services
-description: Learn about the data and service limits when using Custom Text Analytics for health.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: conceptual
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h, references_regions
----
-
-# Custom Text Analytics for health service limits
-
-Use this article to learn about the data and service limits when using custom Text Analytics for health.
-
-## Language resource limits
-
-* Your Language resource has to be created in one of the [supported regions](#regional-availability).
-
-* Your resource must be one of the supported pricing tiers:
-    
-    |Tier|Description|Limit|
-    |--|--|--|
-    |S |Paid tier|You can have unlimited Language S tier resources per subscription. | 
-    
-    
-* You can only connect one storage account per resource. This process is irreversible. If you connect a storage account to your resource, you cannot unlink it later. Learn more about [connecting a storage account](../how-to/create-project.md#create-language-resource-and-connect-storage-account)
-
-* You can have up to 500 projects per resource.
-
-* Project names have to be unique within the same resource across all custom features.
-
-## Regional availability 
-
-See [Language service regional availability](../../concepts/regional-support.md#custom-text-analytics-for-health).
-
-## API limits
-
-|Item|Request type| Maximum limit|
-|:-|:-|:-|
-|Authoring API|POST|10 per minute|
-|Authoring API|GET|100 per minute|
-|Prediction API|GET/POST|1,000 per minute|
-|Document size|--|125,000 characters. You can send up to 20 documents as long as they collectively do not exceed 125,000 characters|
-
-> [!TIP]
-> If you need to send larger files than the limit allows, you can break the text into smaller chunks of text before sending them to the API. You use can the [chunk command from CLUtils](https://github.com/microsoft/CognitiveServicesLanguageUtilities/blob/main/CustomTextAnalytics.CLUtils/Solution/CogSLanguageUtilities.ViewLayer.CliCommands/Commands/ChunkCommand/README.md) for this process.
-
-## Quota limits
-
-|Pricing tier |Item |Limit |
-| --- | --- | ---|
-|S|Training time| Unlimited, free |
-|S|Prediction Calls| 5,000 text records for free per language resource|
-
-## Document limits
-
-* You can only use `.txt`. files. If your data is in another format, you can use the [CLUtils parse command](https://github.com/microsoft/CognitiveServicesLanguageUtilities/blob/main/CustomTextAnalytics.CLUtils/Solution/CogSLanguageUtilities.ViewLayer.CliCommands/Commands/ParseCommand/README.md) to open your document and extract the text.
-
-* All files uploaded in your container must contain data. Empty files are not allowed for training.
-
-* All files should be available at the root of your container.
-
-## Data limits
-
-The following limits are observed for authoring.
-
-|Item|Lower Limit| Upper Limit |
-| --- | --- | --- |
-|Documents count | 10 | 100,000 |
-|Document length in characters | 1 | 128,000 characters; approximately 28,000 words or 56 pages. |
-|Count of entity types | 1 | 200 |
-|Entity length in characters | 1 | 500 |
-|Count of trained models per project| 0 | 10 |
-|Count of deployments per project| 0 | 10 |
-
-## Naming limits
-
-| Item | Limits |
-|--|--|
-| Project name |  You can only use letters `(a-z, A-Z)`, and numbers `(0-9)` , symbols  `_ . -`, with no spaces. Maximum allowed length is 50 characters. |
-| Model name |  You can only use letters `(a-z, A-Z)`, numbers `(0-9)` and symbols `_ . -`. Maximum allowed length is 50 characters.  |
-| Deployment name |  You can only use letters `(a-z, A-Z)`, numbers `(0-9)` and symbols `_ . -`. Maximum allowed length is 50 characters.  |
-| Entity name| You can only use letters `(a-z, A-Z)`, numbers `(0-9)` and all symbols except ":", `$ & %  * (  ) + ~ # / ?`. Maximum allowed length is 50 characters. See the supported [data format](../concepts/data-formats.md#entity-naming-rules) for more information on entity names when importing a labels file. |
-| Document name | You can only use letters `(a-z, A-Z)`, and numbers `(0-9)` with no spaces. |
-
-
-## Next steps
-
-* [Custom text analytics for health overview](../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタムテキスト分析のサービス制限に関する文書の削除"
}
```

### Explanation
この変更では、カスタムテキスト分析のサービス制限に関する文書(`service-limits.md`)が削除されました。この文書には、カスタムテキスト分析サービスを使用する際のデータやサービスの制限に関する重要な情報が含まれており、全体で93行の内容が削除されています。

削除された文書には、言語リソースの制限、APIの制限、ドキュメントの制限、データの制限、命名の制限など、サービスを利用する上で必要な技術的制限についての詳細が記載されていました。例えば、プロジェクト名は50文字以内で、使用することができる文字や数字の制限があること、また、APIリクエストの最大制限が設定されていることなどが具体的に示されていました。

この文書の削除により、特に新しいユーザーやサービスを導入しようとしている開発者にとって、必要な制限を把握し、適切にリソースを設定することが困難になる可能性があります。新しい情報源が提供されない限り、ユーザーは重要な制限事項を理解する手段を失うことになります。したがって、この情報の代替となるリソースを準備し、利用者に必要なガイダンスを提供することが求められます。

## articles/ai-services/language-service/index.yml{#item-c9444f}

<details>
<summary>Diff</summary>
````diff
@@ -53,9 +53,6 @@ conceptualContent:
         - itemType: overview
           text: Text analytics for health
           url:  text-analytics-for-health/overview.md
-        - itemType: overview
-          text: Custom text analytics for health
-          url:  custom-text-analytics-for-health/overview.md
     - title: Summarize text-based content
       summary: Summarize lengthy documents and conversation transcripts.
       links:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムテキスト分析の概要に関する項目の削除"
}
```

### Explanation
この変更では、AIサービスのインデックスファイル(`index.yml`)が修正され、カスタムテキスト分析に関連する概要項目が削除されました。具体的には、カスタムテキスト分析の概要に関する3行が削除されました。

削除された項目は、カスタムテキスト分析に関する情報のリンクを含んでおり、そのセクションは「カスタムテキスト分析の健康」というタイトルで記載されていました。この変更により、ユーザーはAIサービスのインデックスからカスタムテキスト分析の概要に直接アクセスできなくなります。

これは、サービスの構造が変更されたことを示しており、今後はカスタムテキスト分析に関する情報を他の方法で提供することになる可能性があります。この変更は、文書の整合性を高めたり、情報の整理を目的としていると思われますが、ユーザーにとっては新たな情報源を探す手間が増えることになります。

## articles/ai-services/language-service/overview.md{#item-f138b4}

<details>
<summary>Diff</summary>
````diff
@@ -180,17 +180,6 @@ The Language service also provides several new features as well, which can eithe
    :::column-end:::
 :::row-end:::
 
-### Custom text analytics for health
-
-:::row:::
-   :::column span="":::
-      :::image type="content" source="text-analytics-for-health/media/call-api/health-named-entity-recognition.png" alt-text="A screenshot of a custom text analytics for health example." lightbox="text-analytics-for-health/media/call-api/health-named-entity-recognition.png":::
-   :::column-end:::
-   :::column span="":::
-      [Custom text analytics for health](./custom-text-analytics-for-health/overview.md) is a custom feature that extract healthcare specific entities from unstructured text, using a model you create.  
-   :::column-end:::
-:::row-end:::
-
 ## Which Language service feature should I use?
 
 This section will help you decide which Language service feature you should use for your application:
@@ -206,7 +195,6 @@ This section will help you decide which Language service feature you should use
 | Disambiguate entities and get links to Wikipedia. | Unstructured text | [Entity linking](./entity-linking/overview.md) | | 
 | Classify documents into one or more categories. | Unstructured text | [Custom text classification](./custom-text-classification/overview.md) | ✓|
 | Extract medical information from clinical/medical documents, without building a model. | Unstructured text | [Text analytics for health](./text-analytics-for-health/overview.md) | |
-| Extract medical information from clinical/medical documents using a model that's trained on your data. | Unstructured text | [Custom text analytics for health](./custom-text-analytics-for-health/overview.md) | |
 | Build a conversational application that responds to user inputs. | Unstructured user inputs | [Question answering](./question-answering/overview.md) | ✓ |
 | Detect the language that a text was written in. | Unstructured text | [Language detection](./language-detection/overview.md) | | 
 | Predict the intention of user inputs and extract information from them. | Unstructured user inputs | [Conversational language understanding](./conversational-language-understanding/overview.md) | ✓ |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "健康に関するカスタムテキスト分析の情報の削除"
}
```

### Explanation
この変更では、言語サービスの概要文書(`overview.md`)が修正され、カスタムテキスト分析に関するセクションが削除されました。具体的には、12行が削除され、その中にはカスタムテキスト分析の健康に特化した機能やそれに関連する説明が含まれていました。

削除されたセクションでは、カスタムテキスト分析が医療特有のエンティティを抽出するために使用されることが説明されており、視覚的なイメージも添えられていました。この機能が削除されたことにより、読者はこの特定の機能を今後の文書から直接確認することができなくなります。

この更新は、情報の再編成や文書のシンプル化を図るためのものと考えられますが、ユーザーにとっては、特に医療関連のデータを扱っている場合、その機能についての情報が失われる可能性があるため、他のリソースを探し直す必要があるかもしれません。これにより、利用者が必要なサービス機能に簡単にアクセスできるようにするために、代替情報の提供が重要です。

## articles/ai-services/language-service/sentiment-opinion-mining/custom/concepts/data-formats.md{#item-b252b4}

<details>
<summary>Diff</summary>
````diff
@@ -1,103 +0,0 @@
----
-title: Custom sentiment analysis data formats
-titleSuffix: Azure AI services
-description: Learn about the data formats accepted by custom sentiment analysis.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: conceptual
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ner
----
-
-# Accepted custom sentiment analysis data formats
-
-If you are trying to [import your data](../how-to/create-project.md#import-a-custom-sentiment-analysis-project) into custom sentiment analysis, it has to follow a specific format. If you don't have data to import, you can [create your project](../how-to/create-project.md) and use Language Studio to [label your documents](../how-to/label-data.md).
-
-## Labels file format
-
-Your Labels file should be in the `json` format below to be used in [importing](../how-to/create-project.md#import-a-custom-sentiment-analysis-project) your labels into a project.
-
-```json
-{
-    "projectFileVersion": "2023-04-15-preview",
-    "stringIndexType": "Utf16CodeUnit",
-    "metadata": {
-        "projectKind": "CustomTextSentiment",
-        "storageInputContainerName": "custom-sentiment-2",
-        "projectName": "sa-test",
-        "multilingual": false,
-        "description": "",
-        "language": "en-us"
-    },
-    "assets": {
-        "projectKind": "CustomTextSentiment",
-        "documents": [
-            {
-                "location": "document_1.txt",
-                "language": "en-us",
-                "sentimentSpans": [
-                    {
-                        "category": "positive",
-                        "offset": 0,
-                        "length": 60
-                    },
-                    {
-                        "category": "neutral",
-                        "offset": 61,
-                        "length": 31
-                    }
-                ],
-                "dataset": "Train"
-            },
-            {
-                "location": "document_2.txt",
-                "language": "en-us",
-                "sentimentSpans": [
-                    {
-                        "category": "positive",
-                        "offset": 0,
-                        "length": 50
-                    },
-                    {
-                        "category": "positive",
-                        "offset": 51,
-                        "length": 49
-                    },
-                    {
-                        "category": "positive",
-                        "offset": 101,
-                        "length": 26
-                    }
-                ],
-                "dataset": "Train"
-            }
-        ]
-    }
-}
-
-```
-
-|Key  |Placeholder  |Value  | Example |
-|---------|---------|----------|--|
-| `multilingual` | `true`| A boolean value that enables you to have documents in multiple languages in your dataset and when your model is deployed you can query the model in any supported language (not necessarily included in your training documents). See [language support](../../language-support.md#multi-lingual-option-custom-sentiment-analysis-only) to learn more about multilingual support. | `true`|
-|`projectName`|`{PROJECT-NAME}`|Project name|`myproject`|
-| storageInputContainerName|`{CONTAINER-NAME}`|Container name|`mycontainer`|
-| `sentimentSpans` | | Array containing all the sentiments and their locations in the document. |  |
-| `documents` | | Array containing all the documents in your project and list of the entities labeled within each document. | [] |
-| `location` | `{DOCUMENT-NAME}` |  The location of the documents in the storage container. Since all the documents are in the root of the container this should be the document name.|`doc1.txt`|
-| `dataset` | `{DATASET}` |  The test set to which this file will go to when split before training. Learn more about data splitting [here](../how-to/train-model.md#data-splitting) . Possible values for this field are `Train` and `Test`.      |`Train`|
-| `offset` |  |  The inclusive character position of the start of a sentiment in the text.      |`0`|
-| `length` |  |  The length of the bounding box in terms of UTF16 characters. Training only considers the data in this region.      |`500`|
-| `category` |  |  The sentiment associated with the span of text specified. | `positive`|
-| `offset` |  |  The start position for the entity text. | `25`|
-| `length` |  |  The length of the entity in terms of UTF16 characters. | `20`|
-| `language` | `{LANGUAGE-CODE}` |  A string specifying the language code for the document used in your project. If your project is a multilingual project, choose the language code of the majority of the documents. See [Language support](../../language-support.md) for more information about supported language codes. |`en-us`|
-
-
-
-## Next steps
-* You can import your labeled data into your project directly. Learn how to [import project](../how-to/create-project.md#import-a-custom-sentiment-analysis-project)
-* See the [how-to article](../how-to/label-data.md)  more information about labeling your data. When you're done labeling your data, you can [train your model](../how-to/train-model.md).  
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム感情分析データフォーマットに関する文書の削除"
}
```

### Explanation
この変更では、カスタム感情分析データフォーマットに関する文書(`data-formats.md`)が完全に削除されました。具体的には、103行の情報がこのファイルから除外されました。

削除された内容には、カスタム感情分析で受け入れられるデータフォーマットについての詳細な説明が含まれており、特に、ラベルファイルの形式、必要なJSONの構造、そしてユーザーがデータをインポートするために必要な手順が記載されていました。また、各フィールドの意味や用途、例も与えられており、ユーザーがデータを準備するためのガイダンスが提供されていました。

この変更は、カスタム感情分析機能を使用するユーザーにとって重要な情報の喪失を意味します。特に、データのインポートやプロジェクトの設定が困難になる可能性が高く、利用者は他のリソースや文書を探し直す必要があります。したがって、この変更は、カスタム感情分析に関するワークフローやプロジェクト作成に影響を及ぼす可能性があり、新たに情報を学習する必要が出てくることも考えられます。

## articles/ai-services/language-service/sentiment-opinion-mining/custom/how-to/call-api.md{#item-54966c}

<details>
<summary>Diff</summary>
````diff
@@ -1,56 +0,0 @@
----
-title: Send a Custom sentiment analysis request to your custom model
-description: Learn how to send requests for Custom sentiment analysis.
-titleSuffix: Azure AI services
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.devlang: csharp
-# ms.devlang: csharp, python
-ms.custom: language-service-custom-ner
----
-
-# Send a Custom sentiment analysis request to your custom model
-
-After the deployment is added successfully, you can query the deployment to extract entities from your text based on the model you assigned to the deployment.
-You can query the deployment programmatically using the [Prediction API](/rest/api/language/text-analysis-runtime/analyze-text) or through the client libraries (Azure SDK). 
-
-## Test a deployed Custom sentiment analysis model
-
-You can use Language Studio to submit the custom entity recognition task and visualize the results. 
-
-[!INCLUDE [Test model](../../../includes/custom/language-studio/test-model.md)]
-
-<!--:::image type="content" source="../media/test-model-results.png" alt-text="View the test results" lightbox="../media/test-model-results.png":::--->
-
-
-## Send a sentiment analysis request to your model
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Get prediction URL](../../../includes/custom/language-studio/get-prediction-url.md)]
-
-# [REST API](#tab/rest-api)
-
-First you need to get your resource key and endpoint:
-
-[!INCLUDE [Get keys and endpoint Azure Portal](../../../includes/key-endpoint-page-azure-portal.md)]
-
-
-
-
-### Submit a Custom sentiment analysis task
-
-[!INCLUDE [submit a Custom sentiment analysis task using the REST API](../../includes/custom/rest-api/submit-task.md)]
-
-### Get task results
-
-[!INCLUDE [get Custom sentiment analysis task results](../../includes/custom/rest-api/get-results.md)]
-
-## Next steps
-
-* [Sentiment Analysis overview](../../overview.md)
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム感情分析API呼び出しに関する文書の削除"
}
```

### Explanation
この変更では、カスタム感情分析のリクエストを送信する方法に関する文書(`call-api.md`)が完全に削除されました。具体的には、56行の内容が削除されています。

削除された文書には、カスタムモデルへのリクエストの送信手順、デプロイされたカスタム感情分析モデルをテストする方法、特定のAPIやクライアントライブラリを使用した質問方法が含まれていました。また、リソースキーやエンドポイントの取得方法、カスタム感情分析タスクを送信する方法、タスク結果を取得する方法が詳細に説明されており、ユーザーが容易に機能を利用できるようになっていました。

この文書が削除されることは、カスタム感情分析機能を使用しているユーザーにとって重要な情報源が失われることを意味します。このため、ユーザーはAPIを利用したリクエストの送信方法やモデルのテスト方法について、再度情報を探し直す必要があります。したがって、この変更はカスタム感情分析のワークフローに影響を及ぼし、追加の学習リソースを見つける手間を生じるかもしれません。

## articles/ai-services/language-service/sentiment-opinion-mining/custom/how-to/create-project.md{#item-7699a8}

<details>
<summary>Diff</summary>
````diff
@@ -1,117 +0,0 @@
----
-title: How to create Custom sentiment analysis projects
-titleSuffix: Azure AI services
-description: Learn about the steps for using Azure resources with Custom sentiment analysis.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-classification, references_regions
----
-
-# How to create Custom sentiment analysis project
-
-Use this article to learn how to set up the requirements for starting with Custom sentiment analysis and create a project.
-
-## Prerequisites
-
-Before you start using Custom sentiment analysis, you'll need:
-
-* An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services).
-
-## Create a Language resource 
-
-Before you start using Custom sentiment analysis, you'll need an Azure Language resource. It's recommended to create your Language resource and connect a storage account to it in the Azure portal. Creating a resource in the Azure portal lets you create an Azure storage account at the same time, with all of the required permissions preconfigured. You can also read further in the article to learn how to use a pre-existing resource, and configure it to work with Custom sentiment analysis.
-
-You also need an Azure storage account where you'll upload your `.txt` documents that will be used to train a model to classify text.
-
-> [!NOTE]
->  * You need to have an **owner** role assigned on the resource group to create a Language resource.
->  * If you will connect a pre-existing storage account, you should have an **owner** role assigned to it.
-
-## Create Language resource and connect storage account
-
-
-> [!Note]
-> You shouldn't move the storage account to a different resource group or subscription once it's linked with the Language resource.
-
-[!INCLUDE [create a new resource from the Azure portal](../../../includes/custom/resource-creation-azure-portal.md)]
-
-[!INCLUDE [create a new resource from Language Studio](../../../includes/custom/resource-creation-language-studio.md)]
-
-[!INCLUDE [create a new resource with Azure PowerShell](../../../includes/custom/resource-creation-powershell.md)]
-
-
----
-
-> [!NOTE]
-> * The process of connecting a storage account to your Language resource is irreversible, it cannot be disconnected later.
-> * You can only connect your language resource to one storage account.
-
-## Using a pre-existing Language resource
-
-[!INCLUDE [use an existing resource](../../../includes/custom/use-pre-existing-resource.md)]
-
-
-## Create a Custom sentiment analysis project
-
-Once your resource and storage container are configured, create a new Custom sentiment analysis project. A project is a work area for building your custom AI models based on your data. Your project can only be accessed by you and others who have access to the Azure resource being used. If you have labeled data, you can [import it](#import-a-custom-sentiment-analysis-project) to get started.
-
-### [Language Studio](#tab/studio)
-
-[!INCLUDE [Language Studio project creation](../../../includes/custom/language-studio/create-project.md)]
-
-
-### [REST APIs](#tab/apis)
-
-[!INCLUDE [REST APIs project creation](../../includes/custom/rest-api/create-project.md)]
-
----
-
-## Import a Custom sentiment analysis project
-
-<!--If you have already labeled data, you can use it to get started with the service. Make sure that your labeled data follows the [accepted data formats](../concepts/data-formats.md).-->
-
-### [Language Studio](#tab/studio)
-
-[!INCLUDE [Import project](../../../includes/custom/language-studio/import-project.md)]
-
-### [REST APIs](#tab/apis)
-
-[!INCLUDE [Import project](../../includes/custom/rest-api/import-project.md)]
-
----
-
-## Get project details
-
-### [Language Studio](#tab/studio)
-
-[!INCLUDE [Language Studio project details](../../../includes/custom/language-studio/project-details.md)]
-
-### [REST APIs](#tab/apis)
-
-[!INCLUDE [REST API project details](../../includes/custom/rest-api/project-details.md)]
-
----
-
-## Delete project
-
-### [Language Studio](#tab/studio)
-
-[!INCLUDE [Delete project using Language Studio](../../../includes/custom/language-studio/delete-project.md)]
-
-### [REST APIs](#tab/apis)
-
-[!INCLUDE [Delete project using the REST API](../../includes/custom/rest-api/delete-project.md)]
-
----
-
-## Next steps
-
-* [Sentiment analysis overview](../../overview.md)
-<!--* You should have an idea of the [project schema](design-schema.md) you will use to label your data.
-
-* After your project is created, you can start [labeling your data](tag-data.md), which will inform your text classification model how to interpret text, and is used for training and evaluation.-->
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム感情分析プロジェクト作成に関する文書の削除"
}
```

### Explanation
この変更では、カスタム感情分析プロジェクトを作成するための手順を説明した文書(`create-project.md`)が完全に削除されました。具体的には、117行の内容が削除されています。

削除された文書には、カスタム感情分析を開始するために必要な要件やプロジェクト作成手順が含まれていました。これには、Azureサブスクリプションの作成、言語リソースの作成、ストレージアカウントの接続、およびカスタム感情分析プロジェクトの具体的な設定方法が説明されていました。また、事前に設定されたリソースを使用する方法や、Azure PortalやREST APIを通じてのプロジェクト作成手順も詳述されていました。

この文書の削除は、カスタム感情分析の利用者にとって重要な情報源の喪失を意味します。新たにプロジェクトを作成しようとするユーザーは、この手順を自力で学ぶ必要があり、作業の複雑さが増す可能性があります。したがって、この変更はカスタム感情分析の導入や管理に影響を及ぼし、利用者の作業効率を低下させる要因となるでしょう。

## articles/ai-services/language-service/sentiment-opinion-mining/custom/how-to/deploy-model.md{#item-435eeb}

<details>
<summary>Diff</summary>
````diff
@@ -1,104 +0,0 @@
----
-title: Deploy a Custom sentiment analysis model
-titleSuffix: Azure AI services
-description: Learn about deploying a model for Custom sentiment analysis.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-ta4h
----
-
-# Deploy a Custom sentiment analysis model
-
-Once you're satisfied with how your model performs, it's ready to be deployed and used to recognize entities in text. Deploying a model makes it available for use through the [prediction API](https://aka.ms/ct-runtime-swagger).
-
-## Prerequisites
-
-* A successfully [created project](create-project.md) with a configured Azure storage account.
-* Text data that has [been uploaded](design-schema.md#data-preparation) to your storage account.
-<!--* [Labeled data](label-data.md) and a successfully [trained model](train-model.md).
-* Reviewed the [model evaluation details](view-model-evaluation.md) to determine how your model is performing.
-
-For more information, see [project development lifecycle](../overview.md#project-development-lifecycle).-->
-
-## Deploy model
-
-After you've reviewed your model's performance and decided it can be used in your environment, you need to assign it to a deployment. Assigning the model to a deployment makes it available for use through the [prediction API](https://aka.ms/ct-runtime-swagger). It is recommended to create a deployment named *production* to which you assign the best model you have built so far and use it in your system. You can create another deployment called *staging* to which you can assign the model you're currently working on to be able to test it. You can have a maximum of 10 deployments in your project. 
-
-<!--# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Deploy a model using Language Studio](../../../includes/custom/language-studio/deploy-model.md)]
-   
-# [REST APIs](#tab/rest-api)
--->
-### Submit deployment job
-
-[!INCLUDE [deploy model](../../includes/custom/rest-api/deploy-model.md)]
-
-### Get deployment job status
-
-[!INCLUDE [get deployment status](../../includes/custom/rest-api/get-deployment-status.md)]
-
-## Swap deployments
-
-After you are done testing a model assigned to one deployment and you want to assign this model to another deployment you can swap these two deployments. Swapping deployments involves taking the model assigned to the first deployment, and assigning it to the second deployment. Then taking the model assigned to second deployment, and assigning it to the first deployment. You can use this process to swap your *production* and *staging* deployments when you want to take the model assigned to *staging* and assign it to *production*. 
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Swap deployments](../../../includes/custom/language-studio/swap-deployment.md)]
-
-# [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Swap deployments](../../includes/custom/rest-api/swap-deployment.md)]
-
----
-
-
-## Delete deployment
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Delete deployment](../../../includes/custom/language-studio/delete-deployment.md)]
-
-# [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Delete deployment](../../includes/custom/rest-api/delete-deployment.md)]
-
----
-
-## Assign deployment resources
-
-You can [deploy your project to multiple regions](../../../concepts/custom-features/multi-region-deployment.md) by assigning different Language resources that exist in different regions.
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Assign resource](../../../includes/custom/language-studio/assign-resources.md)]
-
-# [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Assign resource](../../includes/custom/rest-api/assign-resources.md)]
-
----
-
-## Unassign deployment resources
-
-When unassigning or removing a deployment resource from a project, you will also delete all the deployments that have been deployed to that resource's region.
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Unassign resource](../../../includes/custom/language-studio/unassign-resources.md)]
-
-# [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Unassign resource](../../includes/custom/rest-api/unassign-resources.md)]
-
----
-
-## Next steps
-
-* [Sentiment analysis overview](../../overview.md)
-<!--After you have a deployment, you can use it to [extract entities](call-api.md) from text.-->
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム感情分析モデルのデプロイに関する文書の削除"
}
```

### Explanation
この変更では、カスタム感情分析モデルのデプロイ方法を説明した文書(`deploy-model.md`)が完全に削除されました。具体的には、104行の内容が削除されています。

削除された文書には、モデルのデプロイ準備、デプロイメントの設定、モデルのパフォーマンスレビュー後にデプロイメントへのモデルの割り当てを行う方法など、デプロイに関する詳細な手順が含まれていました。また、デプロイメントの入れ替えや削除の手順、複数のリージョンにプロジェクトをデプロイする方法についても触れられていたため、ユーザーはAzure環境での効率的なモデル運用が可能でした。

この文書の削除により、カスタム感情分析モデルをデプロイする際のガイドラインが失われ、今後この機能を利用しようとするユーザーは、必要な情報を他のリソースから収集する必要があります。結果として、この変更はユーザーの作業の複雑さを増す要因となり、モデルのデプロイやメンテナンスにおける効率が低下する可能性があります。

## articles/ai-services/language-service/sentiment-opinion-mining/custom/how-to/design-schema.md{#item-f66944}

<details>
<summary>Diff</summary>
````diff
@@ -1,51 +0,0 @@
----
-title: How to prepare data and define a custom sentiment analysis schema
-titleSuffix: Azure AI services
-description: Learn about data selection and preparation for custom sentient analysis projects.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-classification
----
-
-# How to prepare data for custom sentiment analysis
-
-In order to create a Custom sentiment analysis model, you will need quality data to train it. This article covers how you should select and prepare your data, along with defining a schema. Defining the schema is the first step in the project development lifecycle, and it defines the classes that you need your model to classify your text into at runtime.
-
-## Data selection
-
-The quality of data you train your model with affects model performance greatly.
-
-* Use real-life data that reflects your domain's problem space to effectively train your model. You can use synthetic data to accelerate the initial model training process, but it will likely differ from your real-life data and make your model less effective when used.
-
-* Balance your data distribution as much as possible without deviating far from the distribution in real-life.
-
-* Use diverse data whenever possible to avoid overfitting your model. Less diversity in training data may lead to your model learning spurious correlations that may not exist in real-life data. 
- 
-* Avoid duplicate documents in your data. Duplicate data has a negative effect on the training process, model metrics, and model performance. 
-
-* Consider where your data comes from. If you are collecting data from one person, department, or part of your scenario, you are likely missing diversity that may be important for your model to learn about. 
-
-> [!NOTE]
-> If your documents are in multiple languages, select the **multiple languages** option during project creation and set the **language** option to the language of the majority of your documents.
-
-## Data preparation
-
-As a prerequisite for creating a Custom sentiment analysis project, your training data needs to be uploaded to a blob container in your storage account. You can create and upload training documents from Azure directly, or through using the Azure Storage Explorer tool. Using the Azure Storage Explorer tool allows you to upload more data quickly.  
-
-* [Create and upload documents from Azure](/azure/storage/blobs/storage-quickstart-blobs-portal#create-a-container)
-* [Create and upload documents using Azure Storage Explorer](/azure/vs-azure-tools-storage-explorer-blobs)
-
-You can only use `.txt`. documents for custom text. If your data is in other format, you can use [CLUtils parse command](https://github.com/microsoft/CognitiveServicesLanguageUtilities/blob/main/CustomTextAnalytics.CLUtils/Solution/CogSLanguageUtilities.ViewLayer.CliCommands/Commands/ParseCommand/README.md) to change your file format.
-
-## Test set
-
-When defining the testing set, make sure to include example documents that are not present in the training set. Defining the testing set is an important step to calculate the model performance<!--[model performance](view-model-evaluation.md#model-details)-->. Also, make sure that the testing set include documents that represent all classes used in your project.
-
-## Next steps
-
-If you haven't already, create a Custom sentiment analysis project. If it's your first time using Custom sentiment analysis, consider following the [quickstart](../quickstart.md) to create an example project. You can also see the [project requirements](../how-to/create-project.md) for more details on what you need to create a project.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム感情分析スキーマの定義に関する文書の削除"
}
```

### Explanation
この変更では、カスタム感情分析モデルのためのデータ準備とスキーマ定義に関する文書(`design-schema.md`)が完全に削除されました。具体的には、51行の内容が削除されています。

削除された文書には、カスタム感情分析モデルを構築するために必要なデータの選択と準備に関するガイドが含まれていました。このガイドでは、質の高いデータがモデルのパフォーマンスにどのように影響するか、データの収集方法や偏りのない分布を保つための戦略、重複データを避ける重要性について説明されていました。また、訓練データをストレージアカウントにアップロードする方法や、テストセットを定義する際の注意点も詳述され、プロジェクトの開発ライフサイクルにおける重要なステップが強調されていました。

この文書の削除により、カスタム感情分析プロジェクトを立ち上げるための基本的なデータ準備に関する情報が失われ、初めてこの分析機能を利用しようとするユーザーにとって重要なリソースが欠けることになります。その結果、新しくプロジェクトを開始する際の作業が煩雑化し、適切なデータ準備のプロセスを理解するのが難しくなる可能性があります。

## articles/ai-services/language-service/sentiment-opinion-mining/custom/how-to/label-data.md{#item-a91115}

<details>
<summary>Diff</summary>
````diff
@@ -1,75 +0,0 @@
----
-title: How to label your data for Custom sentiment analysis - Azure AI services
-titleSuffix: Azure AI services
-description: Learn about how to label your data for use with the custom Sentiment analysis.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-classification
----
-
-# Label text data for training your model for Custom sentiment analysis
-
-Before training your model you need to label your documents with the sentiments you want to categorize them into. This data will be used in the next step when training your model so that your model can learn from the labeled data. If you already have labeled data, you can directly [import](create-project.md) it into your project. Be sure that your data follows the [accepted data format](../concepts/data-formats.md).
-
-Before creating a Custom sentiment analysis model, you need to have labeled data first. If your data isn't labeled already, you can label it in the [Language Studio](https://aka.ms/languageStudio). Labeled data informs the model how to interpret text, and is used for training and evaluation.
-
-## Prerequisites
-
-Before you can label data, you need:
-
-* [A successfully created project](create-project.md) with a configured Azure blob storage account.
-* Documents containing text data that have [been uploaded](design-schema.md#data-preparation) to your storage account.
-
-See the [project development lifecycle](../../overview.md#project-development-lifecycle) for more information.
-
-## Data labeling guidelines
-
-After [preparing your data](design-schema.md) and [creating your project](create-project.md), you will need to label your data. Labeling your data is important so your model knows which documents will be associated with the sentiments you need. When you label your data in [Language Studio](https://aka.ms/languageStudio) (or import labeled data), these labels will be stored in the JSON file in your storage container that you've connected to this project. 
-
-As you label your data, keep in mind:
-
-* In general, more labeled data leads to better results, provided the data is labeled accurately.
-
-* There is no fixed number of labels that can guarantee your model will perform the best. Model performance on possible ambiguity in your [data](design-schema.md), and the quality of your labeled data.
-
-## Label your data
-
-Use the following steps to label your data:
-
-1. Go to your project page in [Language Studio](https://aka.ms/languageStudio).
-
-2. From the left side menu, select **Data labeling**. You can find a list of all documents in your storage container.
-
-    >[!TIP]
-    > You can use the filters in top menu to view the unlabeled files so that you can start labeling them.
-    > You can also use the filters to view the documents that are labeled with a specific sentiment.
-
-3. Change to a single file view from the left side in the top menu or select a specific file to start labeling. You can find a list of all `.txt` files available in your projects to the left. You can use the **Back** and **Next** button from the bottom of the page to navigate through your documents.
-
-    > [!NOTE]
-    > If you enabled multiple languages for your project, you will find a **Language** dropdown in the top menu, which lets you select the language of each document.
-
-
-4. In the right side pane, you can add sentiments to your project to start labeling your data with them. <!--You can also use the [auto labeling feature](use-autolabeling.md) to ensure complete labeling.-->
-
-6. In the right side pane under the **Labels** pivot you can find all the sentiments in your project and the count of labeled instances for each.
-
-7. In the bottom section of the right side pane you can add the current file you are viewing to the training set or the testing set. By default all the documents are added to your training set. Learn more about [training and testing sets](train-model.md#data-splitting) and how they are used for model training and evaluation.
-
-    > [!TIP]
-    > If you are planning on using **Automatic** data splitting use the default option of assigning all the documents into your training set.
-
-8. Under the **Distribution** pivot you can view the distribution across training and testing sets. You have two options for viewing:
-   * *Total instances* where you can view count of all labeled instances of a specific sentiment.
-   * *Documents with at least one label* where each document is counted if it contains at least one labeled instance of this sentiment.
-
-9. While you're labeling, your changes will be synced periodically, if they have not been saved yet you will find a warning at the top of your page. If you want to save manually, click on **Save labels** button at the bottom of the page.
-
-## Next steps
-
-After you've labeled your data, you can begin [training a model](train-model.md) that will learn based on your data.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム感情分析のためのデータラベリングに関する文書の削除"
}
```

### Explanation
この変更では、カスタム感情分析用のデータラベリング方法に関する文書(`label-data.md`)が完全に削除されました。具体的には、75行の内容が削除されています。

削除された文書には、モデルを訓練するために必要なテキストデータのラベリング手順が詳細に説明されていました。ラベリングは、モデルがどのようにテキストを解釈するかを学ぶために必要な重要なステップであり、この文書ではラベリングに伴う前提条件や具体的なガイドライン、手順が含まれていました。特に、ラベリングの際のデータの選択、正確なラベル付けの重要性、ラベルを使用したデータのインポート方法などが詳述されていました。

この文書が削除されることにより、カスタム感情分析プロジェクトを進めるユーザーは、データラベリングのプロセスに関する重要な情報を失い、タスクの進行が妨げられる可能性があります。特に、初めてプロジェクトを立ち上げるユーザーにとっては、適切なラベリング手法を理解するのが難しくなり、モデルのパフォーマンスに悪影響を及ぼす恐れがあります。結果として、この変更はユーザーのエクスペリエンスを大きく損なうこととなります。

## articles/ai-services/language-service/sentiment-opinion-mining/custom/how-to/train-model.md{#item-2b8047}

<details>
<summary>Diff</summary>
````diff
@@ -1,86 +0,0 @@
----
-title: How to train your Custom sentiment analysis model - Azure AI services
-titleSuffix: Azure AI services
-description: Learn about how to train your model for Custom sentiment analysis.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: how-to
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-custom-classification
----
-
-# How to train a Custom sentiment analysis model
-
-<!--Training is the process where the model learns from your [labeled data](label-data.md). After training is completed, you'll be able to [view the model's performance](view-model-evaluation.md) to determine if you need to improve your model.-->
-
-To train a model, start a training job. Only successfully completed jobs create a usable model. Training jobs expire after seven days. After this period, you won't be able to retrieve the job details. If your training job completed successfully and a model was created, it won't be affected by the job expiration. You can only have one training job running at a time, and you can't start other jobs in the same project. 
-
-The training times can be anywhere from a few minutes when dealing with few documents, up to several hours depending on the dataset size and the complexity of your schema.
-
-
-
-## Prerequisites
-
-Before you train your model, you need:
-
-* [A successfully created project](create-project.md) with a configured Azure blob storage account.
-<!--* Text data that has [been uploaded](design-schema.md#data-preparation) to your storage account.
-* [Labeled data](label-data.md).
-
-See the [project development lifecycle](../../overview.md#project-development-lifecycle) for more information.-->
-
-## Data splitting
-
-Before you start the training process, labeled documents in your project are divided into a training set and a testing set. Each one of them serves a different function.
-The **training set** is used in training the model, this is the set from which the model learns the class/classes assigned to each document. 
-The **testing set** is a blind set that is not introduced to the model during training but only during evaluation. 
-After the model is trained successfully, it is used to make predictions from the documents in the testing set. Based on these predictions, the model's evaluation metrics will be calculated. 
-It is recommended to make sure that all your classes are adequately represented in both the training and testing set.
-
-Custom sentiment analysis supports two methods for data splitting:
-
-* **Automatically splitting the testing set from training data**: The system will split your labeled data between the training and testing sets, according to the percentages you choose. The system attempts to have a representation of all classes in your training set. The recommended percentage split is 80% for training and 20% for testing. 
-
- > [!NOTE]
- > If you choose the **Automatically splitting the testing set from training data** option, only the data assigned to training set will be split according to the percentages provided.
-
-* **Use a manual split of training and testing data**: This method enables users to define which labeled documents should belong to which set. <!--This step is only enabled if you have added documents to your testing set during [data labeling](tag-data.md).-->
-
-## Train model
-
-# [Language studio](#tab/Language-studio)
-
-[!INCLUDE [Train model](../../../includes/custom/language-studio/train-your-model.md)]
-
-# [REST APIs](#tab/REST-APIs)
-
-### Start training job
-
-[!INCLUDE [train model](../../includes/custom/rest-api/train-model.md)]
-
-### Get training job status
-
-Training could take sometime depending on the size of your training data and complexity of your schema. You can use the following request to keep polling the status of the training job until it is successfully completed.
-
- [!INCLUDE [get training model status](../../includes/custom/rest-api/get-training-status.md)]
-
----
-
-### Cancel training job
-
-# [Language Studio](#tab/language-studio)
-
-[!INCLUDE [Cancel training](../../../includes/custom/language-studio/cancel-training.md)]
-
-# [REST APIs](#tab/rest-api)
-
-[!INCLUDE [Cancel training](../../includes/custom/rest-api/cancel-training.md)]
-
----
-
-## Next steps
-
-After training is completed, you will be able to view the model's performance to optionally improve your model if needed. Once you're satisfied with your model, you can deploy it, making it available to use for use.
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム感情分析モデルの訓練に関する文書の削除"
}
```

### Explanation
この変更では、カスタム感情分析モデルを訓練する方法に関する文書(`train-model.md`)が完全に削除されました。具体的には、86行の内容が削除されています。

削除された文書には、モデルの訓練プロセスに関する重要な情報が含まれていました。具体的には、訓練ジョブの開始方法、データの分割方法、訓練に必要な要件、訓練が成功した後のモデルの評価方法について説明されていました。また、訓練の際に考慮すべき点や、手動または自動でデータをトレーニングセットやテストセットに分割する方法が詳細に示されていました。

この文書の削除によって、カスタム感情分析プロジェクトを進めるユーザーは、モデルの訓練に必要な手続きや重要な注意点についての情報が失われることになります。特に初心者にとって、適切な訓練手法を理解するのが難しくなり、モデルの品質やパフォーマンスに悪影響を及ぼす可能性があります。その結果、ユーザーエクスペリエンスが大きく損なわれ、プロジェクトの進行が困難になるリスクがあります。

## articles/ai-services/language-service/sentiment-opinion-mining/custom/quickstart.md{#item-32972e}

<details>
<summary>Diff</summary>
````diff
@@ -1,45 +0,0 @@
----
-title: Quickstart - Custom sentiment analysis
-titleSuffix: Azure AI services
-description: Quickly start building an AI model to identify the sentiment of text.
-#services: cognitive-services
-author: jboback
-manager: nitinme
-ms.service: azure-ai-language
-ms.topic: quickstart
-ms.date: 11/21/2024
-ms.author: jboback
-ms.custom: language-service-sentiment-opinion-mining
-zone_pivot_groups: usage-custom-language-features
----
-
-# Quickstart: Custom sentiment analysis (preview)
-
-> [NOTE]
-> Custom sentiment analysis (preview) will be retired on 10 January 2025, please transition to other custom model training services, such as custom text classification in Azure AI Language, by that date. From now to 10 January 2025, you can continue to use custom sentiment analysis (preview) in your existing projects without disruption. You can’t create new projects. On 10 January 2025 – workloads running on custom sentiment analysis (preview) will be deleted and associated project data will be lost. 
-
-Use this article to get started with creating a Custom sentiment analysis project where you can train custom models for detecting the sentiment of text. A model is artificial intelligence software that's trained to do a certain task. For this system, the models classify text, and are trained by learning from tagged data.
-
-::: zone pivot="language-studio"
-
-[!INCLUDE [Language Studio quickstart](../includes/custom/quickstarts/language-studio.md)]
-
-::: zone-end
-
-::: zone pivot="rest-api"
-
-[!INCLUDE [REST API quickstart](../includes/custom/quickstarts/rest-api.md)]
-
-::: zone-end
-
-## Next steps
-
-After you've created a Custom sentiment analysis model, you can:
-* [Use the runtime API to classify text](how-to/call-api.md)
-
-When you start to create your own Custom sentiment analysis projects, use the how-to articles to learn more about developing your model in greater detail:
-
-* [Data selection](how-to/design-schema.md)
-* [Tag data](how-to/label-data.md)
-* [Train a model](how-to/train-model.md)
-<!--* [View the model's evaluation](how-to/view-model-evaluation.md)-->
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カスタム感情分析のクイックスタート文書の削除"
}
```

### Explanation
この変更では、カスタム感情分析に関するクイックスタート文書(`quickstart.md`)が完全に削除されました。具体的には、45行の内容が削除されています。

削除された文書には、カスタム感情分析プロジェクトを迅速に開始するための手順や説明が含まれていました。特に、カスタム感情分析が2025年1月10日に退役することに関する重要な警告や、プロジェクトの作成と使用についてのガイダンスが記載されていました。また、言語スタジオやREST APIを使用したクイックスタートのリンクも含まれており、ユーザーがモデルを作成するための具体的な手順を示していました。

この文書の削除により、カスタム感情分析モデルの立ち上げに関する基本的な情報が失われ、特に新たにプロジェクトを始めようとしているユーザーにとっての障壁が高くなる可能性があります。ユーザーは適切な手順を知らないままプロジェクトを進めることになり、結果的に適切なモデル構築ができないリスクが高まります。これは、ユーザーエクスペリエンスの低下をもたらす重大な変更となるでしょう。

## articles/ai-services/language-service/sentiment-opinion-mining/overview.md{#item-831fe6}

<details>
<summary>Diff</summary>
````diff
@@ -16,17 +16,15 @@ ms.custom: language-service-sentiment-opinion-mining
 
 Sentiment analysis and opinion mining are features offered by [the Language service](../overview.md), a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. These features help you find out what people think of your brand or topic by mining text for clues about positive or negative sentiment, and can associate them with specific aspects of the text. 
 
-Both sentiment analysis and opinion mining work with a variety of [written languages](./language-support.md).
+Both sentiment analysis and opinion mining work with various [written languages](./language-support.md).
 
 ## Sentiment analysis 
 
-The sentiment analysis feature provides sentiment labels (such as "negative", "neutral" and "positive") based on the highest confidence score found by the service at a sentence and document-level. This feature also returns confidence scores between 0 and 1 for each document & sentences within it for positive, neutral and negative sentiment. 
+The sentiment analysis feature provides sentiment labels (such as "negative", "neutral" and "positive") based on the highest confidence score found by the service at a sentence and document-level. This feature also returns confidence scores between 0 and 1 for each document & sentences within it for positive, neutral, and negative sentiment. 
 
 ## Opinion mining
 
-Opinion mining is a feature of sentiment analysis. Also known as aspect-based sentiment analysis in Natural Language Processing (NLP), this feature provides more granular information about the opinions related to words (such as the attributes of products or services) in text.
-
-#### [Prebuilt model](#tab/prebuilt)
+Opinion mining is a feature of sentiment analysis, also known as aspect-based sentiment analysis in Natural Language Processing (NLP). This feature provides more granular information about the opinions related to words (such as the attributes of products or services) in text.
 
 [!INCLUDE [Typical workflow for pre-configured language features](../includes/overview-typical-workflow.md)]
 
@@ -36,43 +34,9 @@ Opinion mining is a feature of sentiment analysis. Also known as aspect-based se
 
 [!INCLUDE [Developer reference](../includes/reference-samples-text-analytics.md)] 
 
-#### [Custom model (preview)](#tab/custom)
-
-Custom sentiment analysis enables users to build custom AI models to classify text into sentiments pre-defined by the user. By creating a Custom sentiment analysis project, developers can iteratively label data, train, evaluate, and improve model performance before making it available for consumption. The quality of the labeled data greatly impacts model performance. To simplify building and customizing your model, the service offers a custom web portal that can be accessed through the [Language studio](https://aka.ms/languageStudio). You can easily get started with the service by following the steps in this [quickstart](quickstart.md). 
-
-
-## Project development lifecycle
-
-Creating a Custom sentiment analysis project typically involves several different steps. 
-
-:::image type="content" source="media/development-lifecycle.png" alt-text="Diagram of the development lifecycle" lightbox="media/development-lifecycle.png":::
-
-Follow these steps to get the most out of your model:
-
-1. **Define your schema**: Know your data and identify the sentiments you want, to avoid ambiguity.
-
-2. **Label your data**: The quality of data labeling is a key factor in determining model performance. Avoid ambiguity, make sure that your sentiments are clearly separable from each other.
-
-3. **Train the model**: Your model starts learning from your labeled data.
-
-4. **View the model's performance**: View the evaluation details for your model to determine how well it performs when introduced to new data.
-
-5. **Deploy the model**: Deploying a model makes it available for use via the [Analyze API](https://aka.ms/ct-runtime-swagger).
-
-6. **Classify text**: Use your custom model for sentiment analysis tasks.
-
-## Development options
-
-|Development option  |Description  |
-|---------|---------|
-|Language studio     | Language Studio is a web-based platform that lets you try entity linking with text examples without an Azure account, and your own data when you sign up.       |
-|REST API     | Integrate sentiment analysis into your applications programmatically using the REST API.    |
-
-For more information, see [sentiment analysis quickstart](./custom/quickstart.md).   
-
 ## Reference documentation
 
-As you use Custom sentiment analysis, see the following reference documentation and samples for the Language service:
+As you use sentiment analysis, see the following reference documentation and samples for the Language service:
 
 |Development option / language  |Reference documentation |Samples  |
 |---------|---------|---------|
@@ -81,13 +45,11 @@ As you use Custom sentiment analysis, see the following reference documentation
 
 --- 
 
-
 ## Responsible AI 
 
-An AI system includes not only the technology, but also the people who use it, the people who will be affected by it, and the environment in which it's deployed. Read the [transparency note for sentiment analysis](/legal/cognitive-services/language-service/transparency-note-sentiment-analysis?context=/azure/ai-services/language-service/context/context) to learn about responsible AI use and deployment in your systems. You can also see the following articles for more information:
+An AI system includes not only the technology, but also the people who use it, the people who are affected by it, and the environment in which it's deployed. Read the [transparency note for sentiment analysis](/legal/cognitive-services/language-service/transparency-note-sentiment-analysis?context=/azure/ai-services/language-service/context/context) to learn about responsible AI use and deployment in your systems. You can also see the following articles for more information:
 
 ## Next steps
 
 * The quickstart articles with instructions on using the service for the first time.
-    * [Use the prebuilt model](./quickstart.md)
-    * [Create a custom model](./custom/quickstart.md)  
+    * [Use sentiment analysis and opinion mining](./quickstart.md)
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "感情分析と意見マイニングの概要文書の更新"
}
```

### Explanation
この変更では、感情分析と意見マイニングに関する概要文書(`overview.md`)が修正され、44行が削除され、6行が追加されました。文書は、感情分析と意見マイニングの機能についての情報を提供しています。

主な変更点は、以下の通りです：

1. **文章の明確化**: 「さまざまな言語」というフレーズが「多様な言語」に変更され、文の流れが改善されています。
2. **センテンスのコンマ**: センテンスの最後におけるコンマの使用に一貫性が持たされ、可読性が向上しました。
3. **カスタムモデルに関するセクションの削除**: カスタム感情分析に関する詳細な説明やプロジェクト開発ライフサイクル、開発オプションの部分が削除され、より簡潔な形式となりました。これにより、文書がより短く、必要な情報がすっきりと整理されています。
4. **責任あるAIに関するセクションの簡略化**: AIシステムに関する説明が要約され、重要な情報を維持しつつ、冗長性が削減されました。

これらの修正により、文書はより直感的で、特に新規ユーザーが感情分析と意見マイニングの主な機能や導入方法を把握しやすくなっています。全体として、情報が整理され、誤解を招く可能性のある部分が改善されたため、ユーザーエクスペリエンスの向上に寄与しています。

## articles/ai-services/language-service/toc.yml{#item-12f1f0}

<details>
<summary>Diff</summary>
````diff
@@ -555,116 +555,15 @@ items:
     items:
       - name: Sentiment analysis and opinion mining overview
         href: sentiment-opinion-mining/overview.md
+      - name: Sentiment analysis and opinion mining quickstart
+        href: sentiment-opinion-mining/quickstart.md
       - name: Sentiment analysis and opinion mining language support
         href: sentiment-opinion-mining/language-support.md
-      - name: Prebuilt
-        items:
-        - name: Sentiment analysis and opinion mining quickstart
-          href: sentiment-opinion-mining/quickstart.md
-        - name: Responsible use of AI
-          items:
-          - name: Transparency note for sentiment analysis and opinion mining
-            href: /legal/cognitive-services/language-service/transparency-note-sentiment-analysis?context=/azure/ai-services/language-service/context/context
-            displayName: Transparency note for sentiment analysis, opinion mining transparency, Responsible AI, Responsible use of AI
-          - name: Integration and responsible use
-            href: /legal/cognitive-services/language-service/guidance-integration-responsible-use?context=/azure/ai-services/language-service/context/context
-            displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
-          - name: Data, privacy, and security
-            href: /legal/cognitive-services/language-service/data-privacy?context=/azure/ai-services/language-service/context/context
-            displayName: Data privacy, logging, data retention
-        - name: How-to guides
-          items:
-          - name: Call Sentiment Analysis and Opinion Mining
-            href: sentiment-opinion-mining/how-to/call-api.md
-          - name: Use containers
-            items:
-            - name: Use Docker Containers
-              href: sentiment-opinion-mining/how-to/use-containers.md
-            - name: Configure containers
-              href: concepts/configure-containers.md
-            - name: Use container instances
-              href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
-            - name: Use containers in disconnected environments
-              href: ../containers/disconnected-containers.md
-            - name: Azure AI containers overview
-              href: ../cognitive-services-container-support.md
-        - name: Tutorials
-          items:
-          - name: Use Flask to translate text, analyze sentiment, and synthesize speech
-            href: /training/modules/python-flask-build-ai-web-app/
-        - name: Reference
-          items:
-          - name: REST API
-            items:
-              - name: Text analysis runtime API (v2023-04-01)
-                href: https://go.microsoft.com/fwlink/?linkid=2239169
-              - name: Text analysis runtime API (v2022-04-15-preview)
-                href: /rest/api/language/2023-04-15-preview/text-analysis-runtime
-              - name: Previous versions
-                items:
-                - name: v3.2-preview.2
-                  href: https://westus2.dev.cognitive.microsoft.com/docs/services/TextAnalytics-v3-2-Preview-2/operations/Sentiment
-                - name: v3.1
-                  href: https://westus2.dev.cognitive.microsoft.com/docs/services/TextAnalytics-v3-1/operations/Sentiment
-          - name: SDKs
-            items:
-            - name: Latest
-              items:
-                - name: .NET
-                  href: /dotnet/api/azure.ai.textanalytics?view=azure-dotnet&preserve-view=true
-                - name: Python
-                  href: /python/api/overview/azure/ai-textanalytics-readme?view=azure-python&preserve-view=true
-                - name: Java
-                  href: /java/api/overview/azure/ai-textanalytics-readme?view=azure-java-stable&preserve-view=true
-                - name: Node.js
-                  href: /javascript/api/overview/azure/ai-language-text-readme?view=azure-node-latest&preserve-view=true
-            - name: Preview
-              items:
-                - name: .NET
-                  href: /dotnet/api/azure.ai.textanalytics?view=azure-dotnet-preview&preserve-view=true
-                - name: Python
-                  href: /python/api/azure-ai-textanalytics/azure.ai.textanalytics?view=azure-python-preview&preserve-view=true
-                - name: Java
-                  href: /java/api/overview/azure/ai-textanalytics-readme?view=azure-java-preview&preserve-view=true
-                - name: Node.js
-                  href: /javascript/api/overview/azure/ai-language-text-readme?view=azure-node-preview&preserve-view=true
-      - name: Custom (preview)
-        items:
-          - name: Quickstart
-            href: sentiment-opinion-mining/custom/quickstart.md
-          - name: Concepts
-            items:
-              - name: Data formats
-                href: sentiment-opinion-mining/custom/concepts/data-formats.md
-          - name: How-to guides
-            items:
-              - name: Data preparation
-                href: sentiment-opinion-mining/custom/how-to/design-schema.md
-              - name: Label data
-                href: sentiment-opinion-mining/custom/how-to/label-data.md
-              - name: Create projects
-                href: sentiment-opinion-mining/custom/how-to/create-project.md
-              - name: Train model
-                href: sentiment-opinion-mining/custom/how-to/train-model.md
-              - name: Deploy model
-                href: sentiment-opinion-mining/custom/how-to/deploy-model.md
-              - name: Call the API
-                href: sentiment-opinion-mining/custom/how-to/call-api.md
-  - name: Text Analytics for health
-    items:
-    - name: Text Analytics for health overview
-      href: text-analytics-for-health/overview.md
-    - name: Text Analytics for health quickstart
-      href: text-analytics-for-health/quickstart.md
-    - name: Text Analytics for health language support
-      href: text-analytics-for-health/language-support.md
-    - name: Prebuilt
-      items:
       - name: Responsible use of AI
         items:
-        - name: Transparency note for Text Analytics for health
-          href: /legal/cognitive-services/language-service/transparency-note-health?context=/azure/ai-services/language-service/context/context
-          displayName: Transparency note for Text Analytics health, Text Analytics for health transparency, Responsible AI, Responsible use of AI
+        - name: Transparency note for sentiment analysis and opinion mining
+          href: /legal/cognitive-services/language-service/transparency-note-sentiment-analysis?context=/azure/ai-services/language-service/context/context
+          displayName: Transparency note for sentiment analysis, opinion mining transparency, Responsible AI, Responsible use of AI
         - name: Integration and responsible use
           href: /legal/cognitive-services/language-service/guidance-integration-responsible-use?context=/azure/ai-services/language-service/context/context
           displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
@@ -673,66 +572,67 @@ items:
           displayName: Data privacy, logging, data retention
       - name: How-to guides
         items:
-        - name: How to call the API
-          href: text-analytics-for-health/how-to/call-api.md
+        - name: Call Sentiment Analysis and Opinion Mining
+          href: sentiment-opinion-mining/how-to/call-api.md
         - name: Use containers
           items:
-          - name: Use Docker containers
-            href: text-analytics-for-health/how-to/use-containers.md
-          - name: Configure Docker containers
-            href: text-analytics-for-health/how-to/configure-containers.md
+          - name: Use Docker Containers
+            href: sentiment-opinion-mining/how-to/use-containers.md
+          - name: Configure containers
+            href: concepts/configure-containers.md
           - name: Use container instances
             href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
+          - name: Use containers in disconnected environments
+            href: ../containers/disconnected-containers.md
           - name: Azure AI containers overview
             href: ../cognitive-services-container-support.md
-      - name: Concepts
-        items:
-        - name: Recognized entity categories
-          href: text-analytics-for-health/concepts/health-entity-categories.md
-        - name: Relation extraction
-          href: text-analytics-for-health/concepts/relation-extraction.md
-        - name: Assertion detection
-          href: text-analytics-for-health/concepts/assertion-detection.md
-        - name: Fast Healthcare Interoperability Resources (FHIR) structuring
-          href: text-analytics-for-health/concepts/fhir.md
-    - name: Custom (preview)
-      items:
-      - name: Custom text analytics for health overview
-        href: custom-text-analytics-for-health/overview.md
-      - name: Custom text analytics for health quickstart
-        href: custom-text-analytics-for-health/quickstart.md
-      - name: Custom text analytics for health language support
-        href: custom-text-analytics-for-health/language-support.md
-      - name: How-to guides
-        items:
-        - name: Create projects
-          href: custom-text-analytics-for-health/how-to/create-project.md
-        - name: Data selection and schema design
-          href: custom-text-analytics-for-health/how-to/design-schema.md
-        - name: Label data
-          href: custom-text-analytics-for-health/how-to/label-data.md
-        - name: Train a model
-          href: custom-text-analytics-for-health/how-to/train-model.md
-        - name: View your model's evaluation
-          href: custom-text-analytics-for-health/how-to/view-model-evaluation.md
-        - name: Deploy a model
-          href: custom-text-analytics-for-health/how-to/deploy-model.md
-        - name: Call the API
-          href: custom-text-analytics-for-health/how-to/call-api.md
-        - name: Back up and recover your models
-          href: custom-text-analytics-for-health/how-to/fail-over.md
-      - name: Concepts
+      - name: Tutorials
         items:
-        - name: Data formats
-          href: custom-text-analytics-for-health/concepts/data-formats.md
-        - name: Entity components
-          href: custom-text-analytics-for-health/concepts/entity-components.md
-        - name: Evaluation metrics
-          href: custom-text-analytics-for-health/concepts/evaluation-metrics.md
-      - name: Reference
+        - name: Use Flask to translate text, analyze sentiment, and synthesize speech
+          href: /training/modules/python-flask-build-ai-web-app/
+  - name: Text Analytics for health
+    items:
+    - name: Text Analytics for health overview
+      href: text-analytics-for-health/overview.md
+    - name: Text Analytics for health quickstart
+      href: text-analytics-for-health/quickstart.md
+    - name: Text Analytics for health language support
+      href: text-analytics-for-health/language-support.md
+    - name: Responsible use of AI
+      items:
+      - name: Transparency note for Text Analytics for health
+        href: /legal/cognitive-services/language-service/transparency-note-health?context=/azure/ai-services/language-service/context/context
+        displayName: Transparency note for Text Analytics health, Text Analytics for health transparency, Responsible AI, Responsible use of AI
+      - name: Integration and responsible use
+        href: /legal/cognitive-services/language-service/guidance-integration-responsible-use?context=/azure/ai-services/language-service/context/context
+        displayName: Responsible deployment, Responsible use, Responsible integration, AI deployment, AI use
+      - name: Data, privacy, and security
+        href: /legal/cognitive-services/language-service/data-privacy?context=/azure/ai-services/language-service/context/context
+        displayName: Data privacy, logging, data retention
+    - name: How-to guides
+      items:
+      - name: How to call the API
+        href: text-analytics-for-health/how-to/call-api.md
+      - name: Use containers
         items:
-        - name: Service limits
-          href: custom-text-analytics-for-health/reference/service-limits.md
+        - name: Use Docker containers
+          href: text-analytics-for-health/how-to/use-containers.md
+        - name: Configure Docker containers
+          href: text-analytics-for-health/how-to/configure-containers.md
+        - name: Use container instances
+          href: ../containers/azure-container-instance-recipe.md?context=/azure/ai-services/language-service/context/context
+        - name: Azure AI containers overview
+          href: ../cognitive-services-container-support.md
+    - name: Concepts
+      items:
+      - name: Recognized entity categories
+        href: text-analytics-for-health/concepts/health-entity-categories.md
+      - name: Relation extraction
+        href: text-analytics-for-health/concepts/relation-extraction.md
+      - name: Assertion detection
+        href: text-analytics-for-health/concepts/assertion-detection.md
+      - name: Fast Healthcare Interoperability Resources (FHIR) structuring
+        href: text-analytics-for-health/concepts/fhir.md
   - name: Summarization
     items:
     - name: Summarization overview
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "感情分析および意見マイニングのTOCの更新"
}
```

### Explanation
この変更では、感情分析および意見マイニングに関連する目次（`toc.yml`）が修正され、158行が削除され、58行が追加されました。全体として、216行の変更が行われました。具体的には、次のような内容が含まれています：

1. **新たなクイックスタートリンクの追加**: 目次に「感情分析および意見マイニングのクイックスタート」というセクションが新たに追加されました。これにより、ユーザーはこの機能を迅速に始めるための情報にアクセスしやすくなります。

2. **不要なセクションの削除**: 以前は目次に含まれていた多くのサブセクション（例: プリビルトモデルに関する詳細やカスタムモデルの手順）が削除され、情報が簡潔になりました。これにより、ユーザーがより必要な情報に集中できるようになっています。

3. **責任あるAIに関する情報の整理**: 「透明性ノート」や「統合と責任ある使用」などのリファレンスに関するリンクが整頓され、関連する情報が一箇所にまとめられました。

4. **コンテナに関するセクションの新しいリンク**: Dockerコンテナや関連する設定に関する新しい情報へのリンクが明確に整理され、開発者が必要な手続きを確認しやすくなった。

この更新により、感情分析と意見マイニングに関連するリソースへのアクセスが改善され、ユーザーが必要な情報を効率的に見つけられるようになっています。また、不要な情報が削除されることで、目次はより清潔で役立つものとなりました。

## articles/ai-services/language-service/tutorials/prompt-flow.md{#item-22c24b}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: jboback
 ms.author: jboback
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 07/09/2024
+ms.date: 01/31/2025
 ---
 
 # Use Language in Azure prompt flow
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトフローに関するチュートリアルの日付の更新"
}
```

### Explanation
この変更では、プロンプトフローに関するチュートリアル（`prompt-flow.md`）のメタデータの日付が修正され、07/09/2024から01/31/2025に変更されました。この修正は、文書が最新の情報や機能に基づいていることを反映するために重要です。

具体的には、以下の点が含まれています：

1. **日付の更新**: チュートリアルが説明している内容が将来的に有効であることを示すために、関連する日付が変更されました。これは、ユーザーにとって、最新の内容に基づいたガイダンスを受け取っていることを示すものです。

この小さな変更は、文書の正確性と信頼性を向上させるものであり、ユーザーが最新の情報をもとに行動できるようサポートしています。

## articles/ai-studio/how-to/prompt-flow-tools/serp-api-tool.md{#item-144ed7}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom:
   - ignite-2023
   - build-2024
 ms.topic: how-to
-ms.date: 5/21/2024
+ms.date: 01/31/2025
 ms.reviewer: keli19
 ms.author: lagayhar
 author: lgayhardt
@@ -29,15 +29,12 @@ Sign up on the [Serp API home page](https://serpapi.com/).
 To create a Serp connection:
 
 1. Sign in to [Azure AI Foundry](https://ml.azure.com/).
-1. Go to **Project settings** > **Connections**.
-1. Select **+ New connection**.
-1. Add the following custom keys to the connection:
+1. Go to project settings by selecting  **Management Center** > **Overview**
+1. Under *Connected resources*, select **+ New connection**.
+1. Under *Other resource types*, select **Serp**.
+1. Add your API key for Serp and make a connection name. Then select **Add connection**.
 
-    - `azureml.flow.connection_type`: `Custom`
-    - `azureml.flow.module`: `promptflow.connections`
-    - `api_key`: Your Serp API key. You must select the **is secret** checkbox to keep the API key secure.
-    
-    :::image type="content" source="../../media/prompt-flow/serp-custom-connection-keys.png" alt-text="Screenshot that shows adding extra information to a custom connection in Azure AI Foundry portal." lightbox = "../../media/prompt-flow/serp-custom-connection-keys.png":::
+    :::image type="content" source="../../media/prompt-flow/serp-connection-keys.png" alt-text="Screenshot that shows adding Serp connection in Azure AI Foundry portal." lightbox = "../../media/prompt-flow/serp-connection-keys.png":::
 
 The connection is the model used to establish connections with the Serp API. Get your API key from the Serp API account dashboard.
 
@@ -52,7 +49,7 @@ The connection is the model used to establish connections with the Serp API. Get
 
     :::image type="content" source="../../media/prompt-flow/serp-api-tool.png" alt-text="Screenshot that shows the Serp API tool added to a flow in Azure AI Foundry portal." lightbox="../../media/prompt-flow/serp-api-tool.png":::
 
-1. Select the connection to one of your provisioned resources. For example, select **SerpConnection** if you created a connection with that name. For more information, see [Prerequisites](#prerequisites).
+1. Select the connection to one of your provisioned resources. For example, select "Serp Connection" if you created a connection with that name. For more information, see [Prerequisites](#prerequisites).
 1. Enter values for the Serp API tool input parameters described in the [Inputs table](#inputs).
 1. Add more tools to your flow, as needed. Or select **Run** to run the flow.
 1. The outputs are described in the [Outputs table](#outputs).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Serp APIツールに関するドキュメントの更新"
}
```

### Explanation
この変更では、Serp APIツールに関するドキュメント（`serp-api-tool.md`）に対して、軽微な修正が加えられました。内容の更新に伴い、7行が追加され、10行が削除され、合計17行の変更が行われました。

具体的な変更点は以下の通りです：

1. **日付の更新**: 文書のメタデータにおける日付が変更され、2024年5月21日から2025年1月31日に更新されました。この変更は文書が最新の情報を反映していることを示しています。

2. **手順の改訂**: プロジェクト設定に関する手順で、アクセス手順が明確化されました。以前の手順から、新しい手順に変更され、「**管理センター** > **概要**」を選択してプロジェクト設定に移行するよう指示があります。

3. **接続情報の強化**: Serp APIの接続を追加する手順が細かく説明されており、ユーザーがAPIキーを簡単に追加できるように具体的な指示が提供されています。また、関連するスクリーンショットも更新され、視覚的に手順をサポートしています。

4. **用語の修正**: 他の小さな用語の修正も行われており、例として「SerpConnection」という名前が「Serp Connection」に変更され、より明確な表現になっています。

これらの変更によって、ユーザーはSerp APIツールをより円滑に理解し、利用できるような内容になっています。教育的効果が強化され、アクセスのしやすさが向上しています。

## articles/ai-studio/media/prompt-flow/serp-api-tool.png{#item-2a4be2}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Serp APIツールの画像に関する変更"
}
```

### Explanation
この変更では、Serp APIツールに関連する画像ファイル（`serp-api-tool.png`）が修正されました。しかし、追加、削除、変更は行われておらず、実質的なコンテンツの変更はありません。

具体的なポイントは以下の通りです：

1. **画像の更新**: 画像ファイルにアクセスするためのリンクが提供されていますが、これに対する具体的な修正内容は示されていません。ファイル自体は変更されていないと考えられます。

2. **ファイルのリファレンス**: 画像は、Azure AI Foundryツールと関連してユーザーにとって重要な視覚リソースであるため、アクセスしやすい場所に保持されています。この状態は、ユーザーが必要な情報を見つけやすくする役割を果たします。

この変更は、主にファイルの参照やリンクの整備によるものであり、ユーザーの体験を向上させるための背景として管理されています。画像自体には変更がないため、ファイルの利用に影響はありません。

## articles/ai-studio/media/prompt-flow/serp-connection-keys.png{#item-50b509}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Serp API接続キーの画像が追加されました"
}
```

### Explanation
この変更では、新しい画像ファイル（`serp-connection-keys.png`）が追加されました。これにより、Serp APIに関連する接続キーの視覚的な情報が提供され、ユーザーの理解を助ける役割を果たします。

具体的には以下のポイントが挙げられます：

1. **新しいリソースの追加**: このファイルは、Serp APIの接続キーに関する情報を視覚的に示すものであり、ユーザーが手順や設定を理解しやすくするための重要な要素です。

2. **アクセスリンクの提供**: 画像ファイルにアクセスするためのリンクが提供され、ユーザーは必要に応じてこの情報を参照することができます。

3. **ドキュメントの充実**: 新しい画像の追加により、関連する内容が視覚的に強化され、読者がドキュメントをより効果的に利用できるようになります。この変更により、説明がより具体的になり、ユーザーの学習体験が向上します。

全体として、この変更は文書の有用性を向上させる新機能の追加として位置付けることができます。

## articles/ai-studio/media/prompt-flow/serp-custom-connection-keys.png{#item-e22fae}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "Serp APIカスタム接続キーの画像が削除されました"
}
```

### Explanation
この変更では、Serp APIに関連するカスタム接続キーの画像ファイル（`serp-custom-connection-keys.png`）が削除されました。この変更は、リファレンスやドキュメントの内容に影響を与える可能性があります。

以下の点が重要です：

1. **画像の削除**: この画像が削除されたことで、Serp APIのカスタム接続キーに関する視覚的な情報が失われています。これにより、ユーザーは該当する情報をビジュアルで理解するのが難しくなる可能性があります。

2. **情報の利用への影響**: 削除された画像が、ドキュメント内で重要な役割を果たしていた場合、読者がその内容を理解するのに支障が出るかもしれません。この変更は、ユーザーの体験に直接的な影響を及ぼす重要な更新です。

3. **ドキュメントの更新が必要**: この画像の削除に伴い、関連する説明や手順についても更新が必要かもしれません。利用者が他のリソースに依存することが求められます。

全体として、この変更は重要なビジュアルコンテンツの削除を意味し、ユーザーへの情報提供において注意が必要です。


