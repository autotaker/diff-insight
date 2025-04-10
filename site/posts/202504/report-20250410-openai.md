---
date: '2025-04-10'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:24b31df...MicrosoftDocs:a9279bd
summary: このコードの変更は、AIサービスのモデルアップグレードとAzure OpenAIサービスのクォータおよび制限に関する情報の強化を含む一連のマイナーな更新を反映しています。新機能として、地域別クォータ能力制限に関する新しい情報とAIモデルアップグレードに関する注意点が追加され、Spring
  Bootアプリケーションのサンプルコードや依存関係も更新されています。また、`gpt-4`のVision-previewバージョンのアップグレードに伴い、一部の機能が無効化されることが警告されています。最終的に、これらの更新により、Azure
  OpenAIサービスの利用者はリソースの管理を効率化し、開発体験を向上させることができるようになるでしょう。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:24b31df...MicrosoftDocs:a9279bd){target="_blank"}

# ハイライト
このコードの変更は、AIサービスのモデルアップグレード、およびAzure OpenAIサービスのクォータと制限に関する情報を充実させ、Spring Bootアプリケーションの更新を含む一連のマイナーな更新を反映しています。

## 新機能
- 地域別クォータキャパシティ制限に関する新しい情報の追加
- AIサービスのモデルアップグレードに関する新しい注意点の追加
- Spring Bootアプリケーションのサンプルコードや依存関係のアップデート

## 破壊的変更
- `gpt-4` の Vision-previewバージョンのアップグレードによる、Vision enhancements preview 機能の無効化が警告されています。

## その他の更新
- 地域別クォータ制限に関するリンクの修正により、アクセス性を向上

# インサイト
このコードベースの変更は、Azure OpenAIサービスの利用者にとって、非常に現実的な影響をもたらす更新が含まれています。まず、地域別に設定されたクォータ制限に関する詳細が追加されたことで、リソースをより効率的に管理するための新たな手段が提供されました。これにより、個々の組織が自身の使用状況に応じて、リソースの利用を最適化できるようになります。

AIモデルアップグレードに関する注意点の追加は、特に地域によるタイムラグを考慮せずに実施されるアップグレードについて、利用者が事前に計画を立てるための重要な情報を提供しています。また、`gpt-4` Vision-previewの機能がアップグレードによって無効化される点は、今後の開発において考慮が必要な重要な情報です。

Spring Bootアプリケーションの更新は、AI機能を統合し利用する開発者にとって、最新のSpringフレームワークと整合性を保つための必須の変更です。依存関係のアップデートやサンプルコードの改善によって、開発者はよりスムーズな開発体験を享受できるでしょう。

