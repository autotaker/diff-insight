---
date: '2024-10-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:00d70d8...MicrosoftDocs:6e9a4a2
summary: 今回の修正はAzureドキュメントに対するリンク構造の改善や新しいインクルードファイルの追加、文書の整合性強化が中心です。特に、ドキュメントインテリジェンス関連の改善や機能・モデルプレビューのための新インクルードファイル追加が目立ちます。また、Azure
  OpenAIに関する新セクションの追加や機能プレビューの警告も重要な更新です。大規模な破壊的変更はありませんが、インクルードパスの修正により、リンクの整合性が向上しました。これらの変更は、ドキュメントの品質向上やユーザー体験の向上に貢献します。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:00d70d8...MicrosoftDocs:6e9a4a2){target="_blank"}

<format>
# Highlights
今回の修正は多岐にわたるAzureのドキュメントに対するもので、主にリンク構造の改善、新しいインクルードファイルの追加、および文書の整合性を強化するための調整が中心となっています。特にドキュメントインテリジェンス関連の改善や機能およびモデルプレビューの新しいインクルードファイルの追加が目立ちます。また、機能プレビューの警告と新しいTOCにAzure OpenAIセクションの追加という重要な更新も含まれています。

## New features
- 新しいインクルードファイルが`feature-preview.md`および`models-preview.md`として追加され、これに伴い、多くのドキュメントでインクルードファイルへのパス修正が行われました。
- `toc.yml`ファイルにてAzure OpenAIに関する新しいセクション「What is Azure OpenAI?」が追加されました。

## Breaking changes
- 特に大規模な破壊的変更はありませんが、インクルードパスの修正は、正しいリンクが設定されていることを確認する必要があり、関連するドキュメントへの影響を確認することが重要です。

## Other updates
- 各種ドキュメントでのインクルードタグのパス修正が行われ、リンクされたコンテンツの整合性が改善されています。
- 特定の文書において、軽微なテキスト修正と文言の一貫性を高めるための変更が加えられています。

# Insights
今回のドキュメント更新は、Azureドキュメントの品質向上を目的とした体系的なリンク修正作業がメインとなっています。Azure AI Studioなどのプラットフォームで提供される機能やモデルのプレビューにアクセスする際、使用者に最新の正確な情報を提供するためにインクルードファイルが標準化されました。この変更はユーザーが着実に最新のドキュメントにアクセスできるよう支援する重要な施策です。

また、Azure OpenAIに関する新セクションの追加は、AI Studioのユーザーがこのサービスについてより詳細な情報と具体例を簡単に参照できるようにするための戦略的な位置づけです。このようなTOC更新は、ユーザー体験の向上と情報ナビゲーションの一貫性・効率向上に寄与します。

