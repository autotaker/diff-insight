---
date: '2025-04-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0b31bb0...MicrosoftDocs:6c8ccfa
summary: このコード差分は、Azure AIに関連するドキュメントの手順や表現を修正し、情報の明確さと可読性を向上させるためのマイナーアップデートです。新機能や重大な変更はなく、軽微な修正が行われています。具体的には、手順の順序の数値表記の訂正や表現の簡略化が施され、「アシスタントのロジックアプリに関する手順」や「RBACに関する手順」、そして「データスタジオ接続手順」において一貫性が強化されています。これにより、ユーザーが理解しやすいガイドが提供され、全体的なユーザーエクスペリエンスが向上することを目的としています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:0b31bb0...MicrosoftDocs:6c8ccfa){target="_blank"}

# ハイライト
このコード差分は、Azure AIに関連するドキュメントの手順や表現を修正し、情報の明確さと可読性を向上させることを目的としたマイナーアップデートです。

## 新機能
該当なし。この更新では新機能の追加は行われていません。

## 重大な変更
該当なし。すべての変更は既存のコンテンツに対する軽微な修正に留まっています。

## その他の更新
- 「アシスタントのロジックアプリに関する手順」では、手順の順序の数値表記を訂正し、文言を少し簡略化しました。
- 「RBACに関する手順」では、「左のナビゲーションペイン」という表現を「左のペイン」に簡略化しました。
- 「データスタジオ接続手順」でも同様に文言を「左のペイン」に統一しました。

# 洞察
このコード差分は、Azure AI関連のドキュメントにおける一連の軽微な修正を示しています。特に、手順の文言の簡略化や、視覚的に読みやすいガイダンスをユーザーに提供することを目的とした修正が目立ちます。

例えば、「アシスタントのロジックアプリに関する手順」や「RBACに関する手順」では、ユーザーがドキュメントを読み解くときに混乱を生じさせる可能性のある冗長な言い回しが見直されています。手順の数値表記の訂正も、誤解を避け、正確な指示をユーザーに伝えるための重要な修正です。

また、「データスタジオ接続手順」では、統一感のある表現が採用されることで、ドキュメント全体を通じた一貫性が強化されています。このような文言の修正は、初心者からプロユーザーまで、誰にとっても理解しやすいガイドを提供する基本となります。

これらの修正は、すでに確立された機能セットの使用をテキストレベルでサポートし、ユーザーエクスペリエンス全体を改善するためのものであると理解できます。このようなマイナーな改良を積み重ねることにより、全体的に信頼できるドキュメントが提供され続けることとなります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assistants-logic-apps.md](#item-57ae37) | minor update | アシスタントのロジックアプリに関する手順の修正 | modified | 1 | 1 | 2 | 
| [role-based-access-control.md](#item-4b9817) | minor update | RBACに関する手順の表現を更新 | modified | 1 | 1 | 2 | 
| [connect-your-data-studio.md](#item-c34da8) | minor update | データスタジオ接続手順の表現を修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/how-to/assistants-logic-apps.md{#item-57ae37}

<details>
<summary>Diff</summary>
````diff
@@ -89,7 +89,7 @@ Here are the steps to create a new Logic Apps workflow for function calling.
 
 Here are the steps to import your Logic Apps workflows as function in the Assistants playground in Azure AI Foundry:
 
-1. In Azure AI Foundry, select **Playgrounds** from the left navigation menu, and then **Assistants playground**. Select an existing Assistant or create a new one. After you have configured the assistant with a name and instructions, you are ready to add a function. Select **+ Add function**. 
+1. In Azure AI Foundry, select **Playgrounds** from the left pane, and then **Assistants playground**. Select an existing Assistant or create a new one. After you have configured the assistant with a name and instructions, you are ready to add a function. Select **+ Add function**. 
 
     :::image type="content" source="..\media\how-to\assistants\logic-apps\assistants-playground-add-function.png" alt-text="A screenshot showing the Assistant playground with the add function button." lightbox="..\media\how-to\assistants\logic-apps\assistants-playground-add-function.png":::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アシスタントのロジックアプリに関する手順の修正"
}
```

### Explanation
このコードの変更は、ドキュメント内の手順の一部で、ロジックアプリのワークフローを作成するための手順の数値表記を変更しています。具体的には、手順の先頭にある「-1.」が「+1.」に変更されました。この変更は、内容に実質的な影響を与えないものであり、情報の明確さを向上させることを目的としています。また、左のナビゲーションメニューからの表現が「左のペイン」に簡略化されました。このドキュメントは、Azure AI Foundryでのアシスタントの設定および機能追加に関する指示を提供しています。

## articles/ai-services/openai/how-to/role-based-access-control.md{#item-4b9817}

<details>
<summary>Diff</summary>
````diff
@@ -23,7 +23,7 @@ Azure RBAC can be assigned to an Azure OpenAI resource. To grant access to an Az
    > [!NOTE]
    > You can also set up Azure RBAC for whole resource groups, subscriptions, or management groups. Do this by selecting the desired scope level and then navigating to the desired item. For example, selecting **Resource groups** and then navigating to a specific resource group.
 
-1. Select **Access control (IAM)** on the left navigation pane.
+1. Select **Access control (IAM)** on the left pane.
 1. Select **Add**, then select **Add role assignment**.
 1. On the **Role** tab on the next screen, select a role you want to add.
 1. On the **Members** tab, select a user, group, service principal, or managed identity.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "RBACに関する手順の表現を更新"
}
```

### Explanation
このコードの変更は、Azure RBAC（ロールベースのアクセス制御）に関連する手順の表現を若干修正したものです。具体的には、「左のナビゲーションペイン」という表現が「左のペイン」に簡略化されました。この変更は、手順をより簡潔にし、ユーザーにとって分かりやすくすることを目的としています。手順の残りの部分は変更されておらず、Azure OpenAIリソースへのアクセスを付与するための一連のステップを示しています。この修正は、ドキュメントの可読性を向上させるためのもので、ユーザーが操作を進めやすくなっています。

## articles/ai-services/openai/includes/connect-your-data-studio.md{#item-c34da8}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ Navigate to [Azure AI Foundry portal](https://ai.azure.com/) and sign-in with cr
 
     :::image type="content" source="../media/use-your-data/ai-foundry-homepage.png" alt-text="A screenshot of the Azure AI Foundry portal landing page." lightbox="../media/use-your-data/ai-foundry-homepage.png":::
 
-1. Select **Chat** under **Playgrounds** in the left navigation menu, and select your model deployment.
+1. Select **Chat** under **Playgrounds** in the left pane, and select your model deployment.
 
 1. In the **Chat playground**, Select **Add your data** and then **Add a data source**
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データスタジオ接続手順の表現を修正"
}
```

### Explanation
このコードの変更は、データスタジオとの接続手順に関する文言の一部を修正したものです。具体的には、「左のナビゲーションメニュー」という表現が「左のペイン」に変更されています。この変更により、手順がより明確で一貫性のあるものとなり、ユーザーがAzure AI Foundryポータルを操作する際に理解しやすくなっています。この手順には、Azure AI Foundryにサインインしてからのモデルデプロイメントの選択方法が含まれています。全体として、この変更はドキュメントの可読性を向上させる目的で行われました。