全体として、これらの更新はAzure OpenAIサービスを使用するユーザーが、より効率的にサービスを活用し、技術的な課題に対処できるための準備をサポートするものとなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | モデルのアップグレードに関する情報の追加 | modified | 5 | 0 | 5 | 
| [chatgpt-spring.md](#item-114b66) | minor update | Spring Boot アプリケーションの依存関係とサンプルコードの更新 | modified | 93 | 100 | 193 | 
| [quotas-limits.md](#item-06c6f9) | minor update | 地域別のクォータキャパシティ制限に関する新しい情報の追加 | modified | 39 | 2 | 41 | 
| [whats-new.md](#item-53303b) | minor update | 地域別クォータ制限に関するリンクの修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -118,6 +118,11 @@ These models are currently available for use in Azure OpenAI Service.
 
  **<sup>1</sup>** We'll notify all customers with these preview deployments at least 30 days before the start of the upgrades. We'll publish an upgrade schedule detailing the order of regions and model versions that we'll follow during the upgrades, and link to that schedule from here.
 
+> [!TIP]
+> **Will a model upgrade happen if the new model version is not yet available in that region?**
+>
+> Yes, even in cases where the latest model version is not yet available in a region, we will automatically upgrade deployments during the scheduled upgrade window. For more information, see [Azure OpenAI model versions](/azure/ai-services/openai/concepts/model-versions#will-a-model-upgrade-happen-if-the-new-model-version-is-not-yet-available-in-that-region).
+
 > [!IMPORTANT]
 > Vision enhancements preview features including Optical Character Recognition (OCR), object grounding, video prompts will be retired and no longer available once `gpt-4` Version: `vision-preview` is upgraded to `turbo-2024-04-09`. If you're currently relying on any of these preview features, this automatic model upgrade will be a breaking change.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルのアップグレードに関する情報の追加"
}
```

### Explanation
この変更では、AI サービスにおけるモデルのアップグレードに関する注意点が追記されました。具体的には、以下の2つの重要な情報が追加されています。 

1. 新しいモデルバージョンが特定の地域でまだ利用できない場合でも、予定されたアップグレードのウィンドウ中に、自動的にデプロイメントがアップグレードされることが確認されています。このことに関する詳細は「Azure OpenAI モデルバージョン」にリンクされて説明されています。

2. Vision enhancements preview 機能（光学文字認識やオブジェクトグラウンディング、動画プロンプトを含む）は、`gpt-4` の Vision-preview バージョンが `turbo-2024-04-09` にアップグレードされると利用できなくなることが強調されています。この自動モデルアップグレードは、現在これらのプレビューフィーチャーに依存している場合には、破壊的変更を引き起こす可能性があると警告されています。

これにより、ユーザーはアップグレードの影響を理解し、予め対応策を考えた上で準備するための情報を得ることができます。

## articles/ai-services/openai/includes/chatgpt-spring.md{#item-114b66}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.author: mbullwin
 ms.date: 11/27/2023
 ---
 
-[Source code](https://github.com/spring-projects-experimental/spring-ai) | [Artifacts (Maven)](https://repo.spring.io/ui/native/snapshot/org/springframework/experimental/ai/spring-ai-openai-spring-boot-starter/0.7.0-SNAPSHOT) | [Sample](https://github.com/rd-1-2022/ai-azure-openai-prompt-roles)
+[Source code](https://github.com/spring-projects/spring-ai) | [Artifacts (Maven)](https://repo.spring.io/ui/native/snapshot/org/springframework/experimental/ai/spring-ai-openai-spring-boot-starter/0.7.0-SNAPSHOT) | [Sample](https://github.com/Azure-Samples/spring-ai-samples/tree/main/ai-chat-demo)
 
 ## Prerequisites
 
@@ -75,56 +75,68 @@ ai-chat-demo/
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
-       xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
-       <modelVersion>4.0.0</modelVersion>
-       <parent>
-           <groupId>org.springframework.boot</groupId>
-           <artifactId>spring-boot-starter-parent</artifactId>
-           <version>3.2.0</version>
-           <relativePath/> <!-- lookup parent from repository -->
-       </parent>
-       <groupId>com.example</groupId>
-       <artifactId>ai-chat-demo</artifactId>
-       <version>0.0.1-SNAPSHOT</version>
-       <name>AIChat</name>
-       <description>Demo project for Spring Boot</description>
-       <properties>
-           <java.version>17</java.version>
-       </properties>
-       <dependencies>
-           <dependency>
+         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
+      <modelVersion>4.0.0</modelVersion>
+      <parent>
+         <groupId>org.springframework.boot</groupId>
+         <artifactId>spring-boot-starter-parent</artifactId>
+         <version>3.3.4</version>
+         <relativePath/> <!-- lookup parent from repository -->
+      </parent>
+      <groupId>com.example</groupId>
+      <artifactId>ai-chat-demo</artifactId>
+      <version>0.0.1-SNAPSHOT</version>
+      <name>AIChat</name>
+      <description>Demo project for Spring Boot</description>
+      <properties>
+         <java.version>17</java.version>
+         <spring-ai.version>1.0.0-M5</spring-ai.version>
+      </properties>
+      <dependencies>
+         <dependency>
+            <groupId>org.springframework.boot</groupId>
+            <artifactId>spring-boot-starter</artifactId>
+         </dependency>
+         <dependency>
+            <groupId>org.springframework.ai</groupId>
+            <artifactId>spring-ai-azure-openai-spring-boot-starter</artifactId>
+         </dependency>
+         <dependency>
+            <groupId>org.springframework.boot</groupId>
+            <artifactId>spring-boot-starter-test</artifactId>
+            <scope>test</scope>
+         </dependency>
+      </dependencies>
+      <dependencyManagement>
+         <dependencies>
+            <dependency>
+               <groupId>org.springframework.ai</groupId>
+               <artifactId>spring-ai-bom</artifactId>
+               <version>${spring-ai.version}</version>
+               <type>pom</type>
+               <scope>import</scope>
+            </dependency>
+         </dependencies>
+      </dependencyManagement>
+      <build>
+         <plugins>
+            <plugin>
                <groupId>org.springframework.boot</groupId>
-               <artifactId>spring-boot-starter</artifactId>
-           </dependency>
-           <dependency>
-               <groupId>org.springframework.experimental.ai</groupId>
-               <artifactId>spring-ai-azure-openai-spring-boot-starter</artifactId>
-               <version>0.7.0-SNAPSHOT</version>
-           </dependency>
-           <dependency>
-               <groupId>org.springframework.boot</groupId>
-               <artifactId>spring-boot-starter-test</artifactId>
-               <scope>test</scope>
-           </dependency>
-       </dependencies>
-       <build>
-           <plugins>
-               <plugin>
-                   <groupId>org.springframework.boot</groupId>
-                   <artifactId>spring-boot-maven-plugin</artifactId>
-               </plugin>
-           </plugins>
-       </build>
-       <repositories>
-           <repository>
-               <id>spring-snapshots</id>
-               <name>Spring Snapshots</name>
-               <url>https://repo.spring.io/snapshot</url>
-               <releases>
-                   <enabled>false</enabled>
-               </releases>
-           </repository>
-       </repositories>
+               <artifactId>spring-boot-maven-plugin</artifactId>
+            </plugin>
+         </plugins>
+      </build>
+      <repositories>
+         <repository>
+            <id>spring-milestones</id>
+            <name>Spring Milestones</name>
+            <url>https://repo.spring.io/milestone</url>
+            <snapshots>
+               <enabled>false</enabled>
+            </snapshots>
+         </repository>
+      </repositories>
+
    </project>
    ```
 
@@ -133,55 +145,36 @@ ai-chat-demo/
    ```java
    package com.example.aichatdemo;
 
-   import java.util.ArrayList;
-   import java.util.List;
-
-   import org.springframework.ai.client.AiClient;
-   import org.springframework.ai.prompt.Prompt;
-   import org.springframework.ai.prompt.messages.ChatMessage;
-   import org.springframework.ai.prompt.messages.Message;
-   import org.springframework.ai.prompt.messages.MessageType;
-   import org.springframework.beans.factory.annotation.Autowired;
+   import org.slf4j.Logger;
+   import org.slf4j.LoggerFactory;
+   import org.springframework.ai.chat.client.ChatClient;
    import org.springframework.boot.CommandLineRunner;
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
+   import org.springframework.context.annotation.Bean;
 
    @SpringBootApplication
-   public class AiChatApplication implements CommandLineRunner
-   {
-       private static final String ROLE_INFO_KEY = "role";
-
-       @Autowired
-       private AiClient aiClient;
-
-       public static void main(String[] args) {
-           SpringApplication.run(AiChatApplication.class, args);
-       }
-
-       @Override
-       public void run(String... args) throws Exception
-       {
-           System.out.println(String.format("Sending chat prompts to AI service. One moment please...\r\n"));
-
-           final List<Message> msgs = new ArrayList<>();
-
-           msgs.add(new ChatMessage(MessageType.SYSTEM, "You are a helpful assistant"));
-           msgs.add(new ChatMessage(MessageType.USER, "Does Azure OpenAI support customer managed keys?"));
-           msgs.add(new ChatMessage(MessageType.ASSISTANT, "Yes, customer managed keys are supported by Azure OpenAI?"));
-           msgs.add(new ChatMessage(MessageType.USER, "Do other Azure AI services support this too?"));
-
-           final var resps = aiClient.generate(new Prompt(msgs));
-
-           System.out.println(String.format("Prompt created %d generated response(s).", resps.getGenerations().size()));
-
-           resps.getGenerations().stream()
-             .forEach(gen -> {
-                 final var role = gen.getInfo().getOrDefault(ROLE_INFO_KEY, MessageType.ASSISTANT.getValue());
-
-                 System.out.println(String.format("Generated respose from \"%s\": %s", role, gen.getText()));
-             });
-       }
-
+   public class AiChatApplication {
+
+      private static final Logger log = LoggerFactory.getLogger(AiChatApplication.class);
+
+      public static void main(String[] args) {
+         SpringApplication.run(AiChatApplication.class, args);
+      }
+
+      @Bean
+      CommandLineRunner commandLineRunner(ChatClient.Builder builder) {
+         return args -> {
+            var chatClient = builder.build();
+            log.info("Sending chat prompts to AI service. One moment please...");
+            String response = chatClient.prompt()
+                  .user("What was Microsoft's original internal codename for the project that eventually became Azure?")
+                  .call()
+                  .content();
+
+            log.info("Response: {}", response);
+         };
+      }
    }
    ```
 
@@ -203,14 +196,14 @@ ai-chat-demo/
  \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
   '  |____| .__|_| |_|_| |_\__, | / / / /
  =========|_|==============|___/=/_/_/_/
- :: Spring Boot ::                (v3.1.5)
 
-2023-11-07T13:31:10.884-06:00  INFO 6248 --- [           main] c.example.aichatdemo.AiChatApplication   : No active profile set, falling back to 1 default profile: "default"
-2023-11-07T13:31:11.595-06:00  INFO 6248 --- [           main] c.example.aichatdemo.AiChatApplication   : Started AiChatApplication in 0.994 seconds (process running for 1.28)
-Sending chat prompts to AI service. One moment please...
+ :: Spring Boot ::                (v3.3.4)
 
-Prompt created 1 generated response(s).
-Generated respose from "assistant": Yes, other Azure AI services also support customer managed keys. Azure AI Services, Azure Machine Learning, and other AI services in Azure provide options for customers to manage and control their encryption keys. This allows customers to have greater control over their data and security.
+2025-03-14T13:35:30.145-04:00  INFO 93252 --- [AIChat] [           main] c.example.aichatdemo.AiChatApplication   : Starting AiChatApplication using Java 23.0.2 with PID 93252 (/Users/vega/dev/msft/spring-ai-samples/ai-chat-demo/target/classes started by vega in /Users/vega/dev/msft/spring-ai-samples/ai-chat-demo)
+2025-03-14T13:35:30.146-04:00  INFO 93252 --- [AIChat] [           main] c.example.aichatdemo.AiChatApplication   : No active profile set, falling back to 1 default profile: "default"
+2025-03-14T13:35:30.500-04:00  INFO 93252 --- [AIChat] [           main] c.example.aichatdemo.AiChatApplication   : Started AiChatApplication in 0.445 seconds (process running for 0.633)
+2025-03-14T13:35:30.501-04:00  INFO 93252 --- [AIChat] [           main] c.example.aichatdemo.AiChatApplication   : Sending chat prompts to AI service. One moment please...
+2025-03-14T13:35:31.950-04:00  INFO 93252 --- [AIChat] [           main] c.example.aichatdemo.AiChatApplication   : Response: Microsoft's original internal codename for the project that eventually became Azure was "Project Red Dog." This initiative ultimately led to the development and launch of the Microsoft Azure cloud computing platform.
 ```
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Spring Boot アプリケーションの依存関係とサンプルコードの更新"
}
```

### Explanation
この変更は、Spring Boot アプリケーションに関する情報を大幅に更新したものです。具体的には、以下の内容が含まれています。

1. **依存関係の変更**: `spring-boot-starter-parent` のバージョンが `3.2.0` から `3.3.4` にアップグレードされ、`spring-ai` フレームワークのバージョンも `1.0.0-M5`として新たに追加されました。

2. **サンプルコードの修正**: コードの構造が修正され、より最新のクライアント API を反映する形で、`AiClient` から `ChatClient` への変更が行われました。また、コマンドラインから AI へのプロンプト送信方法が改善され、コードの可読性が向上しています。

3. **サンプルの参照先**: GitHub リポジトリのリンクが更新されました。元のリンクが `spring-projects-experimental/spring-ai` から `spring-projects/spring-ai` に変更され、サンプルが見やすくなるように改良されています。 

これらの変更により、ユーザーは最新の機能を活用でき、開発者体験が向上するようになっています。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -55,8 +55,6 @@ The following sections provide you with a quick guide to the default quotas and
 
 <sup>1</sup> Our current APIs allow up to 10 custom headers, which are passed through the pipeline, and returned. Some customers now exceed this header count resulting in HTTP 431 errors. There's no solution for this error, other than to reduce header volume. **In future API versions we will no longer pass through custom headers**. We recommend customers not depend on custom headers in future system architectures.
 
-## Regional quota limits
-
 > [!NOTE]
 > Quota limits are subject to change. 
 
@@ -274,6 +272,45 @@ Quota increase requests can be submitted via the [quota increase request form](h
 
 For other rate limits, [submit a service request](../cognitive-services-support-options.md?context=/azure/ai-services/openai/context/context).
 
+## Regional quota capacity limits
+
+You can view quota availability by region for your subscription in the [Azure AI Foundry portal](https://ai.azure.com/resource/quota).
+
+Alternatively to view quota capacity by region for a specific model/version you can query the [capacity API](/rest/api/aiservices/accountmanagement/model-capacities/list) for your subscription. Provide a `subscriptionId`, `model_name`, and `model_version` and the API will return the available capacity for that model across all regions, and deployment types for your subscription.
+
+> [!NOTE]
+> Currently both the Azure AI Foundry portal and the capacity API will return quota/capacity information for models that are [retired](./concepts/model-retirements.md) and no longer available.
+
+[API Reference](/rest/api/aiservices/accountmanagement/model-capacities/list)
+
+```python
+import requests
+import json
+from azure.identity import DefaultAzureCredential
+
+subscriptionId = "Replace with your subscription ID" #replace with your subscription ID
+model_name = "gpt-4o"     # Example value, replace with model name
+model_version = "2024-08-06"   # Example value, replace with model version
+
+token_credential = DefaultAzureCredential()
+token = token_credential.get_token('https://management.azure.com/.default')
+headers = {'Authorization': 'Bearer ' + token.token}
+
+url = f"https://management.azure.com/subscriptions/{subscriptionId}/providers/Microsoft.CognitiveServices/modelCapacities"
+params = {
+    "api-version": "2024-06-01-preview",
+    "modelFormat": "OpenAI",
+    "modelName": model_name,
+    "modelVersion": model_version
+}
+
+response = requests.get(url, params=params, headers=headers)
+model_capacity = response.json()
+
+print(json.dumps(model_capacity, indent=2))
+
+```
+
 ## Next steps
 
 Explore how to [manage quota](./how-to/quota.md) for your Azure OpenAI deployments.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域別のクォータキャパシティ制限に関する新しい情報の追加"
}
```

### Explanation
この変更では、Azure OpenAI サービスにおけるクォータおよび制限に関する情報を更新し、地域別のクォータキャパシティ制限に関する新しいセクションを追加しました。具体的な更新内容は以下の通りです。

1. **地域別クォータキャパシティ制限の追加**: ユーザーはAzure AI Foundry ポータルで、サブスクリプションごとの地域別クォータの可用性を確認できることが説明されています。また、特定のモデルやバージョンに対するクォータ容量を確認するための新しいAPI（capacity API）へのアクセス方法も紹介されています。

2. **API参照の提供**: capacity API を使用するための具体的なエンドポイントが提示され、必要なパラメータ（`subscriptionId`、`model_name`、`model_version`）を使って、モデルの可用容量を取得する方法が示されています。

3. **サンプルコードの追加**: Python での API 呼び出しの具体例が追加されており、Azure 認証を使用してモデルのキャパシティ情報を取得する手順が詳細に説明されています。このサンプルは、ユーザーが新機能を迅速に利用できるよう設計されています。

これにより、ユーザーは自分のサブスクリプションのクォータ状況をより良く把握し、効率的にリソースを管理できるようになります。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -771,7 +771,7 @@ Azure OpenAI Service now supports speech to text APIs powered by OpenAI's Whispe
 
 ### Regional quota limits increases
 
-- Increases to the max default quota limits for certain models and regions. Migrating workloads to [these models and regions](./quotas-limits.md#regional-quota-limits) will allow you to take advantage of higher Tokens per minute (TPM).  
+- Increases to the max default quota limits for certain models and regions. Migrating workloads to [these models and regions](./quotas-limits.md) will allow you to take advantage of higher Tokens per minute (TPM).  
 
 ## August 2023
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "地域別クォータ制限に関するリンクの修正"
}
```

### Explanation
この変更は、Azure OpenAI サービスに関する「新機能」セクションの内容を更新したもので、具体的には地域別クォータ制限に関連するリンクを修正しました。以下に詳細を説明します。

1. **リンクの修正**: 元の文章では、地域別クォータ制限に関する追加情報を提供するためのリンクが `quotas-limits.md#regional-quota-limits` という特定のセクションへのリンクになっていましたが、変更後は `quotas-limits.md` というファイル全体へのリンクに修正されました。これにより、利用者はクォータに関する情報をより幅広く参照できるようになります。

2. **文章全体の構造は保持**: 変更があったのはリンクの部分のみで、文章の内容や他の情報はそのまま維持されています。新しいリンクが追加されたことで、情報のアクセス性が向上しています。

このように、修正されたリンクはユーザーが必要な情報により簡単にアクセスできるように配慮された内容です。