今後も、こうした細かな改善を継続的に実施することで、ドキュメントの利用価値を高め、ユーザーの利便性と信頼性を向上させるとともに、新しいユーザーでも必要な情報にすぐにアクセスできる環境を提供し続けられるでしょう。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [bank-check.md](#item-8655d6) | minor update | 銀行小切手に関するドキュメントの更新 | modified | 3 | 16 | 19 | 
| [bank-statement.md](#item-fa4383) | minor update | 銀行明細書に関するドキュメントの更新 | modified | 3 | 22 | 25 | 
| [business-card.md](#item-114b38) | minor update | 名刺に関するドキュメントの更新 | modified | 3 | 17 | 20 | 
| [contract.md](#item-6d01dd) | minor update | 契約に関するドキュメントの更新 | modified | 5 | 17 | 22 | 
| [credit-card.md](#item-5d0c6d) | minor update | クレジットカードに関するドキュメントの更新 | modified | 5 | 17 | 22 | 
| [health-insurance-card.md](#item-6b1c0e) | minor update | 健康保険カードに関するドキュメントの更新 | modified | 3 | 43 | 46 | 
| [id-document.md](#item-bf45fa) | minor update | IDドキュメントに関するドキュメントの更新 | modified | 3 | 136 | 139 | 
| [invoice.md](#item-cabbf9) | minor update | 請求書に関するドキュメントの更新 | modified | 8 | 73 | 81 | 
| [marriage-certificate.md](#item-936798) | minor update | 婚姻証明書に関するドキュメントの更新 | modified | 5 | 27 | 32 | 
| [pay-stub.md](#item-7f747e) | minor update | 給与明細書に関するドキュメントの更新 | modified | 7 | 24 | 31 | 
| [receipt.md](#item-089054) | breaking change | 領収書に関するドキュメントの大幅な改訂 | modified | 3 | 170 | 173 | 
| [toc.yml](#item-81aa7b) | minor update | ドキュメント目次の更新 | modified | 21 | 1 | 22 | 
| [evaluation-approach-gen-ai.md](#item-ac9697) | minor update | 評価アプローチに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [evaluation-improvement-strategies.md](#item-9854b1) | minor update | 評価改善戦略に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [evaluation-metrics-built-in.md](#item-d455bd) | minor update | 評価および監視指標に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [fine-tuning-overview.md](#item-31b07b) | minor update | ファインチューニングの概要に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [safety-evaluations-transparency-note.md](#item-a4dacb) | minor update | 安全評価に関する透明性ノートの文書のリンク修正 | modified | 1 | 1 | 2 | 
| [vulnerability-management.md](#item-e37d54) | minor update | 脆弱性管理に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [autoscale.md](#item-ad23fa) | minor update | オートスケールに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [concept-data-privacy.md](#item-af88ce) | minor update | データプライバシーに関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [connections-add.md](#item-6f5a17) | minor update | 接続の追加に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [costs-plan-manage.md](#item-6d5c73) | minor update | Azure AI Studioのコスト管理に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [create-azure-ai-hub-template.md](#item-c8813b) | minor update | Azure AI Hubテンプレート作成に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [create-manage-compute-session.md](#item-6ed743) | minor update | Azure AI Studioのコンピュートセッション管理に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [create-manage-compute.md](#item-156c7f) | minor update | Azure AI Studioのコンピュートインスタンス作成に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [create-secure-ai-hub.md](#item-adbe6e) | minor update | セキュアなAzure AIスタジオハブ作成に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [data-add.md](#item-6139b1) | minor update | Azure AI Studioプロジェクトへのデータ追加に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [data-image-add.md](#item-a1f038) | minor update | GPT-4 Turbo with Visionを使用した画像データの追加に関するドキュメントのリンク修正 | modified | 1 | 1 | 2 | 
| [deploy-models-cohere-command.md](#item-3e97f4) | minor update | Cohere Commandチャットモデルの使用に関するドキュメントのリンク修正 | modified | 2 | 2 | 4 | 
| [deploy-models-cohere-embed.md](#item-eab662) | minor update | Cohere Embed V3モデルの使用に関するドキュメントのリンク修正 | modified | 2 | 2 | 4 | 
| [deploy-models-cohere-rerank.md](#item-5047f8) | minor update | Cohere Rerankモデルの使用に関するドキュメントのリンク修正 | modified | 3 | 1 | 4 | 
| [deploy-models-jais.md](#item-0bd11f) | minor update | JAISチャットモデルの使用に関するドキュメントのリンク修正 | modified | 2 | 2 | 4 | 
| [deploy-models-jamba.md](#item-eeefca) | minor update | AI21のJambaモデルに関するドキュメントのリンクと内容の更新 | modified | 5 | 3 | 8 | 
| [deploy-models-llama.md](#item-6274a7) | minor update | Meta Llamaモデルに関するドキュメントのリンクの更新 | modified | 4 | 3 | 7 | 
| [deploy-models-mistral-nemo.md](#item-e7b729) | minor update | Mistral Nemoチャットモデルに関するドキュメントのリンク更新 | modified | 2 | 1 | 3 | 
| [deploy-models-mistral-open.md](#item-84e005) | minor update | MistralおよびMixtralチャットモデルに関するドキュメントのリンク更新 | modified | 2 | 1 | 3 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | Mistralプレミアムチャットモデルに関するドキュメントのリンク更新 | modified | 2 | 1 | 3 | 
| [deploy-models-openai.md](#item-de796b) | minor update | Azure OpenAIモデルに関するドキュメントのリンク更新 | modified | 1 | 1 | 2 | 
| [deploy-models-phi-3-5-vision.md](#item-8d6d7d) | minor update | Phi-3.5ビジョン付きチャットモデルに関するドキュメントのリンク更新 | modified | 2 | 2 | 4 | 
| [deploy-models-phi-3-vision.md](#item-bd5aae) | minor update | Phi-3ビジョン付きチャットモデルに関するドキュメントのリンク更新 | modified | 2 | 2 | 4 | 
| [deploy-models-phi-3.md](#item-47e305) | minor update | Phi-3ファミリーのチャットモデルに関するドキュメントのリンク更新 | modified | 2 | 2 | 4 | 
| [deploy-models-serverless-availability.md](#item-143252) | minor update | サーバーレスモデルのデプロイに関する文書の更新 | modified | 2 | 0 | 2 | 
| [deploy-models-serverless-connect.md](#item-4faded) | minor update | サーバーレスAPIエンドポイントに関する文書の更新 | modified | 2 | 0 | 2 | 
| [deploy-models-serverless.md](#item-f8177f) | minor update | サーバーレスAPIデプロイに関する文書の更新 | modified | 2 | 0 | 2 | 
| [deploy-models-timegen-1.md](#item-bd50f3) | minor update | TimeGEN-1モデルデプロイに関する文書の更新 | modified | 3 | 1 | 4 | 
| [ai-template-get-started.md](#item-d71b59) | minor update | AIテンプレートの概要文書の更新 | modified | 1 | 1 | 2 | 
| [connections-add-sdk.md](#item-14b519) | minor update | Azure Machine Learning SDKを使用した新しい接続の追加に関する文書の更新 | modified | 1 | 1 | 2 | 
| [create-hub-project-sdk.md](#item-8c3e99) | minor update | Azure Machine Learning SDKおよびCLIを使用したハブプロジェクト作成に関する文書の更新 | modified | 1 | 1 | 2 | 
| [evaluate-sdk.md](#item-9d5197) | minor update | Azure AI評価SDKを使用した評価に関する文書の修正 | modified | 1 | 1 | 2 | 
| [index-build-consume-sdk.md](#item-2ee880) | minor update | インデックスの構築と消費に関する文書の更新 | modified | 2 | 2 | 4 | 
| [simulator-interaction-data.md](#item-c753d1) | minor update | シミュレーションインタラクションデータに関する文書の修正 | modified | 1 | 1 | 2 | 
| [trace-local-sdk.md](#item-f7dfb5) | minor update | プロンプトフローSDKによるアプリケーションのトレースに関する文書の更新 | modified | 1 | 1 | 2 | 
| [trace-production-sdk.md](#item-8d5b4c) | minor update | プロダクションSDKによるトレーシングの有効化に関する文書の更新 | modified | 1 | 1 | 2 | 
| [vscode.md](#item-24bd97) | minor update | VS CodeでのAzure AI Studioプロジェクトの開始に関する文書の更新 | modified | 1 | 1 | 2 | 
| [disaster-recovery.md](#item-963556) | minor update | 顧客主導の災害復旧に関する文書の更新 | modified | 1 | 1 | 2 | 
| [evaluate-generative-ai-app.md](#item-451c6e) | minor update | 生成AIアプリの評価に関する文書の更新 | modified | 1 | 1 | 2 | 
| [evaluate-prompts-playground.md](#item-2b9a45) | minor update | Azure AI Studioプレイグラウンドにおけるプロンプト評価に関する文書の更新 | modified | 1 | 1 | 2 | 
| [evaluate-results.md](#item-416e77) | minor update | Azure AI Studioにおける評価結果の表示に関する文書の更新 | modified | 1 | 1 | 2 | 
| [fine-tune-model-llama.md](#item-2a42d8) | minor update | Azure AI StudioにおけるMeta Llamaモデルのファインチューニングに関する文書の更新 | modified | 3 | 1 | 4 | 
| [fine-tune-phi-3.md](#item-5b722a) | minor update | Azure AI StudioにおけるPhi-3モデルのファインチューニングに関する文書の更新 | modified | 5 | 0 | 5 | 
| [flow-bulk-test-evaluation.md](#item-e60767) | minor update | フローのバルクテスト評価に関する文書の更新 | modified | 1 | 1 | 2 | 
| [flow-deploy.md](#item-e7fc64) | minor update | フローのデプロイに関する文書の更新 | modified | 1 | 1 | 2 | 
| [flow-develop-evaluation.md](#item-8514d1) | minor update | 評価フローの開発に関する文書の更新 | modified | 1 | 1 | 2 | 
| [flow-develop.md](#item-d1ac3e) | minor update | プロンプトフローの開発に関する文書の更新 | modified | 1 | 1 | 2 | 
| [flow-process-image.md](#item-1476f6) | minor update | プロンプトフローでの画像処理に関する文書の更新 | modified | 1 | 1 | 2 | 
| [flow-tune-prompts-using-variants.md](#item-882979) | minor update | Azure AI Studioにおけるバリアントを使用したプロンプト調整の文書更新 | modified | 1 | 1 | 2 | 
| [groundedness.md](#item-e3c37c) | minor update | グラウンデッドネス検出に関する文書の更新 | modified | 1 | 1 | 2 | 
| [index-add.md](#item-1b013b) | minor update | Azure AI Studioにおけるベクターインデックスの構築と利用に関する文書の更新 | modified | 1 | 1 | 2 | 
| [model-benchmarks.md](#item-82de8e) | minor update | Azure AI Studioにおけるモデルベンチマークに関する文書の更新 | modified | 1 | 1 | 2 | 
| [model-catalog-overview.md](#item-278001) | minor update | Azure AI Studioのモデルカタログに関する文書の更新 | modified | 2 | 2 | 4 | 
| [monitor-quality-safety.md](#item-61adb3) | minor update | デプロイされたプロンプトフローアプリケーションの品質とトークン使用量の監視に関する文書の更新 | modified | 1 | 1 | 2 | 
| [azure-open-ai-gpt-4v-tool.md](#item-053d0d) | minor update | Azure AI StudioにおけるGPT-4 Turbo with Visionツールに関する文書の更新 | modified | 1 | 1 | 2 | 
| [content-safety-tool.md](#item-09b048) | minor update | Azure AI Studioのコンテンツセーフティツールに関する文書の更新 | modified | 2 | 2 | 4 | 
| [embedding-tool.md](#item-81420c) | minor update | Azure AI Studioの埋め込みツールに関する文書の更新 | modified | 1 | 1 | 2 | 
| [index-lookup-tool.md](#item-cad66d) | minor update | Azure AI Studioのインデックスルックアップツールに関する文書の更新 | modified | 1 | 1 | 2 | 
| [llm-tool.md](#item-6691f4) | minor update | Azure AI StudioのLLMツールに関する文書の更新 | modified | 1 | 1 | 2 | 
| [prompt-flow-tools-overview.md](#item-fd7471) | minor update | Azure AI Studioのプロンプトフローツールに関する概要文書の更新 | modified | 1 | 1 | 2 | 
| [prompt-tool.md](#item-c6a9a0) | minor update | Azure AI Studioのプロンプトツールに関する文書の更新 | modified | 1 | 1 | 2 | 
| [python-tool.md](#item-c9200f) | minor update | Azure AI StudioのPythonツールに関する文書の更新 | modified | 1 | 1 | 2 | 
| [rerank-tool.md](#item-dd52bf) | minor update | Azure AI Studioの再ランキングツールに関する文書の更新 | modified | 1 | 1 | 2 | 
| [serp-api-tool.md](#item-144ed7) | minor update | Azure AI StudioのSERP APIツールに関する文書の更新 | modified | 2 | 2 | 4 | 
| [prompt-flow.md](#item-9fdb4a) | minor update | Azure AI Studioのプロンプトフローに関する文書の更新 | modified | 1 | 1 | 2 | 
| [prompt-shields.md](#item-ed4acd) | minor update | Azure AI Studioのプロンプトシールドに関する文書の更新 | modified | 1 | 1 | 2 | 
| [quota.md](#item-39c866) | minor update | Azure AI Studioのクォータ管理に関する文書の更新 | modified | 1 | 1 | 2 | 
| [troubleshoot-deploy-and-monitor.md](#item-6b0de7) | minor update | Azure AI Studioのデプロイおよびモニターのトラブルシューティングに関する文書の更新 | modified | 1 | 1 | 2 | 
| [troubleshoot-secure-connection-project.md](#item-32d5c4) | minor update | プライベートエンドポイントを使用したプロジェクトへの接続トラブルシューティングに関する文書の更新 | modified | 1 | 1 | 2 | 
| [feature-preview.md](#item-931f1e) | new feature | 機能プレビューに関するインクルードファイルの追加 | added | 13 | 0 | 13 | 
| [models-preview.md](#item-d2bea2) | new feature | モデルプレビューに関するインクルードファイルの追加 | added | 13 | 0 | 13 | 
| [content-safety.md](#item-bdaebf) | minor update | コンテンツ安全性クイックスタートのインクルードファイルパスの修正 | modified | 1 | 1 | 2 | 
| [get-started-code.md](#item-8a5082) | minor update | カスタムチャットアプリのクイックスタートのインクルードファイルパスの修正 | modified | 1 | 1 | 2 | 
| [get-started-playground.md](#item-e4d7fb) | minor update | チャットプレイグラウンドのクイックスタートのインクルードファイルパスの修正 | modified | 1 | 1 | 2 | 
| [hear-speak-playground.md](#item-3167bc) | minor update | チャットプレイグラウンドの音声機能クイックスタートのインクルードファイルパスの修正 | modified | 1 | 1 | 2 | 
| [multimodal-vision.md](#item-740e84) | minor update | マルチモーダルビジョンのクイックスタートのインクルードファイルパスの修正 | modified | 1 | 1 | 2 | 
| [reference-model-inference-api.md](#item-9fe240) | minor update | モデル推論APIのリファレンスのインクルードファイルパスの修正 | modified | 1 | 1 | 2 | 
| [reference-model-inference-chat-completions.md](#item-e09823) | minor update | チャットコンプリーションのモデル推論リファレンスのインクルードファイルパスの修正 | modified | 1 | 1 | 2 | 
| [reference-model-inference-completions.md](#item-bae39d) | minor update | コンプリーションのモデル推論リファレンスのインクルードファイルパスの修正 | modified | 1 | 1 | 2 | 
| [reference-model-inference-embeddings.md](#item-5e9064) | minor update | エンベディングのモデル推論リファレンスのインクルードファイルパスの修正 | modified | 1 | 1 | 2 | 
| [reference-model-inference-images-embeddings.md](#item-70c7ac) | minor update | 画像エンベディングのモデル推論リファレンスのインクルードファイルパスの修正 | modified | 1 | 1 | 2 | 
| [reference-model-inference-info.md](#item-e465b4) | minor update | モデル推論情報リファレンスのファイルパスとモデルタイプの修正 | modified | 2 | 2 | 4 | 
| [region-support.md](#item-d402e1) | minor update | リージョンサポートに関するリファレンスのインクルードパスの修正 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-2745cd) | new feature | TOCにAzure OpenAIに関するセクションを追加 | modified | 2 | 0 | 2 | 
| [deploy-chat-web-app.md](#item-987845) | minor update | チャットWebアプリのデプロイに関するチュートリアルのインクルードパスの修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/prebuilt/bank-check.md{#item-8655d6}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 10/03/2024
+ms.date: 10/16/2024
 ms.author: lajanuar
 monikerRange: '>=doc-intel-4.0.0'
 ---
@@ -53,24 +53,11 @@ A check is a secure way to transfer amount from payee's account to receiver's ac
 
 ## Supported languages and locales
 
-*See* our [Language Support](../language-support/prebuilt.md) page for a complete list of supported languages.
+ For a complete list of supported languages, *see* our [prebuilt model language support](../language-support/prebuilt.md) page.
 
 ## Field extractions
 
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`PayerName`|`string`|Name of the payer (drawer)|Jane Doe|
-|`PayerAddress`|`address`|Address of the payer (drawer)|123 Main St., Redmond, Washington, 98052|
-|`PayTo`|`string`|Name of the payee|John Smith|
-|`CheckDate`|`date`|Date the check was written|2023-04-01|
-|`NumberAmount`|`number`|Amount of the check written in numeric form|150.00|
-|`WordAmount`|`number`|Amount of the check written in letter form|one-hundred-fifty and 00/100|
-|`BankName`|`string`|Name of the bank|Contoso Bank|
-|`Memo`|`string`|Short note describing the payment|April Rent Payment|
-|`MICR`|`object`|Magnetic Ink Character Recognition (MICR) line|⑈0740⑈ ⑆123456789⑆ 1001001234⑈|
-|`MICR.RoutingNumber`|`string`|Routing number of the bank|⑆123456789⑆|
-|`MICR.AccountNumber`|`string`|Account number|1001001234⑈|
-|`MICR.CheckNumber`|`string`|Check number|⑈0740⑈|
+For supported document extraction fields, refer to the [bank check model schema](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/bank-check.md) page in our GitHub sample repository.
 
 ## Supported locales
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "銀行小切手に関するドキュメントの更新"
}
```

### Explanation
この修正は、Azureのドキュメント「銀行小切手」に関連するものです。以下の変更が行われました：

1. **日付の更新**: ドキュメントの日付が2024年10月3日から2024年10月16日に変更されました。
   
2. **言語サポートの説明の修正**: 「言語サポート」が提供されていることに関する文言が改善され、より明確に関連ページへの誘導が行われるようになりました。

3. **フィールド抽出の紹介の修正**: フィールド抽出のセクションについて、以前の内容は削除され、代わりに、銀行小切手モデルのスキーマに関する情報へのリンクが提供されました。

これにより、ユーザーは銀行小切手に関する情報をより簡単に取得できるようになります。全体として、ドキュメントがより整理され、最新の情報が反映されています。

## articles/ai-services/document-intelligence/prebuilt/bank-statement.md{#item-fa4383}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 10/03/2024
+ms.date: 10/16/2024
 ms.author: lajanuar
 ms.custom: references_regions
 monikerRange: '>=doc-intel-4.0.0'
@@ -51,30 +51,11 @@ A bank statement helps review account's activities during a specified period. It
 
 ## Supported languages and locales
 
-*See* our [Language Support](../language-support/prebuilt.md) page for a complete list of supported languages.
+For a complete list of supported languages, *see* our [prebuilt model language support](../language-support/prebuilt.md) page.
 
 ## Field extractions
 
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`AccountNumber`|`string`|Account number on the bank statement|987-654-3210|
-|`AccountType`|`string`|Type of account on the bank statement|Checking|
-|`BankAddress`|`address`|Listed address of the bank|123 Main St., Redmond, Washington 98052|
-|`BankName`|`string`|Listed name of the bank|Contoso Bank|
-|`AccountHolderAddress`|`address`|Address of the account holder|456 Main St., Redmond, Washington 98052|
-|`AccountHolderName`|`string`|Name of the account holder|JOHN DOE|
-|`EndingBalance`|`number`|Ending balance on the bank statement|$1488.03|
-|`BeginningBalance`|`number`|Beginning balance on the bank statement|$1488.03|
-|`StatementStartDate`|`date`|Start date of the bank statement|July 01, 2017|
-|`StatementEndDate`|`date`|End date of the bank statement|July 31, 2017|
-|`TotalServiceFees`|`number`|Total service fees|$0.00|
-|`Transactions`|`array`|Extracted transaction line item|07/17<br>OnlineTransfer From Check...6609 Transaction#: 6373187418<br>$1,500.00|
-|`Transactions.*`|`object`|||
-|`Transactions.*.Date`|`date`|Transaction date|07/17|
-|`Transactions.*.Description`|`string`|Transaction description|OnlineTransfer From Check...6609 Transaction#: 6373187418|
-|`Transactions.*.CheckNumber`|`string`|Check number of the transaction|6609|
-|`Transactions.*.DepositAmount`|`number`|Amount of deposit in the transaction|$1500.00|
-|`Transactions.*.WithdrawalAmount`|`number`|Amount of withdrawal in the transaction|$1500.00|
+For supported document extraction fields, refer to the [bank check model schema](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/bank-statement.md) page in our GitHub sample repository.
 
 ## Supported locales
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "銀行明細書に関するドキュメントの更新"
}
```

### Explanation
この修正は、Azureのドキュメント「銀行明細書」に関連しており、以下の変更が行われました。

1. **日付の更新**: ドキュメントの日付が2024年10月3日から2024年10月16日に変更されました。

2. **言語サポートの説明の修正**: 言語サポートに関する文言が若干修正され、関連ページへの誘導がより明確になりました。

3. **フィールド抽出に関する情報の変更**: 銀行明細書のフィールド抽出に関する詳細情報が削除され、新たに銀行明細書モデルのスキーマに関するリンクが追加されました。これにより、ユーザーは関連情報へのアクセスが容易になります。

これらの変更により、ドキュメントの内容がより整理され、最新の情報が反映され、ユーザーが必要とする資料を見つけやすくなっています。

## articles/ai-services/document-intelligence/prebuilt/business-card.md{#item-114b38}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 05/23/2024
+ms.date: 10/16/2024
 ms.author: lajanuar
 ---
 
@@ -176,25 +176,11 @@ See how data, including name, job title, address, email, and company name, is ex
 
 ## Supported languages and locales
 
-*See* our [Language Support](../language-support/prebuilt.md) page for a complete list of supported languages.
+For a complete list of supported languages, *see* our [prebuilt model language support](../language-support/prebuilt.md) page.
 
 ## Field extractions
 
-|Name| Type | Description |Standardized output |
-|:-----|:----|:----|:----:|
-| ContactNames | Array of objects | Contact name |  |
-| FirstName | String | First (given) name of contact |  |
-| LastName | String | Last (family) name of contact |  |
-| CompanyNames | Array of strings | Company name|  |
-| Departments | Array of strings | Department or organization of contact |  |
-| JobTitles | Array of strings | Listed Job title of contact |  |
-| Emails | Array of strings | Contact email address |  |
-| Websites | Array of strings | Company website |  |
-| Addresses | Array of strings | Address extracted from business card | |
-| MobilePhones | Array of phone numbers | Mobile phone number from business card |+1 xxx xxx xxxx |
-| Faxes | Array of phone numbers | Fax phone number from business card | +1 xxx xxx xxxx |
-| WorkPhones | Array of phone numbers | Work phone number from business card | +1 xxx xxx xxxx |
-| OtherPhones     | Array of phone numbers | Other phone number from business card | +1 xxx xxx xxxx |
+For supported document extraction fields, refer to the [business card model schema](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2023-07-31/business-card.md) page in our GitHub sample repository.
 
 ::: moniker-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "名刺に関するドキュメントの更新"
}
```

### Explanation
この修正は、Azureのドキュメント「名刺」に関連しています。以下の点が変更されました：

1. **日付の更新**: ドキュメントの日付が2024年5月23日から2024年10月16日に更新されました。

2. **言語サポートの説明の修正**: 言語サポートに関する説明が少し調整され、関連ページへの誘導が、より分かりやすくなりました。

3. **フィールド抽出の情報の変更**: フィールド抽出セクションにおいて、以前の情報が削除され、新たに名刺モデルのスキーマへのリンクが追加されました。これにより、ユーザーは名刺から抽出される情報に関する詳細をより容易に取得できるようになります。

これらの変更により、ドキュメントは整理され、最新の情報が提供され、ユーザーが必要な情報へ迅速にアクセスできるようになっています。

## articles/ai-services/document-intelligence/prebuilt/contract.md{#item-6d01dd}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 08/07/2024
+ms.date: 10/16/2024
 ms.author: lajanuar
 monikerRange: '>=doc-intel-3.0.0'
 ---
@@ -89,25 +89,13 @@ See how data, including customer information, vendor details, and line items, is
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
+For a complete list of supported languages, *see* our [Language Support—prebuilt models](../language-support/prebuilt.md) page.
 
 ## Field extraction
 
-The following are the fields extracted from a contract in the JSON output response. 
-
-|Name| Type | Description | Example output |
-|:-----|:----|:----|:---:|
-| Title | String | Contract title| Service agreement |
-| ContractId | String | Contract title| AB12956 |
-| Parties | Array |List of legal parties| |
-| ExecutionDate | Date |Date when the agreement was fully signed and agreed upon by all parties|`On this twenty-third day of February two thousand and twenty two` |
-| ExpirationDate | Date |Date when the contract ends| One year |
-| EffectiveDate  | Date |Date when the contract is in effect| immediately |
-| RenewalDate | Date |Date when the contract needs to be renewed| `On this twenty-third day of February two thousand and twenty two` |
-| ContractDuration | String | Contract terms | Five (5) years |
-| Jurisdictions | Array | List of jurisdictions| |
-
-The contract key-value pairs and line items extracted are in the `documentResults` section of the JSON output.
+* For supported document extraction fields, refer to the [contract model schema](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/contract.md) page in our GitHub sample repository.
+
+* The contract key-value pairs and line items extracted are in the `documentResults` section of the JSON output.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "契約に関するドキュメントの更新"
}
```

### Explanation
この修正は、Azureのドキュメント「契約」に関するもので、以下の変更が行われました：

1. **日付の更新**: ドキュメントの日付が2024年8月7日から2024年10月16日に変更されました。

2. **言語サポートの説明の修正**: 言語サポートの関連文言が若干修正され、より明確にページへの誘導が行われています。

3. **フィールド抽出の情報の変更**: 契約に関するフィールド抽出の詳細が調整され、契約モデルのスキーマへのリンクが追加されました。また、フィールドの説明が整理され、JSON出力内の `documentResults` セクションにおける契約のキー・バリューのペアとラインアイテムについての説明が強調されています。

これらの変更により、ドキュメントは最新の情報が反映され、ユーザーが必要な情報を容易に見つけられるようになっています。

## articles/ai-services/document-intelligence/prebuilt/credit-card.md{#item-5d0c6d}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 10/03/2024
+ms.date: 10/16/2024
 ms.author: lajanuar
 monikerRange: '>=doc-intel-4.0.0'
 ---
@@ -68,25 +68,13 @@ To see how data extraction works for the Credit/Debit card service, you need the
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
+For a complete list of supported languages, *see* our [prebuilt model language support](../language-support/prebuilt.md) page.
 
 ## Field extraction
 
-The following are the fields extracted from a contract in the JSON output response.
-
-|Name| Type | Description | Example output |
-|:-----|:----|:----|:---:|
-| CardNumber | String | A unique identifier for the card| 4275 0000 0000 0000 |
-| IssuingBank | String | The name of the bank that issued the card| Woodgrove Bank |
-| PaymentNetwork | String |The payment network that processes the card transaction| VISA |
-| CardHolderName | String |The name of the person who owns the card| JOHN SMITH |
-| CardHolderCompanyName | String| The name of the company that the card is associated with | Contoso, Ltd. |
-| ValidDate | Date | Valid from date | 01/16 |
-| ExpirationDate | Date | Expiration date| 01/19 |
-| CardVerificationValue | String | Card verification value (CVV) | 764 |
-| CustomerServicePhoneNumbers | Array | List of support numbers | +1 (555) 123-4567 |
-
-The bank cards key-value pairs and line items extracted are in the `documentResults` section of the JSON output.
+* For supported document extraction fields, refer to the [credit card model schema](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/credit-card.md) page in our GitHub sample repository.
+
+* The bank cards key-value pairs and line items extracted are in the `documentResults` section of the JSON output.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クレジットカードに関するドキュメントの更新"
}
```

### Explanation
この修正は、Azureのドキュメント「クレジットカード」に関連しており、以下の変更が行われました：

1. **日付の更新**: ドキュメントの日付が2024年10月3日から2024年10月16日に更新されました。

2. **言語サポートの説明の修正**: 言語サポートに関する文言が若干修正され、より明確に関連ページへの誘導が行われています。

3. **フィールド抽出の情報の変更**: クレジットカードに関するフィールド抽出の説明が調整され、クレジットカードモデルのスキーマへのリンクが新たに追加されました。また、フィールドの説明が整理され、JSON出力内の `documentResults` セクションにおけるカードのキー・バリューのペアとラインアイテムについての情報が強調されています。

これらの変更により、ドキュメントは最新の情報が反映され、ユーザーが必要な情報を容易に見つけられるようになっています。

## articles/ai-services/document-intelligence/prebuilt/health-insurance-card.md{#item-6b1c0e}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 05/23/2024
+ms.date: 10/16/2024
 ms.author: lajanuar
 monikerRange: 'doc-intel-4.0.0 || >=doc-intel-3.0.0'
 ---
@@ -93,51 +93,11 @@ See how data is extracted from health insurance cards using the Document Intelli
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
+For a complete list of supported languages, *see* our [prebuilt model language support](../language-support/prebuilt.md) page.
 
 ## Field extraction
 
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`Insurer`|`string`|Health insurance provider name|PREMERA<br>BLUE CROSS|
-|`Member`|`object`|||
-|`Member.Name`|`string`|Member name|ANGEL BROWN|
-|`Member.BirthDate`|`date`|Member date of birth|01/06/1958|
-|`Member.Employer`|`string`|Member name employer|Microsoft|
-|`Member.Gender`|`string`|Member gender|M|
-|`Member.IdNumberSuffix`|`string`|Identification Number Suffix as it appears on some health insurance cards|01|
-|`Dependents`|`array`|Array holding list of dependents, ordered where possible by membership suffix value||
-|`Dependents.*`|`object`|||
-|`Dependents.*.Name`|`string`|Dependent name|01|
-|`IdNumber`|`object`|||
-|`IdNumber.Prefix`|`string`|Identification Number Prefix as it appears on some health insurance cards|`ABC`|
-|`IdNumber.Number`|`string`|Identification Number|123456789|
-|`GroupNumber`|`string`|Insurance Group Number|1000000|
-|`PrescriptionInfo`|`object`|||
-|`PrescriptionInfo.Issuer`|`string`|ANSI issuer identification number (IIN)|(80840) 300-11908-77|
-|`PrescriptionInfo.RxBIN`|`string`|Prescription issued BIN number|987654|
-|`PrescriptionInfo.RxPCN`|`string`|Prescription processor control number|63200305|
-|`PrescriptionInfo.RxGrp`|`string`|Prescription group number|BCAAXYZ|
-|`PrescriptionInfo.RxId`|`string`|Prescription identification number. If not present, defaults to membership ID number|P97020065|
-|`PrescriptionInfo.RxPlan`|`string`|Prescription Plan number|A1|
-|`Pbm`|`string`|Pharmacy Benefit Manager for the plan|CVS CAREMARK|
-|`EffectiveDate`|`date`|Date from which the plan is effective|08/12/2012|
-|`Copays`|`array`|Array holding list of Co-Pay Benefits||
-|`Copays.*`|`object`|||
-|`Copays.*.Benefit`|`string`|Co-Pay Benefit name|Deductible|
-|`Copays.*.Amount`|`currency`|Co-Pay required amount|$1,500|
-|`Payer`|`object`|||
-|`Payer.Id`|`string`|Payer ID Number|89063|
-|`Payer.Address`|`address`|Payer address|123 Service St., Redmond, Washington, 98052|
-|`Payer.PhoneNumber`|`phoneNumber`|Payer phone number|+1 (987) 213-5674|
-|`Plan`|`object`|||
-|`Plan.Number`|`string`|Plan number|456|
-|`Plan.Name`|`string`|Plan name - If Medicaid -> then `medicaid` (all lower case).|HEALTH SAVINGS PLAN|
-|`Plan.Type`|`string`|Plan type|`PPO`|
-|`MedicareMedicaidInfo`|`object`|||
-|`MedicareMedicaidInfo.Id`|`string`|Medicare or Medicaid number|1AB2-CD3-EF45|
-|`MedicareMedicaidInfo.PartAEffectiveDate`|`date`|Effective date of Medicare Part A|01-01-2023|
-|`MedicareMedicaidInfo.PartBEffectiveDate`|`date`|Effective date of Medicare Part B|01-01-2023|
+For supported document extraction fields, refer to the [health insurance card model schema](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/health-insurance-card.md) page in our GitHub sample repository.
 
 ### Migration guide and REST API v3.1
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "健康保険カードに関するドキュメントの更新"
}
```

### Explanation
この修正は、Azureのドキュメント「健康保険カード」に関するもので、以下の変更が行われました：

1. **日付の更新**: ドキュメントの日付が2024年5月23日から2024年10月16日に更新されました。

2. **言語サポートの説明の修正**: 「言語サポート」セクションでは、関連ページへの誘導がより明確に記載されています。

3. **フィールド抽出の情報の変更**: 健康保険カードに関するフィールド抽出の詳細情報が整理され、仕様ページへのリンクが追加されました。これにより、フィールドの説明が簡素化され、JSON出力内の `documentResults` セクションの説明が強調されるようになりました。

4. **削除された行の数**: 修正には43行の削除が含まれています。これは、以前の冗長な情報や未使用の説明が削除された結果です。

これらの変更は、ドキュメントの読みやすさと情報の正確さを向上させ、ユーザーが必要な情報を見つけやすくすることを目的としています。

## articles/ai-services/document-intelligence/prebuilt/id-document.md{#item-bf45fa}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 08/07/2024
+ms.date: 10/16/2024
 ms.author: lajanuar
 ms.custom:
   - references.regions
@@ -228,145 +228,12 @@ Extract data, including name, birth date, and expiration date, from ID documents
 
 ## Field extractions
 
-The following are the fields extracted per document type. The Document Intelligence ID model `prebuilt-idDocument` extracts the following fields in the `documents.*.fields`. The json output includes all the extracted text in the documents, words, lines, and styles.
-
-::: moniker-end
-
-::: moniker range="doc-intel-3.1.0"
-
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Prebuilt_model/sample_analyze_identity_documents.py)
-
-::: moniker-end
-
-::: moniker range="doc-intel-4.0.0"
-
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Prebuilt_model/sample_analyze_identity_documents.py)
+For supported document extraction fields, refer to the [ID document model schema](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/id-document.md) page in our GitHub sample repository.
 
 ::: moniker-end
 
 <!--docutune:disable -->
 
-::: moniker range=">=doc-intel-3.0.0"
-
-### `idDocument.driverLicense`
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`CountryRegion`|`countryRegion`|Country or region code|USA|
-|`Region`|`string`|State or province|Washington|
-|`DocumentNumber`|`string`|Driver license number|WDLABCD456DG|
-|`DocumentDiscriminator`|`string`|Driver license document discriminator|12645646464554646456464544|
-|`FirstName`|`string`|Given name and middle initial if applicable|LIAM R.|
-|`LastName`|`string`|Surname|TALBOT|
-|`Address`|`address`|Address|123 STREET ADDRESS YOUR CITY WA 99999-1234|
-|`DateOfBirth`|`date`|Date of birth|01/06/1958|
-|`DateOfExpiration`|`date`|Date of expiration|08/12/2020|
-|`DateOfIssue`|`date`|Date of issue|08/12/2012|
-|`EyeColor`|`string`|Eye color|BLU|
-|`HairColor`|`string`|Hair color|BRO|
-|`Height`|`string`|Height|5'11"|
-|`Weight`|`string`|Weight|185LB|
-|`Sex`|`string`|Sex|M|
-|`Endorsements`|`string`|Endorsements|L|
-|`Restrictions`|`string`|Restrictions|B|
-|`PersonalNumber`|`string`|Personal Id. No.|A234567893|
-|`PlaceOfBirth`|`string`|Place of birth|MASSACHUSETTS, U.S.A.|
-|`VehicleClassifications`|`string`|Vehicle classification|D|
-
-### `idDocument.passport`
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`DocumentNumber`|`string`|Passport number|340020013|
-|`FirstName`|`string`|Given name and middle initial if applicable|JENNIFER|
-|`MiddleName`|`string`|Name between given name and surname|REYES|
-|`LastName`|`string`|Surname|BROOKS|
-|`Aliases`|`array`|||
-|`Aliases.*`|`string`|Also known as|MAT LIN|
-|`DateOfBirth`|`date`|Date of birth|1980-01-01|
-|`DateOfExpiration`|`date`|Date of expiration|2019-05-05|
-|`DateOfIssue`|`date`|Date of issue|2014-05-06|
-|`Sex`|`string`|Sex|F|
-|`CountryRegion`|`countryRegion`|Issuing country or organization|USA|
-|`DocumentType`|`string`|Document type|P|
-|`Nationality`|`countryRegion`|Nationality|USA|
-|`PlaceOfBirth`|`string`|Place of birth|MASSACHUSETTS, U.S.A.|
-|`PlaceOfIssue`|`string`|Place of issue|LISBON|
-|`IssuingAuthority`|`string`|Issuing authority|United States Department of State|
-|`PersonalNumber`|`string`|Personal ID. No.|A234567893|
-|`MachineReadableZone`|`object`|Machine readable zone (MRZ)|P<USABROOKS<<JENNIFER<<<<<<<<<<<<<<<<<<<<<<< 3400200135USA8001014F1905054710000307<715816|
-|`MachineReadableZone.FirstName`|`string`|Given name and middle initial if applicable|JENNIFER|
-|`MachineReadableZone.LastName`|`string`|Surname|BROOKS|
-|`MachineReadableZone.DocumentNumber`|`string`|Passport number|340020013|
-|`MachineReadableZone.CountryRegion`|`countryRegion`|Issuing country or organization|USA|
-|`MachineReadableZone.Nationality`|`countryRegion`|Nationality|USA|
-|`MachineReadableZone.DateOfBirth`|`date`|Date of birth|1980-01-01|
-|`MachineReadableZone.DateOfExpiration`|`date`|Date of expiration|2019-05-05|
-|`MachineReadableZone.Sex`|`string`|Sex|F|
-
-### `idDocument.nationalIdentityCard`
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`CountryRegion`|`countryRegion`|Country or region code|USA|
-|`Region`|`string`|State or province|Washington|
-|`DocumentNumber`|`string`|National identity card number|WDLABCD456DG|
-|`DocumentDiscriminator`|`string`|National identity card document discriminator|12645646464554646456464544|
-|`FirstName`|`string`|Given name and middle initial if applicable|LIAM R.|
-|`LastName`|`string`|Surname|TALBOT|
-|`Address`|`address`|Address|123 STREET ADDRESS YOUR CITY WA 99999-1234|
-|`DateOfBirth`|`date`|Date of birth|01/06/1958|
-|`DateOfExpiration`|`date`|Date of expiration|08/12/2020|
-|`DateOfIssue`|`date`|Date of issue|08/12/2012|
-|`EyeColor`|`string`|Eye color|BLUE|
-|`HairColor`|`string`|Hair color|BROWN|
-|`Height`|`string`|Height|5'11"|
-|`Weight`|`string`|Weight|185LB|
-|`Sex`|`string`|Sex|M|
-|`PersonalNumber`|`string`|Personal Id. No.|A234567893|
-|`PlaceOfBirth`|`string`|Place of birth|MASSACHUSETTS, U.S.A.|
-
-### `idDocument.residencePermit`
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`CountryRegion`|`countryRegion`|Country or region code|USA|
-|`DocumentNumber`|`string`|Residence permit number|WDLABCD456DG|
-|`FirstName`|`string`|Given name and middle initial if applicable|LIAM R.|
-|`LastName`|`string`|Surname|TALBOT|
-|`DateOfBirth`|`date`|Date of birth|01/06/1958|
-|`DateOfExpiration`|`date`|Date of expiration|08/12/2020|
-|`DateOfIssue`|`date`|Date of issue|08/12/2012|
-|`Sex`|`string`|Sex|M|
-|`PersonalNumber`|`string`|Personal Id. No.|A234567893|
-|`PlaceOfBirth`|`string`|Place of birth|Germany|
-|`Category`|`string`|Permit category|DV2|
-|`Address`|`string`|Address|123 STREET ADDRESS YOUR CITY WA 99999-1234|
-
-### `idDocument.usSocialSecurityCard`
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`DocumentNumber`|`string`|Social security card number|WDLABCD456DG|
-|`FirstName`|`string`|Given name and middle initial if applicable|LIAM R.|
-|`LastName`|`string`|Surname|TALBOT|
-|`DateOfIssue`|`date`|Date of issue|08/12/2012|
-
-### `idDocument`
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`Address`|`address`|Address|123 STREET ADDRESS YOUR CITY WA 99999-1234|
-|`DocumentNumber`|`string`|Driver license number|WDLABCD456DG|
-|`FirstName`|`string`|Given name and middle initial if applicable|LIAM R.|
-|`LastName`|`string`|Surname|TALBOT|
-|`DateOfBirth`|`date`|Date of birth|01/06/1958|
-|`DateOfExpiration`|`date`|Date of expiration|08/12/2020|
-
-::: moniker-end
-
 ::: moniker range="doc-intel-2.1.0"
 
 <!--docutune:enable -->
@@ -387,7 +254,7 @@ The following are the fields extracted per document type. The Document Intellige
 |  LastName | string | Extracted surname | "BROOKS" |
 |  Nationality | country | Country code compliant with ISO 3166 standard | "USA" |
 |  Sex | gender | Possible extracted values include "M" "F" "X" | "F" |
-|  MachineReadableZone | object | Extracted Passport MRZ including two lines of 44 characters each | "P<USABROOKS<<JENNIFER<<<<<<<<<<<<<<<<<<<<<<< 3400200135USA8001014F1905054710000307<715816" |
+|  MachineReadableZone | object | Extracted Passport `MRZ` including two lines of 44 characters each | "P<USABROOKS<<JENNIFER<<<<<<<<<<<<<<<<<<<<<<< 3400200135USA8001014F1905054710000307<715816" |
 |  DocumentType | string | Document type, for example, Passport, Driver's License | "passport" |
 |  Address | string | Extracted address (Driver's License only) | "123 STREET ADDRESS YOUR CITY WA 99999-1234"|
 |  Region | string | Extracted region, state, province, etc. (Driver's License only) | "Washington" |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "IDドキュメントに関するドキュメントの更新"
}
```

### Explanation
この修正は、Azureのドキュメント「IDドキュメント」に関連しており、以下の変更が行われました：

1. **日付の更新**: ドキュメントの日付が2024年8月7日から2024年10月16日に更新されました。

2. **フィールド抽出情報の簡素化**: ダウンストリームの変更に伴い、抽出されるフィールドの構造や説明が整理されました。特に、以前は提供されていたかなりの数のフィールド情報が136行削除されています。

3. **サンプルコードへのリンクの統一**: GitHub上のサンプルコードへのリンクが一つの場所に集約され、よりシンプルな説明に変更されています。

4. **マシンリーダブルゾーン(MRZ)の説明**: 説明が整備され、マシンリーダブルゾーンに関する内容が反映されています。

これらの修正により、ドキュメントがより明確になり、ユーザーが情報を容易に参照できるようになっています。

## articles/ai-services/document-intelligence/prebuilt/invoice.md{#item-cabbf9}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 08/07/2024
+ms.date: 10/16/2024
 ms.author: lajanuar
 ms.custom: references_regions
 ---
@@ -44,7 +44,7 @@ The Document Intelligence invoice model uses powerful Optical Character Recognit
 
 ## Automated invoice processing
 
-Automated invoice processing is the process of extracting key accounts payable fields from billing account documents. Extracted data includes line items from invoices integrated with your accounts payable (AP) workflows for reviews and payments. Historically, the accounts payable process is performed manually and, hence, very time consuming. Accurate extraction of key data from invoices is typically the first and one of the most critical steps in the invoice automation process.
+Automated invoice processing is the process of extracting key `accounts payable` fields from billing account documents. Extracted data includes line items from invoices integrated with your accounts payable (AP) workflows for reviews and payments. Historically, the accounts payable process is performed manually and, hence, very time consuming. Accurate extraction of key data from invoices is typically the first and one of the most critical steps in the invoice automation process.
 
 ::: moniker range=">=doc-intel-3.0.0"
 
@@ -183,82 +183,17 @@ See how data, including customer information, vendor details, and line items, is
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
+For a complete list of supported languages, *see* our [prebuilt model language support](../language-support/prebuilt.md) page.
 
 ## Field extraction
-The Document Intelligence invoice model `prebuilt-invoice` extracts the following fields.
 
-::: moniker range="doc-intel-3.1.0"
-
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Prebuilt_model/sample_analyze_invoices.py)
 
-::: moniker-end
-
-::: moniker range="doc-intel-4.0.0"
+:::moniker range=">=doc-intel-3.1.0"
 
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Prebuilt_model/sample_analyze_invoices.py)
+* For supported document extraction fields, refer to the [invoice model schema](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/invoice.md) page in our GitHub sample repository.
 
-::: moniker-end
+* The invoice key-value pairs and line items extracted are in the `documentResults` section of the JSON output.
 
-|Name| Type | Description | Standardized output |
-|:-----|:----|:----|:----|
-| CustomerName |string | Invoiced customer|Microsoft Corp|
-| CustomerId |string | Customer reference ID |CID-12345 |
-| PurchaseOrder |string | Purchase order reference number |PO-3333 |
-| InvoiceId |string | ID for this specific invoice (often Invoice Number) |INV-100 |
-| InvoiceDate |date |date the invoice was issued | mm-dd-yyyy|
-| DueDate |date |date payment for this invoice is due |mm-dd-yyyy|
-| VendorName |string | Vendor who created this invoice |CONTOSO|
-| VendorAddress |address|  Vendor mailing address| 123 456th St, New York, NY 10001 |
-| VendorAddressRecipient |string | Name associated with the VendorAddress |Contoso Headquarters  |
-| CustomerAddress |address | Mailing address for the Customer | 123 Other St, Redmond, WA, 98052|
-| CustomerAddressRecipient |string | Name associated with the CustomerAddress |Microsoft Corp |
-| BillingAddress |address | Explicit billing address for the customer | 123 Bill St., Redmond, WA, 98052 |
-| BillingAddressRecipient |string | Name associated with the BillingAddress |Microsoft Services |
-| ShippingAddress |address | Explicit shipping address for the customer | 123 Ship St., Redmond, WA, 98052|
-| ShippingAddressRecipient |string | Name associated with the ShippingAddress |Microsoft Delivery  |
-|Sub&#8203;Total| currency| Subtotal field identified on this invoice | $100.00 |
-| TotalDiscount | currency | The total discount applied to an invoice | $5.00 |
-| TotalTax | currency| Total tax field identified on this invoice | $10.00 |
-| InvoiceTotal | currency | Total new charges associated with this invoice | $10.00 |
-| AmountDue |  currency | Total Amount Due to the vendor | $610 |
-| PreviousUnpaidBalance | currency| Explicit previously unpaid balance | $500.00 |
-| RemittanceAddress |address| Explicit remittance or payment address for the customer |123 Remit St New York, NY, 10001   |
-| RemittanceAddressRecipient |string | Name associated with the RemittanceAddress |Contoso Billing |
-| ServiceAddress |address | Explicit service address or property address for the customer |123 Service St., Redmond WA, 98052 |
-| ServiceAddressRecipient |string | Name associated with the ServiceAddress |Microsoft Services  |
-| ServiceStartDate |date | First date for the service period (for example, a utility bill service period) | mm-dd-yyyy |
-| ServiceEndDate |date | End date for the service period (for example, a utility bill service period) | mm-dd-yyyy|
-| VendorTaxId |string | The taxpayer number associated with the vendor |123456-7 |
-|CustomerTaxId|string|The taxpayer number associated with the customer|765432-1|
-| PaymentTerm |string | The terms of payment for the invoice |Net 90 |
-| KVKNumber |string | A unique identifier for businesses registered in the Netherlands (NL-only)|12345678|
-| CurrencyCode |string | The currency code associated with the extracted amount | |
-| PaymentDetails | array | An array that holds Payment Option details such as `IBAN`,`SWIFT`, `BPayBillerCode(AU)`, `BPayReference(AU)` |  |
-|TaxDetails|array|An array that holds tax details like amount and rate||
-| TaxDetails | array | AN array that holds added tax information such as `CGST`, `IGST`, and `SGST`. This line item is currently only available for the Germany (`de`), Spain (`es`), Portugal (`pt`), and English Canada (`en-CA`) locales| |
-
-### Line items array
-
-Following are the line items extracted from an invoice in the JSON output response (the following output uses this [sample invoice](../media/sample-invoice.jpg):
-
-|Name| Type | Description | Value (standardized output) |
-|:-----|:----|:----|:----|
-| Amount | currency | The amount of the line item | $60.00 |
-| Date | date| Date corresponding to each line item. Often it's a date the line item was shipped | 3/4/2021|
-| Description | string | The text description for the invoice line item | Consulting service|
-| Quantity | number | The quantity for this invoice line item | 2 |
-| ProductCode | string| Product code, product number, or SKU associated with the specific line item | A123|
-| Tax | currency | Tax associated with each line item. Possible values include tax amount and tax Y/N | $6.00 |
-| TaxRate | string | Tax Rate associated with each line item. | 18%|
-| Unit | string| The unit of the line item, e.g,  kg, lb etc. | Hours|
-| UnitPrice | number | The net or gross price (depending on the gross invoice setting of the invoice) of one unit of this item | $30.00 |
-
-The invoice key-value pairs and line items extracted are in the `documentResults` section of the JSON output.
-
-:::moniker range=">=doc-intel-3.1.0"
 
 ### Key-value pairs
 
@@ -334,8 +269,8 @@ List all the detected payment options detected on the field.
 
 |Name| Type | Description | Text (line item #1) | Value (standardized output) |
 |:-----|:----|:----|:----| :----|
-| IBAN | string | Internal Bank Account Number | GB33BUKB20201555555555 | |
-| SWIFT | string | SWIFT code | BUKBGB22 | |
+| `IBAN` | string | Internal Bank Account Number | GB33BUKB20201555555555 | |
+| `SWIFT` | string | SWIFT code | BUKBGB22 | |
 | BankAccountNumber | string | Bank account number, a unique identifier for a bank account | 123456 | |
 | BPayBillerCode | string | Australian B-Pay Biller Code | 12345 | |
 | BPayReference | string | Australian B-Pay Reference Code | 98765432100 | |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "請求書に関するドキュメントの更新"
}
```

### Explanation
この修正は、Azureのドキュメント「請求書」に関連しており、以下の変更が行われました：

1. **日付の更新**: ドキュメントの日付が2024年8月7日から2024年10月16日に更新されました。

2. **自動請求書処理の説明修正**: 請求書処理の説明文が若干修正され、特に「accounts payable」というフレーズが強調されています。

3. **サポートされる言語の説明の簡素化**: 「サポートされている言語と地域」に関するセクションが修正され、リンクの表現がより明確にされています。

4. **フィールド抽出情報の整理**: 請求書モデルのフィールド抽出情報が簡素化され、特に「documentResults」セクションにおけるキーと値のペアやラインアイテムに関する詳しいデータが整理されています。

5. **不要な行の削除**: 73行の削除が行われ、冗長な情報が排除されることで、全体の可読性が向上しています。

これらの修正により、ドキュメントの内容がより明確になり、ユーザーが必要な情報を迅速に見つけやすくなっています。

## articles/ai-services/document-intelligence/prebuilt/marriage-certificate.md{#item-936798}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 10/03/2024
+ms.date: 10/16/2024
 ms.author: lajanuar
 monikerRange: '>=doc-intel-4.0.0'
 ---
@@ -68,35 +68,13 @@ To see how data extraction works for the marriage certificate card service, you
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
+For a complete list of supported languages, *see* our [prebuilt model language support](../language-support/prebuilt.md) page.
 
 ## Field extraction
 
-The following are the fields extracted from a marriage certificate  in the JSON output response.
-
-|Name| Type | Description | Example output |
-|:-----|:----|:----|:---:|
-| `Spouse1FirstName` | String | Spouse 1's first name| Wesley |
-| `Spouse1MiddleName` | String | Spouse 1's middle name| M. |
-| `Spouse1LastName` | String | Spouse 1's surname| Perry |
-| `Spouse1Age` | Integer | Spouse 1's age| 26 |
-| `Spouse1BirthDate` | Date | Spouse 1's birth date| Nov. 16, 1997 |
-| `Spouse1Address` | Address |Spouse 1's address| 4292 Don Jackson Lane, Bloomfield Township, Michigan 48302 |
-| `Spouse1BirthPlace`| String | Spouse 1's birth place| Michigan |
-| `Spouse2FirstName` | String | Spouse 2's first name| Beth |
-| `Spouse2MiddleName` | String | Spouse 2's middle name| R. |
-| `Spouse2LastName` | String | Spouse 2's surname| Mason |
-| `Spouse2Age` | Integer | Spouse 2's age| 23 |
-| `Spouse2BirthDate` | Date | Spouse 2's birth date| Jul. 22, 2000 |
-| `Spouse2Address` | Address |Spouse 2's address| 2671 Comfort Court, Madison, Wisconsin 53704 |
-| `Spouse2BirthPlace`| String | Spouse 2's birth place| Wisconsin |
-| `DocumentNumber`| String | Document number | 01976/202 |
-| `IssueDate` | Date | Issue date of the certificate | Oct. 10, 2023 |
-| `IssuePlace` | String | Issue place of the certificate | 2398 Echo Lane, Hastings, Michigan 49058 |
-| `MarriageDate`| Date | Marriage date | Oct. 10, 2023 |
-| `MarriagePlace` | String | Marriage place | 105 Coal Street, Galloway, Wisconsin 54432 |
-
-The marriage certificate key-value pairs and line items extracted are in the `documentResults` section of the JSON output.
+* For supported document extraction fields, refer to the [marriage certificate model schema](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/marriage-certificate.md) page in our GitHub sample repository.
+
+* The marriage certificate key-value pairs and line items extracted are in the `documentResults` section of the JSON output.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "婚姻証明書に関するドキュメントの更新"
}
```

### Explanation
この修正は、Azureのドキュメント「婚姻証明書」に関連しており、以下の変更が行われました：

1. **日付の更新**: ドキュメントの日付が2024年10月3日から2024年10月16日に更新されました。

2. **サポートされる言語の説明の簡素化**: 「サポートされる言語と地域」に関するセクションが修正され、リンクの表現がより明確にされています。

3. **フィールド抽出情報の整理**: 婚姻証明書から抽出されるフィールドに関する情報が若干修正され、具体的なフィールド名のリストが削除されています。代わりに、詳細なスキーマ情報をより簡潔に提供する形式に変更されています。

4. **情報の統一**: 抽出された婚姻証明書のキーと値のペアに関する文が整理され、情報の一致と整合性が向上しています。

これらの修正により、ドキュメントがより明確になり、ユーザーが必要な情報を迅速に見つけやすくなっています。

## articles/ai-services/document-intelligence/prebuilt/pay-stub.md{#item-7f747e}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: Document Intelligence pay stub model
+title: Document Intelligence payStub model
 titleSuffix: Azure AI services
 description: Automate compensation and earnings information from pay slips and stubs.
 author: laujan
@@ -13,15 +13,15 @@ monikerRange: '>=doc-intel-4.0.0'
 
 <!-- markdownlint-disable MD033 -->
 
-# Document Intelligence pay stub model
+# Document Intelligence payStub model
 
-The Document Intelligence pay stub model combines powerful Optical Character Recognition (OCR) capabilities with deep learning models to analyze and extract compensation and earnings data from pay slips. The API analyzes documents and files with payroll related information; extracts key information and returns a structured JSON data representation.
+The Document Intelligence payStub model combines powerful Optical Character Recognition (OCR) capabilities with deep learning models to analyze and extract compensation and earnings data from pay slips. The API analyzes documents and files with payroll related information; extracts key information and returns a structured JSON data representation.
 
 | Feature   | version| Model ID |
 |----------  |---------|--------|
-|Pay stub model|&bullet; v4.0:2024-07-31 (preview)|**`prebuilt-payStub.us`**|
+|payStub model|&bullet; v4.0:2024-07-31 (preview)|**`prebuilt-payStub.us`**|
 
-## Try pay stub data extraction
+## Try payStub data extraction
 
 Pay stubs are essential documents issued by employers to employees, providing earnings, deductions, and net pay information for a specific pay period. See how data is extracted using `prebuilt-payStub.us` model. You need the following resources:
 
@@ -45,28 +45,11 @@ Pay stubs are essential documents issued by employers to employees, providing ea
 
 ## Supported languages and locales
 
-*See* our [Language Support](../language-support/prebuilt.md) page for a complete list of supported languages.
+For a complete list of supported languages, *see* our [prebuilt model language support](../language-support/prebuilt.md) page.
 
 ## Field extractions
 
-|Name| Type | Description |Standardized output |
-|:-----|:----|:----|:----:|
-|`EmployeeAddress`|`address`|Address of the employee|123 Maple Street, Springfield, IL, 62701|
-|`EmployeeName`|`string`|Name of the employee|John A. Doe|
-|`EmployeeSSN`|`string`|Social security number of the employee|123-45-6789|
-|`EmployerAddress`|`address`|Address of the employer|456 Oak Avenue, Metropolis, NY, 10101|
-|`EmployerName`|`string`|Listed name of the employer|Contoso Corporation|
-|`PayDate`|`date`|Date of salary payment|Feb. 26, 2020|
-|`PayPeriodStartDate`|`date`|Start date of the pay period|Feb. 19, 2020|
-|`PayPeriodEndDate`|`date`|End date of the pay period|Feb. 25, 2020|
-|`CurrentPeriodGrossPay`|`number`|Gross pay of the current period|$744.10|
-|`YearToDateGrossPay`|`number`|Year-to-date gross pay|$2744.10|
-|`CurrentPeriodTaxes`|`number`|Taxes of the current period|$410.10|
-|`YearToDateTaxes`|`number`|Year-to-date taxes|$855.90|
-|`CurrentPeriodDeductions`|`number`|Deductions of the current period|$410.10|
-|`YearToDateDeductions`|`number`|Year-to-date deductions|$855.90|
-|`CurrentPeriodNetPay`|`number`|Net pay of the current period|$744.10|
-|`YearToDateNetPay`|`number`|Year-to-date net pay|$2744.10|
+For supported document extraction fields, refer to the [payStub model schema](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/pay-stub.md) page in our GitHub sample repository.
 
 ## Supported locales
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "給与明細書に関するドキュメントの更新"
}
```

### Explanation
この修正は、Azureのドキュメント「給与明細書」に関連しており、以下の変更が行われました：

1. **モデル名の表記変更**: ドキュメント内の「pay stub」という表現が「payStub」に統一されました。これにより、表記の一貫性が向上しています。

2. **日付の更新**: モデルのバージョン情報が含まれるセクションで、日付の表現に特段の変更はありませんが、タイトルや説明文で用語の整頓が行われています。

3. **サポートされる言語の説明の簡素化**: 「サポートされる言語と地域」に関するセクションが修正され、文の表現が簡潔になっています。

4. **フィールド抽出情報の整理**: 給与明細書から抽出されるフィールドの情報が修正され、特定のフィールドについては個別に名前や型、説明がリストアップされていた箇所が整理され、よりシンプルにリファレンスする形式に変更されています。

5. **リンクの追加**: 給与明細書モデルスキーマへのリンクが追加され、ユーザーがより詳細な情報に容易にアクセスできるようになっています。

これらの変更により、ドキュメントがより明確かつ一貫性のある内容となり、ユーザーが必要な情報を見つけやすくなっています。

## articles/ai-services/document-intelligence/prebuilt/receipt.md{#item-089054}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 05/23/2024
+ms.date: 10/16/2024
 ms.author: lajanuar
 ---
 
@@ -195,7 +195,7 @@ See how Document Intelligence extracts data, including time and date of transact
 
 ## Supported languages and locales
 
-*See* our [Language Support—prebuilt models](../language-support/prebuilt.md) page for a complete list of supported languages.
+For a complete list of supported languages, *see* our [prebuilt models language support](../language-support/prebuilt.md) page.
 
 ## Field extraction
 
@@ -223,177 +223,10 @@ See how Document Intelligence extracts data, including time and date of transact
 
 ::: moniker range=">=doc-intel-3.0.0"
 
- Document Intelligence v3.0 and later versions introduce several new features and capabilities. In addition to thermal receipts, the **Receipt** model supports single-page hotel receipt processing and tax detail extraction for all receipt types.
-
- Document Intelligence v4.0 and later versions introduces support for currency for all price-related fields for thermal and hotel receipts.
+For supported document extraction fields, refer to the [receipt model schema](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/receipt.md) page in our GitHub sample repository.
  
 ::: moniker-end
 
-::: moniker range="doc-intel-3.1.0"
-
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/v3.1(2023-07-31-GA)/Python(v3.1)/Prebuilt_model/sample_analyze_receipts.py)
-
-::: moniker-end
-
-::: moniker range="doc-intel-4.0.0"
-
-> [!div class="nextstepaction"]
-> [View samples on GitHub.](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/Python(v4.0)/Prebuilt_model/sample_analyze_receipts.py)
-
-::: moniker-end
-
-::: moniker range=">=doc-intel-3.0.0"
-
-### Receipt
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
-|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
-|`MerchantAddress`|`address`|Listed address of merchant|123 Main St. Redmond, Washington 98052|
-|`Total`|`number`|Full transaction total of receipt|$14.34|
-|`TransactionDate`|`date`|Date the receipt was issued|June 06, 2019|
-|`TransactionTime`|`time`|Time the receipt was issued|4:49 PM|
-|`Subtotal`|`number`|Subtotal of receipt, often before taxes are applied|$12.34|
-|`TotalTax`|`number`|Tax on receipt, often sales tax, or equivalent|$2.00|
-|`Tip`|`number`|Tip included by buyer|$1.00|
-|`Items`|`array`|||
-|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
-|`Items.*.TotalPrice`|`number`|Total price of line item|$999.00|
-|`Items.*.Description`|`string`|Item description|Surface Pro 6|
-|`Items.*.Quantity`|`number`|Quantity of each item|1|
-|`Items.*.Price`|`number`|Individual price of each item unit|$999.00|
-|`Items.*.ProductCode`|`string`|Product code, product number, or SKU associated with the specific line item|A123|
-|`Items.*.QuantityUnit`|`string`|Quantity unit of each item||
-|`TaxDetails`|`array`|||
-|`TaxDetails.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
-|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$999.00|
-
-### receipt.retailMeal
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
-|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
-|`MerchantAddress`|`address`|Listed address of merchant|123 Main St. Redmond, Washington 98052|
-|`Total`|`number`|Full transaction total of receipt|$14.34|
-|`TransactionDate`|`date`|Date the receipt was issued|June 06, 2019|
-|`TransactionTime`|`time`|Time the receipt was issued|4:49 PM|
-|`Subtotal`|`number`|Subtotal of receipt, often before taxes are applied|$12.34|
-|`TotalTax`|`number`|Tax on receipt, often sales tax, or equivalent|$2.00|
-|`Tip`|`number`|Tip included by buyer|$1.00|
-|`Items`|`array`|||
-|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
-|`Items.*.TotalPrice`|`number`|Total price of line item|$999.00|
-|`Items.*.Description`|`string`|Item description|Surface Pro 6|
-|`Items.*.Quantity`|`number`|Quantity of each item|1|
-|`Items.*.Price`|`number`|Individual price of each item unit|$999.00|
-|`Items.*.ProductCode`|`string`|Product code, product number, or SKU associated with the specific line item|A123|
-|`Items.*.QuantityUnit`|`string`|Quantity unit of each item||
-|`TaxDetails`|`array`|||
-|`TaxDetails.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
-|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$999.00|
-
-### receipt.creditCard
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
-|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
-|`MerchantAddress`|`address`|Listed address of merchant|123 Main St. Redmond, Washington 98052|
-|`Total`|`number`|Full transaction total of receipt|$14.34|
-|`TransactionDate`|`date`|Date the receipt was issued|June 06, 2019|
-|`TransactionTime`|`time`|Time the receipt was issued|4:49 PM|
-|`Subtotal`|`number`|Subtotal of receipt, often before taxes are applied|$12.34|
-|`TotalTax`|`number`|Tax on receipt, often sales tax, or equivalent|$2.00|
-|`Tip`|`number`|Tip included by buyer|$1.00|
-|`Items`|`array`|||
-|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
-|`Items.*.TotalPrice`|`number`|Total price of line item|$999.00|
-|`Items.*.Description`|`string`|Item description|Surface Pro 6|
-|`Items.*.Quantity`|`number`|Quantity of each item|1|
-|`Items.*.Price`|`number`|Individual price of each item unit|$999.00|
-|`Items.*.ProductCode`|`string`|Product code, product number, or SKU associated with the specific line item|A123|
-|`Items.*.QuantityUnit`|`string`|Quantity unit of each item||
-|`TaxDetails`|`array`|||
-|`TaxDetails.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
-|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$999.00|
-
-### receipt.gas
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
-|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
-|`MerchantAddress`|`address`|Listed address of merchant|123 Main St. Redmond, Washington 98052|
-|`Total`|`number`|Full transaction total of receipt|$14.34|
-|`TransactionDate`|`date`|Date the receipt was issued|June 06, 2019|
-|`TransactionTime`|`time`|Time the receipt was issued|4:49 PM|
-|`Subtotal`|`number`|Subtotal of receipt, often before taxes are applied|$12.34|
-|`TotalTax`|`number`|Tax on receipt, often sales tax, or equivalent|$2.00|
-|`Tip`|`number`|Tip included by buyer|$1.00|
-|`Items`|`array`|||
-|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
-|`Items.*.TotalPrice`|`number`|Total price of line item|$999.00|
-|`Items.*.Description`|`string`|Item description|Surface Pro 6|
-|`Items.*.Quantity`|`number`|Quantity of each item|1|
-|`Items.*.Price`|`number`|Individual price of each item unit|$999.00|
-|`Items.*.ProductCode`|`string`|Product code, product number, or SKU associated with the specific line item|A123|
-|`Items.*.QuantityUnit`|`string`|Quantity unit of each item||
-|`TaxDetails`|`array`|||
-|`TaxDetails.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
-|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$999.00|
-
-### receipt.parking
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
-|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-3210|
-|`MerchantAddress`|`address`|Listed address of merchant|123 Main St. Redmond, Washington 98052|
-|`Total`|`number`|Full transaction total of receipt|$14.34|
-|`TransactionDate`|`date`|Date the receipt was issued|June 06, 2019|
-|`TransactionTime`|`time`|Time the receipt was issued|4:49 PM|
-|`Subtotal`|`number`|Subtotal of receipt, often before taxes are applied|$12.34|
-|`TotalTax`|`number`|Tax on receipt, often sales tax, or equivalent|$2.00|
-|`Tip`|`number`|Tip included by buyer|$1.00|
-|`Items`|`array`|||
-|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
-|`Items.*.TotalPrice`|`number`|Total price of line item|$999.00|
-|`Items.*.Description`|`string`|Item description|Surface Pro 6|
-|`Items.*.Quantity`|`number`|Quantity of each item|1|
-|`Items.*.Price`|`number`|Individual price of each item unit|$999.00|
-|`Items.*.ProductCode`|`string`|Product code, product number, or SKU associated with the specific line item|A123|
-|`Items.*.QuantityUnit`|`string`|Quantity unit of each item||
-|`TaxDetails`|`array`|||
-|`TaxDetails.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
-|`TaxDetails.*.Amount`|`currency`|The amount of the tax detail|$999.00|
-
-### receipt.hotel
-
-| Field | Type | Description | Example |
-|:------|:-----|:------------|:--------|
-|`MerchantName`|`string`|Name of the merchant issuing the receipt|Contoso|
-|`MerchantPhoneNumber`|`phoneNumber`|Listed phone number of merchant|987-654-310|
-|`MerchantAddress`|`address`|Listed address of merchant|123 Main St. Redmond, Washington 98052|
-|`Total`|`number`|Full transaction total of receipt|$14.34|
-|`ArrivalDate`|`date`|Date of arrival|27Mar21|
-|`DepartureDate`|`date`|Date of departure|28Mar21|
-|`Currency`|`string`|Currency unit of receipt amounts (ISO 4217), or 'MIXED' if multiple values are found|USD|
-|`MerchantAliases`|`array`|||
-|`MerchantAliases.*`|`string`|Alternative name of merchant|Contoso (R)|
-|`Items`|`array`|||
-|`Items.*`|`object`|Extracted line item|1<br>Surface Pro 6<br>$999.00<br>$999.00|
-|`Items.*.TotalPrice`|`number`|Total price of line item|$999.00|
-|`Items.*.Description`|`string`|Item description|Room Charge|
-|`Items.*.Date`|`date`|Item date|27Mar21|
-|`Items.*.Category`|`string`|Item category|Room|
-
----
-
-::: moniker-end
-
 ::: moniker range="doc-intel-2.1.0"
 
 ### Migration guide and REST API v3.1
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "領収書に関するドキュメントの大幅な改訂"
}
```

### Explanation
この修正は、Azureのドキュメント「領収書」に対する大規模な更新を反映しており、以下の主要な変更が行われました：

1. **日付の更新**: 文書の日付が2024年5月23日から2024年10月16日に変更され、最新の情報を反映しています。

2. **内容の大幅な削減**: 領収書関連のすべてのフィールドの詳細およびモデルに関する記述が大幅に削除され、ドキュメントの内容が広範囲に簡素化されました。これは特に、複数のモデルバージョンに関する説明が削除され、特定のフィールドや説明がほとんどなくなったことを意味します。

3. **情報の整理とリンクの追加**: 残るセクションでは、領収書モデルスキーマへのリンクが追加され、ユーザーが必要なエクストラクションフィールドの情報を確認できるようになっています。具体的には、GitHubのサンプルリポジトリへのリンクが提供され、モデルのスキーマに関する最新情報を取得できるようになっています。

4. **文の表現の改良**: 言語サポートセクションが改訂されており、より明確で読みやすい表現になっています。

この修正により、ドキュメントはよりシンプルになり、特定の詳細情報はオンラインリソースへのリンクを通じて確認する必要があります。結果として、ユーザーは簡潔で更新された情報にアクセスできるようになりますが、特定の詳細が失われたため、既存ユーザーにとっては影響が大きい可能性があります。

## articles/ai-services/document-intelligence/toc.yml{#item-81aa7b}

<details>
<summary>Diff</summary>
````diff
@@ -322,8 +322,28 @@ items:
       href: /python/api/overview/azure/ai-documentintelligence-readme?view=azure-python-preview&preserve-view=true
   - name: Schema
     items:
+    - name: Bank check
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/bank-check.md
+    - name: Bank statement
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/bank-statement.md
+    - name: Business card (2023-07-31 GA)
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2023-07-31/business-card.md
+    - name: Contract
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/contract.md
+    - name: Credit card
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/credit-card.md
+    - name: Health insurance card
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/health-insurance-card.md
+    - name: ID document
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/id-document.md
+    - name: Invoice
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/invoice.md
     - name: Marriage certificate
-      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/marriage-certificate/2024-07-31-preview.json?context=/azure/ai-services/context/context
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/marriage-certificate.md
+    - name: Pay stub
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/pay-stub.md
+    - name: Receipt
+      href: https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-07-31-preview/receipt.md
 - name: Resources
   items:
   - name: Enterprise readiness
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメント目次の更新"
}
```

### Explanation
この修正は、Azureの「ドキュメントインテリジェンス」に関する目次ファイル（toc.yml）の更新を反映しています。主な変更点は以下の通りです：

1. **新しいリンクの追加**: 新たに多くの文書スキーマに関するリンクが追加されました。この変更により、以下のスキーマが目次に含まれるようになりました。
   - 銀行小切手
   - 銀行明細書
   - 名刺 (2023-07-31 GA)
   - 契約
   - クレジットカード
   - 健康保険証
   - IDドキュメント
   - 請求書
   - 結婚証明書
   - 給与明細書
   - 領収書

2. **結婚証明書リンクの更新**: 結婚証明書に関するリンクが、JSONファイル形式からマークダウン形式のファイルリンクに変更されました。これにより、ユーザーがより多くの詳細情報を得られるようになります。

この改訂により、ユーザーは新たに追加された多くのスキーマに関する情報に簡単にアクセスできるようになり、ドキュメント全体のナビゲーションが向上しています。全体として、目次の構成はより包括的で使いやすくなりました。

## articles/ai-studio/concepts/evaluation-approach-gen-ai.md{#item-ac9697}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Evaluation of generative AI applications
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Advancements in language models such as GPT-4 via Azure OpenAI Service offer great promise while coming with challenges related to responsible AI. If not designed carefully, systems built upon these models can perpetuate existing societal biases, promote misinformation, create manipulative content, or lead to a wide range of other negative impacts. Addressing these risks while maximizing benefits to users is possible with an iterative approach through four stages: [identify, measure, and mitigate, operate](https://aka.ms/LLM-RAI-devstages).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価アプローチに関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azureの「生成AIアプリケーションの評価」に関するドキュメント内のリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内で使われているインクルードタグのリンクが更新され、正しいパスが設定されました。この変更により、`feature-preview`に関する部分が適切なファイルに参照され、読者が最新の情報にアクセスできるようになります。

具体的には、元のリンクから新しいパスに変更され、ドキュメントが正確で一貫性のある内容を提供するための重要な更新です。この修正は軽微なものですが、文書の整合性を保つために必要な措置となっています。

## articles/ai-studio/concepts/evaluation-improvement-strategies.md{#item-9854b1}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Content risk mitigation strategies with Azure AI
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Mitigating content risks and poor quality generations presented by large language models (LLMs) such as the Azure OpenAI models requires an iterative, layered approach that includes experimentation and continual measurement. We recommend developing a mitigation plan that encompasses four layers of mitigations for the identified risks in the earlier stages of the process:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価改善戦略に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azureの「コンテンツリスク緩和戦略」に関するドキュメント内のリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内にあったインクルードタグのパスが変更され、正しいファイルへの参照が設定されました。この修正により、`feature-preview`に関する内容が適切なパスに更新され、読者が最新かつ正確な情報にアクセスできるようになります。

具体的には、元のリンクの形式から新しい相対パス形式に変わっており、ドキュメント全体の整合性が維持されています。この変更は軽微ですが、正確な文書を提供するためには重要な改善です。

## articles/ai-studio/concepts/evaluation-metrics-built-in.md{#item-d455bd}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: lgayhardt
 
 # Evaluation and monitoring metrics for generative AI
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Azure AI Studio allows you to evaluate single-turn or complex, multi-turn conversations where you ground the generative AI model in your specific data (also known as Retrieval Augmented Generation or RAG). You can also evaluate general single-turn query and response scenarios, where no context is used to ground your generative AI model (non-RAG). Currently, we support built-in metrics for the following task types:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価および監視指標に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azureの「生成AIの評価および監視指標」に関するドキュメント内のリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内のインクルードタグが変更され、これにより`feature-preview`に関する内容が新しい相対パスに更新されました。これにより、読者が正しいファイルにアクセスでき、最新の情報を参照できるようになります。

具体的には、元のリンクが相対パス形式に修正され、情報の整合性が向上しています。この修正は軽微ですが、ドキュメントの正確性と一貫性を保つために必要です。

## articles/ai-studio/concepts/fine-tuning-overview.md{#item-31b07b}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: sdgilley
 
 # Fine-tune models in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Fine-tuning retrains an existing large language model (LLM) by using example data. The result is a new, custom LLM that's optimized for the provided examples.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングの概要に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azureの「ファインチューニングモデル」の概要に関するドキュメント内のリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内のインクルードタグが修正され、`feature-preview`に関する内容のリンクが新しい相対パスに更新されました。この変更により、読者が正確で最新の情報にアクセスできるようになります。

具体的には、元のリンクからより適切な位置にある相対パス形式に変わっており、文書の整合性が向上しています。この改訂は軽微ではありますが、ドキュメントの正確性と利用可能性を維持するために重要です。

## articles/ai-studio/concepts/safety-evaluations-transparency-note.md{#item-a4dacb}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: lgayhardt
 
 # Transparency Note for Azure AI Studio safety evaluations
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 ## What is a Transparency Note
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "安全評価に関する透明性ノートの文書のリンク修正"
}
```

### Explanation
この修正は、Azureの「安全評価に関する透明性ノート」の文書内でのリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内のインクルードタグが変更され、`feature-preview`に関する内容のリンクが新しい相対パスに更新されました。この変更により、読者が正確で最新の情報にアクセスできるようになります。

具体的には、以前の相対パスから新しい相対パス形式に修正されており、これによって文書の整合性と正確性が高まっています。この更新は軽微なものでありますが、利用者が必要な情報を容易に取得できるようするために重要です。

## articles/ai-studio/concepts/vulnerability-management.md{#item-e37d54}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: Blackmist
 
 # Vulnerability management for Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Vulnerability management involves detecting, assessing, mitigating, and reporting on any security vulnerabilities that exist in an organization's systems and software. Vulnerability management is a shared responsibility between you and Microsoft.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "脆弱性管理に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azureの「脆弱性管理」に関する文書内でのリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内のインクルードタグが変更され、`feature-preview`に関するリンクが新しい相対パスに改訂されました。この修正により、読者は正確で最新の情報を効率的に参照できるようになります。

具体的には、元の相対パスから変更された新しい相対パス形式に修正され、文書の整合性と正確性が高まっています。この更新は軽微なものですが、利用者が必要な情報に容易にアクセスできるようにするための重要な改善です。

## articles/ai-studio/how-to/autoscale.md{#item-ad23fa}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: Blackmist
 
 # Autoscale Azure AI limits
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 This article provides guidance for how you can manage and increase quotas for resources with Azure AI Studio.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オートスケールに関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azureの「オートスケール」に関する文書内でのリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内の`feature-preview`に関するインクルードタグが、新しい相対パスに更新されました。この変更により、読者は正確で最新の情報を参照しやすくなります。

具体的には、以前の相対パス形式から修正された新しい相対パス形式に改訂されており、これによって文書の整合性と正確性が向上します。この更新は軽微なものでありますが、利用者が必要な情報を容易に取得できるようにするために重要な改善となります。

## articles/ai-studio/how-to/concept-data-privacy.md{#item-af88ce}

<details>
<summary>Diff</summary>
````diff
@@ -40,7 +40,7 @@ When you deploy a model from the model catalog (base or fine-tuned) by using ser
 
 The model processes your input prompts and generates outputs based on its functionality, as described in the model details. Your use of the model (along with the provider's accountability for the model and its outputs) is subject to the license terms for the model. Microsoft provides and manages the hosting infrastructure and API endpoint. The models hosted in this *model as a service* (MaaS) scenario are subject to Azure data, privacy, and security commitments. [Learn more about Azure compliance offerings applicable to Azure AI Studio](https://servicetrust.microsoft.com/DocumentPage/7adf2d9e-d7b5-4e71-bad8-713e6a183cf3).
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Microsoft acts as the data processor for prompts and outputs sent to, and generated by, a model deployed for pay-as-you-go inferencing (MaaS). Microsoft doesn't share these prompts and outputs with the model provider. Also, Microsoft doesn't use these prompts and outputs to train or improve Microsoft models, the model provider's models, or any third party's models.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データプライバシーに関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azureの「データプライバシー」に関する文書内でのリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内の`feature-preview`に関するインクルードタグが、新しい相対パス形式に更新されました。この変更により、読者はより正確で最新の情報にアクセスしやすくなります。

具体的には、以前の相対パスから新しい相対パスへの変更があり、文書の整合性が向上しています。この修正は軽微なものでありますが、利用者が必要な情報を迅速に入手できるようにするための重要な改善となります。

## articles/ai-studio/how-to/connections-add.md{#item-6f5a17}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: Blackmist
 
 # How to add a new connection in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn how to add a new connection in Azure AI Studio.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "接続の追加に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azure AI Studioにおける「新しい接続の追加」に関する文書内でのリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内に含まれている`feature-preview`に関するインクルードタグが、新しい相対パスに修正されました。この変更により、読者が最新かつ正確な情報にアクセスできるようになります。

具体的には、古い相対パスから新しい相対パスへの改訂が行われており、文書の整合性が向上しています。この更新は軽微なものでありますが、利用者が必要な情報を迅速に見つけやすくするために重要な改善となります。

## articles/ai-studio/how-to/costs-plan-manage.md{#item-6d5c73}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: Blackmist
 
 # Plan and manage costs for Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 This article describes how you plan for and manage costs for Azure AI Studio. First, you use the Azure pricing calculator to help plan for Azure AI Studio costs before you add any resources for the service to estimate costs. Next, as you add Azure resources, review the estimated costs.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのコスト管理に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azure AI Studioにおける「コストの計画と管理」に関する文書内でのリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内に含まれている`feature-preview`に関するインクルードタグが、新しい相対パス形式に変更されました。この修正により、読者が最新かつ正確な情報にアクセスしやすくなります。

具体的には、旧リンクから新リンクへの変更があり、文書の品質と利用者への情報提供が向上しています。この更新は軽微なものでありますが、Azure AI Studioの利用者が必要な情報を迅速に得られるようにするための重要な改善です。

## articles/ai-studio/how-to/create-azure-ai-hub-template.md{#item-c8813b}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: Blackmist
 
 # Use an Azure Resource Manager template to create an Azure AI Studio hub
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Use a [Microsoft Bicep](/azure/azure-resource-manager/bicep/overview) template to create a hub for Azure AI Studio. A template makes it easy to create resources as a single, coordinated operation. A Bicep template is a text document that defines the resources that are needed for a deployment. It might also specify deployment parameters. Parameters are used to provide input values when using the template.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Hubテンプレート作成に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azure AI Studioにおける「Azure AI Hubテンプレートの作成」に関する文書内でのリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内に含まれている`feature-preview`に関するインクルードタグが、新しい相対パスに変更されました。この変更により、読者が最新かつ正確な情報にアクセスできるようになります。

具体的には、変更されたリンクは記事の整合性を高め、ユーザーが必要な情報を簡単に見つけられるように改善されています。この更新は軽微なものであるものの、Azure AI Studioの利用において重要なリファレンス情報へのアクセスを強化します。

## articles/ai-studio/how-to/create-manage-compute-session.md{#item-6ed743}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: sdgilley
 
 # Create and manage prompt flow compute sessions in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 You need a compute session to run [prompt flows](prompt-flow.md). Use Azure AI Studio to create and manage prompt flow compute sessions.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのコンピュートセッション管理に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azure AI Studioにおける「プロンプトフローのコンピュートセッションの作成と管理」に関する文書内でのリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内の`feature-preview`に関するインクルードタグが、新しい相対パス形式に更新されました。この修正により、ユーザーはより正確で最新の情報にアクセスできるようになっています。

この更新は軽微なものでありながら、Azure AI Studioの利用者が必要な情報を迅速に見つけるための重要な改善となります。全体として、ドキュメントの整合性と使いやすさが向上しています。

## articles/ai-studio/how-to/create-manage-compute.md{#item-156c7f}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: sdgilley
 
 # How to create and manage compute instances in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn how to create a compute instance in Azure AI Studio. You can create a compute instance in the Azure AI Studio.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのコンピュートインスタンス作成に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、Azure AI Studioでの「コンピュートインスタンスの作成と管理」に関する文書内でのリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内の`feature-preview`に関するインクルードタグが、新しい相対パスに変更されました。この更新により、ユーザーが必要な情報にアクセスしやすくなります。

全体として、この更新はドキュメントの精度を向上させ、ユーザーがAzure AI Studioでのコンピュートインスタンスの作成方法を効果的に学ぶ手助けをします。軽微ではありますが、リンクの修正により情報の整合性が確保され、一貫したユーザー体験が提供されます。

## articles/ai-studio/how-to/create-secure-ai-hub.md{#item-adbe6e}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: Blackmist
 
 # How to create a secure Azure AI Studio hub and project with a managed virtual network
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 You can secure your Azure AI Studio hub, projects, and managed resources in a managed virtual network. With a managed virtual network, inbound access is only allowed through a private endpoint for your hub. Outbound access can be configured to allow either all outbound access, or only allowed outbound that you specify. For more information, see [Managed virtual network](configure-managed-network.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "セキュアなAzure AIスタジオハブ作成に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、「セキュアなAzure AIスタジオハブとプロジェクトの作成」に関する文書内でのリンクを更新しました。主な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内で使用されている`feature-preview`に関するインクルードタグが、新しい相対パス形式に変更されました。この修正により、ユーザーが最新の情報にアクセスしやすくなります。

この更新は、Azure AI Studioのユーザーがセキュリティ設定に関する正確な情報を取得できるようにするためのもので、全体的にドキュメントの整合性と使いやすさを向上させています。情報の更新は軽微ですが、ユーザー体験を向上させるために重要な役割を果たします。

## articles/ai-studio/how-to/data-add.md{#item-6139b1}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: fbsolo-ms1
 
 # How to add and manage data in your Azure AI Studio project
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 This article describes how to create and manage data in Azure AI Studio. Data can be used as a source for indexing in Azure AI Studio.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioプロジェクトへのデータ追加に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、「Azure AI Studioプロジェクトへのデータの追加と管理」に関する文書の中でのリンクを更新しました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内で使用されている`feature-preview`に関するインクルードタグが、新しい相対パス形式に変更されました。この変更により、関連情報へのアクセスが容易になります。

この修正は、Azure AI Studioを使用するユーザーに対して、データの追加と管理に関する正確で最新の情報を提供することを目的としています。リンクの更新は軽微ですが、全体のドキュメントの信頼性とユーザー体験を向上させるために重要です。

## articles/ai-studio/how-to/data-image-add.md{#item-a1f038}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: PatrickFarley
 
 # Azure OpenAI enterprise chat with images using GPT-4 Turbo with Vision
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Use this article to learn how to provide your own image data for GPT-4 Turbo with Vision, Azure OpenAI's vision model. GPT-4 Turbo with Vision enterprise chat allows the model to generate more customized and targeted answers using retrieval augmented generation based on your own images and image metadata.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4 Turbo with Visionを使用した画像データの追加に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、「GPT-4 Turbo with Visionを使用した企業向けチャットにおける画像データの追加」に関する文書内でのリンクを更新しました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: ドキュメント内で使われている`feature-preview`に関するインクルードタグが、最新の相対パス形式に変更されました。この更新により、ユーザーは関連情報によりアクセスしやすくなります。

この更新は、Azure OpenAIのビジョンモデルに関連する機能の使い方を分かりやすくすることを目的としており、特にGPT-4 Turboを活用した画像データの取り扱い方を説明しています。リンクの修正は軽微ですが、文書の正確性とユーザー体験の向上に寄与しています。

## articles/ai-studio/how-to/deploy-models-cohere-command.md{#item-3e97f4}

<details>
<summary>Diff</summary>
````diff
@@ -16,12 +16,12 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 
 # How to use Cohere Command chat models
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Cohere Command chat models and how to use them.
 The Cohere family of models includes various models optimized for different use cases, including chat completions, embeddings, and rerank. Cohere models are optimized for various use cases that include reasoning, summarization, and question answering.
 
-
+[!INCLUDE [models-preview](../includes/models-preview.md)]
 
 ::: zone pivot="programming-language-python"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cohere Commandチャットモデルの使用に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、「Cohere Commandチャットモデルの使用」に関する文書内でのリンクを更新し、内容を強化しました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグが新しい相対パス形式に更新されました。この変更により、関連情報へのアクセスが改善されます。

2. **新しいインクルードの追加**: `models-preview`というインクルードタグが新たに追加されました。これにより、Cohereモデルのプレビューに関する情報へのリンクが提供され、ユーザーは追加のリソースに簡単にアクセスできるようになります。

この更新は、Cohere Commandチャットモデルの機能と使用方法に関する情報をより明確にし、ユーザーが必要とする知識を得やすくすることを目的としています。リンクの修正は、文書の全体的な信頼性を向上させる重要な要素です。

## articles/ai-studio/how-to/deploy-models-cohere-embed.md{#item-eab662}

<details>
<summary>Diff</summary>
````diff
@@ -16,12 +16,12 @@ zone_pivot_groups: azure-ai-model-catalog-samples-embeddings
 
 # How to use Cohere Embed V3 models with Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Cohere Embed V3 models and how to use them with Azure AI Studio.
 The Cohere family of models includes various models optimized for different use cases, including chat completions, embeddings, and rerank. Cohere models are optimized for various use cases that include reasoning, summarization, and question answering.
 
-
+[!INCLUDE [models-preview](../includes/models-preview.md)]
 
 ::: zone pivot="programming-language-python"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cohere Embed V3モデルの使用に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、「Cohere Embed V3モデルの使用に関する」文書内でのリンクを更新し、情報を強化しました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグが新しい相対パス形式に更新され、ユーザーが関連情報によりアクセスしやすくなりました。

2. **新しいインクルードの追加**: `models-preview`というインクルードタグが新たに追加され、Cohereモデルのプレビューに関する情報へのリンクが提供され、ユーザーが追加のリソースに簡単にアクセスできるようになりました。

この更新は、Cohere Embed V3モデルの機能とAzure AI Studioでの使用方法に関する情報をより明確にすることを目的としており、ユーザーが必要とする知識を得るのを容易にします。文書のリンク修正は、全体的な内容の信頼性と使いやすさの向上に寄与しています。

## articles/ai-studio/how-to/deploy-models-cohere-rerank.md{#item-5047f8}

<details>
<summary>Diff</summary>
````diff
@@ -14,10 +14,12 @@ ms.custom: references_regions, build-2024
 
 # How to deploy Cohere Rerank models with Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about the Cohere Rerank models, how to use Azure AI Studio to deploy them as serverless APIs with pay-as-you-go token-based billing, and how to work with the deployed models.
 
+[!INCLUDE [models-preview](../includes/models-preview.md)]
+
 ## Cohere Rerank models
 
 Cohere offers two Rerank models in [Azure AI Studio](https://ai.azure.com). These models are available in the model catalog for deployment as serverless APIs:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Cohere Rerankモデルの使用に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、「Cohere Rerankモデルの使用に関する」文書内でのリンクと内容を更新し、情報を充実させました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグが新しい相対パス形式に更新され、ユーザーが関連情報により簡単にアクセスできるようになりました。

2. **新しいインクルードの追加**: `models-preview`という新しいインクルードタグが追加され、Cohereモデルのプレビューに関する情報が提供されるようになりました。

3. **新セクションの追加**: 新たに「Cohere Rerank models」というセクションが追加され、CohereのRerankモデルについての情報が明示化されました。このセクションでは、これらのモデルがAzure AI Studioでどのように利用できるかに関する説明が含まれています。

この更新は、Cohere Rerankモデルの機能とAzure AI Studioでの使用方法に関する情報を明確にし、ユーザーが必要な知識を得るのをサポートします。また、リンクと情報の更新によって、文書の全体的な信頼性が向上します。

## articles/ai-studio/how-to/deploy-models-jais.md{#item-0bd11f}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 
 # How to use Jais chat models
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Jais chat models and how to use them.
 JAIS 30b Chat is an autoregressive bi-lingual LLM for **Arabic** & **English**. The tuned versions use supervised fine-tuning (SFT). The model is fine-tuned with both Arabic and English prompt-response pairs. The fine-tuning datasets included a wide range of instructional data across various domains. The model covers a wide range of common tasks including question answering, code generation, and reasoning over textual content. To enhance performance in Arabic, the Core42 team developed an in-house Arabic dataset and translated some open-source English instructions into Arabic.
@@ -25,7 +25,7 @@ JAIS 30b Chat is an autoregressive bi-lingual LLM for **Arabic** & **English**.
 * **Input:** Model input is text only.
 * **Output:** Model generates text only.
 
-
+[!INCLUDE [models-preview](../includes/models-preview.md)]
 
 ::: zone pivot="programming-language-python"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JAISチャットモデルの使用に関するドキュメントのリンク修正"
}
```

### Explanation
この修正は、「JAISチャットモデルの使用に関する」文書のリンクと内容を更新し、情報をより明確にしました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグが新しい相対パス形式に更新され、ユーザーが必須情報によりアクセスできるようになりました。

2. **新しいインクルードの追加**: `models-preview`というインクルードタグが追加され、JAISモデルのプレビューに関する情報へのリンクが提供され、ユーザーが追加のリソースに簡単にアクセスできるようになります。

これらの変更は、JAISチャットモデルに関する情報をより充実させ、ユーザーが必要とする情報にアクセスしやすくすることを目的としています。全体として、文書の信頼性と使いやすさの向上に寄与しています。

## articles/ai-studio/how-to/deploy-models-jamba.md{#item-eeefca}

<details>
<summary>Diff</summary>
````diff
@@ -14,14 +14,16 @@ ms.custom: references_regions
 
 # How to deploy AI21's Jamba family models with Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn how to use Azure AI Studio to deploy AI21's Jamba family models as a serverless API with pay-as-you-go billing.
 
 The Jamba family models are AI21's production-grade Mamba-based large language model (LLM) which leverages AI21's hybrid Mamba-Transformer architecture. It's an instruction-tuned version of AI21's hybrid structured state space model (SSM) transformer Jamba model. The Jamba family models are built for reliable commercial use with respect to quality and performance.
 
-> [!TIP]
-> See our announcements of AI21's Jamba family models available now on Azure AI Model Catalog through [AI21's blog](https://aka.ms/ai21-jamba-1.5-large-announcement) and [Microsoft Tech Community Blog](https://aka.ms/ai21-jamba-1.5-large-microsoft-annnouncement).
+See our announcements of AI21's Jamba family models available now on Azure AI Model Catalog through [AI21's blog](https://aka.ms/ai21-jamba-1.5-large-announcement) and [Microsoft Tech Community Blog](https://aka.ms/ai21-jamba-1.5-large-microsoft-annnouncement).
+
+[!INCLUDE [models-preview](../includes/models-preview.md)]
+
 
 ## Deploy the Jamba family models as a serverless API
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI21のJambaモデルに関するドキュメントのリンクと内容の更新"
}
```

### Explanation
この修正は、AI21のJambaファミリーモデルの使用に関する文書のリンクと内容を更新し、詳細を充実させました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグが新しい相対パス形式に更新され、ユーザーが関連情報により簡単にアクセスできるようになりました。

2. **新しいインクルードの追加**: `models-preview`という新しいインクルードタグが追加され、Jambaモデルに関する追加情報へのリンクが提供されます。

3. **TIPセクションの変更**: TIPセクション内のマークダウン構文が削除され、テキストがより直接的に表示されるようになります。この変更により、情報の表示が向上します。

これらの更新は、AI21のJambaモデルに関する情報を明確にし、ユーザーが必要なリソースを探しやすくすることを目的としています。全体として、文書の整合性と使いやすさを向上させ、ユーザー体験を改善しています。

## articles/ai-studio/how-to/deploy-models-llama.md{#item-6274a7}

<details>
<summary>Diff</summary>
````diff
@@ -16,12 +16,13 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 
 # How to use the Meta Llama family of models
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about the Meta Llama family of models and how to use them. Meta Llama models and tools are a collection of pretrained and fine-tuned generative AI text and image reasoning models - ranging in scale from SLMs (1B, 3B Base and Instruct models) for on-device and edge inferencing - to mid-size LLMs (7B, 8B and 70B Base and Instruct models) and high performant models like Meta Llama 3.1 405B Instruct for synthetic data generation and distillation use cases.
 
-> [!TIP]
-> See our announcements of Meta's Llama 3.2 family models available now on Azure AI Model Catalog through [Meta's blog](https://aka.ms/llama-3.2-meta-announcement) and [Microsoft Tech Community Blog](https://aka.ms/llama-3.2-microsoft-announcement).
+See our announcements of Meta's Llama 3.2 family models available now on Azure AI Model Catalog through [Meta's blog](https://aka.ms/llama-3.2-meta-announcement) and [Microsoft Tech Community Blog](https://aka.ms/llama-3.2-microsoft-announcement).
+
+[!INCLUDE [models-preview](../includes/models-preview.md)]
 
 ::: zone pivot="programming-language-python"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Meta Llamaモデルに関するドキュメントのリンクの更新"
}
```

### Explanation
この修正は、Meta Llamaファミリーモデルに関する文書のリンクと表示内容の更新を行いました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグが新しい相対パスに変更され、より簡単に関連情報にアクセスできるようになります。

2. **新しいインクルードの追加**: `models-preview`という新しいインクルードタグが追加され、Llamaモデルに関連する追加情報へのリンクが提供されます。

3. **TIPセクションの変更**: TIPセクション内のマークダウン構文が削除され、より直接的な表現に変更されています。これにより、情報の視認性が向上します。

これらの更新により、Meta Llamaファミリーモデルに関する情報がより明瞭に整理され、ユーザーが必要なリソースにアクセスしやすくなります。全体として、文書の内容の整合性とユーザー体験の向上を図ることを目的としています。

## articles/ai-studio/how-to/deploy-models-mistral-nemo.md{#item-e7b729}

<details>
<summary>Diff</summary>
````diff
@@ -16,11 +16,12 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 
 # How to use Mistral Nemo chat model
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Mistral Nemo chat model and how to use them.
 Mistral AI offers two categories of models. Premium models including [Mistral Large and Mistral Small](deploy-models-mistral.md), available as serverless APIs with pay-as-you-go token-based billing. Open models including [Mistral Nemo](deploy-models-mistral-nemo.md), [Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01](deploy-models-mistral-open.md); available to also download and run on self-hosted managed endpoints.
 
+[!INCLUDE [models-preview](../includes/models-preview.md)]
 
 ::: zone pivot="programming-language-python"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistral Nemoチャットモデルに関するドキュメントのリンク更新"
}
```

### Explanation
この修正では、Mistral Nemoチャットモデルに関連する文書の情報とリンクを更新しました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグが新しい相対パスに変更され、関連情報へのアクセスが容易になりました。

2. **新しいインクルードの追加**: `models-preview`という新しいインクルードタグが追加され、Mistralモデルに関する追加情報へのリンクが提供されるようになりました。

3. **文章内容の更新**: Mistral AIが提供するモデルのカテゴリに関する説明が明確にされ、PremiumモデルとOpenモデルの情報が整理されています。

これらの変更は、ユーザーがMistral Nemoチャットモデルに関する情報をより理解しやすく、必要なリソースに簡単にアクセスできるようにすることを目的としています。全体として、文書の内容の整合性と快適さを向上させる修正となっています。

## articles/ai-studio/how-to/deploy-models-mistral-open.md{#item-84e005}

<details>
<summary>Diff</summary>
````diff
@@ -16,11 +16,12 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 
 # How to use Mistral-7B and Mixtral chat models
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Mistral-7B and Mixtral chat models and how to use them.
 Mistral AI offers two categories of models. Premium models including [Mistral Large and Mistral Small](deploy-models-mistral.md), available as serverless APIs with pay-as-you-go token-based billing. Open models including [Mistral Nemo](deploy-models-mistral-nemo.md), [Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01](deploy-models-mistral-open.md); available to also download and run on self-hosted managed endpoints.
 
+[!INCLUDE [models-preview](../includes/models-preview.md)]
 
 ::: zone pivot="programming-language-python"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "MistralおよびMixtralチャットモデルに関するドキュメントのリンク更新"
}
```

### Explanation
この修正では、Mistral-7BおよびMixtralチャットモデルに関する文書の情報とリンクを更新しました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグが新しい相対パスに変更され、ユーザーが関連情報により簡単にアクセスできるようになりました。

2. **新しいインクルードの追加**: `models-preview`という新しいインクルードタグが追加され、Mistralモデルに関する追加情報へのリンクが提供されるようになりました。

3. **文章内容の更新**: Mistral AIが提供するモデルのカテゴリに関する説明が整理され、PremiumモデルとOpenモデルの情報がクリアになりました。これにより、各モデルの利用方法がより明確に理解できるようになります。

これらの変更によって、MistralおよびMixtralチャットモデルに関する情報が向上し、ユーザーが必要なリソースに簡単にアクセスできるように設計されています。全体として、文書の整合性と使いやすさが改善されています。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -16,11 +16,12 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 
 # How to use Mistral premium chat models
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Mistral premium chat models and how to use them.
 Mistral AI offers two categories of models. Premium models including [Mistral Large and Mistral Small](deploy-models-mistral.md), available as serverless APIs with pay-as-you-go token-based billing. Open models including [Mistral Nemo](deploy-models-mistral-nemo.md), [Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01](deploy-models-mistral-open.md); available to also download and run on self-hosted managed endpoints.
 
+[!INCLUDE [models-preview](../includes/models-preview.md)]
 
 ::: zone pivot="programming-language-python"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralプレミアムチャットモデルに関するドキュメントのリンク更新"
}
```

### Explanation
この修正では、Mistralプレミアムチャットモデルに関する文書の情報とリンクを更新しました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグが新しい相対パスに変更され、関連情報へのアクセスが改善されました。

2. **新しいインクルードの追加**: `models-preview`という新しいインクルードタグが追加され、Mistralモデルに関する追加情報へのリンクが提供されるようになりました。

3. **文章内容の更新**: Mistral AIが提供するモデルのカテゴリについての説明が明確に整理され、PremiumモデルとOpenモデルが区別されています。これにより、各モデルの利用方法がよりわかりやすくなっています。

この変更により、Mistralプレミアムチャットモデルに関する情報が向上し、ユーザーが必要なリソースに容易にアクセスできるようになります。文書全体の整合性と使いやすさが改善されており、より効果的な学習体験を提供します。

## articles/ai-studio/how-to/deploy-models-openai.md{#item-de796b}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: msakande
 
 # How to deploy Azure OpenAI models with Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn to create Azure OpenAI model deployments in Azure AI Studio.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAIモデルに関するドキュメントのリンク更新"
}
```

### Explanation
この修正では、Azure OpenAIモデルに関する文書の内容とリンクを更新しました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグの相対パスが更新され、より正確なリンクが提供されるようになりました。これにより、ユーザーが最新の情報へのアクセスが容易になります。

2. **文章全体の再確認**: この変更により、本記事がAzure AI StudioでのAzure OpenAIモデルのデプロイに関する学習リソースとして、より一層使いやすくなっています。

この修正全体として、Azure OpenAIモデルのデプロイに関する情報の整合性とアクセス性が向上し、ユーザー体験が改善されています。

## articles/ai-studio/how-to/deploy-models-phi-3-5-vision.md{#item-8d6d7d}

<details>
<summary>Diff</summary>
````diff
@@ -16,12 +16,12 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 
 # How to use Phi-3.5 chat model with vision
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Phi-3.5 chat model with vision and how to use them.
 The Phi-3.5 small language models (SLMs) are a collection of instruction-tuned generative text models.
 
-
+[!INCLUDE [models-preview](../includes/models-preview.md)]
 
 ::: zone pivot="programming-language-python"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3.5ビジョン付きチャットモデルに関するドキュメントのリンク更新"
}
```

### Explanation
この修正では、Phi-3.5ビジョン付きチャットモデルに関する文書の情報とリンクを更新しました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグの相対パスが更新され、より正確なリンクが提供されるようになりました。これにより、関連情報へのアクセスが容易になります。

2. **新しいインクルードの追加**: `models-preview`という新しいインクルードタグが追加され、Phi-3.5モデルに関する追加情報へのリンクが提供されるようになりました。

3. **情報の整備**: Phi-3.5チャットモデルとその利用方法に関する説明が整えられ、読者がモデルの特性や使い方を明確に理解できるようになっています。

この変更により、Phi-3.5ビジョン付きチャットモデルに関する情報の整合性とアクセス性が向上し、ユーザー体験が改善されています。

## articles/ai-studio/how-to/deploy-models-phi-3-vision.md{#item-bd5aae}

<details>
<summary>Diff</summary>
````diff
@@ -16,12 +16,12 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 
 # How to use Phi-3 chat model with vision
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Phi-3 chat model with vision and how to use them.
 The Phi-3 family of small language models (SLMs) is a collection of instruction-tuned generative text models.
 
-
+[!INCLUDE [models-preview](../includes/models-preview.md)]
 
 ::: zone pivot="programming-language-python"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3ビジョン付きチャットモデルに関するドキュメントのリンク更新"
}
```

### Explanation
この修正では、Phi-3ビジョン付きチャットモデルについての文書の内容とリンクを更新しました。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関するインクルードタグの相対パスが修正され、最新情報がより確実に参照できるようになりました。

2. **新しいインクルードの追加**: `models-preview`という新しいインクルードタグが追加され、Phi-3モデルに関する追加情報へのアクセスが可能になりました。

3. **情報の整備**: Phi-3チャットモデルの特性や使用方法についての説明が調整され、文書の全体が整理されています。これにより、読者はモデルの利用方法をより明確に理解できるようになります。

この変更により、Phi-3ビジョン付きチャットモデルに関する情報の整合性が高まり、ユーザーが必要な情報にアクセスしやすくなっているため、全体のユーザー体験が改善されています。

## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -16,12 +16,12 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 
 # How to use Phi-3 family chat models
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Phi-3 family chat models and how to use them.
 The Phi-3 family of small language models (SLMs) is a collection of instruction-tuned generative text models.
 
-
+[!INCLUDE [models-preview](../includes/models-preview.md)]
 
 ::: zone pivot="programming-language-python"
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Phi-3ファミリーのチャットモデルに関するドキュメントのリンク更新"
}
```

### Explanation
この修正では、Phi-3ファミリーのチャットモデルに関連する文書の内容とリンクを更新しています。具体的な変更点は以下の通りです：

1. **インクルードのリンク修正**: `feature-preview`に関連するインクルードタグのパスが更新され、正確な情報へのリンクが提供されるようになりました。これにより、読者が最新の機能にアクセスしやすくなっています。

2. **新しいインクルードの追加**: `models-preview`という新たなインクルードタグが追加され、Phi-3モデルに関する詳細情報へのアクセスが可能になりました。

3. **情報の整備**: Phi-3ファミリーのチャットモデルとその使用法についての説明が整えられ、文書全体の明確性が向上しています。これにより、読者がモデルの特性や利用方法をより簡単に理解できるようになります。

この変更により、Phi-3ファミリーのチャットモデルに関する情報が整理され、ユーザーが必要な情報にアクセスしやすくなっているため、全体的なユーザー体験が向上しています。

## articles/ai-studio/how-to/deploy-models-serverless-availability.md{#item-143252}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,8 @@ ms.custom:
 
 In this article, you learn about which regions are available for each of the models supporting serverless API endpoint deployments.
 
+[!INCLUDE [models-preview](../includes/models-preview.md)]
+
 Certain models in the model catalog can be deployed as a serverless API with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. This deployment option doesn't require quota from your subscription.
 
 ## Region availability
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスモデルのデプロイに関する文書の更新"
}
```

### Explanation
この修正では、サーバーレスモデルのデプロイに関する文書の内容を更新しています。具体的な変更点は以下のとおりです：

1. **新しいインクルードの追加**: `models-preview`というインクルードタグが追加され、サーバーレスAPIデプロイメントをサポートする各モデルの詳細情報へのアクセスが可能になりました。これにより、読者は最新のモデル情報を簡単に参照できるようになります。

2. **コンテンツの整備**: サーバーレスAPIエンドポイントを用いたデプロイの特徴と利点についての説明が追加され、読者がこのデプロイオプションの利点をより理解しやすくなっています。特に、ホスティングを必要とせずにモデルをAPIとして利用できること、企業のセキュリティやコンプライアンスを保持できる点が強調されています。

この変更により、サーバーレスデプロイに関する情報が整理され、ユーザーが必要な情報により簡単にアクセスできるようになることで、全体的なユーザー体験が向上しています。

## articles/ai-studio/how-to/deploy-models-serverless-connect.md{#item-4faded}

<details>
<summary>Diff</summary>
````diff
@@ -19,6 +19,8 @@ ms.custom:
 
 In this article, you learn how to configure an existing serverless API endpoint in a different project or hub than the one that was used to create the deployment.
 
+[!INCLUDE [models-preview](../includes/models-preview.md)]
+
 [Certain models in the model catalog](deploy-models-serverless-availability.md) can be deployed as serverless APIs. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. This deployment option doesn't require quota from your subscription.
 
 The need to consume a serverless API endpoint in a different project or hub than the one that was used to create the deployment might arise in situations such as these:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスAPIエンドポイントに関する文書の更新"
}
```

### Explanation
この修正では、サーバーレスAPIエンドポイントの設定に関する文書を更新しています。具体的な変更点は以下の通りです：

1. **新しいインクルードの追加**: `models-preview`というインクルードタグが追加され、読者がサーバーレスAPIをサポートする最新のモデル情報に簡単にアクセスできるようになりました。

2. **情報の整理**: サーバーレスAPIとしてデプロイ可能なモデルに関する情報が強調され、従来のホスティングを必要とせずに、企業が必要とするセキュリティとコンプライアンスを保持した状態でモデルをAPIとして利用できる点が明確にされています。

この変更により、サーバーレスAPIエンドポイントに関する理解が深まり、特に異なるプロジェクトやハブでの利用ケースについての情報が提供されることで、ユーザーの役に立つ内容となっています。全体として、サーバーレスデプロイの利点が明確になり、読者が必要な情報に容易にアクセスできるようになっています。

## articles/ai-studio/how-to/deploy-models-serverless.md{#item-f8177f}

<details>
<summary>Diff</summary>
````diff
@@ -17,6 +17,8 @@ ms.custom: build-2024, serverless, devx-track-azurecli
 
 In this article, you learn how to deploy a model from the model catalog as a serverless API with pay-as-you-go token based billing.
 
+[!INCLUDE [models-preview](../includes/models-preview.md)]
+
 [Certain models in the model catalog](deploy-models-serverless-availability.md) can be deployed as a serverless API with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. This deployment option doesn't require quota from your subscription.
 
 This article uses a Meta Llama model deployment for illustration. However, you can use the same steps to deploy any of the [models in the model catalog that are available for serverless API deployment](deploy-models-serverless-availability.md).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "サーバーレスAPIデプロイに関する文書の更新"
}
```

### Explanation
この修正では、サーバーレスAPIとしてモデルをデプロイする方法に関する文書を更新しています。具体的な変更点は以下の通りです：

1. **新しいインクルードの追加**: `models-preview`というインクルードタグが追加され、サーバーレスAPIとして利用できるモデルの最新情報に容易にアクセスできるようになりました。この追加により、読者は最新のモデルに関して確認しやすくなっています。

2. **情報の明確化**: サーバーレスAPIデプロイの概要や利点が強調され、特に従量課金制でのトークンベースの課金方法が注目されています。また、特定のモデルがサーバーレスAPIとしてデプロイ可能であることが明記されており、企業が自社のニーズに合わせて安全にモデルを利用できることが強調されています。

これらの変更により、文章がよりわかりやすくなり、ユーザーが専門的な内容にアクセスしやすくなるとともに、サーバーレスAPIデプロイメントに関する理解が深まります。全体として、読者にとって有益な情報が提供され、実際のデプロイプロセスの手順を示すために、具体的なモデルの利用例も挙げられています。

## articles/ai-studio/how-to/deploy-models-timegen-1.md{#item-bd50f3}

<details>
<summary>Diff</summary>
````diff
@@ -15,13 +15,15 @@ ms.custom: references_regions, build-2024
 
 # How to deploy a TimeGEN-1 model with Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn how to use Azure AI Studio to deploy the TimeGEN-1 model as a serverless API with pay-as-you-go billing.
 You filter on the Nixtla collection to browse the TimeGEN-1 model in the [Model Catalog](model-catalog.md).
 
 The Nixtla TimeGEN-1 is a generative, pretrained forecasting and anomaly detection model for time series data. TimeGEN-1 can produce accurate forecasts for new time series without training, using only historical values and exogenous covariates as inputs.
 
+[!INCLUDE [models-preview](../includes/models-preview.md)]
+
 ## Deploy TimeGEN-1 as a serverless API
 
 Certain models in the model catalog can be deployed as a serverless API with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. This deployment option doesn't require quota from your subscription.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "TimeGEN-1モデルデプロイに関する文書の更新"
}
```

### Explanation
この修正では、TimeGEN-1モデルをAzure AI Studioを使ってデプロイする方法についての文書が更新されています。具体的な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`のインクルードタグが`feature-preview`に変更されており、関連情報のリンク先が更新されました。これにより、最新の情報を提供するための管理が向上しています。

2. **新しいインクルードの追加**: `models-preview`というインクルードタグが新たに追加され、サーバーレスAPIとして利用可能なモデルに関する最新情報にもアクセスできるようになりました。

3. **内容の明確化**: TimeGEN-1モデルの説明部分が明確化され、このモデルが時系列データに対する生成的かつ事前学習された予測および異常検出モデルであることが強調されており、使い方に関する具体的な価値が示されています。

4. **デプロイメントの説明**: 文章の一部に、特定のモデルがサーバーレスAPIとしてデプロイ可能であることが説明され、その利点が改めて述べられています。これにより、ユーザーは従量課金制でAPIとしてモデルを利用しやすくなり、セキュリティやコンプライアンスの保持についても安心して利用できることが強調されています。

全体として、これらの変更により、読者にとってTimeGEN-1モデルのデプロイに関する理解が深まり、実際の使用例や価値のある情報が提供されています。

## articles/ai-studio/how-to/develop/ai-template-get-started.md{#item-d71b59}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ author: sdgilley
 
 # How to get started with an AI template
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 Streamline your code-first development with prebuilt, task-specific Azure AI templates. Benefit from using the latest features and best practices from Microsoft Azure AI, with popular frameworks like LangChain, prompt flow, and Semantic Kernel in multiple languages.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIテンプレートの概要文書の更新"
}
```

### Explanation
この修正では、AIテンプレートを使った開発に関する入門文書が更新されています。具体的な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`というインクルードタグのパスが変更され、正しいリンク先に修正されました。これにより、最新の機能に関する情報が確実に参照できるようになり、ユーザーが必要とする情報へのアクセスが向上しています。

2. **内容の一貫性の向上**: 文書内の表現が微調整され、全体としてより読みやすく、一貫性のある内容になりました。具体的には、Azure AIのテンプレートを使用した開発の利点が引き続き強調されており、Microsoft Azure AIの最新機能やベストプラクティスについての説明が明確に表現されています。

これらの変更を通じて、ユーザーはAIテンプレートの効果的な使用方法を把握しやすくなり、開発作業を効率化するための信頼性の高い情報を得ることができます。全体的には、文書の内容がユーザーのニーズにより適したものになっています。

## articles/ai-studio/how-to/develop/connections-add-sdk.md{#item-14b519}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: Blackmist
 
 # Add a new connection using the Azure Machine Learning SDK
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 In this article, you learn how to add a new connection using the Azure Machine Learning SDK.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Machine Learning SDKを使用した新しい接続の追加に関する文書の更新"
}
```

### Explanation
この修正では、Azure Machine Learning SDKを用いた新しい接続の追加に関する文書が更新されています。具体的な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`のインクルードタグのパスが更新され、正しい参照先に変更されました。これにより、最新の機能に関する情報が正確に参照できるようになり、ユーザーの利便性が向上しています。

2. **内容の明確化**: 修正後の文書において、Azure Machine Learning SDKを使用した新しい接続の追加に関する説明が一貫した形で維持されています。この知識を得ることで、読者はこのSDKを利用して接続を作成する手順をより理解しやすくなります。

全体として、これらの小さな更新により文書がより正確で、使いやすいものになっており、ユーザーはAzure Machine Learning SDKを使用する際の具体的なガイダンスを容易に得られるようになっています。

## articles/ai-studio/how-to/develop/create-hub-project-sdk.md{#item-8c3e99}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ author: sdgilley
 
 # Create a hub using the Azure Machine Learning SDK and CLI
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 In this article, you learn how to create the following AI Studio resources using the Azure Machine Learning SDK and Azure CLI (with machine learning extension):
 - An Azure AI Studio hub
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Machine Learning SDKおよびCLIを使用したハブプロジェクト作成に関する文書の更新"
}
```

### Explanation
この修正では、Azure Machine Learning SDKおよびCLIを使用してハブを作成する方法に関する文書が更新されています。具体的な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`のインクルードタグのパスが改訂され、適切なリンク先に修正されました。この変更により、ユーザーは最新の機能に関する正確な情報をアクセスできるようになります。

2. **コンテンツの整備**: 文書内では、Azure SDKとCLIを利用して作成できるAIスタジオリソースについての説明が維持されています。具体的には、Azure AI Studioハブの作成について言及されており、読者が必要な知識を得る手助けとなります。

これらの修正により、文書がより正確で、ユーザーがAzure Machine Learningを使用して効果的に作業できるようサポートするものとなっています。全体として、ユーザーがハブプロジェクトを作成する際の理解を向上させるための小さな改善が行われています。

## articles/ai-studio/how-to/develop/evaluate-sdk.md{#item-9d5197}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: lgayhardt
 ---
 # Evaluate with the Azure AI Evaluation SDK
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 > [!NOTE]
 > Evaluate with the prompt flow has been retired and replaced with Azure AI Evaluate.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI評価SDKを使用した評価に関する文書の修正"
}
```

### Explanation
この修正では、Azure AI評価SDKを利用した評価に関する文書が更新され、いくつかの変更が行われています。具体的には以下の通りです：

1. **インクルードタグの修正**: `Feature preview`のインクルードタグのパスが変更され、正しい参照先に修正されました。これによって、ユーザーが最新の機能情報にアクセスしやすくなります。

2. **注意書きの追加**: 文書内に新たに注意書きが追加され、「プロンプトフローを用いた評価が廃止され、Azure AI Evaluateに置き換えられた」という重要な情報が伝えられています。この情報により、ユーザーは現在の機能についての理解を深めることができます。

これらの変更を通じて、文書はより正確で、ユーザーがAzure AI評価SDKの機能を効果的に活用できるように改善されています。全体として、利用者に対する適切な情報提供がなされており、ドキュメントの信頼性を向上させるための小さな修正が行われています。

## articles/ai-studio/how-to/develop/index-build-consume-sdk.md{#item-2ee880}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: sdgilley
 
 # How to build and consume an index using code
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 In this article, you learn how to create an index and consume it from code. To create an index locally, we use the `promptflow-rag` package. To create a remote index on the cloud, we use the `azure-ai-ml` package. We consume the indexes using `langchain`.
 
@@ -183,7 +183,7 @@ client.indexes.create_or_update(
 ```
 
 > [!NOTE]
-> Environment variables are intended for convenience in a local environment. However, if you register a local index created using environment variables, the index may not function as expected because secrets from environment variables won’t be transferred to the cloud index. To address this issue, you can use a `ConnectionConfig` or `connection_id` to create a local index before registering.
+> Environment variables are intended for convenience in a local environment. However, if you register a local index created using environment variables, the index may not function as expected because secrets from environment variables won't be transferred to the cloud index. To address this issue, you can use a `ConnectionConfig` or `connection_id` to create a local index before registering.
 
 ## Build an index (remotely) in your AI Studio project
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "インデックスの構築と消費に関する文書の更新"
}
```

### Explanation
この修正では、「コードを使用したインデックスの構築と消費」に関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`のインクルードタグが新しい参照先へ修正され、最新の情報が反映されるようになっています。これにより、ユーザーが正確で関連性のあるコンテンツにアクセスできるようになります。

2. **文書内の注意書きの修正**: 注意書きの文言が微調整され、特に環境変数の利用についての説明が明確になりました。環境変数がローカル環境での利用のためのものであることが強調され、ローカルインデックスの登録時に機能が期待通りに動作しない可能性についての警告が含まれています。また、`ConnectionConfig`や`connection_id`を使用してローカルインデックスを作成する方法が示唆されています。

これらの変更により、文書は利用者にとっての役立つ情報を提供し、インデックスの作成と消費に関するより良い理解を促進するように改善されています。全体的に言えば、ユーザーが求める知識の明瞭さと正確性が向上した小さな更新です。

## articles/ai-studio/how-to/develop/simulator-interaction-data.md{#item-c753d1}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: lgayhardt
 
 # Generate synthetic and simulated data for evaluation
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 Large language models are known for their few-shot and zero-shot learning abilities, allowing them to function with minimal data. However, this limited data availability impedes thorough evaluation and optimization when you might not have test datasets to evaluate the quality and effectiveness of your generative AI application. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "シミュレーションインタラクションデータに関する文書の修正"
}
```

### Explanation
この修正では、シミュレーションインタラクションデータに関する文書が更新されています。主な変更は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`に関するインクルードタグが新しいパスに修正され、より正確な情報が参照されるようになっています。この修正により、ユーザーは最新の機能情報にアクセスできるようになります。

2. **文書内容の明確化**: 更新された文書では、大規模言語モデル（LM）が持つ少数ショットおよびゼロショット学習能力について説明があり、データが限られている場合の評価と最適化の難しさが強調されています。特に、テストデータセットがない場合において、生成AIアプリケーションの品質と効果を評価する上での課題について触れています。

これにより、文書はデータシミュレーションと評価のプロセスにおける重要な情報を提供しており、ユーザーが生成AIアプリケーションの効果をよりよく理解し、評価するための助けとなる内容に改善されています。全体として、これは文書のクオリティを向上させるための小さな更新です。

## articles/ai-studio/how-to/develop/trace-local-sdk.md{#item-f7dfb5}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: sdgilley
 
 # How to trace your application with prompt flow SDK | Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 Tracing is a powerful tool that offers developers an in-depth understanding of the execution process of their generative AI applications such as agents, [AutoGen](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat), and retrieval augmented generation (RAG) use cases. It provides a detailed view of the execution flow, including the inputs and outputs of each node within the application. This essential information proves critical while debugging complex applications or optimizing performance.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトフローSDKによるアプリケーションのトレースに関する文書の更新"
}
```

### Explanation
この修正では、プロンプトフローSDKを用いてアプリケーションをトレースする方法についての文書が更新されています。主な変更は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`に関するインクルードタグが新しいパスに修正されており、最新の機能に関する情報が提供されるようになっています。これにより、開発者は新しい情報を容易に取得できるようになります。

2. **トレースの重要性の強調**: 文書内で、トレース機能が開発者にとってどれほど強力なツールであるかについての説明が強調されています。特に、エージェント、AutoGen、リトリーバル拡張生成（RAG）などの生成AIアプリケーションの実行プロセスの詳細な理解を提供する点が重要視されています。各ノードの入力や出力を含む実行フローの詳細が提供され、複雑なアプリケーションのデバッグやパフォーマンスの最適化において欠かせない情報であることが示されています。

このように、これらの変更により、文書はユーザーにとってより有用な情報を提供し、AIアプリケーションの開発と最適化を支援する内容として改善されています。全体的に見て、これは文書のクオリティを向上させる小さな更新です。

## articles/ai-studio/how-to/develop/trace-production-sdk.md{#item-8d5b4c}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: lgayhardt
 
 # Enable tracing and collect feedback for a flow deployment
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 After deploying a Generative AI APP in production, you might want to enhance your understanding and optimize performance. Trace data for each request, aggregated metrics, and user feedback play critical roles.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロダクションSDKによるトレーシングの有効化に関する文書の更新"
}
```

### Explanation
この修正では、プロダクションSDKを使用してトレーシングを有効にし、フローデプロイメントに関するフィードバックを収集する方法についての文書が更新されています。主な変更点は次の通りです：

1. **インクルードタグの修正**: `Feature preview`に関するインクルードタグが新しいパスに修正され、最新の情報にアクセスできるようになっています。この修正により、ユーザーが正確で最新の機能情報を取得することが可能です。

2. **トレーシングの重要性の説明強化**: 文書内では、生成AIアプリケーションをプロダクション環境にデプロイした後の理解を深め、パフォーマンスを最適化するために、トレースデータ、集約メトリック、およびユーザーフィードバックの重要性が強調されています。これにより、開発者はトレースデータを利用してアプリケーションの挙動を深く理解し、改善を行うための方向性を得ることができます。

これらの変更により、文書はユーザーにとってより価値のある情報を提供し、AIアプリケーションの性能最適化に役立つ内容として改善されています。全体として、これは文書のクオリティを向上させるための小さな更新です。

## articles/ai-studio/how-to/develop/vscode.md{#item-24bd97}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: sdgilley
 
 # Get started with Azure AI Studio projects in VS Code (Preview)
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 Azure AI Studio supports developing in VS Code - Desktop and Web. In each scenario, your VS Code instance is remotely connected to a prebuilt custom container running on a virtual machine, also known as a compute instance.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "VS CodeでのAzure AI Studioプロジェクトの開始に関する文書の更新"
}
```

### Explanation
この修正では、Azure AI StudioプロジェクトをVS Codeで開始する方法についての文書が更新されています。主な変更は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`に関連するインクルードタグが新しいパスに修正されており、最新の機能に関する情報を適切に参照できるようになっています。この修正により、ユーザーは新機能の情報を容易に取得できるようになります。

2. **VS Codeでの開発環境の説明**: 文書内では、Azure AI StudioがVS Code - デスクトップおよびウェブでの開発をサポートしていることが説明されています。具体的には、VS Codeインスタンスが仮想マシン上で稼働する事前構築されたカスタムコンテナにリモート接続される仕組みが強調されています。この点が明確に示されることで、開発者がVS Codeを使用したプロジェクトの環境設定や利用方法をより理解しやすくなっています。

これらの変更により、文書はユーザーにとってより有益な情報を提供し、VS Code環境でのAzure AI Studioの利用を促進する内容として改善されています。全体的に見て、これは文書のクオリティを向上させるための小さな更新です。

## articles/ai-studio/how-to/disaster-recovery.md{#item-963556}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.date: 5/21/2024
 
 # Customer enabled disaster recovery
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 To maximize your uptime, plan ahead to maintain business continuity and prepare for disaster recovery with Azure AI Studio. Since Azure AI Studio builds on [Azure Machine Learning architecture](/azure/machine-learning/concept-workspace), it's beneficial to reference the foundational architecture.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "顧客主導の災害復旧に関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioにおける顧客主導の災害復旧に関する文書が更新されています。主な変更点は次の通りです：

1. **インクルードタグの修正**: `Feature preview`に関するインクルードタグが新しいパスに修正されており、最新の情報を確実に参照できるようになっています。これにより、ユーザーは機能プレビューに関する正確な情報を簡単に得ることができます。

2. **ビジネス継続性と災害復旧の計画強調**: 文書では、ビジネスの継続性を維持し、災害復旧の準備をするためにAzure AI Studioを利用する重要性が強調されています。また、Azure AI StudioがAzure Machine Learningアーキテクチャに基づいているため、基盤となるアーキテクチャを参照することが有益であると指摘されています。これにより、開発者やユーザーは健全な災害復旧計画を策定する際の基本的な理解を深めることができます。

これらの変更により、文書はより実用的な情報を提供し、災害復旧に関する理解を促進する内容として改善されています。全体的に、この更新は文書のクオリティを向上させるための小さな調整と位置づけられます。

## articles/ai-studio/how-to/evaluate-generative-ai-app.md{#item-451c6e}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ author: lgayhardt
 
 # How to evaluate generative AI apps with Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 To thoroughly assess the performance of your generative AI application when applied to a substantial dataset, you can initiate an evaluation process. During this evaluation, your application is tested with the given dataset, and its performance will be quantitatively measured with both mathematical based metrics and AI-assisted metrics. This evaluation run provides you with comprehensive insights into the application's capabilities and limitations. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "生成AIアプリの評価に関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioを使用して生成AIアプリを評価する方法に関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`に関連するインクルードタグが新しいパスに修正されました。これにより、最新の機能プレビュー情報へのアクセスが改善され、ユーザーにとっての情報の一貫性が向上します。

2. **生成AIアプリの評価プロセスの説明強調**: 文書では、生成AIアプリケーションの性能を実際の大規模データセットに適用して評価するプロセスについて詳しく説明しています。この評価プロセスでは、与えられたデータセットを用いてアプリケーションがテストされ、数学的なメトリクスとAI支援のメトリクスを用いてその性能が定量的に測定されることが強調されています。これにより、ユーザーはアプリケーションの能力と限界に関する包括的な洞察を得ることができるため、評価結果はより実用的で理解しやすいものになります。

このような変更により、文書は生成AIを評価するための具体的で有益な情報を提供し、ユーザーが自らのアプリケーションの性能を正確に理解する手助けをする内容として改善されています。全体として、この更新は文書の質を高めるための小さな調整と見なされます。

## articles/ai-studio/how-to/evaluate-prompts-playground.md{#item-2b9a45}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Manually evaluate prompts in Azure AI Studio playground
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 When you get started with prompt engineering, you should test different inputs one at a time to evaluate the effectiveness of the prompt can be very time intensive. This is because it's important to check whether the content filters are working appropriately, whether the response is accurate, and more. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioプレイグラウンドにおけるプロンプト評価に関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioプレイグラウンドにおけるプロンプトの手動評価に関する文書が更新されています。主な変更点は次の通りです：

1. **インクルードタグの修正**: `Feature preview`に関連するインクルードタグのパスが新しいものに修正され、ユーザーが正確な情報にアクセスできるようになりました。この変更により、最新の機能プレビュー情報を効率的に取得できるようになります。

2. **プロンプトエンジニアリングに関する説明の強調**: 文書には、プロンプトエンジニアリングを開始する際に、異なる入力を一つずつテストしてプロンプトの効果を評価することが時間を要することが強調されています。具体的には、コンテンツフィルタが適切に機能しているか、応答が正確であるか、その他の要素を確認することの重要性が述べられています。この点は、ユーザーがプロンプトの評価プロセスを円滑に進めるための理解を深める助けになります。

このような変更は、文書がプロンプト評価に関する具体的で実践的なアドバイスを提供する内容として改善されており、ユーザーがより効果的にプロンプトを評価するためのサポートを強化しています。全体として、この更新は文書の質を向上させるための小さな調整と見なされます。

## articles/ai-studio/how-to/evaluate-results.md{#item-416e77}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # How to view evaluation results in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 The Azure AI Studio evaluation page is a versatile hub that not only allows you to visualize and assess your results but also serves as a control center for optimizing, troubleshooting, and selecting the ideal AI model for your deployment needs. It's a one-stop solution for data-driven decision-making and performance enhancement in your AI Studio projects. You can seamlessly access and interpret the results from various sources, including your flow, the playground quick test session, evaluation submission UI, and SDK. This flexibility ensures that you can interact with your results in a way that best suits your workflow and preferences.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioにおける評価結果の表示に関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioにおける評価結果の表示に関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`に関連するインクルードタグのパスが更新され、正しい場所から最新情報を取得できるように修正されました。これにより、ユーザーは機能プレビューに関する正確な情報にアクセスしやすくなります。

2. **評価結果の視覚化と最適化に関する説明強化**: 文書では、Azure AI Studioの評価ページが単なる結果の視覚化だけでなく、最適化、トラブルシューティング、理想的なAIモデルの選択のためのコントロールセンターとしての役割を果たすことが強調されています。このページは、データ駆動の意思決定やAI Studioプロジェクトでのパフォーマンス向上を一手に担うソリューションと位置付けられています。また、異なるソース（フロー、プレイグラウンドのクイックテストセッション、評価提出UI、SDKなど）から結果をシームレスにアクセスして解釈できることが説明されており、これによりユーザーは自分のワークフローや好みに最も適した方法で結果を利用できる柔軟性が提供されていることが記述されています。

このような変更は、文書がユーザーにとっての利便性を高め、効果的な意思決定をサポートする情報をしっかりと提供している内容として改善されています。全体として、この更新は文書の質を向上させるための小さな調整と見なされます。

## articles/ai-studio/how-to/fine-tune-model-llama.md{#item-2a42d8}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.custom: references_regions, build-2024
 
 # Fine-tune Meta Llama models in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Azure AI Studio lets you tailor large language models to your personal datasets by using a process known as *fine-tuning*. 
 
@@ -25,6 +25,8 @@ In this article, you learn how to fine-tune Meta Llama models in [Azure AI Studi
 
 The [Meta Llama family of large language models (LLMs)](./deploy-models-llama.md) is a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. The model family also includes fine-tuned versions optimized for dialogue use cases with Reinforcement Learning from Human Feedback (RLHF), called Llama-Instruct.
 
+[!INCLUDE [models-preview](../includes/models-preview.md)]
+
 ## Models
 # [Meta Llama 3.1](#tab/llama-three)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI StudioにおけるMeta Llamaモデルのファインチューニングに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI StudioにおけるMeta Llamaモデルのファインチューニングに関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`に関連するインクルードタグのパスが更新され、最新情報が正しく取得できるよう修正されました。これにより、ユーザーが機能プレビューに関連する情報にアクセスしやすくなります。

2. **モデルプレビューに関する新しいインクルードタグの追加**: 新たに`models-preview`に関するインクルードタグが追加され、ユーザーが利用可能なモデルに関する最新情報を67得ることができるようになりました。これにより、ファインチューニングの対象となるモデルについての理解を深めることが可能になります。

3. **文書内容の強化**: Meta Llamaモデルファミリーについて、事前学習済みおよびファインチューニング済みの生成テキストモデルが、パラメータのスケールに応じて7億から70億まで展開されていることが説明されており、特に対話用途に最適化されたモデルであるLlama-Instructについての情報が含まれています。

これらの修正は、文書の情報をより充実させ、ユーザーが実際の作業を進める上での参考になるよう整理されています。全体として、この更新は文書の質を向上させるための小さな調整と見なされます。

## articles/ai-studio/how-to/fine-tune-phi-3.md{#item-5b722a}

<details>
<summary>Diff</summary>
````diff
@@ -8,14 +8,19 @@ ms.custom:
 ms.topic: how-to
 ms.date: 7/16/2024
 ---
+
 # Fine-tune Phi-3 models in Azure AI Studio
 
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
+
 Azure AI Studio lets you tailor large language models to your personal datasets by using a process known as fine-tuning. Fine-tuning provides significant value by enabling customization and optimization for specific tasks and applications. It leads to improved performance, cost efficiency, reduced latency, and tailored outputs.
 
 In this article, you learn how to fine-tune Phi-3 family of small language models (SLMs) in Azure AI Studio as a service with pay-as you go billing.
 
 The Phi-3 family of SLMs is a collection of instruction-tuned generative text models.  Phi-3 models are the most capable and cost-effective small language models (SLMs) available, outperforming models of the same size and next size up across various language, reasoning, coding, and math benchmarks.
 
+[!INCLUDE [models-preview](../includes/models-preview.md)]
+
 ## [Phi-3-mini](#tab/phi-3-mini)
 
 Phi-3 Mini is a 3.8B parameters, lightweight, state-of-the-art open model built upon datasets used for Phi-2 - synthetic data and filtered websites - with a focus on high-quality, reasoning dense data. The model belongs to the Phi-3 model family, and the Mini version comes in two variants 4K and 128K which is the context length (in tokens) it can support.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI StudioにおけるPhi-3モデルのファインチューニングに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI StudioにおけるPhi-3モデルのファインチューニングに関する文書が更新されています。主な変更点は以下の通りです：

1. **新しいインクルードタグの追加**: 機能プレビューに関連する`feature-preview`のインクルードタグが新たに追加され、最新の機能情報を取得できるようにされました。これにより、ユーザーは利用可能な機能についての理解を深めることができます。

2. **モデルプレビューに関する新しいインクルードタグの追加**: 新たに`models-preview`に関連するインクルードタグが採用され、Phi-3モデルファミリーに関連する情報を簡単に取得しやすくなりました。

3. **ファインチューニングの利点の明確化**: 文書では、ファインチューニングがカスタマイズや特定のタスクへの最適化を可能にし、パフォーマンスの向上、コスト効率、レイテンシの短縮、カスタマイズされた出力が得られることが強調されています。

4. **Phi-3ファミリーの説明の充実**: Phi-3ファミリーの小型言語モデル（SLMs）が指示調整された生成テキストモデルのコレクションであり、同サイズや一つ上のサイズのモデルに対してさまざまな言語、推論、コーディング、数学のベンチマークで優れた性能を発揮することが述べられています。

5. **Phi-3 Miniモデルの特徴の追加**: Phi-3 Miniモデルに関する説明が追加され、3.8Bのパラメータを持つ軽量なオープンモデルであること、Phi-2で使用された合成データとフィルタリングされたウェブサイトを用いたデータセットに基づいていること、そして高品質で推論に密なデータに焦点を当てていることが紹介されています。

これらの修正により、文書はより詳細で、有用な情報を提供する内容として強化されています。全体として、この更新は文書の質を向上させるための小さな調整と見なされます。

## articles/ai-studio/how-to/flow-bulk-test-evaluation.md{#item-e60767}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Submit a batch run and evaluate a flow
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 To evaluate how well your flow performs with a large dataset, you can submit batch run and use an evaluation method in prompt flow.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フローのバルクテスト評価に関する文書の更新"
}
```

### Explanation
この修正では、フローにおけるバルクテスト評価に関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`に関連するインクルードタグのパスが修正され、これにより正しい情報を含む最新の機能プレビューが取得できるようになりました。具体的には、タグが`~/reusable-content/...`から`../includes/...`に変更されました。

2. **フローの性能評価の説明強化**: 文書には、大規模なデータセットでフローの性能を評価するためにバッチ実行を送信し、プロンプトフローにおける評価方法を使用することができる旨が明記されています。これにより、利用者がフローの能力をより具体的に評価する方法についての理解が深まります。

この更新は、フローのバルクテスト評価に必要な情報を明確にし、ユーザーが実際に実行する際の手助けとなる内容に整理されています。全体として、文書の品質向上を目的とした小さな調整と見なされます。

## articles/ai-studio/how-to/flow-deploy.md{#item-e7fc64}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Deploy a flow for real-time inference
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 After you build a prompt flow and test it properly, you might want to deploy it as an online endpoint. Deployments are hosted within an endpoint, and can receive data from clients and send responses back in real-time.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フローのデプロイに関する文書の更新"
}
```

### Explanation
この修正では、フローのリアルタイム推論のデプロイに関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`に関連するインクルードタグのパスが修正され、正しい情報を参照できるようになりました。これにより、タグが`~/reusable-content/...`から`../includes/...`に変更され、最新の機能プレビューが反映されるようになりました。

2. **フローのデプロイに関する説明の明確化**: 文書には、プロンプトフローを構築して適切にテストした後、オンラインエンドポイントとしてデプロイしたい場合について具体的に述べられています。デプロイメントはエンドポイント内にホストされ、クライアントからデータを受け取り、リアルタイムで応答を返すことができると説明されています。

この更新により、フローのデプロイ手順とその機能についての情報がより明確に伝わるようになり、ユーザーの理解を深めることを目的としています。全体として、この修正は文書の質を向上させるための小さな調整となります。

## articles/ai-studio/how-to/flow-develop-evaluation.md{#item-8514d1}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Develop an evaluation flow in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Evaluation flows are special types of flows that assess how well the outputs of a run align with specific criteria and goals.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価フローの開発に関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioにおける評価フローの開発に関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`に関連するインクルードタグのパスが修正され、正確な情報を参照できるようになりました。具体的には、タグが`~/reusable-content/...`から`../includes/...`に変更され、最新の機能プレビューが適切に反映されるようになっています。

2. **評価フローの説明の強化**: 文書では、評価フローが特別な種類のフローであり、実行の出力が特定の基準や目標とどのように一致するかを評価する目的を持っていることが明記されています。この説明により、ユーザーに評価フローの重要性や役割についての理解が深まります。

この更新により、評価フローの開発に必要な情報が明確化され、利用者が使用する際の指針が強化されています。全体として、文書の質を向上させるための小さな調整と位置付けられています。

## articles/ai-studio/how-to/flow-develop.md{#item-d1ac3e}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Develop a prompt flow
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Prompt flow is a development tool designed to streamline the entire development cycle of AI applications powered by Large Language Models (LLMs). Prompt flow provides a comprehensive solution that simplifies the process of prototyping, experimenting, iterating, and deploying your AI applications.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトフローの開発に関する文書の更新"
}
```

### Explanation
この修正では、プロンプトフローの開発に関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`に関連するインクルードタグのパスが更新されました。具体的には、タグが`~/reusable-content/...`から`../includes/...`に変更され、最新の機能プレビューが適切に参照されるようになっています。

2. **プロンプトフローの機能説明の明確化**: 文書では、プロンプトフローがLarge Language Models（LLMs）を利用したAIアプリケーションの開発サイクル全体を効率化するためのツールであることが示されています。プロンプトフローは、プロトタイピング、実験、反復、デプロイのプロセスを簡素化する包括的なソリューションを提供すると説明されています。

この更新によって、プロンプトフローの意義とその機能についての理解が深まり、利用者がその利点をよりよく活用できるようになります。全体として、文書の質を向上させるための小さな調整と見なされます。

## articles/ai-studio/how-to/flow-process-image.md{#item-1476f6}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: lgayhardt
 
 # Process images in prompt flow
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Multimodal Large Language Models (LLMs), which can process and interpret diverse forms of data inputs, present a powerful tool that can elevate the capabilities of language-only systems to new heights. Among the various data types, images are important for many real-world applications. The incorporation of image data into AI systems provides an essential layer of visual understanding. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトフローでの画像処理に関する文書の更新"
}
```

### Explanation
この修正では、プロンプトフローにおける画像処理に関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグの修正**: `Feature preview`に関連するインクルードタグのパスが修正され、正しい参照が確保されました。具体的には、タグが`~/reusable-content/...`から`../includes/...`に変更され、最新の機能プレビューが適切に表示されるようにされています。

2. **マルチモーダル大規模言語モデルの機能の強調**: 文書では、マルチモーダルな大規模言語モデル（LLMs）が多様なデータ入力を処理・解釈できる強力なツールであり、言語のみのシステムの能力を新たな高みへと引き上げる可能性があることが説明されています。特に、画像データの取り組みが多くの実世界のアプリケーションにおいて重要であり、AIシステムにおける視覚的理解の層を追加することの意義が強調されています。

この更新により、プロンプトフローを用いた画像処理の重要性と、大規模言語モデルを活用するための文書のクオリティが向上し、利用者がAI技術をより効果的に利用できるようになります。全体として、文書の質を高めるための小さな調整として位置付けられています。

## articles/ai-studio/how-to/flow-tune-prompts-using-variants.md{#item-882979}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Tune prompts using variants in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn how to use variants to tune prompts and evaluate the performance of different variants.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioにおけるバリアントを使用したプロンプト調整の文書更新"
}
```

### Explanation
この修正では、Azure AI Studioを使用したバリアントによるプロンプトの調整に関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグの修正**: 文書内の`Feature preview`に関連するインクルードタグのパスが修正されました。この修正により、参照が`~/reusable-content/...`から`../includes/...`に変更され、現在の機能プレビューが正確に表示されることが確保されています。

2. **バリアントによる調整の説明の強化**: 記事では、バリアントを使ってプロンプトを調整し、異なるバリアントのパフォーマンスを評価する方法が紹介されています。この内容は、読者がプロンプトを最適化する技法を具体的に学ぶ手助けとなります。

この更新により、バリアントを利用したプロンプト調整の方法が明確にされ、利用者がより効果的にAzure AI Studioを活用できるようになります。全体として、この文書は小さな調整によって品質が向上したと考えられます。

## articles/ai-studio/how-to/groundedness.md{#item-e3c37c}

<details>
<summary>Diff</summary>
````diff
@@ -13,7 +13,7 @@ ms.author: pafarley
 
 # Groundedness detection (preview)
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Learn how to use Azure AI Content Safety Groundedness detection to check whether the text responses of large language models (LLMs) are grounded in the source materials provided by the users.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "グラウンデッドネス検出に関する文書の更新"
}
```

### Explanation
この修正では、Azure AIのコンテンツ安全性におけるグラウンデッドネス検出に関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`に関連するインクルードタグのパスが修正され、正しい参照が確保されました。具体的には、タグのパスが`~/reusable-content/...`から`../includes/...`に変更され、機能プレビューが適切に表示されるようにしています。

2. **グラウンデッドネス検出の説明**: 記事では、ユーザーが提供するソース資料に基づいて、巨大な言語モデル（LLMs）のテキスト応答がどの程度グラウンドされているかをチェックする方法について説明しています。この機能は、AIの応答の信頼性を確認するために重要です。

この更新により、グラウンデッドネス検出の利用方法が明確にされ、利用者がAzure AIを用いたコンテンツ評価をより効果的に行えるようになります。この修正は、文書の内容を改善するための小さな調整として位置付けられます。

## articles/ai-studio/how-to/index-add.md{#item-1b013b}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: ssalgadodev
 
 # How to build and consume vector indexes in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn how to create and use a vector index for performing [Retrieval Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioにおけるベクターインデックスの構築と利用に関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioにおけるベクターインデックスの構築と利用についての文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内に存在する`Feature preview`に関連するインクルードタグのパスが修正されました。この変更により、参照が`~/reusable-content/...`から`../includes/...`に変更され、機能プレビューが正確に表示されるようにされています。

2. **ベクターインデックスの利用方法の説明**: 記事では、ベクターインデックスを作成し、Retrieval Augmented Generation (RAG)を実行する方法について紹介しています。この情報は、読者がAzure AI Studioを利用してより効果的な検索と生成を行う際に役立ちます。

この更新により、ベクターインデックスの概念と使用方法が明確にされ、ユーザーがAzure AIの機能を最大限に活用できるようになっています。全体として、文書の内容が小さな調整によって改善されたと考えられます。

## articles/ai-studio/how-to/model-benchmarks.md{#item-82de8e}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: sdgilley
 
 # Model benchmarks in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In Azure AI Studio, you can compare benchmarks across models and datasets available in the industry to decide which one meets your business scenario. You can find model benchmarks under **Get started** on the left menu in Azure AI Studio.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioにおけるモデルベンチマークに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioにおけるモデルベンチマークに関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内にある`Feature preview`に関連するインクルードタグのパスが修正されました。これにより、タグが`~/reusable-content/...`から`../includes/...`に変更され、機能プレビューが適切に表示されるようになっています。

2. **モデルベンチマークの説明**: 記事では、Azure AI Studioで利用できるモデルとデータセットのベンチマークを比較し、ビジネスシナリオに最適なモデルを選択する方法について解説しています。また、ユーザーがAzure AI Studioでモデルベンチマークを見つける場所として、左側のメニューの**Get started**セクションが案内されています。

この更新により、モデルベンチマークの活用法がより明確になり、ユーザーが具体的な業務ニーズに適した選択をしやすくなっています。文書全体が小さな調整を通じて改善されていることが見受けられます。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -17,13 +17,13 @@ author: ssalgadodev
 
 # Model catalog and collections in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 The model catalog in Azure AI Studio is the hub to discover and use a wide range of models for building generative AI applications. The model catalog features hundreds of models across model providers such as Azure OpenAI Service, Mistral, Meta, Cohere, NVIDIA, and Hugging Face, including models that Microsoft trained. Models from providers other than Microsoft are Non-Microsoft Products as defined in [Microsoft Product Terms](https://www.microsoft.com/licensing/terms/welcome/welcomepage) and are subject to the terms provided with the models.
 
 ## Model collections
 
-The model catalog organizes models into three types collections:
+The model catalog organizes models into three collections:
 
 * **Curated by Azure AI**: The most popular non-Microsoft open-weight and proprietary models packaged and optimized to work seamlessly on the Azure AI platform. Use of these models is subject to the model providers' license terms. When you deploy these models in Azure AI Studio, their availability is subject to the applicable [Azure service-level agreement (SLA)](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services), and Microsoft provides support for deployment problems.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのモデルカタログに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioにおけるモデルカタログの概要に関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`に関するインクルードタグのパスが修正され、正確な参照に更新されています。これにより、参照が`~/reusable-content/...`から`../includes/...`に変更され、機能プレビューが適切に表示されるようになっています。

2. **文言の明確化**: モデルカタログがモデルを「三つのタイプのコレクション」に整理するという表現が、「三つのコレクション」に簡略化されました。この変更により、文章がより明確になり、読みやすさが向上しています。

3. **モデルカタログの説明**: Azure AI Studioのモデルカタログは、生成AIアプリケーションを構築するための広範なモデルを発見・利用するための中心となるものであり、多数のモデルがさまざまなプロバイダーから提供されています。従って、文書ではMicrosoft以外のプロバイダーについても言及され、それぞれのライセンス条件が適用されることが明示されています。

この更新により、モデルカタログの機能と構成がより視覚的かつ理解しやすくなり、ユーザーがAzure AI Studioを使用してモデルをより効果的に活用できるようになっています。文書全体として、情報の正確性と可読性が向上しています。

## articles/ai-studio/how-to/monitor-quality-safety.md{#item-61adb3}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: msakande
 
 # Monitor quality and token usage of deployed prompt flow applications
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Monitoring applications that are deployed to production is an essential part of the generative AI application lifecycle. Changes in data and consumer behavior can influence your application over time, resulting in outdated systems that negatively affect business outcomes and expose organizations to compliance, economic, and reputation risks. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイされたプロンプトフローアプリケーションの品質とトークン使用量の監視に関する文書の更新"
}
```

### Explanation
この修正では、デプロイされたプロンプトフローアプリケーションの品質およびトークン使用量の監視に関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`に関するインクルードタグのパスが修正されました。新しいパスは`../includes/feature-preview.md`に変更されており、これにより正確な機能プレビューの表示が可能になっています。

2. **監視の重要性の強調**: 文書は、プロダクションにデプロイされたアプリケーションの監視が生成AIアプリケーションライフサイクルの重要な部分であることを強調しています。データの変化や消費者行動の変化がアプリケーションに与える影響についての説明があり、古くなったシステムがビジネス結果に悪影響を与え、コンプライアンス、経済、評判のリスクを露呈する可能性があることが述べられています。

この更新により、アプリケーションの監視の重要性とその影響がより明確に伝わるようになり、読者に将来のリスクを認識させる内容となっています。また、インクルードタグの正確性も改善され、コンテンツの整合性が向上しています。

## articles/ai-studio/how-to/prompt-flow-tools/azure-open-ai-gpt-4v-tool.md{#item-053d0d}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: lgayhardt
 
 # Azure OpenAI GPT-4 Turbo with Vision tool in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 The prompt flow Azure OpenAI GPT-4 Turbo with Vision tool enables you to use your Azure OpenAI GPT-4 Turbo with Vision model deployment to analyze images and provide textual responses to questions about them.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI StudioにおけるGPT-4 Turbo with Visionツールに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studio内のAzure OpenAI GPT-4 Turbo with Visionツールに関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`に関するインクルードタグのパスが修正され、正しいパスである`../../includes/feature-preview.md`に更新されました。これにより、機能プレビューが正確に参照されるようになっています。

2. **ツールの機能説明**: 更新された文書では、GPT-4 Turbo with Visionツールの機能が簡潔に説明されており、このツールがAzure OpenAI GPT-4 Turbo with Visionモデルを使って画像を分析し、それに関する質問に対してテキスト応答を提供することができると述べられています。

この変更により、ユーザーに対してツールの利用方法がより明確になり、機能の理解を助ける内容となっています。また、インクルードタグの修正によって、文書内のコンテンツの整合性が向上しています。

## articles/ai-studio/how-to/prompt-flow-tools/content-safety-tool.md{#item-09b048}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Content safety tool for flows in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 The prompt flow Content Safety tool enables you to use Azure AI Content Safety in Azure AI Studio.
 
@@ -26,7 +26,7 @@ Azure AI Content Safety is a content moderation service that helps detect harmfu
 
 To create an Azure Content Safety connection:
 
-1. Sign in to [Azure AI Studio](https://studio.azureml.net/).
+1. Sign in to [Azure AI Studio](https://ai.azure.com/).
 1. Go to **Project settings** > **Connections**.
 1. Select **+ New connection**.
 1. Complete all steps in the **Create a new connection** dialog. You can use an Azure AI Studio hub or Azure AI Content Safety resource. We recommend that you use a hub that supports multiple Azure AI services.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのコンテンツセーフティツールに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioにおけるコンテンツセーフティツールに関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`に関するインクルードタグのパスが修正され、正しいパスである`../../includes/feature-preview.md`に更新されました。この変更により、機能プレビューが適切に参照され、文書の整合性が向上しています。

2. **サインインURLの変更**: ユーザーがAzure AI StudioにサインインするためのURLが、`https://studio.azureml.net/`から`https://ai.azure.com/`に変更されました。この修正は最新のURLに対応するもので、ユーザーが正しいプラットフォームにアクセスできるようになります。

3. **手順の明確化**: Azure Content Safety接続を作成する手順が提供されており、ステップの最初にあるサインイン方法が変更された点が強調されています。このことで、ユーザーが正確な手順に従うことで、コンテンツセーフティツールを効率よく利用できるようになります。

これらの変更により、文書の精度とユーザーの利便性が向上し、Azure AI Studioにおけるコンテンツセーフティツールの使用方法がより明確に伝わる内容となっています。

## articles/ai-studio/how-to/prompt-flow-tools/embedding-tool.md{#item-81420c}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Embedding tool for flows in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 The prompt flow Embedding tool enables you to convert text into dense vector representations for various natural language processing tasks.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioの埋め込みツールに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioにおける埋め込みツールに関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`に関するインクルードタグのパスが修正され、正しいパスである`../../includes/feature-preview.md`に更新されました。この変更により、機能プレビューが適切に参照され、内容の整合性が確保されています。

2. **ツールの機能説明**: 更新された文書では、埋め込みツールの機能が明確に説明されており、テキストをさまざまな自然言語処理タスク用の密なベクトル表現に変換することができると述べられています。

これらの変更により、文書の正確性とユーザーに対する情報の明確さが向上し、Azure AI Studioにおける埋め込みツールの利用方法がより理解しやすくなっています。

## articles/ai-studio/how-to/prompt-flow-tools/index-lookup-tool.md{#item-cad66d}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: lgayhardt
 
 # Index Lookup tool for Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 The prompt flow Index Lookup tool enables the use of common vector indices (such as Azure AI Search, Faiss, and Pinecone) for retrieval augmented generation in prompt flow. The tool automatically detects the indices in the workspace and allows the selection of the index to be used in the flow.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのインデックスルックアップツールに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioにおけるインデックスルックアップツールに関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`に関するインクルードタグのパスが修正され、正しいパスである`../../includes/feature-preview.md`に更新されました。これにより、機能プレビューが適切に参照され、文書全体の整合性が向上します。

2. **ツールの機能説明の強化**: 更新された文書において、インデックスルックアップツールの機能が詳細に説明されており、Azure AI Search、Faiss、Pineconeなどの一般的なベクトルインデックスを利用して、プロンプトフロー内でのリトリーバル・拡張生成をサポートすることが述べられています。また、このツールはワークスペース内のインデックスを自動的に検出し、使用するインデックスの選択を可能にする機能を持っていることも強調されています。

これらの変更により、文書の精度とユーザーに対する情報の明確さが向上し、Azure AI Studioにおけるインデックスルックアップツールの利用方法がより理解しやすくなっています。

## articles/ai-studio/how-to/prompt-flow-tools/llm-tool.md{#item-6691f4}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # LLM tool for flows in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 To use large language models (LLMs) for natural language processing, you use the prompt flow LLM tool.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI StudioのLLMツールに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI StudioにおけるLLM（大規模言語モデル）ツールに関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`に関するインクルードタグのパスが修正され、正しいパスである`../../includes/feature-preview.md`に更新されました。この修正により、機能プレビューが正確に参照され、文書の整合性が向上します。

2. **ツールの機能説明の補強**: 更新内容には、自然言語処理のために大規模言語モデル（LLM）を使用する際に必要なプロンプトフローLLMツールの利用目的が簡潔に説明されています。これにより、ユーザーがこのツールの役割をより明確に理解できるようになります。

これらの変更により、文書の正確性が向上し、ユーザーに対する情報の明瞭さが増し、Azure AI StudioにおけるLLMツールの利用方法がより分かりやすくなっています。

## articles/ai-studio/how-to/prompt-flow-tools/prompt-flow-tools-overview.md{#item-fd7471}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: lgayhardt
 
 # Overview of prompt flow tools in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 The following table provides an index of tools in prompt flow.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのプロンプトフローツールに関する概要文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioにおけるプロンプトフローツールの概要文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`に関連するインクルードタグのパスが変更され、正しいパスである`../../includes/feature-preview.md`に更新されました。この修正により、機能プレビューの内容が正確に参照され、文書全体の一貫性が確保されます。

2. **ツールインデックスの紹介**: 更新された文書には、プロンプトフロー内のツールのインデックスを提供するテーブルが紹介されています。このテーブルは、ユーザーが利用可能な各ツールについての情報を迅速に参照できるように設計されています。

これらの改善により、文書の正確性とユーザーへの情報提供の明瞭さが強化され、Azure AI Studioにおけるプロンプトフローツールの利用がより円滑になることが期待されます。

## articles/ai-studio/how-to/prompt-flow-tools/prompt-tool.md{#item-c6a9a0}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Prompt tool for flows in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 The prompt flow Prompt tool offers a collection of textual templates that serve as a starting point for creating prompts. These templates, based on the [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) template engine, facilitate the definition of prompts. The tool proves useful when prompt tuning is required before the prompts are fed into the large language model (LLM) in the prompt flow.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのプロンプトツールに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioのプロンプトツールに関する文書が更新されています。主な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`関連のインクルードタグのパスが修正され、正しいパスである`../../includes/feature-preview.md`に更新されました。これにより、機能プレビューの情報が正確に参照され、文書の整合性が向上します。

2. **プロンプトツールの説明強化**: 更新されたセクションでは、プロンプトフローツールが提供するテキストテンプレートのコレクションが説明されています。これらのテンプレートは、[Jinja](https://jinja.palletsprojects.com/en/3.1.x/) テンプレートエンジンに基づいており、プロンプトの定義を容易にします。ツールは、プロンプトが大規模言語モデル（LLM）に渡される前にプロンプト調整が必要な場合に役立つと説明されています。

これらの変更により、文書の正確性が向上し、ユーザーがAzure AI Studioのプロンプトツールを効果的に活用できるように情報が強化されています。

## articles/ai-studio/how-to/prompt-flow-tools/python-tool.md{#item-c9200f}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ author: lgayhardt
 
 # Python tool for flows in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 The prompt flow Python tool offers customized code snippets as self-contained executable nodes. You can quickly create Python tools, edit code, and verify results.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI StudioのPythonツールに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI StudioのPythonツールに関連する文書が変更されています。主な変更点は以下のとおりです：

1. **インクルードタグのパス修正**: 文書内で使用されている`Feature preview`に関連するインクルードタグのパスが変更され、正確なパスである`../../includes/feature-preview.md`に更新されました。この修正により、機能プレビューに関する情報が正しく参照され、信頼性が向上します。

2. **Pythonツールの機能説明の強化**: 更新された部分では、プロンプトフローのPythonツールが提供する機能について詳述されています。このツールは、自己完結型の実行可能ノードとしてカスタマイズされたコードスニペットを提供し、ユーザーがPythonツールを迅速に作成、コードを編集し、結果を検証できることが説明されています。

これらの変更により、文書がより正確になり、ユーザーがAzure AI StudioのPythonツールを効果的に活用できるようにするための情報が強化されています。

## articles/ai-studio/how-to/prompt-flow-tools/rerank-tool.md{#item-dd52bf}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 The prompt flow Rerank tool improves search quality of relevant documents given a query for retrieval-augment generation (RAG) in prompt flow. This tool works best with [Index Look up tool](index-lookup-tool.md) as a ranker after the initial retrieval.
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 ## Use the Rerank tool
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioの再ランキングツールに関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Studioの再ランキングツールに関する文書を更新しています。主な変更点は次のとおりです：

1. **インクルードタグのパス修正**: 文書内にある`Feature preview`に関連するインクルードタグのパスが修正され、正しいパスである`../../includes/feature-preview.md`に更新されました。この変更により、機能プレビューの情報が正確に参照され、文書の整合性が向上します。

2. **再ランキングツールの機能説明の明確化**: 修正後のセクションでは、プロンプトフローの再ランキングツールがクエリに基づいて関連文書の検索品質を向上させることが詳述されています。このツールは、初期の検索結果の後にランカーとして使用され、[Index Look up tool](index-lookup-tool.md)との組み合わせで最適な結果を提供します。

これらの変更により、文書がより正確になり、ユーザーがAzure AI Studioの再ランキングツールを効果的に利用できるように情報が強化されています。

## articles/ai-studio/how-to/prompt-flow-tools/serp-api-tool.md{#item-144ed7}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Serp API tool for flows in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../../includes/feature-preview.md)]
 
 The prompt flow Serp API tool provides a wrapper to the [Serp API Google Search Engine Results API](https://serpapi.com/search-api) and [Serp API Bing Search Engine Results API](https://serpapi.com/bing-search-api).
 
@@ -28,7 +28,7 @@ Sign up on the [Serp API home page](https://serpapi.com/).
 
 To create a Serp connection:
 
-1. Sign in to [Azure AI Studio](https://studio.azureml.net/).
+1. Sign in to [Azure AI Studio](https://ai.azure.com/).
 1. Go to **Project settings** > **Connections**.
 1. Select **+ New connection**.
 1. Add the following custom keys to the connection:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI StudioのSERP APIツールに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI StudioのSERP APIツールに関連する文書が変更されています。主な変更点は以下のとおりです：

1. **インクルードタグのパス修正**: `Feature preview`に関連するインクルードタグのパスが更新され、正しいパスである`../../includes/feature-preview.md`に修正されました。これにより、機能プレビューに関する情報が正確に参照され、より信頼性のある文書となります。

2. **Azure AI Studioのサインインリンク更新**: ユーザーがSerp接続を作成するための手順において、「Azure AI Studio」のサインインリンクが`https://studio.azureml.net/`から`https://ai.azure.com/`に変更されました。この更新は、最新のプラットフォームへのアクセスを保証します。

これらの変更により、文書が更新され、Azure AI StudioのSERP APIツールを使用する際の指示が明確かつ正確になり、ユーザーの利便性が向上します。

## articles/ai-studio/how-to/prompt-flow.md{#item-9fdb4a}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: lgayhardt
 
 # Prompt flow in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Prompt flow is a development tool designed to streamline the entire development cycle of AI applications powered by Large Language Models (LLMs). Prompt flow provides a comprehensive solution that simplifies the process of prototyping, experimenting, iterating, and deploying your AI applications.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのプロンプトフローに関する文書の更新"
}
```

### Explanation
この更新は、Azure AI Studioのプロンプトフローに関連する文書の修正です。主な内容は以下の通りです：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`に関連するインクルードタグのパスが修正され、`../includes/feature-preview.md`という正しいパスが使用されています。この修正により、機能プレビューの情報が適切に参照され、ユーザーに対して有用な情報が提供されるようになります。

2. **プロンプトフローの説明の保持**: プロンプトフロー自体についての説明は変更されていませんが、文書全体がより正確で信頼性の高い情報を提供するものとなっています。プロンプトフローは、大規模言語モデル（LLM）を活用したAIアプリケーションの開発サイクルを効率化するためのツールであり、プロトタイピング、実験、反復、デプロイメントの過程を簡素化する包括的なソリューションを提供します。

これらの変更によって、文書が最新の状態になり、ユーザーがAzure AI Studioのプロンプトフローを利用する際の理解が深まることが期待されます。

## articles/ai-studio/how-to/prompt-shields.md{#item-ed4acd}

<details>
<summary>Diff</summary>
````diff
@@ -12,7 +12,7 @@ ms.author: pafarley
 ---
 
 # Prompt Shields (preview)
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Learn how to use Azure AI Content Safety Prompt Shields to check large language model (LLM) inputs for both User Prompt attacks and Document attacks.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのプロンプトシールドに関する文書の更新"
}
```

### Explanation
この修正では、Azure AI Studioのプロンプトシールドに関連する文書が更新されています。主な変更は以下の通りです：

1. **インクルードタグのパス修正**: 文書内で使用されている`Feature preview`に関連するインクルードタグのパスが修正され、`../includes/feature-preview.md`が正しいパスとして指定されています。この変更により、機能プレビューに関する情報が正確に参照され、ユーザーにとってさらに役立つ情報がアクセス可能になります。

2. **プロンプトシールドの説明の保持**: プロンプトシールドに関する基本的な説明は変更されていません。Azure AIコンテンツセーフティプロンプトシールドが、ユーザープロンプト攻撃やドキュメント攻撃に対する大規模言語モデル（LLM）入力を検査する方法について説明されています。

これにより、文書が更新され、ユーザーがAzure AI Studioのプロンプトシールド機能を効果的に利用するための情報が強化されています。ユーザーは、最新の機能や安全対策を適切に理解し、実施できるようになります。

## articles/ai-studio/how-to/quota.md{#item-39c866}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: Blackmist
 
 # Manage and increase quotas for resources with Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Quota provides the flexibility to actively manage the allocation of rate limits across the deployments within your subscription. This article walks through the process of managing quota for your Azure AI Studio virtual machines and Azure OpenAI models.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのクォータ管理に関する文書の更新"
}
```

### Explanation
この変更は、Azure AI Studioにおけるリソースのクォータ管理に関する文書の更新です。以下のポイントが主な変更内容です：

1. **インクルードタグのパス修正**: 文書内の`Feature preview`に関連するインクルードタグのパスが修正され、`../includes/feature-preview.md`という正しいパスが指定されています。この修正により、ユーザーが機能プレビューの情報に正しくアクセスできるようになり、より正確な情報が提供されます。

2. **クォータ管理に関する説明の保持**: クォータ管理の説明部分は変更されていません。クォータ機能は、サブスクリプション内のデプロイメントに対するレート制限の割り当てを効果的に管理する柔軟性を提供し、Azure AI Studioの仮想マシンおよびAzure OpenAIモデルのクォータ管理プロセスについて解説されています。

これらの変更は、文書が最新の状態に保たれることを目的としており、ユーザーがAzure AI Studioのリソース管理をより理解し、活用できるようにするための情報を強化しています。

## articles/ai-studio/how-to/troubleshoot-deploy-and-monitor.md{#item-6b0de7}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,7 @@ author: msakande
 
 # How to troubleshoot your deployments and monitors in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 This article provides instructions on how to troubleshoot your deployments and monitors in Azure AI Studio. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioのデプロイおよびモニターのトラブルシューティングに関する文書の更新"
}
```

### Explanation
この修正は、Azure AI Studioにおけるデプロイおよびモニターのトラブルシューティングに関する文書の更新です。具体的な変更点は以下の通りです：

1. **インクルードタグのパス修正**: 文書内で用いられている`Feature preview`のインクルードタグのパスが修正され、`../includes/feature-preview.md`という正しいパスが指定されています。これにより、機能プレビューに関する最新の情報が正しく参照され、ユーザーに役立つ情報が提供されます。

2. **トラブルシューティングの内容は維持**: デプロイメントとモニターのトラブルシューティングに関する説明は変更されていません。この記事では、Azure AI Studioでのデプロイメントやモニターの問題を解決するための手順が説明されています。

これらの変更により、文書が最新の情報に基づいて常に更新され、ユーザーがAzure AI Studioを効果的に使用できるよう繰り返しサポートされることを目的としています。

## articles/ai-studio/how-to/troubleshoot-secure-connection-project.md{#item-32d5c4}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: Blackmist
 
 # Troubleshoot connection to a project with a private endpoint
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 When connecting to a project that has been configured with a private endpoint, you may encounter a 403 or a messaging saying that access is forbidden. Use the information in this article to check for common configuration problems that can cause this error.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートエンドポイントを使用したプロジェクトへの接続トラブルシューティングに関する文書の更新"
}
```

### Explanation
この変更は、プライベートエンドポイントを使用したプロジェクトへの接続に関するトラブルシューティングの文書を更新したものです。具体的には以下の変更点があります：

1. **インクルードタグのパス修正**: 文書内に記載されている`Feature preview`のインクルードタグのパスが変更され、`../includes/feature-preview.md`という正しいパスに修正されています。これによって、ユーザーは最新の機能プレビューに関する情報に正確にアクセスできるようになります。

2. **内容の維持**: プライベートエンドポイントに設定されたプロジェクトへの接続時に発生する403エラーやアクセス拒否メッセージに関する説明は変更がありません。この記事は、これらのエラーを引き起こす一般的な設定上の問題を確認するための情報を提供しています。

これらの変更により、文書が最新の状態に保たれ、ユーザーがAzure AI Studioを使用してプロジェクトへの接続のトラブルシューティングを効果的に行えるようサポートしています。

## articles/ai-studio/includes/feature-preview.md{#item-931f1e}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,13 @@
+---
+title: include file
+description: include file
+author: msakande
+ms.author: mopeakande
+ms.service: azure-ai-studio
+ms.topic: include
+ms.date: 10/10/2024
+ms.custom: include file
+---
+
+> [!IMPORTANT]
+> Items marked (preview) in this article are currently in public preview. This preview is provided without a service-level agreement, and we don't recommend it for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "機能プレビューに関するインクルードファイルの追加"
}
```

### Explanation
この変更は、機能プレビューに関する新しいインクルードファイルを追加したものです。具体的な内容は以下の通りです：

1. **新しいインクルードファイルの作成**: `feature-preview.md`という新しいファイルが作成され、Azure AI Studioにおける機能プレビューに関連する情報が含まれています。このファイルは、特定の機能がパブリックプレビューとして利用可能であることを示しています。

2. **重要な注意事項の追加**: ドキュメント内には、プレビュー版の機能についての重要な注意事項が含まれており、これらの項目はサービスレベル契約がなく、プロダクションワークロードには推奨されないことが明記されています。また、特定の機能がサポートされていない場合や制約がある場合があることも強調されています。

3. **メタ情報の追加**: ファイルには、タイトル、説明、著者、サービス、トピック、日付、カスタム情報といったメタデータが含まれています。これにより、ドキュメントがより整理され、利用者が情報を見つけやすくなります。

この新しいインクルードファイルは、Azure AI Studioのユーザーに対して機能プレビューに関する情報を提供し、これらの機能を試す際の注意点を明確にすることを目的としています。

## articles/ai-studio/includes/models-preview.md{#item-d2bea2}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,13 @@
+---
+title: include file
+description: include file
+author: msakande
+ms.author: mopeakande
+ms.service: azure-ai-studio
+ms.topic: include
+ms.date: 10/10/2024
+ms.custom: include file
+---
+
+> [!IMPORTANT]
+> Models that are in preview are marked as _preview_ on their model cards in the model catalog.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "モデルプレビューに関するインクルードファイルの追加"
}
```

### Explanation
この変更は、モデルプレビューに関する新しいインクルードファイルを追加したものです。具体的な内容は以下の通りです：

1. **新しいインクルードファイルの作成**: `models-preview.md`というファイルが新たに作成され、Azure AI Studioのモデルカタログにおけるプレビューモデルに関する情報が含まれています。

2. **重要な注意事項の追加**: ドキュメント内には、プレビュー中のモデルについての重要な情報が記載されており、プレビューモデルはそのモデルカードに「_preview_」と表示されることが明記されています。これにより、ユーザーはどのモデルが現在プレビュー状態にあるかを簡単に識別できるようになります。

3. **メタ情報の追加**: このファイルには、タイトル、説明、著者、サービス、トピック、日付、カスタム情報といったメタデータが含まれており、ドキュメントの内容が明確に整理されています。

この新しいインクルードファイルは、Azure AI Studioのユーザーに対してプレビューモデルに関する重要な情報を提供し、利用者がモデル選定時に役立てることを目的としています。

## articles/ai-studio/quickstarts/content-safety.md{#item-bdaebf}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: PatrickFarley
 
 # QuickStart: Moderate text and images with content safety in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this quickstart, you use the [Azure AI Content Safety](/azure/ai-services/content-safety/overview) service in Azure AI Studio to moderate text and images. Content Safety detects harmful user-generated and AI-generated content in applications and services. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツ安全性クイックスタートのインクルードファイルパスの修正"
}
```

### Explanation
この変更は、`content-safety.md`というドキュメント内でのインクルードファイルのパスを修正したものです。具体的には、以下の内容が含まれています。

1. **インクルードファイルのパス変更**: 元々のパス「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」から、「`../includes/feature-preview.md`」に変更されました。この修正により、インクルードファイルへの参照が正確になり、ドキュメントの安定性が向上します。

2. **変更の影響**: この修正は主にリンクの構造に関わるものであり、コンテンツそのものには直接的な変更はありません。しかし、インクルードファイルのパスを更新することで、ドキュメントが正しい情報を参照できるようになり、ユーザーが受け取る情報の正確性が保証されます。

このアップデートは、ドキュメントのメンテナンスと改善に寄与しており、Azure AI Studioのユーザーが内容をスムーズに確認できるようにします。

## articles/ai-studio/quickstarts/get-started-code.md{#item-8a5082}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ author: sdgilley
 
 # Build a custom chat app in Python using the prompt flow SDK
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this quickstart, we walk you through setting up your local development environment with the prompt flow SDK. We write a prompt, run it as part of your app code, trace the LLM calls being made, and run a basic evaluation on the outputs of the LLM.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムチャットアプリのクイックスタートのインクルードファイルパスの修正"
}
```

### Explanation
この変更は、`get-started-code.md`というドキュメント内でのインクルードファイルのパスを修正したものです。具体的には、次の内容が述べられています。

1. **インクルードファイルのパス変更**: 元のパス「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」が、「`../includes/feature-preview.md`」に変更されました。この更新により、インクルードファイルへの正確なリンクが確保され、ドキュメントの整合性が向上します。

2. **変更の影響**: この修正は主にリンクの構成に関するもので、コンテンツ自体には変更がありませんが、インクルードファイルの正確な参照が行えるようになるため、ユーザーに提供される情報の正確性と可用性が改善されます。

この更新は、Azure AI Studioのクイックスタートガイドをより使いやすくし、開発者がプロンプトフローSDKを用いたカスタムチャットアプリの構築に集中できるようにすることを目的としています。

## articles/ai-studio/quickstarts/get-started-playground.md{#item-e4d7fb}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: sdgilley
 
 # Quickstart: Create a project and use the chat playground in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this [Azure AI Studio](https://ai.azure.com) quickstart, you create a project, deploy a chat model, and use it in the chat playground in Azure AI Studio.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットプレイグラウンドのクイックスタートのインクルードファイルパスの修正"
}
```

### Explanation
この変更は、`get-started-playground.md`というドキュメント内でのインクルードファイルのパスを修正したものです。具体的な内容は次の通りです。

1. **インクルードファイルのパス変更**: 元々のインクルードファイルパス「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」が、「`../includes/feature-preview.md`」に変更されました。この更新により、ファイルへの参照が正確になり、ドキュメント内での情報の整合性が向上します。

2. **変更の影響**: この修正はリンクの構成に関わるものであり、ドキュメントの主要な内容には直接的な変更はありません。ただし、インクルードファイルへの正確な参照を持つことで、ユーザーにとっての利便性が増し、正しい情報が提供されます。

このアップデートは、Azure AI Studioのクイックスタートガイドの品質向上に寄与しており、ユーザーがプロジェクトを作成し、チャットモデルをデプロイしてチャットプレイグラウンドで利用する際の手助けになります。

## articles/ai-studio/quickstarts/hear-speak-playground.md{#item-3167bc}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: eric-urban
 
 # Quickstart: Hear and speak with chat models in the AI Studio chat playground
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Give your app the ability to hear and speak by pairing Azure OpenAI Service with Azure AI Speech to enable richer interactions.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットプレイグラウンドの音声機能クイックスタートのインクルードファイルパスの修正"
}
```

### Explanation
この変更は、`hear-speak-playground.md`というドキュメント内でのインクルードファイルのパスを修正したものです。具体的には以下の内容が含まれています。

1. **インクルードファイルのパス変更**: 元のパス「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」が新しいパス「`../includes/feature-preview.md`」に変更されました。この変更により、インクルードファイルへのアクセスがより確実になり、情報の整合性が向上します。

2. **変更の影響**: この修正はリンク構成に関するもので、ドキュメントの内容そのものには直接の変更はありませんが、ユーザーが正確な情報にアクセスできるようになります。これにより、Azure OpenAI ServiceとAzure AI Speechを組み合わせて、アプリに音声機能を追加する際のガイドとしての役割が強化されます。

このアップデートは、ユーザーにとって一層良好な体験を提供し、AI Studioでの音声によるインタラクションを簡単に実現することを目的としています。

## articles/ai-studio/quickstarts/multimodal-vision.md{#item-740e84}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ author: PatrickFarley
 
 # Quickstart: Get started using GPT-4 Turbo with Vision on your images and videos in Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Use this article to get started using [Azure AI Studio](https://ai.azure.com) to deploy and test the GPT-4 Turbo with Vision model. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチモーダルビジョンのクイックスタートのインクルードファイルパスの修正"
}
```

### Explanation
この変更は、`multimodal-vision.md`というドキュメント内でのインクルードファイルのパスを修正したものです。具体的な内容は以下の通りです。

1. **インクルードファイルのパス変更**: 元のパス「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」が新しいパス「`../includes/feature-preview.md`」に変更されました。この変更により、正しいファイルへの参照が確保され、情報の整合性が改善されます。

2. **変更の影響**: この修正はドキュメントの主要な内容に直接影響を与えるものではありませんが、インクルードファイルへの正確なリンクを提供することで、ユーザーはより容易に関連情報にアクセスできます。このドキュメントは、ユーザーがAzure AI StudioにおいてGPT-4 Turboをビジョンモデルとともに利用し始めるためのガイドとなります。

このアップデートは、新しい機能の導入に際して、ユーザーが適切な情報を得られるよう促進する役割を果たしています。

## articles/ai-studio/reference/reference-model-inference-api.md{#item-9fe240}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.custom:
 
 # Azure AI Model Inference API | Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 The Azure AI Model Inference is an API that exposes a common set of capabilities for foundational models and that can be used by developers to consume predictions from a diverse set of models in a uniform and consistent way. Developers can talk with different models deployed in Azure AI Studio without changing the underlying code they are using.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル推論APIのリファレンスのインクルードファイルパスの修正"
}
```

### Explanation
この変更は、`reference-model-inference-api.md`というドキュメントにおけるインクルードファイルのパスを修正したものです。具体的には以下の点が重要です。

1. **インクルードファイルのパス変更**: 元のパス「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」が新しいパス「`../includes/feature-preview.md`」に変更されました。この変更により、インクルードファイルへのアクセスが精度を持ち、関連情報に容易に到達できるようになります。

2. **変更の影響**: この修正は、ユーザーがAzure AI Studioにおけるモデル推論APIを理解し、利用するための情報の正確性を向上させるものです。具体的には、開発者がさまざまなモデルから予測を一貫して取得できるようにし、コードの変更なしに異なるモデルとやり取りできる能力を維持しつつ、正しい文書を参照できることを促進します。

このアップデートは、ユーザーに対して一貫した情報アクセスを提供し、Azure AI Studioの利用体験を向上させることを目的としています。

## articles/ai-studio/reference/reference-model-inference-chat-completions.md{#item-e09823}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.custom:
 
 # Reference: Chat Completions | Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Creates a model response for the given chat conversation.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットコンプリーションのモデル推論リファレンスのインクルードファイルパスの修正"
}
```

### Explanation
この変更は、`reference-model-inference-chat-completions.md`というドキュメントにおけるインクルードファイルのパスを修正したものです。主な内容は以下の通りです。

1. **インクルードファイルのパス変更**: 元のパス「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」が新しいパス「`../includes/feature-preview.md`」に変更されています。このアップデートにより、関連するインクルードファイルへのアクセスが容易になり、文書の整合性が向上します。

2. **変更の影響**: 修正されたパスは、ユーザーがAzure AI Studioにおけるチャットコンプリーションのモデル推論機能に関する情報にアクセスする際の利便性を高めます。この機能は、与えられたチャット会話に対するモデルの応答を生成するために使用されるため、正確な情報を参照できることが重要です。

この変更は、ユーザーに対して正確な文書を提供し、Azure AI Studioの機能をより効果的に活用できるようにすることを目的としています。

## articles/ai-studio/reference/reference-model-inference-completions.md{#item-bae39d}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.custom:
 
 # Reference: Completions | Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Creates a completion for the provided prompt and parameters.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンプリーションのモデル推論リファレンスのインクルードファイルパスの修正"
}
```

### Explanation
この変更は、`reference-model-inference-completions.md`におけるインクルードファイルのパスを修正したものです。具体的には以下の内容が含まれています。

1. **インクルードファイルのパス変更**: インクルードされているファイルのパスが「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」から「`../includes/feature-preview.md`」に変更されました。この修正により、正しいパスへのアクセスが確保され、文書の整合性が向上します。

2. **変更の影響**: このパスの修正は、Azure AI Studioにおけるコンプリーションのモデル推論機能に関する情報を提供する際の利便性を高めます。この機能は、提供されたプロンプトとパラメータに基づいてコンプリーションを生成するものであり、ユーザーが正確な情報に容易にアクセスできることが重要です。

この変更は、Azure AI Studioの機能を利用する際のユーザーエクスペリエンスを向上させることを目的としています。

## articles/ai-studio/reference/reference-model-inference-embeddings.md{#item-5e9064}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.custom:
 
 # Reference: Embeddings | Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Creates an embedding vector representing the input text.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンベディングのモデル推論リファレンスのインクルードファイルパスの修正"
}
```

### Explanation
この変更は、`reference-model-inference-embeddings.md`というドキュメントにおけるインクルードファイルのパスを修正したものです。以下のポイントが含まれています。

1. **インクルードファイルのパス変更**: 元のパス「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」が新しいパス「`../includes/feature-preview.md`」に変更されています。この更新により、関連するインクルードファイルへのアクセスが改善され、文書の整合性が向上します。

2. **変更の影響**: 修正されたパスは、Azure AI Studioにおけるエンベディング機能に関する情報を提供する際の便利さを高めます。この機能の目的は、入力テキストを表すエンベディングベクトルを生成することであり、正確な情報が素早く取得できることが重要です。

この変更は、ユーザーがエンベディング機能をより効果的に利用できるように文書を改善することを目指しています。

## articles/ai-studio/reference/reference-model-inference-images-embeddings.md{#item-70c7ac}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.custom:
 
 # Reference: Image Embeddings | Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Creates an embedding vector representing the input image and text pair.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像エンベディングのモデル推論リファレンスのインクルードファイルパスの修正"
}
```

### Explanation
この変更は、`reference-model-inference-images-embeddings.md`というドキュメントの中で、インクルードファイルのパスを修正したものです。詳細は以下の通りです。

1. **インクルードファイルのパス変更**: 変更前のパス「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」が新しいパス「`../includes/feature-preview.md`」に修正されました。この更新により、正しいファイルへのアクセスが確保され、文書の整合性が向上します。

2. **変更の影響**: この修正によって、Azure AI Studioにおける画像とテキストペアを表すエンベディングベクトルを生成する機能に関する情報が、より分かりやすくなることが期待されます。ユーザーが必要な情報に迅速にアクセスできることは、機能を効果的に使用する上で非常に重要です。

この変更は、画像エンベディング機能に関するリファレンス文書を改善し、ユーザーエクスペリエンスを向上させることを目的としています。

## articles/ai-studio/reference/reference-model-inference-info.md{#item-e465b4}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ ms.custom:
 
 # Reference: Info | Azure AI Studio
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Returns the information about the model deployed under the endpoint.
 
@@ -85,7 +85,7 @@ Status code: 200
 ```json
 {
   "model_name": "phi3-mini",
-  "model_type": "chat_completion",
+  "model_type": "chat-completions",
   "model_provider_name": "Microsoft"
 }
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル推論情報リファレンスのファイルパスとモデルタイプの修正"
}
```

### Explanation
この変更は、`reference-model-inference-info.md`というドキュメントに対して行われたもので、以下の点が修正されています。

1. **インクルードファイルのパス変更**: インクルード文が修正され、以前のパス「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」から新しいパス「`../includes/feature-preview.md`」に更新されました。この変更により、関連情報へのアクセスが向上し、文書の品質が改善されます。

2. **モデルタイプの名称変更**: モデル情報に関するJSONレスポンスの中で、`"model_type"`の値が「`chat_completion`」から「`chat-completions`」に変更されました。この修正は、用語の一貫性を保つためと、正確な機能を反映させるためのものです。

この変更により、Azure AI Studioのモデル推論に関する情報がより明確になり、ユーザーが必要な情報を簡単に理解できるようになります。

## articles/ai-studio/reference/region-support.md{#item-d402e1}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,7 @@ ms.custom: references_regions, build-2024
 
 # Azure AI Studio feature availability across clouds regions
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 Azure AI Studio brings together various Azure AI capabilities that previously were only available as standalone Azure services. While we strive to make all features available in all regions where Azure AI Studio is supported at the same time, feature availability may vary by region. In this article, you'll learn what Azure AI Studio features are available across cloud regions.  
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リージョンサポートに関するリファレンスのインクルードパスの修正"
}
```

### Explanation
この変更は、`region-support.md`というドキュメントに対するもので、以下のポイントが修正されています。

1. **インクルードファイルのパス変更**: 以前のインクルード文「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」が、新しいパス「`../includes/feature-preview.md`」に更新されました。この変更により、関連情報へのアクセスが容易になり、ドキュメントの一貫性が向上します。

2. **文書の内容強化**: 修正されたファイル内で、Azure AI Studioの機能がどのように異なるクラウドリージョンで利用可能であるかに関する情報が説明されています。特に、この文書はAzure AI Studioの機能がどのように統合されているか、各リージョンでの利用状況に関してユーザーに重要な情報を提供することを目的としています。

この修正により、ユーザーはAzure AI Studioの機能に関する正確で最新の情報にアクセスできるようになり、より良い理解を深めることが期待されます。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -12,6 +12,8 @@ items:
     href: reference/region-support.md
   - name: Azure AI FAQ
     href: faq.yml
+  - name: What is Azure OpenAI?
+    href: ../ai-services/openai/overview.md?context=/azure/ai-studio/context/context
   - name: "AI Studio or Azure Machine Learning studio: Which should I choose?"
     href: /ai/ai-studio-experiences-overview?context=/azure/ai-studio/context/context
 - name: Quickstarts
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "TOCにAzure OpenAIに関するセクションを追加"
}
```

### Explanation
この変更は、`toc.yml`という目次ファイルに対するもので、以下の点が追加されています。

1. **新しいセクションの追加**: 新たに「What is Azure OpenAI?」という項目が追加され、関連するドキュメントへのリンクも設定されています。具体的には、`href`として「`../ai-services/openai/overview.md?context=/azure/ai-studio/context/context`」が指定されています。この追加により、ユーザーはAzure OpenAIに関する情報を簡単に見つけることができるようになります。

2. **文書構成の強化**: この変更により、Azure AI Studioの文書がより包括的になり、ユーザーがAIサービスに関する情報を探求する際の利便性が向上します。新しいセクションは、Azure OpenAIがどのようにAI Studioと関連しているかを理解する助けとなります。

このような修正は、ユーザーエクスペリエンスを向上させ、Azure AIに関連する情報のナビゲーションを容易にすることを目的としています。

## articles/ai-studio/tutorials/deploy-chat-web-app.md{#item-987845}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,7 @@ author: aahill
 
 # Tutorial: Deploy an Enterprise Chat web app
 
-[!INCLUDE [Feature preview](~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md)]
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you deploy an enterprise chat web app that uses your own data with a large language model in AI Studio.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットWebアプリのデプロイに関するチュートリアルのインクルードパスの修正"
}
```

### Explanation
この変更は、`deploy-chat-web-app.md`というチュートリアル文書に対するもので、以下の点が修正されています。

1. **インクルード文のパス変更**: チュートリアル内のインクルード文が修正されており、以前のパス「`~/reusable-content/ce-skilling/azure/includes/ai-studio/includes/feature-preview.md`」が、新しいパス「`../includes/feature-preview.md`」に更新されました。この変更により、関連コンテンツへのリンクが正しく機能するようになり、ユーザーが必要な情報を容易に見つけることができるようになります。

2. **文書の整合性向上**: インクルードパスの修正は、ドキュメント全体の整合性を保ち、ユーザーがチュートリアルを通じて一貫した体験を得られるようにするための重要な更新です。

この修正により、ユーザーはAI Studioを使用したエンタープライズチャットWebアプリのデプロイ方法を学ぶための正確でアクセスしやすい情報に頼ることができ、チュートリアルの価値が向上します。


